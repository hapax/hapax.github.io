---
Layout: post
mathjax: true
comments: true
title:  "Momentum and Schrödinger's equation"
categories: [Maths, Physics, Hacks]
date:  2021-04-17
---

**April 17, 2021.** *A quick post explaining how matter waves lead to
  (a) the identification of momentum operator with derivatives, and
  (b) the Schrödinger equation.*

#### Light and matter

We learnt in a
[previous post](https://hapax.github.io/physics/mathematics/hacks/emcc/)
that Einstein's famous formula $E = mc^2$ can also be written

$$
E^2 = m_0^2 c^4 + p^2 c^2,
$$

where $m_0$ is the rest mass of the object we're considering and $p$
its momentum.
If the object happens to be a *massless* particle, say a photon of
light, then $m_0 = 0$ and we end up with the curious identity:

$$
E = pc.
$$

Now, it just so happens we have a different expression for the energy
of a photon. This was also proposed by Einstein in 1905, to
[explain why](https://en.wikipedia.org/wiki/Photoelectric_effect)
shining a light on a bit of metal releases electrons only when the
colour is blue enough.
Conceptually, light isn't interacting with electrons as a wave, but
as a *particle* whose energy is determined by colour!
The experimental results show that the energy per photon is given by

$$
E = hf,
$$

where $f$ is the frequency (oscillations per second) and $h = 6.63 \times 10^{-34} \text{ J s}$ is *Planck's constant*.
Using our two expressions for the energy, we find that the momentum of
a photon is

$$
p = \frac{hf}{c}.
$$

You can use this to compute how many laser pointers you would need to repel
an incoming asteroid (exercise left to the reader).

#### Plane waves

But if we zoom out from the photon, or rather, *measure it
differently*, say by getting it to
[diffract](https://en.wikipedia.org/wiki/Diffraction) through some
slits rather than disloding individual electrons from a metal, it will
be described by a wave.
For simplicity, let's consider a single spatial dimension $x$.
A *plane wave* is a simple sinusoidal displacement of some medium
(e.g. air pressure, the surface of a body of water, electromagnetic
fields) with amplitude

$$
A(x, y) = A_0 \sin \left[k(x - vt)\right].
$$

The constant $A_0$ is just the maximum size of the envelop, but $k$
and $v$ require a bit more explanation.
Here, $v$ is the *speed* of the wave, since a point of fixed $C = x -
vt$ in time $\Delta t$ must move $\Delta x$ obeying

$$
C = x - vt = (x + \Delta x) - v (t + \Delta t) = C + \Delta x -v
\Delta t \quad \Longrightarrow \quad \frac{\Delta x}{\Delta t} = v.
$$

If we take a snapshot of the wave at fixed time $t$, then it will
repeat itself when the argument of the sine function is increased by
$2\pi$, or

$$
k(x - vt) \mapsto k(x - vt) + 2\pi = k\left(x + \frac{2\pi}{k} - vt\right).
$$

Since $t$ is fixed, it follows that when we increment $x$ by $2\pi/k$,
the wave repeats itself. In other words, $\lambda = 2\pi/k$ is the
*wavelength*.
By the same reasoning, if we freeze $x$ the wave repeats itself with a
period in time,

$$
T = \frac{2\pi}{vk}.
$$

Since the frequency $f = 1/T$ is the inverse of the period, we find
that frequency times wavelength equals speed:

$$
f\lambda = \frac{vk}{2\pi}\cdot \frac{2\pi}{k} = v.
$$

At this point, It will simplify things dramatically to use the
[exponential](https://hapax.github.io/maths/physics/hacks/exponential/)
instead of the sine wave.
Since Euler's marvellous formula tells us that

$$
e^{i\theta} = \cos\theta + i \sin\theta,
$$

we can replace the sinusoid with

$$
A(x, t) = A_0 e^{i k(x - vt)},
$$

and if we really want the sine, just consider the imaginary part.

#### Adding and extracting momentum

Let's now consider a photon, moving at speed $v =c$ and with momentum
obeying

$$
p = \frac{hf}{c} = \frac{hf}{f \lambda} = \frac{h}{\lambda} =
\frac{h}{2\pi}\cdot \frac{2\pi}{\lambda} = \hbar k,
$$

where we used $c = f\lambda$, $k = 2\pi/\lambda$, and defined a new
constant $\hbar = h/2\pi$, called *Planck's reduced constant*.
This lets us rewrite the plane wave as

$$
A(x, t) = A_0 e^{i (p/\hbar)(x - ct)}.
$$

In 1924, Louis de Broglie made the bold suggestion that *matter could
also be described as a wave*.
These matter waves would have the usual momentum (now taken to be
slowly moving and non-relativistic) $p = mv$, but frequency given by
$p = hf/v$. Identical reasoning gives a plane matter wave

$$
A(x, t) = A_0 e^{i (p/\hbar)(x - vt)}.
$$

This could describe an electron, a proton, or something as absurd as a
[buckyball](https://www.nature.com/articles/44348), passing for
instance through two slits and recombining to exhibit wavelike
interference. Pretty nifty!

We won't be concerned with this, however.
Instead, we would like to think how to *extract* the momentum from a
plane wave.
One way is to rearrange $A(x, t)$ to find $p$.
Instead, we will define a procedure which simply pulls $p$ out.
It is, as you have probably already guessed, simply the derivative
with respect to $x$:

$$
\frac{\partial}{\partial x}A(x, t) = A_0 \frac{\partial}{\partial
x}e^{i (p/\hbar)(x - vt)} = A_0 \frac{ip}{\hbar}e^{i (p/\hbar)(x -
vt)} = \frac{ip}{\hbar} A(x, t).
$$

The *momentum operator* $\hat{p}$ is simply defined as a derivative which gives
us $p$ without the extra constants. We will usually treat $t$ as a
constant, so that the partial derivative becomes an ordinary derivative:

$$
\hat{p} = -i\hbar \frac{d}{d x}.
$$
