---
Layout: post
mathjax: true
comments: true
title:  "Hacking Kepler's problem"
categories: [Physics, Hacks]
date:  2020-10-16
---

**October 16, 2020.** A quick hack for deriving Kepler's first law --- the hard one about ellipses!

#### Kepler's laws

I've always found Kepler's laws a mixed bag. Here they are in their
full glory:

1. The orbit of a planet is an ellipse with the sun at one focus.
2. Planets sweep out equal times in equal areas.
3. The square of the planet's orbital period is proportional to the cube of its semi-major axis.

It's fairly simple to if we specialize the ellipse to a circle.
The focus is the centre, where the sun (when taken to be much heavier
than the planet) sits, and the semi-major axis is just the radius $r$.
Kepler's second law is simply the statement that the planet orbits at
a fixed speed $v$, and the relation between orbital period and orbital
radius implies

$$
T^2 = \left(\frac{2\pi r}{v}\right)^2 \propto \frac{r^2}{v^2} = \frac{r}{a}.
$$

since centripetal acceleration is $a = v^2/r$.
In order for this to be proportional to $r^3$, we need $a \propto
r^{-2}$, which is how Newton arrived at his inverse square law.
As a reminder, Newton's law of gravitation implies

$$
a = \frac{F}{m} = \frac{GM}{r^2}.
$$

So far so good. The messiness comes from the fact that the first law
allows for more mysterious *elliptical* orbits! Where the heck do
these come from? Last night, I was finding it hard to fall asleep and
a sweet hack occurred to me.

#### Angular momentum

As opposed to Newton, who started with Kepler's laws and derived his
from there, we are going to go in the other direction, and use
Newtonian notions to get the ellipses.
First, let's recall the basics of angular momentum.
Suppose an object of mass $m$ is at a distance $r$ from some point, and has an
angular velocity $\omega = d\theta/dt$.
Then the angular momentum $L$ is

$$
L = m \frac{r^2\,  d\theta}{d\t}.
$$

If $L$ is fixed, then in a fixed, small time increment $dt$, $r^2\,
d\theta$ is fixed.
But this is twice the area swept out!


#### The first law
