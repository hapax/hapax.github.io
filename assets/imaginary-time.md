---
Layout: post
mathjax: true
comments: true
title:  "Imaginary time"
categories: Physics
date:  2018-20-20
---

**October 20, 2018.** *What the heck is imaginary time? It's a trick
which turns heat into geometry. More precisely, hot systems repeat
themselves in time. This perspective leads to a quick proof of the Unruh effect
(empty space looks hot when you accelerate) and with a little
more work, to Hawking radiation (black holes are hot since observers
near the horizon accelerate).*

## Introduction

*Prerequisites: quantum mechanics, statistical mechanics, special relativity.*

Thermodynamic systems, like light bulbs and puddles, consist of many
components bouncing around and interacting randomly.
Rather than predict what will happen exactly, it
makes more sense to consider a probability distribution over
configurations of the system, also called an *ensemble*.
There are different sensible choices, depending on experimental
conditions, but they all yield the same answers when you have lots of
particles.

The easiest to work with is the *canonical ensemble*, where the
temperature $T$ is fixed.
The probability of seeing a state with energy $E$ dies off
exponentially, and is controlled by the ratio of $E$ to the characteristic
thermal energy, $k_B T$, where $k_B$ is Boltzmann's constant:

$$
p_\beta(E) \propto e^{-\beta E}.
$$

We can immediately write down the full probability distribution, using
the fact that it must be unit normalised:

$$
p_\beta(E) = \frac{1}{Z[\beta]}e^{-\beta E}, \quad Z[\beta] = \sum_{E} n(E) e^{-\beta E}.
$$

Here, $n(E)$ is the *density of states*, telling us roughly how
many ways the system can be at energy $E$ (or more precisely, what
volume of classical phase space they occupy).
The normalisation factor $Z[\beta]$ is called the *partition
function*, which captures all the statistical properties of the system.
A simple example is the average energy of the system:

$$
\langle E \rangle = \sum_E n(E) p_\beta(E) E = \frac{\sum_E n(E) e^{-\beta E}
E}{\sum_E \rho(E) e^{-\beta}} = \frac{-\partial_\beta Z[\beta]}{Z[\beta]} =
-\partial_\beta \ln Z[\beta].
$$

Another example is the *Helmholtz free energy* $F = -k_B T \ln
Z[\beta]$, which is minimised in equilibrium.
Put a different way, free energy tells us how to how density of states
balances exponential suppression of high energy states.

## Quantum statistical mechanics

The partition function also controls the statistics of *quantum*
thermodynamic systems.
Instead of a probability distribution $p_\beta$ over classical
configurations, we have a probability distribution over *quantum
states*, which is once again exponential:

$$
\rho_\beta = \frac{1}{Z[\beta]}\sum_E e^{-\beta E}|E\rangle\langle E|,
$$

where $Z[\beta]$ is once again a normalisation.
Here, we are using Dirac's bra-ket notation, and $|E\rangle\langle
E|$ projects onto the energy eigenstate $|E\rangle$, and for
simplicity, we assume no degeneracy of energy eigenstates.
Instead of having unit norm, the density $\rho_\beta$ is defined to have unit
*trace*:

$$
1 = \mbox{Tr}[\rho_\beta] = \frac{1}{Z[\beta]}\sum_E e^{-\beta
E}\mbox{Tr}[|E\rangle\langle E|] = \frac{1}{Z[\beta]}\sum_E e^{-\beta
E} \quad \Longrightarrow \quad Z[\beta] = \sum_E e^{-\beta E}.
$$

The normalisation is precisely the partition function $Z[\beta]$, as
before.

There is a nicer way to write the density $\rho_\beta$.
What is an energy eigenstate?
Well, it's just an eigenvector of the system's *Hamiltonian*
$\hat{H}$, with $\hat{H}|E\rangle = E|E\rangle$.
But by a standard linear algebra trick, we can write any
diagonalisable operator as a sum of projectors onto its eigenvectors,
weighted by its eigenvalues:

$$
\hat{H} = \sum_E E |E\rangle \langle E.
$$

It follows that

$$
\rho_\beta = \frac{1}{Z[\beta]}e^{-\beta \hat{H}}, \quad \mbox{Tr}[e^{-\beta \hat{H}}] = Z[\beta].
$$

So the density and partition function can be written simply in terms
of the Hamiltonian.

## Amplitudes and Wick rotation

The connection to imaginary time comes through the Hamiltonian.
First, recall that the *Schrödinger equation* tells us how to evolve a
state $|\psi\rangle$ of the system using the Hamiltonian.
This is simple to solve when the Hamiltonian itself is time-independent:

$$
i\hbar \partial_t |\psi(t)\rangle = \hat{H}|\psi(t)\rangle \quad
\Longrightarrow \quad |\psi(t)\rangle  = e^{-i\hat{H}t}|\psi(0)\rangle.
$$

We call $e^{-i\hat{H}t} = U(t)$ the *propagator*.
The amplitude for a system to go from state $|\phi\rangle$ to
$|\varphi\rangle$ in time $t$ is just

$$
\langle\phi|U(t)|\varphi\rangle,
$$

since the $U(t)$ updates the state, and the overlap with the bra
$\langle\phi|$ tells us "how much" of $|\phi\rangle$ is in the evolved
state $|\varphi(t)\rangle$.

We can look at the density matrix $\rho_\beta$ in terms of transition
amplitudes.
Instead of discussing transitions between pure states, we can now
consider the probability of 

$$

$$

---

**Exercise 1.** *Statistical mechanics.*

1. Show that, when the 

---

## Rindler coordinates and the Unruh effect

Let's now turn from quantum mechanics to special relativity.
To keep life simple, we stick to two dimensions with Minkowski
coordinates $(t, x)$.
Recall that the signed distance $s^2$ from the origin to a point in
spacetime $P(t, x)$ is given by

$$
s^2 = -t^2 + x^2.
$$

For small displacements, this defines the *Minkowski metric*

$$
ds^2 = -dt^2 + dx^2.
$$

The curves at fixed distance $s^2 > 0$ from the origin are hyperbolas
covering the east-west quadrants.
We can use these hyperbolas to
define a new coordinate system on, say, the east quadrant:

$$
x = \alpha^{-1} \cosh\xi, \quad t = \alpha^{-1} \sinh\xi.
$$

Note that $s^2 = \alpha^{-2}$ on a hyperbola, and $t = x \tanh\xi$ for
fixed $\xi \in \mathbb{R}$.
Thus, we can draw our coordinates as follows:

---

**Exercise 2.** *Rindler coordinates.*
1. Verify the geometric description of $\alpha, \xi$ above.
2. For an observer on a fixed hyperbola labelled by $\alpha$, verify
   that their proper time is $\alpha \xi$ and their proper
   acceleration has magnitude $\alpha$.
   This gives a second way of interpreting Rindler coordinates.
3. Show that the Minkowski metric in Rindler coordinates is

    $$
    ds^2 = -\frac{1}{\alpha^2}d\xi^2 + \frac{1}{\alpha^4} d\alpha^2.
    $$

4. Defining $\rho = 1/\alpha$, show that the metric takes the simple form

    $$
    ds^2 = -\rho^2\, d\xi^2 + d\rho^2.
	$$

---

To understand the thermal properties of Rinder coordinates, we
go to imaginary time, $\xi = -i \theta$.
This leads to the metric

$$
ds^2 = \rho^2\, d\theta^2 + d\rho^2.
$$

This is precisely the metric on a disk, with radius $\rho$ and polar
angle $\theta$.
If this language of metrics is confusing, we can see it explicitly from the change of
coordinates:

$$
x = \rho \cosh(-i\theta) = \rho\cos\theta, \quad \tau = it = i\rho
\sinh(-i\theta) = \rho \sin\theta.
$$

Of course, the period in imaginary time depends on whether we choose
$\tau$, $\theta$, or the imaginary proper time $\alpha\theta$.
It turns out that *temperature is in the eye of the beholder*, and we
must choose the imaginary proper time to determine the energies they
will measure.
Since the proper time is $\alpha\xi$, the period in proper
imaginary time is $2\pi \rho$.
Recalling our mantra, we are led to predict that the "system" --- empty
space --- appears thermal, with temperature

$$
T_\text{U} = \frac{\alpha}{2\pi}.
$$

The fact that empty space looks thermal to an accelerating observer is
called the *Unruh effect*, and $T_\text{U}$ the *Unruh temperature*.
If we restore the factor of $\hbar$ omitted from Schrödinger's
equation, the factor of $k_\text{B}$ omitted from the inverse
temperature $\beta$, and the factor of $c$ omitted from the Minkowski
metric, we get the expression

$$
T_\text{U} = \frac{\hbar \alpha}{2\pi k_\text{B} c}.
$$

You may be wondering where quantum mechanics enters the picture here.
Roughly, *space itself* is the quantum system due to the existence of
quantum fields, such as the photon, which can be excited at any location.
This means that an accelerating observer will see a thermal bath of
photons at the Unruh temperature.
We can derive this result rigorously (see the references), but
imaginary time gives us a nice shortcut!

## Hawking radiation from Newtonian gravity

Black holes are attractive, and therefore induce acceleration at the event horizon.
The Unruh effect, combined with the equivalence principle, then
*implies* the existence of Hawking radiation.
In the next section, we will show this a bit more carefully using a
few basic ideas from general relativity.
Here, we will content ourselves with a *Newtonian* argument which,
although it is physically misleading, gives the right answer.

Imagine a black hole of mass $M$ at the origin of flat space.
The classical escape velocity for a test particle of mass $m$ a
distance $r$ away is given by equating the kinetic and potential
energies and solving for $v$:

$$
\frac{GMm}{r} = \frac{1}{2}mv^2 \quad \Longrightarrow \quad v^2 = \frac{2GM}{r}.
$$

To find the event horizon $r_\text{h}$ of the black hole, we simply set the escape
velocity to the speed of light $v = c$, modelling the point at which
not even light can escape:

$$
r_\text{h} = \frac{2GM}{c^2}.
$$

An observer sitting at the horizon wants to fall into the black hole,
and needs to accelerate *away* in order just to remain stationary.
The acceleration needed is

$$
\alpha = \frac{GM}{r_\text{h}^2} = \frac{c^4}{4GM}.
$$

If we forget all about spacetime curvature, and just imagine that an
observer hovering at the black hole horizon is accelerating at
$\alpha$ in flat space, we expect a version of the Unruh effect with temperature

$$
T_\text{H} = \frac{\hbar \alpha}{2\pi k_\text{B} c} = \frac{\hbar c^3}{8\pi k_\text{B} GM}.
$$

This is precisely the temperature predicted by Hawking!
Our imaginary time approach leads us (via some Newtonian
sleight-of-hand) to the incredible conclusion that black holes radiate.

## Hawking radiation from Euclidean gravity*

The preceding argument is cute, but gravity is not Newtonian!
We can fix it up using some tools from general relativity, focusing on
spherically symmetric black holes for simplicity.
When we Wick rotate, the signature of the metric becomes Euclidean,
and so this version of general relativity is called *Euclidean gravity*.
Imagine an observer far from the black hole, who has proper time $t$
and sets up spherical coordinates with radial coordinate $r$ and the
black hole at $r = 0$.
In these coordinates, small displacements have signed length given by
the *Schwarzschild metric*:

$$
ds^2 = -f(r)\, dt^2 + \frac{1}{f(r)} dr^2 + \cdots
$$

where $f(r)$ is a function we'll discuss in a moment, and the
$\cdots$ indicate additional spherical coordinates that wont' matter
to us.

Let's consider an outgoing radial null ray with parameter $\lambda$,
and radial position $r(\lambda)$ obeying

$$
0 = -f(r)\, \dot{t}^2 + \frac{1}{f(r)} \dot{r}^2 \quad \Longrightarrow
\quad \frac{\dot{r}}{\dot{t}} = \frac{dr}{dt} = f(t).
$$

We see that if $f(r) = 0$, an outgoing light ray will be "stuck".
Since nothing travels faster than light, *nothing* will be able to
leave the region $r < r_\text{h}$ for an *event horizon* where
$f(r_\text{h}) = 0$.

Suppose that at the horizon, the function $f$ vanishes but has nonzero
derivative, i.e. Taylor-expanding to first order gives

$$
f(r) \approx f(r_\text{h}) (r - r_\text{h}) + \cdots
$$

Then to first order, we can expand the Schwarzschild metric as

$$
ds^2 = -f'(r_\text{h})(r-r_\text{h}) \, dt^2 +
\frac{1}{f'(r_\text{h})(r-r_\text{h})} dr^2 + \cdots
$$

Let's go to imaginary time and define new coordinates $\rho, \theta$ by

$$
\rho^2 = \frac{4(r-r_\text{h})}{f'(r_\text{h})}, \quad \theta =
-\frac{1}{2}i|f'(r_\text{h})| t.
$$

Substituting these back into the metric, we get

$$
ds^2 = \rho^2 \, d\theta^2 + d\rho^2 + \cdots
$$

---

**Exercise 2.** *Euclidean black holes.*
1. Do the algebra to deduce the metric above.
2. Adapt the argument for a metric

    $$
    ds^2 = -f(r)\,dt^2 + \frac{1}{g(r)}dr^2 + \cdots
	$$

	where both $f, g$ vanish at $r = r_\text{h}$ but have nonvanishing
    derivatives.

---

Ignoring the $\cdots$, this is precisely the form of the metric we saw
in Rindler coordinates!
We learn that the near-horizon region of a black hole resembles
Rindler coordinates on flat space.
Moreover, for the imaginary proper time associated to the far away
observer, the period is $4\pi/|f'(r_\text{h})|$.
Hence, from afar, the black hole looks hot, with temperature

$$
T_\text{H} = \frac{|f'(r_\text{h})|}{4\pi}.
$$

Now consider a spherically symmetric black hole in four dimensions.
Our earlier Newtonian argument, or the correct general relativistic argument, shows
that there is a horizon at $r_\text{h} = 2GM$.
The relevant choice of $f(r)$ (which solves Einstein's equation) is

$$
f(r) = \frac{r - 2GM}{r} \quad \Longrightarrow \quad f(2GM) = 0, \quad f'(2GM) = \frac{1}{2GM}.
$$

Plugging this into our expression for the Hawking temperature, we
recover our earlier, somewhat dodgy Newtonian result

$$
T_\text{H} = \frac{1}{8\pi GM}.
$$

The advantage of talking about things this way is that we can
calculate temperatures for a much wider range of black holes.

---

**Exercise 3.** *Hot black holes in higher dimensions.*
In $d$ dimensions, a Schwarzschild black hole is associated with a
function

$$
f(r) = 1 -\frac{\mu}{r^{d-3}}
$$

for some constant $\mu \propto GM$.
Show that the temperature is

$$
T_\text{H} = \frac{d-3}{4\pi}(2\mu)^{-1/(d-3)}.
$$

---

## Conical deficits and cigars*

In deriving both the Unruh and Hawking effect, I've made a subtle
assumption about the Euclidean geometry: the absence of a *conical
deficit*.
A conical deficit occurs when the polar angle $\theta$ subtends less
than $2\pi$, so that the geometry of a circle is wrapped up into a cone.
We can easily see how this happens from a picture:

There is a simple way of seeing this doesn't happen, for either
Rindler coordinates or black holes,

## Conclusion

## References

## Extra

A unitary operator is an inner-product preserving change of basis, so
the propagator just moves probability amplitude around the system.

Physically, at a finite temperature $T$, energies $E_n \gg k_\text{B} T$ are
exponentially suppressed.

Since $\hat{H}$ is Hermitian, it follows that $U(t)$ is unitary:

$$
U(t)^\dagger U(t) = e^{+i\hat{H}^\dagger t}e^{-i\hat{H}t} =
e^{+i\hat{H} t}e^{-i\hat{H}t} = \mathbb{I}.
$$

(For a stable system, we need a ground state, and we can always shift
the energy so that this is positive. The requirement is not essential
but makes things a bit simpler.)

Alternatively, using the rule for conditional probabilities,

$$
\mathbb{P} (A | B) = \frac{\mathbb{P} (A \cap B)}{\mathbb{P} (B)},
$$

we can also view $P(B) \propto Z[\beta]$, and the normalisation as
conditioning on the system being at fixed temperature $T$.

We can think of the terms $e^{-\beta E_n}$ as unnormalised
probabilities for the system to have energy $E_n$, and $Z[\beta]$ as
the normalisation factor.

Let's return to our earlier, real-time expression $\mathcal{A}(\text{periodic in } t)$.
Let $\{|n\rangle\}$ is the energy eigenbasis with energies $\{E_n\}$.
Surprisingly, the amplitude for the system to be *periodic in
imaginary time* $\tau = \beta$ is precisely the canonical partition $Z[\beta]$:

$$
\mathcal{A}(\text{periodic in } -i\beta) = \mbox{Tr}\left[e^{-\hat{H}\beta}\right] = \sum_n \langle
n|e^{-\hat{H}\beta}|n\rangle = \sum_n e^{-\beta E_n} = Z[\beta].
$$

This suggests that we view a thermal system as one which is periodic
in imaginary time.
It's possible to check this works using the tools 

We can make this analogy more precise, but this is the main formal
trick and the key physical idea.

We also note that since $\alpha$ fixes the hyperbola, we can view
$\xi$ as parameterising boosts to the observer.

There are in fact two strategies here:
- a direct argument based on the resemb

There is something peculiar about Rindler coordinates on the east
wedge.
Since an accelerating observer never leaves the wedge, they can never
receive any signals from the west or north wedge.
Effectively, there is a *horizon*, just like the event horizon of a
black hole.

We will focus on simple black holes, with no charge or spin, for
simplicity.

Fixing $\xi$, we get the straight line

$$
\frac{t}{x} = \tanh\xi.
$$

Fixing $\alpha$, we obtain

$$
ds^2 = -\frac{1}{\alpha^2}[\cosh^2\xi - \sinh^2\xi]\, d\xi^2 = -\frac{1}{\alpha^2}d\xi^2,
$$

so $\xi/\alpha$ is the proper time of an observer moving on the
hyperbola labelled by $\alpha$.

Keeping $\alpha$ fixed, we can obtain the proper acceleration from the
second derivative with respect to proper time:

$$
\frac{\partial^2}{\partial (\xi/\alpha)^2} x^\mu = \alpha^2 x^\mu =
\alpha (\sinh \xi, \cosh\xi),
$$

which has length $\alpha$.
Thus, $\alpha$ is the magnitude of proper acceleration along the hyperbola.

both in $t$ and $\xi$:

$$
t = -i\tau,\quad \xi = -i \theta.
$$

The change of coordinates is now

$$
x = \alpha^{-1} \cos \theta, \quad \tau = \alpha^{-1} \sin\theta.
$$

In other words, $x$ and $\tau$ parameterise the position on a circle
with period $2\pi\alpha^{-1}$ in imaginary time.
But recall our earlier mantra, that periodicity in imaginary time
means the system is thermal?
That's exactly what we have here!
Define

If we restore the factor of $\hbar$ omitted from Schrödinger's
equation, and the factor of $c$ omitted from the Minkowski metric,
we get the formula

$$
T_\text{U} = \frac{\hbar \alpha}{2\pi k_\text{B} c}.
$$

Consider a quantum system with Hilbert space $\mathcal{H}$ and a
time-independent, Hermitian Hamiltonian $\hat{H}$.
Schrödinger's equation states that $\hat{H}$ is the time evolution
operator, which we can formally solve with an exponential:

$$
i\partial_t |\psi(t)\rangle = \hat{H}|\psi(t)\rangle \quad \Longrightarrow
\quad |\psi(t)\rangle = e^{-i\hat{H}t}|\psi(0)\rangle.
$$

This exponential is the *propagator* $U(t) = e^{-i\hat{H}t}$, and I
can use it to evolve any state forward in time.
Recall that the *transition amplitude* to go from an initial state
$|\psi\rangle$ to a final state
$|\phi\rangle$ in time $t$ is obtained by evolving
$|\psi\rangle$ forward in time, then taking the overlap with the bra
$\langle \phi|$:

$$
\mathcal{A}(\phi, \psi; t) = \langle \phi| U(t)|\psi\rangle.
$$

If $|\psi\rangle = |\phi\rangle$, we have the probability the
system returns to the state it started in in time $t$.
For an orthonormal basis $\{|n\rangle\}$ of $\mathcal{H}$, the
amplitude for the system to be *periodic* in time $t$ is just the sum over $\{|n\rangle\}$:

$$
\mathcal{A}(t) = \sum_n \langle n| U(t)|n\rangle.
$$

So far, our discussion has assumed that $t$ is real.
But what happens if we plug $t = -i\tau$ into the propagator?
Formally making time imaginary is called a *Wick rotation*.
Instead of evolving unitarily, it will squash things exponentially:

$$
U(-i\tau) = U_E(\tau) = e^{-\hat{H}\tau}.
$$

If we expand in eigenvectors of $\hat{H}$, we see that when we evolve
in imaginary time $\tau$, things get suppressed according to their energy.
But this should remind us of thermal systems!
Indeed, recall that for a system with energies $\{E_n\}$, the canonical
partition function at temperature $T = 1/\beta$ is

$$
Z[\beta] = \sum_n e^{-\beta E_n}.
$$

This is precisely the "amplitude" for the system to be *periodic in
imaginary time* $\beta$:

$$
\mathcal{A}(-i\beta) =
\sum_n \langle n|e^{-\hat{H}\beta}|n\rangle = \sum_n e^{-\beta E_n} = Z[\beta].
$$

Since the partition function encodes the statistical properties of a
thermal system, this suggests we should view thermal systems as those
which are periodic in imaginary time.
We could expend more effort justifying this, but the connection
between propagators and partition functions is the main idea.
So, although it sounds crazy, repeat after me: if a system is periodic
in imaginary time $\beta$, we can regard it as thermal
at temperature $T = 1/\beta$.
