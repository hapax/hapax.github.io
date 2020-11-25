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
If the light has frequency $\omega$, one of these bundles has energy

$$
E = \hbar \omega, \quad \hbar \sim 10^{-34} \text{ J s},
$$

where $\hbar$ is called *Planck's constant*.

A few years later, Einstein used Planck's assumption to explain how
light makes electricity (as in solar cells, for instance).
Let's talk briefly about what Einstein did.
At an atomic level, a chunk of metal is a dense array of
positively-charged nuclei, bathed in a sea of negatively charged
electrons.
The electrons are not bound to any nucleus in particular, but rather
to the positively-charged array as a whole.
If we want to liberate an electron from the sea, we need to give it
some minimum amount of energy $\epsilon$, called the *binding energy*.
One way to supply that energy is to 
