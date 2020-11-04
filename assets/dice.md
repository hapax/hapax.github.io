---
Layout: post
mathjax: true
comments: true
title:  "Asymmetric dice cannot be fair"
categories: [Mathematics, Physics, Statistics]
date:  2020-11-03
---

**November 3, 2020.** *If a dice is symmetric, we can ignore the
  mechanics of rolling in analysing fairness. But if the dice is
  asymmetric, the mechanics become important, and fairness depends on
  how fast you roll! We'll analyse a relatively simple 2d example, and
  show how to "dynamically load" fair dice.*

#### Introduction

If a dice is made of homogenous material, it's easy to ensure it's
fair: simply pick a shape where the sides are indistinguishable,
or in technical language, *isohedral*.
Then it is as likely to land on one side as any other, since you
have no way of telling them apart if you remove the numbers.
The simplest example are the Platonic solids, where not only the faces
but the vertices are indistinguishable. These have 4 (tetrahedron), 6
(cube), 8 (octahedron), 12 (icosahedron) and 20 (dodecahedron) sides
respectively.
There is a more general class of a isohedral shapes which are not
symmetric between vertices, called the *Catalan solids*, but I won't
describe them here.

It's clear that, however you roll the dice, as long as the way it
lands or *impact parameter* is random, the probability distribution
should be uniform.
There is no way to bias towards a face if all the faces are the same.
But what if the faces are different?
In this case, as we will see, *the probability distribution depends on
how you roll*.
This leads to a notion of "dynamic loading": a dice which is fair in
some regime can be loaded by rolling it differently.
This gives us another, very strong reason to prefer symmetry dice.

#### Dice in two dimensions

We're going to focus on a simple setup where everything can be done
reasonably explicitly: a two-dimensional dice.
We will ignore its translational motion, the additional complications
of frictions, etc, and focus on the key mechanism of the roll,
*angular momentum*.
In more detail, suppose we have a convex polygon of $n$ sides.
It has some varying density, and because it is convex, the centre of
mass $C$ is inside the polygon.
(Hopefully this is intuitive; to get it to fall outside the shape, one
needs some non-convex "wings".)

We will need some further parameters.
Let us label the corners $c_i$ and faces $f_i$ anticlockwise, $i = 1,
\ldots, n$, with $f_i$ between $c_i$ and $c_{i+1}$.
Each corner is a distance $d_i$ from the centre of mass, and each face
subtends a *face angle* $\alpha_i$, as well as a left corner angle
$\beta_i$, defined in the figure.

When the dice is rolled, the roller imparts some angular momentum
$L = \omega I$ around the centre of mass, where $I$ is the moment of
inertia and $\omega the angular velocity$.
We will assume that when the dice falls, it lands at some random,
uniformly chosen angle around $C$.
It will almost certainly land on a corner, and then roll one or more
times so it sits on a face.
We are going to ignore linear motion, and focus
only on the effects of angular momentum on the probability
distribution.
Finally, we assume that the result of the throw is that face it lands on.

#### Slow fairness

To begin with, let's suppose that $\omega = 0$.
The dice simply falls down at some random, uniformly chosen angle
around the centre of mass, and tilts over to lie on the closest side.
If the angle falls within the angle $\phi_i$ subtended by face $f_i$,
it will fall onto this face.
Thus, the probability of obtaining this face is

$$
p_i^\text{slow} = \frac{\alpha_i}{2\pi}.
$$

The probabilities $p_i^\text{slow}$ remain a good
approximation to the probability distribution when the dice are rolled
very slowly (we will explain how slow below), so the chance of tipping
over due to angular momentum is low.
We say that a dice obeys a *slow fairness* condition if this
probability distribution is uniform, or

$$
\alpha_i = \frac{2\pi}{n}.
$$

The faces of a slowly fair dice subtend equal angles.
Incidentally, this does not mean faces have the same areas!
But a comparatively large face, subtending the same angle, means the
centre of mass is closer to the short sides.
The smaller area is compensated for by the concentration of mass.

#### The flip barrier

Let us now take the opposite limit where the angular momentum is very
high (we will say how high, parametrically speaking, in the next
section).
In order to analyse this, let's analyse how much energy it takes to
flip the dice from face $f_i$ to $f_{i-1}$, supposing it rolls clockwise.
The centre of mass sits at a height

$$
h_i = d_i cos \beta_i.
$$

In order to roll over to $f_{i-1}$, it needs to be raised to a height
$d_i$, so the dice is standing on the corner with the line from $C$ to
$c_i$ vertical. The height difference is then

$$
\delta h_i = d_i(1 - \cos\beta_i).
$$

If the dice has mass $m$, the corresponding change in gravitational
potential energy is

$$
\Delta U = mg \Delta h_i = mg d_i(1 - \cos\beta_i).
$$

This energy will be supplied in the form of rotational kinetic energy
by the roller.
If the dice has angular velocity $\omega$ around the centre of mass,
and hits at corner $c_i$ without slipping, it now pivots around the
corner.
The moment of inertia is (via the parallel axis therem)
