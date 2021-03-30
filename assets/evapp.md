---
Layout: post
mathjax: true
comments: true
title:  "From heat death to tiny black holes"
categories: [Physics, Hacks]
date:  2021-03-29
---

**March 29, 2021.** *Black holes leak energy into the environment and
  ultimately evaporate. In this post, I'll explore two applications of
  evaporation: estimating the life expectancy of the universe, and
  showing that the LHC cannot produce dangerous black holes.*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">The end of the universe</a>
3. <a href="#sec-3">Black holes at the LHC</a>
4. <a href="#sec-A">Appendix: evaporation</a>

#### 1. Introduction<a id="sec-1" name="sec-1"></a>

In 1974, Stephen Hawking discovered that black holes glow.
This means that, over time, a black hole loses energy and eventually
disappears altogether.
We're going to use this to do some fun stuff, first guessing the
time until entropic heat death, and secondly, giving a heuristic
argument that the Large Hadron Collider (LHC) does not produce
dangerous microscopic black holes.
We won't derive anything in detail, but rather, slap estimates together
to get an order-of-magnitude vibe for what's going on.
Our key formula will be that, for a black hole of mass $M$, the
evaporation timescale is roughly

$$
t_\text{evap} \sim \frac{G^2M^3}{\hbar c^4} \sim 10^{67} \text{ years}
\left(\frac{M}{M_\odot}\right)^3,
$$

where $M_\odot = 2\times 10^{30} \text{ kg}$ is the mass of the sun,
and $G$ is Newton's constant, $c$ the speed of light, and $\hbar$ is
Planck's constant. I'll explain these constants if and when we need
them.
Now for our applications!

#### 2. The end of the universe<a id="sec-2" name="sec-2"></a>

Careful observation of the night sky reveals that everything is flying
apart at an accelerating rate. Eventually, every galaxy (or any other
system clumped together by gravity) will be moving away from other
systems faster than light.
At this point, it has entered its *cosmological horizon*, from which
it can no longer send messages.
We can loosely estimate how long it will take us to fall into our
cosmological horizon as follows.
The bigger gravitationally bound structure we are part of is the
[*local group*](https://en.wikipedia.org/wiki/Local_Group), a collection of galaxies a few million light
years across.
Around 13 million light years away, we encounter the
[M94 group](https://en.wikipedia.org/wiki/M94_Group), which is *not*
gravitationally bound to us.

So, we can estimate "time to horizon" as the time it takes the M94
group to move at the speed of light, relative to us.
To do this, we can use *Hubble's law*.
This says that an object a distance $d$ away recedes from us at a
speed $v$ given by

$$
v = H_0d, \quad H_0 \approx 70 \, \frac{\text{km/s}}{\text{Mpc}}
= 7 \times 10^{-11} \, \frac{c}{\text{ly}},
$$

where $H_0$ is the *Hubble parameter*, and we have converted from the
conventional units (km/s per megaparsec) to even weirder units (light
speed units per light year, or inverse years).
To see how long it takes M94 to reach light speed, we technically need
to do calculus, but I'm lazy and we won't. Instead, I simply claim
that things move away *exponentially quickly*, with distance and speed

$$
d(t) = d_0 e^{H_0t}, \quad v(t) = H_0 d_0 e^{H_0t} = H_0 d(t).
$$

So, to figure out when M94 reaches light speed, we note that (if now
is $t = 0$) then

$$
d_0 = 13 \times 10^6 \text{ ly},
$$

and we want $v(t) = c$. Thus,

$$
c = H_0 d_0 e^{H_0t} \quad \Longrightarrow \quad t =
\frac{1}{H_0}\log\left(\frac{c}{H_0 d_0}\right) =
\frac{10^{11}}{7}\log\left(\frac{10^{11}}{7 \cdot (13 \times 10^6)}\right) \text{
y} \approx 100 \text{ Gy},
$$

i.e. $100$ billion years.

#### 3. Black holes at the LHC<a id="sec-3" name="sec-3"></a>

#### 4. Appendix: evaporation<a id="sec-4" name="sec-4"></a>
