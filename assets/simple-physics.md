---
Layout: post
mathjax: true
comments: true
title:  "The awesome power of simple physics"
categories: [Physics, Teaching]
date:  2020-01-06
---

**January 6, 2020.** *Physics is often presented as the most arcane and
  mathematical of natural sciences. Here, we show how
  simple physical ideas, with a dash of pre-calculus mathematics, can
  still be awesomely powerful.*

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

## 1. Introduction <a id="sec-1" name="sec-1"></a>

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
tediously intricate mechanics problems with a smattering of circuits,
optics, and other elementary topics.

I decided to view this as a challenge: do more with less.
I am not above writing tediously intricate mechanics problems, but it
was much more instructive to master some simple physics hacks and use
them to discover new things.
I'm not sure about the students, but it has certainly made me a better physicist!
The goal of this post is to share a few of these hacks and convince
you of their awesome power.

To keep things interesting, I avoid overlap with my
[physics circle problems](https://hapax.github.io/assets/circle-probs.pdf),
though I encourage you to have a look if you want more examples.
I also recommend Sanjoy Mahajan's book
[*Street-Fighting Mathematics*](http://streetfightingmath.com/), covering similar ground in greater depth.

## 2. Dimensional analysis <a id="sec-2" name="sec-2"></a>

Physics is ultimately about experimental measurements.
We take some system, e.g., an old pumpkin, and poke or prod it with a
measuring device, thereby obtaining a number.
The *dimension* of the measurement is not the number, but the
*physical property* probed by that device.
If we compare the width of the pumpkin to a ruler, for instance, the
dimension is the *length*.

Length ($L$) is one of the basic dimensions we can use to build other
dimensions.
The two other basic dimensions are *time* ($T$) and *mass* ($M$).
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
physical laws relating some quantities from their dimensions!
Once again, this is easier to show with examples than abstract descriptions.

#### 2.1. Pendulous pumpkins <a id="sec-2-1" name="sec-2-1"></a>

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

I'm going to do something a bit sneaky, though it will seem natural if
you've dealt with oscillations before.
Instead of period $t$, we will deal with the *angular frequency*

$$
\omega = \frac{2\pi}{t}.
$$

If we imagine the oscillations as being ticked off on a clock of unit
radius, with one cycle per period, then this is just the velocity of
the tip of the hand.
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
frequency) means this is *exactly* correct (for small kicks):

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

**Exercise 1 (large pumpkin ruler).** You can use an old pumpkin to
measure very large objects as well.
Place the sun at one end of the object, and the pumpkin at the other.
If you kick the pumpkin with enough energy and in the right direction,
it will orbit the sun in a circle of radius $r$ (the length of the
object) with angular frequency $\omega$.
Using dimensional analysis, show that

$$
r \sim \left[\frac{GM}{\omega^2}\right]^{1/3},
$$

where $M$ is the mass of the sun and $G = 6.7 \times 10^{-11} \text{
m}^3 \text{/kg s}^2$ is *Newton's constant*, controlling the strength
of gravity.

*Hint.* You can ignore the mass of the pumpkin due to the
[equivalence principle](https://en.wikipedia.org/wiki/Equivalence_principle),
i.e. because objects fall the same way in gravitational fields, whatever
their mass.

---

#### 2.2. Drag and drop<a id="sec-2-2" name="sec-2-2"></a>

Maybe pumpkins aren't your thing.
Let's ratchet down the
whimsy and turn to something a little more high-minded: the
aerodynamics of spheres.
So, imagine a sphere moving through a fluid, e.g. a
[Bathysphere](https://en.wikipedia.org/wiki/Bathysphere) sinking to
the ocean floor.
(You can explore this example in Exercise 2.)
In realistic fluids, nearby layers of flow like to stick together and will
resist *shearing* forces which pull them apart.
Dragging an object through a fluid wil then take work, because the
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
Imagine two layers separated by a distance $d$.
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

We finish this example by calculating the *terminal velocity* of
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

**Exercise 2 (sinking bathysphere).**
The [Bathysphere](https://en.wikipedia.org/wiki/Bathysphere) was a
hollow ball of steel designed for deep-sea exploration.
It weighed $2.25$ tons (above water) and had a diameter of $1.45$ m.
Roughly how long would it take to sink to the bottom of the Mariana Trench?
The Mariana Trench is $11$ km deep, and filled with cold water of
viscosity $\mu \approx 0.0016 \text{ kg/m s}$.

*Hint.* Assume it is travelling at terminal velocity, and Stokes' law
 applies. You should also take buoyancy forces into account!

---

#### 2.3. Usage notes<a id="sec-2-3" name="sec-2-3"></a>

Dimensional analysis has its limits.
First of all, since we throw away numbers, it only good up
to an overall numerical factor.
In the first example, I sneakily chose angular frequency so that the
missing numerical factor was $1$, but in the second example, we were off by
$6\pi \approx 20$.
It is perhaps better to think of dimensional analysis as giving
system-dependent *scales* rather than answers to specific questions.
That said, nature is bountiful, and more often than not the missing
number is close to $1$!

A more serious problem is the overabundance of parameters.
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
For more details, check out my
[notes on dimensional analysis](https://hapax.github.io/assets/dimensional-analysis.pdf) or
*Street-Fighting Mathematics*.

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

#### 3.1. Geometric means<a id="sec-3-1" name="sec-3-1"></a>

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

**Exercise 3 (lunar radius).** Fermi estimate the radius of the moon.

*Hint.* Take the geometric mean of an overestimate and an underestimate.
For an overestimate, you could try the radius of
 the earth, $r_\oplus = 6300 \text{ km}$.

---

#### 3.2. Subestimates<a id="sec-3-2" name="sec-3-2"></a>

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
[random, non-peer-reviewed article](https://www.worldatlas.com/articles/how-many-fish-are-there-in-the-ocean.html). Huh!

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

**Exercise 4 (churches in the US).** Guess the number of churches in
the US.

*Hint.* A particularly useful intermediate factor is *people*, both in
 this problem and in general.
 The US has a population of around $300$ million.

---

#### 3.3. KISS<a id="sec-3-3" name="sec-3-3"></a>

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
PhD [comprehensive exam](https://www.phas.ubc.ca/sites/phas/files/comp_aug2018.pdf)!)
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

**Exercise 5 (Canadian budget).** Estimate Canada's 2019 budget.

*Hint.* You may need to use all three techniques!

---

#### 3.4. Usage notes<a id="sec-3-4" name="sec-3-4"></a>

So far, I've described what I think are the key methods for doing
Fermi estimates.
But it's a subtle art, and just like dimensional analysis, there is
quite a bit going on under the hood to ensure it works.
First of all, somewhat counterintuitively, *more subestimates is
better*.
Roughly, our under- and overestimates will tend to balance each other
out.
This is the same reason geometric means work!
More explicitly, if the true value is $x$, and $a$ underestimates by a
factor $c$, while $b$ overestimates by a factor $c$, then $\sqrt{ab} =
\sqrt{x^2} = x$, the true value.

https://www.lesswrong.com/posts/PsEppdvgRisz5xAHG/fermi-estimates

##### 4. Random walks <a id="sec-4" name="sec-4"></a>

##### 5. Scaling <a id="sec-5" name="sec-5"></a>


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
