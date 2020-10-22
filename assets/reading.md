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
If we linearize around the central wavenumber, we have

$$
\omega(k) \approx \omega(k_0) + v(k - k_0) \quad \Longrightarrow \quad
v = \frac{\Delta \omega}{\Delta k} = \frac{\Delta E}{\Delta p},
$$

where now $\Delta p$ is interpreted as the momentum spread of the
wavepacket and $\Delta E$ is the correspond energy spread.
Let $\Delta t$ be the time taken for the wavepacket to
travel the distance of its own spread, $\Delta x$, then $v\Delta t =
\Delta x$.
The position-momentum uncertainty principle then gives

$$
\Delta x \cdot \Delta p \approx \frac{\Delta E}{\Delta p} \Delta
t \cdot \Delta p = \Delta E \cdot \Delta t \gtrsim \hbar.
$$

So we get the energy-time form of the uncertainty principle!
But it's very different from the position-momentum form.
Position and momentum are bases to measure the wavepacket in, and
correspond to legitimate quantum-mechanical operators.
Energy also corresponds to an operator, namely the Hamiltonian.
But time is not an operator! Here, it appears very specifically as the
time the wavepacket takes to move a whole $\Delta x$ away.
Physically, this is the point at which *the position changes
distinguishably*.
Prior to this time, there is large overlap between the wavepackets at
the two different times.
This is the seed of a rigorous version of the energy-time uncertainty
principle which doesn't depend on having a localized wavepacket.

#### MTML bound

In 1945,
[Mandelstamm and Tamm](https://link.springer.com/chapter/10.1007/978-3-642-74626-0_8)
gave the first rigorous version of the energy-time uncertainty
relation.
It's important, because it tells us what it means!
I'll present the nice proof from
[Defner and Campell (2017)](https://arxiv.org/pdf/1705.08023.pdf),
since it's closely related 

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
- ["The Uncertainty Relation Between Energy and Time in Non-relativistic Quantum Mechanics"](https://link.springer.com/chapter/10.1007/978-3-642-74626-0_8)
  (1945), L. MandelstamIg. Tamm.
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
