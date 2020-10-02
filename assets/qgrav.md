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

#### Microscopes make black holes

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

where $m_0$ is the mass of the particle at rest and $m$ is the
*relativistic mass*, which increases when it picks up kinetic energy.
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

The \emph{Schwarzschild radius} $r_s$ of a (four-dimensional) spherical black hole is
related to its mass-energy $E$ by

$$
r_s \sim \frac{GE}{c^4}\;.
$$

Thus, the Schwarzschild radius associated with our microscope is

$$
r_s \sim \frac{G\hbar}{\Delta x \cdot c^3} = \frac{\ell_P^2}{\Delta x}\;,
$$

where $\ell_P := \sqrt{G\hbar/c^3}$ is the *Planck length*.
If $\Delta x \lesssim \ell_P$, then $r_S \gtrsim \Delta x$.
In other words, if we try to probe below the Planck scale, our microscope will
create a black hole.
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
