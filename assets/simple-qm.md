---
Layout: post
mathjax: true
comments: true
title:  "Making light of quantum mechanics"
categories: [Physics, Hacks]
date:  2020-04-30
---

**April 30, 2020.** *Light wobbles up and down in a particular
  direction. From this simple fact, we develop enough quantum quantum
  mechanics to share secrets and build a quantum computer.*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Photons</a>
   1. <a href="#sec-2-1">Polarisers</a>
   2. <a href="#sec-2-2">Stern-Gerlach</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

## 2. Photons <a id="sec-2" name="sec-2"></a>

Classically, light consists of intertwined electric and magnetic
fields, separately wobbling up and down, but at right angles to each
other.
In quantum mechanics, this wave can also be viewed as a particle, the
*photon*.
Thus, a single photon has some plane in which the corresponding
electric field wobbles up and down.
The direction in which the electric field wobbles is the
*polarisation* of the photon.

Let's set up a coordinate system with the $z$-axis coinciding with the
path of the photon, and $x$ and $y$ perpendicular to it.
The polarization makes an angle $\theta$ with respect to the $x$-axis,
as picture below.
We can place the angle on the unit circle in the $x$-$y$ plane, and
recall that the coordinates of the corresponding point are

$$
x = \cos\theta, \quad y = \sin \theta.
$$

A *polariser* is a slit (in real life, a grating) which allows only
certain polarisations to pass through.
Surprisingly, experiments with polarisers that you can do at home
reveal the basic features of quantum mechanics!

### 2.1. Polariser <a id="sec-2-1" name="sec-2-1"></a>

Let's grab a polariser and align it with the $y$ axis at $\theta_y = \pi/2$.
Now a single photon comes along with polarisation $\theta$.
What happens?
A polariser is designed to allow only the polarisation angle
$\theta_y$ through, so it seems reasonable to guess the photon will
be blocked unless $\theta = \pi/2$.
Call this "strong" polarisation.
To check whether polarisers are strong, consider an ordinary beam of
light from flashlight.
This consists of many photons with *random* polarisation angles
$\theta$, and since $\theta$ can be anywhere on the circle, most
photons won't have $\theta = \pi/2$.
If the polariser is strong, most light will be blocked.

You can perform an experiment at home to see if this is true.
Take some polarising sunglasses and shine a flashlight at them.
Is most of the light blocked?
You should find the answer is *no*.
Clearly, polarisers do not act in a "strong" way on photons.

and in fact, if you have a light
meter (or a light meter app on your phone), you can check that the
intensity of light is reduced by around half.

This is the same as saying that the energy carried by the light beam
is reduced by half.
Finally, in a monochromatic beam of light, each photon has the same
energy

### 2.2. Stern-Gerlach <a id="sec-2-2" name="sec-2-2"></a>

#### References

- qm: polarisers/filters, stern-gerlach, superposition, uncertainty,
entanglement, qkd, quantum computing, measurement problem, parallel
universes 
