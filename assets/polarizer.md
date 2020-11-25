---
Layout: post
mathjax: true
comments: true
title:  "From sunglasses to quantum secrets"
date:  2020-12-07
---

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Fun with photons</a>
   1. <a href="#sec-2-1">Light is a particle</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

In this tutorial, we'll be introducing quantum mechanics in a simple,
experimentally motivated way. From the apparently unremarkable fact
that you can see through sunglasses, we will learn about the quantum
nature of light, and end by exchanging quantum secrets and teleportation!

## 2. Fun with photons <a id="sec-2" name="sec-2"></a>

According to Maxwell's laws, light is a self-propagating
electromagnetic wave: a changing electric field creates a changing
magnetic field, which in turn gives rise to a changing electric field.
It's like a perpetual motion machine!
Unlike their mechanical counterparts, this "machine" is allowed by the laws of nature.
The wave-like nature of light explains common phenomena like rainbows,
transparency, or the fringes you see when you shine a pocket laser at
a thread of hair.
But there is more to light than meets the eye.

### 2.1. Light is a particle <a id="sec-2-1" name="sec-2-1"></a>

In the early 20th century, experiments began to suggest there was
something amiss with this wave picture.
On the one hand, assuming light is a continuous, wave-like disturbance
implies that a lump of hot coal emits an infinite amount of
energy. Clearly, this can't be true, and
[Max Planck](https://en.wikipedia.org/wiki/Max_Planck#Black-body_radiation)
figured out that to get the right answer, light needs to come into
discrete bundles of energy called *quanta*.
If the light has angular frequency $\omega = 2\pi f$, one of these bundles has energy

$$
E = \hbar \omega, \quad \hbar \sim 10^{-34} \text{ J s},
$$

where $\hbar$ is called *Planck's constant*.
A few years later, Einstein used Planck's quanta to explain how
light creates electricity (the basis of solar panels, for instance).
Briefly, the idea is as follows.
At an atomic level, a chunk of metal looks like a rigid array of
positive nuclei surrounded by a free-flowing sea of negative
electrons.
Electrons are not bound to any nucleus in particular, just to the
chunk as a whole.
To pull an electron out of the chunk, we need to give it some minimum
energy $\epsilon_\text{bind}$ called the *binding energy*.
We can create a sort of electrostatic hoover which sucks up any
free electrons and tells us when they have been liberated.

We can deliver energy by shining a torch on the chunk.
Classically, this is identical to the way ocean waves deposit energy on the shore.
To complete the analogy, imagine the electron as a beach ball
sitting in a small dip in the sand.
An arriving wave will continuously deliver energy to the ball until it
gets enough ($\epsilon_\text{bind}$) to be dislodged from the dip.
The waves could be very high, or arrive one after the other in quick
succession, but it makes no difference to the beach ball.

For light, the equivalent of the height of waves is the *amplitude* $A$
and the rate waves come in is the frequency $\omega$.
If light is like the waves trying to dislodge the beach ball, we
expect that we could liberate electrons either by making $A$ big or
$\omega$ big.
But experimentalists noticed that, weirdly, for a given metal, below a
certain frequency electrons would never be liberated, no matter what
the intensity of the torchlight!
This is very surprising, almost like a low-frequency tsunami failing
to dislodge the beach ball.
What gives?

Einstein's explanation was simple.
He took Planck's idea that light carried energy in discrete lumps $E =
\hbar\omega$ depending only on frequency, and deposits it to the
electrons as a lump sum.
In other words, we need

$$
E = \hbar\omega > \epsilon_\text{bind}.
$$
