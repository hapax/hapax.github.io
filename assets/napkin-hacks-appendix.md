---
Layout: post
mathjax: true
comments: true
title:  "Hacking physics: solutions and technicalities"
date:  2020-02-24
---

This is a technical appendix to my blog post on
[napkin hacks](https://hapax.github.io/physics/teaching/hacks/napkin-hacks/). It
contains solutions to exercises and some technical results.
Very much under construction!

### Contents

1. <a href="#sec-1">Solutions to exercises</a>
   1. <a href="#sec-1-1">Interplanetary pumpkins</a>
   2. <a href="#sec-1-2">Terminal raindrops</a>
2. <a href="#sec-2">Technicalities</a>
   1. <a href="#sec-2-1">Random walks</a>
   2. <a href="#sec-2-2">Equilibrium for pollen grains</a>

## 1. Solutions to exercises <a id="sec-1" name="sec-1"></a>

### 1.1. Interplanetary pumpkins <a id="sec-1-1" name="sec-1-1"></a>

### 1..2. Terminal raindrops <a id="sec-1-2" name="sec-1-2"></a>

## 2. Technicalities <a id="sec-2" name="sec-2"></a>

### 1.1. Random walks <a id="sec-2-1" name="sec-2-1"></a>

*Prerequisites: basic probability theory.*

We will prove the square root scaling of random walks, first in 1D, and then extend
almost immediately to many dimensions.
The only prerequisite is a little probability theory and knowledge of vectors.

*Proof (1D).* Suppose we toss a coin, and move a counter
left or right one unit depending on whether we gets heads or tails.
Label the outcome of the $n$th toss $s_n$, where $s_n = -1$ for heads
and $s_n = +1$ for tails.
If we start at $0$, the position $x$ after $n$ tosses is the sum of steps:

$$
x = s_1 + s_2 + \cdots + s_n.
$$

This is a random process, so what do we expect to happen on average?
We can calculate this with an *expectation*: a weighted average over all the things
that can happen, where the weights are probabilities.
We denote this by $\langle f(s_1, \ldots, s_n)\rangle$, where $f$ is
any function of the steps.
For instance, if the coin is fair, then on average an individual step
is zero:

$$
\langle s\rangle = P(s=-1)(-1) + P(s=+1)(+1) = \frac{1}{2}-\frac{1}{2}
= 0.
$$

A very similar calculation shows that $x$ vanishes on average:

$$
\begin{align*}
\langle x\rangle &= \langle s_1 + \cdots + s_n\rangle\\
& = \langle s_1\rangle + \cdots + \langle s_n\rangle\\
& = 0 + \cdots + 0 = 0,
\end{align*}
$$

where we used the fact that expectation is *linear*, $\langle f +
g\rangle = \langle f\rangle + \langle g\rangle$.
This makes sense, since if the coin is unbiased, it has no preference
between heads and tails.
If $\langle x\rangle >0$, for instance, then the coin is exhibiting a
bias towards tails.
The story is different for the *square* of a step:

$$
\langle s^2\rangle = P(s=-1)(-1)^2 + P(s=+1)(+1)^2 =
\frac{1}{2}+\frac{1}{2} = 1.
$$

What about a product of different coin flips?
Each possible outcome $--$, $-+$, $+-$, $++$ has chance $1/4$, and hence

$$
\langle X_i \cdot X_j\rangle =
\frac{1}{4}\left[(-1)^2 + (-1)(+1) + (+1)(-1) + (+1)^2\right] = 0.
$$

Combining these two facts, we can calculate the *variance*:

$$
\begin{align*}
\langle x^2\rangle & = \langle (s_1 + \cdots + s_n)^2\rangle \\
& = \langle s_1^2\rangle + \cdots + \langle s_n^2\rangle +
2\left\{\langle s_1\cdot s_2\rangle + \cdots + \langle s_{n-1}\cdot
s_n\rangle\right\} \\
& = n \langle s^2\rangle = n.
\end{align*}
$$

The counter moves back and forth, and on average $\langle x\rangle =
0$.
But the size of the region explored as it moves back and forth is the
square root of the variance, also called the *root mean square* (rms)
displacement, $\sqrt{\langle x^2\rangle} = \sqrt{n}$.
This is the distance from the origin the counter will tend to wander
in the first $n$ steps.
If instead of steps $\pm 1$, we have steps $\pm \ell$, then $\langle
s^2\rangle = \ell^2$ and the rms displacement becomes

$$
\sqrt{\langle x^2\rangle} = \ell\sqrt{n}
$$

as claimed above.

*Proof (many D).* The proof is almost identical in $d$ dimensions,
 where a step can be written as a vector $\vec{s}$ with $d$ components:

$$
\vec{s} = (s^1, s^2\, \ldots, s^d).
$$

The length of $\vec{s}$ is given by a generalisation of Pythagoras'
theorem (Exercise A.1):

$$
|\vec{s}| = \sqrt{(s^1)^2 + (s^2)^2 + \cdots + (s^d)^2}.
$$

Let's assume that the average step length is $ \ell $, and steps are
unbiased, so

$$
\langle \vec{s} \rangle = \vec{0} = (0, 0, \ldots, 0), \quad \langle |\vec{s}|^2 \rangle = \ell^2.
$$

Finally, we assume that steps are independent, so any two components of
distinct steps satisfy

$$
\langle s_i^a \cdot s^b_j \rangle = 0,
$$

where $\vec{s}_i, \vec{s}_j$ are distinct steps, and $a, b$ labels
components.
Then, if $\vec{x} = \vec{s}_1 + \cdots + \vec{s}_n$, the random walk has variance

$$
\begin{align*}
\langle |\vec{x}|^2\rangle & = \langle (s_1^1 + s_2^1 + \cdots
s_n^1)^2 + \cdots + (s_1^n + s_2^n + \cdots s_n^n)^2 \rangle \\
	& = \langle [(s_1^1)^2 + (s_2^1)^2 + \cdots
(s_n^1)^2] + \cdots +  [(s_1^n)^2 + (s_2^n)^2 + \cdots +(s_n^n)^2]
\rangle \\
& \qquad \qquad + 2 \langle
[s_1^1 \cdot s_2^1 + \cdots + s_{n-1}^1\cdot s_n^1]+\cdots + [s_1^n \cdot s_2^n + \cdots + s_{n-1}^n\cdot s_n^n] \rangle\\
& = \langle [(s_1^1)^2 + (s_1^2)^2 + \cdots
(s_1^n)^2] + \cdots +  [(s_n^1)^2 + (s_n^2)^2 + \cdots +(s_n^n)^2]
\rangle \\
& = \langle [(s_1^1)^2 + (s_1^2)^2 + \cdots
(s_1^n)^2] + \cdots +  [(s_n^1)^2 + (s_n^2)^2 + \cdots +(s_n^n)^2]\\
& = \langle |\vec{X}_1|^2\rangle + \cdots +\langle
|\vec{X}_n|^2\rangle\\
& = n \ell^2,
\end{align*}
$$

where on the third line we used the fact that the components of
different steps are independent, on the fourth line we reorganised the
terms $(s_i^a)^2$ into individual steps, on the fifth line we used the
definition of length and the linearity of expectation, and on the
last line we used the assumption about average step length.
Taking square roots, we find the rms displacement

$$
\sqrt{\langle |\vec{x}|^2\rangle} = \ell\sqrt{n},
$$

in any number of dimensions.
Notice also that we do not need to assume the steps are the same
length or live on lattice.

---

**Exercise A.1 (Pythagoras in higher dimensions).** Consider a vector
$\vec{C} = (C^1, \ldots, C^d)$ in $d$ dimensions.

(a) We can write the vector as a sum

$$
\vec{C} = (C^1, \ldots, C^{d-1}, 0) + (0, \ldots, 0, C^d) = \vec{A}+\vec{B}.
$$

Argue that these two summands are at right angles, and use Pythagoras'
theorem (in the plane spanned by $\vec{A}$ and $\vec{B}$) to argue
that

$$
|\vec{C}|^2 = |\vec{A}|^2 + |\vec{B}|^2 = |\vec{A}|^2 + (C^d)^2.
$$

(b) Now iteratively repeat this argument for $\vec{A}$, and deduce
that, as we claimed above, length squared in $d$ dimensions is

$$
|\vec{C}|^2 = (C^1)^2 + \cdots + (C^d)^2.
$$

---

### 2.2. Equilibrium for pollen grains <a id="sec-2-2" name="sec-2-2"></a>

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

In a thermal system, the laziness of nature takes the form of an
exponential penalty for energies which are large compared to the
thermal energy,

$$
\text{probability} \propto e^{-E/k_B\mathcal{T}}.
$$

In this case, the energy is just the gravitational potential energy $E
= mgh$, and the number density of particles is proportional to the
probability.
The result is called the *barometric distribution*:

$$
n(h) = n_0 e^{-mgh/k_B\mathcal{T}},
$$

for some constant $n_0$ we won't care about.

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
the barometric distribution), there will be a net upward movement of
walkers.
We expect this will involve $\Delta n$, the difference in
number density, and the rate of diffusion $D$.
The rate of gain should then take the form (Exercise A.2)

$$
R_\text{gain} = D A \Delta n.
$$

Finally, in equilibrium, the rate of gain and loss are equal!
Thus, we have that

$$
n A \Delta h v_\text{term} = D A \Delta n \quad \Longrightarrow \quad v_\text{term} = \frac{D}{n}\frac{\Delta n}{\Delta h}.
$$

This looks complicated, but for the barometric distribution (Exercise
A.3), it turns out that

$$
\frac{1}{n}\frac{\Delta n}{\Delta h} = \frac{mg}{k_B\mathcal{T}} \quad \Longrightarrow \quad
v_\text{term}  = \frac{Dmg}{k_B\mathcal{T}}.
$$

If we now plug in the terminal velocity from Stokes' law, we can
rearrange to find the Stokes-Einstein relation we derived with
trickery in the main text:

$$
D  = \frac{k_B\mathcal{T}}{6\pi \mu r}.
$$

---

**Exercise A.2 (grabbing granules).** The rate at which a
  thin slice of fluid gains resin particles, $R_\text{gain}$, will
  involve:
  - The difference in concentration $\Delta n$ between it and the
  next layer down.
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

**Exercise A.3 (exponential change).** One way of defining an
exponential is as the limit

$$
e^x = \lim_{n\to\infty} \left(1 + \frac{x}{n}\right)^n.
$$

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
(b) Argue that, for $x \ll 1$,
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
Using the previous exercise, show that, if $\Delta h \ll
k_B\mathcal{T}/mg$, then
</span>

$$
\frac{\Delta n}{\Delta h} = \frac{n(h+\Delta h) - n(h)}{\Delta h} \approx \frac{n(h)mg}{k_B\mathcal{T}}.
$$

---
