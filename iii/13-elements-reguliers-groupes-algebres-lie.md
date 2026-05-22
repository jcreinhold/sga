# Exposé XIII. Regular elements of algebraic groups and Lie algebras

<!-- label: III.XIII -->

*by A. Grothendieck*

## 1. An auxiliary lemma on varieties with operators

<!-- label: III.XIII.1 -->

<!-- original page 249 -->

Let $S$ be a prescheme, $G$ an $S$-prescheme in groups acting on the left on an $S$-prescheme $V$, $W$ a closed
$S$-subprescheme of $V$, $N$ its stabilizer in $G$ — the subgroup of $G$ whose points, with values in an $S'$ over $S$,
are the $g \in G(S')$ such that $g \cdot W_{S'} = W_{S'}$. We endow $(Sch)/S$ with the faithfully flat quasi-compact
topology, and identify $G$, $V$, $W$ with the corresponding sheaves (cf. IV). We shall therefore argue in the category
of sheaves on $(Sch)/S$, and in this section the term "locally" refers to the topology we have just specified on
$(Sch)/S$. Note that $N$ is a sheaf; consider the quotient sheaf $G/N$. One sees at once that it is isomorphic to the
following functor: to every $S'$ over $S$, one associates the set of subsheaves $W'$ of $V_{S'}$ that are locally
conjugate to $W_{S'}$ by the group $G$. Let $X$ be the subsheaf of $G/N \times_{S} V$ whose value, for every $S'$ over
$S$, is the set of pairs $(W', v)$, where $W'$ is as above and $v$ is a section of $W'$ over $S'$ (hence a section of
$V_{S'}$ over $S'$). Let $Z$ be the inverse image of $X$ in $G \times_{S} V$, so that we have the cartesian diagram

```text
              Z  ─────────→  X
              │              │
        (✱)   │              │ i
              ↓              ↓
           G ×_S V ─→ G/N ×_S V,
```

<!-- label: eq:III.XIII.1.star -->

where $i$ is the canonical immersion, and the second horizontal arrow comes from the canonical morphism $G \to G/N$.

<!-- original page 250 --> Since this morphism sends the point `g ∈ G(S′)` to the subsheaf `g · W_{S′}` of `V_{S′}`, one

sees that $Z(S')$ is the set of pairs $(g, v) \in G(S') \times V(S')$ such that $v \in g \cdot W_{S'}(S')$.
Consequently, $Z$ is isomorphic to the sheaf $G \times_{S} W$, by means of the isomorphism

```text
G ×_S W ─⥲→ Z
```

defined by $(g, w) \mapsto (g, g \cdot w)$. Thus the preceding cartesian diagram gives the cartesian diagram

```text
                 q
              G ×_S W ─────→  X
                │              │
       (✱✱)    λ│              │ i
                ↓              ↓
              G ×_S V ─→ G/N ×_S V
```

<!-- label: eq:III.XIII.1.doublestar -->

where $\lambda(g, w) = (g, g \cdot w)$, hence $q(g, w) = (\bar{g}, g \cdot w)$, where `ḡ` denotes the image of $g$ under
the canonical map $G(S') \to (G/N)(S')$. One sees finally from diagram `(✱)` that $Z \to X$ makes $Z$ into a principal
bundle with base $X$ and group $N$ acting on the right by $(g, v) \cdot n = (gn, v)$, so that in `(✱✱)`,
$q : G \times_{S} W \to X$ makes $G \times_{S} W$ into a principal bundle with base $X$ and group $N$ acting on the
right by

```text
(g, w) · n = (gn, n⁻¹ · w).
```

We summarize the principal morphisms above in the following diagram:

```text
                       G ×_S W
                      ╱       ╲
                     q         ϕ
                    ╱           ╲
                   ↓             ↘
        G/N ←── p─ X ──ψ──→ V
                   │
                pr₁│  i↓    ↗pr₂
                   ↓
              G/N ×_S V
(D)
```

<!-- label: eq:III.XIII.1.D -->

where $\psi = pr_{2} \circ i$ and $\varphi = \psi \circ q$, i.e. $\varphi(g, w) = g \cdot w$. If $v$ is a section of $V$
over $S$, the subsheaf $X_{v}$ of $X$, inverse image of this section by $\psi$, is given by <!-- original page 251 -->
$X_{v}(S') =$ set of subsheaves $W'$ of $V_{S'}$ which are locally conjugate to $W_{S'}$ by $G$ and which contain the
section $v_{S'}$ of $V_{S'}$, while the subsheaf of $G \times_{S} W$ inverse image of $v$ by $\varphi$ is isomorphic to
the subsheaf $M_{v}$ of $G$ given by $M_{v}(S') =$ set of $g \in G(S')$ such that $v_{S'} \in g \cdot W(S')$, i.e. such
that $g^{-1} v_{S'} \in W(S')$. If $v$ is a section of $W$ and not merely of $V$, then $M_{v}$ evidently contains $N$.

In these explicit descriptions we have not used the fact that $G$, $V$, $W$ are representable (nor that the site over
which we work is defined in terms of preschemes!). But suppose now that $N$ is representable and faithfully flat and
quasi-compact over $S$, and that $G/N$ is representable. When $S$ is the spectrum of a field, and $G$ is of finite type
over $k$, one knows that this hypothesis is necessarily satisfied (VIII 6 and VI_B.11.18). One then sees from the
cartesian diagram `(✱✱)`, using the theory of faithfully flat quasi-compact descent and the fact that
$Z \to G \times_{S} V$ is a closed immersion, that $X$ is representable (it is obtained by descent of the closed
subprescheme $Z$ of $G \times_{S} V$ by the faithfully flat quasi-compact morphism
$G \times_{S} V \to G/N \times_{S} V$). Hence diagram `(D)` is a diagram of morphisms of preschemes over $S$.

We henceforth assume that $S$ is the spectrum of a field $k$, and that $G$, $V$, $W$ are of finite type over $k$. Let
$\mathfrak{n}$ be the Lie algebra of $N$, so that $\dim N \leqslant rank \mathfrak{n}$, with equality if and only if $N$
is smooth over $k$ (Exp VI [^N.D.E-XIII-1]). Let $a \in W(k)$, and consider the subscheme $M_{a}$ of $G$ defined above,
containing $N$, and isomorphic to $\varphi^{-1}(a)$; we shall denote by $\mathfrak{m}_{a}$ its Zariski tangent space at
the identity element $e$ of $N$, so that one has

```text
(1)    𝔫 ⊂ 𝔪_a,    dim N ⩽ rank 𝔫 ⩽ rank 𝔪_a.
```

<!-- label: eq:III.XIII.1.1 -->

**Lemma 1.1.** *With the preceding notation:*

<!-- label: III.XIII.1.1 -->

<!-- original page 252 -->

*a) Consider the following conditions:*

- *(i) $\mathfrak{n} = \mathfrak{m}_{a}$ and $N$ is smooth over $k$.*
- *(i bis) $\dim N = rank_{k} \mathfrak{m}_{a}$.*
- *(ii) The morphism $\psi : X \to V$ is unramified at $(\bar{e}, a)$.*
- *(iii) $M_{a}$ and $N$ coincide in a neighborhood of $e$.*

*Then one has the implications (i) ⇔ (i bis) ⇒ (ii) ⇔ (iii).*

*b) Suppose $\varphi : G \times_{S} W \to V$ is smooth at $(e, a)$. Then $M_{a}$ is smooth over $k$ at $e$, and $\psi$
is smooth at $(\bar{e}, a)$.*

*Proof.* a) The equivalence of (i) and (i bis) follows at once from the relations (1) and from the fact already noted
that $N$ is smooth over $k$ if and only if $\dim N = rank_{k} \mathfrak{n}$. On the other hand, consider the inclusion
morphism $N \to M_{a}$; it is well known [^N.D.E-XIII-2] that if $N$ is smooth over $k$ at $e$ and the tangent map at
$e$ is surjective, then $N \to M_{a}$ is smooth at $e$, hence (being an immersion) is an isomorphism at $e$, which shows
that (i) implies (iii). To prove the equivalence of (ii) and (iii), consider as above $X_{a} = \psi^{-1}(a)$ and use the
isomorphism $M_{a} \simeq \varphi^{-1}(a) \simeq q^{-1}(X_{a})$ to obtain a morphism $p_{a} : M_{a} \to X_{a}$ which
makes $M_{a}$ a principal homogeneous bundle with group $N_{X_{a}}$. Consider the following diagram

```text
                  j_a
       M_a  ←──────────── N
        │                  │
      p_a│                 │
        ↓        j_a′      ↓
       X_a  ←──────  S = Spec(k),
```

where $\operatorname{Spec}(k) \to X_{a}$ is defined by the point $(\bar{e}, a)$ of $X$, and $j_{a} : N \to M_{a}$ is the canonical immersion. To say
that $\psi$ is unramified at $(\bar{e}, a)$ means that $j_{a}'$ is an open immersion, or equivalently that it induces an
isomorphism $S \xrightarrow{\sim} \operatorname{Spec}(\mathcal{O}_{X_{a}, \bar{a}})$. <!-- original page 253 --> Since $p_{a}$ is flat, it is equivalent to say that the
morphism deduced from the preceding by the base change $\operatorname{Spec}(\mathcal{O}_{M_{a}, e}) \to \operatorname{Spec}(\mathcal{O}_{X_{a}, \bar{a}})$ is an isomorphism; now this
deduced morphism is none other than the morphism $\operatorname{Spec}(\mathcal{O}_{N, e}) \to \operatorname{Spec}(\mathcal{O}_{M_{a}, e})$, which proves the equivalence of
(ii) and (iii).

One will note moreover that the proof shows that conditions (ii), (iii) imply the following condition, apparently
stronger than (iii):

- (iii bis) *$N$ is an open and closed subscheme of $M_{a}$.*

b) The first assertion follows from the fact that $M_{a}$ is isomorphic to $\varphi^{-1}(a)$, the second from the fact
that $q$ is flat and $q(e, a) = (\bar{e}, a)$.

## 2. Density theorem and theory of the regular points of G

<!-- label: III.XIII.2 -->

We shall apply the constructions and notation of the preceding section to the case where $G$ is a connected smooth
algebraic group over $k$, where $V = G$ on which $G$ acts by inner automorphisms, and where $W$ is a connected smooth
algebraic subgroup $H$ of $G$. We shall denote by $\mathfrak{g}$ the Lie algebra of $G$, by $\mathfrak{h}$ that of $H$,
by $N$ the normalizer of $H$ in $G$, and by $\mathfrak{n}$ the Lie algebra of $N$. If $a \in G(k)$, we shall denote, as
in section 1, by $M_{a}$ the symmetric of its transporter into $H$, so that if $a \in H(k)$, one has $N \subset M_{a}$;
in this case, we denote by $\mathfrak{m}_{a}$ the Zariski tangent space of $M_{a}$ at the identity element $e$ of $G$.
Note that

```text
𝔥 ⊂ 𝔫 ⊂ 𝔪_a    for a ∈ H(k).
```

We shall need the following:

<!-- original page 254 -->

**Lemma 2.0.** *In order that $H = N^{0}$, it is necessary and sufficient that $(\mathfrak{g}/\mathfrak{h})^{H} = 0$
(where the first member denotes the subspace of invariants under the action of $H$ deduced from the adjoint
representation). When this condition is satisfied, $N$ is smooth and $\dim X = \dim G$. In any case,
$\dim X \leqslant \dim G$, and this inequality is an equality if and only if $H$ is of finite index in $N$.*

<!-- label: III.XIII.2.0 -->

Indeed, one has seen (II 5.2.3 (i)) that $\mathfrak{n}$ equals the inverse image of $(\mathfrak{g}/\mathfrak{h})^{H}$
under the morphism $\mathfrak{g} \to \mathfrak{g}/\mathfrak{h}$, hence $(\mathfrak{g}/\mathfrak{h})^{H} = 0$ is
equivalent to $\mathfrak{h} = \mathfrak{n}$, which is also equivalent (since $H$ is a smooth connected algebraic
subgroup of the algebraic group $N$) to $H = N^{0}$ (cf. VI.2). This evidently implies that $N$ is smooth. On the other
hand, one has

```text
dim X = (dim G − dim N) + dim H = dim G − (dim N − dim H),
```

hence

```text
dim X ⩽ dim G,
```

with equality if and only if $\dim H = \dim N$, i.e. if and only if $H$ is of finite index in $N$. This is the case in
particular if $H = N^{0}$, which completes the proof of 2.0.

**Theorem 2.1.** *Let $G$ be a smooth connected algebraic group over the algebraically closed field $k$, $H$ a connected
smooth algebraic subgroup, $N$ its normalizer, $\mathfrak{g}$, $\mathfrak{h}$, $\mathfrak{n}$ the Lie algebras,
$X = G \times^{N} H$ the scheme (fibered over $G/N$ with typical fiber $H$) introduced in section 1, $\psi : X \to G$
the canonical morphism (whose image is also the image of $\varphi : G \times H \to G$ defined by
$\varphi(g, h) = int(g)h = ghg^{-1}$). The following conditions are all equivalent:*

<!-- label: III.XIII.2.1 -->

- *(i) $H$ contains a Cartan subgroup (XII 1) $C$ of $G$.*
- *(i bis) $H$ has the same reductive rank and the same nilpotent rank (XII 1) as $G$.*
- *(ii) $H$ contains a maximal torus $T$ of $G$, and $(\mathfrak{g}/\mathfrak{h})^{T} = 0$.*

<!-- original page 255 -->

- *(iii) The set of conjugates of $H$ containing a given maximal torus is finite and non-empty, and $H$ is of finite
  index in its normalizer.*
- *(iv) There exists $a \in H(k)$ contained only in finitely many conjugates of $H$ (or merely such that $\psi^{-1}(a)$
  has an isolated point), and $H$ is of finite index in its normalizer.*
- *(iv bis) The morphism $\psi : X \to G$ is generically quasi-finite (i.e. there exists a dense open of $X$ on which
  $\psi$ is quasi-finite), and $H$ is of finite index in its normalizer.*
- *(v) There exists a dense open $U$ in $G$ such that for every $x \in U(k)$, the set of conjugates of $H$ containing
  $x$ is finite and non-empty, i.e. $\psi : X \to G$ is dominant and generically quasi-finite.*
- *(vi) There exists a dense open $U$ of $G$ such that every $x \in U(k)$ is contained in a conjugate of $H$, i.e.
  $\psi : X \to G$ is dominant.*
- *(vii) There exists $a \in H(k)$ such that the subspace of $\mathfrak{g}/\mathfrak{h}$ of fixed points of
  $ad_{\mathfrak{g}/\mathfrak{h}}(a)$ is zero.*

*Furthermore, these conditions imply that $H$ is its own connected normalizer, i.e. $N$ is smooth and $\dim H = \dim N$,
and that $\psi : X \to G$ is generically étale.*

*Proof.* By 2.0, one has $\dim X \leqslant \dim G$, with equality if and only if $\dim H = \dim N$, i.e. $H$ of finite
index in $N$. From the inequality $\dim X \leqslant \dim G$ it follows that $\psi$ is dominant if and only if it is
dominant and generically quasi-finite, or again if and only if $\psi$ is generically quasi-finite and $\dim X = \dim G$.
As this latter equality means also, by 2.0, that $H$ is of finite index in $N$, we have proved the equivalence of (vi),
(v), (iv bis). The equivalence of (iv) and (iv bis) is immediate.

The equivalence of (i) and (i bis) is immediate from the definitions, and is left to the reader. On the other hand, if
$H$ contains a Cartan subgroup $C$ of $G$, then it contains the maximal torus $T$ of $C$, which is a maximal torus of
$G$. <!-- original page 256 --> Since $C$ is the centralizer of $T$, its Lie algebra $\mathfrak{c}$ is given by

$$
\mathfrak{c} = \mathfrak{g}^{T}
$$

(II, 5.2.3 (ii)). Hence as $H \supset C$, so that $\mathfrak{h} \supset \mathfrak{c}$, it follows that
$\mathfrak{c} \subset \mathfrak{g}^{T}$, which is equivalent (by I, 4.7.3) to the relation

```text
(✱)    (𝔤/𝔥)^T = 0.
```

Conversely, suppose that $H$ contains the maximal torus $T$ and that the preceding relation holds, i.e. that
$\mathfrak{h} \supset \mathfrak{c}$; I claim that $H$ contains the centralizer $C$ of $T$ (which will establish (i) ⇔
(ii)). This follows from the:

**Lemma 2.1.1.** *Let $G$ be a smooth algebraic group over the field $k$, $T$ a subgroup of multiplicative type of $G$,
$C$ its connected centralizer (equal to the centralizer of $T$ if $G$ is connected and $T$ is a torus, (XII 6.6 b))),
$H$ a smooth subgroup of $G$ containing $T$. In order that $H$ contain $C$, it is necessary and sufficient that its Lie
algebra $\mathfrak{h}$ contain that $\mathfrak{c}$ of $C$.*

<!-- label: III.XIII.2.1.1 -->

Indeed, one knows (XI 2.4) that $Centr_{G}(T)$ is smooth over $k$, hence $C$ is smooth over $k$; similarly
$Centr_{H}(T)$ is smooth over $k$, and $Centr_{H}(T) = Centr_{G}(T) \cap H$ has $\mathfrak{h} \cap \mathfrak{c}$ as Lie
algebra; hence the hypothesis implies that the smooth subgroup $Centr_{H}(T)$ of the smooth group $Centr_{G}(T)$ has the
same Lie algebra, so it contains the connected component $C$ of the latter, and thus $H$ contains $C$. *QED*.

Let us prove the equivalence of (i) and (iii), which amounts to proving that if $H$ contains the maximal torus $T$ of
$G$, then the condition $H \supset C$ (which is also equivalent to `(✱)` above, as we have just seen) is equivalent to
the fact that $H$ is of finite index in its normalizer <!-- original page 257 --> and that the set of conjugates of $H$
containing $T$ is finite. If $H$ contains $C$, hence if one has `(✱)`, then a fortiori

```text
(✱✱)   (𝔤/𝔥)^H = 0,
```

and we know that $\mathfrak{n}$ is the inverse image of the first member of the preceding relation under the canonical
homomorphism $\mathfrak{g} \to \mathfrak{g}/\mathfrak{h}$ (II 5.2.3 (i)), so that the preceding relation means, by 2.0,
that $H = N^{0}$, and a fortiori $H$ is of finite index in its normalizer. Now consider the diagram of subgroups

```text
   T  ───→  N(T) ∩ H  ───→  H
              │              │
              ↓              ↓
       N(T) ∩ N(H)  ───→  N(H)
              │
              ↓
            N(T).
```

Using the theorem of conjugacy of maximal tori in $H$ (XII 6.6 a)), one sees that every conjugate of $H$ containing $T$
is a conjugate of $H$ by an element of $N(T)(k)$, so the set of conjugates of $H$ containing $T$ is in bijective
correspondence with the set of points of $N(T)/N(T) \cap N(H)$ with values in $k$; but as $H \supset C$, one has
$N(T) \cap H \supset C$, hence the preceding set is a quotient of $(N(T)/C)(k)$, which is a finite set, hence is finite.
This proves (i) ⇒ (iii). Conversely, suppose (iii), i.e. $N(T)/N(T) \cap N(H)$ finite and $N(H)/H$ finite. Using again
the conjugacy theorem in $H$, one sees again that the homomorphism

```text
N(T) ∩ N(H)/N(T) ∩ H ─→ N(H)/H
```

induced by the preceding diagram is bijective on points with values in $k$ (in fact, it is an isomorphism), hence as the
latter is finite, so is the former, so $N(T) \cap H$ is of finite index in $N(T)$, hence contains $C = N(T)^{0}$, hence
$H \supset C$. Thus (i), (i bis), (ii), (iii) are equivalent conditions.

<!-- original page 258 -->

Let us prove that (ii) ⇒ (vii). One sees at once that conditions (ii) and (vii) are each invariant under an extension
$k \to k'$ of the base field, with $k'$ algebraically closed, which allows us to assume that $k$ has infinite
transcendence degree over its prime subfield. Then it is well known (and easily verified) that there exists an element
$a$ of $T(k)$ such that the subgroup of $T(k)$ it generates is dense in $T$ for the Zariski topology. One easily
concludes that $(\mathfrak{g}/\mathfrak{h})^{T} = (\mathfrak{g}/\mathfrak{h})^{ad(a)}$, and as the first member is zero
by hypothesis, one concludes (vii).

Let us prove (vii) ⇒ (vi). This implication is contained in the following result, which sharpens 2.1:

**Corollary 2.2.** *Let $G$ be a smooth algebraic group over a field $k$, $H$ a smooth algebraic subgroup, $N$ its
normalizer in $G$, $\varphi : G \times H \to G$ the morphism defined by $\varphi(g, h) = ad(g)h = ghg^{-1}$,
$\psi : X = G \times^{N} H \to G$ the morphism deduced from $\varphi$ by passage to the quotient (cf. section 1),
$a \in H(k)$. The following conditions are equivalent:*

<!-- label: III.XIII.2.2 -->

- *(i) $\varphi$ is smooth at $(e, a)$.*
- *(ii) $\psi$ is étale at $(\bar{e}, a)$, and $N$ is smooth over $k$.*
- *(iii) $(\mathfrak{g}/\mathfrak{h})^{ad(a)} = 0$ (where $\mathfrak{g}$, $\mathfrak{h}$ are the Lie algebras of $G$,
  $H$).*

*These conditions imply $H^{0} = N^{0}$.*

We know that the smoothness of $\varphi$ (which is a morphism between smooth $k$-preschemes) at a $k$-rational point is
equivalent to the surjectivity of the tangent map at that point. Now an immediate calculation shows that this tangent
map is written (using the usual identifications of the tangent spaces at points of $G$ and $H$ with the Lie algebras of
$G$ and $H$)

```text
dϕ(ξ, η) = (id − ad(a)) · ξ + η,
```

regarded as a map from $\mathfrak{g} \times \mathfrak{h}$ to $\mathfrak{g}$. <!-- original page 259 --> Surjectivity
therefore amounts to the surjectivity of $(id - ad(a))$ on $\mathfrak{g}/\mathfrak{h}$, i.e. to (iii). Now (iii) implies
a fortiori $(\mathfrak{g}/\mathfrak{h})^{H} = 0$, i.e. (cf. 2.0, where the connectedness hypothesis at the beginning of
the section is unnecessary) $H^{0} = N^{0}$. From this we deduce that $N$ is smooth, and $\dim H = \dim N$, whence
$\dim X = \dim G$. Now since $q : G \times H \to X$ is flat and $\psi \circ q = \varphi$ is smooth at $(e, a)$, it
follows that $\psi$ is smooth at $q(e, a) = (\bar{e}, a)$, hence étale at this point by reasons of dimension. So we have
proved (i) ⇔ (iii) ⇒ (ii); on the other hand (ii) ⇒ (i), because the smoothness of $N$ implies that of $q$. *QED*.

Let us finally prove (vi) ⇒ (i), which, together with the implications already established, will prove the theorem.
Suppose first that $G$ is affine. Let $U$ be a non-empty open of $G$ such that $x \in U(k)$ implies that $x$ is
contained in a conjugate of $H$. Let $C$ be a Cartan subgroup of $G$. Using the implication (i) ⇒ (iv) for $C$ in place
of $H$ (this is Borel's "density theorem"), it follows that one can find a conjugate of $C$ which meets $U$, so one can
assume $U \cap C \neq \emptyset$, i.e. that there exists a non-empty open $V$ in $C$ such that for every $x \in V(k)$,
$x$ is contained in a conjugate of $H$. Write $C$ as a product

$$
C = T \cdot C_{u}
$$

where $T$ is the maximal torus of $C$ (which is a maximal torus of $G$) and $C_{u}$ is the unipotent part of $C$, $T$
being in the center of $C$ (*Bible* 6 th. 2). We can again assume that $k$ has infinite transcendence degree over its
prime subfield, which allows us to find an element $t$ of $T(k)$ that is in the projection of $V$ onto $T$ (which is a
non-empty open of $T$), i.e. $t \cdot C_{u} \cap V \neq \emptyset$, and such that $t$ "generates" $T$. Since every
algebraic subgroup of $G$ containing a product $t \cdot u$ ($t \in T(k)$, $u \in C_{u}(k)$) contains the two factors
(*Bible* 4 th. 3), it follows, with the preceding choice of $t$, <!-- original page 260 --> and taking
$t \cdot u \in V(k)$, that there exists a conjugate of $H$ containing $t$, hence $T$. So we may already assume that one
has

$$
T \subset H.
$$

If $W$ is the open of $C_{u}$ inverse image of $V$ by $u \mapsto t \cdot u$, one sees therefore that for every element
$x$ of $(T \cdot W)(k)$, there exists a conjugate of $H$ containing $T$ and $x$. As we have already noted, such a
conjugate is of the form $int(g) \cdot H$, where $g \in N(T)(k)$. Consider then the morphism

```text
f : N(T) × H → G
```

defined by $f(g, h) = int(g) \cdot h = ghg^{-1}$; then the image of $f$ contains $T \cdot W$, so as $N(T)$ is a finite
union of translates $C \cdot g_{i}$ (where $g_{i} \in N(T)(k)$) since $C$ is of finite index in $N(T)$, it follows that
there exists a dense open $V_{0}$ of $C = T \cdot C_{u}$ which is contained in the image of $(C \cdot g_{i}) \times H$
by $f$. Replacing $H$ by $int(g_{i}) \cdot H$ if necessary, we may assume $g_{i} = e$, i.e.
$f(C \times H) \supset V_{0}$. So for every $u \in V_{0}(k)$, there exist $v \in C(k)$ and $h \in H(k)$ such that

```text
v⁻¹ h v = u, whence vuv⁻¹ ∈ H(k),
```

hence, setting

```text
C₀ = C ∩ H = Centr_H(T),
```

$vuv^{-1} \in C_{0}$, whence $int(v) \cdot C_{0} \supset u$. This proves that the union of the conjugates of $C_{0}$ in
$C$ (by elements of $C(k)$) is dense, which implies (as we have seen for the pair $(G, H)$ instead of $(C, C_{0})$) that
$C_{0}$ is of finite index in its normalizer in $C$. By *Bible* 7, lemma of section 1, it follows that $C_{0} = C$,
hence $C = H$, which proves (vi) ⇒ (i) when $G$ is affine.

In the general case, we proceed by induction on $n = \dim G$, the assertion being trivial if $n = 0$. Let $Z$ be the
center of $G$, and distinguish two cases:

1°) $\dim Z \cap H > 0$: then setting $G' = G/(Z \cap H)$, one has $\dim G' < n$; <!-- original page 261 --> on the
other hand the hypothesis (vi) on $H$ implies the same condition for the image $H'$ of $H$ in $G'$, so $H'$ contains a
Cartan subgroup $C'$ of $G'$, hence $H$ contains the inverse image $C$ of $C'$, which is a Cartan subgroup by XII 6.6
e).

2°) $\dim Z \cap H = 0$: then the canonical morphism $H \to G/Z$ is a finite morphism, and as $G/Z$ is affine by virtue
of XII 6.1, it follows that $H$ is affine, hence every homomorphism from $H$ into an abelian variety is zero (and even
every morphism of preschemes from $H$ to an abelian variety is zero): this follows from the fact that an affine smooth
connected algebraic group over an algebraically closed field is a rational variety, or simply that it is the union of
its Borel subgroups (*Bible* 6 th. 5 b)), and it follows very easily from the structure theorems *Bible* 6.2 and 6.3
that an affine smooth connected solvable group is a rational variety. Now use Chevalley's structure theorem for $G$,
according to which $G$ is an extension of an abelian variety $A$ by a smooth affine group. Then the image of $H$ in $A$
is zero, $H$ being affine; on the other hand it is identical to $A$, because the union of its conjugates in $A$ must be
dense. So $A = 0$, hence $G$ is affine, and we are reduced to the case already treated. This completes the proof of 2.1.

**Corollary 2.3.** *Assume that the equivalent conditions of 2.1 hold.*

<!-- label: III.XIII.2.3 -->

*a) Let $k(X)$ (resp. $k(G)$) be the field of rational functions of $X$ (resp. $G$); then $k(X)$ is a finite separable
extension of $k(G)$. Denote its degree by $d$.*

*b) Let $T$ be a maximal torus of $G$ contained in $H$ (which exists by form 2.1 (ii)), and let $C$ be the corresponding
Cartan subgroup of $G$. Then $C \subset H$. On the other hand, $Norm_{G}(T)$ is a smooth subgroup of $G$ and
`Norm_G(T) ∩ Norm_G(H) = Norm_{Norm_G(H)}(T)` is a smooth subgroup of it, of finite index equal to $d$ (defined in a)).
The number of conjugates of $H$ containing a given maximal torus or a given Cartan subgroup is equal to $d$.*

*c) Let $U$ be the largest open of $G$ such that <!-- original page 262 --> $\psi : X \to G$ induces a morphism
$\psi^{-1}(U) \to U$ that is finite and étale. Then $U$ is a dense open, and for $g \in G(k)$, one has $g \in U(k)$ if
and only if there exist exactly $d$ conjugates of $H$ containing $g$, or again if and only if there exist at least $d$
distinct conjugates $H_{i}$ of $H$ containing $g$ such that for every $i$, $(\mathfrak{g}/\mathfrak{h}_{i})^{ad(g)} = 0$
(where $\mathfrak{h}_{i} = Lie(H_{i})$).*

Assertion a) comes from the fact that $\psi$ is generically étale (which was stated at the end of 2.1); this also
implies that the open $U$ introduced in c) is non-empty, i.e. dense, and the two characterizations stated for the
elements of $U(k)$ (taking into account that $\psi$ is separated, $X$ integral and $G$ integral normal, SGA 1 I 10.11,
and that $(\mathfrak{g}/\mathfrak{h}_{i})^{ad(g)} = 0$ means that $\psi$ is étale at the point $x_{i}$ of $\psi^{-1}(g)$
corresponding to $H_{i}$). If $H$ contains the maximal torus $T$ of $G$, then the centralizers of $T$ in $H$ and $G$
have the same dimension, and are smooth and connected (XII 6.6 b)), hence are equal, which proves that $C \subset H$.
Moreover, one knows that the normalizer of $T$ in a smooth group containing it is smooth (XI, 2.4 bis), so $Norm_{G}(T)$
and $Norm_{Norm_{G}(H)}(T)$ are smooth (N.B. we have noted that $N = Norm_{G}(H)$ is smooth at the end of the statement
of 2.1); also $Norm_{N}(T)$ contains $C$, which is of finite index in $N(T)$, so it is of finite index in $N(T)$. Using
the theorem of conjugacy for maximal tori in $H$, one sees that the index in question equals the number of conjugates of
$H$ containing $T$, or what amounts to the same, containing $C$. Now since the union of the conjugates of $C$ in $G$ is
dense (by 2.1 (i) ⇒ (vi) applied to $C$ instead of $H$), and the open $U$ defined in c) is evidently stable under inner
automorphisms, one sees that $C \cap U \neq \emptyset$. Proceeding as in the proof of the implication (vi) ⇒ (ii) of
2.1, one concludes that (up to a harmless change of base field) there exists $g \in (C \cap U)(k)$ such that every
conjugate of $H$ containing $g$ contains $T$, and hence also $C$. So the conjugates of $H$ containing $C$ are those
containing $g$, and as $g \in U(k)$, their number equals $d$, which completes the proof of b). One will note that we
have in fact shown that the set of conjugates of $H$ containing $T$ is a homogeneous set <!-- original page 263 -->
under the group of rational points of

$$
W_{G}(T) = Norm_{G}(T)/Centr_{G}(T),
$$

which proves in particular that

```text
d ⩽ order of the Weyl group of G.
```

**Corollary 2.4.** *With the notation of 2.1, the following conditions are equivalent:*

<!-- label: III.XIII.2.4 -->

- *(i) $\psi : X \to G$ is a birational morphism.*
- *(ii) There is exactly one conjugate of $H$ containing a given Cartan subgroup of $G$.*
- *(iii) $H$ contains a Cartan subgroup $C$ of $G$, and $Norm_{G}(H) \supset Norm_{G}(C)$.*
- *(iv) There exists a non-empty open $V$ of $G$ such that $g \in V(k)$ implies that $g$ is contained in exactly one
  conjugate of $H$.*

This is clear from 2.1 and 2.3.

**Corollary 2.5.** *Assume that the conditions of 2.4 hold, and let $g \in G(k)$. The following conditions are
equivalent:*

<!-- label: III.XIII.2.5 -->

- *(i) $g \in U(k)$, where $U$ is defined in 2.3 c), i.e. $g$ is contained in exactly one conjugate of $H$.*
- *(ii) The set of conjugates of $H$ containing $g$ is finite and non-empty.*
- *(iii) The scheme $\psi^{-1}(g)$ "of conjugates of $H$ containing $g$" has an isolated point.*
- *(iv) There exists a conjugate $H'$ of $H$ containing $g$, and one has $(\mathfrak{g}/\mathfrak{h}')^{ad(g)} = 0$,
  where $\mathfrak{h}' = Lie(H')$.*

*Finally, $U$ is also the largest open of $G$ such that $\psi$ induces an isomorphism
$\psi^{-1}(U) \xrightarrow{\sim} U$.*

<!-- original page 264 -->

The equivalence of (i), (ii), (iii) and the last assertion follow from the "Main Theorem"[^N.D.E-XIII-3] applied to the
birational morphism $\psi : X \to G$, given that $G$ is normal. The equivalence of these conditions with (iv) follows at
once from the last assertion of 2.1 characterizing the set of points of $X$ at which $\psi$ is étale.

**Theorem 2.6.** *Let $G$ be a smooth connected algebraic group over an algebraically closed field $k$, $C$ a Cartan
subgroup, associated to a maximal torus $T$, $N = Norm_{G}(C) = Norm_{G}(T)$ (cf. XII 8.4), let $X = G \times^{N} C$,
where $N$ acts on the left factor $G$ by right translations, and on the right factor $C$ by inner automorphisms, and let
$\psi : X \to G$ be the canonical morphism.*

<!-- label: III.XIII.2.6 -->

*a) The morphism $\psi$ is birational.*

*b) Let $U$ be the largest open of $G$ such that $\psi$ induces an isomorphism $\psi^{-1}(U) \xrightarrow{\sim} U$ (cf.
2.5). Let*

```text
ρ = ρ_ν(G) = dim C
```

*be the nilpotent rank of $G$. Then for every $g \in G(k)$, the multiplicity of the eigenvalue `1` in $ad(g)$ acting on
$\mathfrak{g}$ is at least equal to $\rho$, and for it to equal $\rho$, it is necessary and sufficient that
$g \in U(k)$.*

*Proof.* Since condition 2.1 (i) is satisfied, one can apply 2.4 (iii) ⇒ (i), which establishes a). In *Bible* 7 (in the
case where $G$ is affine) the points of $U(k)$ are called the *regular points* of $G(k)$, and we shall follow this
terminology, calling $U$ the *open of regular points* of $G$. (N.B. The proof given in the *Bible*
    <!-- original page 265 --> that the set in question is itself open is incorrect, but we have obtained it in the present
Exposé under more general conditions.)

Let us prove b); for this, introduce for every $g \in G(k)$ the characteristic polynomial

```text
P(ad(g), t) = tⁿ + c₁(g) tⁿ⁻¹ + ⋯ + c_n(g);
```

one sees at once (replacing $k$ by any algebra over $k$) that the $c_{i}(g)$ come from well-determined sections

$$
c_{i} \in \Gamma(G, \mathcal{O}_{G}).
$$

When $g \in G(k)$ is an element contained in a Cartan subgroup (for example a regular element), which we may assume to
be $C$, then by 2.5 (iv) one sees that $(\mathfrak{g}/\mathfrak{c})^{ad(g)} = 0$ if and only if $g$ is regular (where
$\mathfrak{c}$ denotes the Lie algebra of $C$); on the other hand, since $C$ is nilpotent, one sees at once that
$ad_{\mathfrak{c}}(g)$ has only the eigenvalue `1`, which proves that the multiplicity of the eigenvalue `1` in
$ad_{\mathfrak{g}}(g)$ is $\geqslant \rho$, and equal exactly to $\dim C = \rho$ if and only if $g$ is regular. In
particular, the polynomial above is divisible by $(t - 1)^{\rho}$. Since the relation of divisibility by
$(t - 1)^{\rho}$ is expressed by linear relations (with integer coefficients) among the coefficients of the polynomial,
and these relations are satisfied for $g \in U(k)$, $U$ being a dense open, it follows ($G$ being reduced) that they
hold for all $g$; in fact one has a relation

```text
(†)    tⁿ + c₁ tⁿ⁻¹ + ⋯ + c_n = (t − 1)^ρ (tⁿ⁻ρ + b₁ tⁿ⁻ρ⁻¹ + ⋯ + b_{n−ρ})
```

<!-- label: eq:III.XIII.2.6.dagger -->

in the ring of polynomials over $\Gamma(G, \mathcal{O}_{G})$; in particular for every $g \in G(K)$, $ad(g)$ has the
eigenvalue `1` with multiplicity at least $\rho$. Moreover, we have seen that equality holds if $g$ is regular; let us
prove the converse. To this end, suppose first $G$ affine, and write $g$ as a product

$$
g = g_{s} g_{u}
$$

of its semisimple part and its unipotent part (*Bible* 4 section 4); then <!-- original page 266 -->

$$
ad(g) = ad(g_{s}) ad(g_{u})
$$

is the analogous decomposition of $ad(g)$ (loc. cit. cor. to th. 3), so $ad(g)$ and $ad(g_{s})$ have the same
eigenvalues (counted with multiplicity); in particular the eigenvalue `1` appears with the same multiplicity in $ad(g)$
and in $ad(g_{s})$.

Moreover, by *Bible* 7 th. 2 cor. 1, $g$ is regular if and only if $g_{s}$ is. Hence to prove b), we may assume
$g = g_{s}$, i.e. $g$ semisimple, so contained in a maximal torus by *Bible* 6 th. 5 c), and a fortiori in a Cartan
subgroup — the case already treated. This proves b) in the case $G$ affine. In the general case, let
$Z = Centr(G)_{red}$; then by XII 6.6 e) the Cartan subgroups of $G$ are the inverse images of those of $G' = G/Z$,
hence $g$ is regular in $G$ if and only if its image $g'$ in $G'$ is regular in $G'$. On the other hand, since $Z$ is
smooth, the Lie algebra $\mathfrak{g}'$ of $G'$ is none other than $\mathfrak{g}/\mathfrak{z}$, where
$\mathfrak{z} = Lie(Z)$, and $ad(g')$ is none other than $ad(g)_{\mathfrak{g}/\mathfrak{z}}$; hence the multiplicity of
the eigenvalue `1` in $ad(g)$ equals $d = \dim Z$ plus the multiplicity of the eigenvalue `1` in $ad(g')$, whence at
once the first is equal to the nilpotent rank of $G$ if and only if the second is equal to the nilpotent rank of $G'$.
Thus we are reduced to the case of $G'$; now $G'$ being affine by XII 6.1, this case has already been treated. This
completes the proof of 2.6.

**Corollary 2.7.** *With the notation of the preceding proof,[^N.D.E-XIII-4] let*

```text
b = 1 + b₁ + ⋯ + b_{n−ρ} ∈ Γ(G, 𝒪_G).
```

*Then the open of regular points of $G$ is given by*

$$
U = G_{b}
$$

<!-- label: III.XIII.2.7 -->

*(set of points of $G$ at which $b$ is invertible); in particular $U$ is an affine open if $G$ is affine.*

<!-- original page 267 -->

**Corollary 2.8.** *Let $H$ be a smooth connected algebraic subgroup of $G$ containing a Cartan subgroup of $G$.*

<!-- label: III.XIII.2.8 -->

*a) Let $C$ be an algebraic subgroup of $H$. In order that $C$ be a Cartan subgroup of $H$, it is necessary and
sufficient that it be a Cartan subgroup of $G$.*

*b) Let $g \in G(k)$, and let $d$ be the integer introduced in 2.3. In order that $g$ be a regular point of $G$, it is
necessary and sufficient that there exist exactly $d$ conjugates $H_{i}$ of $H$ containing $g$, and that for each $i$,
$g$ be a regular element of $H_{i}$; or again, that there be at most $d$ conjugates of $H$ containing $g$, and that $g$
be regular in one of them. If so, and if $C$ is the unique Cartan subgroup of $G$ containing $g$, then the conjugates of
$H$ containing $g$ are the conjugates of $H$ containing $C$.*

*c) Let $g \in H(k)$; in order that $g$ be regular in $G$, it is necessary and sufficient that it be regular in $H$, and
that one have $(\mathfrak{g}/\mathfrak{h})^{ad(g)} = 0$.*

Let us prove a). Under either hypothesis on $C$, the unique maximal torus $T$ of $C$ is a maximal torus of $H$ and of
$G$ ($H$ having the same reductive rank as $G$); hence as $Centr_{H}(T) \subset Centr_{G}(T)$ are smooth connected
groups of the same dimension, they are equal, so it amounts to the same to say that $C$ is equal to one or the other of
these two groups, which proves a).

Let us prove b). Suppose first $g$ regular in $G$, let $C$ be the unique Cartan subgroup of $G$ containing $g$. Then by
2.3 b) there exist exactly $d$ conjugates $H_{i}$ of $H$ containing $C$. Since
$(\mathfrak{g}/\mathfrak{c})^{ad(g)} = 0$, i.e. $ad(g)$ has no eigenvalue `+1` on $\mathfrak{g}/\mathfrak{c}$, one has a
fortiori $(\mathfrak{g}/\mathfrak{h}_{i})^{ad(g)} = 0$, hence by 2.3 c) there are exactly $d$ conjugates of $H$
containing $g$, namely the $H_{i}$. For such an $H_{i}$, a Cartan subgroup of $H_{i}$ <!-- original page 268 -->
containing $g$ is a Cartan subgroup of $G$ containing $g$ by a), hence equals $C$, which proves that $g$ is regular in
$H_{i}$. Conversely, suppose that there are at most $d$ conjugates $H_{i}$ of $H$ containing $g$, and that $g$ is
regular in one of them, which we may assume to be $H$. Let us prove that $g$ is regular in $G$. Since $g$ is regular in
$H$, it is contained in a unique Cartan subgroup $C$ of $H$; by a) this is a Cartan subgroup of $G$. Let $C'$ be a
Cartan subgroup of $G$ containing $g$; let us prove $C' = C$ (which will prove that $g$ is regular in $G$). Indeed, by
2.3 b) there exist exactly $d$ conjugates of $H$ containing $C'$, and as these latter contain $g$, they are necessarily
the $H_{i}$, hence the $H_{i}$ and in particular $H$ contain $C'$. Hence $C$, $C'$ are two Cartan subgroups of $H$ (by
a)) that contain the same regular element $g$ of $H$, so they are equal. *QED*.

Let us prove c). Denoting by $\nu(u)$ the nullity[^N.D.E-XIII-5] of $id - u$, for an endomorphism of a
finite-dimensional vector space, one has

$$
\nu(ad(g)_{\mathfrak{g}}) = \nu(ad(g)_{\mathfrak{h}}) + \nu(ad(g)_{\mathfrak{g}/\mathfrak{h}}),
$$

and the two terms on the right-hand side are respectively $\geqslant$ nilpotent rank of $H$ (equal to the nilpotent rank
$\rho$ of $G$ by a)) and $\geqslant 0$; hence one has $\nu(ad(g)_{\mathfrak{g}}) = \rho$ if and only if
$\nu(ad(g)_{\mathfrak{h}}) = \rho$ and $\nu(ad(g)_{\mathfrak{g}/\mathfrak{h}}) = 0$, i.e. $g$ is regular in $G$ if and
only if $g$ is regular in $H$ and $ad(g)_{\mathfrak{g}/\mathfrak{h}}$ has no non-zero invariants. *QED*.

**Remarks 2.9.** *In the statement of 2.1, one cannot weaken condition (iii) by assuming only that $H$ contains a
maximal torus and is of finite index in its normalizer, even if one further requires that this normalizer be smooth,
i.e. that $H = N^{0}$, and even when $G$ is affine solvable. An example is furnished by the group $G$ of matrices of the
form*

<!-- label: III.XIII.2.9 -->

```text
       ⎛ t a c ⎞
   g = ⎜ 0 1 b ⎟,
       ⎝ 0 0 1 ⎠
```

*and the subgroup $H$ of matrices of the preceding form with $b = c = 0$ (N.B. the Cartan subgroup of $G$ is here the
matrices $g$ with $a = c = 0$).*

<!-- original page 269 -->

**Remarks 2.10.** *Let $G$ be a smooth algebraic group over $k$, $H$ a smooth algebraic subgroup, but we no longer
assume $H$ and $G$ connected. Suppose that $H^{0}$ contains a Cartan subgroup of $G^{0}$. Then
$(\mathfrak{g}/\mathfrak{h})^{H} \subset (\mathfrak{g}/\mathfrak{h})^{H^{0}} = 0$, hence $H^{0} = N^{0}$ ($N$ is the
normalizer of $H$), in particular $N$ is smooth. However, one easily constructs examples, with $G$ connected, where $H$
has a connected component $H_{i}$ such that for no $h \in H_{i}(k)$ one has $(\mathfrak{g}/\mathfrak{h})^{ad(h)} = 0$,
i.e. the morphism $(g, h) \mapsto ad(g) \cdot h$ from $G \times H_{i}$ to $G$ is étale (nor even quasi-finite) at no
point (take for example for $H$ the normalizer of the maximal torus in $SL(2)_{k}$). Similarly, even if the image $H''$
of $H$ in the finite group $G'' = G/G^{0}$ equals $G''$, it is not necessarily true that the union of conjugates of $H$
in $G$ is dense (take for $G$ the semidirect product of $\mathbb{Z}/2\mathbb{Z}$ with $G^{0} = SL(2)_{k}$ on which it
acts by "symmetry", and for $H$ the semidirect product $\mathbb{Z}/2\mathbb{Z} \cdot T$, where $T$ is a maximal torus of
$G^{0}$). On the other hand, if one does not assume a priori that $H^{0}$ contains a Cartan subgroup of $G^{0}$, but
that the union of conjugates of $H$ in $G$ is dense, then $H^{0}$ necessarily contains a Cartan subgroup of $G^{0}$: to
verify this, one may evidently suppose $G$ connected, and it suffices to redo the proof of 2.1 (vi) ⇒ (i), which is
valid without assuming $H$ connected.*

<!-- label: III.XIII.2.10 -->

## 3. The case of an arbitrary base prescheme

<!-- label: III.XIII.3 -->

<!-- original page 270 -->

Suppose first that we are over a base field $k$, not necessarily algebraically closed. Since conditions 2.1 (i bis), (iv
bis), (v), (vi) are invariant under extension of the base field, one sees by passing to the algebraic closure $\bar{k}$
of $k$ that they are equivalent to each other, and equivalent to the fact that $H_{\bar{k}}$ contains a Cartan subgroup
of $G_{\bar{k}}$. When this condition is satisfied, then (with the notation of 2.3) it will still be true that $k(X)$ is
a finite separable extension of $k(G)$, of degree $d$ independent of any extension of the base. If $U$ is the largest
open of $G$ such that $\psi$ induces a morphism $\psi^{-1}(U) \to U$ that is finite and étale, then the formation of $U$
commutes with extension of the base field. If $\psi$ is birational, then $U$ is also the largest open of $G$ such that
$\psi$ induces an isomorphism $\psi^{-1}(U) \xrightarrow{\sim} U$, and if then $g \in U(k)$, there exists a subgroup
$H'$ of $G$ and only one, conjugate to $H$ over the algebraic closure $\bar{k}$ of $k$, such that $H' \ni g$.

A point $g \in G(k)$ is said to be *regular* if it is regular as an element of $G(\bar{k}) = G_{\bar{k}}(\bar{k})$. More
generally, the construction of 2.7 gives us an open of $G$, whose formation commutes with any extension of the base
field, called the *open of regular points* of $G$, which is also characterized by the fact that for every algebraically
closed extension $K$ of $k$ and every point $g \in G(K)$, $g$ is a regular point of `G_K` if and only if $g \in U(K)$.
If $g \in U(k)$,[^N.D.E-XIII-6] one sees that $g$ is contained in one and only one Cartan subgroup of $G$, as we shall
show under more general conditions below.

Let $G$ be a smooth, separated, finite-type prescheme in groups with connected fibers over the prescheme $S$; consider
the functor $\mathcal{C} : (Sch)^{\circ}/S \to (Ens)$ defined by

```text
𝓒(S′) = set of Cartan subgroups (XII 3.1) of G_{S′}.
```

Suppose this functor is representable by a smooth prescheme over $S$; we give in XV a necessary and sufficient condition
for this to be so, but we already know that this hypothesis is satisfied if $G$ is affine over $S$ with locally constant
reductive rank (XII 3.3), or more generally if $G$ admits locally for the fpqc topology a maximal torus (XII 7.1 a)),
for example if $S$ is the spectrum of a field. <!-- original page 271 --> Let $X$ be the Cartan subgroup of the
$\mathcal{C}$-prescheme in groups $G_{\mathcal{C}}$, the "universal Cartan subgroup" of $G$. As a prescheme over $S$,
$X$ therefore represents the functor

```text
X(S′) = set of pairs (C, g), C a Cartan subgroup of G_{S′} and g a section of C over S′.
```

Consider the canonical projection morphism $(C, g) \mapsto g$

$$
\psi : X \to G.
$$

One then has the:

**Theorem 3.1.** *Under the preceding conditions on $G$, and with the preceding notation, let $U$ be the set of
$g \in G$ such that $g$ is a regular element of its fiber $G_{s}$.*

<!-- label: III.XIII.3.1 -->

*Then $U$ is open, and it is also the largest open $U$ of $G$ such that $\psi$ induces an isomorphism
$\psi^{-1}(U) \xrightarrow{\sim} U$.*

Let us first prove that $U$ is open. From the hypothesis of representability of $\mathcal{C}$ as a smooth prescheme over
$S$, since its structural morphism is evidently surjective, one concludes at once that $G$ admits locally for the étale
topology a Cartan subgroup, and that the nilpotent rank of the fibers of $G$ is locally constant. The same holds for the
dimension of the fibers of $G$, and up to localizing on $S$, one may assume that both are constant, say $\rho$ and $n$.
Consider then the Killing polynomial

```text
P_G(t) = tⁿ + c₁ tⁿ⁻¹ + ⋯ + c_n ∈ A[t],   where A = Γ(G, 𝒪_G).
```

The restriction of this polynomial to the fibers $G_{s}$ of $G$, and in particular to the fibers at the maximal points
of $S$, is divisible by $(t - 1)^{\rho}$, which is expressed by the fact that certain linear combinations with integer
coefficients of the $c_{i}$ vanish on the fibers $G_{s}$. <!-- original page 272 --> When $S$ is reduced (which we may
assume in order to establish that $U$ is open), it follows that they are themselves zero, hence the Killing polynomial
itself is divisible by $(t - 1)^{\rho}$, say

```text
P_G(t) = (t − 1)^ρ (tⁿ⁻ρ + b₁ tⁿ⁻ρ⁻¹ + ⋯ + b_{n−ρ}).
```

Let $b$ be the sum of the coefficients $b_{0} = 1, b_{1}, \cdots, b_{n-\rho}$ of the second factor; then by 2.7 applied
to the fibers of $G$, one sees that

$$
U = G_{b},
$$

which indeed proves that $U$ is open.

To prove that $\psi^{-1}(U) \to U$ is an isomorphism, we are reduced by SGA 1, I 5.7 to verifying it fiber by fiber,
which reduces to the case of a base field, which we may assume algebraically closed. Then there exists a Cartan subgroup
$C$ of $G$, and if $N$ is its normalizer, $\mathcal{C}$ is identified by the conjugacy theorem XII 7.1 a) and b) with
$G/N$, and the morphism $\psi : X \to G$ considered here is none other than that defined in section 2. One concludes
then by 2.6 b). The same reasoning also shows that $U$ is the largest open of $G$ such that $\psi$ induces an
isomorphism $\psi^{-1}(U) \to U$.

**Corollary 3.2.** *Under the conditions of 3.1, let $g$ be a regular section of $G$, i.e. such that for every
$s \in S$, $g(s)$ is a regular point of $G_{s}$. Then there exists one and only one Cartan subgroup $C$ of $G$ such that
$g$ is a section of $C$.*

<!-- label: III.XIII.3.2 -->

Indeed, the hypothesis on $g$ means that $g$ is a section of $U$, and the conclusion means that there exists a unique
section of $X$ lifting it, which is just another way of expressing that $\psi^{-1}(U) \to U$ is an isomorphism.

Note now that the open $\psi^{-1}(U)$ of the Cartan subgroup $X$ of $G_{\mathcal{C}}$ is none other than <!-- original page 273 --> the
open of $X$ consisting of the points of $X$ that are regular in $G_{\mathcal{C}}$ (by which we mean: regular in their fiber). One
thus obtains a natural "fibration" of the dense open $U$ of regular points of $G$ over the prescheme $\mathcal{C}$, the fibers
being dense opens of Cartan subgroups of the fibers of $G_{\mathcal{C}}$ (namely the opens of regular points in $G$). One finds for
example the following result (which will be considerably refined in the following Exposé):

**Corollary 3.3.** *Let $G$ be a smooth connected algebraic group over the field $k$, $\mathcal{T}$ the scheme of
maximal tori of $G$ (≃ the scheme of Cartan subgroups of $G$). Then the field of functions $k(G)$ of $G$ is isomorphic
to the field of functions of a smooth connected affine nilpotent algebraic group $C$ over the field of functions
$k(\mathcal{T})$ of $\mathcal{T}$, namely $C =$ "the generic Cartan subgroup of $G$". If $G$ is affine of zero unipotent
rank, i.e. if the Cartan subgroups of `G_K` are tori, then $k(G)$ is a unirational extension of $k(\mathcal{T})$.*

<!-- label: III.XIII.3.3 -->

Of course, by *generic Cartan subgroup* of $G$, we mean (by abuse of language) the Cartan subgroup of
$G_{k(\mathcal{T})}$ generic fiber of $X$ over $\mathcal{T}$. It remains only to prove the last assertion of 3.3, which
is contained in the following well-known result (due to Chevalley):

**Lemma 3.4.** *Let $k$ be a field, $T$ a torus over $k$, $k(T)$ the field of rational functions on $T$; then $k(T)$ is
a unirational extension of $k$, i.e. is contained in a pure transcendental extension of $k$.*

<!-- label: III.XIII.3.4 -->

Indeed, let $k'$ be a finite separable extension of $k$ that splits[^N.D.E-XIII-7] $T$ (X 1.4); then $T \otimes_{k} k'$
is a rational variety, i.e. admits a dense open isomorphic to a dense open of affine space $\mathbb{A}^{n}_{k'}$; hence
`T′ = ∏_{Spec(k′)/Spec(k)} T_{k′}/Spec(k′)` is a rational variety (because it admits a dense open isomorphic to a dense
open of <!-- original page 274 --> $\prod_{\operatorname{Spec}(k')/\operatorname{Spec}(k)} \mathbb{A}^{n}_{k'}$, which
is isomorphic to affine space of dimension `mn` over $k$, where $m = [k' : k]$). Consider the norm homomorphism from
$T'$ to $T$ (defined whenever $T$ is a commutative group scheme over $k$); the composite $T \to T' \to T$ is the $m$-th
power in $T$, hence dominant, hence $T' \to T$ is dominant, which proves that $T$ is unirational.

Let us return to the conditions of 3.1, but assume further that $G$ admits, locally for the fpqc topology, a maximal
torus (XII 7.1). Let $Y$ be the maximal torus of the Cartan subgroup $X$ of $G_{\mathcal{C}}$, so that the morphism
$\psi : X \to G$ induces a morphism $Y \to G$ whose image is set-theoretically the semisimple elements of the fibers of
$G$ (XII 8). Finally, it follows from 3.1 that the restriction of $\psi$ to the open $Y_{reg}$ of regular points of $Y$
induces a closed immersion

$$
Y_{reg} \to U = G_{reg}.
$$

Making explicit the meaning of $Z = Y_{reg}$ as a functor on $S$, one finds:

**Corollary 3.5.** *Let $G$ be a smooth, separated, finite-type $S$-prescheme in groups with connected fibers over the
prescheme $S$, admitting locally for the fpqc topology a maximal torus. Let $Z : (Sch)^{\circ}/S \to (Ens)$ be the
functor defined by*

<!-- label: III.XIII.3.5 -->

```text
Z(S′) = set of regular sections of G_{S′} over S′ that are contained in
        a maximal torus of G_{S′}.
```

*Then $Z$ is representable by a closed sub-prescheme, smooth over $S$, of the open $U = G_{reg}$ of $G$ introduced in
3.1.*

To finish, let us note the following result, which sharpens the density theorem 2.1 (i) ⇒ (vi):

**Corollary 3.6.** *Under the conditions of 3.5, let $C$ be a Cartan subgroup of $G$, <!-- original page 275 --> and
consider the morphism*

<!-- label: III.XIII.3.6 -->

```text
ϕ : Z × C → G
```

*defined by $\varphi(g, h) = ad(g)h = ghg^{-1}$. Then $\varphi$ is dominant.*

It evidently suffices to prove this fiber by fiber, which reduces us to the case where $S$ is the spectrum of an
algebraically closed field. Let $T$ be the maximal torus of $C$, $t_{0}$ an element of $T(k)$ regular in $G$, $c_{0}$ an
element of $C(k)$ regular in $G$; consider $\varphi^{-1}(\varphi(t_{0}, c_{0}))$, whose $k$-rational points are the
pairs $(t, c)$ with $t \in Z(k)$, $c \in C(k)$, such that

```text
ad(t) c = ad(t₀) c₀   i.e.   c = ad(t⁻¹ t₀) c₀,
```

which are therefore in bijective correspondence with the $t \in Z(k)$ such that $ad(t^{-1} t_{0}) c_{0} \in C$, or
equivalently (since $c_{0}$ is regular) such that $t^{-1} t_{0} \in N$ (normalizer of $C$), i.e. $t \in N$. One obtains
an open and closed part of this fiber by restricting to the $t \in Z(k)$ such that $t \in C(k)$. So we have found a
connected component of $\varphi^{-1}\varphi(t_{0}, c_{0})$ isomorphic to $T$ (N.B. that the preceding set-theoretic
reasoning indeed gives an isomorphism of schemes is seen by replacing points with values in $k$ by points with values in
an arbitrary $k$-prescheme); hence the generic fiber of $\varphi$ is of dimension $\leqslant \dim T$, so $Im(\varphi)$
is of dimension `⩾ dim Z × C − dim T = dim Z + dim C − dim T`; now one has
`dim Z = dim Y = dim 𝓒 + dim T = dim G − dim C + dim T`, whence finally $\dim Im(\varphi) \geqslant \dim G$, so
$\varphi$ is dominant. *QED*.

**Remarks 3.7.** *One will note that the reasoning shows moreover that the connected component at $(t_{0}, c_{0})$ of
the fiber $\varphi^{-1}(\varphi(t_{0}, c_{0}))$ is isomorphic to $T$, in particular is smooth over $k$, and has the same
dimension as the generic fiber, which implies that $\varphi$ is in fact smooth <!-- original page 276 --> at
$(t_{0}, c_{0})$ (which one ought to be able to verify also by calculating the tangent map). It follows that under the
conditions of 3.6 the induced morphism $Z \times_{S} C_{reg} \to G_{reg}$ (where one has set $C_{reg} = C \cap G_{reg}$)
is a smooth morphism. One sees similarly that the analogous morphism $Z \times T_{reg} \to Z$ (where $T$ is a maximal
torus of $G$) is smooth; more generally, for every smooth connected invariant algebraic subgroup $H$ of $C$ containing a
regular element $c_{0}$ of $G(k)$, the image of $Z \times H \to G$ is dense in that of $G \times H \to G$.*

<!-- label: III.XIII.3.7 -->

## 4. Lie algebras over a field: rank, regular elements, Cartan subalgebras

<!-- label: III.XIII.4 -->

In what follows of this Exposé, we take up the theory developed by Chevalley in his book *Théorie des Groupes de Lie
III* (Act. Sc. Ind. 1226, Paris 1955), the technique of schemes allowing us to eliminate the hypothesis of
characteristic zero. We begin by recalling in the present section certain well-known notions and results.

Let $\mathfrak{g}$ be a Lie algebra over a ring $k$. For every $a \in \mathfrak{g}$, one denotes by $ad(a)$ the
endomorphism

```text
ad(a) · x = [a, x]
```

of $\mathfrak{g}$, which is a derivation of the Lie algebra $\mathfrak{g}$. Now for any derivation $D$ of the Lie
algebra $\mathfrak{g}$, the nil-space of $D$, i.e. the union of the kernels of the iterates of $D$, is a Lie subalgebra
of $\mathfrak{g}$, as one sees from the Leibniz formula

```text
Dᵐ([x, y]) = Σ_{0 ⩽ p ⩽ m} (m choose p) [Dᵖ x, Dᵐ⁻ᵖ y].
```

We shall set

```text
Nil(a, 𝔤) = nil-space of ad(a) = ⋃_{m ⩾ 0} Ker ad(a)ᵐ;
```

<!-- original page 277 -->

when no confusion need be feared, we shall denote it simply $Nil(a)$, and we shall call it the *nil-space of $a$ (in
$\mathfrak{g}$)*.

**Proposition 4.1.** *For every $a \in \mathfrak{g}$, its nil-space $Nil(a, \mathfrak{g})$ is a Lie subalgebra of
$\mathfrak{g}$, equal to its own normalizer.*

<!-- label: III.XIII.4.1 -->

It remains to prove that it is its own normalizer, i.e. that every element of $\mathfrak{g} / Nil$ annihilated by the
adjoint representation of `Nil` on $\mathfrak{g} / Nil$ is zero, which is trivial (since every element in this quotient
annihilated by $Ad(a)$ is zero).

In what follows of this section, we suppose that $k$ is a field, and that $\mathfrak{g}$ is of finite dimension over
$k$. We shall denote by $W(\mathfrak{g})$ the scheme over $k$ defined by $\mathfrak{g}$, whose points in the $k$-algebra
$A$ are the elements of $\mathfrak{g} \otimes_{k} A$. If $a \in \mathfrak{g}$, the characteristic polynomial of $ad(a)$
is also called the *characteristic polynomial* or *Killing polynomial* of $a$ in $\mathfrak{g}$, namely

```text
P_𝔤(a, t) = tⁿ + c₁(a) tⁿ⁻¹ + ⋯ + c_n(a),
```

where $n = rank_{k} \mathfrak{g}$, the $c_{i}(a) \in k$. Taking this polynomial also for
$a \in \mathfrak{g} \otimes_{k} A$,[^N.D.E-XIII-8] where $A$ is any $k$-algebra, one sees that the $c_{i}(a)$ come from
well-determined sections $c_{i}$ of the structural sheaf of $W(\mathfrak{g})$, i.e. from elements of the symmetric
algebra $A = Sym_{k}(\mathfrak{g}^{\vee})$, where $\mathfrak{g}^{\vee}$ is the dual of the $k$-module $\mathfrak{g}$.
(When $k$ is an infinite field, the $c_{i}$ are determined by knowing the corresponding polynomial functions
$\mathfrak{g} \to k$, but this is no longer the case if $k$ is a finite field.) Let $r$ be the largest integer such that
the Killing polynomial

```text
P_𝔤(t) = tⁿ + c₁ tⁿ⁻¹ + ⋯ + c_n ∈ A[t]
```

is divisible by `tʳ`, i.e. one has:

```text
P_𝔤(t) = tⁿ + c₁ tⁿ⁻¹ + ⋯ + c_{n−r} tʳ,    c_{n−r} ≠ 0.
```

<!-- original page 278 -->

The integer $r$ is called the *nilpotent rank* of the Lie algebra $\mathfrak{g}$. It is invariant under extension of the
base field.

**Proposition 4.2.** *Let $r$ be the nilpotent rank of $\mathfrak{g}$, and $a \in \mathfrak{g}$. Then one has*

<!-- label: III.XIII.4.2 -->

```text
rank_k Nil(a, 𝔤) ⩾ r,
```

*with equality if and only if*

$$
c_{n-r}(a) \neq 0.
$$

*In this case, $Nil(a, \mathfrak{g})$ is a nilpotent Lie algebra (and we shall see in 5.7 b) the converse, when
$\mathfrak{g}$ is the Lie algebra of an algebraic group $G$ smooth over $k$).*

The first assertion is trivial, since by definition $rank_{k} Nil(a, \mathfrak{g}) =$ multiplicity of the zero root in
$P_{\mathfrak{g}}(a, t)$. Let us prove that if $c_{n-r}(a) \neq 0$, then $Nil(a)$ is nilpotent, which also means that
for every $x \in Nil(a)$, $ad_{Nil(a)}(x)$ is a nilpotent endomorphism. One may assume $k$ algebraically closed; then as
$ad(a)_{\mathfrak{g}/Nil(a)}$ is injective, there exists a non-empty open $U$ of $W(Nil(a))$ such that for every
$x \in U(k)$, $ad(x)_{\mathfrak{g}/Nil(a)}$ is injective, hence $Nil(x) \subset Nil(a)$; one may further suppose $U$
contained in the open of points where $c_{n-r}$ does not vanish (since this open is non-empty by $c_{n-r}(a) \neq 0$),
and then $Nil(x)$ having the same dimension as $Nil(a)$, one will have $Nil(x) = Nil(a)$. Consequently, for every
$x \in U(k)$, $ad(x)_{Nil(a)}$ is nilpotent, and by the principle of extension of algebraic identities, this remains
true for every $x \in Nil(a)$, hence $Nil(a)$ is nilpotent.

One says that the element $a$ of $\mathfrak{g}$ is *regular* if $c_{n-r}(a) \neq 0$, i.e. if
$rank_{k} Nil(a, \mathfrak{g}) = r$. When $k$ is infinite, this also means that $rank_{k} Nil(a, \mathfrak{g})$ is the
smallest possible <!-- original page 279 --> (for $a$ varying in $\mathfrak{g}$). In any case, the notion of regular
element of $\mathfrak{g}$ is invariant under extension of the base field, and the set of points of $W(\mathfrak{g})$
that are regular (i.e. that come from regular points of $W(\mathfrak{g})$ with values in a suitable extension of $k$) is
open, since identical to $W(\mathfrak{g})_{c_{n-r}}$ (set of points where $c_{n-r}$ is invertible).

**Corollary 4.3.** *Let $a$ be a regular element of $\mathfrak{g}$, and $\mathfrak{h}$ a Lie subalgebra of
$\mathfrak{g}$ containing $a$. Then $\mathfrak{h}$ is nilpotent if and only if
$\mathfrak{h} \subset Nil(a, \mathfrak{g})$; in particular, $Nil(a, \mathfrak{g})$ is a maximal nilpotent subalgebra of
$\mathfrak{g}$.*

<!-- label: III.XIII.4.3 -->

Since $Nil(a)$ is nilpotent, the relation $\mathfrak{h} \subset Nil(a)$ indeed implies that $\mathfrak{h}$ is nilpotent;
and conversely, if $\mathfrak{h}$ is nilpotent, it is contained in the nil-space of its element $a$, i.e.
$\mathfrak{h} \subset Nil(a)$.

**Proposition 4.4.** *Suppose $k$ infinite. Let $\mathfrak{d}$ be a Lie subalgebra of $\mathfrak{g}$. Consider the
following conditions:*

<!-- label: III.XIII.4.4 -->

- *(i) $\mathfrak{d}$ is maximal nilpotent and contains a regular element of $\mathfrak{g}$.*
- *(i bis) $\mathfrak{d}$ is of the form $Nil(a, \mathfrak{g})$, where $a$ is a regular element of $\mathfrak{g}$.*
- *(ii) $\mathfrak{d}$ is nilpotent and of the form $Nil(a, \mathfrak{g})$, where $a \in \mathfrak{g}$.*
- *(ii bis) $\mathfrak{d}$ is nilpotent, and there exists $a \in \mathfrak{d}$ such that
  $ad(a)_{\mathfrak{g}/\mathfrak{d}}$ is injective.*
- *(iii) $\mathfrak{d}$ is nilpotent and identical to its own normalizer.*

*One has the implications:*

```text
(i) ⇔ (i bis) ⇒ (ii) ⇔ (ii bis) ⇔ (iii)
```

*(and we shall see in 5.7 a) that if $\mathfrak{g}$ is the Lie algebra of a smooth algebraic group, then all the
preceding conditions are equivalent).*

<!-- original page 280 -->

The equivalence of (i) and (i bis) is trivial by 4.3, and these conditions trivially imply (ii). The equivalence of (ii)
and (ii bis) is also trivial, as is (ii bis) ⇒ (iii) (cf. 4.1). It remains to prove the implication (iii) ⇒ (ii bis),
the only one moreover that uses the fact that $k$ is infinite, and which follows at once from:

**Lemma 4.5.** *Let $\mathfrak{d}$ be a nilpotent Lie algebra over an infinite field $k$, acting on a finite-dimensional
vector space $V$. Suppose that for every $x \in \mathfrak{d}$, the endomorphism $u(x)$ is non-injective. Then there
exists a non-zero element $v$ of $V$ annihilated by $\mathfrak{d}$.*

<!-- label: III.XIII.4.5 -->

One may suppose $k$ algebraically closed and $\mathfrak{d}$ of finite dimension. One knows then that $V$ is a direct sum
of finitely many non-zero stable subspaces $V_{i}$ ($1 \leqslant i \leqslant n$), such that for every $i$, and every
$x \in \mathfrak{d}$, $u(x)|V_{i}$ has a single eigenvalue $\lambda_{i}(x)$ (cf. Bourbaki, *Groupes et Algèbres de Lie*,
Chap. I, §4, Exercise 22). Let $c_{i}(x)$ be the constant term of the characteristic polynomial of $u(x)|V_{i}$, so that
$\lambda_{i}(x) = 0$ if and only if $c_{i}(x) = 0$. Then $c_{i}$ is a polynomial function on $\mathfrak{d}$, and the
hypothesis means that $\mathfrak{d}$ is the union of the sets of zeros of the $c_{i}$. So one of the $c_{i}$ is zero,
which reduces us (replacing $V$ by $V_{i}$) to the case where $V$ is such that the $u(x)$ ($x \in \mathfrak{d}$) are
nilpotent. But then Engel's theorem (Bourbaki loc. cit. th. 1) implies that there exists a non-zero $v$ in $V$
annihilated by $\mathfrak{d}$. *QED*.

One sees easily that ($k$ being always an infinite field) conditions (i) (i bis) of 4.4 are invariant under any
extension of the base field. If they are satisfied, one will say that $\mathfrak{d}$ is a *Cartan subalgebra* of
$\mathfrak{g}$; in the general case ($k$ not necessarily infinite) one will say that $\mathfrak{d}$ is a Cartan
subalgebra of $\mathfrak{g}$ if it becomes a Cartan subalgebra under one (and hence any) extension of the base field
$k \to k'$, with $k'$ infinite. This thus implies that $\mathfrak{d}$ is nilpotent and equal to its own normalizer.

<!-- original page 281 -->

**Proposition 4.6.** *a) Let $a$ be an element of $\mathfrak{g}$. If $a$ is regular, it is contained in one and only one
Cartan subalgebra of $\mathfrak{g}$ (and we shall see in 6.1 d) the converse when $k$ is algebraically closed and
$\mathfrak{g}$ is the Lie algebra of a smooth algebraic group).*

<!-- label: III.XIII.4.6 -->

*b) Let $\mathfrak{d}$ be a Cartan subalgebra of $\mathfrak{g}$, $a$ an element of $\mathfrak{d}$; then $a$ is regular
in $\mathfrak{g}$ if and only if $ad(a)_{\mathfrak{g}/\mathfrak{d}}$ is injective.*

Indeed, for a) one notes that if $a$ is regular, then $Nil(a, \mathfrak{g})$ is a Cartan subalgebra of $\mathfrak{g}$
(because this is true over an infinite extension $k'$ of $k$), and it follows then at once from 4.3 that every Cartan
subalgebra of $\mathfrak{g}$ containing $a$ is identical to the preceding one. For b) one notes that the
nullity[^N.D.E-XIII-9] of $ad(a)_{\mathfrak{g}}$ is equal to the sum of the nullities of $ad(a)_{\mathfrak{d}}$ and of
$ad(a)_{\mathfrak{g}/\mathfrak{d}}$, and as the first equals $r$, the sum is equal to $r$ if and only if
$ad(a)_{\mathfrak{g}/\mathfrak{d}}$ is injective. *QED*.

**Corollary 4.7.** *Let $a$ be a regular element of $\mathfrak{g}$, $\mathfrak{d}$ a Cartan subalgebra of $\mathfrak{g}$
containing $a$, $A$ an algebra over $k$, $\mathfrak{g}_{A}$ and $\mathfrak{d}_{A} \subset \mathfrak{g}_{A}$ the $A$-Lie
algebras deduced from $\mathfrak{g}$, $\mathfrak{d}$ by base change, $a_{A}$ the image of $a$ in $\mathfrak{g}_{A}$. Let
$u$ be an automorphism of $\mathfrak{g}_{A}$. In order that $u(\mathfrak{d}_{A}) = \mathfrak{d}_{A}$, it is necessary
and sufficient that one have $u(a_{A}) \in \mathfrak{d}_{A}$.*

<!-- label: III.XIII.4.7 -->

The condition is trivially necessary; let us prove that it is also sufficient. If it is satisfied, then
$\mathfrak{d}' = u(\mathfrak{d}_{A})$ is a Lie subalgebra containing $a_{A}$, and every element $b$ of which is such
that $ad(b)_{\mathfrak{d}'}$ is nilpotent (because $\mathfrak{d}'$ is isomorphic to $\mathfrak{d}_{A}$, which has this
property, as follows at once from the definition of "nilpotent" in Bourbaki, *Groupes et Algèbres de Lie*, Chap. I, §4,
def. 1). Taking $b = a_{A}$, one sees that the nil-space $Nil(b, \mathfrak{g}_{A})$ contains $\mathfrak{d}'$; on the
other hand it is equal to $\mathfrak{d}_{A}$, and as $\mathfrak{d}'$ is locally a direct factor in the module
$\mathfrak{g}_{A}$ ($\mathfrak{d}$ being so), hence in $\mathfrak{d}_{A}$, and as it is a projective module of the same
rank $r$ as the latter, one concludes that it equals it. *QED*.

**Proposition 4.8.** *Let $\mathfrak{h}$ be a Lie subalgebra of $\mathfrak{g}$.*

<!-- label: III.XIII.4.8 -->

<!-- original page 282 -->

*a) The following conditions are equivalent if $k$ is infinite:*

- *(i) $\mathfrak{h}$ contains a Cartan subalgebra $\mathfrak{d}$ of $\mathfrak{g}$.*
- *(ii) $\mathfrak{h}$ contains a regular element $a$ of $\mathfrak{g}$, and an element $b$ such that
  $ad(b)_{\mathfrak{g}/\mathfrak{h}}$ is injective.*
- *(iii) $\mathfrak{h}$ has the same nilpotent rank as $\mathfrak{g}$, and contains a regular element of
  $\mathfrak{g}$.*

*These conditions are invariant under extension of the base field $k$.*

*b) Suppose these conditions are satisfied over a suitable infinite extension $k'$ of $k$. Let $a \in \mathfrak{h}$;
then $a$ is regular in $\mathfrak{g}$ if and only if it is regular in $\mathfrak{h}$ and
$ad(a)_{\mathfrak{g}/\mathfrak{h}}$ is injective, i.e. if and only if $Nil(a, \mathfrak{h}) = Nil(a, \mathfrak{g})$ and
this is a Cartan subalgebra of $\mathfrak{h}$.*

*c) Under the conditions of b), let $\mathfrak{d}$ be a Lie subalgebra of $\mathfrak{h}$; in order that it be a Cartan
subalgebra of $\mathfrak{h}$, it suffices that it be a Cartan subalgebra of $\mathfrak{g}$ (and we shall see in 5.8 that
the condition is also necessary if $\mathfrak{g}$ is the Lie algebra of a smooth algebraic group $G$, and $\mathfrak{h}$
the Lie algebra of a smooth algebraic subgroup $H$ of $G$).*

One sees at once that conditions (ii) and (iii) of a) are invariant under extension of the base field $k$ (assumed
infinite), and that in statements b) and c), one may assume $k$ infinite, which we shall do. If $\mathfrak{h}$ contains
the Cartan subalgebra $\mathfrak{d} = Nil(a, \mathfrak{g})$, then $a$ is a regular element of $\mathfrak{g}$ such that
$ad(a)_{\mathfrak{g}/\mathfrak{h}}$ is injective, hence (i) ⇒ (ii). Conversely, if (ii) is satisfied, then for an
element $a$ "sufficiently general" of $\mathfrak{h}$, $a$ satisfies simultaneously the two conditions of (ii), hence
$Nil(a, \mathfrak{g})$ is a Cartan subalgebra of $\mathfrak{g}$ and is contained in $\mathfrak{h}$, so one has (i). So
(i) and (ii) are equivalent. Suppose them satisfied, let $a$ be a variable element of $\mathfrak{h}$; then

<!-- original page 283 -->

```text
(✱)   rank_k Nil(a, 𝔤) = rank_k Nil(a, 𝔥) + rank_k Nil(ad(a)_{𝔤/𝔥}),
```

on the other hand, the two terms of the right-hand side are respectively $\geqslant r_{0} =$ nilpotent rank of
$\mathfrak{h}$, and $\geqslant 0$, the equalities being moreover attained[^N.D.E-XIII-10] for an element "sufficiently
general" of $\mathfrak{h}$. Moreover, one has also $rank_{k} Nil(a, \mathfrak{g}) \geqslant r =$ nilpotent rank of
$\mathfrak{g}$, with equality attained for an element "sufficiently general" of $\mathfrak{h}$, and attained if and only
if $a$ is regular in $\mathfrak{g}$. One concludes from this that one has $r = r_{0}$, and that $a$ is regular if and
only if the two terms of the right-hand side of `(✱)` equal respectively $r_{0}$ and `0`, i.e. if and only if $a$ is
regular in $\mathfrak{h}$ and $ad(a)_{\mathfrak{g}/\mathfrak{h}}$ is injective, which proves b), and c) follows
trivially by taking an element $a$ in $\mathfrak{d}$ regular in $\mathfrak{g}$, so that
$Nil(a, \mathfrak{g}) = \mathfrak{d}$. Moreover, the preceding result shows that (i) ⇒ (iii); finally (iii) ⇒ (i),
because under (iii), an element sufficiently general $a$ of $\mathfrak{h}$ is regular in $\mathfrak{h}$ and in
$\mathfrak{g}$, hence $Nil(a, \mathfrak{h}) \subset Nil(a, \mathfrak{g})$ are respectively Cartan subalgebras of
$\mathfrak{h}$ and of $\mathfrak{g}$, and as they have the same rank over $k$, they are identical, which proves (i).
This completes the proof of 4.8.

## 5. The case of the Lie algebra of a smooth algebraic group: density theorem

<!-- label: III.XIII.5 -->

Let $G$ be a smooth algebraic group over the field $k$, and $\mathfrak{g}$ its Lie algebra. Let $\mathfrak{h}$ be a Lie
subalgebra of $\mathfrak{g}$. Let $G$ act on $W(\mathfrak{g})$ by the adjoint representation, and consider the subscheme
$W(\mathfrak{h})$. The construction of section 1 leads us to introduce

$$
N = Norm_{G}(\mathfrak{h}) = Norm_{G}(W(\mathfrak{h})),
$$

which is an algebraic subgroup of $G$ (not necessarily smooth),

$$
\mathfrak{n} = Lie(N),
$$

<!-- original page 284 -->

and the scheme

```text
X = G ×^N W(𝔥)
```

quotient of $\tilde{X} = G \times W(\mathfrak{h})$ by $N$ acting on the right by $(g, x) \cdot n = (gn, Ad(n^{-1})x)$.
We consider the canonical morphisms

```text
                      G × W(𝔥)
                       │     ╲
                      q│      ╲ ϕ
                       │       ╲
                       ↓        ↘
                       X ──ψ──→ W(𝔤).
```

**Theorem 5.1.** *With the preceding notation, suppose $k$ infinite. Consider the following conditions:*

<!-- label: III.XIII.5.1 -->

- *(i) $\mathfrak{h}$ contains a Cartan subalgebra $\mathfrak{d}$ of $\mathfrak{g}$.*
- *(ii) There exists $a \in \mathfrak{h}$ such that $ad(a)_{\mathfrak{g}/\mathfrak{h}}$ is injective.*
- *(iii) $\varphi : G \times W(\mathfrak{h}) \to W(\mathfrak{g})$ is generically smooth.*
- *(iv) The preceding morphism $\varphi$ (or also $\psi : X \to W(\mathfrak{g})$) is dominant, and $\mathfrak{h}$ has
  the same nilpotent rank as $\mathfrak{g}$.*
- *(v) $\psi : X \to W(\mathfrak{g})$ is generically smooth and $\mathfrak{h} = \mathfrak{n}$.*
- *(vi) $\psi : X \to W(\mathfrak{g})$ is dominant, and $\mathfrak{h} = \mathfrak{n}$.*
- *(vii) $\psi : X \to W(\mathfrak{g})$ is dominant.*
- *(viii) $\psi : X \to W(\mathfrak{g})$ is dominant, and $N$ is smooth.*
- *(ix) $\psi : X \to W(\mathfrak{g})$ is dominant, and $\mathfrak{h} = \mathfrak{n}$, and $\mathfrak{h}$ is the Lie
  algebra of a smooth algebraic subgroup $H$ of $G$.*
- *(x) $\psi : X \to W(\mathfrak{g})$ is generically quasi-finite, and $\mathfrak{n} = \mathfrak{h}$.*
- *(xi) $\psi : X \to W(\mathfrak{g})$ is generically étale, and $\mathfrak{n} = \mathfrak{h}$.*
- *(xii) There exists a smooth algebraic subgroup $H$ of $G$ with Lie algebra $\mathfrak{h}$, and $\mathfrak{h}$
  contains a Cartan subalgebra $\mathfrak{d}$ of $\mathfrak{g}$.*
- \*(xiii) There exists $a \in \mathfrak{h}$ such that $N$ and the transporter $M_{a}$ of $a$ to $\mathfrak{h}$ (cf. section 1) coincide
    <!-- original page 285 --> in a neighborhood of `e`, and `𝔫 = 𝔥`.*

*One then has the following diagram of implications:*

```text
  (xi) ⇔ (xii) ⇔ (xiii)  ⇒  (viii) ⇔ (ix) ⇔ (x)
                                                    ↓
   (i) ⇔ (ii) ⇔ (iii) ⇔ (iv)  ⇒ (v)  ⇒ (vi) ⇒ (vii).
```

*When $k$ is of characteristic zero, all the conditions considered are equivalent. Finally, one has*

```text
(xi) ⇔ [(i) and (viii)] ⇔ [(v) and (viii)].
```

Let us first note the trivial implications:

```text
(v) ⇒ (vi) ⇒ (vii),    (ix) ⇒ (vi),    (xi) ⇔ [(x) and (v)].
```

Let us prove the equivalence of conditions (i) to (iv) and that they imply (v). The implication (i) ⇒ (ii) is trivial.
On the other hand (iii) means, when $k$ is algebraically closed, that there exists a $k$-rational point of
$G \times W(\mathfrak{h})$ at which the tangent map to $\varphi$ is surjective, and one sees at once that this point may
be taken of the form $(e, a)$, where $a \in \mathfrak{h}$ (up to transforming it by an operation of $G(k)$). One
concludes that if $k$ is infinite (not necessarily algebraically closed) this condition (evidently sufficient) of
generic smoothness is still necessary. Now the tangent map is easily calculated: identifying the tangent space to
$W(\mathfrak{h})$ at $a$ with $\mathfrak{h}$, it is the map

```text
(ξ, x) ↦ [ξ, a] + x
```

from $\mathfrak{g} \times \mathfrak{h}$ to $\mathfrak{g}$. To say that it is surjective also means that
$ad(a)_{\mathfrak{g}/\mathfrak{h}}$ is surjective, or what amounts to the same, injective. This proves the equivalence
of conditions (ii) and (iii). Moreover, (ii) evidently implies $\mathfrak{h} = \mathfrak{n}$, and (iii) implies that
$\psi$ is generically smooth, <!-- original page 286 --> since if $\varphi$ is smooth at a point $u$, it follows ($q$
being flat) that $\psi$ is smooth at $q(u)$. So (ii), (iii) imply (v). Let us prove that they imply (i). For this, note
that since $\psi$ is dominant, and the set of regular points of $\mathfrak{g}$ is open dense, it follows that
$\mathfrak{h}$ contains regular elements of $\mathfrak{g}$, hence a "sufficiently general" element $b$ of $\mathfrak{h}$
is regular in $\mathfrak{g}$ and satisfies $ad(b)_{\mathfrak{g}/\mathfrak{h}}$ injective, so
$Nil(b, \mathfrak{g}) \subset \mathfrak{h}$, hence $\mathfrak{h}$ contains the Cartan subalgebra
$\mathfrak{d} = Nil(b, \mathfrak{g})$. So (i), (ii), (iii) are equivalent; finally (i) ⇔ (iv), since we have already
noted that if $\mathfrak{h}$ contains a Cartan subalgebra, it has the same rank as $\mathfrak{g}$ (4.6), so (i) ⇒ (iv);
conversely, if (iv) is satisfied, then $\mathfrak{h}$ contains a regular element of $\mathfrak{g}$, and since it has the
same rank as $\mathfrak{g}$, it contains a Cartan subalgebra by 4.6.

Let us prove the equivalence of conditions (viii) to (x). Let us first remark the following facts:

**Lemma 5.2.** *a) If $N$ is smooth, then*

<!-- label: III.XIII.5.2 -->

```text
dim X ⩽ dim G,
```

*with equality if and only if $\mathfrak{h} = \mathfrak{n}$.*

*b) If $\mathfrak{h} = \mathfrak{n}$, then*

```text
dim X ⩾ dim G,
```

*with equality if and only if $N$ is smooth.*

These assertions follow at once from the formula

```text
dim X = dim G − dim N + dim_k 𝔥,
```

and from the fact that $\dim N = \dim_{k} \mathfrak{n}$ is equivalent to $N$ smooth.

<!-- original page 287 -->

This established, (viii) ⇒ (x), since (viii) implies $\dim X \geqslant \dim G$, hence by 5.2 a) the equality of these
dimensions and $\mathfrak{h} = \mathfrak{n}$, hence (x); and one sees similarly (x) ⇒ (viii) by applying 5.2 b). On the
other hand, (viii) implies (ix), since it implies $\mathfrak{h} = \mathfrak{n}$, hence $\mathfrak{h}$ is the Lie algebra
of the smooth algebraic subgroup $N$ of $G$; and conversely (ix) ⇒ (viii), since $H$ normalizes its Lie algebra
$\mathfrak{h}$, so it is contained in $N$, and as $H$ is smooth and has the same Lie algebra as $N$, it follows that $N$
is smooth.

Let us finally prove the equivalence of conditions (xi), (xii), (xiii) and the fact that they entail (iii) (which will
complete the establishment of our diagram of implications). One has (xi) ⇔ (xiii), since if
$\mathfrak{n} = \mathfrak{h}$, then by 5.2 b) one has $\dim X \geqslant \dim G$, hence (xi) is then equivalent (given
that $W(\mathfrak{g})$ is normal) to the fact that $\psi$ is generically unramified, which is equivalent also to (xiii)
by (1.1 (ii) ⇔ (iii)), proceeding as above for the proof of (ii) ⇔ (iii). Since (xi) ⇒ (x) ⇒ (viii) by what we have
seen, one sees that (xi) implies that $N$ is smooth, i.e. $q : G \times W(\mathfrak{h}) \to X$ is smooth, hence the
composite $\varphi = \psi \circ q$ is generically smooth, i.e. one has (iii). Since (iii) ⇒ (i), it also follows that
(xi) ⇒ (xii).[^N.D.E-XIII-11] Finally (xii) ⇒ (xi), since one evidently has (xii) ⇒ (i), so as one has seen (i) ⇒ (iii)
⇒ (v), one has (xii) ⇒ (v); it follows that one has also (xii) ⇒ (ix), and as one has seen (ix) ⇒ (x), it follows that
(xii) ⇒ ((v) and (x)), hence (xii) ⇒ (xi) since generically étale = generically smooth + generically quasi-finite.

Finally, when $k$ is of characteristic 0, then (vii) ⇒ (viii), since by a theorem of Cartier, $N$ is automatically
smooth (VI_B 1.6.1), and [(viii) and (x)] ⇒ (xi), since in characteristic zero, for a morphism of integral preschemes,
generically étale = dominant and generically quasi-finite. This shows that in this case, all the conditions (i) to
(xiii) are equivalent.

<!-- original page 288 -->

**Corollary 5.3.** *Under the equivalent conditions (viii) to (x), there exists a unique smooth connected algebraic
subgroup $H$ of $G$ whose Lie algebra is $\mathfrak{h}$, and one has*

<!-- label: III.XIII.5.3 -->

```text
Norm_G(H) = Norm_G(𝔥) = N,    H = N⁰.
```

Indeed, $H = N^{0}$ will satisfy the required conditions; on the other hand if $H$ satisfies them, then (since $H$
normalizes its Lie algebra $\mathfrak{h}$) one has $H \subset N$, hence as this is an inclusion of smooth groups having
the same Lie algebra, with $H$ connected, one will have $H = N^{0}$. For the identity
$Norm_{G}(H) = Norm_{G}(\mathfrak{h})$, one may assume $k$ algebraically closed; then from what one has just seen, it
follows immediately that the points of the two groups with values in $k$ are the same; on the other hand the inclusions
$H \subset Norm_{G}(H) \subset N$ show that $Norm_{G}(H)$ and $N$ have the same Lie algebra, hence they are identical.

**Corollary 5.4.** *Under the equivalent conditions (i) to (iv), let $a \in \mathfrak{h}$. Then the following conditions
are equivalent, and are realized if $a$ is regular in $\mathfrak{g}$:*

<!-- label: III.XIII.5.4 -->

- *(i) $\varphi$ is smooth at $(e, a)$.*
- *(ii) $M_{a} = Transp_{G}(a, \mathfrak{h})$ is smooth at $e$, and $\dim_{e}(M_{a}) = rank_{k} \mathfrak{h}$.*
- *(iii) $ad(a)_{\mathfrak{g}/\mathfrak{h}}$ is injective (or again, bijective).*

*When one is under the equivalent conditions (xi) to (xiii), let $H$ be the algebraic subgroup of $G$ considered in 5.3.
Then the preceding conditions are also equivalent to the following conditions:*

- *(iv) $\psi$ is étale at $(\bar{e}, a)$.*
- \*(v) Denoting by $M^{0}_{a}$ the connected component of $e$ in the transporter $M_{a}$ of $a$ to $\mathfrak{h}$,
    <!-- original page 289 --> endowed with the structure induced by `M_a`, one has*

$$
H = M^{0}_{a}.
$$

Evidently (i) ⇒ (ii) since $M_{a}$ is isomorphic to the fiber $\varphi^{-1}(a)$, the point $e$ corresponding to
$(e, a)$; and one has (ii) ⇒ (i), since (ii) implies that $\varphi$ is "equidimensional" at $(e, a)$ (i.e. the dimension
of the fiber passing through this point equals that of the generic fiber), which implies ($G \times W(\mathfrak{h})$ and
$W(\mathfrak{g})$ being regular) that it is flat at $(e, a)$, hence smooth since its fiber is at this point. The
equivalence of (i) and (iii) has been seen in the proof of 5.1 as resulting from the simple calculation of the tangent
map. Moreover, one has seen in 4.8 b) that "$a$ regular in $\mathfrak{g}$" ⇒ (iii). Under conditions (xi) to (xiii),
since $q : G \times W(\mathfrak{h}) \to X$ is smooth ($N$ being smooth), it follows that (i) is equivalent to $\psi$
smooth at $(\bar{e}, a)$, and as $\psi$ is generically étale, this is equivalent to (iv). Finally, as was noted at the
end of the proof of 1.1, (iv) implies that $N$ is the prescheme induced on $M_{a}$ by an open and closed part of
$M_{a}$, whence (v); finally (v) ⇒ (ii) trivially (or again (v) ⇒ (iv) by 1.1, since $\psi$ is dominant and
$W(\mathfrak{g})$ normal, "unramified" is here equivalent to "étale"). This completes the proof of 5.4.

**Corollary 5.5.** *Let $G$ be a smooth algebraic group over a field $k$, $H$ a smooth algebraic subgroup such that its
Lie algebra $\mathfrak{h}$ contains (at least over a suitable extension of $k$) a Cartan subalgebra of the Lie algebra
$\mathfrak{g}$ of $G$. Let $K$ be a connected algebraic subgroup of $G$ (not necessarily smooth), with Lie algebra
$\mathfrak{k}$; suppose that $\mathfrak{k}$ contains a regular element $a$ of $\mathfrak{g}$ (at least over a suitable
extension of $k$). Then $H$ contains $K$ if and only if $\mathfrak{h}$ contains $\mathfrak{k}$.*

<!-- label: III.XIII.5.5 -->

Indeed, by 5.4 (iii) ⇒ (v) one has $H = M^{0}_{a}$ (N.B. of course, this relation being invariant under extension of the
base field, it is valid without the hypothesis that the latter be infinite!); on the other hand
$\mathfrak{k} \subset \mathfrak{h}$ evidently implies $K \subset M_{a}$, hence as $K$ is connected,
$K \subset M^{0}_{a}$, whence $K \subset H$. *QED*.

<!-- original page 290 -->

**Corollary 5.6.** *Let $G$, $H$ be as in 5.5, and let $K$ be an algebraic subgroup of $G$; suppose $H$ connected and
$K$ smooth. Then $K$ contains $H$ if and only if $\mathfrak{k}$ contains $\mathfrak{h}$.*

<!-- label: III.XIII.5.6 -->

Indeed, if $\mathfrak{k} \supset \mathfrak{h}$, then $K$ satisfies the hypothesis considered in 5.5 for $H$; on the
other hand $H$ evidently satisfies the condition considered for $K$ in 5.5. The conclusion then follows from 5.5.

**Corollary 5.7.** *Let $\mathfrak{g}$ be the Lie algebra of a smooth algebraic group $G$ over a field $k$. Then:*

<!-- label: III.XIII.5.7 -->

*a) Let $\mathfrak{d}$ be a Lie subalgebra of $\mathfrak{g}$. In order that $\mathfrak{d}$ be a Cartan subalgebra, it is
necessary and sufficient that $\mathfrak{d}$ be nilpotent and equal to its own normalizer.*

*b) Let $a$ be an element of $\mathfrak{g}$; in order that $a$ be regular, it is necessary and sufficient that
$Nil(a, \mathfrak{g})$ be nilpotent.*

Up to making an extension of the base field, one may assume $k$ infinite. Given 4.4, one is reduced for a) to proving
that if $\mathfrak{d}$ is nilpotent and contains an element $a$ such that $ad(a)_{\mathfrak{g}/\mathfrak{d}}$ is
injective, then $\mathfrak{d}$ is a Cartan subalgebra. Now by 5.1 (ii) ⇒ (i), $\mathfrak{d}$ contains a Cartan
subalgebra $\mathfrak{d}' = Nil(a, \mathfrak{g})$, and by 4.3 one concludes from the fact that $\mathfrak{d}$ is
nilpotent that $\mathfrak{d} = \mathfrak{d}'$. To prove b), one notes that $Nil(a, \mathfrak{g})$ is a Cartan subalgebra
of $\mathfrak{g}$ by a), hence $a$ is regular.

**Corollary 5.8.** *Let $G$ be a smooth algebraic group over a field $k$, $H$ a smooth algebraic subgroup,
$\mathfrak{g}$, $\mathfrak{h}$ the Lie algebras; suppose that after suitable extension of the base field, $\mathfrak{h}$
contains a Cartan subalgebra of $\mathfrak{g}$. Let $\mathfrak{d}$ be a Lie subalgebra of $\mathfrak{h}$; then it is a
Cartan subalgebra of $\mathfrak{h}$ if and only if it is a Cartan subalgebra of $\mathfrak{g}$.*

<!-- label: III.XIII.5.8 -->

<!-- original page 291 -->

Given 4.8 c), it remains to show that if $\mathfrak{d}$ is a Cartan subalgebra of $\mathfrak{h}$, it is a Cartan
subalgebra of $\mathfrak{g}$; for this one is reduced to showing that $\mathfrak{d}$ contains an element $a$ regular in
$\mathfrak{g}$, assuming (which is permissible) $k$ algebraically closed. But since there is a dense open in
$\mathfrak{h}$ consisting of regular points of $\mathfrak{g}$, our assertion follows from 5.1 (i) ⇒ (vii) applied to
$(\mathfrak{h}, \mathfrak{d})$.

## 6. Cartan subalgebras and subgroups of type (C), relative to a smooth algebraic group

<!-- label: III.XIII.6 -->

For simplicity, we restrict ourselves in the following theorem to the case of an algebraically closed base field (the
case of an arbitrary base prescheme being treated in the next Exposé):

**Theorem 6.1.** *Let $G$ be a smooth algebraic group over an algebraically closed field $k$, $\mathfrak{g}$ its Lie
algebra. Then:*

<!-- label: III.XIII.6.1 -->

*a) The Cartan subalgebras of $\mathfrak{g}$ are conjugate.*

*b) Let $\mathfrak{d}$ be a Cartan subalgebra of $\mathfrak{g}$. Then its normalizer $N$ in $G$ is smooth, and
$D = N^{0}$ is the only smooth connected subgroup of $G$ whose Lie algebra is $\mathfrak{d}$. One has*

```text
Norm_G(𝔡) = Norm_G(D) = N,    hence D = Norm_G(D)⁰.
```

*c) With $\mathfrak{d}$ as in b), set as in section 5: $X = G \times^{N} W(\mathfrak{d})$, and consider the canonical
morphism*

$$
\psi : X \to W(\mathfrak{g}),
$$

*(whose fiber at $a \in \mathfrak{g}$ has as points with values in $k$ the set of Cartan subalgebras of $\mathfrak{g}$
containing $a$). Then $\psi$ is a birational morphism.*

*d) With the notation of c), let $U$ be the largest open of $W(\mathfrak{g})$ such that $\psi$ induces an isomorphism*
    <!-- original page 292 -->

$$
\psi^{-1}(U) \xrightarrow{\sim} U.
$$

*Then for $a \in \mathfrak{g}$, the following conditions are equivalent:*

- *(i) $a \in U(k)$.*
- *(ii) $a$ is contained in one and only one Cartan subalgebra of $\mathfrak{g}$.*
- *(iii) The set of Cartan subalgebras of $\mathfrak{g}$ containing $a$ is finite and non-empty.*
- *(iv) The fiber $\psi^{-1}(a)$ has an isolated point.*
- *(v) (If $a \in \mathfrak{d}$) The morphism $\psi$ is étale (or merely: quasi-finite) at the point $(\bar{e}, a)$.*
- *(vi) $a$ is a regular element of $\mathfrak{g}$.*
- *(vii) With the notation of 5.4 (iii), one has $N = M_{a}$.*

*Proof.* Let us apply 5.1 when $\mathfrak{h}$ is a Cartan subalgebra $\mathfrak{d}$ of $\mathfrak{g}$; let us show that
the strongest conditions (xi) to (xiii) are then satisfied. This is evident, either in form (xiii) given 4.7 (which
implies that for a regular element $a$ of $\mathfrak{g}$ contained in $\mathfrak{d}$, one has $N = M_{a}$), or in form
(xi) = (x) + (i), since condition (i) is trivial and condition (x) follows from the fact that a regular point of
$\mathfrak{g}$ is contained in a single Cartan subalgebra of $\mathfrak{g}$ (4.6 a)), and a fortiori in a single
conjugate of $\mathfrak{d}$. Then b) follows from 5.3, and c) follows from the fact that $\psi$ is generically étale and
that a sufficiently general point (more precisely, a regular point) of $\mathfrak{g}$ is contained in a single Cartan
subalgebra of $\mathfrak{g}$. Under these conditions, the equivalence of conditions (i) to (v) on $a$ is an immediate
consequence of Zariski's Main Theorem for the separated birational morphism $\psi$, given that $W(\mathfrak{g})$ is
normal and $X$ is integral. <!-- original page 293 --> The equivalence of (v) and (vi) is a particular case of 5.4 (iii)
⇔ (iv) (reducing to the case where $a \in \mathfrak{d}$ by transforming $a$ by a suitable element $g \in G(k)$), given
4.6 b). Moreover, by 5.4, (v) and (vi) are also equivalent to $N \supset M^{0}_{a}$, and by 4.7 already invoked, this
even implies $N = M_{a}$. This proves d).

Of course, b), c), and the equivalence of (i), (iv), (v), (vi), (vii) remain valid over an arbitrary base field. Let us
now prove a) using the fact that $k$ is algebraically closed. By 5.1 (i) ⇒ (vii), $\psi : X \to W(\mathfrak{g})$ is
dominant, hence there exists a dense open $V$ of $W(\mathfrak{g})$ such that every $a \in V(k)$ is the image of an
element of $X(k)$, i.e. is contained in a conjugate of $\mathfrak{d}$. Applying this result to a second Cartan
subalgebra $\mathfrak{d}'$ of $\mathfrak{g}$, one sees that one may take $V$ such that every element of $V(k)$ is a
conjugate of an element of $\mathfrak{d}$ and of an element of $\mathfrak{d}'$. Taking a regular element in $V(k)$, it
follows that there is a conjugate $\mathfrak{d}''$ of $\mathfrak{d}'$ which contains an element of $\mathfrak{d}$
regular in $\mathfrak{g}$, hence which equals $\mathfrak{d}$ by 4.6 a). This completes the proof of 6.1.

**Definition 6.2.** *Let $G$ be a smooth algebraic group over a field $k$. One calls a* subgroup of type (C) *of $G$ any
smooth connected algebraic subgroup whose Lie algebra is a Cartan subalgebra of $\mathfrak{g}$. One calls the*
infinitesimal rank *of $G$ the nilpotent rank of its Lie algebra $\mathfrak{g}$, equal to the dimension of any subgroup
of type (C) of $G$.*

<!-- label: III.XIII.6.2 -->

From 6.1 b) one concludes at once:

**Corollary 6.3.** *Under the conditions of 6.2, the map $D \mapsto \mathfrak{d} = Lie D$ establishes a bijective
correspondence between subgroups of type (C) of $G$, and Cartan subalgebras $\mathfrak{d}$ of $\mathfrak{g}$. If $D$ is
a subgroup of type (C) of $G$, $D$ is its own connected normalizer:*

<!-- label: III.XIII.6.3 -->

$$
D = Norm_{G}(D)^{0}.
$$

<!-- original page 294 -->

Combining 6.1 (a) and 6.3, one finds:

**Corollary 6.4.** *If $k$ is algebraically closed, the subgroups of type (C) of $G$ are conjugate to each other.*

<!-- label: III.XIII.6.4 -->

**Corollary 6.5.** *Let $G$ be a smooth algebraic group over algebraically closed $k$, $H$ a smooth algebraic subgroup
of $G$, $\mathfrak{g}$ and $\mathfrak{h}$ the Lie algebras. In order that $\mathfrak{h}$ contain a Cartan subalgebra of
$\mathfrak{g}$, it is necessary and sufficient that $H$ contain a subgroup $D$ of type (C) of $G$.*

<!-- label: III.XIII.6.5 -->

This is evidently sufficient, and is also necessary, since in order that one have $H \supset D$, it is necessary and
sufficient that $\mathfrak{h} \supset \mathfrak{d}$, by 5.5.

**Remarks 6.6.** *a) One will note that the connected subgroups $H$ of $G$ described in 6.5 correspond bijectively to
the Lie subalgebras $\mathfrak{h}$ of $\mathfrak{g}$ satisfying the strongest condition (xii) of 5.1 (and by 5.5,
inclusion relations between such subgroups can already be recognized on their Lie algebras).*

<!-- label: III.XIII.6.6 -->

*b) Suppose still that $k$ is algebraically closed, and let $D$ be a subgroup of type (C) of $G$; then it is easy to
show that $D$ contains a Cartan subgroup $C$ of $G$: indeed, let $V = \mathfrak{g}/\mathfrak{d}$; then for a "general"
element $a$ of $\mathfrak{d}$, $ad(a)$ acting on $V$ is injective (it suffices that $a$ be regular in $\mathfrak{g}$);
from this one easily concludes that for $g \in D(k)$ "general", $Ad(g)$ acting on $V$ has no non-zero invariants, which
allows one to apply 2.1 (vii) ⇒ (i). In fact, we shall see in the following Exposé a more precise result: every Cartan
subgroup $C$ of $G$ is contained in one and only one subgroup of type (C) of $G$.*

\*c) One should not confuse in general Cartan subgroups and subgroups of type (C): the subgroups of type (C) of $G$ are
Cartan subgroups <!-- original page 295 --> if and only if they are nilpotent (Cartan subgroups being indeed maximal
nilpotent subgroups), and it may happen that $\mathfrak{g}$ is nilpotent without $G$ being so (example: $SL(2)_{k}$ for
$k$ of characteristic 2); then the Cartan subalgebras of $\mathfrak{g}$ are identical to $\mathfrak{g}$, i.e. $G$ is a
subgroup of type (C) of itself if $G$ is connected, but it is not a Cartan subgroup of $G$! On the other hand, we shall
see in XIV that if $G$ is a semisimple adjoint group, then its subgroups of type (C) are its Cartan subgroups.
Similarly, in characteristic 0, without restriction on the smooth algebraic group $G$ over $k$, the same conclusion is
valid: this follows at once from the fact that in characteristic 0, a connected algebraic group is nilpotent if (and
only if) its Lie algebra is. This follows at once from the fact that in characteristic zero, the center $Z$ of the
connected algebraic group $G$ has as Lie algebra the center of $\mathfrak{g}$ (for one obtains a priori the space of
invariants of $\mathfrak{g}$ under the adjoint representation of $G$; now $G$ being connected and $k$ of characteristic
zero, these are also the "invariants" in the infinitesimal sense of the adjoint representation of $\mathfrak{g}$, i.e.
the center of $\mathfrak{g}$), and that by Cartier's theorem (cf. VI_B 1.6.1) $Z$ is smooth.

<!-- LEDGER DELTA — Exposé XIII — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| variétés à opérateurs | varieties with operators | Section 1 title; standard. |
| sous-S-préschéma fermé | closed S-subprescheme | Standard. |
| stabilisateur | stabilizer | Already in glossary. |
| fibré principal | principal bundle | Already in glossary. |
| fibré principal homogène | principal homogeneous bundle | Variant; preserve. |
| transporteur | transporter | Already in glossary. |
| symétrique de son transporteur | symmetric of its transporter | Technical; preserve literal rendering. |
| rang réductif | reductive rank | Per glossary (Tome II material). |
| rang nilpotent | nilpotent rank | Standard SGA 3 term. |
| rang infinitésimal | infinitesimal rank | Per Definition 6.2. |
| polynôme de Killing | Killing polynomial | Standard. |
| nil-espace | nil-space | Preserve hyphen; matches Bourbaki nilespace. |
| nullité | nullity | Per footnote N.D.E-XIII-5: dimension of the nil-space. |
| élément régulier | regular element | Per glossary. |
| sous-algèbre de Cartan | Cartan subalgebra | Standard. |
| sous-groupe de type (C) | subgroup of type (C) | Preserve parenthesized capital. |
| sous-groupe de Cartan | Cartan subgroup | Already in glossary. |
| ouvert dense | dense open | Standard. |
| génériquement étale / lisse / quasi-fini | generically étale / smooth / quasi-finite | Standard. |
| sous-groupe radiciel de hauteur 1 | (not used here) | — |
| splitte (FR slang) | splits | N.D.E-XIII-7 notes ambiguity; rendered "splits" with footnote. |
| variété rationnelle / unirationnelle | rational / unirational variety | Standard. |
| extension transcendante pure | pure transcendental extension | Standard. |
| sous-groupe lisse | smooth subgroup | Standard. |
| sous-groupe distingué | normal subgroup | (Not in this Exposé but glossary entry confirmed.) |
| BIBLE 4 / 6 / 7 | *Bible* 4 / 6 / 7 | Italicised, matching SGA 3 glossary convention for the Chevalley Seminar. |
| Main Theorem | "Main Theorem" | Zariski's; footnote preserves the SGA editorial gloss. |
-->

[^N.D.E-XIII-1]: Not having identified this reference, we refer to Theorem II.5.2.1 of the book: M. Demazure & P.
    Gabriel, *Groupes algébriques* I, Masson (1970).

[^N.D.E-XIII-2]: See, for example, EGA IV₄, Th. 17.11.1 d).

[^N.D.E-XIII-3]: of Zariski!

[^N.D.E-XIII-4]: cf. (†) above.

[^N.D.E-XIII-5]: i.e. the dimension of its nil-space.

[^N.D.E-XIII-6]: correction of $G(k)$ to $U(k)$.

[^N.D.E-XIII-7]: splits (?), or: "over which $T$ is split".

[^N.D.E-XIII-8]: $W \otimes_{k} A$ has been corrected to $\mathfrak{g} \otimes_{k} A$.

[^N.D.E-XIII-9]: i.e. the dimension of the nil-space.

[^N.D.E-XIII-10]: "equality" has been replaced by "the equalities".

[^N.D.E-XIII-11]: because $H = N$ works.
