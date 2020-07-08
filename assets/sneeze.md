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
The time it takes for a droplet to fall to the ground under the
influence of gravity is given by

$$
h = \frac{1}{2}gt^2 \quad \Longrightarrow \quad t = \sqrt{\frac{2h}{g}}.
$$

The *range* is the horizontal distance covered in this time.
If you impart speed $v_0$ to the droplet, then the range $R$ is

$$
R = v_0t = v_0 \sqrt{\frac{2h}{g}}.
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

**Exercise 1.** (a) Show that if fired at angle $\theta$ to the
horizontal, the range is

$$
R = v_0t_0 + v_0\sqrt{\frac{2h}{g} + t_0^2}, \quad t_0 = \frac{v_0\sin\theta}{g}.
$$

(b) Using the parameters above, how far does a ballistic droplet travel
when "fired" at $\theta = 45^\circ$?

<!-- 140 m! -->

---

#### Resistance is futile

Obviously, we've missed something big. The WHO is not instructing us
to stay $50$ m away from one another!
In reality, droplets are subject to *air resistance*.
This is a force directed against motion, and which increases with velocity.
The first question is what sort of drag force the sneeze particles are
subject to.
To check, we first compute something called the *Reynolds number*,
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
If emitted at $100 \text{ m/s}$, the Reynolds number is

$$
\text{Re} = \frac{\rho v D}{\mu} = \frac{1.2 \cdot 100 \cdot
10^{-4}}{1.8 \times 10^{-5}} \approx 700.
$$

Consulting various
[tables](https://www.me.psu.edu/cimbala/me325web_Spring_2012/Labs/Drag/intro.pdf),
this is large enough for interesting things to happen in the wake of
the droplet, such as vortex formation and shedding.
For a droplet of radius $r$, the drag force takes the form

$$
F \approx \rho v^2 r^2
$$

<!-- https://www.grc.nasa.gov/www/k-12/airplane/dragsphere.html -->
As a simple approximation, suppose it still takes $t = \sqrt{2h/g}$
for the droplet to hit the ground.
We will focus on how far it travels when subject only to resistance in
the horizontal direction of motion.

#### References
