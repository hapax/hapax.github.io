---
Layout: post
mathjax: true
comments: true
title:  "The physics of sneezes"
categories: Physics
date:  2020-07-07
---

**July 7, 2020.** *The physics of sneezing and aeorosols is
  fascinating and particularly timely given concerns around physical
  distancing guidelines for COVID. Here, we explore a few simple (and
  medically unsound) models to get a feel for the problem.*

#### Ballistic droplets

When you sneeze, you eject a range of particles at a range of
speeds.
To start with, we will consider the simple case of *ballistic
droplets*, where droplets are subject only to gravity.
Suppose your mouth is at height $h$ above the ground.
The time it takes for a droplet to fall to the ground $t_\text{G}$ under the
influence of gravity is given by

$$
h = \frac{1}{2}gt_\text{G}^2 \quad \Longrightarrow \quad t_\text{G} = \sqrt{\frac{2h}{g}}.
$$

The *range* is the horizontal distance covered in this time.
If you impart speed $v_0$ to the droplet, then the range $R$ is

$$
R = v_0t_\text{G} = v_0 \sqrt{\frac{2h}{g}}.
$$

Let's plug in some numbers and see if the range is reasonable.
Droplets can be emitted at speeds of up to $v_0 = 100 \text{ m/s}$.
A reasonable height is $h \approx 2 \text{m}$, and $g = 9.8 \text{
m/s}^2$.
So we get a range of

$$
R = 100 \sqrt{\frac{2 \cdot 2}{9.8}} \text{ m} \approx 50 \text{ m}.
$$

This is obviously much too large! It gets even worse if we change the
firing angle.

---

**Exercise 1.** (a) Show that if fired at an angle $\theta$ to the
horizontal, then the droplet reaches the top of the parabolic arc at
time

$$
t_\text{top} = \frac{v_0\sin\theta}{g}.
$$

(b) Show that, for angle $\theta$, the time it takes for the droplet
to fall is

$$
t_\text{G} = t_\text{top} + \sqrt{\frac{2h}{g} + t_\text{top}^2}.
$$

(c) Finally, give an expression for the range $R$.

(d) How far does a ballistic droplet travel for $\theta = 45^\circ$?
Use $v = 100 \text{ m/s}$ and $h = 2\text{ m}$.

<!-- 140 m! -->

---

#### Stokes' law

Obviously, we've missed something big. The WHO is not instructing us
to stay $50$ m away from one another!
In reality, droplets are subject to *air resistance*.
This is a force directed against motion, and which increases with
velocity.
In the simplest case, the force is directly proportional to the
velocity:

$$
\mathbf{F}_\text{drag} = -\gamma \mathbf{v}.
$$

Solving the problem in two dimensions is a little tricky, so I will
use a very rough approximation, and see how far it moves in one
dimension, but in the time $t_\text{G}$ we discussed in the last
section.
Newton's second law is

$$
m \dot{v} = F_\text{drag} = -\gamma v.
$$

We can solve immediately using an exponential,

$$
v(t) = v_0 e^{-\gamma t/ m}.
$$

To find the position at time $t = t_\text{G}$, we have to
integrate once:

$$
x(t_\text{G}) = \int_0^{t_\text{G}} dt \, v(t) = v_0 \int_0^{t_\text{G}} dt
\, e^{-\gamma t/ m} = \frac{mv_0}{\gamma} \left(1 - e^{-\gamma t_\text{G}/m}\right).
$$

The particle slows down exponentially and gradually approaches the
maximum distance of $mv_0/\gamma$.
Let's plug in some numbers and see what this maximum distance is.
To find $m$, we need to know that droplets are mostly water, with
density $ \rho_\text{water} \approx 10^3 \text{ kg/m}^3$ and have
typical size $2r \sim 100 \,\mu\text{m}$, with mass

$$
m = \rho_\text{water} \cdot \frac{4\pi}{3}r^3 \approx 5.2 \times 10^{-10} \text{ kg}.
$$

Finally, we need to find $\gamma$.
This is the trickiest part.
For a slowly moving droplet, the drag is given by *Stokes' law*:

$$
\gamma = 6\pi \eta r \approx 1.7 \times 10^{-8} \text{ kg/s},
$$

where $\eta = 1.8\times 10^{-5} \text{ kg/m s}$ is the viscosity of
air and $r$ the droplet radius.
This gives a maximum distance of

$$
x_\text{max} = \frac{m v_0}{\gamma} \approx \frac{(5.2 \times 10^{-10})
100}{(1.7 \times 10^{-8}) } \text{ m} \approx 3 \text{ m}.
$$

This looks much better!
If we plug in the time to ground from the previous section,
$t_\text{G} = \sqrt{2h/g} \approx 0.6 \text{ s}$, we get more or less
the same answer.
This is still a bit larger than the WHO recommendations.
You can see in the next problem that solving in two dimensions gives
the same maximum distance.

---

**Exercise 2.** Let's solve the problem in two dimensions, and include a
nonzero firing angle for the heck of it.
The velocity is denoted $\mathbf{v} = (v_x, v_y)$, with $\mathbf{v}_0
= v_0 (\cos\theta, \sin\theta)$.
The equation of motion is

$$
m \dot{\mathbf{v}} = -mh \hat{\mathbf{y}} - \gamma \mathbf{v}.
$$

(a) Separate into $x$ and $y$ components. Solve for $v_x$, and show
that

$$
v_x(t) = v_0 \cos\theta e^{-\gamma t/mg}.
$$

(b) Similarly, show that

$$
v_y(t) = v_0\sin\theta e^{-\gamma t/mg} - \frac{mg}{\gamma}\left(1 - e^{-\gamma t/mg}\right).
$$

(c) Integrate your result from part (a) to find

$$
x(t) = \frac{m v_0 \cos\theta}{\gamma} (1 - e^{-\gamma t/mg}).
$$

Thus, although the time dependence is different, the maximum distance
is the same as the one-dimensional case.
Incidentally, this maximum distance is largest for a horizontally
fired droplet, unlike pure ballistic motion.

---

#### Reynolds number and quadratic drag

Our answer is a wee bit too big, so perhaps something was wrong with
our drag force.
In fact, to use Stokes' law, the droplet needs to be moving slowly.
When it moves fast, however, there is a different physics at play, and
the drag is *quadratic* in $v$.
To tell the difference, we have to quantify whether the fluid feels
*sticky* (linear drag) or *bumpy* (quadratic drag) to the droplet.
The *Reynolds number* is the ratio of bumpiness to stickiness.
It is defined as the ratio

$$
\text{Re} = \frac{\rho v D}{\mu}.
$$

where $D = 2r$ is the diameter of the droplet.
When $\text{Re}  < 1$, Stokes' law applies, but otherwise we should
use quadratic drag.
Air has density around $1.2 \text{ kg/m}^3$, and we introduced the
numbers in the preceding section.
Plugging them in gives

$$
\text{Re} = \frac{\rho v D}{\mu} = \frac{1.2 \cdot 100 \cdot
10^{-4}}{1.8 \times 10^{-5}} \approx 700.
$$

Stokes' law is definitely not valid!
We should be using the quadratic form for the drag force,

$$
\mathbf{F}_\text{drag} = - \alpha v^2 \hat{\mathbf{v}},
$$

To simplify, let's solve the toy one-dimensional version of the problem.
The equation of motion is

$$
F_\text{drag} = m\dot{v} = - \alpha v^2.
$$

This is easily solved by separation of variables:

$$
-\frac{dv}{v^2 } = \frac{\alpha}{m} dt \quad \Longrightarrow \quad
v(t) = \frac{m}{\alpha t + mv_0^{-1}}.
$$

Integrating gives a log:

$$
x(t) = \int_0^{t} dt' \, v(t') =
\frac{m}{\alpha}\log\left[1 + \frac{\alpha v_0 t}{m}\right].
$$

It seems there is no longer any maximum distance!
This is because $v^2$ shrinks *faster* than $v$ at small $v$, so that
at slow speeds the droplet experiences much less drag.
Finally, $\alpha$ is to a good approximation given by

$$
\alpha \approx \frac{1}{2}\rho A = \frac{1}{2}\pi \rho r^2,
$$

where $\rho$ is the density of air.
(In fact, there is dimensionless *drag coefficient* sitting out front
of this which depends on the Reynolds number, but we'll ignore it.)

#### Linear and quadratic drag

Of course, there *is* a maximum distance --- once the particle slows
down enough, the linear drag begins to dominate!
This will happen around $\text{Re} = 1$, or

$$
\text{Re} = \frac{2\rho v_\text{L} r}{\mu} = 1 \quad \Longrightarrow \quad v_\text{L} =
\frac{\mu}{2\rho r} \approx 0.15 \text{ m/s}.
$$

We can find the time $t_\text{L}$ at which this happens using our equation for
velocity in the quadratic drag regime:

$$
v(t_\text{L}) = \frac{m}{\alpha t_\text{L} + mv_0^{-1}} = v_\text{L} \quad
\Longrightarrow \quad t_\text{L} =
\frac{m}{\alpha}\left(v_\text{L}^{-1}  - v_0^{-1}\right).
$$

Plugging this into our formula for distance, along with the recipe
for$\alpha$, gives

$$
x(t_\text{L}) = \frac{2m}{\pi \rho r^2}\log\left(\frac{v_0}{v_\text{L}}\right).
$$

We can plug all our numbers in and see if we get a more sensible
result.
Note that this won't be the full answer, just how far the droplet
moves before Stokes' drag kicks in:

$$
x(t_\text{L}) \approx \frac{2(5.2 \times 10^{-10})\text{m}}{1.2 \pi(5
\times 10^{-5})^2}\log\left(\frac{100}{0.15}\right) \approx 0.7 \text{
m}.
$$

This is looking very good!

#### References

<!-- https://en.wikipedia.org/wiki/Aerosol#Solution_to_the_general_dynamic_equation -->
<!-- https://en.wikipedia.org/wiki/Cunningham_correction_factor -->
<!-- https://arxiv.org/pdf/1009.0557.pdf -->
<!-- http://farside.ph.utexas.edu/teaching/336k/Newtonhtml/node29.html -->

<!-- The first question is what sort of drag force the sneeze particles are
subject to. To check, we first compute something called the *Reynolds number*,
defined as the ratio

$$
\text{Re} = \frac{\rho v D}{\mu},
$$

where $\mu$ is the viscosity of the fluid, $\rho$ the density, $v$ the
velocity of the particle, and $D$ its rough size.
In the case of a sneeze, the fluid is air, with viscosity $\mu = 1.8
\times 10^{-5} \text{ kg/m s}$ and density around $1.2 \text{
kg/m}^3$.
Sneeze droplets come in different sizes, but we will start by looking
at "large" droplets, around $100 \, \mu \text{m} = 10^{-4} \text{m}$
in diameter.
If emitted at $100 \text{ m/s}$, the Reynolds number is -->

<!-- $$
\text{Re} = \frac{\rho v D}{\mu} = \frac{1.2 \cdot 100 \cdot
10^{-4}}{1.8 \times 10^{-5}} \approx 700.
$$ -->

<!-- Consulting various
[tables](https://www.me.psu.edu/cimbala/me325web_Spring_2012/Labs/Drag/intro.pdf),
this is large enough for interesting things to happen in the wake of
the droplet, such as vortex formation and shedding.
For a droplet of radius $r$, the drag force takes the form -->

<!-- https://www.grc.nasa.gov/www/k-12/airplane/dragsphere.html -->
<!-- As a simple approximation, suppose it still takes $t = -->
<!-- \sqrt{2h/g}$ for the droplet to hit the ground. We will focus on how far it travels -->
<!-- when subject only to resistance in the horizontal direction of motion. -->
