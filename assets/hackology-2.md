## 5. Conclusion<a id="sec-5" name="sec-5"></a>

It's mysterious to me that these techniques are not usually taught
in either high school or first year physics.
Lack of mathematical background is not the problem.

#### References

Finally, I recommend Sanjoy Mahajan's book
[*Street-Fighting Mathematics*](http://streetfightingmath.com/),
covering similar ground in greater depth.

http://www.fractalcities.org/book/Fractal%20Cities%20Introduction.pdf

https://users.math.yale.edu/~bbm3/web_pdfs/076stochasticModels.pdf

https://core.ac.uk/download/pdf/82639372.pdf

https://dogfishtacklecompany.com/blogs/news/112355910-first-post

https://www.ias.ac.in/article/fulltext/reso/011/01/0063-0078

https://arxiv.org/pdf/physics/0504201.pdf

http://hermes.ffn.ub.es/luisnavarro/nuevo_maletin/Einstein_1906_thesis.pdf

http://physics.bu.edu/~duffy/HTML5/brownian_motion.html

https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1478-4408.1983.tb03728.x

http://ruina.tam.cornell.edu/research/topics/locomotion_and_robotics/simplest_walking/simplest_walking.pdf

https://www.quora.com/Theoretically-how-tall-or-large-can-a-land-animal-evolve-What-would-happen-if-an-animal-exceeded-this-size

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

---

**Exercise 11 (speed of sound).** Sound travels through a fluid (such
as air) as longitudinal waves, which wobble particles back and forth.
The two factors determining how fast this wobbling can propagating are
(1) the *stiffness* of the fluid, measured using the bulk modulus $K$,
with the same units as pressure; and (2) the *density* $\rho$ of the fluid.

(a) Without performing a full dimensional analysis, show that the
speed of sound $c_s$ scales with bulk modulus as

$$
c_s \propto \sqrt{K}.
$$

*Hint.* Find a dimensional factor in $c_s$ which only appears in $K$.

(b) Complete the dimensional analysis and figure out how $c_s$ depends
on $\rho$. Given that the bulk modulus of air depends very weakly on
temperature, would you expect sound to travel faster or slower on a
hot day?

---

### 4.1. Allometry <a id="sec-4-1" name="sec-4-1"></a>

The study of scaling laws in biology is called *allometry*.
Here, we give a few simple examples.
Tissue density is roughly the same for different
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

**Exercise 12 (walking speed).** (a)
Argue that walking speed scales as $\mathcal{L}^{1/2}$. *Hint.* Model the leg as a <a href="#sec-2-1">pendulum</a>.

(b) Average human walking speed is $\sim 1.4$ m/s.
	Estimate the walking speed of a horse and a garden spider.

<p align="center">
  ⁂
	  </p>

**Exercise 13 (thickness).** (a) Argue that the *radius*
    $r$ of a weight-bearing element should scale as $r \propto
    M^{1/2}$ in order to support the organism's weight.

(b) General Sherman is a giant sequoia tree in California's
    Sequoia National Park.
    The diameter of the trunk is $7.7 \text{ m}$.
    Estimate its mass by comparing to the thickness of the human
    thighbone ($r = 2.3$ cm) and using the radius scaling.

---

### 4.2. Fractals <a id="sec-4-2" name="sec-4-2"></a>

*Box counting.* If $\mathcal{L}$ is some linear measure of an organism's size, it's
natural to expect that volume and surface area scale as
$\mathcal{L}^3$ and $\mathcal{L}^2$, respectively, because volume and
area have dimensions $L^3$ and $L^2$.
For a cube and a square these dimensions are obvious, using the
formulas $V_\text{cube} = s^3$ and $A_\text{square} = s^2$ for side length $s$.
To argue that a general volume or area has these dimensions, you
can imagine splitting the volume into many tiny cubes, and the area
into many tiny squares.
This may be hard in practice (it requires integral calculus!), but in
principle it settles the matter.

Or does it?
In reality, a horse or a garden spider is made out of
atoms, not tiny cubes, and atoms are *point-like*.
When you zoom in, any animal resolves itself into a cloud of
$0$-dimensional objects!
It seems like everything is really $0$-dimensional, and should scale
as $L^0$.
This is obviously nonsense. The problem is that we are looking too
close: if we zoom in enough, all we can see are the *constituents* of matter,
losing sight of the forest for the trees.
To reason about "coarse" properties like the dimension, we should make
sure our resolution (the size of our cubes) is much larger than the
length scale $\epsilon_\min$ associated with whatever constitutes a
horse.

So far, so good: don't look too close and you won't see atoms.
But the surface and volume of a horse are both made of atoms, and
splitting a surface area into little squares, for instance, requires that we *already
know* that it is a surface.
That's cheating!
How can I figure out the scaling without assuming the answer?
One elegant method is called *box counting*, where we measure
*everything* with cubes.
First, fix a resolution, $\epsilon$, and generate a pile of (imaginary)
cubes of size $\epsilon$.
Now count how many cubes you need to cover a spatial object of
interest, for instance, the bulk of a horse, or its surface area.

Let's do an example.
If the horse has surface area $A$, and $\epsilon$ is small
(but much larger than an atom), then
the number of cubes needed to cover its skin is

$$
N(\epsilon) \approx \frac{A}{\epsilon^2} \propto \frac{1}{\epsilon^2},
$$

since a tiny cube will overlap the skin with area around $\epsilon^2$.
(Actually, there are larger cross-sections if you tilt the cube, but
the scaling $\propto 1/\epsilon^2$ remains the same.)
Similarly, if you tried to replace the horse's whole body with boxes,
the number would scale as

$$
N(\epsilon) \approx \frac{V}{\epsilon^3} \propto \frac{1}{\epsilon^3}.
$$

Hopefully you see the pattern: the dimension of the object is the
index of $\epsilon$!
In general, a set has *box counting* or *fractal dimension* $d$ if

$$
N(\epsilon) \propto \epsilon^{-d}.
$$

Here, we assume that $\epsilon \gg \epsilon_\min$ (so we can't see
atoms, or whatever things constitute our object) and $\epsilon \ll
\mathcal{L}$ (so the cubes are relatively small).
Then the dimensional-analysis dimension will be $L^d$, and if we make
the object bigger or smaller, it's "generalised volume" will scale as
$\mathcal{L}^d$.
The appearance of the word "fractal" will be justified in a moment.

*Interdimensional monsters.* Box counting seems like a
rather elaborate way to reproduce things we already know: volumes have
dimension $L^3$, areas $L^2$, curves $L$ and points $L^0$.
Usually, we can tell what's going on immediately by drawing a picture!
But there are interdimensional monsters lurking in the thickets between.
Let's catch one!

You can build a simple example with a pencil and eraser.
Start by drawing a straight line segment, which we'll label with the
unit interval $[0, 1]$.
Then erase the middle third, leaving two small intervals of width
$1/3$, from $[0, 1/3]$ and $[2/3, 1]$.
Let's repeat this step for each remaining segment, erasing middle
thirds and leaving $4 = 2^2$ segments of length $1/9 = 3^{-2}$.
We can iterate this process of erasing middle thirds, and after the
$n$th step, we will have $2^n$ segments of length $3^{-n}$.

In real life, the process will eventually terminate when the segments
reach the atomic length scale.
But in the mathematical realm, $\epsilon_\text{min} = 0$, and we can
let the process run forever!
The *Cantor set* is the resulting, infinitely holey pencil line that
remains.
We can use the construction to easily find the fractal dimension.
Since the $n$th step is $2^n$ segments of length $3^{-n}$, and we only
delete segments from then on, we can cover the Cantor set using these
segments.
Using log laws, we find that for $\epsilon = 3^{-n}$,

$$
N(\epsilon) = N(3^{-n}) = 2^{n} = 3^{n\log_3 2} = \epsilon^{-\log_3 2}.
$$

You may worry about other box sizes, but these smoothly interpolate
between these points and don't change the scaling law.
Thus, the box-counting dimension is $d = \log_3 2 \approx 0.63$.
This is neither a point nor a line, but somewhere in between!

*Self-similarity.* We have just discovered *fractals*: objects whose
fractal dimension is different from the dimensionality of objects they
are made out of.
The Cantor set also exhibits a characteristic feature of fractals,
namely that it is *self-similar*.
By construction, the section of the Cantor set from $[0, 1/3]$ looks
the same as the whole thing, but scaled down by $1/3$.
This is not an accident, but rather, a feature of scaling laws in
general!
If a quantity $A$ scales with some quantity $x$ as

$$
A \propto x^p,
$$

then when we "zoom in" or "zoom out" by choosing a rescaled $\tilde{x}
= x/\ell$, for instance, then we get

$$
A \propto x^p = \ell^p \tilde{x}^p \propto \tilde{x}^p.
$$

Using a different, rescaled variable $\tilde{x}$ does not change the
exponent $p$.
This is what self-similar means!
It is therefore natural for objects with scalings $N \propto
\epsilon^{-d}$ (including less exotic things like volumes and surface areas) to be self-similar.

---

**Exercise 14 (more monsters).** You can generalise the
  pencil-and-eraser construction above by iteratively removing a
  fraction $\gamma$ (instead of $1/3$) from the middle of each
  segment, where $0 < \gamma < 1$.

(a) Show that the box-counting dimension is

$$
d = -\frac{\log 2}{\log [(1-\gamma)/2]} = \log_{2/(1-\gamma)}2.
$$

(b) Conclude that *any* dimension in the range $0 \leq d \leq 1$ is possible.

---

*Fractals in nature.* All this would be rather esoteric and
pathological if fractals were not ubiquitous in nature.
But it turns out they are everywhere!
The most infamous example is coastlines.
Naively, a coastline is just a curve bounding a land mass, and we
would expect it to have dimension $L^1$.
But in fact, coastlines get more jagged and intricate as you
zoom in.
The closer you look, the longer they get!
The box-counting dimension is usually between $1$ and
$2$, with the typical dimension around $d \approx 1.3$.
We will give a (partial) explanation for this in the next section, but
the basic idea is that coastlines are formed by random processes, and
we can study how those random processes scale.

Fractals not only result from random physical process, but from
*evolution*.
Our bodies are full of them!
This is not just a fun fact, but explains some puzzling biological scalings.
One of the most famous is *Kleiber's law*, which is the observation
that metabolic rate $R$ (i.e. rate of energy consumption) scales as
$R \propto M^{4/3}$.
This is impossible to explain using the square-cube arguments we gave
above.
But it is explained by fractals!

The rough idea is as follows.
Energy consumption is governed by the rate blood (which contains
oxygen needed for combustion) is delivered to cells.
We now assume the circulatory system is a self-similar fractal built
out of ever smaller tubes, a bit like gluing the different stages in
the construction of the Cantor set together.
We start with a single big tube, the aorta, which branches into some
child tubes, and these branch again.
With a few physics and design requirements, we can deduce Kleiber's
law!

Let's be more precise.
Our first assumption is a very reaonable one: *blood is conserved*.
Suppose each tube has $k$ children, and the children are narrower by a
factor $\beta$ and shorter by a factor $\gamma$.
The rate blood flows through a tube of cross-section $A$ is $A v$.
There are $k$ children, and each has a cross-section of $\beta^2 A$,
so the total cross-section is $k \beta^2 A$.
Assuming the velocity doesn't change, conservation of blood implies

$$
A v = k\beta^2 A v \quad \Longrightarrow \quad \beta = k^{-1/2}.
$$

The second assumption is also very plausible: *the circulatory
system spreads throughout the body*.
Since we're assuming the structure is self-similar, we guess that
*each level* approximately fills a volume, and hence the circulatory
system has fractal dimension $d = 3$.
If a tube has length $\ell$, it covers an approximate volume $\ell^3$
when we use cubes at that resolution.
It has $k$ children of length $\ell \gamma$, and they should cover
approximately the same volume at the lower resolution, so

$$
\ell^3 \approx k (\ell \gamma)^3 \quad \Longrightarrow \quad \gamma = k^{-1/3}.
$$

Our third assumption concerns the smallest tubes in system: *capillary
width and length are independent of organism*.
The basic idea here is that smallest tubes, which deliver material to
the cells directly, have a cross-section $A_\text{capillary}$ and
length $\ell_\text{capillary}$ dictated by the biological requirements
of the cell and not the organism.
Thus, if the capillaries are $c$ levels down, then the rate of
delivery is

$$
R = A_\text{aorta}v = k^c A_\text{capillary} v \propto k^c,
$$

since $v$ and $A_\text{capillary}$ don't depend on the organism's
size.
We're almost done!

Our last assumption is the plausible guess that *the total volume of
blood is proportional to the organism's mass*.
Put differently, the average composition of a lump of flesh doesn't
depend on where it came from.
Let's also assume that each tube has many children $k$.
Then a tube will carry much more blood than its children, since its
volume $A \ell$ is much larger than the combined volume of its children:

$$
k (A \beta^2 \ell \gamma) = A \ell k^{-1/3} \ll A \ell.
$$

The total volume at the capillary level is then

$$
V_\text{capillary} = k^c \gamma A_\text{capillary} \ell_\text{capillary} \propto k^{c},
$$

since we are assuming $A_\text{capillary}$ and $\ell_\text{capillary}$
do not depend on organism size.
Since most of the blood is actually carried in the aorta, we can "go
up" $c$ levels by multiplying by the $(k^{-1/3})^{-c} = k^{c/3}$, to
obtain

$$
M \propto V \propto k^{c} \cdot k^{c/3} = k^{4c/3}.
$$

Since $R \propto k^c$, we have finally arrived at Kleiber's law:

$$
R \propto k^c = \left(k^{4c/3}\right)^{3/4} \propto M^{3/4}.
$$

---

**Exercise 15 (tick tock).** (a) The volume of the heart scales as
$\mathcal{L}^3$.
Using Kleiber's law, deduce that heart rate $B$ (beats per unit time)
scales as

$$
B \propto M^{-1/4}.
$$

(b) Assume that the size of a cell, and amount of blood it can process
before dying, are independent of organism size.
Argue that the lifetime of an organism scales as

$$
T_\text{organism} \propto M^{-1/4}.
$$

*Hint.* You can assume that $T_\text{organism}\propto T_\text{cell}$
in an organism-independent way.

(c) Combining (a) and (b), deduce that the number of hearbeats is
roughly constant, independent of organism size!
Since a normal human heart rate is around $60$ bpm, estimate how many
tocks of the ticker are allotted to each creature on earth.

**Exercise 16 (walking speed revisited).** Above, we predicted a
$\mathcal{L}^{1/2}$ scaling for walking speed with organism size.
Here, we're going to instead consider how human walking speed scales
with *city size*.
The analysis treats the city as a fractal for distributing people!

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


For instance, if you drop dye into water, it will initially spread
quickly before slowing, since it consists of many random walkers (dye
molecules) obeying the $d \propto \sqrt{t}$ scaling.

World Wide Web conference-2006, Bar-Yossef et a


**Exercise 14 (mid-air collision).** (a) Show that the ideal gas law
(Exercise 3) implies an ideal gas has number density

$$
n = \frac{\mathcal{N}}{V} = \frac{P}{k_B\mathcal{T}},
$$

where $P$ is the pressure, $k_B$ is Boltzmann's constant, and
$\mathcal{T}$ the temperature (in Kelvin).

(b) The average air molecule has size $r = 4 \times 10^{-10} \text{ m}$.
Using this data, estimate the density of air molecules around you
right now.

(c) Find the average distance between collisions of air molecules.

<p align="center">
  ⁂
  </p>

*Collision cylinders.* Let's now turn back to random walks of
colliding particles.
There is a nice way to approximate the step length $\ell$ of the walk
in terms of the size and density of colliding particles.
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

More generally, particles are more interesting than rigid billiard balls,
bouncing off each other elastically.
They can attract and repel one another, and particle size is no longer
the relevant parameter.
Instead, this will be given by an effective area or
*cross-section* $\sigma$:

$$
\sigma \ell = U \quad \Longrightarrow \quad \sigma = \frac{1}{n\ell}.
$$

By definition, a collision cylinder of length $\ell$
and cross-section $\sigma$ will contain one particle on average.

---

**Exercise 15 (chain).** A chain lies

<p align="center">
  ⁂
  </p>

**Exercise 14 (taking the air).** Heat is just the kinetic energy of particles.
More precisely, the the average kinetic energy per particle,
$\epsilon$, is proportional to temperature,

$$
\epsilon \sim k_B \mathcal{T}.
$$

This is called the *equipartition theorem*. I think it gives
the most sensible way to think about heat.

(a) Show that if our particles have mass $m$, the average speed is

$$
v_\text{avg} \sim \sqrt{\frac{k_B \mathcal{T}}{m}}.
$$

(b) Show using Exercise 3 that an ideal gas has number density

$$
n = \frac{\mathcal{N}}{V} = \frac{P}{k_B\mathcal{T}}.
$$

(c) Using the collision cylinder method, show that particles of mass
$m$ and size $r$, in a gas with pressure $P$ and temperature
$\mathcal{T}$, will spread out according to

$$
d \sim \left[\frac{(k_B \mathcal{T})^3}{16\pi^2 P^2 r^4 m}\right]^{1/4}\sqrt{t}.
$$

(d) Finally, the average mass and radius of an air molecule is $m = 5 \times 10^{-26}$
kg and $r = 4 \times 10^{-10}$ m.
Estimate how long it takes an air molecule starting in the middle of a
room to reach a wall.

---

A drop of dye in water consists of many random walkers, spreading
quickly before the $\sqrt{t}$ scaling slows it down.

Dye particles are much larger than water
  molecules, so a cloud of dye spreading in a glass of water is Brownian.
  A drop of dye takes around 
  The viscosity of water at room temperature is $\mu \approx 10^{-3}$ kg/m s.

In 1908, Jean Perrin measured the dance of pollen grains in water.
Perrin (1926) and Einstein (1921) picked up Nobel prizes for their
efforts.

This is also the reason we use geometric means.
If the true value is $x$, and $a$ underestimates by a
factor $c$, while $b$ overestimates by a factor $c$, then $\sqrt{ab} =
\sqrt{x^2} = x$ is the true value.
Note that more subestimates will tend to *increase the variance* of
our answers, so once again, we should KISS.
