---
Layout: post
mathjax: true
comments: true
title:  "A polyhedral turducken"
categories: Mathematics
date:  2021-01-07
---

**January 7, 2021.** *Some thoughts on simplices embedded in the
  intersection of a hypercube and a hypersphere, motivated by the game Spot It! (aka Dobble).*

#### Introduction

The game of *Spot It!* (called *Dobble* in the UK) is a simple game
based on some relatively deep mathematics.
There is a deck of $55$ cards, each of which has eight symbols printed
on it, from a total symbol vocabulary of $57$.
For each two cards in the deck, there is precisely one symbol in
common, and on each round, the first person to find the shared symbol
between the last card and a newly drawn card wins a point.
Eight is a good number since, according to
[Miller's "law"](https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two),
the number of objects the average human can hold in short-term memory
is seven.
(You can play an
[online version](http://thewessens.net/ClassroomApps/Main/intersection.html)
by Ken Wessen.)

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/spotit1.jpg"/>
	</div>
	</figure>

I enjoy the game, but like many mathematically-minded folk who play
it, became distracted by the question: how does it work?
Somewhat nontrivially, as it turns out.

#### Projective geometry and combinatorial designs

The usual approach is to consider an alphabet of $n$ symbols, a deck
of size $d$, and $\ell$ symbols per card, satisfying the constraint
that every two cards share precisely one symbol in common.
If we add the further constraint that each pair of symbols occurs on
one card only, then we have a nice equivalence to
[finite projective geometry](https://en.wikipedia.org/wiki/Projective_plane),
provided we interpret a card as a line and a symbol as a point of
intersection, with "axioms"

1. Any two lines (cards) intersect at exactly one point (symbol).
2. Any two points (symbols) are joined by exactly one line (card).

The question then becomes about the existence of a finite projective
plane with $n$ points and $d$ lines.
There is a simple approach to answering this question, expounded
clearly by
[Yuval Filmus](https://math.stackexchange.com/questions/36798/what-is-the-math-behind-the-game-spot-it).
Let $p$ be a prime number, and $[p] := \\{0, 1, 2, \ldots, p - 1\\}$.
We construct the "regular points" as pairs

$$
R = \{(m ,n) : m , n \in [p]\} = [p] \times [p],
$$

as well as $p + 1$ "points at infinity", $I = [p] \cup \{\infty\}$.
The set of points (symbols) consists of regular points and those at infinity, $R
\cup I$, so that

$$
n = |R \cup I| = p^2 + p + 1.
$$

We construct each line (cards) to have $n + 1$ points (symbols) as
follows.
First, we have lines $L_{mn}$ of slope $m$ and "intercept" $n$,
defined by

$$
L_{mn} = \{(x, mx + n) : x \in [p]\} \cup \{m\},
$$

where sums are taken modulo $p$.
We also have $p$ lines of "infinite slop",

$$
L_{\infty n} = \{n\} \times [p] = \{(n, x) : x \in [p]\}.
$$

Finally, we have a special line $L_\infty = I$ which simply "runs
along" infinity. Altogether, this gives $d = p^2 + p + 1$ lines.
It's easy to see that every combination of symbols occurs on precisely
one card (we've constructed them this way) and each pair of lines
intersects in exactly one point.
(More generally, [this construction works](https://en.wikipedia.org/wiki/Projective_plane#Finite_projective_planes) for $p$ a prime power, so
that $[p]$ can be viewed as a finite field.)

*Spot It!* realises this construction for $p = 7$, with $n = 7^2 + 7 +
1 = 57$ symbols. For some mysterious reason, they removed two cards,
so $d = 55$.

#### Resources

- ["The mathematics of *Spot It!*"](https://openprairie.sdstate.edu/cgi/viewcontent.cgi?article=1016&context=jur)
(2014), Marcus Heemstra.
- ["What is the math behind the game *Spot It!*?"](What is the math
  behind the game Spot It?) (2011), Mathematics StackExchange.
- ["The mathematics of *Dobble*"](http://thewessens.net/ClassroomApps/Main/finitegeometry.html)
  (accessed 2021), Ken Wessen.

<!-- http://www.math.uchicago.edu/~may/VIGRE/VIGRE2011/REUPapers/Markov.pdf -->

<!-- It turns out to involve a wonderful overlap of
[pure](https://en.wikipedia.org/wiki/Incidence_geometry) and
[applied](https://en.wikipedia.org/wiki/Combinatorial_design)
mathematics, and there are many resources (see below) for learning
more. -->
