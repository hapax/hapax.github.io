---
Layout: post
mathjax: true
comments: true
title:  "Bekenstein-Hawking on the cheap"
categories: [Physics, Hacks]
date:  2021-02-23
---

**February 23, 2021.** *A black hole is an object which has collapsed
  under its own gravity to form a light-trapping region. Using a few
  equations and some cheap tricks, we arrive at the Bekenstein-Hawking
  law for black hole entropy.*

#### Introduction


#### System size

Suppose the black hole has mass $M$.
A running theme will be different ways of estimating the energy stored
in the black hole, and to start with, we invoke the [most famous
formula in physics](https://hapax.github.io/physics/mathematics/hacks/emcc/):

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
Hawking made the remarkable discovery that just outside the boundary,
black holes emit faint radiation, just like a hot lump of coal.
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
For a motivation from dimensional analysis, see
[this post](https://hapax.github.io/physics/everyday/sky/).
The key point is that wavelengths get shorter as temperature rises,
and the rest of the constants are added to ensure things make
dimensional sense.
Setting $\lambda = R$ and making $T$ the subject, we obtain the
*Hawking temperature* of a black hole:

$$
\lambda \sim \frac{hc}{kT} \sim \frac{GM_\odot}{c^2}  \quad \Longrightarrow \quad T \sim \frac{hc}{kR} \sim \frac{hc^3}{GMk}.
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

<!-- Note that black holes heat up as they get small!
Once again, we can check what would happen if the sun were a black
hole.
Using our previous result for the Schwarzschild radius, the Hawking
temperature would be

$$
T \sim \frac{(6.62 \times 10^{-34})(3 \times 10^8)}{(1.38 \times
10^{-23})(3000)} \text{ K} = 5 \times 10^{-6} \text{ K}.
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

#### Black hole molecules

We've measured the energy in a black hole using Einstein's mass-energy
formula, and Newton's formula for gravitation.
Let's measure the energy a different way, in terms of *heat*.
People often say that the temperature of the substance measures the
amount of "molecular motion", or kinetic energy per molecule.
This sounds fuzzy, but can be written as a perfectly rigorous
equation called the *equipartition theorem*:

$$
E \sim N kT,
$$

where $E$ is the total kinetic energy of molecules, or *heat*, and $N$
is the total number of particles.
We can use this to estimate the total number of "molecules" in a black
hole. Using the mass-energy form for simplicity, we have

$$
E = Mc^2 \sim Nk T \sim \frac{Nhc}{R} \quad \Longrightarrow \quad N
\sim \frac{RMc}{h} \sim \frac{R^2c^3}{Gh}.
$$

This is a strange and remarkable result.
The first thing to notice is that the number of particles is
proportional to $R^2$, and hence the *surface area* $4\pi R^2$ of the
black hole.
Usually, the number of particles is proportional to the *volume* of a
material, not the surface area, so something weird appears to be
happening.
The second interesting thing is that we are dividing the surface area
by a particular combination of constants,

$$
A_P = \frac{Gh}{c^3},
$$

called the *Planck area*.
For various reasons, it can be regarded as the smallest area that
makes sense.
