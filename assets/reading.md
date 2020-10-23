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
  particles in a quantum-mechanically responsible sense? In this post,
  I derive the uncertainty relations of Mandelstam-Tamm and
  Margolus-Levitin, and make a semi-rigorous connection between
  virtual particles and transitioning to a distinguishable state.*

#### Introduction to uncertainty

*Prerequisites: quantum mechanics.*

When Heisenberg layed down his uncertainty principle in 1927, it came
in two flavours: position-momentum and energy-time.
Schematically, these are usually written

$$
\Delta x \cdot \Delta p \gtrsim \hbar, \quad \Delta E \cdot
\Delta t \gtrsim \hbar.
$$

What we mean by uncertainty is a bit uncertain.
Often, the first semi-rigorous context we encounter these notions is
the *wavepacket*, i.e. a well-localized wavefunction in space $|\psi(x)\rangle$.
This has some spread of positions $\Delta x$, but we can Fourier
transform to momentum space, where it will have some spread $\Delta p$.
The uncertainty principle is then a mathematical result about the
Fourier transform, and in fact, it is true for any wavefunction, not
merely the well-localised ones.

We can derive the energy-time form for a wavepacket using the
following hack.
Let $\psi(x, t)$ denote the profile of the wavepacket.
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
wavepacket and $\Delta E$ is the corresponding energy spread.
Let $\Delta t$ be the time taken for the wavepacket to
travel the distance of its own spread, $\Delta x$, then $v\Delta t =
\Delta x$.
The position-momentum uncertainty principle then gives

$$
\Delta x \cdot \Delta p = v\Delta
t \cdot \Delta p \approx \frac{\Delta E}{\Delta p} \cdot \Delta
t \cdot \Delta p = \Delta E \cdot \Delta t \gtrsim \hbar.
$$

So we get the energy-time form of the uncertainty principle!

But it's very different from the position-momentum form.
Position and momentum are *bases* to measure the wavepacket in,
i.e. they correspond to legitimate quantum-mechanical operators.
Energy is also a legitimate operator; we call it the Hamiltonian.
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
[Mandelstam and Tamm](https://link.springer.com/chapter/10.1007/978-3-642-74626-0_8)
gave the first rigorous version of the energy-time uncertainty
relation.
It's important, because it tells us what it really means!
I'll present the nice proof from
[Levitin and Toffoli (2009)](https://arxiv.org/abs/0905.3417).
Consider some initial state $|\psi_0\rangle$ in a Hilbert space, which
evolves according to a Hamiltonian $H$ with eigenstates $|E_n\rangle$.
Averages with respect to this state are denoted $\langle A\rangle_0 =
\langle\psi_0|A|\psi_0\rangle$.
We can expand our state $|\psi_0\rangle$ and its time-evolved
counterpart in energy eigenstates as

$$
|\psi_0\rangle = \sum_n C_n |E_n\rangle, \quad |\psi_t\rangle = \sum_n
C_n e^{-i E_n t/\hbar} |E_n\rangle,
$$

with normalization giving $\sum_n |C_n|^2 = 1$.
Define the overlap

$$
O(t) = \langle \psi_0 | \psi(t)\rangle = \sum_n |C_n|^2 e^{-i E_n t/\hbar}.
$$

Motivated by the wavepacket example, we expect an energy-time relation
between the energy uncertainty $\Delta E = \sqrt{\langle
H^2\rangle_0 - \langle H\rangle_0^2}$, and the time $\tau$ taken to
evolve to a state with no overlap, $O(\tau) = 0$, i.e. a state which is perfectly distinguishable.
First, we write out the overlap squared:

$$
\begin{align*}
|O(t)|^2 & = \sum_{mn}|C_nC_m|^2 e^{i(E_m - E_n)t/\hbar} =\sum_{mn}|C_nC_m|^2 \cos\left[\frac{(E_m - E_n)t}{\hbar}\right].
\end{align*}
$$

The last equality follows because the overlap squared is real, so we can take the real
part of each term without prejudice.
To proceed, we need to invoke a slightly magical trigonometric
inequality (proved in the appendix),

$$
\cos x \geq 1 - \frac{4}{\pi^2}x \sin x - \frac{2}{\pi^2}x^2.
$$

Applied to the overlap squared, this yields

$$
\begin{align*}
|O(t)|^2 \geq 1 - &\frac{4}{\pi^2}\sum_{mn}|C_nC_m|^2
\sin\left[\frac{(E_m - E_n)t}{\hbar}\right]\frac{(E_m -
E_n)t}{\hbar} \\ - & \frac{2}{\pi^2}\sum_{mn} |C_nC_m|^2\left[\frac{(E_m -
E_n)t}{\hbar}\right]^2,
\end{align*}
$$

where the first term uses $\sum_{mn}|C_mC_n|^2 = 1$.
We can simplify this by observing that the second term is

$$
\sum_{mn}|C_nC_m|^2
\sin\left[\frac{(E_m - E_n)t}{\hbar}\right]\frac{(E_m -
E_n)t}{\hbar} = -t\frac{d}{dt}|O(t)|^2,
$$

which will vanish when $O(\tau) = 0$.
The last term is related to the energy spread, since

$$
\begin{align*}
\sum_{mn} |C_nC_m|^2(E_m - E_n)^2 & =\sum_{mn} |C_nC_m|^2(E_m^2 +
E_n^2 - 2E_m E_n) \\
& = 2\langle H^2\rangle - 2\langle H\rangle^2 =
2\Delta E.
\end{align*}
$$

Thus, we find that when $O(\tau) = 0$,

$$
0 \geq 1 - \frac{1}{\pi^2}\left(\frac{2t \Delta E}{\hbar}\right)^2.
$$

Rearranging gives the Mandelstam-Tamm form of the energy-time
uncertainty principle:

$$
\Delta E \cdot \tau \geq \frac{\pi \hbar}{2}.
$$

You might wonder if we could have manipulated things a different way
and obtained a different result.
In fact, we can!
We will need another magical inequality,

$$
\cos x \geq 1 - \frac{2}{\pi}(x + \sin x).
$$

Now just take the real part of $O(t)$:

$$
\begin{align*}
\Re[O(t)] & = \sum_n |C_n|^2 \cos(E_nt/\hbar) \\
	& \geq \sum_n |C_n|^2
	\left[1 - \frac{2}{\pi}\left(\frac{E_nt}{\hbar}+\sin\left(\frac{E_nt}{\hbar}\right)\right)\right]\\
	& = 1 - \frac{2 Et}{\pi \hbar} + \Im[O(t)],
\end{align*}
$$

where $E = \langle H\rangle$ is the average energy.
As before, when the state evolves to an orthogonal state with $O(\tau) = 0$, the real and
imaginary part vanish, and we are left with the uncertainty relation
of [Margolus and Levitin (1997)](https://arxiv.org/abs/quant-ph/9710043):

$$
E \tau \geq \frac{\pi \hbar}{2}.
$$

Both bounds are correct, so we use whichever is most constraining.
We'll call this combined bound the *Margolus-Levitin-Mandelstam-Tamm (MLMT) uncertainty relation*:

$$
\tau \geq \text{max}\left\{\frac{\pi\hbar}{2\Delta E}, \frac{\pi\hbar}{2E}\right\}.
$$

#### A conjecture about non-conservation and orthogonality

Let's return to the position-momentum version for a moment.
As before, for a state $|\psi\rangle$, we define the spread as the
standard deviation of expectations measured in the state:

$$
\Delta x = \sqrt{\langle x^2\rangle-\langle x\rangle^2}, \quad
\Delta p = \sqrt{\langle p^2\rangle -\langle p\rangle^2}.
$$

For this definition, the precise form of the uncertainty relation is
$\Delta x \cdot \Delta p \geq \hbar/2$.
The *canonical commutation relations* $[x, p] = i\hbar$ tell us that
position and momentum do not commute, and cannot be measured
simultaneously. Since this is true for any state, it is true that
$\langle[x, p]\rangle = i\hbar$.
So, we can rewrite position-momentum uncertainty as

$$
\Delta x \cdot \Delta p \geq \frac{1}{2} |\langle [x, p]\rangle|.
$$

In fact, it's a relatively straightforward exercise to generalise this to
*arbitrary* operators in a pure state:

$$
\Delta A \cdot \Delta B \geq \frac{1}{2}|\langle [A, B]\rangle|.
$$

This is called the *Robertson-Schrödinger uncertainty principle*
(continuing our pattern of double-barrel uncertainty relations) after
[Howard Percy Robertson](https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.163)
and Erwin Schrödinger.
The expectation of the commutator lower bounds the
product of uncertainties.
We can connect this to energy-time uncertainty by plugging in the
Hamiltonian for one of the operators:

$$
\Delta E \geq \frac{1}{2 \Delta A}|\langle [H, A]\rangle|.
$$

Levitin and Toffoli (2009) showed that Mandelstam-Tamm is sometimes
tight, so we assume it is the higher bound. In this case,

$$
\tau \leq \tau_A = \frac{\pi\hbar\Delta A}{|\langle [H, A]\rangle|},
$$

where $\tau_A$ is a "Mandelstam-Tamm-Robertson-Schrödinger" (MTRS) timescale
associated with $A$.
The time needed to evolve to an orthogonal
state has a bound made smaller by the amount of
*non-conservation* of $A$, as measured by $[H, A]$, and larger by the
variance $\Delta A$.
As a quick reminder, if $[H, A] = 0$, then the expectation of $A$ is
conserved by time evolution, since

$$
\begin{align*}
\langle A\rangle_t = \langle \psi(t)| A |\psi(t) \rangle & = \langle \psi(0)| e^{i H t/\hbar} A e^{-i H t/\hbar} |\psi(t)
\rangle \\
& = \langle \psi(0)| A e^{i H t/\hbar} e^{-i H t/\hbar} |\psi(t) \rangle = \langle A\rangle_0.
\end{align*}
$$

This connection seems physically reasonable.
If the expectation of $A$ is changing, it witnesses that
$|\psi(t)\rangle$ is becoming more distinguishable from $|\psi(0)\rangle$.
On the other hand, a large uncertainty $\Delta A$ washes out this effect, since $A$
is too blurry to usefully tell us about changes in the state.
In fact, I think the MTRS timescale should precisely be the time needed
for the state to become effectively distinguishable using $A$,
just like $x$ in the wavepacket case, but I haven't been able to show
this formally yet.
But guided by the wavepacket example, I would expect that after
$\tau_A$, we have a statement like

$$
\langle A\rangle_{\tau_A} - \langle A\rangle_{0} \sim \Delta A.
$$

In other words, I think the expectations should change by the spread
of $A$ in the initial state.

#### Virtual particles

We'll now turn to a specific example of $A$: *particle number*.
The basic setup requires a Fock space, which we take to be bosonic for
simplicity.
We have a set of creation and annihilation operators $a_i^\dagger,
a_i$, satisfying commutation relations

$$
[a_i, a^\dagger_j] = \delta_{ij}.
$$

The states take the form of products of single particle states built
by acting on the vacuum with creation operators:

$$
|n_1, n_2, \ldots, n_k\rangle = C (a_1^\dagger)^{n_1}\cdots (a_k^\dagger)^{n_k}|0\rangle,
$$

for a normalisation constant $C$.
The *number operator* $N_i = a_i^\dagger a_i$ counts the number of $i$
quanta, since the commutation relations imply

$$
N_i |n_1, n_2, \ldots, n_k\rangle = n_i |n_1, n_2, \ldots, n_k\rangle.
$$

Now, this is all static; it has nothing to do with the Hamiltonian.
In particular, *particle number need not be conserved*.
A state may have a well-defined particle number, with $\Delta N_i$
small, but the expected number of particles can change quickly
depending on the commutator $[H, N_i]$.
The particles which appear out of nowhere, or rather, by virtue of
time evolution, are precisely virtual particles!
We know the state will become distinguishable after the MTR timescale,

$$
\tau_i = \frac{\pi\hbar\Delta N_i}{|\langle [H, N_i]\rangle|},
$$

and indeed, if my little hypothesis is correct, they will become
distinguishable with $N_i$.

#### References

<!-- - ["Energy Cost of Information Transfer"](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.46.623)
  (1981), Jakob D. Bekenstein. -->
<!-- - ["Quantum noise and information"](https://projecteuclid.org/euclid.bsmsp/1200513783)
  (1967), H. J. Bremmerman. -->
- ["Quantum speed limits: from Heisenberg’s
uncertainty principle to optimal quantum control"](https://arxiv.org/abs/1705.08023)
(2017), Sebastian Deffner and Steve Campbell.
- ["Ultimate physical limits to computation"](https://arxiv.org/abs/quant-ph/9908043) (2000), Seth Lloyd.
- ["The fundamental limit on the rate of quantum dynamics: the unified bound is tight"](https://arxiv.org/abs/0905.3417) (2009), Lev B. Levitin and
  Tommaso Toffoli.
- ["The uncertainty relation between energy and time in non-relativistic quantum mechanics"](https://link.springer.com/chapter/10.1007/978-3-642-74626-0_8)
  (1945), L. Mandelstam and Ig. Tamm.
- ["The maximum speed of dynamical evolution"](https://arxiv.org/abs/quant-ph/9710043) (1997), Norman Margolus, Lev B. Levitin.
- ["The uncertainty principle"](https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.163) (1929), H. P. Robertson.

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

#### Appendix: magical inequalities
