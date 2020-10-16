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
3. The square of the orbital period is proportional to the cube of the semi-major axis.

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
these come from? Last night, I was finding it hard to sleep when
a sweet hack for finding them occurred to me.

#### Angular momentum

As opposed to Newton, who started with Kepler's laws and derived his
from there, we are going to go in the other direction, and use
Newtonian notions to get the ellipses.
First, let's recall the basics of angular momentum.
Suppose an object of mass $m$ is at a distance $r$ from some point, and has an
angular velocity $\omega = d\theta/dt$.
Then the angular momentum $L$ is

$$
L = mr^2 \omega = m \frac{r^2\,  d\theta}{d\t}.
$$

If $L$ is fixed, then in a fixed, small time increment $dt$, $r^2\,
d\theta$ is fixed.
But this is half the area swept out!
We simply calculate the area of the corresponding circle at that radius:

$$
A = \pi r^2 \cdot \frac{d\theta}{2\pi} = \frac{1}{2} r^2 \,d\theta.
$$

While $r$ itself can change a little, this contributes a negligible
amount as $dt$ gets small.
Adding all these changes up, we find Kepler's second law: equal areas
are swept out in equal times.
Once again, Newton reasoned to conservation of angular momentum based
on the second law.
We will, instead, assume conservation of angular momentum, which
indeed holds for a central force like gravity.

Let's focus now on figuring out what orbits are allowed by gravity.
The hack involves working with the potential energies, so we first
recall the gravitational potential:

$$
U = -\frac{GMm}{r}.
$$

Angular momentum has a counterpart, rotational kinetic energy:

$$
K = \frac{1}{2}mr^2\omega^2 = \frac{L^2}{2m r^2}.
$$

If $L$ is fixed, both kinetic and potential energies are a function of
$r$, suggesting that life will be simpler if we work with a single
variable.
To capture the contribution of this rotational term, we simply *add
it* to the potential, to get an *effective potential* for the planet
which is a function of $r$ only:

$$
E(r) = K + U = \frac{L^2}{2m r^2} - -\frac{GMm}{r}.
$$

We are now left with *Kepler's problem*: determining what orbits are
allowed for this potential.

#### The first law

Here is the hack:
