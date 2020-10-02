---
Layout: post
mathjax: true
comments: true
title:  "Why is quantum gravity hard?"
categories: [Physics, Hacks]
date:  2020-10-02
---

**October 2, 2020.** *People often say that quantum gravity is hard
  because quantum mechanics and gravity are incompatible. I'll give a
  short, relatively non-technical explanation of the real problem ---
  spacetime breaks down when we look too close.*

#### Introduction

Gravity is a theory of heavy things; quantum mechanics is a theory of
small, fuzzy things; *quantum gravity* applies to things which are
both heavy and fuzzy.
People often say that the two theories are "incompatible" because
they use different mathematics.
This is a tad misleading.
The real problem is that Nature is secretive: it hides the details of
quantum gravity inside black holes!
Let's see why.

#### Microscopes make energy

Suppose we have a microscope which has can resolve lengths $\Delta x$.
Heisenberg's uncertainty principle says that the smaller this
resolution, the larger the uncertainty about the momentum of things we
measure, with

$$
\Delta p \gtrsim \frac{\hbar}{\Delta x}
$$

for Planck's constant $\hbar \approx 10^{-34} \text{ J/s}$.
We can relate this to the energy of the particles using Einstein's
famous $E = mc^2$.
In fact, we will write it in the much less well-known form

$$
E^2 = m^2c^4 = p^2c^2 + m_0^2 c^4,
$$

where $m_0$ is the mass of the particle at rest, $c = 3 \times 10^8
\text{ m/s}$ is the speed of light, and $m$ is the *relativistic
mass*, which increases (without limit) as the particle speeds up.
When the particle is moving very quickly, the momentum can be much
larger than the rest mass energy, and $p \approx E/c$.
If we measure very small distances, Heisenberg's principle tells us we
will be smacking around particles at very high momenta, so this is the
form we should use.
Thus, the uncertainty in the energy of particles our microscope is
examining is

$$
\Delta E \sim \frac{\hbar c}{\Delta x}\;.
$$

#### Energy makes black holes

Let's now recall Newton's universal law of gravitation,

$$
F = \frac{Gm_1 m_2}{r^2},
$$

where $G = 6.7\times 10^{-11} \text{ N m}^2\text{ /kg}$ is *Newton's
constant*.
We can use this to estimate the size of a black hole!
A black hole is a region of space where gravity is so strong light
is unable to escape.
To see how light figures in Newton's law, we need to give it a mass.
In classical physics, light is massless, but but we know better: Einstein's
formula tells us that it has some *relativistic* mass related to its
energy, $E = mc^2$.
[If you're curious, the mass of a particle of light, the photon,
depends on its frequency $f$ via

$$
m = \frac{E}{c^2} = \frac{2\pi\hbar f}{c^2},
$$

using the formula for the energy of a photon, $E = 2\pi \hbar f$, also discovered by Einstein.]
Let's continue.
For a black hole of mass $M$, and radius $r_s$, the force it exerts on
a photon with mass-energy $m$ is

$$
F \sim \frac{GMm}{r_s^2}.
$$

Using the work formula, we can view force as energy divided by
distance.
Since the energy of the photon is $E = mc^2$, and the relevant
distance is probably the black hole size $r_s$, we have

$$
\frac{mc^2}{r_s} \sim \frac{GMm}{r_s^2} \quad \Longrightarrow \quad
r_s \sim \frac{GM}{c^2}.
$$

Although we've been rather sloppy, this guess is correct up to a
factor of $2$!
So, if we take a mass $M$ and squish into a ball of radius $\lesssim
GM/c^2$, it will make a black hole.

#### Microscopes make black holes

Now, let's return to our microscope.
In order to zoom in, Heisenberg's principle means it makes some energy
fluctuations, and by $E = mc^2$ these fluctuations have mass.
The associated black hole radius is

$$
r_s \sim \frac{Gm}{c^2} = \frac{G\Delta E}{c^4} = \frac{G\hbar}{\Delta x \cdot c^3}.
$$

It may seem sketchy to replace $E$ with $\Delta E$, but if the energy
of particles has fluctuations of size $\Delta E$ around $E = 0$, some
of them will have energy $E$.
We can clean up this expression by packaging all these constants into
a single object called the *Planck length*:

$$
\ell_P := \sqrt{\frac{G\hbar}{c^3}}.
$$

Then the associated black hole radius for our microscope is

$$
r_s \sim \frac{\ell_P^2}{\Delta x}.
$$

Now, what does this all mean?
Very simply, if the resolution $\Delta x$ of our microscope is within
the associated black hole radius, then our energy fluctuations will
produce a tiny black hole!
We won't see anything at all this black hole at all.
This happens when

$$
\Delta x \lesssim r_s \sim \frac{\ell_P^2}{\Delta x} \quad
\Longrightarrow \quad \Delta x \lesssim \ell_P.
$$

In other words, we can't see below the Planck scale without making
black holes.
Clearly, microscopes this powerful should be kept away from theorists!

#### No local observables

So, the basic difficulty with quantum gravity is that zooming in makes
black holes.
This problem appears in many different guises.
For instance, suppose I want to make statements about what is
happening at a *point* $X$ in spacetime, e.g. an electron has some
probability of being observed there.
So, I wait around with my electron detector to see if the electron
appears at $P$, and in due course, it does.
Or does it really?
If my electron detector can tell what's happening at the point $P$
itself, it's acting as a microscope with infinite resolution!
Clearly, this is not consistent with the argument above.
At best, I can look for electrons in regions larger than the Planck length.

Instead of talking about black holes, we usually say that spacetime
*breaks down* when we try to look too close.
For this reason, it doesn't make sense to talk about what is
happening at a point in spacetime.
The electron detector is an example of something called a *local
observable*: it is defined at a point (local) and makes a
quantum-mechanical measurement (observable).
This conclusion is so important we put it in a quote box:

<span align="center" style="padding-left: 20px; display:block">
*In quantum gravity, there are no local observables.*
</span> 

In fact, this conclusion is already suggested by Einstein's
*classical* theory of gravity, general relativity.
Without going into details, we can briefly explain why, and some of
the fancy words physicists use to dress up the idea.

#### Diffeomorphism invariance

In Newtonian gravity, spacetime is a sort of fixed arena where objects
float around and exert forces on each other. In this picture, gravity
is just another force.
Einstein's profound realization was that gravity isn't a real force at
all!
Rather, *gravity is the shape of space*, and *space is shaped by matter.*
In the beautiful maxim of John Wheeler,

<span align="center" style="padding-left: 20px; display:block">
*Spacetime tells matter how to move; matter tells spacetime how to curve.*
</span>

It doesn't make much sense to talk about stuff happening at a point
$P$ itself.
Rather, physically meaningful statements will involve the shape of
space and matter in the vicinity of $P$.
The shape of space is captured by an object $\mathbf{G}$ called the
*Einstein tensor*, while the "shape" of matter is captured by an
energy-like quantity called the *stress-energy tensor* $\mathbf{T}$.
The governing equation of general relativity is the *Einstein field
equation*:

$$
\mathbf{G} = \frac{8\pi G}{c^4}\mathbf{T}.
$$

Physicists have a hack for enforcing that physics only depends on the
shape of things.
Clearly, the label of the point $P$ will depend on my labelling
system.
But however I choose to label $P$ (and the surrounding points), the
shape of space doesn't change.
A sphere is still a sphere, even if I label points using days of the
week!
Thus, physically meaningful statements do not depend on how we label points.
Physicists like fancy terminology, and "relabelling points" often goes
by "diffeomorphism", and "does not depend on" by "invariance".
So in fancy language, the constraint becomes

<span align="center" style="padding-left: 20px; display:block">
*Physically meaningful statements are invariant under diffeomorphisms.*
</span>

I can't really ask about whether an electron appeared at $P$ because
this question depends on how I label $P$.
Like I said above, there is no quantum mechanics here.
Once we add quantum mechanics, Nature itself enforces invariance under
diffeomorphisms by shrouding ill-formed questions with black holes.

#### What is quantum gravity even about? (Advanced)

The moral is that, in quantum gravity, spacetime fluctuates.
If I zoom in enough, these fluctuations are violent enough to form
black holes, so there are no local observables.
This is also suggested by the *classical* invariance of general
relativity under relabelling points.
But if spacetime itself is fluctuating, what questions can I ask?

To get a feeling for this, let's think about a (hopefully) familiar
example, Newtons second law $F = ma$.
If I have a *quantum-mechanical* particle, then measurements of the
position $x$ and momentum can $p$ fluctuate.
But I can still take *averages* over where I expect it to be, which we
denote by $\langle x\rangle$.
If I do this, I find that Newton's second law still holds for
averages!
This is called *Ehrenfest's theorem*:

$$
\langle F \rangle = m\langle a \rangle.
$$

Is there an equivalent statement for gravity?
The shape of space is given by some object $g(P)$ called the metric,
while the matter floating around is specified by some functions
$\phi(P)$, telling us how much is where.
Note that both of these are functions of position $P$.
The *curvature tensor* of space is given by some function
$\mathbf{G}[g]$, which depends only on the metric, and the *energy-momentum tensor* $\mathbf{T}[\phi, g]$

<!--- We can translate this dimensional argument into the language of -->
<!--quantum field theory. Set $\hbar = c = 1$. Newton's constant $G$ -->
<!--is a \emph{dimensionful} coupling constant for gravity, with mass -->
<!--dimension $[G] = -2$. Perturbation theory is controlled by the -->
<!--effective *dimensionless* coupling constant appearing at energy -->
<!--$E$, roughly $g(E) = GE^{2}$. This leads to a strongly coupled -->
<!--theory when $g \sim 1$, or $E \sim --> 
<!--\sqrt{\frac{1}{G}} \sim E_P\;,$ where $E_P = \sqrt{1/G}$ is the Planck energy.
At the Planck energy, when we expect quantum effects to become
important, the theory becomes strongly coupled! --->
