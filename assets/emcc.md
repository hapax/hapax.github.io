---
Layout: post
mathjax: true
comments: true
title:  "Why does <i>E</i> = <i>mc</i>²?"
categories: [Physics, Hacks]
date:  2021-02-13
---

**February 13, 2021.** *A*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">A Pythagorean parallel</a>
3. <a href="#sec-3">Dilation and contraction</a>
4. <a href="#sec-3">Momentum</a>

#### 1. Introduction <a id="sec-1" name="sec-1"></a>

Relativity is really just the bizarro version of trigonometry.

#### 2. A Pythagorean parallel <a id="sec-2" name="sec-2"></a>

We start by presenting Pythagoras' theorem in a
slightly odd way.
Suppose we have rulers, $x$ and $y$, oriented at right angles
[<sup><a id="fnr.1" name="fnr.1" class="footref" href="#fn.1">1</a></sup>],
and which both have evenly spaced marks.
An $x$-division need not equal a $y$-division, and in general will
correspond to $\Lambda$ units of $y$.
We can measure lengths, say of a plank of wood, in this system, by
simply recording the number of marks it takes up on ruler $x$, call it
$\Delta x$, and the number of marks taken up on $y$, called $\Delta
y$.
Pythagoras’ theorem means that, however we choose to orient the plank
of wood or the rulers themselves, we always find

$$
d^2(\Delta x, \Delta y) = \Delta x^2 + \Lambda^2 \Delta y^2 = L^2,
$$

for some fixed number $L$, depending only on the piece of wood we've
chosen to measure.
It seems reasonable to define $L$ as its length.
But even more importantly, the quantity $d^2$ is *invariant* under a
change in relative orientation.

Relativity parallels this setup closely.
Michelson and Morley's
[famous experiment](https://en.wikipedia.org/wiki/Michelson%E2%80%93Morley_experiment)
in 1887 suggested that the speed of light does not depend on how fast
you are going when you measure it.
Einstein arrived at the same conclusion by thinking long and hard
about electrodynamics.
To measure the speed of light, we use two rulers, $x$ and $t$, though
the latter is usually called a "clock".
The light travels between two points a distance $\Delta x$ apart in
time $\Delta t$, so the speed is $c = \Delta x/\Delta t$.
We can rewrite this suggestively as

$$
s^2(\Delta x, \Delta t) = \Delta x^2 - c^2 \Delta t^2 = 0.
$$

The analogy is hopefully clear.
The ratio between units of $x$ and units of $t$ is given by $c$.
The expression $s^2(\Delta x, \Delta t)$ defines a "spacetime length",
obeying a spacetime version of Pythagoras' theorem, namely that the
$s^2$ distance between events does not change even when we speed up or
slow down.
In particular, $s^2 = 0$ for the measurements defining a light ray
whatever speed *we* are moving, and hence light always travels with
velocity $c$.

#### 3. Dilation and contraction <a id="sec-3" name="sec-3"></a>

We can use the invariance of $s^2$ to quickly deduce that time dilates
and length contracts.
Consider a clock which ticks out time $\tau$ in its own frame of
reference, i.e. where it is stationary.
We call this the *proper time*.
For a proper time interval $\Delta \tau$, the clock moves nowhere
($\Delta x= 0$), so
the spacetime length is

$$
s^2(0, \Delta \tau) = -c^2 \Delta \tau^2.
$$

If the clock moves at speed $v$ in our reference frame, then in time
$\Delta t$ (as measured by our clock), it moves a distance $\Delta x =
v \Delta t$.
Thus, the spacetime length is

$$
s^2(\Delta x, \Delta t) = \Delta x^2 - c^2 \Delta t^2 = -c^2\Delta
t^2\left(1 - \frac{v^2}{c^2}\right).
$$

But since the spacetime length is invariant, we have

$$
-c^2 \Delta \tau^2 = -c^2\Delta t^2\left(1 - \frac{v^2}{c^2}\right)
\quad \Longrightarrow \quad \frac{\Delta t}{\Delta \tau} =
\frac{1}{\sqrt{1-(v/c)^2}} = \gamma,
$$

where we have defined the all-important *Lorentz factor* $\gamma$.
Note that $\gamma \geq 1$, so that less proper time ($\Delta \tau$)
passes for the clock than elapsed time ($\Delta t$) measured in our reference frame.
Thus, the moving clock appears to slow down, a phenomenon called *time
dilation*.
This implies a result for moving rulers, see <a href="#sec-A">below</a>.

#### 4. Momentum <a id="sec-4" name="sec-4"></a>

The

#### A. Length contraction <a id="sec-A" name="sec-A"></a>

Suppose a ruler passes us by at speed $v$.
We can deduce its apparent length $L'$ by timing how long it takes
($\Delta \tau$) to pass some specific spot:

$$
L' = v\Delta \tau.
$$

I've used $\Delta \tau$ since the clock is stationary in our frame.
The length $L$ of the ruler in its own frame of reference is called
the *proper length*, and it can be calculated by timing how long
($\Delta t$) our clock takes to pass from one end to the other:

$$
L = v \Delta t = v \Delta \tau \cdot \frac{\Delta t}{\Delta \tau} =
\gamma L',
$$

using time dilation to relate $\Delta \tau$ to $\Delta t$.
Thus, the apparent length $L'$ is *shorter* than the proper length $L$ by
the Lorentz factor $\gamma$.
This shortening is called *length contraction*.

---

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum"
href="#fnr.1">Footnote 1</a></sup> <p class="footpara">
Or if you prefer, an orthogonal grid of such rulers.
</p></div>
