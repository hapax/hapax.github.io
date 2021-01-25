---
Layout: post
mathjax: true
comments: true
title:  "Black holes as quantum computers"
categories: [Physics]
date:  2021-02-03
---

**February 3, 2021.** *Black holes are mysterious objects. In this tutorial,
  we'll introduce some of the puzzles of black hole physics, and a surprising perspective
  for resolving them: treat the black hole as a quantum computer! This not only
  provides conceptual insights, but will give us an algorithm for
  decoding messages from behind the horizon, which we perform in a
  suitably simplified setup.*

#### Introduction

Black holes are regions of spacetime where gravity is strong enough to
trap light.
Now, light travels pretty fast, about a hundred million times faster than a
speeding pedestrian, so this is no mean feat, and it takes the death of a giant
star, or disastrous collisions at the core of a galaxy, to produce
them.
But we now know, from a whole spectrum of clues, that they exist and
play an important role in the life of star systems, galaxies, and even
the early universe as a whole.

In 2015, the gravitational wave observatory LIGO detected ripples in
spacetime which could only be produced by two black holes, spiralling inwards
and merging a billion light years away.
We've known since the 1990s that a supermassive black hole, millions
of times heavier than our sun, lurks in
the heart of the Milky Way, an achievement recognized by the 2020 Nobel
Prize in Physics.
And most spectacularly, in 2019, the Event Horizon Telescope stitched
together an image of a supermassive black hole, 50 million years old,
in the galaxy M87 far, far away:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/m87.jpg"/>
	</div>
	</figure>

But for all their astronomical richness and complexity, black holes
harbour just as much interest for theoretical physics, and in
particular, the program of combining quantum mechanics with gravity,
known as *quantum gravity*.
The goal of this tutorial will be to explore some of the problems of
black holes and quantum gravity, and to introduce cutting edge
approaches to these problems from the language of quantum
computing.
Rather than give a traditional primer and then laboriously translate
into this language, we'll present black hole physics as a series of
computational slogans.

#### Black holes store physical information

Our first slogan is simply that black holes store physical information.
To make a black hole, you need to collapse some matter, like an old
star or dust clouds in the galactic core, and this matter contains
information: namely, the information about the state it was in when
you collapsed it.
To make the analogy to computing explicit, suppose we have $N$
classical bits, which can be either $0$ or $1$, say electrons which
can be spin up or spin down. We then use an electromagnetic trash
compactor to squish them until they form a black hole.
The state of the system before it collapsed was an $N$-bit string, and
afterwards, those $N$ bits are somehow stored inside the black hole.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/bhqc1.png"/>
	</div>
	</figure>

If our system is quantum, with $N$ qubits in some state
$|\psi\rangle$, then after collapse $|\psi\rangle$ is somehow stored
in the black hole. The story is basically the same.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/bhqc2.png"/>
	</div>
	</figure>

A natural question is how the information stored in the black hole is
related to its physical properties, things we can measure.
In the 1970s, Jacob Bekenstein and Stephen Hawking discovered
something remarkable.
They learned that the amount of information you can store in a black
hole, the number of bits, is proportional to the area of the horizon,
that is, the surface area of the black hole as it appears from outside.
In fact, up to some numbers we're not going to worry, it's the
area of the horizon, $\mathcal{A}$, divided by something called the
*Planck area*, which is the unique area you can build out of basic
physical constants:

$$
\mathcal{A}_P = \frac{\hbar G}{c^3} \approx 2.56 \times 10^{-70}
\text{ m}^2.
$$

<!-- We derive this in an appendix, but for our purposes, it will help us
form a picture of a black hole as a spherical computer. -->
This gives us the license to draw a black hole as a spherical computer
whose surface is split into Planck area-sized pixels. Each of these is
a classical bit, which can be either $1$ or $0$, or a qubit if we want
to go quantum.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/bhqc3.png"/>
	</div>
	</figure>

Once a black hole has formed, you can throw more things into it, a bit
like downloading something onto your computer. In order to
accomodate this new data, the black hole must grow bigger!
For instance, if we add a single bit (or qubit), then the horizon must
grow by at least one Planck area, as this 2D cartoon shows:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/bhqc4.png"/>
	</div>
	</figure>

More generally, if we throw $n$ bits (or qubits) into the black hole, the area
must grow by at least $n$ Planck areas.

#### Black holes glow

<!-- What we've said so far is a bit confusing. It suggests a
So, let's return to our picture of the black hole as a spherical computer.-->
<!-- Our picture of a black hole as a spherical computer suggest that information lives on the surface, and
if it lives on the surface, maybe it can come out again, or create
other detectable features near the horizon. -->
All of this suggests that information is stored on the surface, so
perhaps it can come out again, or at least, create detectable features near the horizon.
Guided by this intuition, in 1975 Stephen Hawking made the most
ambitious calculation of his life.
Using a combination of techniques from gravity and particle physics,
he discovered that black holes are not truly black, but *glow* faintly.
This glow is called *Hawking radiation*, and it costs energy to produce,
gradually depleting the black hole until it disappears.
This disappearing act is known as *black hole evaporation*.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/bhqc5.png"/>
	</div>
	</figure>
	
But if black holes evaporate, it's natural to ask what happens to
the information they store.
Hawking's calculation suggests that the glow of the black hole is
effectively *random*, a noisy and uninformative process like the light from
a hot coal or an incandenscent globe.
If this is true, then when black holes form, information is trapped
irreversibly behind the horizon, and destroyed when the black hole
evaporates.
Quantum gravity takes its secrets to the grave, replacing them with
a random sequence of $1$s and $0$s.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/bhqc6.png"/>
	</div>
	</figure>

This is kind of a big deal, because destroying information is not
allowed by quantum mechanics.
Quantum states always evolve in a reversible fashion, which is why
gates are reversible in quantum computing. It's just a basic physical
requirement; if you have an irreversible gate, you'll never be able to
built it.
So if black holes destroy information, then quantum mechanics must be
wrong.
This tension between quantum mechanics and Hawking's glow is called
the *Information Paradox*, and it's been one of the biggest open problems in
quantum gravity for $45$ years.

#### Black holes encrypt

Before we try and solve this, let's take a step back.
Computers usually do more than passively store data.
They will tke the data, perform some useful computation on it, then
output some results, like doing a google search or playing
Minecraft.
A black hole takes information about collapsing stars, or fatally
inquisitive astronauts, and outputs what looks like random noise.
What computation could connect them?

<!-- But computers usually do more than passively store data.
They will take that data, perform some useful computation on it, and
then output the results, like doing a google search or playing
Minecraft.
If a black hole really is a quantum computer, we can ask: what
computation is it doing, and what is its output?
We'll actually start with the output, and then reverse engineer the
computation, since this mirrors the history of the subject. -->

<!-- In 1975, Stephen Hawking made the most important calculation of his
life.
Hawking didn't think about black holes in terms of information
storage, he thought in terms of entropy, a related concept from
thermodynamics, the physics of hot objects.
Entropy basically measures how many different configurations a system
can be in, or rather, tha natural logarithm of that.
An $N$-bit system, for instance, can be in $2^N$ different states,
so its entropy is

$$
S = k_B \ln 2^N = \ln 2 N k_B \approx 0.7 N k_B.
$$

where $k_B$ is *Boltzmann's constant*.
When a system is at some finite temperature, and different
configurations have different energies, the effective number of
allowed configurations changes, and the entropy with it. -->

<!-- ##### Introduction

A black hole is a very special type of quantum computer. In this
tutorial, we'll explore a few properties of these computers using the
tools of
[physics hacking](https://hapax.github.io/physics/teaching/hacks/napkin-hacks/#sec-1). The
prerequisites are very mild: a background in pre-calculus mathematics
and a nodding familiarity with high school physics.

##### A hacker's guide to black holes

A black hole is an object which has collapsed under its own gravity to
form a light-trapping region.
We can estimate various properties of this region using a few
equations and some inspired guesswork.

#### System size

Suppose the black hole has mass $M$.
A running theme will be different ways of estimating the energy stored
in the black hole, and to start with, we invoke the most famous
formula ever:

$$
E = Mc^2,
$$

where $c = 3 \times 10^8 \text{ m/s}$ is the speed of light.
This is how much *mass-energy* the black hole has, according to
Einstein's gem.
Since a black hole is a gravitational object, it also stores
gravitational energy, which we can estimate as

$$
E \sim \frac{GM^2}{R}
$$

where $R$ is the size of the black hole.
This follows immediately from the formula for gravitational
potential, but we can derive it a little more carefully.
First, note that from Newton's law of gravitation, the force the black
hole applies on itself is roughly

$$
F_\text{grav} \sim \frac{GM^2}{R^2},
$$

where $G = 6.67 \times 10^{-11}$ (in SI units) is Newton's constant.
Applying a force over a distance gives energy (work), so we estimate
that

$$
E \sim F_\text{grav} R \sim \frac{GM^2}{R}
$$

as claimed.
Now, if we equate these two forms of energy, we find the famous
*Schwarzschild radius* $R$:

$$
Mc^2 \sim \frac{GM^2}{R} \quad \Longrightarrow \quad R \sim \frac{GM}{c^2}.
$$

This is exactly what we find in general relativity up to a factor of
two, $R = 2GM/c^2$.
Just to give a sense of how small this is, the sun weights $M_\odot = 2
\times 10^{30} \text{ kg}$, so if it collapsed into a black hole, it
would have a Schwarzschild radius of

$$
R = \frac{2GM_\odot}{c^2} = \frac{2(6.67\times 10^{-11})(2 \times
10^{30})}{(3\times 10^8)^2} \text{ m} \approx 3 \text{ km}.
$$

It would fit on the University Endowment Lands of UBC.

#### Let there be heat

Although a black hole traps any light that falls inside, Stephen
Hawking made the remarkable discovery that just outside the boundary,
black holes emit faint radiation, just like a hot lump of coal.
Once again, we will rather slapdash, and try and work out only the
wavelength of a typical photon coming out of the black hole.
It seems reasonable to assume that, like the fundamental frequency of
a violin or a flute, the black hole likes to make photons with
wavelengths proportional to the Schwarzschild radius $R$.

This has various implications.
Most importantly, the hotter an object is, the smaller the wavelength
of the typical photons it produces.
This explains why a very hot coal is orange or yellow, and becomes red
(a longer wavelength of light) as it cools.
The relationship is governed by something called *Wien's law*:

$$
\lambda \sim \frac{hc}{kT},
$$

where $h = 6.62 \times 10^{-34}$ is Planck's constant,
and $k = 1.38 \times 10^{-23}$ is Boltzmann's constant (both in SI
units).
The key point is that wavelengths get shorter as temperature rises,
and the rest of the constants are added to ensure things make
dimensional sense.
Setting $\lambda = R$ and making $T$ the subject, we obtain the
*Hawking temperature* of a black hole:

$$
T \sim \frac{hc}{kR} \sim \frac{hc^3}{GMk}.
$$

<!-- Max Planck, one of the founding fathers of quantum mechanics, came up
with a general formula for the amount of energy in a photon of
wavelength $\lambda$, $\varepsilon = hc/\lambda$, where $h = 6.62
\times 10^{-34}$ (in SI units).
Then the typical Hawking photon coming out of a black hole has energy
$$
\varepsilon \sim \frac{hc}{R} \sim \frac{hc^3}{GM}.
$$
Not only does the black hole radiate like a hot lump of coal, it does
so for the same reason: it has a temperature!
The relationship between the enery of the photon -->

<!-- Note that black holes heat up as they get small!
Once again, we can check what would happen if the sun were a black
hole.
Using our previous result for the Schwarzschild radius, the Hawking
temperature would be

$$
T \sim \frac{(6.62 \times 10^{-34})(3 \times 10^8)}{(1.38 \times
10^{-23})(3000)} \text{ K} = 5 \times 10^{-6} \text{ K}.
$$

This is millions of times colder than empty space, which has a
temperature of about $3 \text{ K}$.
The black holes in equilibrium with the vacuum have radius around

$$
R \sim \frac{hc}{kT} = \frac{(6.62 \times 10^{-34})(3 \times 10^8)}{(1.38 \times
10^{-23})(3)} \text{ m} = 5 \text{ mm},
$$

<!-- If the sun did collapse to form a black hole, it would get heated up
by the surrounding vacuum.
Since mass gets smaller with temperature, this means it would shrink
dramatically! -->

<!-- about the length of an ant.

#### Black hole molecules

We've measured the energy in a black hole using Einstein's mass-energy
formula, and Newton's formula for gravitation.
Let's measure the energy a different way, in terms of *heat*.
People often say that the temperature of the substance measures the
amount of "molecular motion", or kinetic energy per molecule.
This sounds fuzzy, but can be written as a perfectly rigorous
equation called the *equipartition theorem*:

$$
E \sim N \text{k}T,
$$

where $E$ is the total kinetic energy of molecules, or *heat*, and $N$
is the total number of particles.
We can use this to estimate the total number of "molecules" in a black
hole. Using the mass-energy form for simplicity, we have

$$
E = Mc^2 \sim Nk T \sim \frac{Nhc}{R} \quad \Longrightarrow \quad N
\sim \frac{RMc}{h} \sim \frac{R^2c^3}{Gh}.
$$

This is a strange and remarkable result.
The first thing to notice is that the number of particles is
proportional to $R^2$, and hence the *surface area* $4\pi R^2$ of the
black hole.
Usually, the number of particles is proportional to the *volume* of a
material, not the surface area, so something weird appears to be
happening.
The second interesting thing is that we are dividing the surface area
by a particular combination of constants,

$$
A_P = \frac{Gh}{c^3},
$$

called the *Planck area*.
For various reasons, it can be regarded as the smallest area that
makes sense.

We can recast what we have learned about black holes in terms of
computers.
Things fall into the black hole, a bit like entering data onto a
computer.
The total system size is $N$, which comes from splitting the surface
area of the black hole into pixels of area $A_P$.
Finally, the black hole will output information in the form of photons. -->
<!-- with the typical length given by the current size of the black hole.-->
