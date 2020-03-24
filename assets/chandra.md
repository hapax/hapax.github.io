---
Layout: post
mathjax: true
comments: true
title:  "White dwarfs and black holes"
categories: [Physics, Hacks]
date:  2020-03-23
---

**March 23, 2020.** *If you throw too many electrons into a box, it
  collapses under its own weight to form a black hole. But how many is
  too many? We will hack our way towards an order-of-magnitude
  estimate, and comment on the implications for astrophysics.*

## Introduction <a id="sec-1" name="sec-1"></a>

Though they differ in size by many orders of magnitude, the solar
system and the atom are not so different.
Both involve smaller bodies (electrons/planets) orbiting a much
larger body (nucleus/sun) under the influence of a
central force (electrostatics/gravity).
Orbits also have finite occupancy.
Part of the definition of a planet is that it "clears its
neighbourhood" of any interlopers.
(*Sic transit gloria Pluto.*)
Electrons automatically clear their orbitals by
the *Pauli exclusion principle*, a point we will return to below.

That's where the resemblance ends.
The solar system is classical, and planets can orbit the sun at any
old radius they like.
In contrast, atoms obey quantum mechanics, and the orbits are
*quantised*, occuring only at certain allowed values
Quantisation has tremendous consequences for atomic physics,
hence chemistry, hence life itself.
We're made out of exploded stars, sure, but we're also made from
quantum mechanics.

Quantisation not only governs the heavy elements ejected
from stars, but the degenerate remnants left behind.
Surprisingly, we can model these leftovers by throwing electrons into a box.
Throw in too many electrons, and the box collapses to form a black hole.
With some dimensional analysis and hand-waving, we can turn this into
an upper bound on the mass of remnant stars called the
*Chandrasekhar limit*, after
[Subrahmanyan Chandrasekhar](https://en.wikipedia.org/wiki/Subrahmanyan_Chandrasekhar).

<span style="padding-left: 20px; display:block">
What is intelligible is also beautiful.
</span>

<div style="text-align: right"><i>Subrahmanyan Chandrasekhar</i> </div>

## Quantum box<a id="sec-2" name="sec-2"></a>

### General setup<a id="sec-2-0" name="sec-2-0"></a>

We say that energy is *quantized*.
A familiar example is the atom, where the various shells --- s, p, d, f, and so on --- are successively populated as the atomic number gets larger.
The structure of these levels is complicated, and the electrons in an atom can also interact.

We will consider a simpler scenario called a *non-interacting quantum gas*.
As in the atom, there is a possibly infinite set of allowed energies:

$$
E_1 \leq E_2 \leq E_3 \leq \cdots
$$

However, particles occupying these energy levels do not interact.
It's like a hotel: guests can only stay in designated rooms, which are arranged by price, and do not want to be disturbed by other guests.
To finish describing our gas, we need two more elements.

- *Temperature.* This corresponds to how *cheap* hotel guests are. At zero temperature, they will take the cheapest available room, i.e. the lowest available energy level in the gas. At nonzero temperature, there is some probability they will splash out on a fancy suite, but the more expensive, the less likely it is.
- *Type.* Particles fall into two categories: *bosons* and *fermions*. Bosons are sociable, and arbitrarily many can stay in a single hotel room.
Fermions, on the other hand, are loners, obeying the *Pauli exclusion
principle*: one particle per room!

Let's explore a few immediate consequences for our quantum gas hotel.
For the moment, assume that energy levels *strictly increase*, $E_1 < E_2 < \cdots$, and that the gas is at zero temperature (particles take cheapest available room).

1. Suppose that $N$ bosons arrive at the hotel. Where do they stay? 
2. Suppose that, instead, $N$ fermions come to the hotel.  Which rooms do they occupy?

### One-dimensional box <a id="sec-2-1" name="sec-2-1"></a>

Our ultimate goal will be to study white dwarfs, but as a simple warm-up, consider a one-dimensional "box" of size $L$.
This will give us some feeling for the structure of energy levels.
A quantum particle can be described by a standing *matter wave* in the box, similar to plucking a string with fixed ends.
Suppose that, like the string, the waves are "clamped" at the ends.
(If we square the amplitude of the matter wave at a point, we get the probability of finding the particle there. So we are stating that we never find the particle at the edges of the box.)
What are the allowed wavelengths $\lambda_n$?

For a (classical) particle of momentum $p$ and mass $m$, show the kinetic energy can be written

$$
E = \frac{p^2}{2m}.
$$

In 1924, Louis de Broglie guessed that matter waves had an associated momentum,

$$
p = \frac{2\pi \hbar}{\lambda},
$$

where $\hbar = 10^{-34} \text{ J s}$ is \emph{Planck's (reduced) constant}.
Assuming the energy of the quantum particle is kinetic, and the previous question applies, deduce that the energy levels in the box are

$$
E_n = \frac{8\pi^2 \hbar^2n^2}{mL^2}.
$$

Throw $N$ non-interacting fermions into the box at zero temperature.
The energy of the highest occupied level is called the *Fermi energy* $E_F$, and there is an associated *Fermi temperature* $T_F = E_F/k_B$, where

$$
k_B = 1.4\times 10^{-23} \frac{\text{ m}^2\text{ kg}}{\text{ K s}^2}
$$

is Boltzmann's constant.
Assuming the ideal gas law holds in the form $PV \sim Nk_BT_F$, deduce that the gas in the box has a *degeneracy pressure*

$$
P \sim \frac{N E_F}{L}.
$$

### Three-dimensional box <a id="sec-2-2" name="sec-2-2"></a>

A *white dwarf* is a dense remnant of protons and neutrons left after a star burns up its fuel.
There are two forces on the star: gravity (mostly due to the protons)
trying to make it collapse further, and degeneracy pressure (due to
the electrons) resisting this collapse.
The attraction between protons and electrons is very small compared to these two forces, so we can ignore it.
To a good approximation, the electrons behave like a non-interacting gas at zero temperature.
Let's study a three-dimensional box!

A matter wave in a cube of volume $V = L^3$ oscillates in each dimension independently, with three wavelengths $\vec{\lambda} = (\lambda_x, \lambda_y, \lambda_z)$, and corresponding wave modes $\vec{n} = (n_x,n_y,n_z)$, where $\lambda_{x,y,z} = L/2n_{x,y,z}$.

Assume that the kinetic energies in each direction just add together.
Argue that the energy of a particle of mass $m$ and wave modes $\vec{n}$ is

$$
E_{\vec{n}} = \frac{8\pi^2 \hbar^2}{mV^{2/3}}(n_x^2+n_y^2+n_z^2).
$$

Find the energy and possible wave modes for the lowest energy level(s).
What about the first excited state(s)?

The previous question is meant to demonstrate that energy levels are trickier in three dimensions, and adding up all the possibilities to determine the Fermi energy will be hard work.
But there is a shortcut for many electrons.
Notice that the wave modes $\vec{n}$ can be viewed as vectors in three-dimensional space, with one per unit cube.
Argue that a very large sphere, of radius $n_F \gg 1$ in "wave mode space", contains approximately $N$ points, where

$$
N \approx \frac{4\pi}{3} n_F^3.
$$

Using the previous observation, argue that if we add $N\gg 1$ electrons into our box, the Fermi energy is approximately

$$
E_F \approx \frac{8\pi^{4/3} \hbar^2}{m}\left(\frac{3N}{4V}\right)^{2/3}.
$$

### Stars <a id="sec-3" name="sec-3"></a>

We're finally ready to calculate the mass of the largest white dwarfs.
This is called the *Chandrasekhar limit*.
So far, we have neglected relativity.
 But in a white dwarf, electrons are typically zipping around at close to the speed of light, so the kinetic energy has the *ultrarelativistic form*

$$
E = |\vec{p}|c, \quad \text{ where } \quad |\vec{p}| = \sqrt{p_x^2+p_y^2+p_z^2},
$$

where $c = 3\times 10^8 \text{ m/s}$ is the speed of light.
For $N \gg 1$ neutrons, derive the Fermi energy

$$
E_F \sim \hbar c \left(\frac{N}{V}\right)^{1/3}.
$$

Using the ideal gas law as above, conclude that the degeneracy pressure is

$$
P_\text{degen} \sim \hbar c \left(\frac{N}{V}\right)^{4/3}.
$$

A neutron star is very dense, and wants to collapse under its own weight.
For a star of mass $M$ and radius $R$, argue that force of collapse is roughly

$$
F_\text{grav} \sim \frac{GM^2}{R^2},
$$

where $G = 6.7\times 10^{-11} \text{ m}^3/\text{kg s}^2$ is *Newton's constant*.

*Hint.* The gravitational force is $F = GMm/r^2$ for masses $M,m$
separated by $r$.

From the previous question, deduce that the gravitational pressure is approximately

$$
P_\text{grav} \sim \frac{GM^2}{R^4}.
$$

*Hint.* Recall that $P = F/A$, i.e. pressure is force divided by area.

The maximum mass of a neutron star can be obtained by balancing the gravitational and neutron degeneracy pressure.
Increase the mass, and gravity inevitably wins, forcing the star to collapse into a black hole!
Using $M = Nm_\text{N}$ for neutron mass $m_\text{N} = 1.7 \times 10^{-27} \text{ kg}$, $V \sim R^3$, deduce the Chandrasekhar limit $M_C$:

$$
M_C \sim \left(\frac{c\hbar}{G}\right)^{3/2}\frac{1}{m_\text{N}^2}.
$$

Plug in numbers and compare the mass of the largest neutron star to the mass of our sun, $M_\odot = 2\times 10^{30} \text{ kg}$.
You should find $M_C \approx 1.7 M_\odot$.

## Extra

The fact that only certains orbits --- or, in atomic language,
*orbitals* --- are allowed has deep consequences for the structure of
matter.
It is not a trivial change.
But if the planets were governed by *quantum* physics, only certain
orbits would be allowed!
The orbits are *quantised*.
Suppose we have a big central body, like the sun, being orbited by
much smaller bodies, such as the planets of the solar system.
In classical physics, the planets can orbit at any radius they like.
Kepler's laws relate the period to the radius, for instance, but any
old radius is allowed.
