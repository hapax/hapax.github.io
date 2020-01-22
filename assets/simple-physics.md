---
Layout: post
mathjax: true
comments: true
title:  "Hacking physics from the back of a napkin"
categories: [Physics, Teaching, Hacks]
date:  2020-01-06
---

**January 21, 2020.** **

### Contents

1. <a href="#sec-1">Hacker spirit</a>
2. <a href="#sec-2">Dimensional analysis</a>
   1. <a href="#sec-2-1">Pendulous pumpkins</a>
   2. <a href="#sec-2-2">Drag and drop</a>
   3. <a href="#sec-2-3">Usage notes</a>
3. <a href="#sec-3">Fermi estimates</a>
   1. <a href="#sec-3-1">Geometric means</a>
   2. <a href="#sec-3-2">Subestimates</a>
   3. <a href="#sec-3-3">KISS</a>
   4. <a href="#sec-3-4">Usage notes</a>
4. <a href="#sec-4">Random walks</a>
   1. <a href="#sec-4-1">Polymers</a>
   2. <a href="#sec-4-2">Collisions</a>
   3. <a href="#sec-4-3">Brownian motion</a>
   4. <a href="#sec-4-4">Mathematical details</a>
5. <a href="#sec-5">Conclusion</a>

## 1. Hacking physics <a id="sec-1" name="sec-1"></a>

*Hacker culture.* Nowadays, the word "hacker" conjures up visions of dirtbag genius
teenagers, geopolitical intrigue, and Angelina Jolie sporting a pixie cut.
But a nobler usage predates this.
*Hacker culture*, in the original sense, grew out of places like MIT
in the 60s, with its tradition of highbrow silliness and elaborate technical pranks.
Although associated with programming, hacking spirit can be viewed as
a broader ethos about play, understanding and creativity.
In the words of open-source guru Richard Stallman,

<span style="padding-left: 20px; display:block">
What [hackers] had in common was a love of excellence and
programming. They wanted to make the programs that they used be as
good as they could. They also wanted to make them do neat things. They
wanted to be able to do something in a more exciting way than anyone
believed possible and show  "Look how wonderful this is. I bet you
didn't believe this could be done."
</span>

Using techniques in a clever or unexpected way is a *hack*, with *hack
value* quantifying the degree of ingenuity. (Interestingly, the first
term is a back-formation of the second.)
Hackers do not look for the most powerful, or obvious, or easy tool
for the job.
They delight in the unexpected, in using humble means to achieve
extraordinary ends.
In a way, they realise David Deutsch's
[definition](https://en.wikipedia.org/wiki/The_Beginning_of_Infinity)
of knowledge as
*information with causal power*.
Really understanding something --- enough to hack it --- means you can
not only *do better*, but *do more* with it.

I think physics needs more hacker spirit: more people willing to fool
around and explore what our marvellous toolset can do, to creatively
defy expectations and push the Deutschian envelope.
Physics is not withouts its hackers
([Richard Feynman](https://en.wikipedia.org/wiki/Richard_feynman),
[the folk Niels Bohr](https://en.wikipedia.org/wiki/Barometer_question),
even [Randall Munroe](https://what-if.xkcd.com/)) but unlike computer
science, the hackers tend to be colourful exceptions, tending towards
goofy irreverence or self-mythology.

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
It weighed $2.25$ tons (above water), had a diameter of $1.45$ m, and
held the world record for deepest dive (until 1949) at $923$ m.
Roghly how long did it take to reach that depth?
The viscosity of cold water is $\mu \approx 0.0016$ kg/m s.

*Hint.* Assume it is travelling at terminal velocity, and Stokes' law
applies. You should also take buoyancy forces into account!

(b) Keeping with our theme of whimsical rulers, explain how you can
use Stokes' law to determine the size of small iron spheres dropped in water.

---

### 2.3. Usage notes<a id="sec-2-3" name="sec-2-3"></a>

*Numbers.* Dimensional analysis has its limits.
First of all, it can be wrong by an overall numerical factor.
In the second example, for instance, we were off by $6\pi \approx 20$.
That said, more often than not the missing number is close to $1$, and
we can even account for some factors of $\pi$ by adding an extra
dimension for angles (Exercise 4).

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
There are further subtleties captured by a result called the
[Buckingham $\pi$ theorem](https://en.wikipedia.org/wiki/Buckingham_%CF%80_theorem).
See my [notes](https://hapax.github.io/assets/dimensional-analysis.pdf) or
*Street-Fighting Mathematics* for an elementary treatment.

*Extra dimensions.* Length, mass and time are not
the only basic dimensions.
Two other important dimensions are *temperature* $\Theta$ (measured in
Celsius or Kelvin for instance) and *amount
of stuff* $N$ (usually measured in mol).
These are crucial in atomic physics, thermodynamics and
chemistry, and you can see an application in Exercise 3.

*Constants.* Numbers are dimensionless constants.
However, *dimensionful* constants secretly encode important physical
insights.
Examples include Newton's constant $G$ (Exercise 1) and Boltzmann's
constant $k_B$ (Exercise 3).
See my [notes on dimensional analysis](https://hapax.github.io/assets/dimensional-analysis.pdf)
for more on the powerful role these constants play in dimensional analysis.

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
(Perhaps KISS should stand for "Keep It Spherical, Stupid".)

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

*Why it works.* Fermi approximation is a subtle art.
It seems like it works because over- and underestimates tend to
balance each other out.
This appears to be an example of the
[wisdom of the crowd](https://en.wikipedia.org/wiki/Wisdom_of_the_crowd),
where averaging over different types of ignorance yields wisdom.
In this case, the crowd is made up of subestimates!
But the *variance* (random variability) of subestimates adds up, and a
good rule of thumb is to only factorise into subestimates when the
combined uncertainty of these estimates is much smaller than the original.

*Sanity checks.*
You can increase the reliability of a subestimate by performing a sanity check.
Compare to things you know, or manipulate your guess until you can
make that comparison.
For instance, if we guess the Canadian budget is CAD`$`30
billion, and also know the population (30 million or so), we see this
corresponds to `$`1000 per person.
Since the government typically spends thousands of dollars per student
on public education (let alone everything else!) this number is too low.

*Web of facts.* Aliens cannot sanity check because they don't know
enough about our world.
In general, to be a good estimator, you need a web of facts, figures,
and intuitions to triangulate your position in estimate space and
reduce variance.
Books on Fermi problems,
e.g. [*Guesstimation*](https://www.amazon.ca/Guesstimation-Solving-Worlds-Problems-Cocktail/dp/0691129495)
by Weinstein and Adam, usually have a list of handy numbers in the appendix
for just this reason.
It may feel like cheating, but if you are doing a Fermi
problem in real life, also remember that you can make your web of facts
dramatically larger using Google!

*Nonlinearity.* Another failure mode is "nonlinearity".
(Props to lukeprog's
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

**Exercise 10 (jumping mugs).** (a) Estimate the number of atoms $n_C$ in a
cup of coffee.

(b) Very roughly, what is the probability the coffee jumps
spontaneously into the air?

*Hint.* Atoms move in random directions. The coffee will spontaneously
 jump if most of the atoms in the cup are moving up.

(c) If the cup cycles through a billion different random
configurations a second, and the universe lasts another $13$ billion
years, are we likely to see the cup spontaneously jump?

(d) Given that $n_C$ can vary by an order of magnitude, how does the
probability of spontaneous jumping vary? Does it change your
conclusion in (c)?

---

### 4. Random walks <a id="sec-4" name="sec-4"></a>

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

This $\sqrt{t}$ scaling is the defining feature of a *random walk*.
Remarkably, the scaling does not depend on the number of dimensions.
It is just as true for an atom jiggling in three dimensions, a drunkard wandering a
two-dimensional streetscape, or a virtual bacterium foraging in a
216-dimensional simulation.
The details of the proof are spelt
out in an <a href="#sec-4-3">optional section</a> below.

If a random walker moves with speed $v$, a step takes time
$\tau = \ell/v$, so after time $t$ the walker tends to wander a
distance

$$
d \sim \ell \sqrt{n} = \ell \sqrt{\frac{t}{\tau}} =
\sqrt{\ell v}\cdot \sqrt{t} = \sqrt{Dt},
$$

where we will call $D = \ell v$ the *diffusion coefficient*.
Even though the walker moves at constant velocity, the average distance
travelled scales as $d \propto \sqrt{t}$!
It's important to note that "average distance" is a bit of a
misnomer.
We really mean the *average spread* of distance travelled.
In time $t$, an individual
walker will explore a region of size $\propto \sqrt{t}$, while a
batch of walkers released from the same point will fan out to cover
that region.

---

**Exercise 11 (fractional random walks).** There is a generalisation
  of random walks called *fractional random walks*, where the average
  spread scales as

$$
d \propto t^{H},
$$

for some number $0 < H < 1$ called the *Hurst index*.
Random walks have $H = 1/2$.

(a) Explain why Hurst index $H > 1/2$ requires that steps be
*correlated*.

(b) What relation between steps does Hurst index $H < 1/2$ require?

---

### 4.1. Polymers <a id="sec-4-1" name="sec-4-1"></a>

Random walks not only apply to processes in time, but also in space.
The most important example is polymers: long, jointed chains of
molecules which can often be described by a random walk.
In this case, the step length $\ell$ is the *persistence length* of
the polymer, the distance the polymer remains approximately straight.
After a persistence length, the chain will forget which way it is
pointing and choose a new, uncorrelated direction.
We'll look at a famous biological application to the biggest, baddest,
most biologically indispensable polymer of them all: *DNA*.

Every cell in an organism contains a copy of its building instructions
in DNA form.
Most organisms are *eukaryotes*, meaning every cell has a nucleus for
storing the DNA, but in *prokaryotes* (such as bacteria), the DNA just
floats around in the cell.
Either way, If the container ruptures, the tightly coiled DNA will
spill out and form a random walk of approximately straight chunks.
The persistence length is $\ell = 48$ nm, which corresponds to about
140 base pairs (bp).
(A base pair is just one of the dumbbell components of the double helix.)

In the photo above, the nucleus of a single-celled *Escherichia coli*
(E. coli) bacterium has ruptured.
From the spill, we can estimate the length of its genome!
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

---

**Exercise 11 (deep thinking).** Wandering the shipyards one day, you
notice a rusty old anchor, probably from a decommissioned fishing vessel.
The mooring chain is haphazardly piled on the dock.

(a) The links are around $7$ inches in length, and the piles is $4.7$
m across.
What is the approximate length of the mooring chain?

(b) For vessels in shallow water, a good rule of thumb is that the
mooring chain is $1.5$ times the depth of the water.
How deep was the water this vessel fished in?

---

### 4.2. Collisions <a id="sec-4-2" name="sec-4-2"></a>

Our first goal is to determine the step length $\ell$.
If a fluid particle comes within a distance $r$ of the pollen, a
collision will happen, so to help us keep track of possible collisions
we draw a *collision cylinder* of cross-section $\sigma = \pi r^2$
around the grain as it moves.
On average, there is a single fluid particle in each volume
$U = V/\mathcal{N}$ of fluid
We can determine $\ell$ by assuming that when the collision cylinder
has length $\ell$, it has volume $U$, and hence on average contains a
fluid particle.
This leads to

$$
\sigma \ell = \frac{V}{\mathcal{N}} \quad \Longrightarrow \quad \ell =
\frac{V}{\pi r^2 \mathcal{N}}.
$$

---

**Exercise 13 (mirrorball madness).** An eccentric billionaire decides
to have a disco in space.
The dance floor lies at the centre of a huge glass sphere, with a
"gas" of $\mathcal{N}$ mirrorballs floating around it.
The mirrorballs are illuminated by laser light shot out from pointers
on the dance floor.
The giant glass sphere has radius $R$, while the $\mathcal{N}$ mirror balls have
radius $r$.
Let's follow the trajectory of a single photon.

(a) Argue that the collision cylinder around the photon has radius
$r$.

(b) Compute the approximate time it will take the photon to escape the
giant disco ball.
You should find

$$
t_\text{esc} \sim \frac{3r^2 \mathcal{N}}{4 Rc},
$$

where $c$ is the speed of light.

<p align="center">
  ⁂
</p>

**Exercise 14 (more collisions).** Two spheres of radius $r$
  collide when their centres come within $2r$ of each other, since the
  edges touch.
  To find the average distance between colliding particles of the *same*
  size, we should draw our collision cylinder with cross-section $\sigma = \pi(2r)^2$.

(a) The average air molecule has size $r = 4 \times 10^{-10} \text{ m}$.
Use this to estimate the average distance between collisions of air
molecules in the room around you, $\ell = U/\sigma$.

*Hint.* The ideal gas law lets you rewrite $U = V/\mathcal{N}$ in terms
of temperature and pressure.
Atmospheric pressure is $101$ kPa.

(b) A group of $100$ drunkards crowds into a beer garden of radius $5$
	m.
	A single drunkard decides to leave, moving in a straight line
	until they hit another drunkard, at which point they mumble an apology
	and randomly change direction.
	Roughly how long will it take them to escape,
	and how many apologies will they issue?

*Hint.* Use a *collision rectangle* of width $d$, where
 $d$ is the diameter of a drunkard.

---

### 4.3. Brownian motion <a id="sec-4-3" name="sec-4-3"></a>

Before the 20th century, the notion that matter was
made of tiny, indivisible lumps was regarded with skepticism.
But in 1905, long before we could see atoms with microscopes, a Swiss
patent clerk came up with a brilliant indirect method for proving their
existence.
The clerk was none other than Albert Einstein, and his proof uses
random walks.
Let's see how he did it!

We start by pouring a viscous fluid into a tall container of volume
$V$.
The fluid is made up of $\mathcal{N}$ particles at temperature
$\mathcal{T}$, and we assume it is dilute enough to be described by
the ideal gas law (Exercise 3).
Now plonk some larger, visible particles into this fluid, say some
pollen grains of radius $r$ and mass $m$.
The pollen grains will randomly collide with particles in the fluid,
executing a random walk as they do so.
Assuming the grain is much larger than the fluid particles, we can
treat them as points, so the collision cylinder has cross-section
$\sigma = \pi r^2$.

Counting the number of particles is hard, but measuring the
temperature is easy.
So we use the ideal gas law to swap volume and number for
pressure and temperature:

$$
PV = \mathcal{N} k_B\mathcal{T} \quad \Longrightarrow \quad
\ell = \frac{k_B\mathcal{T}}{\pi P r^2}.
$$

Since the container is tall, the pressure profile $P$ can change with
height.
But if we leave the pollen grains alone for long enough, they will
fall down and settle into *dynamic equilibrium* at the point where the
pressure from the fluid balances the force of gravity.
(We want the pollen grains to be light enough that this isn't the
bottom of the container!)
In other words, we have

$$
P = \frac{F}{A} = \frac{mg}{\pi r^2},
$$

and hence

$$
\ell = \frac{k_B\mathcal{T}}{mg}.
$$

From observing the pollen grains, we can directly see the diffusion
coefficient $D = \ell v$, since $d^2 \sim Dt$.
We still need to work out the velocity, $v$, and here is the clever
part: since our fluid was viscous, and assuming the grains move
slowly, we can apply <a href="#sec-2-2">Stokes' law</a>!
If the grains are in equilibrium, it's reasonable to guess that their
velocity is the terminal velocity we calculated earlier:

$$
v_{\text{term}} = \frac{mg}{6\pi \mu r},
$$

where $\mu$ is the viscosity of the fluid.
Putting it all together, we predict a diffusion coefficient

$$
D \sim \ell v_{\text{term}} = \frac{k_B\mathcal{T}}{6\pi \mu r}.
$$

This is the *Einstein-Smoluchowski-Sutherland (ESS) relation*, after the
three physicists who independently discovered it.
The weight of the pollen cancels out, leaving a diffusion constant
which grows with temperature but is inversely proportional to particle
size.
Big particles jiggle less, hot fluids jiggle more, and things look the
same on Mars!

The jiggling of grains in a fluid was first observed by Robert Brown,
hence the name *Brownian motion*.
(It should perhaps be called *Lucretian motion*, since Lucretius
observed the zigzag motion of dust particles and attributed it to
atoms --- in 60 BC!)
Although Brownian motion is best explained by atoms, Einstein's
genius was to extract specific and testable predictions, confirmed
experimentally in 1908 by Jean Perrin.

---

**Exercise 12 (randomness is slow).** Estimate how long it takes a
drop of dye to spread throughout a cup of water by Brownian motion.
  Dye particles have size $\sim 1\, \mu$m, and water at room
  temperature has viscosity $\eta = 10^{-3}$ kg/m s.
	You should find it is a rather long time!

<p align="center">
  ⁂
</p>

---

### 4.4. Mathematical details (optional) <a id="sec-4-4" name="sec-4-4"></a>

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
If instead of steps $\pm 1$, we have steps $\pm \ell$, then $\langle
X^2\rangle = \ell^2$ and the rms displacement becomes

$$
\sqrt{\langle R^2\rangle} = \ell\sqrt{n}
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

Let's assume that the average step length is $ \ell $, and steps are
unbiased, so

$$
\langle \vec{X} \rangle = \vec{0} = (0, 0, \ldots, 0), \quad \langle |\vec{X}|^2 \rangle = \ell^2.
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
& = n \ell^2,
\end{align*}
$$

where on the third line we used the fact that the components of
different steps are independent, on the fourth line we reorganised the
terms $(X_i^a)^2$ into individual steps, on the fifth line we used the
definition of length and the linearity of expectation, and on the
last line we used the assumption about average step length.
Taking square roots, we find the rms displacement

$$
\sqrt{\langle |\vec{R}|^2\rangle} = \ell\sqrt{n},
$$

in any number of dimensions.
Notice also that we do not need to assume the steps are the same
length or live on lattice.

---

**Exercise 15 (expectation).** Show that, if $f(X)$ and $g(X)$ are
functions of a random variable $X$, then

$$
\langle f(X) + g(X)\rangle = \langle f(X)\rangle + \langle g(X)\rangle.
$$

<p align="center">
  ⁂
	  </p>

**Exercise 16 (length in higher dimensions).** Consider a vector
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

#### References

https://en.wikipedia.org/wiki/Barometer_question
