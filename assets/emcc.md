---
Layout: post
mathjax: true
comments: true
title:  "Why does <i>E</i> = <i>mc</i>²?"
categories: [Physics, Mathematics, Hacks]
date:  2021-02-18
---

**February 18, 2021.** *A self-contained proof of the most famous
  equation in history.*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Spacetime trigonometry</a>
3. <a href="#sec-3">Time dilation</a>
4. <a href="#sec-4">Velocity addition</a>
5. <a href="#sec-5">Conservation laws</a>
6. <a href="#sec-6">The exploding bowling ball</a>

#### 1. Introduction <a id="sec-1" name="sec-1"></a>

#### 2. Spacetime trigonometry<a id="sec-2" name="sec-2"></a>

Relativity is really just the bizarro version of trigonometry.
To make this obvious, we'll present Pythagoras' theorem in a weird
way.
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
More precisely,

$$
s^2(\Delta x, \Delta t) = \Delta x^2 - c^2 \Delta t^2 =
\text{constant}, \tag{1} \label{s2}
$$

when $\Delta x$ and $\Delta t$ are the space and time separation of
any two events, as measured by an observer at constant speed.
As a special case, $s^2 = 0$ for a light ray travelling from $A$ to
$B$, whatever speed *we* are moving.
Hence, light always travels with velocity $c$.
But the implications of (\ref{s2}) are much broader!

#### 3. Time dilation <a id="sec-3" name="sec-3"></a>

We can use (\ref{s2}) to quickly deduce that time dilates
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
s^2(\Delta x, \Delta t) = \Delta x^2 - c^2 \Delta t^2 =
\left(\frac{\Delta x^2}{c^2\Delta t^2} - 1\right) c^2\Delta t^2 = -c^2\Delta
t^2\left(1 - \frac{v^2}{c^2}\right).
$$

But since the spacetime length is invariant, we have

$$
-c^2 \Delta \tau^2 = -c^2\Delta t^2\left(1 - \frac{v^2}{c^2}\right)
\quad \Longrightarrow \quad \frac{\Delta t}{\Delta \tau} =
\frac{1}{\sqrt{1-(v/c)^2}} = \gamma, \tag{2} \label{gamma}
$$

where we have defined the all-important *Lorentz factor* $\gamma$.
Note that $\gamma \geq 1$, so that less proper time ($\Delta \tau$)
passes for the clock than elapsed time ($\Delta t$) measured in our reference frame.
Thus, the moving clock appears to slow down, a phenomenon called *time
dilation*.
The relationship also breaks down if $v > c$, so it appears that, for
this spacetime version of Pythagoras to hold, a clock cannot travel
faster than the speed of light.

---

*Exercise 1 (length contraction).* This immediately implies a result for moving rulers.

<span style="padding-left: 20px; display:block">
(a) Suppose a ruler passes us by at speed $v$.
We can deduce its apparent length $L'$ by timing how long it takes
($\Delta \tau$) to pass some specific spot.
 Show this length is
</span>

$$
L' = v\Delta \tau
$$

<span style="padding-left: 20px; display:block">
where $\Delta \tau$ refers to the clock which is stationary in our frame.
</span>

<span style="padding-left: 20px; display:block">
(b) Using time dilation, show that the *proper length* $L$ of the
ruler, as measured in its frame, is
</span>

$$
L = \gamma L'.
$$

Thus, a moving ruler shrinks by a factor $\gamma$ in our
frame. This is called *length contraction*.

---


#### 4. Velocity addition <a id="sec-4" name="sec-4"></a>

There is a cute way to understand how measurements change when we
speed up or slow down.
Since the spacetime length is a difference of squares, we can
factorise it:

$$
s^2(\Delta x, \Delta t) = \Delta x^2 - c^2 \Delta t^2 = (\Delta x + c
\Delta t) (\Delta x - c \Delta t) = \Delta x^+ \Delta x^-,
$$

where $x^\pm$ represents the "combined rulers" $x \pm ct$.
Then $s^2$ will be invariant under changes of velocity provided that,
in a new frame of reference with rulers $x', t'$, we have

$$
\Delta x^+ \mapsto (\Delta x')^+ = \alpha \Delta x^+, \quad \Delta x^-
\mapsto (\Delta x')^- = \frac{1}{\alpha}\Delta x^-, \tag{3} \label{boost}
$$

for some factor $\alpha$.
To connect $\alpha$ to the relative velocity, we consider the moving clock experiment.
Remember that in the clock frame $\Delta x = 0$ and $\Delta t = \Delta \tau$, but in
our frame, $\Delta t' = \gamma
\Delta \tau$ and $\Delta x' = v \Delta t' = v\gamma
\Delta \tau$.
Thus, we have
<!-- These factors will cancel when we take
the product, so $s^2$ will indeed be invariant.
We can relate $e^{\eta}$ to $v$ by considering the clock example again.
In its own frame (rulers $x, t$), the clock moves nowhere ($\Delta x
= 0$) in $\Delta t = \Delta \tau$ tocks.
Hence, $\Delta x^\pm = \pm c\Delta \tau$.
In our frame (rulers $x', t'$), the clocks tocks over a period $\Delta t' = \gamma
\Delta \tau$, and travels a distance $\Delta x' = v \Delta t' = v\gamma
\Delta \tau$ while it does so.
So $e^\eta$ obeys -->

$$
\alpha^{2} = \frac{(\Delta x')^+}{(\Delta x')^-} \cdot \frac{\Delta
x^-}{\Delta x^+} = \frac{\Delta x' + c\Delta t'}{\Delta x' - c\Delta t'}\cdot \frac{ -c\Delta\tau}{+c\Delta\tau} = \frac{(v + c)\gamma \Delta \tau}{(v - c)\gamma
\Delta \tau} \cdot (-1) =
\frac{c+v}{c-v}. \tag{4} \label{alpha}
$$

We can use this equation to chain together multiple changes of frame.
For instance, suppose a rocket moving at speed $v$ in our frame ($x'', t''$) launches a
clock at speed $u$ in its frame ($x', t'$).
<!-- For instance, suppose a rocket moves at speed $v$ to the right in our
frame ($x'', t''$), and launches a clock to the right at speed $u$ in
its frame ($x', t'$).
The clock frame has rulers $x, t$.
At what speed does the clock appear to travel in our frame?
Let's call this speed $u'' = \Delta x''/\Delta t''$. -->
The speed of the clock in our frame is $u'' = \Delta x''/\Delta t''$,
and obeys

$$
\frac{(\Delta x'')^+}{(\Delta x'')^-} = \frac{\Delta x'' + c\Delta
t''}{\Delta x'' - c\Delta t''} = \frac{u'' + c}{u'' - c}.
$$

But we can also just use (\ref{alpha}) twice:

$$
\frac{(\Delta x'')^+}{(\Delta x'')^-} = \left(\frac{c+v}{c-v}\right)
\frac{(\Delta x')^+}{(\Delta x')^-} = \left(\frac{c+v}{c-v}\right)
\left(\frac{c+u}{c-u}\right) \frac{\Delta x^+}{\Delta x^-} = - \left(\frac{c+v}{c-v}\right)
\left(\frac{c+u}{c-u}\right).
$$

Combining the last two equations, we find

$$
\frac{u'' + c}{u'' - c} = \left(\frac{c+v}{c-v}\right)
\left(\frac{c+u}{c-u}\right) \quad \Longrightarrow \quad u'' = \frac{v + u}{1+ uv/c^2}, \tag{5} \label{add}
$$

after some algebra to isolate $u''$. This is the famous velocity addition formula!

---

*Exercise 2 (the algebra of addition).* Do the algebra to isolate $u''$ in (\ref{add}).

<p align="center">
  ⁂
  </p>

*Exercise 3 (Lorentz transformations).* In this exercise, we will derive something called the
Lorentz transformation. First, we define $\alpha = e^\eta$ for a
"boost parameter" $\eta$. We will also use the hyperbolic functions

$$
\cosh(\eta) = \frac{1}{2}(e^\eta  + e^{-\eta}), \quad \sinh(\eta) =
\frac{1}{2}(e^\eta  - e^{-\eta}), \quad \tanh(\eta) = \frac{\sinh(\eta)}{\cosh(\eta)}.
$$

These play the same role in relativity that the trigonometric
functions $\sin, \cos, \tan$ play in Euclidean geometry, namely,
parameterising the transformations which keep $s^2$ invariant.

<span style="padding-left: 20px; display:block">
(a) Suppose two events are separated by $\Delta x,
\Delta t$ in the $x, t$ frame. Using (\ref{boost}), show that in the
$x', t'$ frame, they are separated by
</span>

$$
\begin{align*}
\Delta x' & = \cosh(\eta) \Delta x + \sinh(\eta) c \Delta t \\
c\Delta t' & = \sinh(\eta) \Delta x + \cosh(\eta) c \Delta t.
\end{align*}
$$

<span style="padding-left: 20px; display:block">
(b) From the clock example (or otherwise), argue that
</span>

$$
\cosh(\eta) = \gamma, \quad \sinh(\eta) = \frac{\gamma v}{c}.
$$

<span style="padding-left: 20px; display:block">
Inserting these into (a) gives the standard form of the Lorentz
transformation:
</span>

$$
\begin{align*}
\Delta x' & = \gamma \Delta x + \gamma v \Delta t \\
\Delta t' & = \left(\frac{\gamma v}{c^2}\right)\Delta x + \gamma\Delta t.
\end{align*}
$$

<span style="padding-left: 20px; display:block">
(c) Show that (b) is consistent with the results of (\ref{alpha}),
i.e. both imply $\tanh(\eta) = v/c$.
</span>

---

#### 5. Conservation laws<a id="sec-5" name="sec-5"></a>

So far, we haven't really done any physics, just bizarro trigonometry.
Let's rectify that and introduce some ideas from Newtonian mechanics.
Suppose a bowling ball of mass $m$ and speed $v$.
Two ways to quantify its motion are *momentum* $p$, and the *kinetic
energy* $K$:

$$
p = mv, \quad K = \frac{1}{2}mv^2.
$$

A consequence of Newton's laws
[<sup><a id="fnr.2" name="fnr.2" class="footref" href="#fn.2">2</a></sup>]
is that if the force on a collection of bowling balls is zero, the
total momentum cannot change even if they collide.
We say that momentum is *conserved*.
So if one bowling ball ($m_1, v_1$) collides with another ($m_2,
v_2$), the combined momentum is the same before and afterwards:

$$
P = p_1 + p_2 = m_1 v_1 + m_2 v_2.
$$

A sneakier conserved quantity is *mass*.
We usually assume $m_1$ and $m_2$ remain fixed, but if the bowling
balls shatter into parts, not only is the total $P$ conserved, but
also the sum of masses.
In contrast, kinetic energy need not be conserved, since energy can
change forms, e.g. from kinetic to energy of deformation when the
bowling balls shatter.
We'll continue to assume that momentum and mass are conserved in any
frame of reference in special relativity, and see what that implies.

#### 6. The exploding bowling ball<a id="sec-6" name="sec-6"></a>

To make things concrete, we'll use the example of an exploding bowling
ball.
We'll start in the rest frame of the bowling ball, where the mass is
$2M_0$, and the momentum $P_\text{rest} = 0$, since the velocity is zero
by definition.
At some point, an explosive device inside the bowling ball detonates,
splitting it into two equal halves of mass $M_0$.
To ensure momentum is conserved, these must zoom off with equal and
opposite velocities:

$$
P_\text{rest} = 0 = M_0u - M_0u.
$$

Let's now go to the frame of the part moving left at speed $u$.
Before the explosion, the bowling ball (in this frame of reference)
was moving at speed $u$ to the right, so the momentum was presumably

$$
P = 2M_0u.
$$

After the collision, one half is stationary (we have chosen to go to
its rest frame), and the other moves at a speed given by the velocity
addition formula (\ref{add}):

$$
v = \frac{2u}{1 + u^2/c^2}. \tag{6} \label{double}
$$

If the second half has mass $M$, the momentum after the collision is

$$
P' = \frac{2M_0u}{1 + (u/c)^2}.
$$

This is clearly different from $P$!
It looks, naively, as if conservation of mass and momentum are not
consistent with relativity after all.
But this is a little too quick.
We said that mass is conserved in any given frame, but *not* that it
is invariant! Perhaps, like time and length, the mass of an object can
change when it speeds up.

Looking at the formula for $P''$, we see that if the mass *increases*
by a factor of $1 + (u/c)^2$, then it will equal $P'$.
But since $P'$ involves a moving mass, that should probably change
too.
So, guided by our clock example, we are simply going to guess that a
mass $M_0$ in its rest frame increases as $M = \gamma M_0$ when it
starts moving.
This means that, before the explosion, in the moving frame the bowling
ball had momentum

$$
P = 2\gamma M_0 u = \frac{2u}{\sqrt{1-(u/c)^2}} \cdot M_0.
$$

After the collision, one half is stationary, while the other half
moves away at speed $v$ given by (\ref{double}). The associated
Lorentz factor is

$$
\begin{align*}
\gamma' & = \frac{1}{\sqrt{1 - (v/c)^2}} \\
& = \left[1 - \frac{4u^2}{c^2(1 + (u/c)^2)^2}\right]^{-1/2} \\
& = \frac{c(1 + (u/c)^2)}{\sqrt{c^2(1 + (u/c)^2)^2 - 4u^2}} \\
& = \frac{1 + (u/c)^2}{\sqrt{(1 - (u/c)^2)^2}} = \frac{1 +
(u/c)^2}{1 - (u/c)^2}.
\end{align*}
$$

#### Conclusion

---

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum"
href="#fnr.1">Footnote 1</a></sup> <p class="footpara">
Or if you prefer, an orthogonal grid of such rulers.
</p></div>

<div class="footdef"><sup><a id="fn.2" name="fn.2" class="footnum"
href="#fnr.2">Footnote 2</a></sup> <p class="footpara">
Newton's second law can be written $F = \Delta p/\Delta t$, i.e. the
force is just the change in momentum with time. When force is
zero, so is the momentum change!
</p></div>

The last leg of our journey will take us to Newtonian mechanics, and
*conservation laws* in particular.
One way to characterise things bumping into each other is the
momentum, $p = mv$.
Newton's second law says this for a collection of particles not
subject to a force, the momentum cannot change, so in particles,
momentum is conserved by particle collisions unless some force acts
from outside.
As a simple example, suppose a stationary particle of mass $2m$ splits
into two equal halves of mass $m$.
Since the initial momentum is zero, so is the final momentum, with

$$
p_0 = 0 = p_1 + p_2, \quad p_1 = mu, \quad p_2 = -mu,
$$

i.e. one half speeds off to the right at speed $u$, the other to the
left at $-u$.
In special relativity, this is still true, at least in the frame where the initial particle is at rest.
But now suppose that, from our perspective, the initial particle is
already moving to the right at speed when it decays.
Naively, it seems like it should have momentum $p_0' = 2mv$, and the from the
addition formula (\ref{add}), the two halves will have momenta

$$
p_1' = mu_1' = \frac{m(v + u)}{1+ uv/c^2}, \quad p_2' = mu_2' = \frac{m(v - u)}{1- uv/c^2}.
$$

It's clear that, in general, $p_0' \neq p_1' + p_2'$, since

$$
p_1' + p_2' = \frac{m(v + u)}{1+ uv/c^2} + \frac{m(v + u)}{1- uv/c^2}
= \frac{2m(u + v)}{1 - u^2 v^2/c^4}.
$$

This only equals $p_0' = 2mv$ when $u = 0$.
So, what gives? Has conservation of momentum failed?
The issue is actually subtler.
In the same way that time and length depend on which reference frame
they are measured in, so does mass itself!
Although momentum and mass are conserved *within frames*, they are not
invariant *between frames*.
So, suppose that in the moving frame, the particle has mass $2m'$
before it splits.
After decay, we assume that mass is conserved, with

$$
2m' = m_1 + m_2,
$$

and momentum is conserved, so

$$
p_0' = 2m' v = m_1u_1' + m_2u_2'.
$$

This may seem tricky, but in fact, it is easily solved by taking
$m_1u_1' = m_2u_2' = m'v$.
This implies

$$
m_1u_1' = \frac{m_1(v + u)}{1+ uv/c^2} = m'v \quad \Longrightarrow
\quad m_1 = \frac{m'(1+ uv/c^2)}{(1 + u/v)},
$$

and a similar result for $m_2$.
This seems unhelpful, but there is an elegant way of rewrite this:

$$
\gamma_1 = \frac{1}{\sqrt{1-(u_1')^2/c^2}} = \frac{1 + uv/c^2}{\sqrt{(1-(u/c)^2)(1-(v/c)^2)}}
$$

<!-- https://www.feynmanlectures.caltech.edu/I_16.html -->


To understand how $x$ and $t$ change (rather than $x^\pm$), note that

$$
\Delta x = \frac{1}{2}\Delta x^+ + \frac{1}{2}\Delta x^-, \quad c\Delta
t = \frac{1}{2}\Delta x^+ - \frac{1}{2}\Delta x^-.
$$

Hence,

$$
\begin{align*}
\Delta x' & = \frac{1}{2}(\Delta x')^+ + \frac{1}{2}(\Delta x')^- \\
& = \frac{e^\eta}{2}\Delta x^+ + \frac{e^{-\eta}}{2}\Delta
	x^- \\
	& = \frac{1}{2}(e^\eta + e^{-\eta})\Delta x +
	\frac{1}{2}(e^\eta - e^{-\eta})\Delta t \\
	& = \cosh(\eta) \Delta x + \sinh(\eta) c\Delta t,
\end{align*}
$$

where $\cosh(\eta) = (e^\eta + e^{-\eta})/2$ and $\sinh(\eta) =
(e^\eta - e^{-\eta})/2$.
Similarly,

$$
c\Delta t' = \sinh(\eta) \Delta x + \cosh(\eta) c\Delta t.
$$

These are called *Lorentz transformations*.
We can easily relate $\eta$ to $v$ using our clock example.
In its rest frame, the ticking clock travels a distance $\Delta x = 0$
over $\Delta t = \Delta \tau$ tocks.
In our frame, with rulers $x', t'$, those same tocks take time $\Delta
t' = \gamma \Delta t$, over which it travels a distance $v\Delta
t'$.
Hence,

$$
c\Delta t' = \gamma c \Delta t = \sinh(\eta) \Delta x + \cosh(\eta) c\Delta t \quad \Longrightarrow \quad \cosh(\eta) = \gamma,
$$

and similarly

$$
\sinh(\eta) = \frac{\gamma
v}{c}.
$$

---


I've used $\Delta \tau$ since the clock is stationary in our frame.
The length $L$ of the ruler in its own frame of reference is called
the *proper length*.
From the ruler's perspective, this is calculated by timing how long it
takes ($\Delta t$) our clock takes to pass from one end to the other.
But the two elapsed times are related by time dilation!
It follows that

$$
L = v \Delta t = v \Delta \tau \cdot \frac{\Delta t}{\Delta \tau} =
\gamma L'.
$$

Thus, the apparent length $L'$ is *shorter* than the proper length $L$ by
the Lorentz factor $\gamma$.
This shortening is called *length contraction*.

By itself, this isn't enough to determine what happens to the bowling
balls after the collision, since there are many ways to conserve $P$.
We need another constraint!
In elementary physics classes, we often consider "elastic" collisions
where kinetic energy is conserved. This is not necessary in general,
since energy can be converted from one form (like kinetic) into
another (like thermal).
We are going to go in a slightly different direction, and consider a
sneaky conservation law which is not usually stated: *conservation of mass*.
