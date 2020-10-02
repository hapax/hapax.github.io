---
Layout: post
mathjax: true
comments: true
title:  "Why is quantum gravity hard?"
categories: [Physics, Hacks]
date:  2020-10-02
---

**October 2, 2020.** *People often say that quantum gravity is hard
  because quantum mechanics and gravity are incompatible. I'll give a
  short, relatively non-technical explanation of why is false, what the real
  problem is (spacetime breaks down when we look too close), and some
  methods for fixing it.*

#### Introduction

Gravity is a theory of heavy things.
Quantum mechanics is a theory of small, fuzzy things.
*Quantum gravity* is a theory of things which are both small and
heavy, i.e. dense, like black holes or the Big Bang.
Often, people say that the two theories are "incompatible" because
they use different mathematics.
This is a tad misleading.
The real problem is that Nature is secretive: it hides the details of
quantum gravity inside black holes!
Let's see why.

#### Powerful microscopes make energy

Suppose we have a microscope which has can resolve lengths $\Delta x$.
Heisenberg's uncertainty principle says that the smaller this
resolution, the larger the uncertainty about the momentum of things we
measure, with

$$
\Delta p \gtrsim \frac{\hbar}{\Delta x}
$$

for Planck's constant $\hbar \approx 10^{-34} \text{ J/s}$.
We can relate this to the energy of the particles using Einstein's
famous formula $E = mc^2$.
In fact, we will write it in the much less well-known form

$$
E^2 = m^2c^4 = p^2c^2 + m_0^2 c^4,
$$

where $m_0$ is the mass of the particle at rest, $c = 3 \times 10^8
\text{ m/s}$ is the speed of light, and $m$ is the *relativistic
mass*, which increases (without limit) as the particle speeds up.
When the particle is moving very quickly, the momentum can be much
larger than the rest mass energy, and $p \approx E/c$.
If we measure very small distances, Heisenberg's principle tells us we
will be smacking around particles at very high momenta, so this is the
form we should use.
Thus, the uncertainty in the energy of particles our microscope is
examining is

$$
\Delta E \sim \frac{\hbar c}{\Delta x}\;.
$$

#### Energy makes black holes

Let's now recall Newton's universal law of gravitation,

$$
F = \frac{Gm_1 m_2}{r^2},
$$

where $G = 6.7\times 10^{-11} \text{ N m}^2\text{ /kg}$ is *Newton's
constant*.
We can use this to estimate the size of a black hole!
A black hole is a region of space where gravity is so strong light
is unable to escape.
To see how light figures in Newton's law, we need to give it a mass.
In classical physics, light is massless, but but we know better: Einstein's
formula tells us that it has some *relativistic* mass related to its
energy, $E = mc^2$.
(If you're curious, the mass of a particle of light, the photon,
depends on its frequency $f$ via

$$
m = \frac{E}{c^2} = \frac{2\pi\hbar f}{c^2},
$$

now using another formula ($E = 2\pi \hbar f$) discovered by Einstein.)
Let's continue.
For a black hole of mass $M$, and radius $r_s$, the force it exerts on
a photon with mass-energy $m$ is

$$
F \sim \frac{GMm}{r_s^2}.
$$

Using the work formula, we can view force as energy divided by
distance.
Since the energy of the photon is $E = mc^2$, and the relevant
distance is probably the black hole size $r_s$, we have

$$
\frac{mc^2}{r_s} \sim \frac{GMm}{r_s^2} \quad \Longrightarrow \quad
r_s \sim \frac{GM}{c^2}.
$$

Although we've been rather sloppy, this guess is correct!
So, if we take a mass $M$ and squish into a ball of radius $\lesssim
r_s$, it will make a black hole.

#### Microscopes make black holes

Now, let's return to our microscope.
In order to zoom in, Heisenberg's principle means it makes some energy
fluctuations, and by $E = mc^2$ these fluctuations have mass.
The associated black hole radius is

$$
r_s \sim \frac{Gm}{c^2} = \frac{G\Delta E}{c^4} = \frac{G\hbar}{\Delta x \cdot c^3}.
$$

It may seem sketchy to replace $E$ with $\Delta E$, but if the energy
of particles has fluctuations of size $\Delta E$ around $E = 0$, some
of them will have energy $E$.
We can clean up this expression by packaging all these constants into
a single object called the *Planck length*:

$$
\ell_P := \sqrt{\frac{G\hbar}{c^3}}.
$$

Then the associated black hole radius for our microscope is

$$
r_s \sim \frac{\ell_P^2}{\Delta x}.
$$

Now, what does this all mean?
Very simply, if the resolution $\Delta x$ of our microscope is within
the associated black hole radius, then our energy fluctuations will
produce a tiny black hole!
We won't see anything at all.
This happens when

$$
\Delta x \lesssim r_s \sim \frac{\ell_P^2}{\Delta x} \quad
\Longrightarrow \quad \Delta x \lesssim \ell_P.
$$

If we try to zoom in to the Planck scale, our microscope will create a
black hole.
Clearly, microscopes this powerful should be kept away from theorists!

#### What's the point?

#### Strong coupling

We can translate this dimensional argument into the language of
quantum field theory.
Set $\hbar = c = 1$.
Newton's constant $G$ is a \emph{dimensionful} coupling constant for gravity, with mass
dimension $[G] = -2$.
Perturbation theory is controlled by the effective
*dimensionless* coupling constant appearing at energy $E$,
roughly $g(E) = GE^{2}$.
This leads to a strongly coupled theory when $g \sim 1$, or

$$
E \sim \sqrt{\frac{1}{G}} \sim E_P\;,
$$

where $E_P = \sqrt{1/G}$ is the Planck energy.
At the Planck energy, when we expect quantum effects to become
important, the theory becomes strongly coupled!
