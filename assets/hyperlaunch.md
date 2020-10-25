---
Layout: post
mathjax: true
comments: true
title:  "A hyperlaunch to space"
categories: [Physics, Engineering]
date:  2020-10-26
---

**October 26, 2020.** *In which I pretend to be Elon Musk, and propose
  to launch rockets into space using vacuum tubes.*

#### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Hyperlaunchers</a>
   1. <a href="#sec-2-1">Pendulous pumpkins</a>
3. <a href="#sec-3">The physics</a>
   1. <a href="#sec-3-1">The barometric equation</a>
   2. <a href="#sec-3-2">Temperature and gravity*</a>
   3. <a href="#sec-3-3">High pressure environment</a>
4. <a href="#sec-4">Design challenges</a>

#### 1. Introduction<a id="sec-1" name="sec-1"></a>

Elon Musk is the CEO and founder of SpaceX, a company which sends
rockets into space. Along with engineers at Tesla and SpaceX, he also
proposed a wacky, high-speed alternative to trains: the *hyperloop*,
the pneumatic tube for people. In this post, I conduct an initial
feasibility study for combining these two ideas, and launching rockets
into space with *vertical* hyperloops.
I call this "hyperlaunch".

Since this is merely a feasibility analysis, I will ignore most of the
important engineering problems, and focus on the physics.
And even though I am focusing on the physics, I will adopt an
order-of-magnitude-estimate (oome) philosophy, which I will call
*oomeism*.
I state for the record that "oomeism" and the "hyperlaunch" are very,
very serious business.

#### 2. Hyperlaunchers<a id="sec-2" name="sec-2"></a>

The basic idea is simple.
Make a giant cylinder stretching from the

##### 2.1. Pendulous pumpkins <a id="sec-2-1" name="sec-2-1"></a>

#### 3. The physics<a id="sec-3" name="sec-3"></a>

With the concept now described, we have some physics to do. Can we
launch anything? How light must it be? What physics are we neglecting?
We'll address all of these, though using a suitably oomeist viewpoint.

##### 3.1. The barometric equation<a id="sec-3-1" name="sec-3-1"></a>

In order to understand how much force is supplied to the plunger, we
need to understand how pressure varies with height, and indeed, how
high the atmosphere effectively is for our purposes.
We will start with the simplest model: it is an ideal gas, in
hydrostatic equilibrium, small enough that gravitational acceleration
is constant.
Let's unpack these.
An ideal gas satisfies the ideal gas law,

$$
PV = Nk_BT \quad \Longrightarrow \quad P = n k_BT,
$$

where $P$ is pressure, $V$ is volume, $k_B
= 1.4 \times 10^{-23}$ in SI units, and $T$ is absolute temperature,
e.g. in Kelvin.
Finally, $N$ is particle number and $n = N/V$ is the number per unit
volume

Hydrostatic equilibrium means that the mass of a small parcel of has
is supported because pressure below is greater than pressure from above.
If the parcel has height $h$ and area $A$, its mass $m$ is the volume
$Ah$, multiplied by the density of particles $n$, multiplied by the
mass per particle $M$.
Using the ideal gas law,

$$
mg = (n MAh)g = \frac{MPAhg}{k_BT}.
$$

Consider an infinitesimally thin parcel, $h = dz$, where $z$ is the
height above the ground.
The difference in pressure above and below is $-dP$ (decreasing as $z$
increases), so that $mg = -A \, dP$ implies

$$
\frac{dP}{P} = -\frac{Mg}{k_BT}\, dz.
$$

This is a differential equation we can solve immediately by
integrating both sides, and obtain the *barometric equation*:

$$
P = P_0e^{-z/\lambda}, \quad \lambda = \frac{k_BT}{Mg},
$$

where $P_0$ is the pressure at $z=0$, and $\lambda$ is called the
*scale height*.
So, in our oomeist model, pressure decreases exponenentially, and is
effectively zero after a few scale heights. We will discuss the
number of scale heights needed for engineering purposes below.

Let's add some numbers now.
The pressure at ground height is just atmospheric pressure,

$$
P_0 = 1 \text{ atm} =  101.1 \text{ kPA}.
$$

The scale depends on a number of things, including temperature,
gravity, and the mass of air molecules.
The last one is easiest.
Air is mostly nitrogen gas $\text{N}_2$ ($28$ atomic mass units), made a
bit heavier by oxygen gas $\text{O}_2$ ($32$ amu), leading to an average
molecular mass

$$
M = 29 \text{ amu} = 48 \times 10^{-26} \text{ kg}.
$$

Neither temperature nor gravitational acceleration are really fixed as
we go far away from the earth.
But we'll assume they vary slowly enough that the scale height can be
computed keeping them constant, and see if this is reasonable.
The average surface temperature of the earth is a cool room, $T = 15^\circ
\text{ C} \approx 290 \text{ K}$, and gravitational acceleration at the
surface is $g = 9.8 \text{ m/s}^2$.
Putting it all together, we get a scale height

$$
\lambda = \frac{k_BT}{Mg} = \frac{(1.4 \times 10^{-23})290}{(4.8
\times 10^{-26})(9.8)} \text{ m} = 8.4 \text{ km}.
$$

This is pretty small! The pressure inside a vacuum clear is around $20
\text{ kPa}$, so this occurs around height

$$
z = \lambda \log \left(\frac{101.1}{20}\right) \approx 13 \text{ km}.
$$

A vacuum cleaner seems like a good place to cap off the atmosphere,
though we will discuss other possibilities below.

##### 3.2. Temperature and gravity*<a id="sec-3-2" name="sec-3-2"></a>

Perhaps, to be really responsible, we should drop our oomeist
prejudices for a moment and acknowledge that it gets colder and
gravity weakens as you go up, and that air is not ideal.
How does that change things?
Gravity is easiest.
From Newton's universal law of gravitation,

$$
g(z) = \frac{GM_\oplus}{(R_\oplus + z)^2},
$$

where $R_\oplus = 6.3 \times 10^6 \text{ m}$ is the radius of the
earth, $M_\oplus = 6.0 \times 10^{24} \text{ kg}$ is its mass, and
$G = 6.67 \times 10^{-11}$ is Newton's constant, in SI units.
This leads to an equation

$$
\frac{dP}{P} = -\frac{M GM_\oplus}{k_BT}\, \frac{dz}{(R_\oplus + z)^2}.
$$

Once again, we just integrate to get

$$
P = P_0 e^{-\lambda} \exp\left[\frac{M GM_\oplus}{k_BT (R_\oplus + z)}\right].
$$

To see if we really need to worry about this, we do a binomial
expansion for $z \ll R_\oplus$ (which is all we will ever worry about)

$$
\frac{1}{R_\oplus + z} \approx \frac{1}{R_\oplus}\left(1 - \frac{z}{R_\oplus}\right).
$$

Plugging back in returns our original barometric formula.
So, as long as we stick to heights much smaller than the earth's
radius, we're good.

What about temperature? This is tricky, since we need some
thermodynamics, and in particular, a further equilibrium condition to
obtain a relation between $T$ and $P$.
Let's assume it isn't raining, and the atmosphere is dry enough for
equilibrium to be set by an *adiabatic* process, where $dQ = T\, dS = 0$.
Then we can relate $T$ and $P$ using the $T\, dS$ equation for
variables $T$ and $P$, using the ideal gas law:

$$
  0 = C_P \, dT - T \frac{\partial V}{\partial T}\bigg|_P \, dP = C_P
  \, dT - V \, dP,
  $$

where we used the ideal gas law, and $C_P$ is the heat capacity for a
volume $V$ of air at constant pressure.
Note that $C_P$ can be written in terms of the degrees of freedom $f$
of the gas as

$$
  C_P = \frac{\gamma N k_B}{\gamma - 1}, \quad \gamma = 1 +
  \frac{2}{f}.
  $$

Plugging this into the result for hydrostatic equilibrium, we find that

$$
dT = \frac{V}{C_P} \, dP = -\frac{Mg(\gamma-1)}{k_B\gamma }\, dz \quad
\Longrightarrow \quad T = T_0 -\left[\frac{Mg(\gamma-1)}{k_B\gamma
}\right] z.
$$

For nitrogen or oxygen gas at atmospheric temperatures, $f = 5$,
consisting of three translational and two rotational degrees of
freedom. There is a vibrational mode at higher temperatures we can
ignore.
Plugging these in, we get a rate of change of temperature, or
*temperature lapse rate*

$$
L = \frac{Mg(\gamma-1)}{k_B\gamma} = \frac{(4.8
\times 10^{-26}) 9.8 \cdot 0.4}{(1.4 \times 10^{-23}) 1.4} \text{ K/m}
\approx 9.6 \text{ K/km}.
$$

It drops roughly $10^\circ \text{ C}$ for every kilometre we go up.
Finally, if we plug this result for temperature back into our result
for hydrostatic equilibrium, we find

$$
\frac{dP}{P} = -\frac{Mg}{k_B(T_0 - L z)}\, dz.
$$

Integrating both sides gives a modified barometric equation, obeying a
power law rather than an exponential:

$$
P = P_0\left(1 - \frac{Lz}{T_0}\right)^{Mg/k_B L}.
$$

Does this change the "vacuum cleaner" height of the atmosphere? Not
by much. It now hits $20 \text{ kPa}$ a bit earlier at $z  = 11 \text{
km}$.
The average height of the atmosphere is $12 \text{ km}$, so both
estimates are reasonable.

##### 3.3. High pressure environment<a id="sec-3-3" name="sec-3-3"></a>
