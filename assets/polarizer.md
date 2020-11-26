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
   2. <a href="#sec-2-2">Flashlights and sunglasses</a>
   3. <a href="#sec-2-3">The law of Malus</a>

### 1. Introduction <a id="sec-1" name="sec-1"></a>

In this tutorial, we'll be introducing quantum mechanics in a simple,
experimentally motivated way. From the apparently unremarkable fact
that you can see through sunglasses, we will learn about the quantum
nature of light, and end by exchanging quantum secrets and teleportation!

### 2. Fun with photons <a id="sec-2" name="sec-2"></a>

According to Maxwell's laws, light is a self-propagating
electromagnetic wave: a changing electric field creates a changing
magnetic field, which in turn gives rise to a changing electric field.
It's like a perpetual motion machine!
Unlike their mechanical counterparts, this "machine" is allowed by the laws of nature.
The wave-like nature of light explains common phenomena like rainbows,
transparency, or the fringes you see when you shine a pocket laser at
a thread of hair.
But there is more to light than meets the eye.

#### 2.1. Light is a particle <a id="sec-2-1" name="sec-2-1"></a>

In the early 20th century, experiments began to suggest there was
something amiss with this wave picture.
Most dramatically, assuming light is a wave implies that a lump of hot
coal emits an infinite amount of energy, and would destroy anything
and everything around it.
This is crazy! Clearly, this can't be true, and
[Max Planck](https://en.wikipedia.org/wiki/Max_Planck#Black-body_radiation)
figured out that in order to get the right answer, light needs to come
in discrete bundles of energy called *quanta*.
For light of frequency $f$, these quanta or *photons* have energy

$$
E = hf, \quad h \sim 6.34 \times 10^{-34} \text{ J s},
$$

where $h$ is called *Planck's constant*.

A few years later, Einstein invoked photons to explain how
light creates electricity.
This *photoelectric effect* is the basis of solar panels, for instance.
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

We can deliver energy by shining a flashlight on the metal.
Physicists expected this to work the same way ocean waves deposit
energy on the shore.
Imagine the electron as a beach ball sitting in a small dip in the sand.
An arriving wave will continuously deliver energy to the ball until it
gets enough ($\epsilon_\text{bind}$) to be dislodged from the dip.
The waves could be very high, or arrive one after the other in quick
succession, but it makes no difference to the beach ball.
It just needs to receive enough energy to get out of the dip.

For light, the equivalent of the height of waves is the *amplitude* $A$
and the rate waves come in is the frequency $\omega$.
In fact, the energy delivered is proportional to the *intensity* $I = A^2$.
If light is like the waves trying to dislodge the beach ball, we
expect that we could liberate electrons either by making $A$ big or
$\omega$ big.
But experimentalists noticed that, weirdly, for a given metal, below a
certain frequency electrons would never be liberated, no matter what
the intensity of the flashlight!
This is very surprising, almost like a low-frequency tsunami failing
to dislodge the beach ball.
What gives?

Einstein's explanation was simple.
He took Planck's idea that light carried energy in discrete lumps $E =
hf$ depending only on frequency, and gives it to the
electrons as a lump sum.
The electrons will begin to flow as soon as the frequency $f$ satisfies

$$
E = hf \geq \epsilon_\text{bind}.
$$

In this picture, the intensity is proportional to *how many* photons
are coming out of our flashlight per second, so increasing intensity
will just liberate more electrons.
It's like the waves at the beach are themselves made of beach
balls, whose energy depends on the frequency of waves, and increasing
the amplitude just stacks more balls on the wave.
Balls can only collide one at a time, so even a tsunami wave of low-energy
beach balls cannot dislodge the ball from the dip.

---

**Exercise 1.** Something?

---

#### 2.2. Flashlights and sunglasses <a id="sec-2-2" name="sec-2-2"></a>

Planck and Einstein teach us that light comes in discrete lumps.
But there's nothing to prevent these lumps from behaving like little,
classical beach balls.
We will see, however, that quantum mechanics is fundamentally
different.
To see how this happens, let's remember that according to classical
electromagnetism, light has an electric component which wobbles up and
down.
The plane in which this wobbling happens is called the *polarization*.

Although wobbling is a classical notion, it is still a valid property
associated with a photon.
Let's set up a coordinate system with the $z$-axis coinciding with the
path of the photon, and $x$ and $y$ perpendicular to it.
The polarization makes an angle $\theta$ with respect to the $x$-axis,
as pictured below.
A *polarizer* is a filter which allows only certain polarizations to
pass through.
A simple example is the polarizing sunglasses that you can find at the
chemist.

Hidden inside the phrase "only allows certain polarizations to pass
through" is a revolution in physics.
To see why, consider the photons coming out of a flashlight.
The polarizations are *random*, for the simple reason that the
flashlight just heats up a filament, and creates light using random
atomic collisions.
What should we expect when the randomly polarized light approaches the
polarizer?
If the polarizer only lets through photons with *precisely* the right
polarization, then almost no light will get through, since the chance
of getting this exact polarization is miniscule.
We wouldn't be able to see through polarizing sunglasses at all!
Since we can see through sunglasses, something else must be
happening.
We can use intensity to help us understand.

---

**Exercise 2.** Remember that intensity tells us how many photons there are.
You can install a lightmeter app on your smartphone that measures
intensity, so you can tell how many photons are getting through.
Now, let's do an experiment!

<span style="padding-left: 20px; display:block">P1.
(a) Measure the intensity of the flashlight, $I_0$.
Pass it through the sunglasses, and measure the intensity, $I_1$.
	What is the ratio $I_1/I_0$?
	</span>

<span style="padding-left: 20px; display:block">P1.
(b) Now pass the light through *two* aligned pairs of sunglasses, and
measure the intensity, $I_2$.
	What is the ratio $I_2/I_1$?
</span>

---

Your experiment should show that the intensity drops by *half* after
the first pair, and should be approximately the same after the second.
In other words, half the photons are blocked, and then most get
through!

#### 2.3. The law of Malus <a id="sec-2-3" name="sec-2-3"></a>
