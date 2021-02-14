---
Layout: post
mathjax: true
comments: true
title:  "Why does <i>E</i> = <i>mc</i>²?"
categories: [Physics, Hacks]
date:  2021-02-13
---

**February 13, 2021.** *A*

#### Introduction

Relativity is really just the bizarro version of trigonometry.

#### A Pythagorean prelude

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
obeying a "spacetime Pythagoras' theorem" which means that $s^2$ does
not change even when we speed up or slow down.
In particular, $s^2 = 0$ for a light ray whatever speed we measure at,
and hence the speed of light is always $c$.

#### Dilation and contraction

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

This immediately implies a result for moving rulers.
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
\gamma L'.
$$

Thus, the apparent length $L'$ is *shorter* than the proper length $L$ by
a factor $\gamma$.
This shortening is called *length contraction*.

---

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum"
href="#fnr.1">Footnote 1</a></sup> <p class="footpara">
Or if you prefer, an orthogonal grid of such rulers.
</p></div>
