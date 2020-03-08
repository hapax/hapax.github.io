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

1. <a href="#sec-1">The parable of the surveyors</a>
   1. <a href="#sec-1-1">Rotating rulers</a>
   2. <a href="#sec-1-2">Trip-planning</a>
   3. <a href="#sec-1-3">Over the mountains</a> 
2. <a href="#sec-2">The surveyors of spacetime</a>
   1. <a href="#sec-2-1">Einstein's outrageous proposal</a>
   2. <a href="#sec-2-2">Making rulers into clocks</a>
   3. <a href="#sec-2-3">The Twin Paradox</a>

## 1. The parable of the surveyors <a id="sec-1" name="sec-1"></a>

I like to imagine that, a thousand years before Pythagoras, Mesopotamian
surveyors trying to measure out parcels of land discovered a curious
fact.
For two measuring sticks at right angles, and measurements $\Delta x$
and $\Delta y$ as shown below, they found that a particular
combination $\Delta x^2 + \Delta y^2$ never changed, however they
oriented their sticks.
In other words,

---

<span style="padding-left: 20px; display:block">
Wherever you place your rulers, $\Delta x^2 + \Delta y^2$ is the same.
</span>

---

This quantity is naturally interpreted as *length squared*:

$$
d^2 = \Delta x^2 + \Delta y^2,
$$

so the surveyor's have discovered that length is preserved when we
move our system of measuring sticks.
This is an empirical rather than a mathematical fact!
This may be surprising, given that Pythagoras' theorem, $a^2 + b^2 =
c^2$, is perhaps the one mathematical fact that everyone knows!
And indeed, you can prove it mathematically.

But this proof only works on a flat, two-dimensional plane.
So really, we should view the empirical observation that $\Delta x^2 +
\Delta y^2$ is invariant as evidence that, to good approximation, the
surface of the earth is a flat plane.

### 1.1. Rotating rulers<a id="sec-1-1" name="sec-1-1"></a>

Our two surveyors now measure the same length
of fence, but with differently-oriented measuring sticks.
For simplicity, let's assume that the stick systems are identical, and
all meet at a point, as well with one end of the fence.

The first surveyor takes a pair of measurements $(x, y)$, while the
second surveyor takes $(x', y')$.
Given that

$$
\Delta x^2 + \Delta y^2 = (\Delta x')^2 + (\Delta y')^2,
$$

how are these two sets of measurements related?
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
In fact, we can choose a system of units where $d_2 = 1$, and the stick has unit length.
As we rotate the stick through a full revolution, we can label the
endpoints as a function of $\theta$:

$$
x(\theta) = \cos(\theta), \quad y(\theta) = \sin(\theta).
$$

Since the stick's length is $1$, these two functions
obey, for any value of $\theta$,

$$
1 = d^2 = x^2 + y^2 = \cos^2(\theta)+\sin^2(\theta).
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
	& = (x^2 + y^2) \left[\cos^2(\theta) + \sin^2(\theta)\right] + 2xy
	\left[\cos(\theta)\sin(\theta)-\sin(\theta)\cos(\theta)\right]\\
	& = (x^2+y^2) \cdot 1 + 2xy \cdot 0 \\
	& = x^2 + y^2.
\end{align*}
$$

Let's summarise the story so far.
Surveyors observe that $\Delta x^2 + \Delta y^2$ is unchanged, however
they choose to orient their measuring sticks.
This suggests that the land they measure is a flat plane, since in
this setting, they can prove the result is true from Pythagoras' theorem.
Finally, by thinking more carefully about relative
orientation, they can precisely relate measurements in their
different measuring-stick systems.
This may seem like an odd way to think about plane
geometry, but it will pay off when we come to study spacetime!

### 1.2. Trip-planning <a id="sec-1-2" name="sec-1-2"></a>

We know that Mesopotamian surveyors really did discover Pythagoras'
theorem.
At this point, however, we will depart from the historical record and speculate
about what other discoveries the surveyors *might* have made.

#### A single side trip

Imagine that our two surveyors are commissioned to plan roads between two
Mesopotamian cities, Assur ($A$) and Babylon ($B$).
The first surveyor thinks a straight line between $A$ and $B$ is
shortest, but the second argues that a side trip to Charax Sidae ($C$)
can provide a shortcut.
Without even knowing where these cities are in relation to one
another, the first surveyor can *prove* the straight line is shortest
using their newfound knowledge of circles.

For convenience, they orient measuring sticks so that
Assur $A$ is at the origin and Babylon $B$ on the vertical stick.
The first surveyor then draws circles from $A$ and $B$ which pass through
$C$, using long ropes with ends fixed at $A$ and $B$ respectively.
This lets us compare the length $AB$ (the length of the straight line
from Assur to Babylon) to the lengths $AC, BC$ traversed when you travel via
Charax.
The circles overlap with some length $L$, in which case

$$
AC + BC = AB + L.
$$

It's clear geometrically that $L$ is always non-negative, so that $AB
\leq AC + BC$, and $L = 0$ just in case Charax Sidae lies directly
between Assur and Babylon.

#### Multi-stop trips

The second surveyor has an even crazier suggestion.
Although a single side trip cannot decrease the length, they propose
that a *sequence* of $n$ intermediate stops, $C_1, C_2, \ldots, C_n$,
can conspire to somehow become shorter than the direct
route.
The first surveyor disagrees once more, and argues against the
multi-trip proposal as follows.
If we visit cities in order, the total length is

$$
AC_1 + C_1C_2 + \cdots C_{n-1}C_n + C_nB.
$$

We can make the trip from $A$ to $C_2$ shorter by eliminating a stop
at $C_1$, since we have already established that the direct route
between two locations is shorter than the route with a single side trip.
Thus,

$$
AC_1 + C_1C_2 \leq AC_2.
$$

But once we've eliminated $C_1$, we can repeat this reasoning for $A$
and $C_2$, then $A$ and $C_3$, and so on, until we have no cities left
except for Assur and Babylon.
An extreme version of this is a curved path, which consists of
infinitely many intermediate stops.
I won't prove it formally, but hopefully it's clear that such a path
is always longer than the straight line as well.
Putting it all together, we learn a basic fact about route planning:

---

<span style="padding-left: 20px; display:block">
Any departures from a straight line increase length.
</span>

---

### 1.3. Over the moutains<a id="sec-1-3" name="sec-1-3"></a>

The second surveyor says to the first: "Your reasoning is all well and
good for a completely flat plane, but there are *mountains* between
$A$ and $B$.
It's not a plane at all!
The side trip to $C$ avoids them, and in general, we may have to make *many* departures from a straight
line in order to minimise the actual time taken to travel from $A$ to $B$."
The second surveyor's proposals weren't so crazy after all!
The two surveyors now have a much harder problem before them: what do the shortest
paths between $A$ and $B$ look like when there are mountains?
And how long are these paths?

The surveyors go out into the mountains with some pieces of
glass that allow them to magnify the ground.
They discover an important fact: when you zoom in with a magnifying
glass, even the mountains look flat.
On a small, flat patch of mountain, the first surveyor's reasoning
works, and straight lines gives the shortest distance between two
points.
A *local* property is one that holds when you zoom in enough, and a
*curved* surface is one which isn't flat. So the surveyors have
learned the following important fact:

---

<span style="padding-left: 20px; display:block">
A curved surface is locally flat.
</span>

---

This actually allows them to determine which paths are shortest, and
even how long they are!
To see why, consider the shortest route between $A$ and $B$ on a
curved surface.
Pick any intermediate locations visited on this route, say $C_1, C_2,
\ldots, C_n$, in order of visiting.
Not only does the shortest route tell us how to get from $A$ to $B$ as
quickly as possible, but also tells us the shortest route between
intermediate locations!
If it didn't, and we took an unnecessarily long path from $D_1$ to
$D_2$ for instance, we could always replace this segment of the path
with the shortest route from $D_2$ to $D_3$ and reduce the overall
length.

Let's pick many, many points $D_i$, and place them close enough
together that every pair of successive points $D_i$ and $D_{i+1}$ is
contained in a small, flat patch.
The shortest path from $A$ to $B$ also gives the shortest path between
each pair $D_i$ and $D_{i+1}$, and as the surveyors realised, the
shortest path in flat patch is just a straight line.
This leads to the key result about lengths on curved surfaces:

---

<span style="padding-left: 20px; display:block">
Shortest paths on a curved surface are locally straight.
</span>

---

In mathematics, these locally straight paths are called *geodesics*.
The distance between $A$ and $B$ is just the length of the shortest
path, which as you might expect, is just the sum of the lengths of
small line segments making up the path:

$$
d(A, B) = AD_1 + D_2D_3 + \cdots D_{n-1}D_n + D_nB.
$$

In general, this will only be an *approximation* to the true length,
but we can make the approximation as good as we like by picking more
and more points.
(In the limit of an infinite number of points, the sum becomes an
*integral*, and the length is exact, but we won't worry about these technicalities.)

## 2. The surveyors of spacetime <a id="sec-2" name="sec-2"></a>

In Newtonian physics, time and space are independent.
You can rotate your measuring stick in different directions, but you
can never rotate a measuring stick into a clock!
In Newton's own and beautiful words:

<span style="padding-left: 20px; display:block">
*Absolute, true and mathematical time, of itself, and from its own
nature, flows equably without relation to anything external.*
</span>

This was the official view until Einstein came along, $200$ years
later.
By combining empirical observation and mathematical reasoning, just
like the Mesopotamian surveyors above, which can recover some of Einstein's
radical insights into the nature of spacetime.

### 2.1. Einstein's outrageous proposal<a id="sec-2-1" name="sec-2-1"></a>

The laws of electromagnetism predict that, in vacuum, light travels at
the speed

$$
c = 3.0 \times 10^8 \text{ m/s}.
$$

Most physicists of the 19th century were convinced that light had
to travel through a medium, which they called *aether*, in the same
way that sound travels through air.
If you move relative to the aether, you will measure a different speed
of light.

But the laws of electromagnetism make no mention of the aether, or
relative motion.
Albert Einstein viewed these laws as so beautiful, and self-evidently
complete, that if they made no mention of the aether then none was
required.
Since the earth should move relative to the aether (it executes
circular motion, and the aether presumably does not), Michelson and
Morley were able to devise a clever experiment to detect differences
in the speed of light in different directions.
Famously, they found no difference at all!

But if there is no aether, and no change in the speed of light as we
move at different speeds, we are left with an outrageous proposition:

---

<span style="padding-left: 20px; display:block">
The speed of light is the same in all reference frames.
</span>

---

This smells very similar to the statement that length does not depend
on where we place our measuring sticks.
We can mathematise accordingly!
Instead of two measuring sticks at right angles, we'll measure
length in a single direction with a ruler, and duration with clocks
attached to the ruler.

To calculate the speed of light, we shoot a laser beam along the
ruler, with two points separated by $\Delta x$, and time how long it
takes using the clocks.
Einstein's outrageous proposal is that, provided the ruler is moving
at constant velocity (an *inertial* reference frame), we always find that

$$
c = \frac{\Delta x}{\Delta t}.
$$

To make things simpler, let's choose a system of units in which $c = 1$.
This just corresponds to choosing a scale on the graph below, where a
light ray travels a single horizontal unit of distance in a single
vertical unit of time:

Now, Einstein's proposal can be written

$$
1 = \frac{\Delta x}{\Delta t} \quad \Longrightarrow \quad \Delta x^2 -
\Delta t^2 = 0
$$

for a light ray in any inertial reference frame.
This should remind you of the discovery of the surveyors, namely that
$\Delta x^2 + \Delta y^2$ does not depend on where we put the
measuring sticks.
This suggests a small generalisation of Einstein's outrageous proposal:

---

<span style="padding-left: 20px; display:block">
Whatever the speed of your ruler-clock system, $\Delta x^2 - \Delta t^2$ is the same.
</span>

---

The invariance of $\Delta x^2 + \Delta y^2$ indicates that the surface
of the earth should be modelled as a plane.
The invariance of $\Delta x^2 - \Delta t^2$ corresponds to a model
called *Minkowski spacetime*, whose properties we'll explore now.

### 2.2. Making rulers into clocks<a id="sec-2-2" name="sec-2-2"></a>

Just as two surveyors measuring the same length of fence may want to
relate their measurements, two spacetime surveyors measuring times and
distances may wish to relate their measurements.
Our strategy will be very similar to rotations, where we started by
giving special names to points on the unit circle,

$$
x^2 + y^2 = 1.
$$

Instead, we're going to label points on the *unit hyperbola*,

$$
t^2 - x^2 = 1.
$$

As on the unit circle, we're going to parameterise 

### 2.3. The Twin Paradox<a id="sec-2-3" name="sec-2-3"></a>

### Xtra

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
of) dimensions is the direct route, and any additional stops make it
longer.

#### Other

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
