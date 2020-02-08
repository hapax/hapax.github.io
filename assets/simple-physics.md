---
Layout: post
mathjax: true
comments: true
title:  "Hacking physics from the back of a napkin"
categories: [Physics, Teaching, Hacks]
date:  2020-01-06
---

**February 8, 2020.** *The computational power of the humble napkin is
  awesome and underappreciated. I introduce three simple napkin
  algorithms --- dimensional analysis, Fermi estimates, and random
  walks --- and use them to figure out why rain falls, the length of the
  E. coli genome, and the mass of a proton (among many other
  things!).*

### Contents

1. <a href="#sec-1">Hacking physics</a>
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
   2. <a href="#sec-4-2">Bumping into things</a>
   3. <a href="#sec-4-3">Rainy day dilemma</a>
   4. <a href="#sec-4-4">Brownian motion</a>
5. <a href="#sec-5">Conclusion</a>

## 1. Hacking physics <a id="sec-1" name="sec-1"></a>

*Hacker spirit.* Nowadays, the word "hacker" conjures up visions of dirtbag genius
teenagers, geopolitical intrigue, and Angelina Jolie's 90s pixie cut.
But a nobler usage predates this.
Hacker culture, in the original sense, grew out of places like MIT
in the 60s, with its tradition of highbrow silliness and elaborate technical pranks.
Although associated with programming, hacking spirit can be viewed as
a broader ethos about play, understanding and creativity.
In the words of open-source guru Richard Stallman,

<span style="padding-left: 20px; display:block">
What [hackers] had in common was a love of excellence and
programming. They wanted to make the programs that they used be as
good as they could. They also wanted to make them do neat things. They
wanted to be able to do something in a more exciting way than anyone
believed possible and show 'Look how wonderful this is. I bet you
didn't believe this could be done.'
</span>

Using techniques in a clever or unexpected way is a *hack*, with *hack
value* quantifying the degree of ingenuity. ("Hack" is actually a
back-formation of "hack value".)
Hackers do not look for the most powerful, or obvious, or easy tool
for the job.
They delight in the unexpected, in using humble means to achieve
extraordinary ends.
In a way, they realise David Deutsch's
[definition](https://en.wikipedia.org/wiki/The_Beginning_of_Infinity)
of knowledge as
*information with causal power*.
Knowing a technique well enough to hack it means you can act on the world in new ways.

I think physics needs more hacker spirit: more people willing to fool
around and explore what our marvellous toolset can do, to creatively
defy expectations and push the Deutschian envelope.
Physics is not withouts its hackers
([Richard Feynman](https://en.wikipedia.org/wiki/Richard_feynman)
springs to mind) but unlike computer
science, the hackers are colourful exceptions, tending towards
goofy irreverence and self-mythology.
But I think hacking should go mainstream.

*Napkin hacks.* My goal in this post is to outline a few simple hacks
for the back of a napkin:
dimensional analysis, Fermi estimates, and random walks.
We can think of these as algorithms for a napkin computer!
They really can be implemented using high school algebra on a napkin,
without calculus or calculators (though the latter save time and labour).
Although there is whimsy and irreverence aplenty, the focus will be
*real physics*, culminating in a proof of the existence of atoms, due
to none other than Albert Einstein!
As a little tribute to my city of residence, Vancouver, there is also
a running theme of *rain*.

Hackery is not just about excellence and creativity for their own
sake, but has clear pedagogical implications.
Most people have to wait until grad school to compute viscous drag, estimate
urban power usage, or determine the size of the E. coli genome.
But imagine a world where high school students are so empowered that,
given a few hints, a pencil, and a napkin, they could discover it all
themselves.
This world is very close to ours; all we need is a little more hacker
spirit in the enjoyment and instruction of physics.

For more examples, I can't resist
plugging [my notes](https://hapax.github.io/outreach) for the
[UBC Physics Circle](https://outreach.phas.ubc.ca/events/metro-vancouver-physics-circle/).
Check them out if you want to see how to apply these hacks
to black holes, aliens, dark energy, turbulence, mosh pits, or the amount
of money concealed in couches across Canada!
I also recommend Sanjoy Mahajan's book
[*Street-Fighting Mathematics*](http://streetfightingmath.com/),
covering similar ground at a more advanced level.

## 2. Dimensional analysis <a id="sec-2" name="sec-2"></a>

Physics is ultimately about experimental measurements.
Take some object, maybe an old pumpkin, and poke or prod it with a
measuring device.
The device returns a number, and the *dimension* is what the number
doesn't tell you: what *physical property* probed by that device.
If we compare the width of the pumpkin to a ruler, for instance, the
dimension is the length.
If we put it on some scales, its mass.
If we see how long it takes to rot, its time.

The basic dimensions we have just mentioned are *length* ($L$), *time* ($T$) and *mass* ($M$).
In general, we use brackets $[\cdot]$ to denote the dimension of a
measurement, for instance

$$
[1 \text{ cm}] = L, \quad [4 \text{ hours}] = T, \quad [400 \text{ lb}] = M.
$$

To find the dimension, throw away the number out front and focus on the unit, asking: what
aspect of the system does it measure? Centimetres measure length,
hours measure time, and pounds measure mass.
More complicated dimensions follow from the basic ones according to
simple rules which are easier to show than tell.
Area, for example, has dimensions $L^2$:

$$
[1 \text{ cm}^2] = [1 \text{ cm} \times 1 \text{ cm}] = [1 \text{ cm}]
\times [1 \text{ cm}] = L^2.
$$

An alternative to units is using general formulas, e.g. for the area of a rectangle:

$$
[\text{area}] = [\text{width}\times \text{height}] = [\text{width}]
\times [\text{height}] = L^2.
$$

Dimensions can be divided as well as multiplied:

$$
[\text{velocity}] = \left[\frac{\text{distance}}{\text{time}}\right] =
\frac{[\text{distance}]}{[\text{time}]} = \frac{L}{T}.
$$

Be careful however: only *measurements with the same dimensions* can
be added and subtracted!
For instance, it makes no sense to ask what "1 cm + 4 hours" is, but it
does make sense to ask for the value of "1 cm + 1 foot".
The dimension doesn't change.

Physical laws tell us how measurements depend
on each other.
For example, Newton's second law $F = ma$ tells us how measurements of
force, mass and acceleration are related.
If the two sides of $F = ma$ are equal, the dimensions must agree,
with

$$
[F] = [m a] = [m]\times \left[\frac{v}{t}\right] = \frac{ML}{T^2}.
$$

The point of dimensional analysis is that you can sometimes *reverse*
this process, and determine the physical laws from dimensions!
Let's see how.

### 2.1. Pendulous pumpkins <a id="sec-2-1" name="sec-2-1"></a>

Suppose we attach an old pumpkin to a length of string and give it a
kick.
Gravity will pull on the pumpkin, causing it to oscillate back and
forth with some period of oscillation $t$.
If we know how the period of oscillation depends on other properties
of the system, we can utilise this knowledge to make a pumpkin clock!
Let's start by listing some relevant quantities:
- the mass of the pumpkin $m$, with dimension $[m] = M$;
- the length of the string $\ell$, dimension $[\ell] = L$;
- gravitational acceleration $g = 9.8 \text{ m/s}^2$, dimension $[g] =
  LT^{-2}$ (from the units);
- the initial displacement of the pumpkin $x$, dimension $[x] = L$.

Not all of these quantities will turn out to be relevant.
Galileo discovered that as long as the initial kick is
small, it has no affect on the period: pendulums are "isochronic".
Grab a pumpkin, stopwatch and string, and check for yourself!
(Galileo realised he could exploit this property to make a reliable
timepiece, and invented the pendulum clock.)
In terms of relevant features, this leaves the pumpkin mass $m$, string length $\ell$, and gravity $g$.
You can also eliminate the pumpkin mass empirically, but as we'll see,
we can leave it in and let dimensional analysis *tell us* it's irrelevant.

I'm going to do something a bit sneaky.
Instead of period $t$, we will deal with the *angular velocity*

$$
\omega = \frac{2\pi}{t}.
$$

If we imagine the oscillations as being ticked off on a clock of unit
radius, with one cycle per period, then this is just the velocity of
the tip of the hand.
(We will explain another way to get factors of $2\pi$ in Exercise 4.)
Dimensional analysis is nothing fancier than guessing that $\omega$ is related to $m$,
$\ell$ and $g$ by a physical law of the form

$$
\omega = m^a \ell^b g^c,
$$

for some powers $a, b, c$.
We can find the powers by matching dimensions on each side:

$$
\begin{align*}
T^{-1} = [\omega] = [m^a \ell^c g^c] = \frac{M^aL^{b+c}}{T^{2c}}.
\end{align*}
$$

Requiring the leftmost and rightmost expressions to be equal, we can immediately read off the powers:
$a = 0$, $2c = 1$, and $b = -c$.
It follows that $\omega \sim (g/c)^{1/2}$, where $\sim$ means "up to numerical factors".
As promised, dimensional analysis also kindly informs us that the mass
is irrelevant!
My earlier piece of sneakiness (replacing period with angular
velocity) actually gives the exact answer for small kicks:

$$
\omega = \sqrt{\frac{g}{\ell}}.
$$

Let me emphasise how powerful this is.
We didn't need to solve a differential equation, analyse forces, or even deal with numbers.
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
They will house a large (typically non-pumpkin) pendulum with
$\ell \approx 1$ m.

In order to make the clock, we need a ruler to measure out the length
of string.
But for maximal whimsy, we can switch things up, and turn a stopwatch,
pumpkin and spool into a ruler!
Measure with the string and snip off the corresponding length, attach
the pumpkin and gently wobble.
By timing the period with the stopwatch, you can figure out how long
the object was.

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
[Kepler's third law](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion#Third_law).)

*Hint.* You can ignore the mass of the pumpkin due to the
[equivalence principle](https://en.wikipedia.org/wiki/Equivalence_principle),
i.e. because objects fall the same way in gravitational fields, whatever
their mass.

---

### 2.2. Drag and drop<a id="sec-2-2" name="sec-2-2"></a>

*Stokes' law.* Maybe pumpkins aren't your thing.
Let's turn to something more high-minded: the
aerodynamics of spheres.
So, imagine a sphere moving through a fluid (a liquid or gas).
In realistic fluids, nearby layers of flow like to stick together and will
resist *shearing* forces which pull them apart.
Dragging an object through fluid takes work because the
fluid shears as it moves around the object; [*viscosity*](https://en.wikipedia.org/wiki/Viscosity) quantifies the
resistance to shearing.

Our goal will be to determine the drag force on a sphere due to viscosity.
Here are some things that might be relevant:
- the radius of the sphere $r$, dimension $[r] = L$;
- the speed of the sphere $v$, dimension $[v] = LT^{-1}$;
- the mass of the sphere $m$, dimension $[m] = M$;
- the density of the fluid $\rho$, dimension $[\rho] = ML^{-3}$;
- the viscosity of the fluid $\mu$.

In general, all of these factors are involved, but this is too much
for dimensional analysis to handle.
(I explain why <a href="#sec-2-4">below</a>.)
When the sphere moves slowly enough, however, its mass $m$ and the
density of the fluid $\rho$ are irrelevant.
Only the viscosity, and size and speed of the sphere, matter.
Like the isochronism of the pendulum, this is an empirical fact we can
determine by brute observation.

I haven't told you the dimensions of viscosity yet, but we can find
them fairly easily.
Imagine two layers of fluid flow separated by a distance $d$.
Suppose I try to shear them by simply moving one layer, parallel to
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
Let's write the drag force on the sphere $F_\text{drag}$ as a product of powers
of the remaining factors:

$$
F_\text{drag} = r^a v^b \mu^c.
$$

Then

$$
\frac{ML}{T^2} = [F_\text{drag}] = [r^a v^b \mu^c] = L^a \cdot
\left(\frac{L}{T}\right)^b \cdot \left(\frac{M}{LT}\right)^c = \frac{L^{a+b-c}M^c}{T^{b+c}}.
$$

On the LHS, mass appears as $M^1$, so $c = 1$.
The LHS also has $T^{-2}$, so $b+c = b+1 = 2$, and hence $b = 1$.
Finally, the LHS has $L^1$, and comparing to the RHS gives $a + b -c =
a = 1$.
Dimensional analysis tells us that the drag force is

$$
F_\text{drag} \sim \mu r v.
$$

As usual, we can't determine if there is a number out front. With considerably more
work,
[George Stokes](https://en.wikipedia.org/wiki/Sir_George_Stokes,_1st_Baronet)
showed that

$$
F_\text{drag}= 6\pi \mu r v.
$$

This is called *Stokes' law* in honour of its discoverer.
But we got pretty darn close with a few lines of algebra!

*Why clouds float.* We finish this example by calculating the *terminal velocity* of
water droplets in a cloud.
This will help explain why clouds float and rain falls!
First, consider the general case of a slowly falling sphere.
A sphere of mass $m$ is pulled down by its weight, $F_\text{weight}= mg$.
As it falls, it is slowed by a drag force proportional to the velocity, $F_d = 6\pi \mu r v$.
The terminal velocity $ v_{\text{term}}$ is the speed at which these
two forces balance out:

$$
F_\text{weight} = mg = 6\pi \mu r v_{\text{term}} = F_\text{drag}\quad \Longrightarrow
\quad v_{\text{term}} = \frac{mg}{6\pi \mu r}.
$$

The sphere accelerates until it reaches $v_{\text{term}}$; if it
starts off faster for some reason, it will *slow* until it reaches $v_{\text{term}}$.
To make life simpler, we can express the mass of the sphere
in terms of its volume $V$ and average density $\rho$:

$$
m = V\rho = \frac{4\pi r^3}{3} \rho \quad \Longrightarrow \quad v_{\text{term}} = \frac{mg}{6\pi \mu r} = \frac{2\rho r^2 g}{9\mu}.
$$

(You can also take buoyancy forces $F_\text{buoy} = V
\rho_\text{fluid}$ into account, where $\rho_{\text{fluid}}$ is the density of the fluid.
This just replaces $\rho$ with $\rho - \rho_{\text{fluid}}$.
Since water is much denser than air, the buoyancy forces in our case
are negligible.)

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

**Exercise 2 (terminal raindrops).** When a raindrop gets big enough
  to fall out of a cloud, it is no longer moving slowly, and Stokes'
  law does not apply.

<span style="padding-left: 20px; display:block">
(a) Raindrops fall fast enough that the viscosity of air is irrelevant,
but the density $\rho_\text{air}$ is.
Repeat the analysis above to find that the drag force on a raindrop of
size $r$ is
</span>

$$
F_\text{drag} \sim \rho_\text{air} v^2 r^2.
$$

<span style="padding-left: 20px; display:block">
(b) Conclude that the terminal velocity for a raindrop of mass $m$ is
</span>

$$
v_\text{term} \sim \sqrt{\frac{mg}{\rho_\text{air} r^2}}.
$$

<span style="padding-left: 20px; display:block">
(c) A typical raindrop has radius around $r \approx 1$ mm. How fast is
it moving when it hits the ground?
</span>

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
Mahajan's book for an elementary treatment.

*Where is the physics?* You might think that since all we do is
algebra, there is no physics here at all.
But to avoid parametric overload, we need to whittle down until we
have a manageable number of factors.
Sometimes we can do this by physical reasoning (e.g. Galileo's clever
argument that objects of different masses fall at the same speed), or
restricting to situations where factors are negligible (e.g. a slowly moving sphere).
Sometimes, neither of these works, and we just have to go out, do
experiments, and see what varies (e.g. isochronism and viscosity).
None of these operations necessarily involves hard maths, but they are
definitely all physics!

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
for applications of fundamental constants to black hole thermodynamics!

---

**Exercise 3 (ideal gas law).** A gas of $\mathcal{N}$ particles takes up
  space (with volume $V$), pushes on its container (with pressure
  $P$), and is hot (with temperature $\mathcal{T}$).
  These properties are not independent!
  Their relationship is revealed by dimensional analysis.

<span style="padding-left: 20px; display:block">
(a) Explain why volume should have dimension $[V] = L^3N$.
</span>

<span style="padding-left: 20px; display:block">
(b) Show that pressure has dimension $[P] = M/LT^2$.
</span>

<span style="padding-left: 20px; display:block">
(c) In thermodynamics, there is a fundamental constant called
*Boltzmann's constant*, $k_B = 1.38 \times 10^{-23} \text{ J/K}$, 
where $\text{K}$ stands for Kelvin.
Confirm that $k_B$ has dimension
</span>

$$
[k_B] = \frac{ML^2}{T^2\Theta}.
$$

<span style="padding-left: 20px; display:block">
(d) Finally, use dimensional analysis to deduce the *ideal gas law*:
</span>

$$
PV \sim \mathcal{N}k_B\mathcal{T}.
$$

In fact, the two sides are actually equal for a dilute gas! This is
the form of the equation we will use in the rest of the post.

<p align="center">
  ⁂
</p>

**Exercise 4 (factors of $\pi$).** We can sometimes account factors of
$\pi$ by giving angle its own dimension.
A periodic system has a cycle, which we can keep track of with an
arrow, rotating at a uniform speed around the unit circle.
The arrow (called a *phasor* if you want to be fancy) subtends an angle of $360^\circ$ over the course of a single
period, so really, a period should be viewed not as a time, but a *time per* $360^\circ$.

If $[1^\circ] = \Xi$ is the dimension of angle, then
$[t_\text{period}] = T/\Xi$.
This will leave factors of $\Xi$ floating around.
To cancel them, we can view $2\pi$ as a "fundamental physical
constant" with dimension $\Xi$.
This isn't totally crazy, since $360^\circ = 2\pi$ radian!

<span style="padding-left: 20px; display:block">
(a) Repeat to the pumpkin problems above, now using $[t_\text{period}] =
T/\Xi$ and $2\pi$ as a conversion factor.
You should obtain the same results!
</span>

<span style="padding-left: 20px; display:block">
(b) If your system executes $n$ cycles in the process you're
considering, what conversion factor should you use instead of $2\pi$?
</span>

<span style="padding-left: 20px; display:block">
(c) The $6\pi$ in Stokes' law does not come from a period.
Where could it come from?
</span>

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
and so $4$ rounds up to $10^1 = 10$!
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

A Fermi estimate should be accurate up to a factor of around
$3.2$, i.e. it can be bigger or smaller than the true answer by a
factor of $3$.
Our earlier counts of planets, countries, and global population, for
instance, are well within this generous factor of $3$!

In general, it makes life a bit easier if instead of restricting to
power of $10$ ($1, 10, 100, \ldots$), we allow for
arbitrary numbers, with the understanding *that they are only accurate
up to a factor of* $10^{0.5}$.
We can denote this using a twiddle, so that

$$
\text{number of countries} \sim 200
$$

means "we guess the number of countries is $200$, possibly up to a
factor of $3$".
(When we do dimensional analysis, we also use a twiddle.
In both cases, we are saying "up to some hopefully small numbers out the front!")
Now you know what a Fermi estimate is, let's learn how to do them!

### 3.1. Geometric means<a id="sec-3-1" name="sec-3-1"></a>

On a linear ruler, we average two numbers $a$ and $b$ by halving the sum, $(a+b)/2$.
On a logarithmic ruler, we *take logs first*, then average.
But what does this correspond to when we undo the logs?
Let's check, using log laws.
First, from $\log x + \log y = \log xy$ and $n \log x = \log (x^n)$,
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
of magnitude, this is better to use than the usual *arithmetic
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

**Exercise 5 (lunar ruler).** Fermi estimate the radius of the moon.

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

**Exercise 7 (churches).** Guess the number of churches in
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
As I'll touch on <a href="#sec-3-4">shortly</a>, this also applied to
subestimates, and we shouldn't factorise unless it reduces total uncertainty.

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
\frac{\text{power}}{\text{Vancouver}} \sim 600 \text{ W} \times (2.5
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

**Exercise 8 (loonie bin).** Guess the Canadian government's
federal budget for 2019.

<p align="center">
  ⁂
  </p>

**Exercise 9 (rain power).** The annual rainfall in the greater
  Vancouver region is about $1000$ mm, meaning that all the rain
  that falls in a year would make a layer $1$ metre deep.
Approximately how much energy arrives in the form of raindrops each
year?

*Hint.* You may find Exercise 2 useful. You will need to Fermi
 estimate the area of greater Vancouver (though you can check with Google).

---

### 3.4. Usage notes<a id="sec-3-4" name="sec-3-4"></a>

*Why it works.* Fermi approximation is a subtle art.
In general, it works well because over- and underestimates
balance each other out.
This is an example of the
[wisdom of the crowd](https://en.wikipedia.org/wiki/Wisdom_of_the_crowd),
where averaging over different types of ignorance yields wisdom.
(In this case, the crowd is made up of subestimates!)
But there is more to it than that.
The *variance* (random variability) of subestimates adds up, and a
good rule of thumb is to only factorise into subestimates when the
combined uncertainty of these estimates is much smaller than the
original.
(To get technical, by "uncertainty", we mean "error on the logarithmic
ruler, squared".)

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
[great tutorial](https://www.lesswrong.com/posts/PsEppdvgRisz5xAHG/fermi-estimates)
for pointing this out.)
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
But here's the rub: if I'm wrong by three coin, l'll be off by a
factor of $8 \approx 10$, which is a whole order of magnitude!
If you want a well-defined order of magnitude estimate, back away
slowly from exponentials.
We'll explore what you *can do* with exponential dependence in
Exercise 11.

---

**Exercise 10 (people power).** Earlier, I guessed (based on a hunch)
  that individuals use around $600$ W (or $10$ light bulbs) on
  average. Let's check this a few different ways.

<span style="padding-left: 20px; display:block">
(a) Ask some friends to guess individual power usage, and
take the geometric mean of their answers.
</span>

<span style="padding-left: 20px; display:block">
(b) Next, sanity check my guess or the answer you got in (a).
</span>

<span style="padding-left: 20px; display:block">
(c) Finally, ask Google. How did I do?
How did your friends do?
</span>

<p align="center">
  ⁂
</p>

**Exercise 11 (jumping mugs).** Exponentials may prevent us from doing
  reliable order of magnitude estimates, but they do not prevent us
  from drawing physical conclusions.
  Let's see how likely it is your mug jumps spontaneously into the air.

<span style="padding-left: 20px; display:block">
(a) Estimate the number of atoms $n_C$ in a
mug of coffee.
</span>

<span style="padding-left: 20px; display:block">
*Hint.* Recall that Avogadro's number $N_A = 6 \times 10^{23}$ is the
number of atoms in $12$ g of carbon-12.
</span>

<span style="padding-left: 20px; display:block">
(b) Very roughly, what is the probability the mug jumps
spontaneously into the air?
</span>

<span style="padding-left: 20px; display:block">
*Hint.* Atoms move in random directions. The coffee will spontaneously
 jump if most of the atoms in the cup are moving up.
</span>

<span style="padding-left: 20px; display:block">
(c) If the cup cycles through a billion different random
configurations a second, and the universe (along with the mug and your
coffee table) lasts another $13$ billion
years, are we likely to see the mug spontaneously jump into the air?
</span>

<span style="padding-left: 20px; display:block">
(d) Given that $n_C$ can vary by an order of magnitude, how does the
probability of spontaneous jumping vary? Does it change your
conclusion in (c)?
</span>

<span style="padding-left: 20px; display:block">
(e) (Challenge.) Give a similar estimate that your mug will spontaneously
launch itself into space.
You will probably need to learn about the Maxwell-Boltzmann
distribution and escape velocity.
</span>

---

### 4. Random walks <a id="sec-4" name="sec-4"></a>

Imagine an atom jiggling around randomly in a hot gas.
On average, it will travel some distance $\ell$ between collisions.
Surprisingly, after $n$ collisions, the approximate distance $d$ from
where it started is proportional to the *square root* of the number of steps:

$$
d \sim \ell \sqrt{n}.
$$

How is this possible?
The basic trick is to consider the *displacement*, a vector we label
$\vec{x}$, which is made up of $n$ steps $\vec{s}_i$:

$$
\vec{x} = \vec{s}_1 + \cdots + \vec{s}_n.
$$

The distance squared is just the length of the displacement square,
$d^2 = |\vec{x}|^2$.
We can expand the displacement into steps as

$$
\begin{align*}
d^2 = |\vec{x}|^2 & = (\vec{s}_1 + \vec{s}_2 + \cdots + \vec{s}_n)^2 \\
& = (s_1^2 + s_2^2 + \cdots +
s_n^2) + \text{cross-terms}.
\end{align*}
$$

This is just a generalisation of the familiar algebraic fact that

$$
(x + y)^2 = x^2 + y^2 + 2xy = x^2 + y^2 + \text{cross-terms}.
$$

If the steps have length $\ell$, then each $s_i^2 = \ell^2$.
If different steps are independent and have no preferred direction,
then on average, the cross-terms are zero, since different steps have
no preferred orientation with respect to each other.
For instance, if $x$ is chosen to be $\pm 1$ with probability
$1/2$, and $y$ is independently chosen the same way, then $xy = +1$
half the time, and $xy = -1$ the other half.
On average, that gives zero.
The conclusion is that

$$
d^2 \sim s_1^2 + s_2^2 + \cdots + s_n^2 =
n\ell^2 \quad \Longrightarrow \quad d \sim \ell \sqrt{n},
$$

as claimed above.

This $\sqrt{n}$ scaling is the defining feature of a *random walk*.
Remarkably, nothing depends on the number of dimensions the
displacement $\vec{x}$ lives in.
It is just as true for an atom jiggling in three dimensions, a
drunkard wandering in two dimensions, or a virtual bacterium foraging in a
216-dimensional simulation.

If a random walker moves with speed $v$, a step takes time
$\tau = \ell/v$. After time $t$, the random walker will tend to wander
a distance

$$
d \sim \ell \sqrt{n} = \ell \sqrt{\frac{t}{\tau}} =
\sqrt{\ell v}\cdot \sqrt{t} = \sqrt{Dt},
$$

where we will call $D = \ell v$ the *diffusion coefficient*.
Even though the walker moves at constant speed, the average distance
from the origin scales as $d \propto \sqrt{t}$!
It's important to note that "average distance" is a bit of a
misnomer.
We really mean the *average spread* of distance travelled.
In time $t$, an individual
walker will explore a region of size $\propto \sqrt{t}$, while a
batch of walkers released from the same point will fan out to cover
that region.

---

**Exercise 12 (fractional random walks).** There is a generalisation
  of random walks called *fractional random walks*, where the average
  spread scales with the number of steps as

$$
d \propto n^{H},
$$

for some number $0 < H < 1$ called the *Hurst index*.
Random walks have $H = 1/2$.

<span style="padding-left: 20px; display:block">
(a) Explain why $H > 1/2$ requires that steps be
*correlated*, i.e. directions persist.
</span>

<span style="padding-left: 20px; display:block">
(b) What relation between steps does Hurst index $H < 1/2$ require?
</span>

This not just a theoretical exercise.
The outlines of a coast are jagged, random curves, typically
described by a fractional random walk with Hurst index $H \sim 0.8$.

<span style="padding-left: 20px; display:block">
(c) Why should a coastline consist of *correlated* random steps?
</span>

---

### 4.1. Polymers <a id="sec-4-1" name="sec-4-1"></a>

Random walks not only apply to processes in time, but also in space.
The most important example is polymers: long, jointed chains of
molecules which can often be described by a random walk.
In this case, the step length $\ell$ is the *persistence length* of
the polymer, the distance the polymer remains approximately straight.
After a persistence length, the chain will forget which way it is
pointing and choose a new, uncorrelated direction.
We'll look at a biological application to the biggest, baddest,
most biologically indispensable polymer of them all: *DNA*.

Every cell in an organism contains a copy of its building instructions
in DNA form.
Most organisms are *eukaryotes*, meaning each cell has a special
chamber called the *nucleus* for storing DNA, but in *prokaryotes*
(such as bacteria), the DNA just freely floats in the cellular soup.
Either way, if the container ruptures, the tightly coiled DNA will
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

Multiplying by the number of base pairs per chunk, we estimate a genome length

$$
L_\text{gen} \sim n \times (140 \text{ bp}) \approx 1.5 \times 10^6
\text{ bp},
$$

or $1.5$ Mbp.
A careful count gives $4.6$ Mbp, so we are just within an order
of magnitude!

---

**Exercise 13 (gone fishing).** Wandering the shipyards one day, you
notice a rusty old anchor, probably from a decommissioned fishing vessel.
The mooring chain is haphazardly piled on the dock.

<span style="padding-left: 20px; display:block">
(a) The links are around $7$ inches in length, and the pile is $4.7$
m across.
What is the approximate length of the mooring chain?
</span>

<span style="padding-left: 20px; display:block">
(b) For vessels in shallow water, a good rule of thumb is that the
mooring chain is $1.5$ times the depth of the water.
How deep was the water this vessel fished in?
</span>

---

### 4.2. Bumping into things <a id="sec-4-2" name="sec-4-2"></a>

Collisions occur when objects happen to be in the same
place at the same time.
If you want to keep track of what is entering your space, imagine that
you sweep out an envelope as you move.
The bigger you are (or more precisely, the bigger your cross-section
in the direction of motion), the more likely you are to collide with
things.
But you are more likely to collide with elephants than fleas!
You also want to take into account the size of the objects you might
be running into.

The formal way of doing this is a *scattering cross-section*
$\sigma$.
The basic idea is that if you sweep out a "collision cylinder" with
cross-section $\sigma$, and the centre of another object lies in the
cylinder, a collision will occur.
The cross-section $\sigma$ takes into account both your size and the
size of the objects you collide with.
If you move a distance $x$, and have scattering cross-section
$d$ with respect to elephants (or whatever it is you are worried
about colliding with), your collision cylinder will have volume

$$
V = x\sigma.
$$

If we know the number of colliding objects (e.g. elephants) per unit
volume in the vicinity, we can estimate the number of collisions!
For instance, if there are $n$ elephants per unit volume, then on average, you will
collide with $nV = n\sigma x$ elephants as you move a distance
$x$.

Let's do some very simple examples of cross-sections.
Picture yourself as a sphere of radius $R$, worried about colliding
with spheres of radius $r$.
You can show in Exercise 14 that the scattering cross-section is

$$
\sigma = \pi (R+r)^2.
$$

This means in particular that if you are much larger than the spheres
you are bumping into, the cross-section is $\pi R^2$, and if you are
much smaller, it is $\pi r^2$.
If you are colliding with spheres of the same size, then the
scattering cross-section is

$$
\sigma = \pi (2R)^2.
$$

This covers most of the cases we will be interested in!

*Mean free path.* Now, back to our regular programming: random walks in gases.
We would like to determine the step length $\ell$ for the random walk
executed by colliding particles, assuming they are all spheres of
radius $r$.
The method is simple.
We just draw a collision cylinder until the number of expected
collisions is $1$, then call it a day:

$$
1 = n V = n \ell \sigma \quad \Longrightarrow \quad \ell =
\frac{1}{n\sigma} = \frac{1}{\pi n (2r)^2}.
$$

Hopefully this makes sense.
We want $\ell$ to be average distance between collisions, and this is
	exactly what the collision cylinder calculates when we set the number
of collisions equal to one.
The fancy name for distance between collisions is *mean free path*,
but we will use this sparingly.

As a simple example, we can estimate the average distance between
collisions of air molecules at room temperature ($300$ K) and
atmospheric pressure ($100$ kPa).
The trick is to exchange temperature and pressure for number per unit
volume using the ideal gas law (Exercise 3):

$$
PV = \mathcal{N}k_B \mathcal{T} \quad \Longrightarrow \quad n = \frac{P}{k_B \mathcal{T}},
$$

where $n = \mathcal{N}/V$ is the number of air particles per unit
volume.
To find $\lambda$, we also need the size of an air molecule.
Most of it is nitrogen, and a little oxygen, with average diameter $2r
= 4 \times 10^{-10}$ m.
We can plug all our numbers in, along with Boltzmann's constant, to
find the mean free path:

$$
\ell = \frac{1}{\pi n (2r)^2} = \frac{k_B\mathcal{T}}{\pi P (2r)^2} =
\frac{(1.38 \times 10^{-23})300}{\pi (100\times 10^3)(4 \times
10^{-10})^2} \text{ m} \sim 80 \text{ nm}.
$$

So, on average an air molecule travels around $80$ nm, around $1000$
human hairs across.
In Exercise 15, you can see how *fast* air molecules diffuse.

One final technical point.
Most of this collision cylinder technology assumes that we are
colliding with *stationary objects*.
If they are stationary *on average*, that is, there is no preferred
direction, then the same estimates still work provided you are not too
much larger than the objects you're colliding with.
When you are too big, remain still and you will collide with many tiny
moving objects!
This is exactly what large objects feel as *pressure*.
To understand how very large objects interact with a bath of tiny,
randomly moving ones, it's better to use thermodynamics than
cylinders.

---

**Exercise 14 (smashing spheres).** Consider two spheres of radius $R$ and $r$.

<span style="padding-left: 20px; display:block">
(a) Show that if the centres come within a distance $R+r$, they
  will collide.
</span>

<span style="padding-left: 20px; display:block">
(b) Explain why the scattering cross-section is $\sigma = \pi (R+r)^2$.
</span>

<span style="padding-left: 20px; display:block">
(c) Conclude that, if $R \gg r$, then $\sigma \approx \pi
R^2$.
</span>

<p align="center">
  ⁂
  </p>

**Exercise 15 (equipartition and air time).** People often say that
"temperature is just atomic motion".
This is shorthand for "temperature is just average kinetic energy per
particle"!
More precisely, temperature is *proportional to* the average kinetic
energy per particle $\epsilon_\text{avg}$,

$$
\epsilon_\text{avg} \sim k_B \mathcal{T},
$$

where $k_B$ is the Boltzmann constant.
This is a simple version of a deep result called the *equipartition
theorem*.
So Boltzmann's constant tells us how to convert temperature into enrgy
per particle.

<span style="padding-left: 20px; display:block">
(a) Show that if the particles have mass $m$, the average speed is
</span>

$$
v_\text{avg} \sim \sqrt{\frac{k_B \mathcal{T}}{m}}.
$$

<span style="padding-left: 20px; display:block">
(b) Using the collision cylinder method, compute the diffusion
constant $D = \ell v$ in a gas with pressure $P$ and temperature
$\mathcal{T}$, consisting of particles of mass $m$ and size $r$.
You should find that
</span>

$$
D \sim \frac{(k_B \mathcal{T})^{3/2}}{\pi \sqrt{m} P (2r)^2 }.
$$

<span style="padding-left: 20px; display:block">
(c) The average mass of an air molecule is $m = 5 \times 10^{-26}$ kg
(once again, this is slightly larger than the mass of an N$_2$
molecule, since its mostly nitrogen plus some heavier elements).
Estimate how long it will take an air molecule near your head to reach the
wall.
</span>

---

### 4.3. Rainy day dilemma<a id="sec-4-3" name="sec-4-3"></a>

(*Note.* This is a fun optional extension of collision
cylinders. It's not needed for the final section on Brownian motion.)

Let's do a twist on collision cylinders and take moving objects into
account.
Rather than do it formally and in general, we will be illustrative and
specific, solving the age-old problem: should you
walk or run in the rain?
Some people argue it doesn't matter (and there is infamous MythBusters
episode which gets it wrong), but we can use collision cylinders to
reason it out!

We will model people as spheres (naturally), but Exercise 16 is more realistic.
So, you are a sphere of radius $R$ caught in a rainstorm, and shelter
is a distance $d$ away.
The rain consists of tiny balls of water, falling directly down
(no wind) at some speed $v$.
Viewed in the reference frame of the falling drops, there are $n$
drops per unit volume.
The speed $v$ and density $n$ can change with height, but we're only
interested in these quantities near the ground, so we are at liberty
to imagine that they are constant everywhere.

We haven't talked about how to deal with colliding objects all moving
in the same direction, and here's the nice thing: we don't need to!
Instead, let's think about everything in the reference frame of the
rain.
Imagine it extends infinitely in all directions, with density of drops
$n$.
You, the sphere, travel in a vertical direction at speed $v$, and
horizontally towards the shelter (represented as a vertical line a
distance $d$ away) at some speed of your choice, $u$.
The question is: does the number of drops you collide with on your way
to shelter depend on $u$?
If it doesn't, you may as well walk.

But the answer is obviously *yes*: if you stand still, you will get infinitely drenched.
Let's explore this with a little more care.
If you move at speed $u > 0$, you arrive at shelter in time $t = d/u$.
Hence, your path has length

$$
x = \sqrt{(vt)^2 + (ut)^2} = d\sqrt{1 + (v/u)^2}.
$$

Since the drops are small, your cross-section is $\sigma = \pi R^2$,
and the number of drops you collide with is then

$$
nV = n  \sigma x = \pi nR^2d\sqrt{1 + (v/u)^2}.
$$

To make this as small as possible, you should make $u$ as large as
possible.
In other words, run for shelter!
This is particularly clear when the rain falls much faster than you
run, with $v/u \gg 1$, in which case

$$
n V \approx \pi n R^2d \cdot \frac{v}{u} = (\pi n R^2 v)t.
$$

How wet you get is directly proportional to how much time you spend in
the rain!

---

**Exercise 16 (box of rain).** Let's now make a slightly more realistic model of a person: a
box of height $h$, width $w$, and breadth $b$.
For simplicity, suppose there is no wind, and shelter is a distance
$d$ away.
The collision cylinder will now be made up of two pieces, associated
with the front and top of the box.

<span style="padding-left: 20px; display:block">
(a) Argue that the volume of the collision cylinder for the front of
the box does not depend on running speed $u$. Is this consistent with
our original
observation that a stationary sphere will get infinitely wet?
</span>

<span style="padding-left: 20px; display:block">
*Hint.* You may find trigonometry useful.
</span>

<span style="padding-left: 20px; display:block">
(b) Show that the collision cylinder for the top of the box has a volume
proportional to $t$.
Once more, this shows you should run (unless you are very, very thin).
</span>

<p align="center">
  ⁂
  </p>

**Exercise 17 (wet and windy).** When the wind blows, it imparts a
horizontal velocity to the rain.
As above, we consider a sphere seeking shelter a distance $d$ away.

<span style="padding-left: 20px; display:block">
(a) If the wind blows *away* from shelter, explain why you should run
as fast as possible.
</span>

<span style="padding-left: 20px; display:block">
(b) Suppose the wind is blowing *towards* shelter with a horizontal
velocity $u'$, and has downward velocity $v$.
Demonstrate that there is a *finite* optimal speed to move towards
shelter, $v^2/u'$.
If it's very windy, it may be better to walk!
</span>

---

### 4.4. Brownian motion <a id="sec-4-4" name="sec-4-4"></a>

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
Now plonk some large, easily visible particles into this fluid,
for instance pollen grains, of radius $r$ and mass $m$.
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

From observing the pollen grains meander, we can directly calculate the diffusion
coefficient $D = \ell v$, since $d^2 \sim Dt$.
We still need to work out the velocity, $v$, and here is the clever
part: since our fluid was viscous, and assuming the grains move
slowly, we can apply <a href="#sec-2-2">Stokes' law</a>!
If the grains are in equilibrium, it's reasonable to guess that their
velocity is the terminal velocity we calculated earlier:

$$
v_{\text{term}} = \frac{mg}{6\pi \mu r},
$$

where $\mu$ is the viscosity.
Putting it all together, we predict a diffusion coefficient

$$
D \sim \ell v_{\text{term}} = \frac{k_B\mathcal{T}}{6\pi \mu r}.
$$

This is called the *Stokes-Einstein relation*, and it is one of the
major results of Einstein's PhD thesis.
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
genius was to extract specific and testable predictions, which Jean
Perrin confirmed experimentally in 1908.
Both Perrin and Einstein received Nobel prizes, in part for this work.
We'll end with one of the practical applications Einstein suggested
and Perrin carried out --- weighing molecules!

---

**Exercise 18 (Avogadro's constant).** You may have seen the ideal gas law
(Exercise 3) in its chemistry guise:

$$
PV = n_\text{mol} \mathcal{R} \mathcal{T},
$$

where $n_\text{mol}$ is the number of particles in mol, and

$$
\mathcal{R} = 8.3 \, \text{ J / K mol}.
$$

Recall that one mole is $N_A$ particles, where $N_A$ is *Avogadro's
constant*, the number of carbon atoms in a $12$ g lump.
But Avogadro didn't know his own constant!
His big contribution is something called *Avogadro's law*:

<span style="padding-left: 20px; display:block">
*Equal volumes of gas, at equal temperature and pressure, contain the
same number of molecules.*
</span>

This was a prescient insight into the atomic nature of matter,
anticipating the ideal gas law 45 years prior.

Determining the number of molecules in a sample of gas is the same as
weighing a molecule.
This turns out to be hard!
But it is easy to measure the volume of the gas (place it in a
container of fixed volume), the pressure (use a barometer), the
temperature (a thermometer), and finally, the number of mole (the
magic of chemistry).
That makes it fairly easy to measure the ideal gas constant $\mathcal{R}$.

<span style="padding-left: 20px; display:block">
(a) By equating the two different forms of the ideal gas law, deduce
that $N_A = \mathcal{R}/k_B$.
</span>

Our goal is going to be to weigh atoms and molecules. If we know the
molar mass, all we need to do is divide by $N_A$!
Perrin and Einstein gave the first modern estimates of Avogadro's
number using Brownian motion, so we will follow in their footsteps.

<span style="padding-left: 20px; display:block">
(b) Suppose a spherical particle jiggles a distance $d$ in time $t$
due to Brownian motion.
Using the Einstein-Stokes relation, show that
</span>

$$
N_A \sim \frac{t}{d^2}\cdot \frac{\mathcal{R}\mathcal{T}}{6\pi \eta r}.
$$

<span style="padding-left: 20px; display:block">
This is the last equation in
[Einstein's famous paper](http://www.maths.usyd.edu.au/u/UG/SM/MATH3075/r/Einstein_1905.pdf)
on Brownian motion!
</span>

Perrin used Einstein's method to determine $N_A$.
He painstakingly prepared tiny spheres of resin, then dropped them
into warm water and watched them dance.
The tracks of three resin particles ($r = 0.52 \times 10^{-6}$ m) are
shown below.
Observations (the dots) were made every $30$ s, and divisions are
ruled every $3.125 \,\mu$m.

<span style="padding-left: 20px; display:block">
(c) Use the tracks to estimate Avogadro's constant.
The temperature of the water was around $\mathcal{T} = 290$ K, with
viscosity $\eta \approx 0.0011$ kg/m s. </span>

<!-- cluster: 20 points with d ~ 5 divisions, 20*30*8.3*290/((5*0.000003125)^2*6*pi*0.0011*(0.52*10^(-6))) -->

Now, as you probably know from chemistry class, the official value is
$N_A = 6.02 \times 10^{23}$ (hopefully you got something close in the
last question).
We can finally use this to weigh a molecule!
As a bonus, we can weigh protons and neutrons as well.

<span style="padding-left: 20px; display:block">
(d) Estimate the mass of a carbon atom.
</span>

<span style="padding-left: 20px; display:block">
(e) Naturally occuring carbon is mostly carbon-12, which has $12$
nucleons (protons and neutrons of approximately equal mass) in the
nucleus.
How heavy is a proton?
</span>

I think this is pretty neat. From watching tiny balls jiggle in water,
we can work out the mass of a proton!

---

## 5. Conclusion <a id="sec-5" name="sec-5"></a>

I hope I've persuaded you that we can hack physics with napkin
computers.
Every single thing we explored --- from pendulum periods to the
ideal gas law, fish in the sea to mooring chains, and rainy runs to
dancing dust specks --- required, at
most, a little pre-calculus math and solid command of a napkin hack.
There is great power in simple techniques.
And we have only scratched the surface!
Physics is brimming with napkin algorithms, just waiting for hackers
to explain and exploit.

This raises the question: why don't we teach these techniques in
schools?
The most charitable answer is that we focus on content rather than
methods since high-leverage methods are deemed too advanced.
But in the words of Cyprian of Carthate, *custom without truth is the
antiquity of error*.
Hacker spirit is the perfect antidote for custom without truth.

#### References

https://uwaterloo.ca/chem13news/sites/ca.chem13news/files/uploads/files/may06_2006_page_14.pdf
