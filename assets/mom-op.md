---
Layout: post
mathjax: true
comments: true
title:  "The momentum operator and Schrödinger's equation"
categories: [Maths, Physics, Hacks]
date:  2021-04-17
---

**April 17, 2021.** *A quick (and hand-wavey) post explaining how matter waves lead to
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
of a photon, also suggested by Einstein in 1905 to
[explain why](https://en.wikipedia.org/wiki/Photoelectric_effect)
shining a light on a bit of metal releases electrons in a way that
depends only on the colour of the light and not how bright it is.
The answer: the light isn't interacting with electrons as a wave, but
as a *particle*, with energy per particle given by

$$
E = hf,
$$

where $f$ is the frequency (oscillations per second) and $h = 6.63 \times 10^{-34} \text{ J s}$ is *Planck's constant*.
Using our two expressions for the energy, we find that the momentum of
a photon is

$$
p = \frac{hf}{c}.
$$

You can use to compute how many laser pointers you would need to repel
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

Here, $v$ is the *speed* of the wave, since a point of fixed $C = x -
vt$ in time $\Delta t$ must move

$$
C = x - vt = (x + \Delta x) - v (t + \Delta t) = C + \Delta x -v
\Delta t \quad \Longrightarrow \quad \frac{\Delta x}{\Delta t} = v.
$$

Or, we can use the [exponential](https://hapax.github.io/maths/physics/hacks/exponential/)
