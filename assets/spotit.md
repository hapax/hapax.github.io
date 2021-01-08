---
Layout: post
mathjax: true
comments: true
title:  "Generalising Dobble"
categories: Mathematics
date:  2021-01-07
---

**January 7, 2021.** *I discuss the mathematics of Spot It! (aka
  Dobble in the UK) and various generalisations: projective planes,
  combinatorial designs, and a polytopal turducken.*

#### Introduction

*Spot It!* (called *Dobble* in the UK) is a simple card game
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

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/spotit1.jpg"/>
	</div>
	</figure>

You can play an
[online version](http://thewessens.net/ClassroomApps/Main/intersection.html)
by Ken Wessen.
I like the game, but like many mathematically-minded folk
who encounter it, became increasingly distracted by the question: how does it work?

#### Finite projective planes

The game requires that every two cards share precisely one symbol
in common.
If we add the further constraint that each pair of symbols occurs on
one card only, then we have a nice equivalence to
[finite projective plane](https://en.wikipedia.org/wiki/Projective_plane),
provided we interpret a card as a line and a symbol as a point at
which lines intersect. In particular, our constraints become the
following "axioms":

1. Any two lines (cards) intersect at exactly one point (symbol).
2. Any two points (symbols) are joined by exactly one line (card).

The question then becomes about the existence of a finite projective
plane.
There is a nice constructive approach, which includes
*Spot It!* as a special case, as
[nicely explained](https://math.stackexchange.com/questions/36798/what-is-the-math-behind-the-game-spot-it)
by Yuval Filmus.
Let $p$ be a prime number, and consider the finite field $\mathbb{Z}_p
= \\{0, 1, 2, \ldots, p - 1\\}$, viewed as $p$ nodes on a circle.
(You can generalise to prime power fields, but we'll stick with primes
for simplicity.)
We picture $\mathbb{Z}_p$ for $p = 3, 5, 7$ below:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/spotit2.png"/>
	</div>
	</figure>

To make a projective plane out of $\mathbb{Z}_p$, you do two things:
make it projective and make it a plane.
"Projective" means we add a point at infinity $\infty$,
giving $\mathbb{Z}_p^* := \mathbb{Z}_p \cup \{\infty\}$.
"Plane" means we consider all pairs made from $\mathbb{Z}_p^*$,
subject to the proviso that $(m, \infty) \overset{S}{\sim} (\infty,
m)$, where $S$ is the relation.
Modding out by $S$ leads to the projective plane

$$
\mathcal{P}_p = (\mathbb{Z}_p^* \times \mathbb{Z}_p^*)/S,
$$

with $n = (p+ 1)^2 - p = p^2 + p + 1$ points.
Here are the steps for $p = 3$:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/spotit3.png"/>
	</div>
	</figure>

In the first figure, we add the grey point "at infinity" (which occurs
after $2$).
In the second figure, the $x$ coordinate is given by the
colour of the node and the $y$ coordinate by the colour of the
triangle it lies on.
Note that the coloured points on the grey triangle are equivalent to
the corresponding grey points on the coloured triangle.
A line in this geometry is very similar to a line in the Cartesian
plane, and defined as something with a finite slope and finite
$y$-intercept, or a vertical line with a (possibly infinite)
$x$-intercept:

$$
y = mx + c \text{ or } x = a.
$$

We illustrate for $p = 3$ once more.
Note that for the lines with finite slope and intercept, it's
convenient to use points on the grey triangle, while for the vertical
lines, it's more convenient to use grey points:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/spotit4.png"/>
	</div>
	</figure>
	
For finite slope and intercept, $m, c \in \mathbb{Z}_p$, while $a
\in \mathbb{Z}_p^*$, so the total number of lines is

$$
d = p^2 + p + 1,
$$

precisely the number of points. We might have expected this from the
fact that in the axioms, the role of lines and points are
interchangeable!
*Spot It!* realises this construction for $p = 7$, with $n = 7^2 + 7 +
1 = 57$ symbols. We can now easily draw a picture of the corresponding
projective plane:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/spotit5.png"/>
	</div>
	</figure>

Each card is a line with $p + 1 = 8$ symbols.
For some mysterious reason, the designers removed two cards, so $d =
55$ rather than $57$.
Speculation on the internet is rife, and I remain agnostic.
But ignoring this mutilation, *Spot It!* is really just a projective
plane built out of the finite field $\mathbb{Z}_7$.
I also can't resist sharing the smallest example, $p = 2$, which leads
to a beautiful object called the *Fano plane*.
There is a conventional way of drawing the points which is related to
our method by the following sequence of transformations:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/spotit6.png"/>
	</div>
	</figure>

Draw each row $\mathbb{Z}_2^*$ as a triangle, and nest
them rather than stacking them.
Get rid of the copied points on the grey triangle, then rotate the red
triangle so it hits the outer green triangle with three colours along
each edge.
Now draw all the lines, and you have the Fano plane!
(This construction also works if you have the grey triangle on the
outside and get rid of the grey points.)
Technically, this is a graph of the points, with an edge just in case
they lie on some line together, called the *incidence geometry*.

We'll show below that, for any projective plane,
it must be the case that $n = q^2 + q + 1$ for some number $q$ which
is one less than the number of symbols per card.
It is conjectured that $q$ must be a prime power, which completely
solves the projective plane generalisation of *Spot It!*".
But this construction fixes certain features that strike me as
unnatural.
First, we added the constraint that any pair of symbols appears on
precisely one card.
Why not two, or three, or no constraint at all?
Or dually, why not allow for an overlap of more than one symbol?
The answers won't be projective geometries.
But they may still be interesting!

#### Combinatorial designs

We'll start with constraints on co-occurence.
Consider a deck of $d$ cards, with an alphabet of $n$ symbols, and $k$
symbols per card.
Further, suppose each symbol appears on $r$ cards, and each given pair
of symbols appears in $\lambda$ distinct cards.
This resulting arrangment is called a $2$-$(n, k, \lambda)$
[*combinatorial design*](https://en.wikipedia.org/wiki/Combinatorial_design),
or $2$-design for short.
We don't bother to list $r$ or $b$ since they are determined by the
other parameters according to the equation

$$
dk = nr.
$$

The proof is simply that the LHS counts the total number of symbols
(with multiplicity) by card, and the RHS by symbol.
In general, [Fisher's inequality](https://en.wikipedia.org/wiki/Fisher%27s_inequality)
shows that $d \geq n$.
The restriction to $d = n$ but arbitrary $\lambda$ is called a
[symmetric 2-design](https://en.wikipedia.org/wiki/Block_design#Symmetric_2-designs_(SBIBDs)),
and the projective plane is the special case $\lambda = 1$.
We can say a little more about these symmetric designs.
A basic contraint is that

$$
\lambda (n - 1) = k(k - 1),
$$

since both sides count the total number of pairs (with multiplicity),
divided by $n$, with the LHS counting by co-occurrence of symbols, and
the RHS from cards (using $k = r$ for a symmetric 2-design).
Setting $\lambda = 1$ for the projective plane, and writing $q = k -
1$,

$$
n = k(k - 1) + 1 = q(q+1) + 1 = q^2 + q + 1,
$$

so that the form of $n$ is necessary, and $q + 1$ is one more than the number
of symbols per card.
Finally, you might ask about the $2$ in $2$-design.
It turns out there is a generalisation called a $t$-*design*, where
instead of having every pair appear $\lambda$ times, you have every
$t$-element subset of the alphabet appear on $\lambda$ cards.
I won't say more about them, but just wanted to point out they exist and
constitute an even broader generalisation.

<!-- A more delicate constraint comes from the
[Bruck–Ryser–Chowla theorem](https://en.wikipedia.org/wiki/Bruck%E2%80%93Ryser%E2%80%93Chowla_theorem). -->

#### The polytopal turducken

We'll finish with a somewhat different generalisation.
(By the by, this is the approach/generalisation that occurred to me
before looking up anything to do with projective geometry or designs.
It is therefore much sketchier.)
The basic idea is to have $n$ symbols (labelled $s_i$), $d$ cards, and $k$ symbols per
card as before. We no longer constrain $\lambda$, but instead
introduce a new variable: $c$, the number of symbols any two cards
have in common.
We can formulate this new constraint geometrically.
A card can be viewed as a vector $\mathbf{v} = (v_i) \in
\mathbb{R}^n$, with $i$ corresponding to symbol labels.
We define

$$
v_i = \begin{cases}
1 & \text{$s_i$ is on the card} \\
0 & \text{otherwise}.
\end{cases}
$$

This has various immediate consequences.
First, any card lies in the set $\\{0, 1\\}^n$, the vertices of the
unit hypercube.
Second, if a card $\mathbf{v}$ has $k$ symbols, then

$$
|\mathbf{v}|^2 = \sum_i (v_i)^2 = k.
$$

This means the vector lies on a hypersphere of radius $\sqrt{k}$
centred at the origin.
Finally, let $V = \{\mathbf{v}^{(a)}\}$ be a set of $d$ cards with $c$
symbols pairwise in common.
Then for any $j \neq k$,

$$
\mathbf{v}^{(a)} \cdot \mathbf{v}^{(b)} = \sum_i v^{(a)}_i v^{(b)}_i = c \quad \Longrightarrow
\quad \cos \theta_{ab} = \frac{\mathbf{v}^{(a)} \cdot \mathbf{v}^{(b)}}{|\mathbf{v}^{(a)}||\mathbf{v}^{(b)}|} = \frac{c}{k}.
$$

Thus, $V$ is a set of vectors which (a) are vertices of the unit
hypercube; (b) lie on the hypersphere of radius $\sqrt{k}$, centred at the origin; and (c) form
the vertices of a regular
$(d-1)$-[simplex](https://en.wikipedia.org/wiki/Simplex), since any
pair of vectors is separated by a constant angle
$\cos^{-1}(c/k)$. I call this a "polytopal turducken" since it
involves a pleasing nesting of the three simplest higher-dimensional
polytopes.

#### Resources

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

<!-- https://pdf.sciencedirectassets.com/271586/1-s2.0-S0024379500X03801/1-s2.0-0024379595005412/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDCsCZFL1RIWDwXIr0AxI4NCD64GFmKIP%2F9dNvxJvO0cgIgXLj%2FVxK%2FglsxK72%2B80YPJKY4Q%2FyJAMtqJeyy5f67p%2BYqtAMISRADGgwwNTkwMDM1NDY4NjUiDKZXqMoRRsmInCbvayqRA36TlUSdCuQvew0WddLkEB9u8oeBbksZv38RSvlobs%2FtlOB2wiwhl3cSteVqAX2vFjGtCPBm2va7jSpYZf4lf5k2XVnAR7K%2BigdZRGHxzMW8Ol6MFGuWtKmbWZQIOZrqRQOT4z%2B4op8liXdTfX91PJgOeAHFasNa8Mb5Csi0gFvppW2lGH%2BT2epj4%2FklD5FMpm6X0ORb23nmdiNvKh6JB8USI1PaTJiSu6ayo3kZV%2FeOVFayxz65urkf35pOAEs%2FmXNSkQ9A2svDA79zxP%2Bo5lJiA36jwsxrfwBIEnXUhfqQ4VboqiuqLZhdigJ046yPwDfL1WnuWkWbqvIXusNMhhzHBIGkL4oaSgD24xKSdJ3hon35HvweCgrcn%2FQs3TLVe3Y%2Fsfo4tNiJtgPLe39XkCdRIjtjcWPbaZ7OF0JK2DyyfQ80LEEBZZ43BEq%2FMJ6kY0il5NowQbo7J42yrTEAUvOi0ZeCUHLi%2B%2F1ol868zsGsHgQVVYrOmGkn9YSjyX9ZLVBxqzxHncWrJLdxZgP3mJ9gMPPV3P8FOusBdzPNBunkwIOcrmyQBbn69McYEJ2kp6Ma5mILsUb92CNyS73w1EshKZBIyCcFqaIG7uA0GFUuSwmzduhtpwvK660lClDbCpIjdWrtPoXnn3YTAL8tAAxEXnqGXbgScaQYD5yf0m6t3qtitlsoEBuuIteuu89dnJ11jh4xExf%2F4fohtfNuJNbvKagNy0zAMWfULceUwGAhcCqiQWhhHRMsyl0KJfvC9Wy85SINd75bhJVl90MqxDzrGjj4mrl9jSowyBILE3yuiqk%2B36U0PVp9ggheMXJNDhhxhyJjbSJ0dE%2B%2BPmglaadaVrJXDg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210107T154329Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYVD553ENZ%2F20210107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=8c72206e548bf3a7bcec46225c55b9d0ce9787b4125af8c469d6af080fbe1ad6&hash=ee4495fbf323769a50ac27b637d461bd4b2e62c8e116b8b8bdbf12347a95097b&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=0024379595005412&tid=spdf-bc20f7c8-3bc7-4444-84d5-0749022f920a&sid=843398ad85237746f73b2f56238ef7c30b60gxrqa&type=client -->
