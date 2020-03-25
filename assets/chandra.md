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

*Prerequisites: basics conceps of quantum mechanics.*

Though they differ in size by many orders of magnitude, the solar
system and the atom are not so different.
Both involve smaller bodies (electrons/planets) orbiting a much
larger body (nucleus/sun) under the influence of a
central force (electrostatics/gravity).
Orbits also have finite occupancy.
Part of the definition of a planet is that it "clears its
neighbourhood" of any interlopers
(sic transit gloria [Pluto](https://en.wikipedia.org/wiki/Pluto#Classification)).
Electrons automatically clear their orbitals by
the *Pauli exclusion principle*, a point we will return to below.

That's where the resemblance ends.
The solar system is classical, and planets can orbit the sun at any
old radius they like.
In contrast, atoms obey quantum mechanics, and the orbits are
*quantised*, occuring only at certain allowed values.
Quantisation has deep consequences for atomic structure,
hence chemistry, hence life itself.
We're made out of exploded stars, sure, but we're also made from
quantum mechanics!
Biology is quantum mechanics writ large.

Quantisation not only governs the heavy elements ejected
from stars, but the compact remnants left behind.
Surprisingly, we can model these leftovers by throwing electrons into a box.
Throw in too many electrons, and the box collapses to form a black hole.
With some dimensional analysis, we can obtain an order-of-magnitude
bound on the mass of remnant stars called the *Chandrasekhar limit*, after
[Subrahmanyan Chandrasekhar](https://en.wikipedia.org/wiki/Subrahmanyan_Chandrasekhar).
The analysis combines the gravity governing the solar
system with the quantisation governing the atom, though a remnant star
is simpler than both.
In the words of Chandra himself,

<span style="padding-left: 20px; display:block">
What is intelligible is also beautiful.
</span>

While the star's ejecta may go on to form life --- remarkable for its
complexity -- what is left behind is beautiful by virtue of its simplicity.

## Fermi gas<a id="sec-2" name="sec-2"></a>

We're going to consider a simple caricature of quantum
mechanics, given by three rules:

1. There is a fixed set of allowed energies, $E_1 \leq E _2 \leq E_3 \leq
   \cdots$.
2. Only one particle can occupy an energy level at a time.
3. If we add particles, they occupy the lowest available energy level.

I think of this as the "hotel" model, since the quantum system is like
a hotel with rooms costing $E_1\leq E_2 \leq \cdots$ and so on.
Particles travel alone, and stay by themselves.
Finally, particles are cheap, looking for the most affordable room the
hotel can offer.

None of these rules is true in general, so let's spell out our assumptions.
The first rule states that energies don't change when particles join
the system, which is only true if the *particles don't interact*.
This is like a gas, where particles are very far apart and only
occasionally collide.
So our hotel describes what is called a *quantum gas*.

The second rule is the *Pauli exclusion principle*.
This holds for electrons, but in fact, a much larger class of
particles called *fermions*, including neutrons, protons and quarks,
i.e. the constituents of matter.
There is a second class of particles called *bosons* ---
including photons --- which do not obey the Pauli exclusion principle,
and will happily pack as many as possible into a hotel room!
So, our model describes a quantum gas of fermionic particles, also
called a *Fermi gas*.

Since we're dealing with a gas, you might wonder if temperature plays
a role.
It turns out that our third rule --- particles are maximally cheap ---
is equivalent to a temperature is *zero*.
If the temperature is nonzero, there is some chance that particles
arriving at the hotel will splash out on a more expensive room.
Our three rules thus describe a *zero temperature Fermi gas*.

### Bohr's model

We'll start by recalling Bohr's model of hydrogen and the role played
by quantisation.
Bohr thought of the nucleus as a big, immovable positive charge, and
the electron as a tiny orbiting negative charge.
To explain why hydrogen emitted and absorbed only certain colours of
light, Bohr postulated that only certain orbits were allowed,
satisfying the *quantisation of angular momentum*:

$$
m_ev r = n \hbar, \quad n = 1, 2, 3, \ldots
$$

where the "quantum" of angular momentum is *Planck's
(reduced) constant* $\hbar$, and $m_e$ is the mass of the electron.
There is a nice way of reformulating this using de Broglie's notion of
*matter waves*.

Let's turn for a moment to light.
The energy, momentum, and wavelength of a single photon of light can
be written

$$
E = \hbar \omega, \quad p = \frac{E}{c}, \quad \lambda = \frac{2\pi c}{\omega},
$$

where $\omega$ is the angular frequency of light and $c$ is its speed.
Rearranging, one finds momentum and wavelength are related by

$$
\lambda = \frac{2\pi c}{\omega} = \frac{2\pi \hbar}{p}.
$$

By analogy, de Broglie guessed that a massive particle could also
exhibit wave-like behaviour, with a wavelength

$$
\lambda = \frac{2\pi \hbar}{p}.
$$

Plugging this into Bohr's quantisation condition gives

$$
pr = n\hbar \quad \Longrightarrow \quad \lambda_n = \frac{2\pi r}{n},
\quad n = 1, 2, 3, \ldots.
$$

This has a lovely interpretation: the allowed orbits are those for
which the matter wave is *periodic*, meeting up with itself after $n$
periods.

To connect to our "hotel" model of quantum mechanics, we need to find
the energy levels of the hydrogen atom.
First, we can express kinetic energy in terms of momentum, hence in
terms of de Broglie wavelength:

$$
E_n = \frac{1}{2}m_e v^2 = \frac{(m_ev)^2}{2m_e} = \frac{p^2}{2m_e} =
\frac{4\pi^2 \hbar^2 n^2}{2m_e (2\pi r_n)^2}.
$$

We still don't know the radius of the orbit $r_n$, and we won't need
it below.
However, the interested reader can supply it themselves in the
following exercise.

---

**Exercise 1.** The key fact we haven't used about the hydrogen atom
  is that the electron orbits due to electrostatic attraction.
  The attractive force between charge $q_1$ and $q_2$ is governed by
  Coloumb's law, an inverse square law analogous to gravity:

$$
F = \frac{k_eq_1q_2}{r^2},
$$

where $k_e$ is a constant analogous to $G$ in Newton's law of gravitation.

<span style="padding-left: 20px; display:block">
(a) Show that the electron is pulled inward with force
</span>

$$
F = \frac{k_e e^2}{r^2}.
$$

<span style="padding-left: 20px; display:block">
(b) For an electron in a circle, the centripetal acceleration $a =
v^2/r$.
Use this and part (a) to derive the relation
</span>

$$
p^2 = \frac{k_e m_e e^2}{r}.
$$

<span style="padding-left: 20px; display:block">
(c) Use (b) to show that the orbits gets larger quadratically with $n$:
</span>

$$
r_n = \left(\frac{\hbar^2}{k_e m_e e^2}\right) n^2.
$$

<span style="padding-left: 20px; display:block">
(d) Conclude that hydrogen has energy levels
</span>

$$
E_n = -\frac{p_n^2}{2m_e} = -\left(\frac{m_ek_e^2
e^4}{2\hbar^2}\right)  \frac{1}{n^2}.
$$

<span style="padding-left: 20px; display:block">
Notice the minus sign in $E_n$.
If we don't add it, energy *decreases* with $n$. From Rule 3,
electrons occupy the lowest available state, so they will zip off to infinity!
</span>

<span style="padding-left: 20px; display:block">
(e) For an ion with $Z$ protons in the nucleus, use the Bohr model to
obtain the single-electron energy levels
</span>

$$
E_n = -\left(\frac{m_ek_e^2 e^4}{2\hbar^2}\right)  \frac{Z^2}{n^2}.
$$

---

### Electrons on a circle <a id="sec-2-1" name="sec-2-1"></a>

Bohr's model is a useful illustration of how to calculate energy
levels.
But the calculation only works for a *single* electron.
Once we start adding more, the electrons repel, and things become
dramatically more complicated.
In other words, an atomic is not a Fermi gas!
Rather than trying to derive chemistry from first principle, we will
ignore all these difficulties, and adapt the Bohr model into something
we can use.

One complication of the Bohr model was the exists of different radii.
Instead, we are going to fix a *single* orbit, of circumference $L =
2\pi r$.
Then the Bohr-de Broglie quantisation condition becomes

$$
\lambda_n = \frac{L}{n},
$$

and the energy levels are

$$
E_n = \left(\frac{2\pi^2 \hbar^2 }{m_e L^2}\right) n^2.
$$

There is no proton in this problem now, since that was only necessary
to figure out $r_n$, and we have fixed that by fiat.
This also lets us get rid of the minus sign we found in Exercise 1,
since that corresponded to the electron being *bound*.
Now, the electron lives on a circle by definition.

So, we have the single-electron energies, just like the atom.
Unlike the atom, we are just going to go ahead and assume that
electrons don't interact, and our hotel model (Rules 1--3) applies.
Suppose we throw $N$ particles onto the circle.
The highest occupied energy level is called the *Fermi energy* $E_F$
(see Exercise 2).
The fact that the Fermi energy is *not* just the lowest energy level
has interesting consequences.
The best way to think of temperature is in terms of
[its relation](https://en.wikipedia.org/wiki/Equipartition_theorem) to
average energy per particle:

$$
E_\text{avg} \sim k_BT,
$$

where $k_B = 1.4\times 10^{-23} \text{ m}^2\text{ kg}/\text{ K s}^2}$ is *Boltzmann's constant*.
This suggests that, even though our Fermi gas is supposed to be at
zero temperature, there is some "effective temperature" due to quantum
effects.
For lack of imagination, we call this the *Fermi temperature*, defined by

$$
T_F = \frac{E_F}{k_B}.
$$

Finally, in an ideal gas, temperature and pressure are related by the
ideal gas law, $PV = k_B N T$.
Once again, the fact that the electrons are separated can be viewed as
an "effective pressure" $P_F$ due to quantum effects.
You can show in Exercise 2 that this pressure is roughly

$$
P_F \sim \frac{N E_F}{L}.
$$

We haven't defined $P_F$ carefully, so $\sim$ indicates a constant
we won't worry about.

---

**Exercise 2.** Let's calculate some simple properties of our Fermi
  gas on the circle.

<span style="padding-left: 20px; display:block">
(a) Show that if we put $N$ into our box, the Fermi energy
is just
</span>

$$
E_F = \left(\frac{2\pi^2 \hbar^2 }{m_e L^2}\right)N^2.
$$

<span style="padding-left: 20px; display:block">
(b) By identifying $T = T_F$ in the ideal gas law, or using
dimensional analysis (see
e.g. [here](https://hapax.github.io/physics/teaching/hacks/napkin-hacks/#sec-2-3)),
argue that
</span>

$$
P_F \sim \frac{N E_F}{L} = \left(\frac{2\pi^2 \hbar^2 }{m_e L^3}\right)N^3.
$$

---

### Three-dimensional box <a id="sec-2-2" name="sec-2-2"></a>

We live in a three-dimensional world.
When you add more than one electron to an atom, they not only
interact, but can have different orientations, you must reckon with
this basic fact about space.
This is where the whole formalism of s, p, d, f, and so on, comes
from, and thus all the wonders of chemistry and biology.

We also want to consider a three-dimensional quantum system for our
eventual application to stellar remnants, but as before, while
avoiding the complications of the atom.

We will also call the circle a "one-dimensional box" since, as $L$
gets large, it's hard to tell the difference between a circle and a
very long line.

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

## A. Periodic boxes

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


Instead of an atom, let's consider the much simple scenario of a
one-dimensional box, of length $L$.

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
