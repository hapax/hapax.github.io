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
2. <a href="#sec-2">Fun with photons</a>
   1. <a href="#sec-2-1">Flashlights and sunglasses</a>
   2. <a href="#sec-2-2">Quantum polarisers</a>
   3. <a href="#sec-2-3">Splitting light</a>
   4. <a href="#sec-2-4">The uncertainty principle</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

## 2. Fun with photons <a id="sec-2" name="sec-2"></a>

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
A *polariser* is a slit (in real life, a series of aligned slits)
which allows only certain polarisations to pass through.
Surprisingly, experiments with polarisers that you can do at home
reveal the basic features of quantum mechanics!

### 2.1. Flashlights and sunglasses <a id="sec-2-1" name="sec-2-1"></a>

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
I_1$, so all the photons are allowed through!

This suggests two rules for polarisers:

---

<span style="padding-left: 20px; display:block">P1.
Any photons emerging from a polariser with angle $\theta_P$ have
polarisation angle $\theta_P$.
</span>

<span style="padding-left: 20px; display:block">P2'.
A polariser with angle $\theta_P$ always admits a photon with angle $\theta_P$.
</span>

---

What about photons with a different angle?
Using (P1), we can test this very precisely.
Fix the angle of the first polariser at $\theta_1 = 0$ for simplicity,
and let the angle $\theta_2 = \theta$ of the second polariser vary.
We can measure the resultant intensity $I_2(\theta)$.
At $\theta = 0$, we know from (P2') that the intensity is unchanged, $I_2 = I_1$.
But as we rotate the second polariser away from the $x$-axis, the
intensity decreases, until it disappears altogether at $\theta =
90^\circ$.
When the polarisers are at right angles, no light gets through at all!

Fitting a curve to the measurements, one finds that the intensity as a
function of angle is

$$
I_2(\theta) = I_1 \cos^2\theta.
$$

This is called *Malus's law* after
[Étienne-Louis Malus](https://en.wikipedia.org/wiki/%C3%89tienne-Louis_Malus) (1775--1812).
If $N_1$ photons come out of the first filter with
horizontal polarisation, only $N_2 = N_1 \cos^2\theta$ make it through the
second, so it seems as if the polariser makes a random decision to let
a photon through, with *probability*

$$
p = \frac{N_2}{N_1} = \cos^2\theta.
$$

Note that $\theta = \theta_2 - \theta_1 = \Delta\theta$ is the
relative angle between photon and polariser, this suggests a general
rule (P2), which includes (P2') as a special case:

---

<span style="padding-left: 20px; display:block">P2.
If a photon and polariser have relative angle $\Delta\theta$, the
photon passes through with
</span>

$$
p(\Delta \theta) = \cos^2(\Delta \theta).
$$

---

We have based our rules on experiments using two filters, but they
more conventionally introduced using *three* filters and the famous
[Stern-Gerlach experiment](https://en.wikipedia.org/wiki/Stern%E2%80%93Gerlach_experiment)
(1922).
You can predict the outcome of this experiment using rules (P1) and
(P2) in Exercise 1.
In Exercise 2, you can see why intensity is halved when a flashlight
beam is polarised.

---

**Exercise 1 (Stern-Gerlach).** The original Stern-Gerlach experiment
was performed with electrons.
Here, you can work out what happens in an analogous experiment for
photons.
As above, consider a flashlight of intensity $I$ illuminating two
filters.
If these are at right angles, they block all incoming light and $I_2 =0$.

<span style="padding-left: 20px; display:block">
(a) Suppose we insert a filter in between the first and the second,
oriented at $45^\circ$ relative to each.
	Using rules (P1) and (P2), what is the resultant intensity?
	</span>

<span style="padding-left: 20px; display:block">
(b) Confirm your result experimentally.
	A couple of minutes at the pharmacy (in the sunglasses section)
	should suffice.
</span>

<p align="center">
  ⁂
  </p>

**Exercise 2 (halving intensity).** We still haven't explained why the
unpolarised flashlight beam is halved in intensity.
Recall that, in a beam of unpolarised light, the angle of individual
photons $\theta$ is random.
To halve the intensity, we need the *average* value of $p(\theta) =
\cos^2\theta$, for $\theta = 0$ to $\theta = 360^\circ$, to be $1/2$.

<span style="padding-left: 20px; display:block">
(a) Use the double angle formula to show that
</span>

$$
\cos^2\theta - \frac{1}{2} = \frac{1}{2}\cos(2x).
$$

<span style="padding-left: 20px; display:block">
(b) Conclude that $p(\theta)$ is symmetric around the line $y =1/2$.
</span>

<span style="padding-left: 20px; display:block">
(c) The average value $p_{\text{avg}}$ is the area underneath the
curve $p(\theta)$ compared to the area beneath the curve with $p = 1$.
Use (a) and (b) to argue that $p_{\text{avg}} = 1/2$.
</span>

---

### 2.3. Splitting light<a id="sec-2-3" name="sec-2-3"></a>

When we have two "crossed" filters, i.e. filters at right angles, all
incoming light is blocked.
But what if we *combine* these crossed slits into a single polariser?
Our rules don't apply in this case, so we need to do some more
experiments.
Since sunglasses are polarised in a single direction only, this is a
little harder to perform at home, so I'll just tell you what happens
and we can continue theory-building from there.

If you shine a flashlight on the cross, and measure the intensity
before ($I$) and afterwards ($I'$), you find *no reduction*.
Every photon gets through!
We can learn even more by polarising the light first, and measuring
the polarisation afterwards.
For concreteness, orient the cross so that the first slit is at
$\theta_x = 0$ and the second at $\theta_y = 90^\circ$.
If an incoming beam is polarised at angle $\theta$, it will obey
Malus's law is true for *both* slits.
In other words, it will have horizontal orientation $\theta_x = 0$
with probability

$$
p_x = \cos^2\theta
$$

and vertical orientation $\theta_y = 90^\circ$ with probability

$$
p_y = \cos^2(\theta - 90^\circ) = \sin^2\theta.
$$

Every photon gets through since these probabilities add up to $1$:

$$
p_x + p_y  = \sin^2\theta + \cos^2\theta = 1.
$$

There is a nice geometric way to interpret this.
Recall that, if $\theta$ labels an angle on the unit circle, then the
$x$ and $y$ coordinates of the point are

$$
x(\theta) = \cos\theta, \quad y(\theta) = \sin \theta.
$$

To get probabilities, we just square coordinates on the unit circle.

Let's recap.
To explain why you can see through polarised sunglasses, we have
postulated that, for individual photons, a single or double polariser
makes a *fundamentally random decision* about what to do with it.
The universe, even at a microscopic level, is probabilistic.
Maybe this seems natural to you, but the physicists of the early 20th
century were used to thinking of the universe as made up of tiny
classical billiard balls, bouncing around on deterministic
trajectories.
Although Einstein was one of the founders of quantum theory, he later
came to reject it, famously state

<span style="padding-left: 20px; display:block">
God does not play dice.
</span>

Ironically, in his efforts to discredit quantum mechanics, Einstein
invented *entanglement*, perhaps the most useful and essentially
quantum phenomenon, as we will see below.
Even when Einstein was wrong, he was right!

### 2.4. The uncertainty principle<a id="sec-2-4" name="sec-2-4"></a>


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

It's not too hard to account for this when we remember that, with a
single slit at angle $\theta_P$, half the photons went through (and
picked up polarisation $\theta_P$) and the other half were absorbed by
the filter.
It seems that, instead of being absorbed, the photons are now getting
spat out with the second polarisation $\theta_P + 90^\circ$.
And the same thing is true if we think about things from the
perspective of the second filter, so this interpretation is consistent!

Once again, we can do better 
Recall that if we place the angle $\theta$ on the unit circle, the $x$
and $y$ coordinates are

$$
x = \cos\theta, \quad y = \sin \theta.
$$

It looks like every photon that comes along is getting polarised into
one of the two directions, with half assigned to the first
polarisation and half to the second.

Now introduce a second, ordinary polariser, align it with the
first of the crossed slits, and measure the intensity $I_1$.
We can similarly measure the intensity $I_2$ when the polariser is
aligned with the second of the crossed slits.
Each of these intensities is precisely half the original intensity:

$$
I' = I = 2I_1 = 2I_2.
$$
