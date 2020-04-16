---
Layout: post
mathjax: true
comments: true
title:  "Making light of quantum mechanics"
categories: [Physics, Hacks]
date:  2020-04-30
---

**April 30, 2020.**

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Photons</a>
   1. <a href="#sec-2-1">Experimenting with polarisers</a>
   2. <a href="#sec-2-2">Quantum polarisers</a>
   3. <a href="#sec-2-3">Stern-Gerlach</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

## 2. Photons <a id="sec-2" name="sec-2"></a>

Classically, light consists of intertwined electric and magnetic
fields, separately wobbling up and down, but at right angles to each
other.
In quantum mechanics, this wave can also be viewed as a particle
called the photon.
The photon's electric field wobbles up and down in some direction
called the *polarisation*.

Let's set up a coordinate system with the $z$-axis coinciding with the
path of the photon, and $x$ and $y$ perpendicular to it.
The polarization makes an angle $\theta$ with respect to the $x$-axis,
as picture below.
We can place the angle on the unit circle in the $x$-$y$ plane, and
recall that the coordinates of the corresponding point are

$$
x = \cos\theta, \quad y = \sin \theta.
$$

A *polariser* is a slit (in real life, a series of aligned slits)
which allows only certain polarisations to pass through.
Surprisingly, experiments with polarisers that you can do at home
reveal the basic features of quantum mechanics!

### 2.1. Experimenting with polarisers <a id="sec-2-1" name="sec-2-1"></a>

Let's grab a polariser and put it at some angle $\theta_P$.
If a single photon comes along with polarisation $\theta$, what
happens?
Intuitively, the polariser should act like a filter which only lets
the angle $\theta_P$ through; anything else is blocked.
Although it's hard to produce a single photon with fixed polarisation,
it's easy to produce many photons with random polarisations, simply by
turning on a flashlight.
If $\theta$ is randomly chosen, most of the time $\theta \neq
\theta_P$, so we might expect a polariser to block the light from a flashlight.
You can test this prediction with a pair of polarising sunglasses.
You'll find that they *don't* block the flashlight.
It would be crazy to make polarised sunglasses otherwise!

Let's see how many photons do get blocked.
Consider a chunk of the beam of light as it leaves the flashlight.
It has some area $A$, a width $w$, and a density of photons $n$, so
the total number of photons is $N = Awn$.
If the beam is monochromatic (one colour), each photon carries the
same amount of energy, $\epsilon$, so the total amount of energy is

$$
E = N\epsilon = Awn\epsilon.
$$

We can measure the *intensity* of light using a light meter, or even
an app on your phone.
It doesn't measure the total energy in a chunk, or even the power
(energy per unit time) delivered by the beam, but rather, the power
per unit are:

$$
I = \frac{E}{t A} = \frac{wn\epsilon}{t} = nc\epsilon.
$$

Here, we used the fact that $w/t = c$ is the speed of light.
Note that the intensity is proportional to the density of photons,
$n$, and two constants, $c$ and $\epsilon$.
Using a light meter app, you can check that after the light passes
through the subglasses, the intensity is reduced by *half*, and hence
the density of photons is reduced by half:

$$
I' = n'c\epsilon = \frac{1}{2}I = \frac{1}{2}nc\epsilon \quad
\Longrightarrow \quad n' = \frac{1}{2}n.
$$

In other words, even though the photons have random polarisations
$\theta$, half of them are let through.
How could this possibly happen?

### 2.2. Quantum polarisers <a id="sec-2-3" name="sec-2-3"></a>

To explain what's happening, let's revisit our original hypothesis:
only light with $\theta = \theta_P$ is let through.
Another way of thinking about this is as follows.
When light hits the slit, the polariser "measures" the angle $\theta$,
and decides to let the light through if $\theta = \theta_P$.
Otherwise, it simply absorbs the photon.
If this view is correct, then in a beam of randomly polarised photons,
most get blocked.

Experimentally, we see that only half the photons are blocked, so we
need to update our model of what the polariser does to a photon.
To help us formulate a model, let's do some more experiments, but now
with multiple polarisers.
To start off with, apply a polariser with $\theta_1$ to a flashlight
beam of intensity $I$.
The intensity is halved to $I_1 = I/2$, and all the light that comes
out has polarisation angle $\theta_1$.
To check this, we can apply another polariser with angle $\theta_2 =
\theta_1$.
The intensity after the second polariser is exactly the same, $I_2 =
I_1$, suggesting that all the photons are allowed through!
This suggests two rules for polarisers:

---

<span style="padding-left: 20px; display:block">P1.
Any photons emerging from a polariser with angle $\theta_P$ have
polarisation angle $\theta_P$.
</span>

<span style="padding-left: 20px; display:block">P2.
A polariser with angle $\theta_P$ always admits a photon with angle $\theta_P$.
</span>

---

What about photons with a different angle?
Using (P1), we can test this very precisely.
Orient the second polariser so that it is horizontal, $\theta_2 =
0$.
Now vary $\theta_1$, and plot the intensity after the beam has passed
through both polarisers, $I_2(\theta_1)$.
You find that, in contrast to setting $\theta_2 =\theta_1$, when the
polarisers are at right angles ($\theta_1 = \pi/2$) no light gets
through at all!
So $I_2(90^\circ) = 0$.
If you turn first filter $180^\circ$, you once again have $I_2 = I_1$.
A guess for unifying these observations --- which turns out to be
correct, as further measurements reveal --- is that

$$
I_2(\theta) = I_1 \cos^2\theta_1.
$$

Put differently, if the photon density is $n_1$ after the first
polariser, it is

$$
n_2 = n_1 \cos^2\theta_1
$$

after the second filter.

### 2.3. Stern-Gerlach <a id="sec-2-3" name="sec-2-3"></a>

#### References

- qm: polarisers/filters, stern-gerlach, superposition, uncertainty,
entanglement, qkd, quantum computing, measurement problem, parallel
universes 

### Extra

Procedurally, we might imagine it as follows: the polariser measures
the photon's polarisation $\theta$, checks it against the angle of the
slit $\theta_P$, and if the two are different, "rejects" the photon.
We'll call this a "classical" polariser for reasons we explain below.
A beam of light will consist of many photons with *random*
polarisation angles $\theta$.
Since $\theta$ can be chosen from anywhere on the circle, most photons
in the beam won't have $\theta = \theta_P$, and if the polariser is
classical, will be blocked.
You can perform a simple experiment to see what happens.
