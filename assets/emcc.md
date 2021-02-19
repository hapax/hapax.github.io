---
Layout: post
mathjax: true
comments: true
title:  "Why does <i>E</i> = <i>mc</i>²?"
categories: [Physics, Mathematics, Hacks]
date:  2021-02-19
---

**February 19, 2021.** *A self-contained proof of the most famous
  equation in history. I start with a crash course on special
  relativity, emphasizing the invariance of spacetime lengths, and end
  by considering the relativistic mechanics of an exploding bowling ball.*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Spacetime trigonometry</a>
3. <a href="#sec-3">Time dilation</a>
4. <a href="#sec-4">Velocity addition</a>
5. <a href="#sec-5">Conservation laws</a>
6. <a href="#sec-6">Mass effect</a>
7. <a href="#sec-7">Mass-energy equivalence</a>

#### 1. Introduction <a id="sec-1" name="sec-1"></a>

I recently stumbled across the book "Why does $E = mc^2$?" by Brian
Cox and Jeff Forshaw in a used bookstore.
I realized, to my chagrin, that I didn't know the answer!
As a theoretical physicist, this was somewhat embarrassing.
So, rather than buy the book, I decided I would make it my homework
not only to derive it from what I knew about special relativity, but
to try and write up my reasoning in a self-contained way.
This post is my homework.

A few preliminary comments. First, the exercises are optional, and
mostly designed to connect my somewhat unconventional presentation to
standard treatments.
Second,
[unlike Einstein](https://www.fourmilab.ch/etexts/einstein/E_mc2/e_mc2.pdf),
I have not made any references to the energy of light, and stuck to
one spatial dimension.
This makes the argument longer but more self-contained.
Finally, these notes gave me the opportunity to dust off some old ideas
about how to present the essence of special relativity, which strongly
guided the approach I took, and in particular the restriction to one
spatial dimension.
I found the process enlightening, and hope my mildly eccentric approach can be of benefit to others.

<!-- Before we get cracking, I'll give a TLDR version.
Relativity is basically what you get when you allow space and time to
rotate into each other while keeping the speed of light unchanged.
If I send a clock in the same direction as a light ray, the light ray
appears to travel a shorter distance; the clock must slow down to make
sure the speed is unchanged.
Thus, moving clocks slow down. -->

#### 2. Spacetime trigonometry<a id="sec-2" name="sec-2"></a>

Relativity is really just the bizarro version of trigonometry.
To make this obvious, we'll present Pythagoras' theorem in an odd
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

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/emcc1.png"/>
	</div>
	</figure>

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
(See Exercise 4 for a discussion of what happens if we *only* ask for
invariance of $s^2 = 0$.)
But the implications of (\ref{s2}) are much broader!

---

*Exercise 1 (rotations).* To make the analogy to spacetime more
 convincing, in this exercise we'll describe relative rotations more
 explicitly.
Let's take our original perpendicular rulers $x, y$ and rotate
them clockwise by some angle $\theta$ into new rulers $x', y'$,
 keeping the origin fixed for the moment.
Mark a point a distance $d$ along the $x$ axis.
In the $x', y'$ system, we define functions $\cos(\theta)$ and
 $\sin(\theta)$ by

$$
x' = d\cos (\theta) = x\cos (\theta), \quad \Lambda y' = -d\sin (\theta)
= x\sin (\theta),
$$

where $x$ denotes the $x$-coordinate of the point.

<span style="padding-left: 20px; display:block">
(a) Argue that a point on the $y$ ruler, $d$ marks along, goes to
coordinates
</span>

$$
x' = d\Lambda \sin(\theta) = -y\Lambda \sin(\theta), \quad y' =
d\cos(\theta) = y\cos(\theta).
$$

<span style="padding-left: 20px; display:block">
(b) Use the equations above to show that, if we move the $x, y$ system
around and then rotate by $\theta$, the displacements $\Delta x$ and
$\Delta y$ become
</span>

$$
\begin{align*}
\Delta x' & = \cos(\theta) \Delta x + \sin(\theta) \Lambda \Delta y \\
\Lambda\Delta y' & = -\sin(\theta) \Delta x + \cos(\theta) \Lambda \Delta y.
\end{align*}
$$

<span style="padding-left: 20px; display:block">
(c) Check that
</span>

$$
d^2(\Delta x', \Delta y') = d^2(\Delta x, \Delta y) [\cos^2(\theta) + \sin^2(\theta)].
$$

<span style="padding-left: 20px; display:block">
Pythagoras' theorem is then equivalent to the trigonometric identity
</span>

$$
\cos^2(\theta) + \sin^2(\theta) = 1.
$$

<span style="padding-left: 20px; display:block">
(d) Consider any point on the $y$ ruler, and define $q =\Delta
x'/\Delta y'$.
Verify that
</span>

$$
\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)} =
\frac{q}{\Lambda}.
$$

---

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

*Exercise 2 (length contraction).* This immediately implies a result for moving rulers.

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
(b) The *proper length* $L$ of the ruler is the length measured in the
frame where it is stationary. It can read this off by looking at our
clock.
Using time dilation, show that
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
factorise it (see also Exercise 2):

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

*Exercise 3 (the algebra of addition).* Do the algebra to make $u''$
 the subject in (\ref{add}).

<p align="center">
  ⁂
  </p>

*Exercise 4 (Lorentz transformations).* In this exercise, we will derive something called the
Lorentz transformation. First, we define $\alpha = e^\eta$ for a
"boost parameter" $\eta$. We will also use the hyperbolic functions

$$
\cosh(\eta) = \frac{1}{2}(e^\eta  + e^{-\eta}), \quad \sinh(\eta) =
\frac{1}{2}(e^\eta  - e^{-\eta}), \quad \tanh(\eta) = \frac{\sinh(\eta)}{\cosh(\eta)}.
$$

These play the same role in relativity that the trigonometric
functions $\sin, \cos, \tan$ play in Euclidean geometry, namely,
parameterising transformations which keep length invariant.

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
This is very clearly analogous to the results in Exercise 1!
</span>

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
\Delta x' = \gamma \Delta x + \gamma v \Delta t , \quad
\Delta t' = \left(\frac{\gamma v}{c^2}\right)\Delta x + \gamma\Delta
t. \tag{6} \label{lorentz}
$$

<span style="padding-left: 20px; display:block">
(c) Show that (b) is consistent with the results of (\ref{alpha}),
i.e. both imply $\tanh(\eta) = v/c$.
Explain why this is analogous to part (d) of Exercise 1.
</span>

<p align="center">
  ⁂
  </p>

*Exercise 5 (from light to length).* We've assumed that (\ref{s2}) is invariant
in general, but light obeys $s^2 = 0$.
What if we only require invariance for this special case?
Using our new coordinates $x^\pm$, we can investigate!

<span style="padding-left: 20px; display:block">
(a) Argue that $s^2 = 0$ is invariant if and only if
</span>

$$
\Delta x^\pm \mapsto (\Delta x')^\pm = \alpha_\pm \Delta x^+
$$

<span style="padding-left: 20px; display:block">
for constants $\alpha^\pm$. As above, we'll take these to be positive
for simplicity.
</span>

<span style="padding-left: 20px; display:block">
(b) Show that for some $\alpha, \lambda > 0$, we can always rewrite
</span>

$$
\alpha^+ = \alpha \lambda, \quad \alpha^- = \frac{\lambda}{\alpha}
$$

<span style="padding-left: 20px; display:block">
(c) Argue that the most general transformation preserving $s^2 = 0$
is a Lorentz transformation followed by a *uniform scaling*:
</span>

$$
x \mapsto x' = \lambda x, \quad t \mapsto t' = \lambda t.
$$

<span style="padding-left: 20px; display:block">
(d) Finally, conclude that if we restrict to transformations induced
by relative motion between frames, invariance of the speed of light
implies invariance of $s^2$ for any value. *Hint*. What is the
relative velocity for a pure scaling, i.e. $\alpha = 1$?
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
also the sum of masses of the fragments.
In contrast, kinetic energy need not be conserved, since energy can
change forms, e.g. from kinetic to energy of deformation when the
bowling balls shatter.
We'll return to conservation of energy below.

Let's continue to assume that momentum and mass are conserved in any
frame of reference in special relativity, and see what that implies.
To make things concrete, we'll use the example of an exploding bowling
ball.
Let's start in the rest frame of the bowling ball, where the mass is
$2M_0$ (as measured by stationary scales), and the momentum $P_i = 0$, since the velocity is zero
by definition.
At some point, an explosive device inside the bowling ball detonates,
splitting it into two equal halves of mass $M_0$.
To ensure momentum is conserved, these zoom off with equal and
opposite velocities $\pm u$, so

$$
P_f = M_0u + M_0(-u) = 0 = P_i.
$$

Let's now go to the frame of the part moving left at speed $u$.
Before the explosion, the bowling ball (in this frame of reference)
was moving at speed $u$ to the right, so the momentum was presumably

$$
P'_i = 2M_0u.
$$

After the collision, one half is stationary (we have chosen to go to
its rest frame), and the other moves at a speed given by the velocity
addition formula (\ref{add}):

$$
u' = \frac{2u}{1 + u^2/c^2}. \tag{7} \label{double}
$$

If the second half has mass $M_0$, the momentum after the collision is

$$
P'_f = \frac{2M_0u}{1 + (u/c)^2}.
$$

This is clearly different from the initial momentum $P'_i$ for nonzero $u$!
It looks, naively, as if conservation of mass and momentum are not
consistent with relativity after all.

<!-- 
We said that mass is conserved in any given frame, but we never forbid
it from *changing between frames*! Perhaps, like time and length, the mass of an object can
change when it speeds up.
The formula for $P'$ can be balanced out if the mass *increases*, so
inspired by time dilation, we are going to guess that a mass $m_0$ in
the stationary frame increases as $m = \gamma m_0$ in a moving frame.
Let's see what whether the implications are consistent.
First of all, in the rest frame for the bowling ball, the two halves
zoom off with mass $M$ and at speed $u$.
This means their rest mass $m_0$ is *smaller* than $M$: -->

---

*Exercise 6 (exploding in other frames).* Consider a frame of
 reference in which the unexploded bowling ball moves right at speed
 $v$.

<span style="padding-left: 20px; display:block">
(a) Show that the two exploded halves move with velocities
</span> 

$$
u'_\pm = \frac{v \pm u}{1 \pm uv/c^2}.
$$

<span style="padding-left: 20px; display:block">
(b) If each has mass $M_0$, show that momentum is only
conserved for $u = 0$ or $v = c$.
</span> 

---

#### 6. Mass effect<a id="sec-6" name="sec-6"></a>

But this is a little too quick.
Mass may be conserved *in a frame*, but it need not be invariant
*between frames*.
And we can fix $P'_f$ by increasing the mass.
Inspired by our results for time dilation and length contraction, we
guess that the rest mass $m_0$ (measured in the frame it is
stationary) increases as $m = \gamma m_0$ in a moving frame.
We will check this guess is sensible.
First, note that in the stationary frame of the unexploded bowling
ball, the exploded halves have a rest mass less than $M_0$:

$$
m_0 = \frac{M_0}{\gamma} =
M_0\sqrt{1-\left(\frac{u}{c}\right)^2}. \tag{8} \label{rest}
$$

In the moving frame, the original bowling ball moves at speed $u$, so
its mass is

$$
2M = 2M_0 \gamma,
$$

and hence its momentum is

$$
P'_i = 2M u = 2M_0 \cdot \frac{u}{\sqrt{1+(u/c)^2}}.
$$

After the collision, one half is stationary, while the other half
moves away at speed $u'$ given by (\ref{double}). The associated
Lorentz factor is

$$
\begin{align*}
\gamma' = \frac{1}{\sqrt{1 - (u'/c)^2}} 
& = \left[1 - \frac{4u^2}{c^2(1 + (u/c)^2)^2}\right]^{-1/2} \\
& = \frac{c(1 + (u/c)^2)}{\sqrt{c^2(1 + (u/c)^2)^2 - 4u^2}} \\
& = \frac{1 + (u/c)^2}{\sqrt{(1 - (u/c)^2)^2}} = \frac{1 +
(u/c)^2}{1 - (u/c)^2}.
\end{align*}
$$

The momentum for this second half is therefore

$$
\begin{align*}
P'_f = 2 m_0 \gamma' u' & = 2 M_0 \cdot \frac{\gamma' u'}{\gamma} \\
& = 2M_0 \cdot \frac{1 +
(u/c)^2}{1 - (u/c)^2} \cdot \frac{2u\sqrt{1-(u/c)^2}}{1 + u^2/c^2} \\
& =
2M_0 \cdot \frac{u}{\sqrt{1+(u/c)^2}} = P'_i.
\end{align*}
$$

With this rule, momentum is indeed conserved!
We give a more general argument that $m = \gamma m_0$ and $p = mv$ are
conserved in the next exercise.

---

*Exercise 7 (two-momentum).* 
Suppose a particle of rest mass $m_0$ moves at speed $v$ for proper
time $\Delta \tau$.
The two-velocity $\mathbf{v}$ and two-momentum $\mathbf{p}$ are
vectors [<sup><a id="fnr.3" name="fnr.3" class="footref" href="#fn.3">3</a></sup>]

$$
\mathbf{v} = \frac{1}{\Delta \tau}(\Delta t, \Delta x) , \quad \mathbf{p} = m_0\mathbf{v}.
$$

<span style="padding-left: 20px; display:block">
(a) Show that two-quantities can be written
</span>

$$
\mathbf{v} = (\gamma, \gamma v), \quad \mathbf{p} = (\gamma m_0, \gamma
m_0 v).
$$

<span style="padding-left: 20px; display:block">
(b) Suppose that the two-momenta before and
after a collision are equal:
</span>

$$
\mathbf{p}_i = \mathbf{p}_f.
$$

<span style="padding-left: 20px; display:block">
Argue that, after a Lorentz transformation (\ref{lorentz}) to a new
frame of reference $x', t'$, the two-momentum remains conserved:
</span>

$$
\mathbf{p}'_i = \mathbf{p}'_f.
$$

<span style="padding-left: 20px; display:block">
This means that if relativistic mass $\gamma m_0$ and momentum $\gamma
m_0 v$ are conserved in one frame, they are conserved in any other!
</span>

<span style="padding-left: 20px; display:block">
(c) At low speeds ($v \ll c$), the Lorentz factor $\gamma \approx 1$.
	We also know that at low speeds, Newtonian mechanics is a good
	description, so mass $m_0$ and momentum $m_0v$ are conserved.
	Extrapolate to the conservation of rwo-momentum.
	</span>

---

#### 7. Mass-energy equivalence<a id="sec-7" name="sec-7"></a>

We've motivated the transformation law $m = \gamma m_0$, but we have
yet to explain why $E = mc^2$.
To see why, let's return to the exploding bowling ball in its rest
frame.
Recall from equation (\ref{rest}) that the rest mass of the halves is actually slightly smaller
than $M_0$.
To see what's going on, let's consider the low-speed limit $u \ll c$.
Using the [binomial approximation](https://hapax.github.io/mathematics/physics/hacker/binomial/),
we have

$$
\left[1 - \left(\frac{u}{c}\right)^2\right]^{-1/2} \approx 1 + \frac{u^2}{2c^2}.
$$

Applying this to (\ref{rest}) gives

$$
M_0 = m_0 \left[1 - \left(\frac{u}{c}\right)^2\right]^{-1/2} \approx
m_0 + \frac{1}{2c^2}m_0 u^2.
$$

Remember that $M_0$ is fixed. As $u$ increases, the term on the right
gets bigger, so the rest mass $m_0$ must get smaller.
That's kind of weird!
It's almost as if the mass is getting converted into something else.
If we multiply this equation through by $c^2$, it becomes clearer what
this "something else" is:

$$
M_0c^2  \approx m_0c^2 + \frac{1}{2}m_0 u^2. \tag{9} \label{energy}
$$

The last term is just the classical kinetic energy of the fragment!
So mass appears to be getting converted into kinetic energy.
The maximum amount that can be converted into kinetic energy is
$M_0c^2$, and the leftover energy is $m_0 c^2$.
This suggests that the total energy of the body is $M_0c^2$.
For relativistic mass $m$, we have the most famous equation of all
time:

$$
E = mc^2. \tag{10} \label{emcc1}
$$

Rest mass also has energy content:

$$
E_0 = m_0 c^2. \tag{11} \label{emcc2}
$$

These have slightly different interpretations, but are both avatars of
Einstein's famous equation.
You might wonder why $E = mc^2$ should be interpreted as the *total*
energy, rather than some special form of mass energy.
The answer is simply that, if we interpret it this way, the mysterious
"conservation of mass" we have been dragging around becomes
conservation of total energy!
And unlike kinetic energy, which can get converted into other things,
one of the fundamental principles of physics is that total energy is
conserved.
So everything hangs together nicely!

---

*Exercise 8 (energy-momentum relation).* We end with an equivalent
 form of Einstein's equation

<span style="padding-left: 20px; display:block">
(a) First, show that
</span>

$$
c^2\gamma^2 = \gamma^2 v^2 + c^2. 
$$

<span style="padding-left: 20px; display:block">
(b) Deduce the energy-momentum relation
</span>

$$
E^2 = p^2 c^2 + m_0^2 c^4.
$$

<span style="padding-left: 20px; display:block">
(c) A photon is massless, with $m_0 = 0$. Use the energy-momentum
relation to argue that the energy and momentum are related by
</span>

$$
E = pc.
$$

<span style="padding-left: 20px; display:block">
Maxwell deduced this from classical electromagnetism, but amusingly,
we got there by think about bowling balls!
</span>

---

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum"
href="#fnr.1">Footnote 1</a></sup> <p class="footpara">
Or if you prefer, an orthogonal grid of such rulers.
</p></div>

<div class="footdef"><sup><a id="fn.2" name="fn.2" class="footnum"
href="#fnr.2">Footnote 2</a></sup> <p class="footpara">
Newton's second law can be written $F = \Delta p/\Delta t$, i.e. the
force is just the rate of change of momentum. When force is
zero, so is the momentum change!
</p></div>

<div class="footdef"><sup><a id="fn.3" name="fn.3" class="footnum"
href="#fnr.3">Footnote 3</a></sup> <p class="footpara">
The "two" refers to the total number of spacetime dimensions.
For three dimensions of space and one of time, the corresponding
quantities are called four-velocity and four-momentum.
</p></div>

<!-- This neatly splits the total squared energy into a kinetic part
$(pc)^2$ and a rest energy part $(m_0c^2)^2$.
It also correctly suggests that for light (or any other massless
particle), the total energy and momentum are related by -->
