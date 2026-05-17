# Introduction

<!-- label: I.0 -->

In the first part of this introduction, we give details on the contents of the present volume; in the second, on the
whole of the “Séminaire de Géométrie Algébrique du Bois-Marie”, of which the present volume is the first tome.

## 1

<!-- label: I.introduction.1 -->

The present volume presents the foundations of a theory of the fundamental group in algebraic geometry, from the
“Kroneckerian” point of view that makes it possible to treat on the same footing the case of an algebraic variety in the
usual sense and, for example, that of the ring of integers of a number field. This point of view can be expressed
satisfactorily only in the language of schemes, and we shall freely use this language, as well as the principal results
set out in the first three chapters of the _Éléments de Géométrie Algébrique_ by J. Dieudonné and A. Grothendieck, cited
below as EGA. The study of the present volume of the “Séminaire de Géométrie Algébrique du Bois-Marie” requires no other
knowledge of algebraic geometry, and can therefore serve as an introduction to current techniques in algebraic geometry
for a reader wishing to become familiar with them.

Exposés I through XI of this book are a textual reproduction, practically unchanged, of the mimeographed notes of the
oral seminar, which were distributed by the Institut des Hautes Études Scientifiques.[^intro-1] We have limited
ourselves to adding a few footnotes to the original text, correcting a few typographical errors, and making one
terminological adjustment: in particular, the term “simple morphism” was in the meantime replaced by “smooth morphism”,
which does not give rise to the same confusions.

Exposés I through IV present the local notions of étale morphism and smooth morphism; they make little use of the
language of schemes, set out in Chapter I of the _Éléments_.[^intro-2] Exposé V presents the axiomatic description of
the fundamental group of a scheme, useful even in the classical case where the scheme reduces to the spectrum of a
field, where one finds a very convenient reformulation of the usual Galois theory. Exposés VI and VIII present descent
theory, which has taken on growing importance in algebraic geometry in recent years and could render analogous services
in analytic geometry and topology. It should be noted that Exposé VII had not been written up, and that its substance is
incorporated into a work of J. Giraud, _Méthode de la Descente_, _Bulletin de la Société Mathématique de France_,
Mémoire 2, 1964, viii + 150 pages.

In Exposé IX, one studies more specifically the descent of étale morphisms, obtaining a systematic approach to Van
Kampen type theorems for the fundamental group, which appear here as simple translations of descent theorems. It is
essentially a method for computing the fundamental group of a connected scheme X, equipped with a surjective and proper
morphism, say X′ → X, in terms of the fundamental groups of the connected components of X′ and of the fiber products X′
×\_X X′, X′ ×\_X X′ ×\_X X′, and of the homomorphisms induced between these groups by the canonical simplicial morphisms
between the preceding schemes. Exposé X gives the theory of specialization of the fundamental group for a proper and
smooth morphism; its most striking result consists in the determination, up to a small ambiguity, of the fundamental
group of a smooth algebraic curve in characteristic p > 0, thanks to the result known by transcendental methods in
characteristic zero. Exposé XI gives some examples and complements, making explicit in cohomological form Kummer’s
theory of coverings and Artin-Schreier’s.

For other comments on the text, see the “Foreword” to the multigraphed version, which follows the present Introduction.

Since this Seminar was written in 1961, M. Artin and I have developed the language of the étale topology and a
corresponding cohomological theory, set out in SGA 4, “Cohomologie étale des schémas”, of the _Séminaire de Géométrie
Algébrique_, to appear in the same series as the present volume. This language, and the results already available in it,
provide a particularly flexible tool for the study of the fundamental group, making it possible to understand better,
and to go beyond, some of the results set out here. The theory of the fundamental group should therefore be taken up
again entirely from this point of view; in fact all the key results already appear in that work.

This was what had been planned for the chapter of the _Éléments_ devoted to the fundamental group, which was also to
contain several other developments that could not find a place here, relying on the technique of resolution of
singularities: the computation of the “local fundamental group” of a complete local ring in terms of a suitable
resolution of the singularities of that ring; local and global Künneth formulas for the fundamental group without a
properness hypothesis (cf. Exposé XIII); and M. Artin’s results on the comparison of the local fundamental groups of an
excellent henselian local ring and of its completion (SGA 4 XIX). Let us also point out the need to develop a theory of
the fundamental group of a topos, which will encompass at once the ordinary topological theory, its semi-simplicial
version, the “profinite” variant developed in Exposé V of the present volume, and the slightly more general pro-discrete
variant of SGA 3 X 7, adapted to the case of schemes that are non-normal and not unibranch.

While awaiting a complete recasting of the theory in this spirit, Exposé XIII by Mme Raynaud, using the language and
results of SGA 4, is intended to show the use that can be made of it in a few typical questions, especially by
generalizing some results of Exposé X to non-proper relative schemes. In particular, it gives the structure of the
prime-to-p fundamental group of a non-complete algebraic curve in arbitrary characteristic, which I had announced in
1959 but for which no proof had been published to date.

Despite these many gaps and imperfections, or as others would say because of these gaps and imperfections, I think the
present volume may be useful to the reader who wishes to become familiar with the theory of the fundamental group, and
also as a reference work, while awaiting the writing and publication of a text escaping the criticisms I have just
enumerated.

## 2

<!-- label: I.introduction.2 -->

The present volume is tome 1 of the “Séminaire de Géométrie Algébrique du Bois-Marie”, whose following volumes are
planned to appear in the same series. The aim of the _Séminaire_, parallel to the treatise _Éléments de Géométrie
Algébrique_ by J. Dieudonné and A. Grothendieck, is to lay the foundations of algebraic geometry according to the points
of view of the latter work. The standard reference for all volumes of the _Séminaire_ consists of Chapters I, II, and
III of the _Éléments de Géométrie Algébrique_, cited as EGA I, II, and III; the reader is assumed to possess the
background in commutative algebra and homological algebra implied by those chapters.[^intro-3] In addition, in each
volume of the _Séminaire_, reference will be made freely, as needed, to earlier volumes of the same _Séminaire_, or to
other published or soon-to-appear chapters of the _Éléments_.

Each part of the _Séminaire_ is centered on a main subject, indicated in the title of the corresponding volume or
volumes; the oral seminar generally covers one academic year, sometimes more. The exposés within each part of the
_Séminaire_ are generally in close logical dependence on one another; by contrast, the different parts of the
_Séminaire_ are, to a large extent, logically independent of one another. Thus the part “Group Schemes” is almost
entirely independent of the two parts of the _Séminaire_ that chronologically precede it, although it frequently appeals
to results of EGA IV. Here is the list of the parts of the _Séminaire_ that are to appear shortly, cited below as SGA 1
through SGA 7:

- SGA 1. Étale coverings and the fundamental group, 1960 and 1961.
- SGA 2. Local cohomology of coherent sheaves and local and global Lefschetz theorems, 1961/62.
- SGA 3. Group schemes, 1963 and 1964, three volumes, in collaboration with M. Demazure.
- SGA 4. Theory of topoi and étale cohomology of schemes, 1963/64, three volumes, in collaboration with M. Artin and J.
    L. Verdier.
- SGA 5. ℓ-adic cohomology and L-functions, 1964 and 1965, two volumes.
- SGA 6. Intersection theory and the Riemann-Roch theorem, 1966/67, two volumes, in collaboration with P. Berthelot and
    L. Illusie.
- SGA 7. Local monodromy groups in algebraic geometry.

Three of these partial seminars were directed in collaboration with other mathematicians, who will appear as co-authors
on the covers of the corresponding volumes. As for the other active participants in the _Séminaire_, whose role, both
editorial and mathematical, has grown from year to year, each participant’s name appears at the head of the exposés for
which he is responsible as lecturer or writer, and the list of those appearing in a given volume is indicated on that
volume’s flyleaf.

It is appropriate to give a few details on the relation between the _Séminaire_ and the _Éléments_. The latter were
intended in principle to give an overall account of the notions and techniques judged most fundamental in algebraic
geometry, as those notions and techniques themselves emerge through the natural play of demands of logical and aesthetic
coherence. From this viewpoint, it was natural to consider the _Séminaire_ as a preliminary version of the _Éléments_,
destined sooner or later to be absorbed almost entirely into them. This process had already begun to some extent several
years ago, since Exposés I through IV of the present volume SGA 1 are entirely encompassed by EGA IV, and Exposés VI
through VIII were to be so within a few years in EGA VI.

However, as the work of building undertaken in the _Éléments_ and in the _Séminaire_ develops, and as the overall
proportions become clearer, the initial principle, according to which the _Séminaire_ would constitute only a
preliminary and provisional version, appears less and less realistic, for reasons including the limits prudently imposed
by nature on the length of human life. Given the care generally taken in writing the different parts of the _Séminaire_,
there will doubtless be reason to take up such a part again in the _Éléments_, or in treatises that might take over from
them, only when later progress permits very substantial improvements, at the cost of fairly deep modifications. This is
already the case for the present seminar SGA 1, as said above, and also for SGA 2, thanks to recent results of Mme
Raynaud. By contrast, nothing at present indicates that this will be so in the near future for any of the parts cited
above, SGA 3 through SGA 7.

References inside the “Séminaire de Géométrie Algébrique du Bois Marie” are given as follows. An internal reference to
one of the parts SGA 1 through SGA 7 of the _Séminaire_ is given in the style III 9.7, where the numeral III denotes the
number of the exposé, which appears at the top of each page of the exposé in question, and 9.7 denotes the number of the
statement, definition, remark, or similar item inside that exposé. If needed, longer decimal numbers may be used, for
example 9.7.1 and 9.7.2 to designate the various steps in the proof of Proposition 9.7. The reference III 9 denotes
paragraph 9 of Exposé III. The number of the exposé is omitted for references internal to an exposé. For a reference to
another part of the _Séminaire_, the same sigla are used, but preceded by the mention of the SGA part in question, for
example SGA 1 III 9.7. Similarly, the reference EGA IV 11.5.7 means: _Éléments de Géométrie Algébrique_, Chapter IV,
statement, definition, etc. 11.5.7; here, the first Arabic numeral again denotes the paragraph number. Apart from these
conventions, in force throughout the SGA, the bibliography for an exposé will generally be gathered at its end, and
inside the exposé it will be referred to by numbers in square brackets, such as [3], according to custom.

Finally, for the reader’s convenience, whenever it seems necessary, we shall append to the end of SGA volumes an index
of notation and a terminological index containing, where appropriate, an English translation of the French terms used.

I wish to add an extra-mathematical comment to this introduction. In November 1969 I learned that the Institut des
Hautes Études Scientifiques, where I had been a professor essentially since its founding, had for three years been
receiving subsidies from the Ministry of the Armed Forces. Already as a beginning researcher I had found extremely
regrettable the lack of scruple shown by most scientists in accepting collaboration in one form or another with military
apparatuses. My motivations at that time were essentially moral in nature, and hence not very likely to be taken
seriously. Today they acquire a new force and a new dimension, given the danger of destruction of the human species with
which we are threatened by the proliferation of military apparatuses and of the means of mass destruction at their
disposal.

I have explained myself elsewhere in more detail on these questions, much more important than the advancement of any
science, mathematics included; one may for example consult on this subject G. Edwards’s article in number 1 of the
journal _Survivre_ (August 1970), summarizing a more detailed exposition of these questions that I had given elsewhere.
Thus I found myself working for three years in an institution while it was taking part, unbeknownst to me, in a mode of
financing that I consider immoral and dangerous.[^intro-4] Being at present alone in holding this opinion among my
colleagues at the IHES, which has doomed to failure my efforts to obtain the removal of military subsidies from the IHES
budget, I have taken the necessary decision and leave the IHES on September 30, 1970, and likewise suspend all
scientific collaboration with this institution as long as it continues to accept such subsidies.

I have asked M. Motchane, director of the IHES, that from October 1, 1970 the IHES abstain from distributing
mathematical texts of which I am the author, or which form part of the Séminaire de Géométrie Algébrique du Bois Marie.
As was said above, distribution of this seminar will be carried out by the Julius Springer publishing house, in the
Lecture Notes series. I am happy to thank Springer and Mr. K. Peters here for the effective and courteous help they gave
me in making this publication possible, in particular by taking charge of the typing for photo-offset of the new exposés
added to old seminars, and of the missing exposés in incomplete seminars.

I also thank Mr. J. P. Delale, who took on the thankless task of compiling the index of notation and the terminological
index.

Massy, August 1970.

<!-- source: /Users/jcreinhold/Code/papers/sga-1/smf_doc-math_3_01.tex, Introduction -->

[^intro-1]: As were the notes of the seminars following this one. Since this mode of distribution proved impractical and
    insufficient in the long run, all the “Séminaire de Géométrie Algébrique du Bois-Marie” will henceforth
    appear in book form, as the present volume does.

[^intro-2]: A more complete study is now available in the _Éléments_, Chapter IV, §§17 and 18.

[^intro-3]: See the Introduction to EGA I for details on this point.

[^intro-4]: It goes without saying that the opinion I have just expressed engages only my own responsibility, and not
    that of the Springer publishing house, which is editing the present volume.
