---
Layout: post
mathjax: true
comments: true
title:  "Virtual particles and uncertainty"
categories: [Physics]
date:  2020-10-22
---

**October 22, 2020.**  *According to quantum mechanics folklore,
  virtual particles are objects which can flit in and out of existence,
  governed by Heisenberg's uncertainty principle in its energy-time
  form. But what is uncertainty in time? And what are virtual
  particles in a quantum-mechanically responsible sense? Here, we
  connect the two rigorously.*

#### Uncertain uncertainty

*Prerequisites: quantum mechanics.*

When Heisenberg layed down his uncertainty principle in 1927, it came
in two flavours: position-momentum and energy-time.
Schematically, these are usually written

$$
\Delta x \cdot \Delta p \gtrsim \hbar, \quad \Delta E \cdot
\Delta t \gtrsim \hbar.
$$

What we mean by uncertainty is a bit uncertain.
Often, the first semi-rigorous context we encounter these notions in
is the *wavepacket*, i.e. a well-localized wavefunction in space
$|\Psi(x)\rangle$.
This has some spread of positions $\Delta x$, but we can Fourier
transform to momentum space, where it will have some spread $\Delta p$.
The uncertainty principle is then a mathematical result about the
Fourier transform, and in fact, it is true for any wavefunction.

We can derive the energy-time form for a wavepacket using the
following hack.
Let $\Psi(x, t)$ denote the profile of the wavepacket.
We assume it's well-localised around some wavenumber $k_0$, so it has *group
velocity*,

$$
v = \frac{\partial \omega}{\partial k}\bigg|_{k_0} = \frac{\hbar
\partial \omega}{\hbar\partial k}\bigg|_{k_0} = \frac{\partial E}{\partial p}\bigg|_{k_0},
$$

using $E = \hbar \omega$ and $p = \hbar \omega$.
If we identify $\Delta t$ as the time taken for the wavepacket to
travel its own spread, $\Delta x$, then $v\Delta t = \Delta x$.
The position-momentum uncertainty principle then gives

$$
\Delta x \cdot \Delta p = \frac{\partial E}{\partial p}\bigg|_{k_0} \Delta
t \cdot \Delta p \gtrsim \hbar.
$$

If you squint, i.e. assume $v = \Delta E/\Delta p$, you get the
energy-time form of the uncertainty principle.

#### MTML bound

#### Virtual particles

#### References

<!-- - ["Energy Cost of Information Transfer"](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.46.623)
  (1981), Jakob D. Bekenstein. -->
<!-- - ["Quantum noise and information"](https://projecteuclid.org/euclid.bsmsp/1200513783)
  (1967), H. J. Bremmerman. -->
- ["Quantum speed limits: from Heisenberg’s
uncertainty principle to optimal quantum control"](https://arxiv.org/abs/1705.08023)
(2017), Sebastian Deffner and Steve Campbell.
<!-- ["Ultimate physical limits to computation"](https://arxiv.org/abs/quant-ph/9908043) (2000), Seth Lloyd. -->
- ["The maximum speed of dynamical evolution"](https://arxiv.org/abs/quant-ph/9710043) (1997), Norman Margolus, Lev B. Levitin.

<!-- *If you believe the speed-reading hype, you can
  read as fast as you like without sacrificing
  comprehension. Responsible psychological research shows this is not
  the case: there is inevitably a cognitive tradeoff between speed and
  fidelity of processing. I perform some less responsible "research"
  and show that, even for a brain vastly superior to ours, there are
  fundamental physics limits on speed reading.* -->

<!-- Now we return to our original problem, namely, placing a fundamental
physical limit on speed reading.
As a test case, we consider Marcel Proust's six-volume epic, *In Search of Lost Time*.
It has around $1.3$ million words, which translates to around
$6$ million bits, assuming a compressibility of one bit per character,
as discussed above. The Bremmerman-Bekenstein bound depends on how heavy the book is.
The Modern Library edition weights in at $m = 3.7 \text{ kg}$, with a
maximal rate $$\nu \leq \frac{\pi mc^2}{\hbar ln 2} \approx 1.5 \times 10^{52} \text{ bit s}^{-1}.
$$ So it can be properly read in $T = 4 \times 10^{-46} \text{ s}$, with
a decrease in time in direct proportion to how much you skim.-->
