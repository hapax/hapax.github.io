---
Layout: post
mathjax: true
comments: true
title:  "The awesome power of simple physics"
categories: [Physics, Teaching]
date:  2020-01-06
---

**January 6, 2020.** *Physics is often presented as the most arcane,
  mathematically impenetrable of natural sciences. Here, we illustrate
  how simple physics hacks using only pre-calculus
  mathematics can still be awesomely powerful.*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Dimensional analysis</a>
   1. <a href="#sec-2-1">The hack</a>
   2. <a href="#sec-2-2">Example: spring-mass system</a>
   4. <a href="#sec-2-4">Usage notes</a>
3. <a href="#sec-3">Fermi estimates</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

I've been heavily involved in running a
[high school physics circle](https://outreach.phas.ubc.ca/events/metro-vancouver-physics-circle/)
for over a year now.
I've learned a lot about logistics, leadership, and balancing leaning
towers of pizza.
But surprisingly, the biggest lesson has been about *physics itself*.
In a physics circle (or high school physics competition more
generally), the mandate is to write problems that high school students
will find challenging but fair given their limited background knowledge.
In particular, problems should avoid calculus, which is not part of
Canada's high school curriculum.
Judging from competition problems, this should restrict us to
tediously intricate mechanics problems, with a smattering of circuits,
optics, and other random elementary topics.

I decided to view this as a challenge: do more with less, i.e. find
ways to introduce advanced topics without pages of tedious algebra.
As a theoretical physicist used to employing a full arsenal of
mathematical tools, this was a strict constraint!
But perversely, creative outcomes are often optimised by *adding* constraints.
In trying to get at more advanced topics, I was led to reappraise
basic physics hacks like dimensional analysis.
Though I am not above writing tediously intricate mechanics problems,
it was much more exciting to use these simple tools to teach myself
something new, with the added benefits that genuine enthusiasm brings.

The goal of this post is to share a few of these hacks.
Hopefully, you'll be convinced of the awesome power of simple physics!
Of course, like every tool, there are quirks and quagmires to be aware
of, and I will comment on these in turn.
To keep things interesting, I've avoided overlap with my
[physics circle problems](https://hapax.github.io/assets/circle-probs.pdf)
and [notes](https://hapax.github.io/assets/dimensional-analysis.pdf),
though feel free to check these out if you want more examples than you
can dangle a plumb bob at.
I also recommend Sanjoy Mahajan's book
[*Street-Fighting Mathematics*](http://streetfightingmath.com/) (which
I only discovered recently!) which covers similar ground in greater depth.

The hacks are in no particular order except for the "fundamental hacks" of
dimensional analysis and Fermi estimation.
Everything else can be read independently and in any order.
For each hack, I quickly outline the physics, do some examples,
and finish with usage notes.

## 2. Dimensional analysis <a id="sec-2" name="sec-2"></a>

#### 2.1. The hack <a id="sec-2-1" name="sec-2-1"></a>

Physics is ultimately about experimental measurements.
The *dimension* of a measurement is the physical property of a system
probed by the measurement.
Basic examples include *length* ($L$), *time* ($T$) and *mass* ($M$).
We use brackets $[\cdot]$ to extract the dimension from a measurement, e.g.

$$
[1 \text{ cm}] = L, \quad [4 \text{ hours}] = T, \quad [400 \text{ lb}] = M.
$$

Note that to find the dimension, we can throw away the number out
front and focus on the unit, asking: what aspect of the system does it
measure?
Other dimensions can be built from these basic dimensions, using
simple algebraic rules.
These are easier to show than to tell.
Area, for example, has dimensions $L^2$:

$$
[1 \text{ cm}^2] = [1 \text{ cm} \times 1 \text{ cm}] = [1 \text{ cm}]
\times [1 \text{ cm}] = L^2.
$$

A more direct way to see this is to use a general result, e.g. the
area of a rectangle:

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
For example, Newton's second law $F = ma$ tells us that if we measure a given force
$F$ on an object whose mass is measured to be $m$, it will accelerate
at a rate $a = F/m$.
It's a very simple observation, but if the two sides of $F = ma$ are
equal, the dimensions must agree.
Sometimes, this observation is enough to *determine* relationships
between measurements!
Since we throw away numbers, dimensional analysis will usually only be
good up to an overall numerical factor.

#### 2.2. Example: spring-mass system <a id="sec-2-2" name="sec-2-2"></a>

Suppose you want to build a spring-driven clock, with time marked off
by the oscillations of a mass stuck to the spring.
When the spring is compressed or extended, you measure the restoring
force $F$ and notice that it is proportional to the displacement $x$
from equilbrium
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

So, if your high school physics lab has springs of stiffness $k = 10^2 \text{
N/m}$ ($100$ Newtons for every meter displaced), then to obtain an
oscillation period of $ t_\text{period} =1$ second, you should attach
a mass

$$
m = \frac{k t_\text{period}^2}{4\pi^2} = \frac{10^2 \text{
kg}}{4\pi^2} \approx 2.5 \text{ kg}.
$$

Woot! We didn't need to analyse any forces, solve a differential
equation, or even deal with numbers.
Dimensional analysis let us skip straight to the answer!

---

1. Using dimensional analysis, show that the angular frequency does
   not depend on the initial displacement $x$ of the mass.

---

#### 2.3. Example: spring-mass system <a id="sec-2-3" name="sec-2-3"></a>

The spring-mass example is neat, but not particularly exciting.

#### 2.4. Usage notes<a id="sec-2-4" name="sec-2-4"></a>

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
