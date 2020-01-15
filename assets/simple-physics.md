---
Layout: post
mathjax: true
comments: true
title:  "The awesome power of simple physics"
categories: [Physics, Teaching, Hacks]
date:  2020-01-06
---

**January 6, 2020.** *Physics is awesomely powerful. Contrary to popular opinion, you don't need
  years of advanced mathematics to taste this power! Simple
  physics hacks and pre-calculus mathematics are
  enough, as I copiously illustrate.*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Dimensional analysis</a>
   1. <a href="#sec-2-1">Pendulous pumpkins</a>
   2. <a href="#sec-2-2">Drag and drop</a>
   3. <a href="#sec-2-3">Usage notes</a>
3. <a href="#sec-3">Fermi estimates</a>
   1. <a href="#sec-3-1">Geometric means</a>
   2. <a href="#sec-3-2">Subestimates</a>
   3. <a href="#sec-3-3">KISS</a>
   4. <a href="#sec-3-4">Usage notes</a>
4. <a href="#sec-4">Scaling</a>
   1. <a href="#sec-4-1">Random walks</a>
   3. <a href="#sec-4-3">Fractals</a>
   4. <a href="#sec-4-4">Power laws</a>
5. <a href="#sec-5">Conclusion</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

How many calculus courses does it take to change a light bulb?
The answer is none, of course.
And how many does it take to work out the period of a
pendulum, why clouds float, or the number of fish in the sea?
Surprisingly, the answer is still none!
As we'll see below, high school math and some simple physics hacks
are sufficient to solve these problems *quantitatively*.
The goal of this post is to explain these hacks and convince
you of their awesome power.

I'm a string theorist, so by necessity a user (and abuser!) of
advanced mathematics.
But preparing for a
[comprehensive exam](https://www.phas.ubc.ca/graduate-program-comprehensive-exam-guidelines-phd-students) and running a
[high school physics circle](https://outreach.phas.ubc.ca/events/metro-vancouver-physics-circle/)
convinced me that *you can do more with less*.
Without calculus or any deep physical lore,
you can still discover
[black hole entropy](https://en.wikipedia.org/wiki/Black_hole_thermodynamics#Overview),
the [dark energy](https://en.wikipedia.org/wiki/Dark_energy) density
of the universe,
[gravitational lensing](https://en.wikipedia.org/wiki/Gravitational_lens),
and even the number of
[extra dimensions](https://en.wikipedia.org/wiki/String_theory#Extra_dimensions)
predicted by string theory.
(See my
[physics circle problems](https://hapax.github.io/assets/circle-probs.pdf)
if you want to learn how.
They have very little overlap with the problems here.)

This post focuses on a set of generic problem-solving tools: *dimensional analysis*, *Fermi approximation*, and *scaling
laws*.
It is not oriented towards problem-solving heuristics (e.g. limiting
arguments or symmetry) or surprisingly useful physical laws (e.g. Stefan-Boltzmann), though
there is nontrivial overlap and I hope to say more about these in future.
I have stuck to methods accessible to high school and first year
students, though it is fair to say some scientific
maturity is required of the former.
The different sections can more or less be dipped into independently.

## 2. Dimensional analysis <a id="sec-2" name="sec-2"></a>

Physics is ultimately about experimental measurements.
We take some system, e.g., an old pumpkin, and poke or prod it with a
measuring device which returns a number.
The *dimension* of the measurement is not the number, but rather the
*physical property* probed by that device.
If we compare the width of the pumpkin to a ruler, for instance, the
dimension is the length.

Length ($L$) is one basic dimension.
Two other basic dimensions are *time* ($T$) and *mass* ($M$).
In general, we apply brackets $[\cdot]$ to a measurement to extract
the dimension, for instance

$$
[1 \text{ cm}] = L, \quad [4 \text{ hours}] = T, \quad [400 \text{ lb}] = M.
$$

We throw away the number out front and focus on the unit, asking: what
aspect of the system does it measure? Centimetres measure length,
hours measure time, and pounds measure mass.
More complicated dimensions follow from the basic ones according to
simple algebraic rules, easier to show than tell.
Area, for example, has dimensions $L^2$:

$$
[1 \text{ cm}^2] = [1 \text{ cm} \times 1 \text{ cm}] = [1 \text{ cm}]
\times [1 \text{ cm}] = L^2.
$$

Rather than use the units, we can use general formulas, e.g. for the area of a rectangle:

$$
[\text{area}] = [\text{width}\times \text{height}] = [\text{width}]
\times [\text{height}] = L^2.
$$

Similarly, we can divide out dimensions:

$$
[\text{velocity}] = \left[\frac{\text{distance}}{\text{time}}\right] =
\frac{[\text{distance}]}{[\text{time}]} = \frac{L}{T}.
$$

Physical laws tell us how measurements depend
on each other.
For example, Newton's second law $F = ma$ tells us how measurements of
force, mass and acceleration are related.
If the two sides of $F = ma$ are equal, the dimensions must agree,
with

$$
[F] = [m a] = [m]\times \left[\frac{v}{t}\right] = \frac{ML}{T^2}.
$$

Remarkably, we can sometimes *reverse* this process, and determine the
physical laws relating quantities from their dimensions!
Once again, this is easier to show with examples than abstract descriptions.

### 2.1. Pendulous pumpkins <a id="sec-2-1" name="sec-2-1"></a>

Suppose we attach the old pumpkin to a length of string and give it a
kick.
Gravity will pull on the pumpkin, causing it to oscillate back and
forth with some period of oscillation $t$.
If we know how the period of oscillation depends on other properties
of the system, we can utilise this knowledge to make a pumpkin clock!
Let's start by listing the possibly relevant properties of the system:
- the mass of the pumpkin $m$, with dimension $[m] = M$;
- the length of the string $\ell$, dimension $[\ell] = L$;
- gravitational acceleration $g = 9.8 \text{ m/s}^2$, dimension $[g] =
  LT^{-2}$ (from the units);
- the initial displacement of the pumpkin $x$, dimension $[x] = L$.

Not all of these quantities will turn out to be relevant.
For instance, the size of the initial kick $x$ can be discarded.
Why?
Go grab a string, a pumpkin, and a stopwatch, and you'll find that
(at least for small kicks) the period is independent of the size of
the kick.
That leaves the pumpkin mass $m$, string length $\ell$, and gravity $g$.
You can also eliminate the pumpkin mass empirically, but as we'll see,
we can leave it in and let dimensional analysis *tell us* it's irrelevant.

I'm going to do something a bit sneak (see Exercise 4 for a justification).
Instead of period $t$, we will deal with the *angular velocity*

$$
\omega = \frac{2\pi}{t}.
$$

If we imagine the oscillations as being ticked off on a clock of unit
radius, with one cycle per period, then this is just the velocity of
the tip of the hand.
(We will explain another way to get factors of $2\pi$ in Exercise 3.)
Dimensional analysis is nothing fancier than guessing that $\omega$ is related to $m$,
$\ell$ and $g$ by a physical law of the form

$$
\omega = m^a \ell^b g^c,
$$

for some powers $a, b, c$.
We can determine the powers from the dimensions of each side:

$$
\begin{align*}
T^{-1} = [\omega] = [m^a \ell^c g^c] = \frac{M^aL^{b+c}}{T^{2c}}.
\end{align*}
$$

Requiring the leftmost and rightmost expression to be equal, we can immediately read off the powers:
$a = 0$, $2c = 1$, $b = -c$, and hence $\omega \sim (g/c)^{1/2}$, where $\sim$ means "up to numerical factors".
As promised, dimensional analysis also kindly informs us that the mass
is irrelevant.
In fact, my earlier piece of sneakiness (replacing period with angular
velocity) means this is *exactly* correct (for small kicks):

$$
\omega = \sqrt{\frac{g}{\ell}}.
$$

Let me emphase how powerful this is.
We didn't need to analyse any forces, solve a differential
equation, or even deal with numbers.
Dimensional analysis let us skip straight to the answer!

Suppose we want to make a pumpkin clock with the conventional
grandfather-clock period of $t = 2 \text{
s}$, so that each half swing takes
one second.
Then we should suspend the old pumpkin from a string of length

$$
\ell = \frac{g}{\omega^2} = \frac{g t^2}{(2\pi)^2} = \frac{9.8 \text{
m}}{\pi^2} \approx 1
\text{ m}.
$$

Incidentally, this explains why grandfather clocks are so large.
They will house a large (typically non-cucurbitar) pendulum with
$\ell \approx 1$ m.
In order to make the clock, we need a ruler to measure out the length
of string.
But for maximal whimsy, we can switch things up, and turn a stopwatch,
pumpkin and spool into a ruler!
Measure with the string, snip off the corresponding length, attach
the pumpkin and gently wobble.
By timing the period with the stopwatch, you can figure out how long
things are!

---

**Exercise 1 (interplanetary pumpkins).** You can use an old pumpkin to
measure very large objects as well.
Place the sun at one end of the object, and the pumpkin at the other.
If you kick the pumpkin with enough energy tangent to the sun,
it will orbit in a circle of radius $r$ (the length of the
object) with angular velocity $\omega$.
Using dimensional analysis, show that

$$
r \sim \left[\frac{GM}{\omega^2}\right]^{1/3},
$$

where $M$ is the mass of the sun and $G = 6.7 \times 10^{-11} \text{
m}^3 \text{/kg s}^2$ is *Newton's constant*, controlling the strength
of gravity.
(This relation is
[Kepler's third law!](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion#Third_law))

*Hint.* You can ignore the mass of the pumpkin due to the
[equivalence principle](https://en.wikipedia.org/wiki/Equivalence_principle),
i.e. because objects fall the same way in gravitational fields, whatever
their mass.

---

### 2.2. Drag and drop<a id="sec-2-2" name="sec-2-2"></a>

*Stokes' law.* Maybe pumpkins aren't your thing.
Let's ratchet down the
whimsy and turn to something more high-minded: the
aerodynamics of spheres.
So, imagine a sphere moving through a fluid, e.g. a
[Bathysphere](https://en.wikipedia.org/wiki/Bathysphere) sinking to
the ocean floor.
(You can explore this example in Exercise 2.)
In realistic fluids, nearby layers of flow like to stick together and will
resist *shearing* forces which pull them apart.
Dragging an object through a fluid will then take work, because the
fluid has to shear as it moves around the object.
This resistance to shearing is called [*viscosity*](https://en.wikipedia.org/wiki/Viscosity).

Our goal will be to determine the drag force on a sphere due to viscosity.
Here are some possibly relevant features of the system:
- the radius of the sphere $r$, dimension $[r] = L$;
- the speed of the sphere $v$, dimension $[v] = LT^{-1}$;
- the mass of the sphere $m$, dimension $[m] = M$;
- the density of the fluid $\rho$, dimension $[\rho] = ML^{-3}$;
- the viscosity of the fluid $\mu$.

In principle, all of these factors are involved, but this is too much
for dimensional analysis to handle.
(See the <a href="#sec-2-4">usage notes</a> to understand why.)
When the sphere moves slowly enough, however, its mass $m$ and the
density of the fluid $\rho$ are irrelevant.
Only the viscosity, and size and speed of the sphere, matter.

I haven't told you the dimensions of viscosity yet, but we can find
them fairly easily.
Imagine two layers of fluid flow separated by a distance $d$.
Suppose I try to separate them by simply moving one layer, parallel to
the second but at speed $v$.
Experiment shows that the fluid will resist with some force $f = F/A$ per
unit area, proportional to $v$ and inversely proportional to the
separation $d$.
The viscosity $\mu$ is the constant of the proportionality, so

$$
f = \frac{F}{A} = \mu \left(\frac{v}{d}\right) \quad \Longrightarrow \quad [\mu] =
\left[\frac{dF}{Av}\right] = \frac{L(ML/T^2)}{L^2(L/T)} = \frac{M}{LT}.
$$

We can now proceed with our dimensional analysis.
Let's write the drag force on the sphere $F_d$ as a product of powers
of the remaining factors:

$$
F_d = r^a v^b \mu^c.
$$

Then

$$
\frac{ML}{T^2} = [F_d] = [r^a v^b \mu^c] = L^a \cdot
\left(\frac{L}{T}\right)^b \cdot \left(\frac{M}{LT}\right)^c = \frac{L^{a+b-c}M^c}{T^{b+c}}.
$$

On the LHS, $M$ appears as $M^1$, so $c = 1$.
The LHS also has $T^{-2}$, so $b+c = b+1 = 2$, and hence $b = 1$.
Finally, the LHS has $L^1$, and comparing to the RHS gives $a + b -c =
a = 1$.
Dimensional analysis thus gives the rather simple answer

$$
F_d \sim \mu r v.
$$

As usual, we can't determine if there is a number out front. With considerably more
work,
[George Stokes](https://en.wikipedia.org/wiki/Sir_George_Stokes,_1st_Baronet)
showed that

$$
F_d = 6\pi \mu r v.
$$

This is called *Stokes' law* in honour of its discoverer.
But we got pretty darn close with a few lines of algebra!

*Why clouds float.* We finish this example by calculating the *terminal velocity* of
water droplets in a cloud.
This will help explain why clouds float and rain falls!
First, consider the general case of a slowly falling sphere.
A sphere of mass $m$ is pulled down by its weight, $F_w = mg$.
As it falls, it is slowed by a drag force proportional to the velocity, $F_d = 6\pi \mu r v$.
The terminal velocity $ v_{\text{term}}$ is the speed at which these
two forces balance out:

$$
F_w = mg = 6\pi \mu r v_{\text{term}} = F_d \quad \Longrightarrow
\quad v_{\text{term}} = \frac{mg}{6\pi \mu r}.
$$

The sphere accelerates until it reaches $v_{\text{term}}$; if it
starts off faster for some reason, it will slow until it reaches $v_{\text{term}}$.
To make life simpler, we can express the mass of the sphere
in terms of its volume $V$ and average density $\rho$:

$$
m = V\rho = \frac{4\pi r^3}{3} \rho \quad \Longrightarrow \quad v_{\text{term}} = \frac{mg}{6\pi \mu r} = \frac{2\rho r^2 g}{9\mu}.
$$

If we like, we can also take buoyancy forces $F_b = V
\rho_\text{fluid}$ into account, where $\rho_{\text{fluid}}$ is the density of the fluid.
This just replaces $\rho$ with $\rho - \rho_{\text{fluid}}$.
Since water is much denser than air, the buoyancy forces in our case
are negligible, so we will ignore them.

The density of water is $\rho \approx 10^3 \text{ kg/m}^3$, and a
[typical droplet of water vapour](https://wxguys.ssec.wisc.edu/2013/09/10/how-fast-do-raindrops-fall/)
has a radius around $r = 2\times 10^{-5} \text{ m}$.
Finally, the viscosity of air is $\mu \approx 2\times 10^{-5} \text{
kg/m s}$.
The terminal speed of a cloud droplet is therefore

$$
v_{\text{term}} = \frac{2\rho r^2 g}{9\mu} = \frac{2(2\times 10^{-5} \text{ m})^2(10^3 \text{
kg/m}^3)(9.8 \text{ m/s}^2)}{9(2\times 10^{-5} \text{
kg/m s})} \approx 0.04 \text{ m/s},
$$

or $4$ centimetres per second.
It requires only mild updrafts of warm air (rising from the warmer
regions near the ground) to keep the cloud aloft.
Stokes' law also explains why rain falls.
The terminal velocity $v_\text{term} \propto r^2$, increasing quickly
as droplets get larger.
If droplets coalesce (for example, with water vapour arriving in an
updraft) they will speed up and fall out of the cloud.
Voilà, rain!

---

**Exercise 2 (sinking balls).**
(a) The [Bathysphere](https://en.wikipedia.org/wiki/Bathysphere) was a
hollow ball of steel designed for deep-sea exploration.
It weighed $2.25$ tons (above water) and had a diameter of $1.45$ m.
Roughly how long would it take to sink to the bottom of the Mariana Trench?
The Mariana Trench is $11$ km deep, and filled with cold water of
viscosity $\mu \approx 0.0016 \text{ kg/m s}$.

*Hint.* Assume it is travelling at terminal velocity, and Stokes' law
applies. You should also take buoyancy forces into account!

(b) Keeping with our theme of whimsical rulers, explain how you can
use Stokes' law to determine the size of small iron spheres dropped in water.

---

### 2.3. Usage notes<a id="sec-2-3" name="sec-2-3"></a>

*Numbers.* Dimensional analysis has its limits.
First of all, since we throw away numbers, it only good up
to an overall numerical factor.
In the first example, I sneakily chose angular velocity so that the
missing numerical factor was $1$, but in the second example, we were off by
$6\pi \approx 20$.
It is perhaps better to think of dimensional analysis as giving
system-dependent *scales* rather than answers to specific questions.
That said, more often than not the missing number is close to $1$, and
we can even account for some factors of $\pi$ by adding an extra
dimension for angles (Exercise 4).

*Constants.* Numbers are dimensionless constants.
However, *dimensionful* constants secretly encode important physical
insights.
Examples include Newton's constant $G$ (Exercise 1) and Boltzmann's
constant $k_B$ (Exercise 3).
See my [notes on dimensional analysis](https://hapax.github.io/assets/dimensional-analysis.pdf)
for more on the role these constants play in dimensional analysis.

*Parametric overload.* A more serious problem is the overabundance of parameters.
If we included the mass of the sphere in the second example,
dimensional analysis would fail: we would not be able to solve the
equations for $a, b$ and $c$, or rather, there would be an *infinite* number of solutions.
Which one do we pick?
With three basic dimensions $M, L, T$, you can have at most three
relevant parameters, since each parameter comes with an unknown $(a,
b,c)$ and each dimension gives us an equation.
Three equations is just right for three unknowns.
Any more unknowns, and you don't have enough equations to determine
them all!

More generally, if you can write everything in terms of $n$
independent basic units, you can have at most $n$ physical parameters
in your dimensional guess; otherwise you have too many unknowns to
determine with your equations.
There are other ways dimensional analysis can break down, e.g. if you
have two relevant quantities (say, two lengths) with the same dimension.
All these subtleties are captured in something called the
[Buckingham $\pi$ theorem](https://en.wikipedia.org/wiki/Buckingham_%CF%80_theorem).
For an elementary treatment, check out my
[notes](https://hapax.github.io/assets/dimensional-analysis.pdf) or
*Street-Fighting Mathematics*.

*Extra dimensions.* Length, mass and time are not
the only basic dimensions.
Two other important dimensions are *temperature* $\Theta$ (measured in
Celsius or Kelvin for instance) and *amount
of stuff* $N$ (usually measured in mol).
These are crucial in atomic physics, thermodynamics and
chemistry, and you can see an application in Exercise 3.
But there are no real restrictions on this list of basic dimensions.
For instance, imagine that artistic taste was objective and did not
vary between individuals.
Humans could "measure" a painting by rating it out of $10$.
The dimension would be the aesthetic merit of a painting, and (as
far as I can tell) there is no way to express this in terms
of other basic dimensions.

---

**Exercise 3 (ideal gas law).** A gas of $\mathcal{N}$ particles takes up
  space (with volume $V$), pushes on its container (with pressure
  $P$), and is hot (with temperature $\mathcal{T}$).
  These properties are not independent!
  Their relationship is revealed by dimensional analysis.

(a) Explain why volume should have dimension $[V] = L^3N$.

(b) Show that pressure has dimension $[P] = M/LT^2$.

(c) In thermodynamics, there is a fundamental constant called
*Boltzmann's constant*, $k_B = 1.38 \times 10^{-23} \text{ J/K}$, 
where $\text{K}$ stands for Kelvin.
Confirm that $k_B$ has dimension

$$
[k_B] = \frac{ML^2}{T^2\Theta}.
$$

(d) Finally, use dimensional analysis to deduce the *ideal gas law*:

$$
PV = \mathcal{N}k_B\mathcal{T}.
$$

<p align="center">
  ⁂
</p>

**Exercise 4 (factors of $\pi$).** We can account for some of the
factors of $\pi$ that keep appearing by introducing a dimension for
angle.
(Sadly, this trick doesn't work for Stokes' law, where the $6\pi$
comes from hard math we are ignoring.)
A periodic system has a cycle, which we track using an arrow rotating at a uniform speed around the unit circle.
The arrow (called a *phasor* if you want to be fancy) subtends an angle of $360^\circ$ over the course of a single
period, so really, a period should be viewed not as a time, but a *time per* $360^\circ$.

If $[360^\circ] = \Xi$ is the dimension of angle, then
$[t_\text{period}] = T/\Xi$.
This will leave factors of $\Xi$ floating around.
To cancel them, we can view $2\pi$ as a "fundamental physical
constant" with dimension $\Xi$.
This isn't totally crazy, since $360^\circ = 2\pi$ radian!

(a) Repeat to the pumpkin problems above, now using $[t_\text{period}] =
T/\Xi$ and $2\pi$ as a conversion factor.
You should obtain the same results!

(b) If your system executes $n$ cycles in the process you're
considering, what conversion factor should you use instead of $2\pi$?

---

## 3. Fermi estimates <a id="sec-3" name="sec-3"></a>

A *Fermi estimate* is a guess accurate to the nearest order of
magnitude, i.e. rounded to the nearest power of $10$.
So, viewed through this generous lens, there are $10$ planets, $100$
countries, and $10$ billion people on the planet.
The finer points of planetary science, contemporary geopolitics, and global
demographics do not affect these guesses!

The nearest power of $10$ is actually a subtle concept.
For instance, is $4$ closer to $1$ or $10$?
If we use a normal or *linear* ruler, the answer is clearly $1$.
But when we are rounding to the nearest power of ten, we do not have
ticks at $0$, $1$, $2$, and so on, but at *powers*:

$$
10^0 = 1, 10^1 = 10, 10^2 = 100, \ldots
$$

We should therefore use a *logarithmic ruler*, where we take logs in
base $10$ and round to the nearest tick, where a tick now represents a
power.
In our case, $\log_{10}4 \approx 0.6$ is closer to $1$ than to $0$,
and hence $4$ actually rounds to $10^1 = 10$!
This is a bit surprising, but the way things work when you think in
Fermi ... termies.

Anyway, on a linear ruler, if there is a tick for every whole number,
rounding to the nearest tick means there is a possible error of $0.5$.
In the same way, rounding to the nearest tick on a logarithmic ruler
has an error of half a tick.
But this really means *half a power of $10$*:

$$
10^{0.5} \approx 3.2.
$$

A Fermi estimate should be accurate up to a factor of around $3.2$,
i.e. the real answer can be around $3$ times bigger or smaller and the
estimate is still correct.
Our earlier counts of planets, countries, and global population, for
instance, are well within a factor of $3$.

In general, it makes life a bit easier if instead of restricting to
order of magnitude per se ($1, 10, 100, \ldots$) we allow for
arbitrary numbers, with the understanding *that they are only accurate
up to a factor of* $10^{0.5}$.
We can denote this using a twiddle, so that

$$
\text{number of countries} \sim 200
$$

means "we guess the number of countries is $200$, possibly up to a
factor of $3$".
Now you know what a Fermi estimate is, let's learn how to do them!

### 3.1. Geometric means<a id="sec-3-1" name="sec-3-1"></a>

On a linear ruler, we average two numbers $a$ and $b$ by halving the sum, $(a+b)/2$.
On a logarithmic ruler, we *take logs first*, then average.
But what does this correspond to when we undo the logs?
Let's check, using log laws.
First, using $\log x + \log y = \log xy$ and $n \log x = \log (x^n)$,
we have

$$
\frac{1}{2}(\log_{10} a + \log_{10} b) = \frac{1}{2}\log_{10} ab = \log_{10}\sqrt{ab}.
$$

From the log law $10^{\log_{10} x} = x$, it follows that

$$
10^{(\log_{10} a + \log_{10} b)/2} = 10^{\log_{10} \sqrt{ab}} = \sqrt{ab}.
$$

This is called the *geometric mean*.
Whenever you are dealing with estimates spread across different orders
of magnitude, this is a better average to use than the *arithmetic
mean* $(a+b)/2$.

Geometric means are useful for averaging an underestimate and an
overestimate.
For instance, if we wanted to guess how many people have been to the
moon, $1$ is clearly an underestimate, and $100$ seems like an
overestimate.
The geometric mean is

$$
\text{moon people} \sim \sqrt{1 \cdot 100} \approx 10.
$$

The answer is actually $12$, so our guess is more or less on the
mooney!

---

**Exercise 5 (lunar radius).** Fermi estimate the radius of the moon.

*Hint.* Take the geometric mean of an overestimate and an underestimate.
For an overestimate, you could try the radius of
the earth, $r_\oplus = 6300 \text{ km}$.

<p align="center">
  ⁂
</p>

**Exercise 6 (beyond your means).** Suppose I want to ask a bunch of people for
  their opinion, and take the geometric rather than the arithmetic
  mean.
  Recall that the usual average of $m$ numbers $a_1, a_2, \ldots, a_m$ is

$$
\frac{a_1+a_2+\cdots + a_m}{m}.
$$

By taking an arithmetic mean on the logarithmic ruler, i.e. of $\log_{10} a_1, \ldots,
\log_{10} a_m$, then plugging your answer into the index, show that
the geometric mean of $m$ numbers is

$$
\sqrt[m]{a_1 \times a_2 \times \cdots a_m}.
$$

---

### 3.2. Subestimates<a id="sec-3-2" name="sec-3-2"></a>

For more complicated Fermi estimates, a good strategy is to break the
number into *subestimates* which are then multiplied together.
For instance, if I want to estimate the number of fish in the sea, I
might factorise it into the total number of fish species and the
number of fish per species:

$$
\text{total fish} \sim \text{species} \times \text{fish per
species}.
$$

This sort of factorisation is crying out to be expressed in terms of "generalised units":

$$
\frac{\text{fish}}{\text{world}} \sim
\frac{\text{species}}{\text{world}}\times \frac{\text{fish}}{\text{species}}.
$$

This not only lets us check that our estimate makes sense (units
cancel on the RHS to give the LHS) but can suggest further
factorisation.
The total number of fish species is hard to estimate, but maybe we
have a better feeling for how many species there are in a given *area*
of ocean:

$$
\frac{\text{species}}{\text{world}} \sim
\frac{\text{species}}{\text{area of ocean}}\times \frac{\text{area of ocean}}{\text{world}}.
$$

The total surface area of ocean is $350$ million km$^2$.
It seems reasonable to guess that there is a different species for
every 10 km$^2$ or so, and that a species of fish has on average
$10^5$ members.
This gives an estimate of

$$
\begin{align*}
\frac{\text{fish}}{\text{world}} & \sim
\frac{\text{species}}{\text{area of ocean}}\times \frac{\text{area of
ocean}}{\text{world}}\times \frac{\text{fish}}{\text{species}} \\ & \sim
\frac{1}{10 \text{ km}^2} \times (350 \times 10^6 \text{ km}^2) \times
10^5 \\ & = 3.5 \times 10^{12}.
\end{align*}
$$

Somewhat unexpectedly, this is exactly the number quoted in a
[non-peer-reviewed article](https://www.worldatlas.com/articles/how-many-fish-are-there-in-the-ocean.html). Huh!

*Full disclosure.* In case you're suspicious, here is where the
intermediate numbers come from.
First, you can calculate the total ocean surface from the radius of
the earth $r_\oplus = 6300$ km, the surface area of a sphere $4\pi
r^2$, and the factoid that $70\%$ of the earth is covered by water.
I have no idea if my remaining guesses are accurate.
I obtained the number of fish per species by lazily taking the mean of an obscenely successful species (humans, population
$\sim 10^{10}$) and a species on the brink of extinction ($\sim 1$).
Similarly, for the density, I just took the average of $1$ species per
$1 \text{ km}^2$ (seems too large) and $100 \text{ km}^2$ (seems too small).
I don't really trust my intuitions about areal biodiversity, but as
often happens with Fermi estimates, you land on your feet!

---

**Exercise 7 (churches in the US).** Guess the number of churches in
the US.

*Hint.* A particularly useful intermediate factor is *people*, both in
 this problem and in general.
 The US has a population of around $300$ million.

---

### 3.3. KISS<a id="sec-3-3" name="sec-3-3"></a>

*KISS* is the proverbial exhortation to "Keep It Simple, Stupid", and it
is especially true for Fermi estimates.
If you want fast, robust estimates, forget about finesse; just
focus on a *single important mechanism*.
You should make simplifying assumptions, ignore subtleties, and strip away
distractions to get at that mechanism.
Embrace the [spherical cow](https://en.wikipedia.org/wiki/Spherical_cow)!
Perhaps KISS should stand for "Keep It Spherical, Stupid".

Let's see how this works in practice.
Suppose we want to estimate the annual electricity usage in the greater
Vancouver area.
(This is an actual question from my
PhD [comprehensive exam](https://www.phas.ubc.ca/sites/phas/files/comp_aug2018.pdf).)
We could consider all sorts of separate contributions,
e.g. households, small businesses, heavy industry, agriculture,
transport, and so on, all
of which would involve different estimation strategies.
Instead, let's focus on a single, simple estimate: *household* power
usage.
This will make up some fixed fraction of the whole, perhaps $10\%$ or
so, so we just multiply by $10$ at the end of the day.

We start by writing some subestimates, factorising our guess using
*people* (rather than households) as an intermediate unit:

$$
\frac{\text{power}}{\text{Vancouver}} \sim
\frac{\text{power}}{\text{person}}\times \frac{\text{person}}{\text{Vancouver}}.
$$

The factor "person/Vancouver" is just the population of greater
Vancouver, which I happen to know is around $2.5$ million.
To estimate individual power usage, we can compare to something
familiar like a good ol' $60$ W globe.
I would guess that with light, heat, household appliances, and
electronic devices, an individual would use the equivalent of $10$
light bulbs on average, or around $600$ W.
Thus,

$$
\frac{\text{power}}{\text{Vancouver}} \sim 600 \text{W} \times (2.5
\times 10^6) = 1.5 \text{ GW}.
$$

To find the total electricity usage, we multiply by the length of a
year, and add an additional factor of $10$ to account for
non-household use.
In gigawatt hours (GWh), this gives a total energy of

$$
\begin{align*}
\text{yearly energy use} & \sim 10 \times (365 \times 24 \text{ h})
\times (1.5 \text{ GW}) \approx 1.3 \times 10^5 \text{ GWh}.
\end{align*}
$$

How did we do?
Our guess translates to around $500$ PJ (petajoules) per year, and according to
[this report](https://pics.uvic.ca/sites/default/files/uploads/publications/Energy_Data_Report_2010_1.pdf),
British Columbia uses $850--1000$ PJ.
Since greater Vancouver has about half the population of the province,
we should be spot on!

---

**Exercise 8 (Canadian budget).** Guess the Canadian government's
  federal budget for 2019.

---

### 3.4. Usage notes<a id="sec-3-4" name="sec-3-4"></a>

*Why it works.* So far, I've described what I think are the key methods for doing
Fermi estimates.
But it's a subtle art, and just like dimensional analysis, there is
quite a bit going on under the hood to ensure it works.
First of all, somewhat counterintuitively, *more subestimates is
better* because our under- and overestimates will tend to balance each
other out.
This is also the reason we use geometric means.
If the true value is $x$, and $a$ underestimates by a
factor $c$, while $b$ overestimates by a factor $c$, then $\sqrt{ab} =
\sqrt{x^2} = x$ is the true value.

This is an example of the
[wisdom of the crowd](https://en.wikipedia.org/wiki/Wisdom_of_the_crowd), where
averaging over different types of ignorance yields wisdom.
In this case, the crowd is made up of subestimates.
But just as a single charismatic fool can bias a crowd, a foolish
subestimate can scuttle your approximation.
The best way to avoid foolish subestimates is to *sanity check* them.
Compare to things you know, or manipulate your guess until you can
make that comparison.
For instance, perhaps we guess the Canadian budget is CAD`$`30
billion.
But if we also know the population (30 million or so) we see this
corresponds to `$`1000 per person.
Since the government typically spends thousands of dollars per student
on public education (let alone everything else!) this number is too low.

*Web of facts.* Aliens cannot perform this sanity check because they don't know
enough about our world.
In general, to be a good estimator, you need a web of facts, figures,
and intuitions to triangulate your position in estimate space.
Books on Fermi problems,
e.g. [*Guesstimation*](https://www.amazon.ca/Guesstimation-Solving-Worlds-Problems-Cocktail/dp/0691129495)
by Weinstein and Adam, have a list of handy numbers in the appendix
for just this reason.
It may feel like cheating, but if you are doing a Fermi
problem in real life, also remember that you can make your web of facts
dramatically larger using Google!

*Nonlinearity.* Another failure mode is "nonlinearity".
(I first saw this highlighted in lukeprog's
[great introduction](https://www.lesswrong.com/posts/PsEppdvgRisz5xAHG/fermi-estimates)
to Fermi estimates.)
Our method of factorising assumes that subestimates
are (a) independent and (b) multiply to give the final answer.
Assumption (a) can easily fail.
For instance, in our electricity calculation, we assumed that average
power usage was independent of population.
But average power usage tends to be
[lower](https://www.eia.gov/consumption/residential/)
in urban areas because the energy infrastructure is all in one place.
Thus, changing one factor (population of a city) will change another
(per capita power usage).
Sometimes you can take this dependence into account with extra
factors, sometimes you can't.

Assumption (b) fails when the final answer has a different type of
functional dependence on its subestimates.
A particularly severe example is *exponential* dependence.
Suppose I throw a fistful of quarters onto the ground.
What's the probability they all come up heads?
Well, if there are $n$ quarters, and each has a $50\%$ chance of
coming up heads, the answer is $(1/2)^n = 2^{-n}$.
It seems like all I need to do is count the quarters in a fistful.
But here's the rub: if I'm wrong by three quarters, l'll be off by a
factor of $8 \approx 10$, a whole order of magnitude!
If you want a well-defined order of magnitude estimate, back away
slowly from exponentials.

---

**Exercise 9 (people power).** Earlier, I guessed (based on a hunch)
  that individuals use around $600$ W (or $10$ light bulbs) on
  average. Let's check this a few different ways.

(a) Ask some friends to guess individual power usage, and
take the geometric mean of their answers.

(b) Next, sanity check my guess or the answer you got in (a).

(c) Finally, ask Google. How did I do?
How did your friends do?

<p align="center">
  ⁂
</p>

**Exercise 10 (fistful of quarters).** (a) How many quarters in a
fistful?
(b) Given that $n$ can vary by a factor of $3$, how does
  the estimate of the "all heads" probability vary?

---

## 4. Scaling<a id="sec-4" name="sec-4"></a>

Both dimensional analysis and Fermi approximation assume the answer
to a question can be written as a *product of powers* of some
other factors:

$$
\text{answer} \sim (\text{factor 1})^a \times (\text{factor 1})^b
\times \cdots.
$$

Instead of trying to completely factorise the answer, we can zoom in
on a single factor, leading to a proportionality relation:

$$
\text{answer} \propto \text{factor}^p.
$$

The symbol $\propto$ means we are ignoring all the other
factors and not just dimensionless numbers.
Sometime, we can nail down a proportionality relation, and in
particular the *scaling exponent* $p$, without considering any other
factors.
Let's illustrate with an example.

*Square-cube law.* Tissue density is roughly the same for different
 species (up to the usual order of magnitude numbers).
If an organism has length around $\mathcal{L}$, then the mass of the organism
should scale as

$$
M \propto \mathcal{L}^3.
$$

The surface area, on the other hand, should scale as $\mathcal{L}^2$.
(In both cases, we are assuming the organism has a simple shape.)
The fact that these things scale differently is called the
*square-cube law*, and was first observed by Galileo.
It may seem trivial, but it has important biological consequences!
Let's do the most famous example.

Galileo realised that materials like bone and wood will break when subject to
too much pressure.
This maximum pressure $P_\text{max}$ does not scale with $\mathcal{L}$, but depends only on the
material.
Since mass goes as $\mathcal{L}^3$, the weight force also goes as $\mathcal{L}^3$.
On the other hand, the cross-section of a weight-bearing element (like
legs or a tree trunk) goes as $\mathcal{L}^2$.
It follows that the pressure will scale with

$$
P = \frac{F}{A} \propto \frac{\mathcal{L}^3}{\mathcal{L}^2} = \mathcal{L}.
$$

An organism cannot get too large without exceeding this maximum
pressure.
Thus, there is no need to worry about giant ants from outer space: they will
collapse under their own weight as soon as they try to invade earth!

---

**Exercise 11 (walking speed).** (a)
Argue that walking speed scales as $\mathcal{L}^{1/2}$. *Hint.* Model the leg as a <a href="#sec-2-1">pendulum</a>.

(b) Average human walking speed is $\sim 1.4$ m/s.
	Estimate the walking speed of a horse and a garden spider.

<p align="center">
  ⁂
	  </p>

**Exercise 12 (thickness).** (a) Argue that the *radius*
    $r$ of a weight-bearing element should scale as $r \propto
    M^{1/2}$ in order to support the organism's weight.

(b) General Sherman is a giant sequoia tree in California's
    Sequoia National Park.
    The diameter of the trunk is $7.7 \text{ m}$.
    Estimate its mass by comparing to the thickness of the human
    thighbone ($r = 2.3$ cm) and using the radius scaling.

---

### 4.1. Random walks <a id="sec-4-1" name="sec-4-1"></a>

One of the most beautiful scaling laws is associated
with *random walks*.
Imagine an atom jiggling around randomly in a hot gas.
On average, it will travel some distance $\ell$ between collisions.
Surprisingly, after $n$ collisions, the approximate distance $d$ from
where it started is proportional to the *square root* of the number of steps:

$$
d \sim \ell \sqrt{n}.
$$

The basic logic is that

$$
\begin{align*}
d^2 & \sim (s_1 + s_2 + \cdots + s_n)^2 \\
& = (s_1^2 + s_2^2 + \cdots +
s_n^2) + \text{correlations between steps},
\end{align*}
$$

where $d^2$ is the average distance squared, and the $s_i$ are
individual steps.
If the steps are uncorrelated, and average step size is $\ell$, then
the second set of terms vanishes and the first set gives $d^2 \sim
n\ell^2$, since each $s_i^2 = \ell^2$.
Taking square roots, $d \sim \ell\sqrt{n}$ as claimed.
(For the mathematically inclined, the details of the proof are spelt
out in the <a href="#app-1">appendix</a>.)

If a random walker moves with speed $v$, a step takes time
$\tau = \ell/v$, so after time $t$ the walker tends to wander a
distance

$$
d \sim \ell \sqrt{n} = \ell \sqrt{\frac{t}{\tau}} \sqrt{t} =
\sqrt{\frac{\ell}{v}}\cdot \sqrt{t}.
$$

Even though the walker moves at constant velocity, distance travelled scales as $d \propto \sqrt{t}$!
It's also important to note that "average distance" is a bit of a
misnomer.
We really mean the *average spread* of distance travelled.
In time $t$, an individual
walker will explore a region of size $\propto \sqrt{t}$, while a
batch of walkers released from the same point will fan out to cover
that region.
For example, a drop of dye in water initially spreads quickly and then slows,
with its size obeying a $\sqrt{t}$ scaling.

*E. coli genome.* We start with a famous biological application of
random walks.
It turns out that when a cell nucleus ruptures, the tightly coiled DNA
will spill out in a random fashion.
The DNA can be modelled as a chain of approximately straight chunks of
length $\ell = 48$ nm, each of which corresponds to about 140 base
pairs.
After the rupture, these chunks remain connected, but are
more or less uncorrelated, forming the steps of a random walk.

In the photo above, a single-celled *Escherichia coli* (E. coli) bacterium has
ruptured.
From the spill, we can estimate the length of the E. coli
genome!
The DNA covers a region with radius

$$
d \approx 5 \,\mu\text{m} = 5000 \text{ nm}.
$$

Then, using the chunk length $\ell = 48$ nm, we guess that the
number of chunks is

$$
n \sim \frac{d^2}{\ell^2} \approx \left(\frac{5000}{48}\right)^2
\approx 1.1 \times 10^5.
$$

Multiplying by the number of base pairs per chunk, we guess a genome length

$$
L_\text{gen} \sim n \times (140 \text{ bp}) \approx 1.5 \times 10^6
\text{ bp},
$$

or $1.6$ Mbp.
A careful count gives $4.6$ Mbp, but we are within an order
of magnitude!

*Collision cylinders.* In the example above, we've adopted a
"collection of walkers" perspective.
We now focus on individual walkers with random motion due to collisions.
We can figure out the step length $\ell$ in terms of the size and
density of colliding particles.
The idea is very simple.
Suppose our particles are spherical, with radius $r$.
We assume the number of particles per unit volume is $n$, or
equivalently, there is on average one particle in a volume $U = 1/n$.
If another particle of the same size comes within $2r$ of the first,
the particles will collide, since the edges just touch at that
distance.

So, as a particle moves, sweep out a *collision cylinder* of radius $2r$ around
it.
For a distance $\ell$, the volume of this cylinder is $V = \pi(2r)^2
\ell$.
To guess the average distance $\ell$ between collisions, we assume
that when the cylinder volume $V$ is large enough to contain one
particle on average, a collision will occur.
Since $U = 1/n$ is the volume per particle, we find that

$$
V = 4\pi r^2 \ell = U = \frac{1}{n} \quad \Longrightarrow \quad \ell =
\frac{1}{4\pi r^2 n}.
$$

If the particles move at speed $v$, the mean time between collisions
is $\tau = v/(4\pi r^2 n)$.

---

**Exercise 14 (mid-air collision).** (a) Show that that ideal gas law
(Exercise 3)
implies that the number density of an ideal gas is

$$
n = \frac{\mathcal{N}}{V} = \frac{P}{k_B\mathcal{T}},
$$

where $P$ is the pressure, $k_B$ Boltzmann's constant, and
$\mathcal{T}$ the temperature (in Kelvin).

(b) The average air molecule has size $r = 4 \times 10^{-10} \text{ m}$.
Using this data, estimate the density of air molecules around you
right now.

(c) Using the collision cylinder method, find the average distance
between collisions of air molecules.

---

## 5. Conclusion<a id="sec-5" name="sec-5"></a>

It's mysterious to me that these techniques are not usually taught
in either high school or first year physics.
Lack of mathematical background is not the problem.

#### References

Finally, I recommend Sanjoy Mahajan's book
[*Street-Fighting Mathematics*](http://streetfightingmath.com/),
covering similar ground in greater depth.

http://ruina.tam.cornell.edu/research/topics/locomotion_and_robotics/simplest_walking/simplest_walking.pdf

https://www.quora.com/Theoretically-how-tall-or-large-can-a-land-animal-evolve-What-would-happen-if-an-animal-exceeded-this-size

## Appendix: random walks<a id="app-1" name="app-1"></a>

We will prove the square root scaling of random walks, first in 1D, and then extend
almost immediately to many dimensions.
The only prerequisite is a little probability theory and knowledge of vectors.

*Proof (1D).* Suppose we toss a coin, and move a counter
left or right one unit depending on whether we gets heads or tails.
Label the outcome of the $n$th toss $X_n$, where $X_n = -1$ for heads
and $X_n = +1$ for tails.
If we start at $0$, the position $X$ after $n$ tosses is the sum of steps:

$$
R = X_1 + X_2 + \cdots + X_n.
$$

This is a random process, so what do we expect to happen on average?
We can calculate this with an *expectation*: a weighted average over all the things
that can happen, where the weights are probabilities.
We denote this by $\langle f(X_1, \ldots, X_n)\rangle$, where $f$ is
any function of the steps.
For instance, if the coin is fair, then on average an individual step
is zero:

$$
\langle X\rangle = P(X=-1)(-1) + P(X=+1)(+1) = \frac{1}{2}-\frac{1}{2}
= 0.
$$

A very similar calculation shows that $R$ vanishes on average:

$$
\begin{align*}
\langle R\rangle &= \langle X_1 + \cdots + X_n\rangle\\
& = \langle X_1\rangle + \cdots + \langle X_n\rangle\\
& = 0 + \cdots + 0 = 0,
\end{align*}
$$

where we used the fact that expectation is *linear*, $\langle f +
g\rangle = \langle f\rangle + \langle g\rangle$ (Exercise A.1).
This makes sense, since if the coin is unbiased, it has no preference
between heads and tails.
If $\langle R\rangle >0$, for instance, then the coin is exhibiting a
bias towards tails.
The story is different for the *square* of a step:

$$
\langle X^2\rangle = P(X=-1)(-1)^2 + P(X=+1)(+1)^2 =
\frac{1}{2}+\frac{1}{2} = 1.
$$

What about a product of different coin flips?
Each possible outcome --, -+, +-, ++ has chance $1/4$, and hence

$$
\langle X_i \cdot X_j\rangle =
\frac{1}{4}\left[(-1)^2 + (-1)(+1) + (+1)(-1) + (+1)^2\right] = 0.
$$

Combining these two facts, we can calculate the *variance*:

$$
\begin{align*}
\langle R^2\rangle & = \langle (X_1 + \cdots + X_n)^2\rangle \\
& = \langle X_1^2\rangle + \cdots + \langle X_n^2\rangle +
2\left\{\langle X_1\cdot X_2\rangle + \cdots + \langle X_{n-1}\cdot
X_n\rangle\right\} \\
& = n \langle X^2\rangle = n.
\end{align*}
$$

The counter moves back and forth, and on average $\langle R\rangle =
0$.
But the size of the region explored as it moves back and forth is the
square root of the variance, also called the *root mean square* (rms)
displacement, $\sqrt{\langle R^2\rangle} = \sqrt{n}$.
This is the distance from the origin the counter will tend to wander
in the first $n$ steps.
If instead of steps $\pm 1$, we have steps $\pm s$, then $\langle
X^2\rangle = s^2$ and the rms displacement becomes

$$
\sqrt{\langle R^2\rangle} = s\sqrt{n}
$$

as claimed above.

*Proof (many D).* The proof is almost identical in $d$ dimensions,
 where a step can be written as a vector $\vec{X}$ with $d$ components:

$$
\vec{X} = (X^1, X^2\, \ldots, X^d).
$$

The length of $\vec{X}$ is given by a generalisation of Pythagoras'
theorem (Exercise A.2):

$$
|\vec{X}| = \sqrt{(X^1)^2 + (X^2)^2 + \cdots + (X^d)^2}.
$$

Let's assume that the average step length is $s$, and steps are
unbiased, so

$$
\langle \vec{X} \rangle = \vec{0} = (0, 0, \ldots, 0), \quad \langle |\vec{X}|^2 \rangle = s^2.
$$

Finally, we assume that steps are independent, so any two components of
distinct steps satisfy

$$
\langle X_i^a \cdot X^b_j \rangle = 0,
$$

where $\vec{X}_i, \vec{X}_j$ are distinct steps, and $a, b$ labels
components.
Then, if $\vec{R} = \vec{X}_1 + \cdots + \vec{X}_n$, the random walk has variance

$$
\begin{align*}
\langle |\vec{R}|^2\rangle & = \langle (X_1^1 + X_2^1 + \cdots
X_n^1)^2 + \cdots + (X_1^n + X_2^n + \cdots X_n^n)^2 \rangle \\
	& = \langle [(X_1^1)^2 + (X_2^1)^2 + \cdots
(X_n^1)^2] + \cdots +  [(X_1^n)^2 + (X_2^n)^2 + \cdots +(X_n^n)^2]
\rangle \\
& \qquad \qquad + 2 \langle
[X_1^1 \cdot X_2^1 + \cdots + X_{n-1}^1\cdot X_n^1]+\cdots + [X_1^n \cdot X_2^n + \cdots + X_{n-1}^n\cdot X_n^n] \rangle\\
& = \langle [(X_1^1)^2 + (X_1^2)^2 + \cdots
(X_1^n)^2] + \cdots +  [(X_n^1)^2 + (X_n^2)^2 + \cdots +(X_n^n)^2]
\rangle \\
& = \langle [(X_1^1)^2 + (X_1^2)^2 + \cdots
(X_1^n)^2] + \cdots +  [(X_n^1)^2 + (X_n^2)^2 + \cdots +(X_n^n)^2]\\
& = \langle |\vec{X}_1|^2\rangle + \cdots +\langle
|\vec{X}_n|^2\rangle\\
& = n s^2,
\end{align*}
$$

where on the third line we used the fact that the components of
different steps are independent, on the fourth line we reorganised the
terms $(X_i^a)^2$ into individual steps, on the fifth line we used the
definition of length and the linearity of expectation, and on the
last line we used the assumption about average step length.
Taking square roots, we find the rms displacement

$$
\sqrt{\langle |\vec{R}|^2\rangle} = s\sqrt{n},
$$

in any number of dimensions.
Notice also that we do not need the steps to be the same length, or
live on a lattice.

---

**Exercise A.1 (expectation).** Show that, if $f(X)$ and $g(X)$ are
functions of a random variable $X$, then

$$
\langle f(X) + g(X)\rangle = \langle f(X)\rangle + \langle g(X)\rangle.
$$

<p align="center">
  ⁂
	  </p>

**Exercise A.2 (length in higher dimensions).** Consider a vector
$\vec{C} = (C^1, \ldots, C^d)$ in $d$ dimensions.

(a) We can write the vector as a sum

$$
\vec{C} = (C^1, \ldots, C^{d-1}, 0) + (0, \ldots, 0, C^d) = \vec{A}+\vec{B}.
$$

Argue that these two summands are at right angles, and use Pythagoras'
theorem (in the plane spanned by $\vec{A}$ and $\vec{B}$) to argue
that

$$
|\vec{C}|^2 = |\vec{A}|^2 + |\vec{B}|^2 = |\vec{A}|^2 + (C^d)^2.
$$

(b) Now iteratively repeat this argument for $\vec{A}$, and deduce
that, as we claimed above, length squared in $d$ dimensions is

$$
|\vec{C}|^2 = (C^1)^2 + \cdots + (C^d)^2.
$$

---

## Extra

*Physics is often presented as the most arcane
  and mathematically challenging of natural sciences. But simple physical
  ideas, combined with pre-calculus mathematics, can be
  mind-bogglingly powerful. I give several examples.*

   5. <a href="#sec-2-5">Binomial approximation</a>
   6. <a href="#sec-2-6">Stefan-Boltzmann law</a>
   7. <a href="#sec-2-7">Randomness and entropy</a>
   8. <a href="#sec-2-8">Quantisation</a>
   9. <a href="#sec-2-9">Relativity</a>

##### 2.5. Binomial approximation <a id="sec-2-5" name="sec-2-5"></a>

##### 2.6. Stefan-Boltzmann law <a id="sec-2-6" name="sec-2-6"></a>

##### 2.7. Randomness and entropy <a id="sec-2-7" name="sec-2-7"></a>

##### 2.8. Quantisation <a id="sec-2-8" name="sec-2-8"></a>

##### 2.9. Relativity <a id="sec-2-9" name="sec-2-9"></a>

fractals, quantisation, entropy


Our best theories of nature seem to involve hard mathematics.
We have electromagnetism, formulated in the language of vector
\[
\begin{align*}
\nabla \cdot \mathbf{E} & = \frac{1}{\epsilon}\rho \\
\nabla \cdot \mathbf{B} & = 0 \\
\nabla \times \mathbf{E} & = -\mu\dot{\mathbf{B}} \\
\nabla \times \mathbf{B} & = \mu\mathbf{J} + \epsilon\dot{\mathbf{E}}
\end{align*}
\]
to Schrödinger
\[
i\frac{\partial}{\partial t}|\psi\rangle = \left(-\frac{\hbar^2}{2m}\nabla^2 + \hat{V}\right)|\psi\rangle
\]
to Einstein
\[
R_{\mu\nu} - \frac{1}{2}\Lambda R g_{\mu\nu} = 8 \pi G T_{\mu\nu},
\]
physics seems at its most powerful and exotic when expressed in
mathematical language.
The more opaque, the more powerful and exotic it seems.

**January 6, 2020.** *Physics is often presented as arcane and
  mathematically challenging. In this post, I try to counter this
  notion by showing that simple physical ideas, combined with
  pre-calculus mathematics, can be mind-bogglingly powerful.*

Physics is embedded in mathematics.
Our best theories of nature seem to require it, and are often stated in the
pithy but impenetrable form of *equations*.
For instance, we can summarise gravity with *Einstein's field equations*:
\[
R_{\mu\nu} -\frac{1}{2}R g_{\mu\nu} = 8\pi G T_{\mu\nu}.
\]
This is a startingly beautiful result, but requires years of training
to appreciate mathematically.


https://web.archive.org/web/20160129142844/http://www.eftaylor.com/exploringblackholes/GravWaves150909v1.pdf

Suppose you want to build a pendulum-driven grandfather clock, with
the mass suspended on a light rod $\ell = 1.5$ metres long.
Approximately how heavy should the pendulum itself be if you want it
to swing back and forth with a period of $t = 1$ second?
We can answer this with dimensional analysis.
We first identify a *target* quantity: the thing we are trying to
control, predict or measure.
In this case, it is the *mass* of the pendulum $m$, which has the
dimension $M$:

$$
[m] = M.
$$

We then list the *relevant parameters* which physically determine our
target quantity.
In this case, they are the period of the pendulum $t$, the length of the
rod $\ell$, and the strength of gravity $g = 9.8 \text{ m/s}^2$, without
which the pendulum will not oscillate!
From the units, this has dimension

$$
[g] = [9.8 \text{ m/s}^2] = \frac{[\text{m}]}{[\text{s}^2]} = \frac{L}{T^2}.
$$

In summary, the relevant parameters and dimensions are:
- period, $[t] = T$;
- length, $[\ell] = L$;
- gravitational acceleration, $[g] = L/T^2$.
We now guess that the target quantity is some *product of powers* of
the relevant parameters,

$$
m = t^a \ell^b g^c,
$$

and by analysing the dimensions on both sides, figure out
what those powers are.
On the LHS, we have dimension $m$.
On the RHS, we have dimensions

$$
\begin{align*}
[t^a \ell^b g^c] & = T^a L^b \cdot \frac{L^c}{T^{2c}}  = \frac{T}{}
\end{align*}
$$

#### 2.2. Example: spring-mass system <a id="sec-2-2" name="sec-2-2"></a>

Suppose you want to build a spring-driven clock, with time marked off
by the oscillations of a mass stuck to the spring.
When the spring is compressed or extended, you measure the restoring
force $F$ and notice that it is proportional to the displacement $x$
from the spring's equilbrium position
([Hooke's law](https://en.wikipedia.org/wiki/Hooke%27s_law)):

$$
F = kx.
$$

This constant $k$ is called the *stiffness*, and it has dimensions

$$
[k] = \frac{[F]}{[x]} = \frac{[ma]}{[x]} = \frac{ML}{T^2L} = \frac{M}{T^2}.
$$

To make our clock, we want the mass to oscillate with a period of $t_\text{period} =
1$ second.
If you are familiar with harmonic motion, you know that a nicer
quantity than period is *angular frequency*:

$$
\omega =
\frac{2\pi}{t_\text{period}},
$$

with dimensions $1/T$.
To help design the clock, we want to know how the angular frequency $\omega$
depends on the stiffness $k$ of the spring and mass $m$.

The general procedure for dimensional analysis is as follows.
We first identify a *target* quantity: the thing we are trying to
control, predict or measure.
In this case, it is the angular frequency.
We then list the *relevant parameters* which our target quantity should
depend on.
In this case, these are the stiffness $k$ and mass $m$, with dimensions
- stiffness, $[k] = M/T^2$;
- mass $[m] = M$.

We now guess that the target quantity is a *product of powers* of
the relevant parameters, taking the form:

$$
\omega = k^a m^b.
$$

(I'll comment on how this assumption can break down in the usage notes.)
We can find the powers $a$ and $b$ from the requirement that the
dimensions on both sides are equal:

$$
\begin{align*}
[k^a m^b] &= \frac{M^a}{T^{2a}}\cdot M^b = \frac{M^{a+b}}{T^{2a}} \\
[\omega] &= \frac{1}{T}.
\end{align*}
$$

Since there are no factors of mass for the RHS, we have $b = -a$, and
hence $T^{2a} = T$, or $a = 1/2$.
Thus, dimensional analysis gives

$$
\omega \sim \sqrt{\frac{k}{m}},
$$

where $\sim$ indicates that some numbers may have gone astray.
In fact, our sneaky choice of angular frequency $\omega$ instead of
period $t_\text{period}$ means this is *exactly* correct, numbers and
all.
(If we stuck with period we would be off by a factor of $2\pi$, which
is not ideal if we want to design a precision timepiece.)
We didn't need to analyse any forces, solve a differential
equation, or even deal with numbers.
Dimensional analysis let us skip straight to the answer!

So, if your high school physics lab has springs of stiffness $k = 10^2 \text{
N/m}$ ($100$ Newtons for every meter displaced), then to obtain an
oscillation period of $ t_\text{period} =1$ second, you should attach
a mass

$$
m = \frac{k t_\text{period}^2}{4\pi^2} = \frac{10^2 \text{
kg}}{4\pi^2} \approx 2.5 \text{ kg}.
$$

MAKE MORE INTERESTING

---

1. Using dimensional analysis, show that the angular frequency does
   not depend on the initial displacement $x$ of the mass.

---

#### 2.3. Example: the wobbling pupm <a id="sec-2-3" name="sec-2-3"></a>

The spring-mass example is neat, but not particularly exciting.
We can make it more interesting by adding some quantum mechanics into
the mix.
The *fundamental constant* appearing in quantum mechanics is *Planck's
constant*, with SI value

$$
\hbar = 1.05 \times 10^{-34} \text{ J s}.
$$

(Technically, this is the "reduced" Planck constant favoured by
theoretical physicists. The original constant is $h = 2\pi \hbar$.)

Pushing an object through a fluid takes work, since as we plough
through we must push the fluid aside.
In realistic fluids, adjacent layers like to stick together, so they
resist the shearing; a phenomenon called *viscosity*.
This is measured by a number $\mu$, 

with the simplest being
to the *terminal velocity* of a sphere falling slowly through a fluid.
This may sound rather artificial, but it lets us explain why clouds
stay in the air, despite being made of droplets much denser than air.


The hacks are in no particular order except for the "fundamental hacks" of
dimensional analysis and Fermi estimates.
Everything else can be read independently.
For each hack, I quickly outline the physics, do some examples,
and finish with usage notes.

The mother of all Fermi estimates was is due to
[Enrico Fermi](https://en.wikipedia.org/wiki/Enrico_Fermi) himself,
who estimated the strength of the
[Trinity nuclear test](https://en.wikipedia.org/wiki/Trinity_(nuclear_test))
by dropping a few pieces of paper.
Fermi doesn't explain his precise reasoning, but
[states that](http://www.dannen.com/decision/fermi.html) he dropped
the paper from a height of around $6$ feet ($1.8$ m) and observed a
displacement of $2.5$ m as the blast wave passed.
Fermi was $16$ km away from the detonation point.

What is the key physical mechanism?
The paper moved because the air around it was displaced.


**Exercise 1 (spring-driven clock).**
You can build a clock out of a spring and an old pumpkin by attaching the
pumpkin to one end and fixing the other, compressing the spring, and
letting it wobble back and forth.
(If you do this horizontally, you can ignore gravity.)
When the spring is moved from equilibrium a distance $x$, there is a
[restoring force](https://en.wikipedia.org/wiki/Hooke%27s_law)
proportional to displacement, $F = kx$, where $k$ is the *stiffness*.
If the hardware store only stocks springs of stiffness $k = 100 \text{
N/m}$, and you want a period of $t = 2$ s, how heavy should your
pumpkin be?

We've already seen examples of KISS when performing dimensional
analysis.
When choosing a list of relevant parameters, for instance, we
neglected things that we did not expect , our answers are usually only
correct to within an order of magnitude because we cannot determine
the numbers out front.

If you are estimating "in real life" (rather than in a test) check
Google.

But if for whatever reason, act like a crowd, and try to intuit some over-
and underestimates you can average.


Here's a simple example.

When we write our guess as a product of subestimates, we are assuming
the final answer is *proportional* to each subestimate.
A very prosaic instance of nonlinearity is when we should use the usual
*arithmetic* mean, $(a+b)/2$.
For instance, with power, there may be economies of scale which
*reduce* the average power usage when there are more people.
Or maybe larger cities will have more amenities, and average power
usage will increase.
Who knows?
Whatever the answer, it is probably a fairly mild *power law*
nonlinearity.
We'll discuss power laws below, but I'll finish with the much more
severe example of *exponential* nonlinearity.

When we write our guess as a product of subestimates, we are assuming
the final answer is *proportional* to each subestimate, e.g. that the
power usage in Vancouver is proportional to the number of people.
But this may not be true!
For instance, with power usage, there may be economies of scale which
*reduce* the average power usage when there are more people.
Conversely, maybe larger cities have more amenities, and average power usage increases.
Examples like this usually obey
[*power laws*](https://en.wikipedia.org/wiki/Power_law), where

$$
\text{final guess} \propto (\text{factor})^\gamma,
$$

for some number $\gamma$.

With this sort of dependence, you can use Fermi estimate techniques to
make a guess, but the answer isn't really well-defined to an order of
magnitude.
Different fists will differ by more than two quarters!
(Our estimate of $n$ will probably be accurate up to an order of
magnitude, i.e. it could be around $3n$ or $n/3$.
So our estimate of the probability is likely to be good up to a cube
or cube root!
We could view this as ticks on a *doubly* logarithmic ruler, but it's
a bit mind-boggling.)

### 1. Introduction <a id="sec-1" name="sec-1"></a>

For the last year or so, I've been heavily involved in running a
[high school physics circle](https://outreach.phas.ubc.ca/events/metro-vancouver-physics-circle/).
I've learned a lot about logistics, leadership, and leaning
towers of pizza, but surprisingly, the biggest lesson has been about *physics itself*.
In a physics circle, the mandate is to write problems that high school
students find challenging but fair given their limited background
knowledge.
In particular, problems should avoid calculus, which is not part of
Canada's high school curriculum.
Judging from competition problems, this restricts us to
tediously intricate mechanics problems and a other elementary topics.

But preparing for my PhD
[comprehensive exam](https://www.phas.ubc.ca/graduate-program-comprehensive-exam-guidelines-phd-students),
I realised that it was possible to do more with less.

I decided to view this as a challenge: do more with less.
I am not above writing tediously intricate mechanics problems, but it
was much more instructive to master some simple physics hacks and use
them to discover new things.
I'm not sure about the students, but it has certainly made me a better
physicist!

The goal of this post is to share a few of these hacks and convince
you of their awesome power.
To keep things interesting, I avoid overlap with my
[physics circle problems](https://hapax.github.io/assets/circle-probs.pdf)
though I encourage you to have a look if you want more examples.
I also recommend Sanjoy Mahajan's book
[*Street-Fighting Mathematics*](http://streetfightingmath.com/), covering similar ground in greater depth.

**January 6, 2020.** *Physics is often presented as the most arcane and
  mathematical of natural sciences. Here, we show how
  simple physical ideas, with a dash of pre-calculus mathematics, can
  still be awesomely powerful.*

, and
we can actually use dimensional analysis to account for some factors of $\pi$
(see *Extra dimensions*).

We say that the answer *scales as* $\text{factor}^p$, or *with power* $p$.

Suppose we have some random process, like tossing a coin, whose
outcome we label by $X = \text{H, T}$ (heads and tails).
The *expectation* of a function $f(X)$, denoted $\langle f(X)\rangle$,
is the average over outcomes, weighted by their probability.
For a fair coin, this is just

$$
\langle f(X)\rangle = \frac{1}{2}[f(\text{H}) + f(\text{T})],
$$

but if the coin is biased, and heads has probability $p$, then

$$
\langle f(X)\rangle = pf(\text{H}) + (1-p)f(\text{T}).
$$

Suppose we toss two coins independently, labelling the first outcome
$X$ and the second $Y$.
"Independent" means that the probability of $X$ and $Y$ is always a product of the
single-coin probability of $X$, and the single-coin probability of
$Y$:

$$
P(X, Y) = P(X)P(Y).
$$

Remarkably, the result does not depend on the number of dimensions.
It is just as true for an atom jiggling in three dimensions, a drunkard wandering a
two-dimensional streetscape, or a virtual bacterium foraging in a
216-dimensional simulation.


For instance, if you drop dye into water, it will initially spread
quickly before slowing, since it consists of many random walkers (dye
molecules) obeying the $d \propto \sqrt{t}$ scaling.
