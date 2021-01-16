---
Layout: post
mathjax: true
comments: true
title:  "Black holes as quantum computers"
categories: [Philosophy]
date:  2021-01-15
---

**January 16, 2021.** *A tutorial on black holes as
  quantum computers.*

#### Introduction

A black hole is a very special type of quantum computer. In this
tutorial, we'll explore a few properties of these computers using the
tools of
[physics hacking](https://hapax.github.io/physics/teaching/hacks/napkin-hacks/#sec-1). The
prerequisites are very mild: a background in pre-calculus mathematics
and a nodding familiarity with high school physics.

#### System size

A black hole is an object which has collapsed under its own gravity to
form a light-trapping region.
We can estimate how big this region is using a few equations and some
inspired guesswork.
Suppose the black hole has mass $M$.
A running theme will be different ways of estimating the energy stored
in the black hole, and to start with, we invoke the most famous
formula ever:

$$
E = Mc^2,
$$

where $c = 3 \times 10^8 \text{ m/s}$ is the speed of light.
This is how much *mass-energy* the black hole has, according to
Einstein's gem.
Since a black hole is a gravitational object, it also stores
gravitational energy, which we can estimate as

$$
E \sim \frac{GM^2}{R}
$$

where $R$ is the size of the black hole.
This follows immediately from the formula for gravitational
potential, but we can derive it a little more carefully.
First, note that from Newton's law of gravitation, the force the black
hole applies on itself is roughly

$$
F_\text{grav} \sim \frac{GM^2}{R^2},
$$

where $G = 6.67 \times 10^{-11}$ (in SI units) is Newton's constant.
Applying a force over a distance gives energy (work), so we estimate
that

$$
E \sim F_\text{grav} R \sim \frac{GM^2}{R}
$$

as claimed.
Now, if we equate these two forms of energy, we find the famous
*Schwarzschild radius* $R$:

$$
Mc^2 \sim \frac{GM^2}{R} \quad \Longrightarrow \quad R \sim \frac{GM}{c^2}.
$$

This is exactly what we find in general relativity up to a factor of
two, $R = 2GM/c^2$.
Just to give a sense of how small this is, the sun weights $M_\odot = 2
\times 10^{30} \text{ kg}$, so if it collapsed into a black hole, it
would have a Schwarzschild radius of

$$
R = \frac{2GM_\odot}{c^2} = \frac{2(6.67\times 10^{-11})(2 \times
10^{30})}{(3\times 10^8)^2} \text{ m} \approx 3 \text{ km}.
$$

It would fit on the University Endowment Lands of UBC.

#### Let there be heat

Although a black hole traps any light that falls inside, Stephen
Hawking made the remarkable discovery that black holes emit faint
radiation, just like a hot lump of coal.
Once again, we will rather slapdash, and try and work out only the
wavelength of a typical photon coming out of the black hole.
It seems reasonable to assume that, like the fundamental frequency of
a violin or a flute, the black hole likes to make photons with
wavelengths proportional to the Schwarzschild radius $R$.

This has various implications.
Most importantly, the hotter an object is, the smaller the wavelength
of the typical photons it produces.
This explains why a very hot coal is orange or yellow, and becomes red
(a longer wavelength of light) as it cools.
The relationship is governed by something called *Wien's law*:

$$
\lambda \sim \frac{hc}{kT},
$$

where $h = 6.62 \times 10^{-34}$ is Planck's constant,
and $k = 1.38 \times 10^{-23}$ is Boltzmann's constant (both in SI
units).
The key point is that wavelengths get shorter as temperature rises,
and the rest of the constants are added to ensure things make
dimensional sense.
Setting $\lambda = R$ and making $T$ the subject, we obtain the
*Hawking temperature*

$$
T \sim \frac{hc}{kR} \sim \frac{hc^3}{GMk}.
$$

<!-- Max Planck, one of the founding fathers of quantum mechanics, came up
with a general formula for the amount of energy in a photon of
wavelength $\lambda$, $\varepsilon = hc/\lambda$, where $h = 6.62
\times 10^{-34}$ (in SI units).
Then the typical Hawking photon coming out of a black hole has energy
$$
\varepsilon \sim \frac{hc}{R} \sim \frac{hc^3}{GM}.
$$
Not only does the black hole radiate like a hot lump of coal, it does
so for the same reason: it has a temperature!
The relationship between the enery of the photon -->

Once again, we can check what would happen if the sun were a black
hole.
Using our previous result for the Schwarzschild radius, the Hawking
temperature would be

$$
T \sim \frac{(6.62 \times 10^{-34})(3 \times 10^8)}{(1.38 \times
10^{-23})(3000)} \text{ K} = 5 \, \mu\text{K}.
$$

This is millions of times colder than empty space, which has a
temperature of about $3 \text{ K}$.
The black holes in equilibrium with the vacuum have radius around

$$
R \sim \frac{hc}{kT} = \frac{(6.62 \times 10^{-34})(3 \times 10^8)}{(1.38 \times
10^{-23})(3)} \text{ m} = 5 \text{ mm},
$$
<!-- If the sun did collapse to form a black hole, it would get heated up
by the surrounding vacuum.
Since mass gets smaller with temperature, this means it would shrink
dramatically! -->

about the length of an ant.

#### Hard drive size
