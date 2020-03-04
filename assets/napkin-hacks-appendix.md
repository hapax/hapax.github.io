---
Layout: post
mathjax: true
comments: true
title:  "Hacking physics: solutions"
date:  2020-02-24
---

This is the technical appendix to my
[post on napkin hacks](https://hapax.github.io/physics/teaching/hacks/napkin-hacks/).
It contains solutions to exercises, and some material I deemed overly
technical for the post.
Very much under construction!

### Contents

1. <a href="#sec-1">Solutions to exercises</a>
   1. <a href="#sec-1-1">Interplanetary pumpkins</a>
   2. <a href="#sec-1-2">Terminal raindrops</a>
2. <a href="#sec-2">Technicalities</a>
   2. <a href="#sec-2-1">Equilibrium for pollen grains</a>

## 1. Solutions to exercises <a id="sec-1" name="sec-1"></a>

### 1.1. Interplanetary pumpkins <a id="sec-1-1" name="sec-1-1"></a>

### 1..2. Terminal raindrops <a id="sec-1-2" name="sec-1-2"></a>

## 2. Technicalities <a id="sec-2" name="sec-2"></a>

### 2.1. Equilibrium for pollen grains <a id="sec-2-1" name="sec-2-1"></a>

*Prerequisites: exponentials; binomial approximation.*

The equilibrium condition for pollen grains is more
complicated than the simple equation I gave in the main text.
If there are many balls of resin, they will settle at different
heights, and the number of particles will change with height.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/hacker-gamboge.jpg" width="60%"/>
		    <figcaption><i>A sketch of Perrin's gamboge granules.</i></figcaption>
	</div>
	</figure>

Nature likes low energy states.
In a hot system, there is an element of randomness, but nature
penalises high energy states by making them exponentially unlikely:

$$
\text{probability}(E) \propto e^{-E/k_B\mathcal{T}}.
$$

They are not exactly zero, but when the energy $E$ is much greater
than the thermal energy $k_B\mathcal{T}$, they may as well be!
For a gas in a tall container, the energy is just the gravitational potential energy, $E
= mgh$, and the number density of particles is proportional to the
probability.
The result is called the *barometric distribution*:

$$
n(h) = n_0 e^{-mgh/k_B\mathcal{T}},
$$

where $n_0$ is a constant (with dimensions of density) that won't concern us.

Consider a thin slice of the fluid at height $h$, with density $n$,
thickness $\Delta h$ and area $A$.
This slice will lose particles as they fall under the influence of
gravity.
In equilibrium, particles fall at the terminal velocity
$v_\text{term}$, and hence the slice loses particles at a rate

$$
R_\text{loss} = n A \Delta h v_\text{term}.
$$

But balls of resin also perform random walks.
They will tend to wander from regions of high concentration to regions
of low concentration, since (as discussed in the main text) a drop of
random walkers spreads out.
Since the layer below will tend to have more resin balls (according to
the barometric distribution), there will be a upward spread of
walkers.
We expect this will involve $\Delta n$, the difference in
number density, and the rate of diffusion $D$.
The rate of gain should then take the form (Exercise A.1)

$$
R_\text{gain} = D A \Delta n.
$$

Finally, in equilibrium, the rate of gain and loss are equal!
Thus, we have that

$$
n A \Delta h v_\text{term} = D A \Delta n \quad \Longrightarrow \quad v_\text{term} = \frac{D}{n}\frac{\Delta n}{\Delta h}.
$$

This looks complicated, but for the barometric distribution (Exercise
A.2), it turns out that

$$
\frac{1}{n}\frac{\Delta n}{\Delta h} = \frac{mg}{k_B\mathcal{T}} \quad \Longrightarrow \quad
v_\text{term}  = \frac{Dmg}{k_B\mathcal{T}}.
$$

If we now plug in the terminal velocity from Stokes' law, we can
rearrange to find the Stokes-Einstein relation we derived (with
considerable trickery) in the main text:

$$
D  = \frac{k_B\mathcal{T}}{6\pi \mu r}.
$$

There are various factors of $2$ I am neglecting.
But given the dimensional analysis-based sloppiness I'm advocating in
general, we won't lose sleep over them!

---

**Exercise A.1 (grabbing granules).** The rate at which a
  thin slice of fluid gains resin particles, $R_\text{gain}$, will
  involve:
  - The difference in concentration $\Delta n$ between layers.
  - The area $A$ of the layer.
  - The diffusion constant $D$ for resin particles.

The rate $R_\text{gain}$ has dimensions of number per time.
Find the dimensions of the terms in the list above, and conclude from
dimensional analysis that

$$
R_\text{gain} \sim D A \Delta n.
$$

<p align="center">
  ⁂
  </p>

**Exercise A.2 (exponential change).** One way of defining an
exponential is as the limit

$$
e^x = \lim_{n\to\infty} \left(1 + \frac{x}{n}\right)^n.
$$

The binomial approximation says that

$$
(1 + X)^\alpha \approx 1 + \alpha X
$$

for small $X$ and any $\alpha$.
We can combine these two facts to learn something cool about the
barometric distribution!

<span style="padding-left: 20px; display:block">
(a) Show using the binomial approximation that
</span>

$$
e^x = \lim_{n\to\infty} \left[1 + x + x^2(\cdots)\right],
$$

<span style="padding-left: 20px; display:block">
where the $ \cdots$ denote terms multiplied by $x^2$.
</span>

<span style="padding-left: 20px; display:block">
(b) Using (a), argue that for $x \ll 1$,
</span>

$$
e^x \approx 1 + x.
$$

<span style="padding-left: 20px; display:block">
(c) The barometric distribution is
</span>

$$
n(h) = n_0 e^{-mgh/k_B\mathcal{T}}.
$$

<span style="padding-left: 20px; display:block">
From the previous exercise, show that, if $\Delta h \ll
k_B\mathcal{T}/mg$, then
</span>

$$
\frac{\Delta n}{\Delta h} = \frac{n(h+\Delta h) - n(h)}{\Delta h} \approx \frac{n(h)mg}{k_B\mathcal{T}}.
$$

---
