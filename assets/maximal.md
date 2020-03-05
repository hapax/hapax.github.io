---
Layout: post
mathjax: true
comments: true
title:  "A Hacker's Guide to the Twin Paradox"
categories: [Physics, Teaching, Hacks]
date:  2020-03-??
---

**March ?, 2020.** *Stuff*

### Contents

1. <a href="#sec-1">The world according to Pythagoras</a>
   1. <a href="#sec-1-1">Length and rotation</a>
   2. <a href="#sec-1-2">A trip to the candy store</a>
   3. <a href="#sec-1-3">Higher-dimensional blobs</a> 

## 1. The world according to Pythagoras  <a id="sec-1" name="sec-1"></a>

Introductory comments?

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

### 1.2. A trip to the candy store <a id="sec-1-2" name="sec-1-2"></a>

So far, we've focused on the length of a single straight stick.
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

### 1.3. Higher-dimensional blobs <a id="sec-1-3" name="sec-1-3"></a>

Our observations about candy store visits are sort of obvious, and
seemed confined to a flat, two-dimensional plane.
But the benefit of stating them the way we did is that we can
generalise to more complicated situations easily.
First, we will think about trip-planning in higher dimensions.
Next, we will understand shortest routes in *curved* spaces.

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
In a slogan,

---

<span style="padding-left: 20px; display:block">
Even in a curved space, straight lines can be defined locally.
</span>

---

With a little more work, we can turn this into a nontrivial result.
The quickest route between $A$ and $B$, even in a blob, *gives the
quickest route between all the intermediate points*.
If it didn't, for instance it gave you a winding detour between two
points $C_1$ and $C_2$, you could shorten the total path by choosing a
shorter path from $C_1$ to $C_2$.
So, let's consider many intermediate points $C_1, C_2, \ldots, C_n$ on
the path from $A$ to $B$.
If we pick enough of these points, we can make successive points close
enough that the blob looks flat!

Then the quickest route between, say, $C_i$ and $C_{i+1}$ will be a
straight line, since this is a locally sensible route.
Zoom in on the shortest route, and it looks straight.
Since this is true for all intermediate points, we arrive at another
important conclusion:

---

<span style="padding-left: 20px; display:block">
On a blob, shortest routes are locally straight.
</span>

---

## Xtra

### Parable

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

### Blobs

A second way we can generalise is to consider *curved* surfaces, and
higher-dimensional versions, all of which I'll call "blobs".
We'll define curvature in a moment, but it's easier to start with an
example: the surface of the globe.
Viewed from the moon, the earth is obviously a sphere, and the surface
is not flat.
But from the human vantage point, it's hard to tell!
(This is one of the reasons flat-earthism is still a thing.)
When I am figuring out the quickest route to school, I don't need to
do a complicated calculation involving spherical geometry.
I just take what looks like a straight-line route, assuming I don't want
candy.

Blobs in general have this property.
When you zoom in on a small patch, it looks flat, and the quickest
route between two points is a straight line.
When you zoom out, straight lines aren't necessarily defined.
On the globe, for instance, the "direct" line goes through the earth!
Instead, to minimise the distance we need to take part of a "great
circle".

But here's a nice observation.
The quickest route between $A$ and $B$, even in a blob, *gives the
quickest route between all the intermediate points*.
If it didn't, for instance it gave you a winding detour between two
points $C_1$ and $C_2$, you could shorten the total path by choosing a
shorter path from $C_1$ to $C_2$.
So, let's consider many intermediate points $C_1, C_2, \ldots, C_n$ on
the path from $A$ to $B$.
If we pick enough of these points, we can make successive points close
enough that the blob looks flat!
Then the quickest route between, say, $C_i$ and $C_{i+1}$ will be a
straight line, since this is a locally sensible route.
Zoom in on the shortest route, and it looks straight.
Since this is true for all intermediate points, we arrive at another
important conclusion:

---

<span style="padding-left: 20px; display:block">
On a blob, shortest routes are locally straight.
</span>

---

Routes with this property have the fancy name of *geodesics*.
