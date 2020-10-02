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

Heavy things are governed by gravity, and small things are governed by
quantum mechanics.
Quantum gravity is the theory of things which are both small, heavy things, like the Big
Bang and black holes.
Unfortuntely, small heavy things are secretive.
Not only are the mathematical obstacles to combining gravity and
quantum mechanics formidable, but for fundamental reasons, nature
obscures the workings of quantum gravity with black holes.

#### Microscopes make black holes

The reason is simple.
Suppose we have a microscope which probes some length scale $\Delta x$.
By Heisenberg's uncertainty principle $\Delta x\Delta p \sim \hbar$
and de Broglie's relation $E = pc$, this corresponds to an energy scale

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
