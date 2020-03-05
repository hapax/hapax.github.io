---
Layout: post
mathjax: true
comments: true
title:  "From twins to "
categories: [Physics, Teaching, Hacks]
date:  2020-03-??
---

**March ?, 2020.** *Stuff*

### Contents

1. <a href="#sec-1">The world according to Pythagoras</a>
   1. <a href="#sec-1-1">Length and rotation</a>
   2. <a href="#sec-1-2">Zigzags and circles</a>

## 1. The world according to Pythagoras  <a id="sec-1" name="sec-1"></a>

### 1.1. Length and rotation <a id="sec-1-1" name="sec-1-1"></a>

When you rotate a stick, it doesn't magically change length,
right? In fact, you can think of this as a *definition* of length: it
is the thing that doesn't change under rotations.
Here is a setup for measuring sticks.
Take two identical rulers and put them at right angles.
Call measurement along the first ruler called $\Delta x$, and the
measurement along the second ruler $\Delta y$.
We picture this below:

You find that, no matter how you orient the stick, these two
measurements obey

$$
\Delta x^2 + \Delta y^2 = \ell^2,
$$

for some constant $\ell$.
The constant $\ell$ is the length of the ruler, and this result is of course
just Pythagoras' theorem.
But it is telling us an important fact about "Pythagorean length":

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
Great! We now have a nice way to talk about rotations.

### 1.2. Zigzags and circles <a id="sec-1-2" name="sec-1-2"></a>

So far, we've just focused on the length of a single straight stick.
But suppose we line up two sticks, end to end.
Can we say anything interesting about the lengths involved?
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

Now, imagine a whole dental career of candy stores, $C_1, C_2,
\ldots, C_n$.
How do multiple side trips compare to the direct route?
The side trip length is something like

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

Then we can get rid of the stop at $C_2$, then $C_3$, and so on, until
we just have the direct route from $A$ to $B$.
We learn that

$$
AC_1 + C_1C_2 + \cdots C_{n-1}C_n + C_nB  \leq \cdots \leq AB.
$$

The extreme case is to imagine a *continuous* path, which consists of
infinitely many candy stores.
I won't prove it formally, but hopefully it's clear that such a path
is always at least as long as the direct, straight-line route.

---

<span style="padding-left: 20px; display:block">
Any departure from a direct route increases total length.
</span>

---

## Xtra

When you rotate a piece of wood, the length doesn't magically change,
right?
To check this, you can take a ruler and line it up along the wood.
As you rotate both ruler and wood, you'll see that the wood always hits the same mark.
But what if some joker comes along and tells you that rotating not only
changes the wood, but the ruler too!
According to this joker, they stretch by the same factor, so you can never
actually tell from ruling if the length is changed.

How could you refute the joker's claim?
One option is to keep your ruler fixed in place, since if you don't
rotate it, you don't need to worry about length changing.
But now it's hard to measure things unless they line up with the ruler.
To get around this, you can devise a system with two identical rulers,
for convenience placed at right angles.
For a rotated piece of wood, you can take a measurement on each ruler
(see below) and call them $x$ and $y$.
Our goal is to cobble these together to get a length.

We can try lining the wood up with the first ruler.
This gives a measurement of, say, $x = \ell$ and $y = 0$, which we
will write as a pair:

$$
(x, y) = (\ell, 0).
$$

If we line the wood up with the second ruler, then lo and behold, we
get the same answer, but with $x$ and $y$ swapped:

$$
(x, y) = (0, \ell).
$$

It seems like the length really is $\ell$!
But of course it looks that way, the Joker says, laughing, because the second
ruler stretches just so in order to compensate for the change in
length of the wood.

Undeterred, you now place the wood halfway between the two rulers, and
get the measurements

$$
(x, y) = \left(\ell/\sqrt{2}, \ell/\sqrt{2}\right).
$$

This is a funny-looking pair of measurements. After playing around
with it for a bit, you realise that these measurements are related to
the length $\ell$ you found earlier by

$$
x^2 + y^2 = \ell^2.
$$

This is neat, but it could be a coincidence.
You try orienting the wood in different ways, and each time, you find
the same relation holds: $x^2 + y^2 = \ell^2$.
Exhilarated, you confront the Joker with this new result.
The Joker gives you a sly look:

<span style="padding-left: 20px; display:block">
"All you've done is cook up a quantity that doesn't change when you
rotate the piece of wood. That doesn't prove the *length* is unchanged."
</span>

It seems impossible to refute the joker! But after a little thought,
you reply:

<span style="padding-left: 20px; display:block">
"Maybe not. But if that's the case, I don't even know what length is!
We may as well *define it* as the quantity which doesn't change under
rotation."
</span>

The Joker smiles again:

<span style="padding-left: 20px; display:block">
"Good. A notion of length is no different from the transformations which preserve it."
</span>
