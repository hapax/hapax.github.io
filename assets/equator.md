---
Layout: post
mathjax: true
comments: true
title:  "The battle of the bulge"
categories: [Physics, Hacks]
date:  2020-10-21
---

**October 21, 2020.** *The earth spins and the equator bulges, turning
  from a sphere into a flattened ellipsoid. To estimate just how
  flattened, we assume that the bulge at the equator compensates for
  the rotation in the sense that the surface is an equipotential.*

#### Energy in a spinning frame

Suppose you're in a spinning reference frame with angular velocity
$\omega$, and a distance $r$.
You will be subject to an acceleration

$$
a = \frac{v^2}{r} = \omega^2 r.
$$

This looks like a *centrifugal force* $F = ma$, arising from a quadratic
potential

$$
F = -\frac{dU_\text{cent}}{dr} \quad \Longrightarrow \quad U_\text{cent} = -\frac{1}{2}m
\omega^2 r^2.
$$

If your spinning reference frame is the earth, then there is a
gravitational potential $U_\text{grav} = -GMm/R$, where $M$ is the
earth's mass and $R$ is the distance to the centre.

We will try to estimate the earth's bulge by assuming that the
*potential is the same at the poles and the equator*.
If the earth was a fluid (and the surface *was* molten at some point),
it would redistribute itself if there were differences in potential
across the surface, so this is not an unreasonable model.
At the poles, there is no spinning, so $\omega = 0$, and

$$
U_{\text{pole}} = U_{\text{grav}}(R) = -\frac{GMm}{R},
$$

where $R$ to be the distance from the centre of the earth to the
poles.
Technically, if the earth is *not* a sphere, then the sphere theorem
(that objects are attracted to the centre) no longer applies, but the
corrections will be small enough we can ignore them.

#### An equatorial expansion

Now, suppose that the radius at the equator is slightly larger, $R +
r$.
Then, including the centrifugal potential,

$$
U_{\text{eq}} = U_{\text{cent}}(R+r) + U_{\text{grav}}(R+r) = -\frac{1}{2}m
\omega^2 (R+r)^2 -\frac{GMm}{R+r}.
$$

We want to equate this with $U_\text{pole}$ and solve for $r$, but
this will lead to a horrible cubic equation to solve.
To proceed, we use a typical physicist's trick: if $\epsilon \ll 1$, then

$$
\frac{1}{1+\epsilon} \approx 1 - \epsilon,
$$

since $(1+\epsilon)(1-\epsilon) = 1 - \epsilon^2 \approx 1$.
In our case, this gives

$$
\frac{1}{R+r} = \frac{1}{R(1+r/R)} \approx \frac{1}{R} - \frac{r}{R^2},
$$

and hence, after some algebra, an equation for the equatorial radius

$$
(R+r)^2 = \frac{2GMr}{\omega^2 R^2}.
$$

We can expand the LHS and solve for $r$ using the quadratic formula:

$$
r^2+2r\left(R - \frac{2GM}{R^2}\right) + R^2 = 0 \quad
\Longrightarrow \quad r =
\frac{2GM}{R^2} - R + \sqrt{\left(R - \frac{2GM}{R^2}\right) \left(R + \frac{2GM}{R^2}\right)}\right].
$$

<!-- \sqrt{\left(R - \frac{2GM}{R^2}\right)^2 - R^2} -->

#### Comparing to reality
