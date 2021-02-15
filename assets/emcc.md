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
4. <a href="#sec-4">Adding velocities</a>
5. <a href="#sec-5">Conservation laws</a>

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
s^2(\Delta x, \Delta t) = \Delta x^2 - c^2 \Delta t^2 =
\left(\frac{\Delta x^2}{c^2\Delta t^2} - 1\right) c^2\Delta t^2 = -c^2\Delta
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
This implies a result for moving rulers, see <a
href="#sec-A">below</a>.
The relationship also breaks down if $v > c$, so it appears that, for
this spacetime version of Pythagoras to hold, a clock cannot travel
faster than the speed of light.

#### 4. Adding velocities <a id="sec-4" name="sec-4"></a>

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
\mapsto (\Delta x')^- = \frac{1}{\alpha} \Delta x^-,
$$

for some factor $\alpha$. These factors of
$\alpha$ will cancel when we take the product.
We can relate $\alpha$ to $v$ by considering the clock example again.
In its own frame (rulers $x, t$), the clock experiences a proper time
$\Delta \tau$, and hence $\Delta x^\pm = \pm c\Delta \tau$.
In our frame (rulers $x', t'$), the clocks travels a distance $\Delta x'
= v \Delta t' = v\gamma \Delta \tau$.
So $\alpha$ obeys

$$
\alpha^2 = \frac{(\Delta x')^+}{(\Delta x')^-} \cdot \frac{\Delta
x^-}{\Delta x^+} = \frac{(v + c)\gamma \Delta \tau}{(v - c)\gamma
\Delta \tau}\cdot \frac{ -c\Delta\tau}{+c\Delta\tau} =
\frac{c+v}{c-v}. \tag{1} \label{alpha}
$$

We can use (\ref{alpha}) to easily chain multiple changes of frame.
For instance, suppose a rocket moves at speed $v$ to the right in our
frame ($x'', t''$), and launches a clock to the right at speed $u$ in
its frame ($x', t'$).
The clock frame has rulers $x, t$.
At what speed does the clock appear to travel in our frame?
Let's call this speed $u'' = \Delta x''/\Delta t''$.
Then we have

$$
\frac{(\Delta x'')^+}{(\Delta x'')^-} = \frac{\Delta x'' + c\Delta
t''}{\Delta x'' - c\Delta t''} = \frac{u'' + c}{u'' - c}.
$$

But we can also just use (\ref{alpha}) twice:

$$
\frac{(\Delta x'')^+}{(\Delta x'')^-} = \left(\frac{c+v}{c-v}\right)
\frac{(\Delta x')^+}{(\Delta x')^-} = \left(\frac{c+v}{c-v}\right)
\left(\frac{c+u}{c-u}\right) \frac{\Delta x+}{\Delta x^-} = - \left(\frac{c+v}{c-v}\right)
\left(\frac{c+u}{c-u}\right).
$$

Combining these two equations, we find that

$$
\frac{u'' + c}{u'' - c} = \left(\frac{c+v}{c-v}\right) \left(\frac{c+u}{c-u}\right).
$$

After a little algebra, we can isolate $u''$ to find

$$
u'' = \frac{v + u}{1+ uv/c^2}.
$$

This is the famous *velocity addition* formula.
We do not just add $u$ and $v$!

#### 5. Conservation laws<a id="sec-5" name="sec-5"></a>

<!-- https://www.feynmanlectures.caltech.edu/I_16.html -->

#### A. Length contraction <a id="sec-A" name="sec-A"></a>

Suppose a ruler passes us by at speed $v$.
We can deduce its apparent length $L'$ by timing how long it takes
($\Delta \tau$) to pass some specific spot:

$$
L' = v\Delta \tau.
$$

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

#### B. Lorentz transformations <a id="sec-B" name="sec-B"></a>

---

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum"
href="#fnr.1">Footnote 1</a></sup> <p class="footpara">
Or if you prefer, an orthogonal grid of such rulers.
</p></div>

never changes.
In <a href="#sec-B">appendix B</a>, we use this to derive the explicit
form of this change, but we won't need it here.
Instead, consider the moving clock example, which has $\Delta x = 0$,
$\Delta t = \Delta \tau$ in its own frame, but velocity $v = \Delta
x'/\Delta t'$ in ours.
Then the factor $\alpha$ (to go from the clock frame to our frame)
satisfies

$$
\alpha^2 = \frac{(\Delta x')^+}{(\Delta x')^-} = \frac{\Delta x' +
c\Delta t'}{\Delta x' - c\Delta t'} = \frac{v+c}{v-c}
$$

where the last term follows from dividing top and bottom by $\Delta t'$.
We can use this to derive the curious *velocity addition* formula.
Suppose we observe a rocket moving to the right at
speed $v$, and then that rocket fires a small probe at speed $u'$ to
the right in its frame of reference.
What is the probe speed, $u$, as measured in our frame?
Let's call our rulers $x, t$, the rocket's rulers $x', t'$, and the 

-mu', mu'

u_1 = (v + u')/(1 - u'v/c^2)
u_2 = (v - u')/(1 + u'v/c^2)

(c-u_1)/(c + u_1) = (c - u')(c - v)/(c + u')(c + v)
(c-u_2)/(c + u_2) = (c + u')(c - v)/(c - u')(c + v)
= [(c- u')/(c + u')]^2(c-u_1)/(c + u_1)
