---
Layout: post
mathjax: true
comments: true
title:  "Maxing out daily temperature"
categories: [Mathematics, Physics, Everyday]
date:  2021-01-26
---

**January 27, 2021.** *I compute the approximate relationship between
  maximum daily temperature, latitude, date, and time, and check
  against real data.*

#### Introduction

The sun heats the earth up, and the earth radiates that heat back into
space. As the sun sets, less heat is delivered, and the maximum
temperature occurs when the two rates---heat delivered and heat
radiated---balance. In this post, we'll work out how this simple
requirement relates maximum temperature to the latitude, time of year,
and time of day the maximum occurs.

#### Energy balance

Consider a small patch of the earth's surface of unit area, at the
point it attains its maximum temperature $T_\text{max}$ in Kelvin.
According to the
[Stefan-Boltzmann law](https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law),
it radiates energy away with intensity

$$
I_\text{out} = \sigma T_\text{max}^4, \quad \sigma = 5.67 \times
10^{-8} \frac{\text{W}}{\text{m}^2 \text{ K}}.
$$

Since this is the maximum attained, it must equal the intensity of
incoming solar radiation $I_\text{in}$.
To a good approximation, this is the radiant intensity of sunlight
striking the earth's surface head on, the so-called insolation
constant $I_0$, multiplied by a geometric term $\cos^2\vartheta$ to account for the
angle of sunlight, and an albedo term $(1-a)$ to account for sunlight
reflected back:

$$
I_\text{in} = I_0 (1- a )\cos^2\vartheta.
$$

The insolation constant is $I_0 = 1367 \text{ W/m}^2$ [<sup><a id="fnr.1" name="fnr.1" class="footref" href="#fn.1">1</a></sup>].
The albedo of the earth is around $a = 0.3$, i.e. $30\%$ reflected
back into space on average, though this depends on cloud cover, snow,
and so on.
We will talk about $\vartheta$ more in a moment.
Setting $I_\text{in} = I_\text{out}$ when the maximum is obtained, we
find

$$
I_0 (1- a )\cos^2\vartheta = \sigma T_\text{max}^4.
$$

#### Solar geometry

---

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum"
href="#fnr.1">Footnote 1</a></sup> <p class="footpara">
This comes once more from the Stefan-Boltzmann law (for the surface
temperature of the sun $T_\odot = 5800 \text{ K}$), and an inverse square
drop-off:

$$
I_0 = \sigma T_\odot^4 \left(\frac{R_\odot}{d}\right)^2 =
5.67 \times 10^{-8} \cdot 5800^4  \left(\frac{7 \times 10^5}{1.5\times
10^8}\right)^2\, \frac{\text{W}}{\text{m}^2}\approx 1400 \, \frac{\text{W}}{\text{m}^2},
$$

where $R_\odot = 7 \times 10^5 \text{ km}$ is the solar radius and $d
= 1.5 \times 10^8 \text{ km}$ the earth-sun distance.
</p></div>
