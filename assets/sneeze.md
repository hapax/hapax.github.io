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
If you impart speed $v$ to the droplet, then the range $R$ is

$$
R = vt = v \sqrt{\frac{2h}{g}}.
$$

Let's plug in some numbers and see if the range is reasonable.
Droplets can be emitted at speeds of up to $v = 40 \text{m/s}$.
A reasonable height is $h \approx 2 \text{m}$, and $g = 9.8 \text{
m/s}^2$.
So we get a range of

$$
R = 40 \sqrt{\frac{2 \cdot 2}{9.8}} \text{ m} \approx 25 \text{ m}.
$$

This is obviously much too large! It gets even worse if we change the
firing angle.

---

**Exercise 1.** (a) Show that if fired at angle $\theta$ to the
horizontal, the range is

$$
R = \frac{v^2\sin\theta}{g} + v\sqrt{\frac{2h}{g}}.
$$

(b) How far does a real droplet go when "fired" at $\theta = 45^\circ$?

---

#### References
