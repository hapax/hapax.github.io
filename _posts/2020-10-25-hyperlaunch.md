---
Layout: post
mathjax: true
comments: true
title:  "A hyperlauncher to the stars"
categories: [Physics, Engineering]
date:  2020-10-25
---

**October 25, 2020.** *In which I pretend to be Elon Musk, and propose
  to launch rockets into space using vacuum tubes. We'll learn a
  little about atmospheric physics, rockets, and building giant
  cylinders, in order to sketch a proof-of-concept.*

#### Contents

1. <a href="#sec-1">Introduction</a>
   1. <a href="#sec-1-1">The basic design</a>
2. <a href="#sec-2">The physics</a>
   1. <a href="#sec-2-1">The barometric equation</a>
   2. <a href="#sec-2-2">Temperature and gravity*</a>
   3. <a href="#sec-2-3">The size of the plunger</a>
3. <a href="#sec-3">Design considerations</a>
   1. <a href="#sec-3-1">Vacuum vexation</a>
   2. <a href="#sec-3-2">Stabilising the plunger</a>
   3. <a href="#sec-3-3">Cylinder stress and construction</a>
4. <a href="#sec-4">Conclusion</a>

##### 1. Introduction<a id="sec-1" name="sec-1"></a>

Elon Musk is the CEO and founder of SpaceX, a company which sends
rockets into space. Along with engineers at Tesla and SpaceX, he also
proposed a wacky, high-speed alternative to trains: the *hyperloop*,
the pneumatic tube for people. In this post, I conduct an initial
feasibility study for combining these two ideas, and launching rockets
into space with *vertical* hyperloops.
I call this the "hyperlauncher".

Since this is merely a feasibility analysis, I will ignore most of the
important engineering problems, and focus on the physics.
And even though I am focusing on the physics, I will adopt a
philosophy of order-of-magnitude (oom) estimates, which I call
*oomism*.
I state for the record that "oomism" and the "hyperlauncher" are very,
very serious business.

*Note: pictures to come.*

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

#### 3.1. Vacuum vexation<a id="sec-3-1" name="sec-3-1"></a>

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
I imagine a sort of shutter mechanism, which can be progressively opened
as the payload comes through, minimising the amount of flooding.
So now our French press-vacuum cleaner is combined with a camera!

#### 3.2. Stabilising the plunger<a id="sec-3-2" name="sec-3-2"></a>

I've been discussing "cylinders" this whole time, hedging on the shape of the plunger.
It seems that, for reasons a symmetry, an old-fashioned circular
cross-section should work best.
If the platform had corners, for instance, these might form points of
preferential vacuum leakage, while a circular platform means we have
one uniform design problem for the edge.
But the circle has an additional advantage we will see in a moment.
If an instability develops, the plunger can tilt, or
even flip, which would obviously be disastrous for the payload.
There needs to be some way to counteract this.
A simple mechanical constraint is a *thick* plunger which
does not have the room to flip within the cylinder.
This increases the mass, and obviously, we don't want the plunger
scraping the sides since friction will reduce launch energies.
We want a smooth ride, with no tilt and no friction.

One entertaining possibility is to stabilise the plunger by spinning it,
just like a frisbee.
The payload itself need not spin, if placed on a gyroscopically
isolated platform above the base of the plunger.
The energy for spinning can be obtained during launch itself by
deploying an array of angled flanges beneath the plunger, and any
excess energy not used for rotation can be stored in flywheels to help
depress the plunger on future runs.
Regarding the rotation itself, the stabilised plunger could spin by
means of bearings around its perimeter, with rolling friction instead
of scraping.
I leave the calculation of the energy dissipation from bearings to a
longer paper expected April next year.

A final question is how the vacuum itself is maintained around the
edges of the plunger.
Another cute possibility is to use the vacuum against itself, adding a
"collar" at the edge, a membrane which seals the "pocket" around the
perimeter with the rolling bearings.
The vacuum will press the collar against the walls of the cylinder and
keep the pocket sealed!
Depending on the interface between the collar and the walls, large
amounts of sliding friction may be generated; this is another
engineering problem I leave to future work.
But in case air does enter the pocket, one could also equip
the base of the plunger with a means of ejecting it.
Again, we could use excess launch energy to power small vacuum pumps
which, connected to the pocket, can flush out any stray air.

<!-- One possibility is a scroll-compressor which can be isolated from the
pocket during a "charging" phase --- once again with excess launch
energy --- but connects to the pocket sucks air out of it during the
"discharging" phase.The budget of excess energy, and expenditure on stabilisation and
vacuum maintenance, is an interesting problem but beyond the scope of
our oomist considerations.-->

#### 3.3. Cylinder stress and construction<a id="sec-3-3" name="sec-3-3"></a>

Finally, we come to the elephant in the oom: the construction of the
cylinder itself.
We are envisioning a structure on the order of a scale height, more
than $10$ times taller than the tallest building ever constructed.
It must not only stand up, i.e. support its own weight, but resist
buckling under the massive pressure of air outside it.
Again, a circular design leads to a uniform distribution of this
pressure.
In line with oomism, we will ignore inhomogeneities, and think about
how a perfect cylinder is compressed by atmospheric pressure, called
*cylinder stress*.
This is the source of many an engineering disaster, though usually the
pressure is on the *inside*, e.g. the
[great Molasses flood](https://en.wikipedia.org/wiki/Great_Molasses_Flood)
of 1919.

Suppose the cylinder has radius $R$ and thickness $d \ll R$.
For thin walls, the
[Young-Laplace equation](https://en.wikipedia.org/wiki/Young%E2%80%93Laplace_equation)
applies, and the cylinder is compressed by a stress

$$
\sigma = \frac{RP}{d}.
$$

Here, the surface tension is $\sigma d$ (force per unit length), but
the tensile stress is $\sigma$ (for per unit area).
We now treat the cylinder as a bent sheet, subject to a stress
$\sigma$.
If the material has Young's modulus $\mathcal{E}$ (not to be confused
with launch energy), the *strain* $\epsilon$ or fractional change in
length is

$$
\epsilon = \frac{\Delta R}{R} = \frac{\sigma}{\mathcal{E}} = \frac{RP}{d \mathcal{E}}.
$$

Thus, the change in radius is

$$
\Delta R = \frac{R^2P}{d\mathcal{E}}.
$$

This relationship only holds up to the *yield point*, a
material-dependent value of the stress at which the response to further stress becomes
nonlinear.
<!-- Somewhere beyond this point, the material itself will
rupture.We can imagine engineering $R$ and $t$ so as to obtain a uniform
cylinder, though we are ignoring the complexities of axial stress for
the purposes of oompoc.-->
Our goal now will be to see what materials we could use and how thick
they will need to be, noting that the strain at ground level is

$$
\epsilon = \frac{RP_0}{d \mathcal{E}}.
$$

First, let's take our earlier calculation of the Falcon Heavy
launchpad.
Rockets will be much lighter if they don't need to carry their own
fuel, but we are not taking the weight of the plunger into account.
At any rate, the radius will be

$$
R = \sqrt{\frac{A}{\pi}} = \sqrt{\frac{900 \text{ m}^2}{\pi}} = 17
\text{ m}.
$$

For concreteness, let's use steel, which can sustain a stress of
around $\sigma_\text{YP} = 500 \text{ MPa}$, with a Young's modulus of
around $\mathcal{E} = 200 \text{ GPa}$.
Then at the yield point, we have a strain

$$
\epsilon = \frac{500 \times 10^6}{200 \times 10^9} = 2.5\times 10^{-3}
$$

This corresponds to a thickness of at least

$$
d = \frac{RP_0}{\epsilon\mathcal{E}} = \frac{17(101.1 \times
10^3)}{2.5\times 10^{-3}(200 \times 10^9)} \text{ m} \approx 3 \text{ mm}.
$$

So, steel $3 \text{ mm}$ thick should resist buckling, and contract
around $\epsilon 3 \text{ mm} = 8$ microns in radius.
The pressures drop as we ascend, so this thickness can be reduced as
we go up, and the radius slowly varied to ensure close to uniform
thickness (though the Young's modulus may be high enough to ignore
this).
So, for a cylinder of height $H = X\lambda$, we estimate the volume of steel
require to resist buckling is at most

$$
V = 2\pi R d H = 2700 X \text{ m}^3.
$$

A cubic meter of steel costs around $\text{USD}4000$, so the raw materials for a hyperlauncher a couple of scale
heights high will cost a mere $\text{USD}22$ million dollars, ignoring
savings due to tapering thickness or costs needed for additional
structural reinforcement.
This sounds very promising, but of course, the real problem is weight.
Steel has a density of $\rho = 8 \text{ tonnes/m}^3$. The resulting
strain at the base is

$$
\sigma_\text{mass} = \frac{V\rho}{2\pi R t} = \rho g H.
$$

Thus, at the thickness needed to resist buckling, the maximum height
(in scale heights) is

$$
X = \frac{\sigma_\text{YP}}{\lambda\rho g} = 0.75.
$$

<!--\frac{500 \times 10^6}{8 \times 10^3 (9.8)}-->
Before our steel cylinder reaches a scale height, it will collapse
under its own weight!

Thus, we see that in order to fully exploit the power of atmospheric
pressure for launching rockets, we have another engineering problem to solve: finding a
suitably strong but light material which can replace steel.
Another major problem is *wind loading*,
i.e. ensuring the structure will not be knocked over by the wind.
It may be that the structural reinforcements which solve this problem
also help distribute the cylinder's weight.
But I won't discuss either of these issues further here.

##### 4. Conclusion<a id="sec-4" name="sec-4"></a>

What started a couple of days ago as a light-hearted tribute to the
pioneering spirit of Elon Musk has, by this point, become a circus of
high-concept oomism. I hope you've enjoyed it; I certainly have.
Please leave a comment or drop me an email if you spot any errors, or
have suggestions for improving the design.
Perhaps one day we will leave the world of kerosene and boosters
behind us, and embark on a bold new age of rockets on frisbees sucked by vacuum cleaners up a
French press and spat out through a camera shutter: our hyperlauncher
to the stars.
