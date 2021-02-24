---
Layout: post
mathjax: true
comments: true
title:  "Planck atoms"
categories: [Physics, Hacks]
date:  2021-02-23
---

**February 23, 2021.** *Black holes have thermodynamics properties,
  including temperature and entropy. This post provides some quick
  hacks for finding these, similar to dimensional analysis but even
  cheaper.*

#### Introduction

Deriving thermodynamic properties of black holes is hard unless you cheat.
One approach is to use dimensional analysis (see
e.g. [here](https://hapax.github.io/assets/dimensional-analysis.pdf))
but even that can get a bit tedious.
In this post, I'll provide a streamlined, scandalously heuristic approach,
similar in spirit to the way the Hawking temperature can be motivated
by considering virtual particles near the horizon.
Without resorting to dimensional analysis, we can throw around
equations with sneaky abandon, starting with the Schwarzschild radius
and ending with the mysterious formula for Bekenstein-Hawking entropy.

#### Sizing up a black hole

Suppose a star of mass $M$ runs out of nuclear fuel and collapses to
form a black hole.
How big is it?
A running theme in this post will be different ways of estimating the energy stored
in the black hole, and to start with, we invoke the [most famous
formula in physics](https://hapax.github.io/physics/mathematics/hacks/emcc/):

$$
E = Mc^2,
$$

where $c = 3 \times 10^8 \text{ m/s}$ is the speed of light.
This is how much *mass-energy* the black hole has, according to
Einstein's gem.
We will equate this to the gravitational energy stored in the black hole.
Recall Newton's inverse square law of gravity,

$$
F_\text{grav} = \frac{GMm}{r^2},
$$

for masses $M$, $m$ separated by distance $r$, and Newton's constant
$G = 6.67 \times 10^{-11}$ (in SI units).
By setting $m = M$, we can estiamte the force the black hole applies
to itself:

$$
F_\text{grav} \sim \frac{GM^2}{R^2}.
$$

Applying a force over a distance gives energy (work), so we estimate
the gravitational energy stored in the black hole is

$$
E \sim F_\text{grav} R \sim \frac{GM^2}{R}.
$$

If we equate this with mass-energy, we find the famous *Schwarzschild radius* $R$:

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

It would fit inside the LHC!
<!-- It would fit on the University Endowment Lands of UBC.-->

#### Fiat flux

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
\lambda \sim \frac{\hbar c}{kT},
$$

where $\hbar = 1.05 \times 10^{-34}$ is Planck's (reduced) constant,
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
\lambda \sim \frac{\hbar c}{kT} \sim \frac{GM}{c^2}  \quad \Longrightarrow \quad T \sim \frac{\hbar c^3}{GMk}.
$$

One of the weird things about black holes is that temperature is
inversely proportional to mass $M$, as we can see directly here.
As it gets smaller, it gets hotter!
<!-- See the appendix for an astrophysical consequence.-->
Before moving on, let's calculate the temperature of our solar mass
black hole.
Since we already know it has a radius of around $R \sim 3$ km, the
temperature from Wien's law is

$$
T \sim \frac{\hbar c}{kR} = \frac{(1.05 \times 10^{-34})(3 \times
10^8)}{(1.38 \times 10^{-23})(3 \times 10^3)} \text{ K} \sim 10^{-6} \text{ K}.
$$

This is a million times colder than empty space!

#### Atoms of spacetime

We've measured the energy in a black hole using Einstein's mass-energy
formula, and Newton's formula for gravitation.
We've said that a black hole is hot, so let's calculate the energy a
third way, in terms of heat.
People often say that the temperature of the substance measures the
amount of "molecular motion", or kinetic energy per molecule.
This sounds fuzzy, but can be written as a perfectly rigorous
equation called the *equipartition theorem*:

$$
\epsilon_\text{avg} \sim kT \quad \Longrightarrow \quad E \sim N kT,
$$

where $\epsilon_\text{avg}$ is the average energy per particle, and
$N$ is the total number of particles, which we multiply by to get the
total energy $E$.
Basically, hot systems are democratic, and try to spread their energy
evenly between their constituents.
Since we have already estimated the energy in a black hole, we can use
equipartition to estimate the total number of particles. Using the
mass-energy for instance, we have

$$
E = Mc^2 \sim Nk T \sim \frac{Nhc}{R} \quad \Longrightarrow \quad N
\sim \frac{RMc}{\hbar} \sim \frac{R^2c^3}{G\hbar}.
$$

This is a very strange result.
The first thing to notice is that the number of particles is
proportional to $R^2$, and hence the *surface area* $4\pi R^2$ of the
black hole.
Usually, the number of particles is proportional to the *volume* of a
material, not the surface area, so something weird appears to be
happening.
The second interesting thing is that we are dividing the surface area
by a particular combination of constants

$$
A_P = \frac{G \hbar}{c^3}
$$

called the *Planck area*. It is the square of the
Planck length $\ell_P
= \sqrt{G\hbar/c^3}$.
For [various reasons](https://hapax.github.io/physics/hacks/qgrav/),
this can be regarded as the smallest length that makes sense when
quantum effects are taken into account.
For a sun-sized black hole, the number of particles is

$$
N \sim \frac{R^2c^3}{G\hbar} = \frac{(3 \times 10^3)^2(3 \times
10^8)^3}{(6.67 \times 10^{-11}) (1.05 \times 10^{-34})} \sim 10^{76}.
$$

This is a stupendously large number! A typical galaxy is estimated to
have around $10^{67}$ atoms, and a solar mass black hole seems to have
a billion times more. How can a black hole have so many more atoms
than the object it collapses from?
The answer is that the nature of the atom is different!
A black hole is not made from the atoms you find in chemistry
textbooks.
Instead, these are "Planck atoms", which are somehow the indivisible units of spacetime
itself.

#### Bekenstein-Hawking entropy

Of course, this raises the question: what the heck is a spacetime
atom?! We know from chemistry textbooks how regular atoms combine and
create matter. Trying to understand how Planck atoms combine and
create spacetime is much harder! But there are a few demystifying
statements we can make.
Suppose each Planck atom can be in $f$ states.
If there are $N$ Planck atoms in our black hole, then the total number
of configurations (assuming all are allowed) $\Omega$ is

$$
\Omega = f \times f \times \cdots \times f = f^N,
$$

since each atom gets $f$ options.
The *entropy* is just a convenient measure of the number of ways to
be, conveniently defined by
[Ludwig Boltzmann](https://en.wikipedia.org/wiki/Ludwig_Boltzmann) as

$$
S = k \log \Omega =Nk \log f,
$$

where $\log$ is the logarithm to the base $e$.
This is often talked about as a measure of disorder, since there are
fewer ways to be highly ordered than disordered. As an example, if we
now demand that all the Planck atoms have the same state, there are
only $f$ different ways to be!
We can connect this to thermodynamics as follows.
Suppose we change the number of particles by $\Delta N$.
Then by definition, the entropy changes as

$$
\Delta S = k \log f \Delta N.
$$

From the equipartition theorem, the total system energy changes as

$$
\Delta E \sim kT\Delta N.
$$

Keeping the temperature $T$ fixed, and ignoring numbers involving $f$, this yields

$$
\Delta S \sim \frac{\Delta E}{T}.
$$

With a bit more care, this can be turned into a *definition* of
entropy, but the point is that there is the microscopic view (ways to
be) and the macroscopic view (change in energy divided by
temperature).
Either way, the entropy of a black hole is

$$
S \sim Nk \sim \frac{k A}{A_P},
$$

up to numerical constants, where $A = 4\pi R^2$ is the area of the
black hole horizon, and $A_P$ is the Planck area.
This result was suggested by
[Jacob Bekenstein](https://en.wikipedia.org/wiki/Jacob_Bekenstein) in
1973, and corroborated by Hawking's temperature calculation in 1974,
so it's called the *Bekenstein-Hawking entropy*.

<!--

This has a rather interesting astrophysical implication.
It turns out that the universe also glows like a lump of coal, a sort
of afterimage of the Big Bang called the *cosmic microwave background*
(CMB). The "microwave" comes from the fact that the predominant
wavelength is in the microwave band, correspond by Wien's law to a
temperature of around $3 \text{ K}$.
A lump of coal sitting in space will cool down until it reaches this
temperature, at which point it will settle into thermal equilibrium
with the CMB.
The black holes in equilibrium with empty space have a Schwarzschild radius

$$
R \sim \frac{hc}{kT} = \frac{(6.62 \times 10^{-34})(3 \times 10^8)}{(1.38 \times
10^{-23})(3)} \text{ m} = 5 \text{ mm},
$$

about the size of an ant. This raises the question: is the universe
filled with ant-sized black holes?
The answer is no for two reasons.
First, the amount of time it takes for an astrophysical black hole to
reach this stage is many times the age of universe, so black holes
formed from stars just haven't had a chance to reach the ant phase
yet.
But even if there is some other process that allows these ant-sized
black holes to form quickly, their equilibrium with the CMB is
unstable.
To see why, imagine that the ant-sized black hole sneezes, and a
little energy comes out.
By $E = mc^2$, it gets smaller, and hence its temperature increases.
The CMB is now feeding it less energy than it outputs, so it keeps
getting smaller and hotter and quickly vanishes altogether!

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
