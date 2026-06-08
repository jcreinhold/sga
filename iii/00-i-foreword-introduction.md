# Foreword and Introduction

<!-- label: III.avertissement-introduction -->

## Avertissement

<!-- label: III.avertissement -->

We present here a slightly revised re-edition of the original Séminaire, whose aim and content are indicated in the
Introduction. The revision consisted essentially in the correction of typographical errors, the addition (in footnotes)
of some supplementary remarks or references, the present subdivision into three volumes each equipped with a detailed
table of contents and an index of notation, and the adjunction of a terminological index at the end of Volume 3. In
addition, Exposé VI_B by J.-E. Bertin has been partially rewritten by him, in particular §§ 5 and 10, so that some
references to that Exposé differ from references to the original Exposé. The reader will find a list of the Séminaire's
Exposés at the beginning of the present volume.

Since the first edition of the present Séminaire appeared, the *Éléments de Géométrie Algébrique*, Chap. IV, have
appeared in their entirety, which renders certain passages of the Séminaire unnecessary; we have occasionally indicated
in footnotes the relevant references to EGA IV that allow such passages to be short-circuited.

For another exposition on algebraic groups using systematically the language of schemes, we point to the book by M.
Demazure and P. Gabriel, *Groupes algébriques* (North-Holland & Masson et Cie). Unlike the present Séminaire, this book
assumes no knowledge of algebraic geometry, but contains all the necessary preliminaries from the theory of schemes, and
its reading can therefore serve as an introduction to the study of our Séminaire. (It also contains themes not covered
in the Séminaire, such as the Dieudonné-style structure theory of commutative affine algebraic groups, in *loc. cit.*
Chap. V.)

Bures-sur-Yvette, March 1970

## Introduction

<!-- label: III.introduction -->

<!-- original page xxi -->

**1.** The aim of the present seminar is twofold.

On the one hand, we aim to give convenient foundations for the theory of group schemes in general. Exposés I to IV will
provide for this purpose the indispensable preliminary exercises in schematic and categorical syntax. To obtain a
language that "fits" geometric intuition effortlessly, and to avoid eventually unbearable circumlocutions, we always
identify a prescheme $X$ over another $S$ with the functor $(Sch)^{\circ}/S \to (Ens)$ that it represents,[^I-intro-1]
and it is necessary to give many definitions in such a way that they apply to arbitrary functors, representable or not.
Moreover, nearly all the functors we shall have to use will be "sheaves" (for the "faithfully flat quasi-compact
topology"); Exposé IV, which treats groups only incidentally, gives a sketch of the language of "localization" and
sheaves, which turns out to be very convenient for questions of representability of functors as well. Above all, this
Exposé will provide us, for questions of passage to the quotient, with the most convenient framework for what follows.

Exposé V gives some general results on the existence of quotients, taken up in Exposé VI_A in the case of the quotient
of an algebraic group over a field (or more generally, over an Artinian ring) by a subgroup.[^I-intro-2] The latter
Exposé and Exposé VI_B which follows it also contain various elementary results specific to algebraic groups over a
field, used routinely thereafter.

Exposé VII studies certain facts linked to the characteristic of the base field, and in particular develops with
appropriate generality the correspondence between radicial group schemes of height 1 and restricted $p$-Lie algebras.

<!-- original page xxii -->

Finally, Exposé XVIII contains the generalization, in the theory of schemes, of Weil's theorem on the "birational"
definition of algebraic groups.

On the other hand, we propose to generalize to groups over an arbitrary base prescheme the Borel–Chevalley structure
theory of affine algebraic groups. It has moreover become apparent in the course of writing up the seminar notes that
the affine hypothesis is unnecessary for many results of the theory. The most complete results are obtained, evidently,
in the case of "semisimple group schemes", or more generally "reductive" ones, with which we shall be exclusively
concerned from Exposé XIX onwards. Chevalley himself had already given the construction of the "Tôhoku" groups over the
ring of integers, a construction that will be taken up in the present seminar. The principal uniqueness
theorem[^I-intro-3] gives a simple characterization of the "twisted" variants of these Tôhoku groups over a base
prescheme $S$: they are the affine and smooth groups over $S$ whose geometric fibers are connected semisimple groups in
the usual sense.[^I-intro-4]

**2.** As in the case of the theory known over an algebraically closed field, a crucial role is played by the sub-tori
of the group schemes under consideration. The preliminary study of tori — and, more generally, of "group schemes of
multiplicative type" (both from the intrinsic viewpoint and from the viewpoint of multiplicative-type subgroups of a
given group) — therefore takes up a fairly large place in this seminar (Exposés VIII to XII). Their remarkable rigidity
(in certain respects greater even than that of abelian schemes, or of semisimple group schemes) makes them very
effective working instruments for the study of certain more general groups.

**3.** From Exposé XII onwards (with the exception of Exposé XVIII already mentioned) we shall routinely use the theory
of affine algebraic groups over an algebraically closed field, which the reader will find in the *Séminaire Chevalley*
1956, in particular in Exposés IV to IX of that seminar. We shall also use, but to a lesser extent, the later Exposés of
the *Séminaire Chevalley*, devoted to the structure of semisimple algebraic groups. Indeed, we shall take up Chevalley's
theory directly in the framework of schemes: it will be seen that in this way (even over a base field) the exposition
gains in simplicity and in precision.

**4.** The principal object of the present seminar is evidently to develop techniques that apply to the study of group
schemes over an arbitrary base, i.e. essentially to the study of families of algebraic groups. As such, the
infinitesimal properties of such families, and in particular the case of an Artinian base scheme, play an important
role. These properties intervene even for the study

<!-- original page xxiii -->

of algebraic groups over a field $k$, in the case where the latter is not perfect, in order in particular to apply the
technique of descent in the non-Galois case. Among the new results obtained in this case, let us mention the existence
of maximal tori and Cartan subgroups in any smooth algebraic group, the rationality of the variety of maximal tori, and
various related results (Exp. XIV[^I-intro-5]), or the correspondence between the "forms" of a semisimple group and the
principal homogeneous bundles under a suitable (in general non-connected) semisimple algebraic group (Exp. XXIV,
1.16–1.20). In general, one may say that the methods required to work over a non-perfect base field are essentially
those used for arbitrary base preschemes, and thereby fall outside the framework of classical algebraic geometry.

**5.** It has not seemed useful to indicate at the head of the written-up Exposés the date or dates of the corresponding
oral presentations at the Séminaire. Let us merely say that the order of the mimeographed Exposés (from I to XXVI) does
correspond to the order of the oral presentations. On the other hand, the writing-up of the final text is sometimes
notably later than the oral presentation, and often differs from it fairly substantially, the written text being
generally more detailed and more complete (such as Exp. IV and VII_B), or indeed substantially more general (such as
Exp. XII or VII_B) than the oral presentation. Other written Exposés correspond to no oral presentation (VI_B, VII_A,
XV, XVI, XVII, and essentially XXVI), and were written up and inserted into the mimeographed seminar either to provide
convenient references for various other Exposés (this is notably the case of VI_B), or because they constitute a natural
extension of the notions and techniques already developed. One should note as a consequence that the reading of Exposés
VII_A, VII_B, XV, XVI, XVII is not necessary for the study of the rest of the seminar, and in particular for the part of
this seminar devoted to reductive group schemes.

**6.** From the theory of schemes, we shall mainly use the general language of schemes, expounded in EGA I; the notions
of flat morphism, étale morphism, smooth morphism, expounded in SGA 1, I to V; and finally the theory of faithfully flat
descent of SGA 1, VIII. We have as far as possible avoided formulating unnecessary noetherian hypotheses, which has
required us in return to replace the usual hypothesis "of finite type" by the hypothesis "of finite presentation". For
the notion of morphism of finite presentation, the reader is referred to [EGA IV, 1.4](https://jcreinhold.github.io/ega/iv/12-ch4-01-relative-finiteness-conditions.html#14-morphisms-locally-of-finite-presentation) and 1.6. The results of SGA 1, I to
IV, most often stated in the noetherian context, will be developed in the general case in EGA IV,[^I-intro-6] where
standard methods for reducing certain types of statements (involving hypotheses of finite presentation) to the
noetherian case will also be developed in detail ([EGA IV, §§ 8](https://jcreinhold.github.io/ega/iv/21-ch4-08-projective-limits.html#8-projective-limits-of-preschemes), 9, 11). The reader who does not wish to admit these
results from EGA IV can simplify certain statements or their proofs by assuming the base prescheme to be locally
noetherian. He will, however, expose himself to difficulties in cases where the proof

<!-- original page xxiv -->

proceeds by descent from `Â` to $A$, where `Â` is the completion of a noetherian local ring $A$, since this method leads
to the introduction of the (in general non-noetherian) ring $\hat{A} \otimes_{A} \hat{A}$.

**7.** References will be made following the usual decimal system: the reference 5.7.11 refers to the proposition (or
lemma, definition, etc.) of that name in the same Exposé; in the reference XVII 7.8 the Roman numeral indicates the
number of the Exposé. We shall use the following abbreviations for our standard references:

| Abbreviation | Expansion                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Bible*      | Séminaire Chevalley, *Groupes de Lie algébriques*, 1956/58                                                                                             |
| EGA X, x.y.z | J. Dieudonné and A. Grothendieck, *Éléments de Géométrie Algébrique*, Chap. X, statement x.y.z (or sub-paragraph x.y, etc.)                            |
| SGA n, X y.z | *Séminaire de Géométrie Algébrique du Bois-Marie*, year $n$, statement y.z of Exposé X.                                                                |
| TDTE         | A. Grothendieck, *Techniques de descente et théorèmes d'existence en Géométrie Algébrique*, Exposés in the *Séminaire Bourbaki* between 1959 and 1962. |

## Bibliography

[CTS79] J.-L. Colliot-Thélène and J.-J. Sansuc, *Fibrés quadratiques et composantes connexes réelles*, Math. Ann.
**244** (1979), 105–134.

[Ha75] W. J. Haboush, *Reductive groups are geometrically reductive*, Ann. of Math. **102** (1975), no. 1, 67–83.

[KM97] S. Keel and S. Mori, *Quotient by groupoids*, Ann. of Math. **145** (1997), no. 1, 193–213.

[Ko97] J. Kollár, *Quotient spaces modulo algebraic groups*, Ann. of Math. **145** (1997), no. 1, 33–79.

[MF82] D. Mumford and J. Fogarty, *Geometric invariant theory*, 2nd ed., Springer-Verlag, 1982; (resp. 3rd ed., with F.
Kirwan, 1994).

[Na64] M. Nagata, *Invariants of a group in an affine ring*, J. Math. Kyoto Univ. **3** (1964), no. 3, 369–377.

[NM64] M. Nagata and T. Miyata, *Note on semi-reductive groups*, J. Math. Kyoto Univ. **3** (1964), no. 3, 379–382.

[Se77] C. S. Seshadri, *Geometric reductivity over an arbitrary base*, Adv. Math. **26** (1977), no. 3, 225–274.

[^I-intro-1]: Such a viewpoint seems to have been envisaged for the first time eight or nine years ago, in connection
    with the theory of formal groups, by P. Cartier, who unfortunately did not take the trouble to make it precise and
    systematic as it deserved.

[^I-intro-2]: For a more thorough study of passage to the quotient, in particular by reductive groups, see the important
    study by D. Mumford, *Geometric Invariant Theory*, Ergebnisse der Mathematik, Bd. 34, Springer, 1965. Let us observe
    that, on an important point, the terminology of this book does not agree with ours: over a field of characteristic
    $p > 0$, the groups that Mumford calls "reductive"[^N.D.E-I-intro-1] are the smooth groups of multiplicative type in
    the sense of the seminar (cf. Exp. IX). One may presumably consider that Mumford's acceptation of the word
    "reductive", which loses its meaning over a base that is not a field, was adopted by him on a provisional basis and
    as a kind of stopgap (and this is also roughly what Mumford explains, for other motives, from the second paragraph
    of his preface!).

[^I-intro-3]: *N.D.E.* This refers to Corollary XXIII.5.6, which is easily deduced from the uniqueness theorem for split
    reductive groups (cf. XXIII, Th. 4.1 and Cor. 5.2), given that every semisimple $S$-group is a "twisted form" (for
    the étale topology) of a "Tôhoku" group (cf. XXII, Cor. 2.3).

[^I-intro-4]: This is the essential result of M. Demazure's thesis (*Schémas en groupes réductifs*, Bull. Soc. Math.
    France **93** (1965), 369–413).

[^I-intro-5]: *N.D.E.* In particular, Theorems 1.1 and 6.1.

[^I-intro-6]: Since the writing of this introduction, the four parts (§§ 1 to 21) of EGA IV have appeared.

[^N.D.E-I-intro-1]: *N.D.E.* Concerning the quotient by a reductive group, the situation has evolved considerably since
    A. Grothendieck wrote Note (∗∗). Indeed, for an affine algebraic group over an arbitrary field $k$, the "good"
    notion, introduced by Mumford, is that of "geometrically reductive" group. (One says, on the other hand, that $G$ is
    "linearly reductive" if every rational representation of $G$ is completely reducible; but, as pointed out in Note
    (∗∗), this condition is too restrictive if $char(k) > 0$.) By the results of M. Nagata and W. J. Haboush ([Na64],
    [NM64], [Ha75]), the geometrically reductive $k$-groups are exactly the reductive $k$-groups in the sense of the
    present seminar. For all this, see the subsequent editions of Mumford's book ([MF82]). Moreover, the extension to
    the case of an arbitrary base of the notion of "geometric reductivity", and of its consequences for passage to the
    quotient, was carried out by C. S. Seshadri ([Se77]), and additions, due to M. Raynaud, are to be found in the
    article [CTS79] of J.-L. Colliot-Thélène and J.-J. Sansuc. Finally, for more recent developments concerning passage
    to the quotient by an algebraic group or, more generally, by a groupoid (cf. Exposé V of the present seminar), we
    point to the articles [Ko97] and [KM97] by J. Kollár and by S. Keel and S. Mori.
