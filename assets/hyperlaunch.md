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
   2. <a href="#sec-3-2">High pressure environment</a>
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
= 1.38 \times 10^{-23}$ in SI units, and $T$ is absolute temperature,
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
integrating both sides:

$$
P = P_0\exp\left[ -\lambda_s^{-1} z\right], \quad \lambda_s = \frac{k_BT}{Mg},
$$

where $P_0$ is the pressure at $z=0$, and $\lambda_s$ is called the
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
bit heavier by oxygen in various compounds, leading an average
molecular mass

$$
M = 29 \text{ amu} = 48 \times 10^{-26} \text{ kg}.
$$

Neither temperature nor gravitational acceleration are really fixed as
we go far away from the earth.
But we'll assume they vary slowly enough that the scale height can be
computed keeping them constant, and see if this is reasonable.
The average surface temperature of the earth is a cool room, $T = 15^\circ
\text{ C} = 288 \text{ K}$, and gravitational acceleration at the
surface is $g = 9.8 \text{ m/s}^2$.
Putting it all together, we get a scale height

$$
\lambda_s = \frac{k_BT}{Mg} = \frac{(1.38 \times 10^{-23})288}{(4.8
\times 10^{-26})(9.8)} \text{ m} = 8.45 \text{ km}.
$$

This is fairly small, so for 

##### 3.2. High pressure environment<a id="sec-3-2" name="sec-3-2"></a>
