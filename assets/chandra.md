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

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Fermi gas</a>
   1. <a href="#sec-2-1">Bohr's model</a>
   2. <a href="#sec-2-2">Electrons on a circle</a>
   3. <a href="#sec-2-3">Electrons on a donut</a>
   3. <a href="#sec-2-4">The Fermi sea</a>
3. <a href="#sec-3">Light and gravity</a>
   1. <a href="#sec-3-1">Ultrarelativity</a>
   2. <a href="#sec-3-2">White dwarfs and neutron stars</a>
   3. <a href="#sec-3-3">The Chandrasekhar limit</a>
   3. <a href="#sec-3-4">Neutron stars</a>
- <a href="#sec-A">A. Donuts and boxes</a>

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
[Subrahmanyan Chandrasekhar](https://en.wikipedia.org/wiki/Subrahmanyan_Chandrasekhar),
who first calculated it in 1931.
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

### Bohr's model<a id="sec-2-1" name="sec-2-1"></a>

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
exhibit wave-like behaviour, with a wavelength related to its momentum
in the same way:

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

### Electrons on a circle <a id="sec-2-2" name="sec-2-2"></a>

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

where $k_B$ is *Boltzmann's constant*.
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
This is also called *degeneracy pressure*.
You can show in Exercise 2 that the degeneracy pressure for a circle
is roughly

$$
P_F \sim \frac{N E_F}{L}.
$$

We haven't defined $P_F$ carefully, and $\sim$ means there is a number
out front we are neglecting.

---

**Exercise 2.** Let's calculate some simple properties of the Fermi
  gas on the circle.

<span style="padding-left: 20px; display:block">
(a) Show that if we put $N$ electrons on the circle, the Fermi energy
is
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
P_F \sim \frac{\hbar^2 N^3}{m_e L^3}.
$$

---

### Electrons on a donut <a id="sec-2-3" name="sec-2-3"></a>

We live in a three-dimensional world.
When you add more than one electron to an atom, they not only
interact, but can have different orientations, you must reckon with
this basic fact about space.
This is where the whole formalism of s, p, d, f, and so on, comes
from, and thus all the wonders of chemistry and biology.
We also want to consider a three-dimensional quantum system for our
eventual application to stellar remnants, but as before,
avoiding the complications of the atom.

There is a neat trick which lets us do this by combining three
circles.
But to see how to do this, we need to think about the circle a little
differently first.
Instead of thinking of a circle of circumference $L$, let's snip it
at some point and straighten it out, giving a line of length $L$.
The matter waves on the circle must join smoothly at the point we
snipped, and if redraw them on the line, we see the amplitude of the
wave at one end must equal the amplitude at the other.
The fancy mathematical name for this is a *periodic boundary
condition*, but really it just means "glue the endpoints".
So we can view a circle as a line with periodic boundary conditions.

Instead of periodic boundary conditions on a line, we could imagine
them on a *square* of side length $L$, described by coordinates $x$ and $y$.
A wave is now a wobbly sheet drawn over the square, with an amplitude
$A(x, y)$.
Periodicity is now the requirement that

$$
A(0, y) = A(L, y), \quad A(x, 0) = A(x, L).
$$

If we glue the two sides, what do we get?
Amazingly, the answer is a donut!
We discuss how to visualise this in <a href="#sec-A">the appendix</a>.

It might seem much more complicated to figure out how to quantise
waves in this space, but it separates nicely into two copies of a
problem we have already solved.
Suppose the wave just wobbles independently in the $x$ and $y$
directions, with respective wavelengths $\lambda_x$ and $\lambda_y$.
We can impose the Bohr-de Broglie condition in each direction
independently, so

$$
\lambda_x = \frac{L}{n_x}, \quad \lambda_y = \frac{L}{n_y}.
$$

To determine the energy, we use the fact that $p^2 = |\vec{p}|^2$ is the *squared
length* of the momentum vector, $\vec{p} = (p_x, p_y)$:

$$
p^2 = p_x^2 + p_y^2.
$$

You can then use the de Broglie relation $\lambda_x = 2\pi\hbar/p_x$, $\lambda_y = 2\pi\hbar/p_y$
in each direction separately to obtain

$$
E_{n_x, n_y} = \frac{p^2}{2m_e} = \frac{p_x^2 + p_y^2}{2m_e} =
\left(\frac{2\pi^2 \hbar^2 }{m_e L^2}\right) (n_x^2 + n_y^2).
$$

We can assemble the two integers $n_x, n_y$ into a vector $\vec{n} =
(n_x, n_y)$, so

$$
p^2 = \left(\frac{2\pi\hbar}{L}\right)^2 |\vec{n}|^2.
$$

This relation actually holds for *any* number of dimensions.
For instance, on a *cube* of side length $L$, with periodic boundary
conditions, we have energy levels

$$
E_{\vec{n}} = \left(\frac{2\pi^2 \hbar^2 }{m_e L^2}\right) |\vec{n}|^2
$$

for $\vec{n} = (n_x, n_y, n_z)$.
We give some ways to visualise the periodic cube, or
*three-dimensional donut*, in the <a href="#sec-A">appendix below</a>.

---

**Exercise 3.** Let's get a feeling for energy levels on a donut.

<span style="padding-left: 20px; display:block">
(a) Compute the lowest three energy levels, and sketch them on the square.
</span>

<span style="padding-left: 20px; display:block">
(b) If I put $N = 10$ electrons in the donut, what is the Fermi energy?
</span>

---

### The Fermi sea <a id="sec-2-4" name="sec-2-4"></a>

As Exercise 3 demonstrates, finding energy levels on the donut takes
some work, even though it is vastly simpler than the atom.
It is even trickier to calculate energy levels on the
three-dimensional donut, where we need to consider all the different
possibilities for $\vec{n} = (n_x, n_y, n_z)$.
Calculating the Fermi energy $E_F$ for large $N$ seems like a hard and
boring task best suited to a computer.

However, there is a shortcut for computationally-inefficients humans when $N$ is very large.
We'll do the calculation for a regular donut, and leave you to do the
calculation for the three-dimensional donut.
The vectors $\vec{n} = (n_x, n_y)$ live on a Cartesian plane, with one
point per unit area.
If we draw a circle of radius $n_F$ in this plane, centred at the
origin, then provided it is large, the number of points it contains is
approximately equal to the area:

$$
N \approx \pi n_F^2.
$$

This circle is called the *Fermi sea*.
The maximum length of a vector in the Fermi sea is $|\vec{n}|^2 \approx
n_F^2$, and the circle contains all vectors of smaller length as well.
Electrons added to the system will find the shortest available vector,
and hence, fill out the circle from the origin outwards.

From the Fermi sea picture, we learn that for large $N$, the Fermi energy is

$$
E_F \approx \left(\frac{2\pi^2 \hbar^2 }{m_e L^2}\right) n_F^2 \approx \left(\frac{2\pi \hbar^2}{m_e L^2}\right) N.
$$

For a handful of matter, say $N \sim 10^{23}$ electrons, this
approximation is basically perfect.
On a donut, the degeneracy pressure is calculated as above, but $L$ is
replaced by $L^2$, so we find that

$$
P_F \sim \frac{NE_F}{L^2} \sim \frac{\hbar^2 N^2}{m_e L^4}.
$$

You can repeat the Fermi sea calculation for a three-dimensional donut
in Exercise 4.

---

**Exercise 4.** Now consider a Fermi gas in a periodic cube of side length $L$.

<span style="padding-left: 20px; display:block">
(a) For $n_F \gg 1$, show that a ball of radius $n_F$ in
$\vec{n}$-space contains approximately $N \approx 4\pi n_F^3/3$
points. *Hint.* Consider area vs perimeter.
</span>

<span style="padding-left: 20px; display:block">
(b) Argue that for large $N$, the Fermi energy is
</span>

$$
E_F \approx \left(\frac{2\pi^2 \hbar^2}{m_eL^2}\right) \left(\frac{3N}{4\pi}\right)^{1/3}.
$$

<span style="padding-left: 20px; display:block">
(c) Conclude that the degeneracy pressure is
</span>

$$
P_F \sim \frac{\hbar^2 N^{4/3}}{m_e L^5}.
$$

---

## Light and gravity <a id="sec-3" name="sec-3"></a>

We're almost ready to perform our thought experiment of throwing
electrons into a box until we make a black hole.
But to apply our Fermi gas model to old stars, we need to tinker a
little with the energy, and learn some facts about light and gravity.

### Ultrarelativity <a id="sec-3-1" name="sec-3-1"></a>

Gravity is very strong in stars, particularly old stars which have
shed their outer layers and contracted to form a dense core.
This means particles are zipping around at close to the speed of
light, and the earlier, classical form of kinetic energy we used is no
longer accurate.
Einstein's famous formula $E = mc^2$ is subtle, concealing the fact
$m$ actually *changes* with velocity.
It is sometimes more helpful to write his equation in the form

$$
E^2 = (m_\text{rest} c^2)^2 + p^2 c^2,
$$

where $p^2 = |\vec{p}|^2$ is the momentum squared as usual, and
$m_\text{rest}$ is the mass of the particle at rest.
Particles in an old star usually have much more momentum than mass energy, so
the kinetic energy takes the *ultrarelativistic form*:

$$
E \approx |\vec{p}|c.
$$

All the business about Bohr-de Broglie quantisation remains unchanged,
and in particular we still have $|\vec{p}| = 2\pi\hbar|\vec{n}|/L$.
It follows that

$$
E_{\vec{n}} = \frac{2\pi\hbar c|\vec{n}|}{L}.
$$

I'll let you find the degeneracy pressure!

---

**Exercise 5.** Consider an ultrarelativistic Fermi gas in a periodic
cube of volume $V$.
Show that, for $N \gg 1$, the degeneracy pressure is

$$
P_F \sim \hbar c\left(\frac{ N}{V}\right)^{4/3}.
$$

---

### White dwarfs and neutron stars<a id="sec-3-2" name="sec-3-2"></a>

Above, I referred mysteriously to various "stellar leftovers".
Let's discuss the life cycle of old stars, and see how the different
endpoints of stellar evolution are related to the Fermi gas.
It will be useful to measure stars using the mass of our sun,

$$
M_\odot = 2\times 10^{30} \text{ kg}.
$$

Stars fuse hydrogen into helium, and so on into the heavier elements.
The pressure generated by these thermonuclear reactions stop the star
from contracting under its own weight.
But once a star runs low on fuel, gravity begins to win, and the fate
of the star depends on its mass $M$ before collapse:
- *White dwarf.* If the star is less than $10$ suns heavy ($M < 10
  M_\odot$), it will contract until the degeneracy pressure of the
  electrons in unspent nuclear fuel stops the collapse.
- *Neutron star.* If the star is between $10$ and $30$ solar masses
  ($10 M_\odot < M  < 30 M_\odot$), electron degeneracy pressure is not
  enough, and a more desparate gambit is required. Electrons and
  protons combine to make neutrons, neutron degeneracy pressure plus
  repulsion due to the [strong nuclear force](https://en.wikipedia.org/wiki/Strong_interaction)
  can resist gravitational collapse.
- *Black holes.* If the star is heavier than $30$ suns ($30 M_\odot < M$), nothing can arrest the collapse, and the star forms a
black hole.

White dwarfs are simpler, so we'll focus on these.
The core is electrically neutral, consisting of $N$ electrons and $N$
protons, the latter providing most of the star's mass.
As a result, electrostatic repulsion plays only a small role, and
instead, the degeneracy pressure of the electrons dominates.
Assuming gravity is strong and the electrons are ultrarelativistic,
the degeneracy pressure is

$$
P_F \sim \hbar c\left(\frac{ N}{V}\right)^{4/3}
$$

where $V$ is the volume of the white dwarf.
We figure out the maximum mass of a white dwarf in the next section by
comparing this degeneracy pressure due to gravity.

Our calculation for $P_F$ is highly suspicious.
To get there, we made two assumptions: first, the gas is at zero
temperature; second, the star is a periodic cube, rather than a
sphere.
Let's see why these assumptions are reasonable:
- *Temperature.* We can approximate a Fermi gas as zero temperature
  provided $T$ is much smaller than the Fermi temperature, $T \ll
  T_F$.
  White dwarfs are typically around $T = 10^7 \text{ K}$, while the
  Fermi temperature is order $T_F \sim 10^9 \text{ K}$ (Exercise 6).
- *Shape.* A white dwarf is a sphere, while a periodix box is not even
  remotely spherical. Nevertheless, our model works because a sphere
  and a box are just different choices of *boundary condition*, and as
  $N$ gets large, boundary conditions become irrelevant.

---

**Exercise 6.** A white dwarf the size of the earth has a density
around $10^9 \text{ kg/m}^3$, consisting mostly of protons.
Show that the Fermi temperature is $T_F \sim 10^9 \text{ K}$.

*Hint.* Use the ideal has law to relate $P_F$ and $T_F$.
You will need to know the numerical values for  mass of a proton $m_p$, the speed of light $c$, Planck's constant $\hbar$, and
Boltzmann's constant $k_B$:

$$
\begin{align*}
m_p & = 1.7 \times 10^{-27} \text{ kg} \\
c & = 3.0 \times 10^8 \text{ m/s} \\
\hbar & = 1.1 \times 10^{-34} \text{ J} \cdot \text{s} \\
k_B & = 1.4\times 10^{-23} \text{ m}^2\text{ kg}/\text{ K s}^2.
\end{align*}
$$

---

### The Chandrasekhar limit<a id="sec-3-3" name="sec-3-3"></a>

We're finally ready to calculate the mass of the largest white dwarfs,
called the *Chandrasekhar limit*.
Our goal will be to calculate the "self-pressure" on the white dwarf
due to gravity, and compare to the degeneracy pressure we calculated
<a href="#sec-3-1">above</a>.
Recall Newton's law of gravitation,

$$
F = \frac{GMm}{R^2}
$$

where $M,m$ are masses separated by $R$, and $G = 6.7\times 10^{-11} \text{ m}^3/\text{kg s}^2$ is *Newton's constant*.

Consider a spherical white dwarf of mass $M$ and radius $R$.
We now want to ask: what gravitational force does this exert on
itself?
Obviously a precise answer will depend on the composition of the dwarf
and other details, but we can make an order-of-magnitude guess from
dimensional analysis.
In Newton's law, we set both masses equal to $M$, since the white
dwarf is both doing the pulling and experiencing the pull.
Similarly, the only length scale in the problem is the radius, $R$, so
we guess

$$
F_\text{grav} \sim \frac{GM^2}{R^2}.
$$

Since pressure is force divided by area, the *gravitational
self-pressure* is going to be this force divided by the surface area
of the sphere, or

$$
P_\text{grav} \sim \frac{F_\text{grav}}{A} \sim \frac{GM^2}{R^4}.
$$

The maximum mass of a neutron star can be obtained by balancing the
gravitational and neutron degeneracy pressure.
Increase the mass, and gravity inevitably wins, forcing the star to
collapse into a black hole!

---

**Exercise 7.** Finally, we can calculate the Chandrasekhar limit.
The mass of a white dwarf is mostly protons, with $M = Nm_p$, while $V \sim R^3$.

<span style="padding-left: 20px; display:block">
(a) Set $P_\text{grav} = P_F$, and show that the corresponding mass is
	</span>

$$
M_C \sim \left(\frac{c\hbar}{G}\right)^{3/2}\frac{1}{m_p^2}.
$$

<span style="padding-left: 20px; display:block">
(b) Evaluate $M_C$ numerically and compare to the mass of the sun. You
should find
</span>

$$
M_C \sim\, 1.7 M_\odot.
$$

<span style="padding-left: 20px; display:block">
The state-of-the-art limit, incorporating details about the white
dwarf's composition and structure, is $ M_C \approx 1.44 \,M_\odot$, so
we've done remarkably well!
</span>

---

### Neutron stars<a id="sec-3-4" name="sec-3-4"></a>

How are neutron stars different from a white dwarf?
Neutrons are fermions, so if we pack them into a box, there will be
degeneracy pressure.
They are still cold compared to the Fermi temperature.
The main difference, apparently, is that there are $N$ neutrons rather
than $N$ protons and electrons.
If we repeat the reasoning above, balancing neutron degeneracy
pressure against gravitational self-pressure, we find

$$
M_N \sim \left(\frac{c\hbar}{G}\right)^{3/2}\frac{1}{m_n^2}
\approx 1.7 \, M_\odot
$$

once more, where $m_n \approx m_p$ is the mass of a neutron.

### A. Donuts and boxes <a id="sec-A" name="sec-A"></a>
