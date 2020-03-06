---
Layout: post
mathjax: true
comments: true
title:  "A Hacker's Guide to Minkowski Spacetime"
categories: [Physics, Teaching, Hacks]
date:  2020-03-??
---

**March ?, 2020.** *Stuff*

### Contents

1. <a href="#sec-1">The world according to Pythagoras</a>
   1. <a href="#sec-1-1">The parable of the surveyors</a>
   2. <a href="#sec-1-2">The parable of the merchants</a>
   3. <a href="#sec-1-3">Length on a blob</a> 
2. <a href="#sec-2">The world according to Minkowski</a>
   1. <a href="#sec-2-1">Einstein's proposal</a>

## 1. The world according to Pythagoras  <a id="sec-1" name="sec-1"></a>

In this post, we're going to be learning some basic lessons about
spacetime, starting with the principle of relativity, exploring the
twin paradox, and ending with some insights into gravity and black
holes.

### 1.1. The parable of the surveyors <a id="sec-1-1" name="sec-1-1"></a>

I like to imagine that, a thousand years before Pythagoras, Babylonian
surveyors trying to measure out parcels of land discovered a curious
fact.
For two measuring sticks at right angles, and measurements $\Delta x$
and $\Delta y$ as shown below, they found that a particular
combination $\Delta x^2 + \Delta y^2$ never changed, however they
oriented their sticks.
In other words,

---

<span style="padding-left: 20px; display:block">
*The quantity $\Delta x^2 + \Delta y^2$ doesn't depend on how measuring
sticks are oriented.
</span>

---

We'll define the *Pythagorean length* $\ell_\text{P}$ by
$\ell_\mathcal{P}^2 = \Delta x^2 + \Delta y^2$.

This is an empirical rather than a mathematical fact.
This may be surprising, given that Pythagoras' theorem, $a^2 + b^2 =
c^2$, is perhaps the one mathematical fact that everyone knows!
Here is a quick visual proof:

But this proof only works on a flat, two-dimensional plane.
We can explain the empirical observation that $\Delta x^2 + \Delta
y^2$ by assuming that the world looks like our model.

We now imagine that two Babylonian surveyors measure the same length
of fence, but with differently-oriented measuring sticks.
For simplicity, let's assume that the stick systems are identical, and
all meet at a point, as well with one end of the fence.

The first surveyor takes a pair of measurements $(x, y)$, while the
second surveyor takes $(x', y')$.
Given that the Pythagorean length is the same, how are these two sets of measurements related?
It will depend on the relative orientation, so we need a way to gauge
this.
Here is a simple and familiar option.
We rotate one measuring-stick system into the other, and trace out the
end of one stick with a piece of string.
If the length of the string is $d_1$, and the length of the stick is
$d_2$, then we can define the "relative orientation parameter"

$$
\theta = \frac{d_1}{d_2}.
$$

Of course, this is just an elaborate way to describe the *angle*,
measured in radians.
In fact, we can choose a system of units where $d_2 = 1$, in other
words, the stick has unit length.
As we rotate the stick through a full revolution, we can label the
endpoints as a function of $\theta$:

$$
x(\theta) = \cos(\theta), \quad y(\theta) = \sin(\theta).
$$

Since the Pythagorean length of the stick is $1$, these two functions
obey, for any value of $\theta$,

$$
1 = \ell_{\text{P}}^2 = x^2 + y^2 = \cos^2(\theta)+\sin^2(\theta).
$$

With these tools in hand, we can finally determine how the
measurements $(x, y)$ and $(x', y')$ are related.
I claim that if we rotate through $\theta$, they are related by

$$
x' = x \cos(\theta) + y \sin(\theta), \quad y' = -x \sin(\theta) + y \cos(\theta).
$$

The picture makes this clear, but we can also check that the
Pythagorean length is unchanged:

$$
\begin{align*}
(x')^2 + (y')^2 & = \left[x \cos(\theta) + y \sin(\theta)\right]^2 +
\left[-x \sin(\theta) + y \cos(\theta)\right]^2 \\
	& = x^2 \left[\cos^2(\theta) + \sin^2(\theta)\right] + y^2
	\left[\sin^2(\theta) + \cos^2(\theta)\right] + 2xy
	\left[\cos(\theta)\sin(\theta)-\sin(\theta)\theta(\theta)\right]\\
	& = x^2 \cdot 1 + y^2 \cdot 1 + 2xy \cdot 0 \\
	& = x^2 + y^2.
\end{align*}
$$

Let's summarise the story so far.
Surveyors observe that $\Delta x^2 + \Delta y^2$ is unchanged, however
they choose to orient their measuring sticks.
This suggests that the land they measure is a flat plane, since in
this, they can prove the result is true.
Finally, by thinking more carefully about how to define relative
orientation, they can figure out precisely how measurements using
different measuring-stick systems are related.
This may seem like a pedantic and overly-elaborate way to describe
plane geometry, but it will pay off when we come to study spacetime.

### 1.2. The parable of the merchants <a id="sec-1-2" name="sec-1-2"></a>

We can imagine that, as experts on length, Babylonian 
To make things more concrete, suppose you can take a direct,
straight-line path from home $A$ to school $B$.
But you can also take a route which stops at the candy store $C$ in
between.
Let's use $AB$ for the length of the route from $A$ to $B$, and so on.

Now, which route is shorter, the direct route or the side trip to the
candy store?
Clearly, the direct route unless the candy store was already on the way.
Although it's obvious, let's prove it using circles.
For convenience, orient the rulers so that home $A$ is at the origin
and school $B$ is on the vertical ruler.
Draw circles from $A$ and $B$ which pass through the candy store $C$.
This lets us compare the length $AB$ of the direct route to the
lengths $AC, BC$ when you have the side trip.

The circles overlap with some length $d$, in which case

$$
AC + BC = AB + d.
$$

It's clear geometrically that $d$ is always non-negative, so that $AB
\leq AC + BC$, and $d = 0$ just in case the candy store lies directly
between home and school.

Now, imagine visiting a sequence of $n$ candy stores, $C_1, C_2,
\ldots, C_n$.
How do multiple side trips compare to the direct route?
If we visit candy stores in order, the total length is

$$
AC_1 + C_1C_2 + \cdots C_{n-1}C_n + C_nB.
$$

Could these trips conspire to somehow become shorter than the direct
route?
Of course not.
A simple way to see this is just to use what we already know!
We can make the trip from $A$ to $C_2$ shorter, for instance, by
eliminating a stop at $C_1$:

$$
AC_1 + C_1C_2 \leq AC_2.
$$

Then we can get rid of the stop at $C_2$, then the stop at $C_3$, and
so on, until we have no candy stores left.
We learn that

$$
AC_1 + C_1C_2 + \cdots C_{n-1}C_n + C_nB  \leq \cdots \leq AB.
$$

The extreme case is to imagine a *continuous* path, which consists of
infinitely many candy stores.
I won't prove it formally, but I hope it's clear that such a path
is always at least as long as the direct, straight-line route, simply
by taking the limit $n \to \infty$ in the argument above.
We can formulate what we've learned as a simple rule:

---

<span style="padding-left: 20px; display:block">
Any departure from the direct route increases total trip length.
</span>

---

If you're in a hurry (or a dental hygiene enthusiast), don't go to
the candy store!

### 1.3. Length on a blob<a id="sec-1-3" name="sec-1-3"></a>

Our observations about candy store visits are sort of obvious, and
seemed confined to a flat, two-dimensional plane.
But the benefit of stating them in an odd way is that we can easily
generalise to more interesting situations.
First, we will think about trip-planning in higher dimensions.
Then we will understand shortest routes in *curved* spaces.

#### Higher dimensions

First, let's imagine that our destinations are located in
three-dimensional, rather than two-dimensional, space.
The extension actually works for higher dimensions, but we'll stick to
three for ease of visualisation.

As before, I want to compare a direct route from $A$ to $B$ to the
route via the candy store $C$.
In two dimensions, we drew circles, but in three dimensions, the set
of points at a fixed distance from $A$ or $B$ is a *sphere*. So it
seems like we'll have to draw some complicated picture with spheres.
Thankfully, this is unecessary!
We can simply *work in the plane containing $A$, $B$ and $C$*.
Three points are always contained in a plane, so this is a reasonable
thing to do.
We then draw circles, and the argument above goes through, word for
word.

Since our result for multiple candy stores (including infinitely
many!) simply iterated the result for a *single* candy store, we can
do the same iteration here.
The quickest route between $A$ and $B$ in three (or indeed any number
of) dimensions is the direct route, and any additional stops make it longer.

#### Blobs

In the situations we've considered so far, we've needed to be able to
draw straight lines between $A$, $B$ and $C$.
But more generally, we can imagine working on a *curved* surface that
does not allow us to draw these lines.
A simple example is the surface of the globe, where a truly straight
line goes through the earth!
If we are confined to move on the surface, then the shortest path is
not a straight line after all.
Can we say anything interesting about this scenario?

The first thing to say is that the earth *looks* flat at the human
scale.
When I walk down the street, it's not obvious the earth is curved, and
this explains (in part) why flat-earthers are able to persist in their
error.
In general, a suitably small patch of a curved surface looks flat.
Though it's harder to imagine, a three-dimensional (or
higher-dimensional) space can also be curved, but once again, in a
small patch, straight lines will make sense.
We'll call curved spaces *blobs*, and use the term *local* to refer to
the small patches where the blob looks flat, and straight lines make sense.
Then, in a slogan,

---

<span style="padding-left: 20px; display:block">
Blobs are locally flat.
</span>

---

With a little more work, we can exploit this slogan to describe
shortest routes on a blob.
So, consider the shortest route between $A$ and $B$ in a blob.
This may not be a straight line, since in general, straight line
routes aren't allowed, or even defined.
Let's list a bunch of intermediate locations visited by this shortest
route from $A$ to $B$, say $D_1, D_2, \ldots, D_n$, in the order they
are visited.
We make another simple observation: the shortest route between $A$ and
$B$ will *also* gives the shortest route between the intermediate
locations!
If it didn't, and took a winding detour from say $D_2$ to $D_3$, we
could always replace this section of the path with a shorter route and
reduce the overall length.

Let's pick many, many points $D_i$, and place them close enough
together that every pair of successive points $D_i$ and $D_{i+1}$ is
contained in a flat-looking patch.
The shortest path from $A$ to $B$ also gives the shortest path between
each pair $D_i$ and $D_{i+1}$, and the shortest path, locally, is just
a straight line.
We've just discovered an important result about blobs:

---

<span style="padding-left: 20px; display:block">
Shortest paths are locally straight. Departures from local straightness increase length.
</span>

---

In mathematics, these blobs are called *Riemannian manifolds*, and
locally straight paths are called *geodesics*.
So we've just proved that, on a Riemannian manifold, the shortest path
between $A$ and $B$ is a geodesic.
Sounds very impressive!

Even though a blob doesn't usually have a single straight line
connecting $A$ and $B$, we can use *locally* straight paths to define
distance.
As you might expect, it's just the sum of the lengths of small line
segments making up the path:

$$
d_\text{P}(A, B) = AD_1 + D_2D_3 + \cdots D_{n-1}D_n + D_nB.
$$

So, we have defined Pythagorean length in a blob!

## 2. The world according to Minkowski <a id="sec-2" name="sec-2"></a>

In Newtonian physics, time and space are completely separate.
In Newton's own and beautiful words:

<span style="padding-left: 20px; display:block">
*Absolute, true and mathematical time, of itself, and from its own
nature, flows equably without relation to anything external.*
</span>

We can rotate between different spatial directions, but we can never
rotate space into time.
This was the official view until Einstein came along, $200$ years
later.
Although Einstein's insights about spacetime are brilliant and revolutionary, we can
present some of them in a way that clearly parallels the situation for
space.
This is why we bothered to describe the world according to Pythagoras!

### 2.1. Einstein's proposal <a id="sec-2-1" name="sec-2-1"></a>

Sound has a speed of $c_S \approx 300 \text{ m/s}$, but only relative
to its medium, the air.
If you move with respect to the air, the
speed of sound will appear to change.
In the 19th century, physicists imagined that a similar situation held for
light. Instead of air, they thought that light propagated in an
invisible substance called "aether".

The study of the aether was hampered by the extreme velocity of light, but
eventually, Albert Michelson and Edward Morley devised a
clever experiment to detect the earth's motion through the aether.
The basic idea was to split up a beam of light on a turntable, send
the beams in different directions, recombine them, and look for the
interference effects that would arise from the different speed of light in
different directions.
This clever and very precise experiment saw *nothing*.
Either that the earth wasn't moving through the aether
(unlikely) or the experiment was insufficiently sensitive.
But Einstein had an even more radical proposal: the aether didn't
exist at all!

Even before the Michelson-Morley experiment, Einstein had come to
doubt the existence of the aether. His reason was simple. The equations
of electromagnetism did not include any reference to aether, and made
a single prediction for the speed of light, $c = 3 \times 10^8 \text{ m/s}$.
This naively suggested that the speed of light was *the same* in any set of
coordinates moving at a constant speed.
This is important enough to state again:

---

<span style="padding-left: 20px; display:block">
The speed of light is the same in all reference frames moving at
constant speed.
</span>

---

As a true believer in the elegance and sufficiency of the laws of
electromagnetism, Einstein decided that this naive proposal was correct.
We will explore the remarkable consequences of this simple idea.

Recall that length is unchanged by rotation, and in particular, rotation of rulers.
Similarly, if Einstein's proposal is true, the speed of light is
unchanged by taking a ruler-clock system (for measuring position and
time) and changing its velocity.
In general, we call the process of imparting velocity to a
ruler-clock system a *boost*.

### Xtra

When you rotate a stick, it doesn't magically change length,
right?
In fact, you can think of this as a *definition* of length: it
is the thing that doesn't change under rotations.
This just seems to be a basic physical fact about the universe.
Here is a setup for measuring sticks.
Take two identical rulers and put them at right angles.
Call measurement along the first ruler called $\Delta x$, and the
measurement along the second ruler $\Delta y$.
We picture this below:

You find that, no matter how you orient the stick, these two
measurements obey

The constant $\ell$ is the length of the ruler, and this result is of course
just Pythagoras' theorem.
But it is telling us an important fact:

---

<span style="padding-left: 20px; display:block">
The quantity $\Delta x^2 + \Delta y^2$ is preserved by rotations.
</span>

---

When we place the end of the stick at the point the rulers meet (the "origin"), this
becomes $x^2 + y^2$, and the equation $x^2 + y^2 = \ell^2$ describes a
circle of radius $\ell$.
Of course, this has to be the case, since geometrically speaking, this
equation describes what happens when you rotate a stick of length
$\ell$ with one end fixed.

There is a convenient way of referring to rotations using circles.
Imagine a stick of unit length, $\ell = 1$, revolved around the point
our rulers meet, so it obeys

$$
x^2 + y^2 = 1.
$$

For some rotation, use a tape measure to find the length of the arc
from the $x$ ruler to the end of the stick, and call this length
$\theta$.
This is the angle measured in *radians*, rather than degrees.
We can view $x(\theta)$ and $y(\theta)$ as functions of $\theta$, and
give them special names:

$$
x(\theta) = \cos(\theta), \quad y(\theta) = \sin(\theta).
$$

It follows immediately, just from the way we've defined things, that

$$
\cos^2(\theta) + \sin^2(\theta) = 1.
$$

For a circle of radius $\ell$, we can still refer to angles using
$\theta$ --- we just choose a ruler for which the circle has unit
radius, and measure $\theta$ as before.
Returning to the original ruler, where the circle has radius
$\ell$, we will find that

$$
x(\theta) = \ell \cos (\theta), \quad y(\theta) = \ell \sin (\theta),
$$

and we can check, from our earlier observation about cos and sin, that
$x^2 + y^2 = \ell^2$.

The point of having a nice way to discuss rotations is not so much
because we want to rotate sticks.
Rather, we want to *rotate rulers*.
Imagine that I have some measurements $(x, y)$ on my pair of rulers.
Now, you have a second pair of rulers which meet at the same point,
but are rotated through some angle $\theta$.
Then your measurements, call them $(x', y')$, will be related to mine
as follows:

$$
x' = x \cos(\theta) + y \sin(\theta), \quad y' = -x \sin(\theta) + y \cos(\theta).
$$

Length is indeed unchanged when we rotate rulers:

$$
\begin{align*}
(x')^2 + (y')^2 & = \left[x \cos(\theta) + y \sin(\theta)\right]^2 +
\left[-x \sin(\theta) + y \cos(\theta)\right]^2 \\
	& = x^2 \left[\cos^2(\theta) + \sin^2(\theta)\right] + y^2
	\left[\sin^2(\theta) + \cos^2(\theta)\right] + 2xy
	\left[\cos(\theta)\sin(\theta)-\sin(\theta)\theta(\theta)\right]\\
	& = x^2 \cdot 1 + y^2 \cdot 1 + 2xy \cdot 0 \\
	& = x^2 + y^2.
\end{align*}
$$

Let's summarise the story so far.
For physical reasons, rotating something shouldn't change its length.
Pythagoras' theorem tells us that

$$
\Delta x^2 + \Delta y^2
$$

doesn't change under rotations.
Thus, we can define the *Pythagorean length* by

$$
d_\text{P}(\Delta x, \Delta y) = \sqrt{\Delta x^2 + \Delta y^2}.
$$

We can draw circles and define trigonometric functions, and use them
not only to rotate sticks, but to relate measurements between ruler systems.
