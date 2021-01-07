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

#### Combinatorial designs and geometry

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
