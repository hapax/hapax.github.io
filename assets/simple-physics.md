---
Layout: post
mathjax: true
comments: true
title:  "The awesome power of simple physics"
categories: [Physics, Teaching]
date:  2020-01-06
---

**January 6, 2020.** *Physics is often presented as the most arcane and
  mathematically impenetrable of natural sciences. Here, we illustrate
  how simple physical ideas, back up by pre-calculus
  mathematics, can be awesomely powerful.*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Dimensional analysis</a>
   1. <a href="#sec-2-1">Pendulous pumpkins</a>
   2. <a href="#sec-2-2">Drag and drop</a>
   3. <a href="#sec-2-3">Usage notes</a>
3. <a href="#sec-3">Fermi estimates</a>

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
Judging from competition problems, this should restrict us to
tediously intricate mechanics problems, with a smattering of circuits,
optics, and other elementary topics.

I decided to view this as a challenge: do more with less.
I am not above writing tediously intricate mechanics problems, but it
was much more instructive to master the basic hacks and use them to teach myself new things.
I'm not sure about the students, but it certainly made me a better physicist!
The goal of this post is to share a few of these hacks and convince
you of their awesome power.

To keep things interesting, I avoid overlap with my
[physics circle problems](https://hapax.github.io/assets/circle-probs.pdf),
though feel free to check these out if you want more examples than you
can dangle a plumb bob at.
I also recommend Sanjoy Mahajan's book
[*Street-Fighting Mathematics*](http://streetfightingmath.com/) (which
I only discovered recently!), covering similar ground in greater depth.
The hacks are in no particular order except for the "fundamental hacks" of
dimensional analysis and Fermi estimation.
Everything else can be read independently and in any order.
For each hack, I quickly outline the physics, do some examples,
and finish with usage notes.

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

Incidentally, this explains why grandfather clocks are so large!
They need to house a large (usually non-cucurbitar) pendulum of
length around one metre.
In order to make the clock, we need a ruler to measure out the length
of string.
But for maximal whimsy, we can turn a stopwatch, pumpkin and spool of
string *into* a ruler!
Use the string as a ruler, snip off the corresponding length, attach
the pumpkin and gently wobble.
By timing the period of the wobble with the stopwatch, we can figure
out how long the string is!

#### 2.2. Drag and drop<a id="sec-2-2" name="sec-2-2"></a>

In case pumpkin timepieces aren't your thing, we'll ratchet down the
whimsy and investigate the aeorodynamics of spheres.
In realistic fluids, adjacent layers of flow like to stick together, and will
resist *shearing* forces which try to pull them apart.
This resistance to shearing is called [*viscosity*](https://en.wikipedia.org/wiki/Viscosity).
Dragging an object through a fluid takes work because, as we plough
through, we necessarily displace these layers.

We're now going to determine the *drag force* on a sphere being
dragged through a viscous fluid.
As above, we're going to use dimensional analysis to write this drag force
as a function of other parameters.
The possibly relevant parameters are:
- the radius of the sphere $r$, dimension $[r] = L$;
- the speed of the sphere $v$, dimension $[v] = LT^{-1}$;
- the mass of the sphere $m$, dimension $[m] = M$;
- the density of the fluid $\rho$, dimension $[\rho] = ML^{-3}$;
- the viscosity of the fluid $\mu$.

In principle, all of these factors will be involved, but this is too many
factors for dimensional analysis to work.
(See <a href="#sec-2-4">the usage notes</a> to understand why.)
But it turns out that the mass of the fluid and sphere are only
relevant when the fluid flow is [*turbulent*](https://en.wikipedia.org/wiki/Turbulence) and unsteady.
If the sphere moves through the fluid slowly enough, only the
geometry of the sphere and viscosity are relevant.
This is called "laminar" (layered) flow because, in contrast to
turbulent flow, the fluid remains in well-defined layers.

I haven't told you the dimensions of viscosity yet, but we can
determine them easily enough.
Imagine two layers separated by a distance $d$.
Suppose I try to separate them by simply moving one layer, parallel to
the second, but at a speed $v$.
Experiment shows that the fluid will resist with some force $f = F/A$ per
unit area, proportional to $v$ and inversely proportional to the
separation $d$.
The constant of the proportionality is the viscosity $\mu$, and we can
use this to determine the dimensions:

$$
f = \frac{F}{A} = \mu \left(\frac{v}{d}\right) \quad \Longrightarrow \quad [\mu] =
\left[\frac{dF}{Av}\right] = \frac{L(ML/T^2)}{L^2(L/T)} = \frac{M}{LT}.
$$

We can now proceed with our dimensional analysis.
Let's write the drag force on the sphere $F_d$ as a product of powers
of the remaining factors,

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
Dimensional analysis has led us to the rather simple answer

$$
F_d \sim \mu r v.
$$

As usual, we can't determine if there is a number out fornt. With considerably more
work,
[George Stokes](https://en.wikipedia.org/wiki/Sir_George_Stokes,_1st_Baronet)
showed that

$$
F_d = 6\pi \mu r v.
$$

This is called *Stokes' law* in honour of its discoverer.
But we got pretty darn close with only a few lines of algebra!

Stokes' law has some wonderful applications, with the simplest being
to the *terminal velocity* of a sphere falling through a fluid.
This may sound rather artificial, but it lets us estimate the speed at
which raindrops and hailstones strike the ground!
Let's start by working out the terminal velocity in general.
A sphere of mass $m$ is pulled down by its weight, $F_w = mg$.
If it falls through a fluid of viscosity $\mu$, then there will be a
drag force proportional to the velocity, $F_d = 6\pi \mu r v$.
At the terminal velocity $ v_{\text{term}}$, these two forces
balance out:

$$
F_w = mg = 6\pi \mu r v_{\text{term}} = F_d \quad \Longrightarrow
\quad v_{\text{term}} = \frac{mg}{6\pi \mu r} = \frac{2\rho r^2 g}{9\mu},
$$

where we traded in the mass of the sphere for its average density
$\rho$ via $m = (4\pi/3)\rho r^3$.

Neither raindrops nor hailstones are perfectly spherical, but it's not a bad
approximation.
Let's start with raindrops

https://wxguys.ssec.wisc.edu/2013/09/10/how-fast-do-raindrops-fall/

#### 2.3. Usage notes<a id="sec-2-3" name="sec-2-3"></a>

Since we throw away numbers, dimensional analysis will usually only be
good up to an overall numerical factor.

[notes](https://hapax.github.io/assets/dimensional-analysis.pdf).

## 3. Fermi estimates <a id="sec-3" name="sec-3"></a>

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
