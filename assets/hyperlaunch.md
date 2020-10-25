---
Layout: post
mathjax: true
comments: true
title:  "A hyperlaunch to space"
categories: [Physics, Engineering]
date:  2020-10-26
---

**October 26, 2020.** *In which I pretend to be Elon Musk, and propose
  to launch rockets into space using vacuum tubes. We'll learn a
  little about atmospheric physics and rockets, and much less about
  real design considerations, to provide a proof-of-concept.*

#### Contents

1. <a href="#sec-1">Introduction</a>
   1. <a href="#sec-1-1">The basic design</a>
3. <a href="#sec-2">The physics</a>
   1. <a href="#sec-2-1">The barometric equation</a>
   2. <a href="#sec-2-2">Temperature and gravity*</a>
   3. <a href="#sec-2-3">The size of the plunger</a>
4. <a href="#sec-3">Design considerations</a>
   1. <a href="#sec-3-1">Vacuum vexation</a>
   2. <a href="#sec-3-2">The French press</a>

##### 1. Introduction<a id="sec-1" name="sec-1"></a>

Elon Musk is the CEO and founder of SpaceX, a company which sends
rockets into space. Along with engineers at Tesla and SpaceX, he also
proposed a wacky, high-speed alternative to trains: the *hyperloop*,
the pneumatic tube for people. In this post, I conduct an initial
feasibility study for combining these two ideas, and launching rockets
into space with *vertical* hyperloops.
I call this the "hyperlaunch".

Since this is merely a feasibility analysis, I will ignore most of the
important engineering problems, and focus on the physics.
And even though I am focusing on the physics, I will adopt a
philosophy of order-of-magnitude (oom) estimates, which I call
*oomism*.
I state for the record that "oomism" and the "hyperlaunch" are very,
very serious business.

#### 1.1. The basic design<a id="sec-2-1" name="sec-2-1"></a>

The basic idea of the hyperlaunch is simple.
Take a giant cylinder, stretching from the ground to the top of the
atmosphere, and put a "plunger" inside which can move up and down,
just like a French press.
If the cylinder and plunger are airtight, one can imagine evacuating
the cylinder and placing the plunger at the bottom, just above the
ground.
One can then flood the the area beneath the plunger with air from
outside the cylinder, at atmospheric pressure, which rushes in and
pushes the plunger into the vacuum above it, from ground level to the
top of the atmosphere, where the object, if it has acquired enough
energy, is liberated from the earth's gravitational pull.
If you prefer household objects to technocrats, we can think of the
hyperlaunch as a French press combined with a vacuum cleaner.

In the next section, we'll discuss simple models of atmospheric
pressure, and check that our scheme can, in principle, launch objects
into space.
This will constitute an oomist proof-of-concept, or *oompoc*.
In the final section, we discuss some elementary issues of design and
engineering.

##### 2. The physics<a id="sec-2" name="sec-2"></a>

Now that the high-concept pitch is out of the way, we have some physics to do. Can we
launch anything? How light must it be? What physics are we neglecting?
We'll address all of these, though with a more or less oomist lens.

#### 2.1. The barometric equation<a id="sec-2-1" name="sec-2-1"></a>

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
So, in our oomist model, pressure decreases exponenentially, and is
effectively zero after a few scale heights. 
Let's calculate some actual numbers.
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

This is pretty small! To get some sense of how quickly this drops,
note that the pressure inside a vacuum cleaner is around $20
\text{ kPa}$. This occurs around height

$$
z = \lambda \log \left(\frac{101.1}{20}\right) \approx 13 \text{ km}.
$$

A vacuum cleaner seems like a good place to cap off the atmosphere,
though we will discuss other possibilities below.

#### 2.2. Temperature and gravity*<a id="sec-2-2" name="sec-2-2"></a>

Perhaps, to be really responsible, we should drop our oomy
prejudices for a moment and acknowledge that it gets colder and
gravity weakens as you go up.
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

Plugging this in, we recover our original barometric formula.
So, as long as we stick to heights much smaller than the earth's
radius, we don't need to worry about changing gravity.

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
*lapse rate*

$$
L = \frac{Mg(\gamma-1)}{k_B\gamma} = \frac{(4.8
\times 10^{-26}) 9.8 \cdot 0.4}{(1.4 \times 10^{-23}) 1.4} \text{ K/m}
\approx 9.6 \text{ K/km}.
$$

It drops roughly $10^\circ \text{ C}$ for every kilometre we go up.
Finally, if we substitute this result for temperature back into our
differential equation for hydrostatic equilibrium, we find

$$
\frac{dP}{P} = -\frac{Mg}{k_B(T_0 - L z)}\, dz.
$$

Integrating both sides gives a modified barometric equation, obeying a
power law rather than an exponential:

$$
P = P_0\left(1 - \frac{Lz}{T_0}\right)^{\Lambda}, \quad \Lambda = \frac{Mg}{k_BL}.
$$

Does this change the "vacuum cleaner" height of the atmosphere? Not
by much. It now hits $20 \text{ kPa}$ a bit earlier at $z  = 11 \text{
km}$.
The average height of the atmosphere is $12 \text{ km}$, so both
estimates are reasonable.

#### 2.3. The size of the plunger<a id="sec-2-3" name="sec-2-3"></a>

Let's see how much energy can be delivered to our giant plunger when
we flood the base with air at atmospheric pressure.
If $A$ is the area of the plunger, then as we travel up a height $H$,
the total energy delivered is just the work done by pressure:

$$
E = A\int_0^H dz \, P(z).
$$

The result will depend on which version of the barometric formula we
use.
For the constant temperature case, the energy is

$$
E_1(H) = A\int_0^H dz \, P_0 e^{-z/\lambda} = AP_0 \lambda \left(1 - e^{-H/\lambda}\right).
$$

For a lapse rate $L$, we instead have

$$
E_2(H) = A\int_0^H dz \, P_0\left(1 - \frac{Lz}{T_0}\right)^{\Lambda} =
\frac{AP_0T_0}{L(\Lambda+1)}\left[1 - \left(1 - \frac{LH}{T_0}\right)^{\Lambda+1}\right].
$$

Both have some maximum energy they can provide per unit area of
plunger.
In the first case, take $H \gg \lambda$, we obtain

$$
\epsilon_1 = \frac{E_1}{A} = P_0 \lambda = 8.5 \times 10^{8}
\text{ J/m}^2.
$$

In the second case, our formula stops making sense when the
temperature hits zero, at $H  = T_0/L$, so we have

$$
\epsilon_2 = \frac{E_2}{A} = \frac{P_0T_0}{L(\Lambda+1)} = 6.8 \times 10^{10}
\text{ J/m}^2.
$$

<!-- 101.1*290/((9.6/1000)(1+((4.8 \times 10^{-26}) 9.8)/((1.4 \times 10^{-23})*(9.6/1000))))-->
We will use the latter estimate because it gives us more energy!
Ahem, I mean because it is more realistic.
A rocket of mass $m$ at the earth's surface has gravitational potential energy

$$
U = -\frac{GM_\oplus m}{R_\oplus} = -mg R_\oplus.
$$

If we want to launch this into space, we need to provide at least this
much energy in order for it to escape the earth's gravitational field.
The minimum plunger size is then

$$
A = \frac{|U|}{\epsilon_2} = \frac{mg R_\oplus L(\Lambda+1)}{P_0T_0}.
$$

A typical rocket mass is on the order of $m = 10^6 \text{ kg}$, so the
minimum area of plunger needed is

$$
A = \frac{10^6 \cdot 9.8 \cdot (6.3 \times 10^6)}{6.8 \times 10^{10}}
\text{ m}^2 = 900 \text{ m}^2.
$$

This is only slightly larger than the area of the Falcon Heavy if laid flat!
If we want to launch a $m  = 1\text{ kg}$ cubesat instead, our
platform can be a million times smaller, so the $100 \text{ cm}^2$
base of the cubesat itself is more than sufficient.

Of course, we are ignoring the mass of the platform.
Assuming it has some areal density $\rho$, then we must instead have

$$
A \geq \frac{m g R_\oplus}{P_0 \lambda - \rho g R_\oplus}.
$$

This means that if $P_0\lambda > \rho g R_\oplus$, i.e. the plunger
can launch itself, it can launch anything else, provided the object is
light enough or the plunger big enough.
This completes our oompoc that a French press cross
vacuum cleaner can launch rockets.

##### 3. Design considerations<a id="sec-3" name="sec-3"></a>

In this last section, we'll address a few basic design concerns, such
as establishing and maintaining the vacuum, the firing mechanism, and
construction.

#### 3.1. Vacuum vexation <a id="sec-3-1" name="sec-3-1"></a>

A simple question is: realistically, how big does the tube need to be?
If it is only $12 \text{ km}$, there is still a pressure of $20 \text{
kPa}$ or so, not to mention mass. Even if we evacuate the cylinder, air will immediately
flood back in at the top.
But how quickly?
Consider the slice of air of height $h$ just above the
cylinder, at height $H$.
We would like $h$ much smaller than the rate of change of $P$,
so it is effectively constant.
This slice mass and is subject to a pressure $P$ from above, so that it is
subject to a combined pressure

$$
P_\text{top} = P + nM gh.
$$

A unit area part of this slice will fall (initially) according to

$$
z(t) = H - \left(\frac{P + nM gh}{2nM h}\right) t^2.
$$

The timescale for appreciable flooding of the top of the cylinder is thus

$$
\tau_\text{flood} \sim \sqrt{\frac{2H}{P/nMh + g}}.
$$

We can make this timescale large enough for practical purposes by
making $P$ small.
For analytic simplicity, let's work with the constant temperature
barometric formula.
Consider $h \ll \lambda$, so that (after a little algebra)

$$
\frac{P}{nMh} \gg g.
$$

Then using the ideal gas law,

$$
\tau_\text{flood} \sim \sqrt{\frac{2nhMH}{P}} = \sqrt{\frac{2hMH}{k_BT}}.
$$

Let's express our heights in terms of scale heights, $x = h/\lambda$
and $X = H/\lambda$.
Then our earlier numbers give

$$
\tau_\text{flood} \approx 0.04 \sqrt{Xx} \text{ s}.
$$

The flooding timescale depends on the geometric mean of the cylinder height $H$
and parcel height $h$, or $\sqrt{Xx}$ in dimensionless terms.
If we want a window of, say, $5$ minutes, we will need an absurd
number of scale heights.

I doubt the situation will improve in more realistic models, so it
seems we must seal the top of the cylinder when we evacuate it, and
open it when we launch.
This seal does not need to be particularly hardy, since the pressures
at the top will be low.
More importantly, it will need to open quickly so that the payload
arrives well before the flooding timescale.
I imagine a sort of shutter mechanism, which can progressively opened
as the payload comes through, minimising the amount of flooding.
So now our French press-vacuum cleaner is combined with a camera!

#### 3.2. The French press<a id="sec-3-2" name="sec-3-2"></a>

I've been discussing "cylinders" this whole time, remaining cagey
about the actual shape of the plunger.
It seems that, for reasons a symmetry, an old-fashioned circular
cross-section should work best.
If the platform had corners, for instance, these might form points of
preferential vacuum leakage, while a circular platform means we have
one uniform design problem for the edge.
Let's address that problem now.

First of all, if an instability develops, the plunger can tilt, or
even flip, which would obviously be disastrous for the payload.
So there needs to be some way to counteract this.
A simple mechanical constraint is to design a *thick* plunger which
does not physical have room to flip.
This increases the mass, and obviously, we do not want the plunger
scraping the sides of the cylinder since this friction will reduce
launch energies.

#### 3.3. Construction<a id="sec-3-3" name="sec-3-3"></a>
