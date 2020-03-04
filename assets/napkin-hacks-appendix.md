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

1. <a href="#sec-1">Technicalities</a>
   1. <a href="#sec-1-1">Random walks</a>
   2. <a href="#sec-1-2">Equilibrium for pollen grains</a>
1. <a href="#sec-2">Solutions to exercises</a>
   1. <a href="#sec-2-1">Interplanetary pumpkins</a>
   2. <a href="#sec-2-2">Terminal raindrops</a>


## 1. Technicalities <a id="sec-1" name="sec-1"></a>

### 1.1. Random walks <a id="sec-1-1" name="sec-1-1"></a>

We will prove the square root scaling of random walks, first in 1D, and then extend
almost immediately to many dimensions.
The only prerequisite is a little probability theory and knowledge of vectors.

*Proof (1D).* Suppose we toss a coin, and move a counter
left or right one unit depending on whether we gets heads or tails.
Label the outcome of the $n$th toss $X_n$, where $X_n = -1$ for heads
and $X_n = +1$ for tails.
If we start at $0$, the position $X$ after $n$ tosses is the sum of steps:

$$
R = X_1 + X_2 + \cdots + X_n.
$$

This is a random process, so what do we expect to happen on average?
We can calculate this with an *expectation*: a weighted average over all the things
that can happen, where the weights are probabilities.
We denote this by $\langle f(X_1, \ldots, X_n)\rangle$, where $f$ is
any function of the steps.
For instance, if the coin is fair, then on average an individual step
is zero:

$$
\langle X\rangle = P(X=-1)(-1) + P(X=+1)(+1) = \frac{1}{2}-\frac{1}{2}
= 0.
$$

A very similar calculation shows that $R$ vanishes on average:

$$
\begin{align*}
\langle R\rangle &= \langle X_1 + \cdots + X_n\rangle\\
& = \langle X_1\rangle + \cdots + \langle X_n\rangle\\
& = 0 + \cdots + 0 = 0,
\end{align*}
$$

where we used the fact that expectation is *linear*, $\langle f +
g\rangle = \langle f\rangle + \langle g\rangle$ (Exercise A.1).
This makes sense, since if the coin is unbiased, it has no preference
between heads and tails.
If $\langle R\rangle >0$, for instance, then the coin is exhibiting a
bias towards tails.
The story is different for the *square* of a step:

$$
\langle X^2\rangle = P(X=-1)(-1)^2 + P(X=+1)(+1)^2 =
\frac{1}{2}+\frac{1}{2} = 1.
$$

What about a product of different coin flips?
Each possible outcome --, -+, +-, ++ has chance $1/4$, and hence

$$
\langle X_i \cdot X_j\rangle =
\frac{1}{4}\left[(-1)^2 + (-1)(+1) + (+1)(-1) + (+1)^2\right] = 0.
$$

Combining these two facts, we can calculate the *variance*:

$$
\begin{align*}
\langle R^2\rangle & = \langle (X_1 + \cdots + X_n)^2\rangle \\
& = \langle X_1^2\rangle + \cdots + \langle X_n^2\rangle +
2\left\{\langle X_1\cdot X_2\rangle + \cdots + \langle X_{n-1}\cdot
X_n\rangle\right\} \\
& = n \langle X^2\rangle = n.
\end{align*}
$$

The counter moves back and forth, and on average $\langle R\rangle =
0$.
But the size of the region explored as it moves back and forth is the
square root of the variance, also called the *root mean square* (rms)
displacement, $\sqrt{\langle R^2\rangle} = \sqrt{n}$.
This is the distance from the origin the counter will tend to wander
in the first $n$ steps.
If instead of steps $\pm 1$, we have steps $\pm \ell$, then $\langle
X^2\rangle = \ell^2$ and the rms displacement becomes

$$
\sqrt{\langle R^2\rangle} = \ell\sqrt{n}
$$

as claimed above.

*Proof (many D).* The proof is almost identical in $d$ dimensions,
 where a step can be written as a vector $\vec{X}$ with $d$ components:

$$
\vec{X} = (X^1, X^2\, \ldots, X^d).
$$

The length of $\vec{X}$ is given by a generalisation of Pythagoras'
theorem (Exercise A.2):

$$
|\vec{X}| = \sqrt{(X^1)^2 + (X^2)^2 + \cdots + (X^d)^2}.
$$

Let's assume that the average step length is $ \ell $, and steps are
unbiased, so

$$
\langle \vec{X} \rangle = \vec{0} = (0, 0, \ldots, 0), \quad \langle |\vec{X}|^2 \rangle = \ell^2.
$$

Finally, we assume that steps are independent, so any two components of
distinct steps satisfy

$$
\langle X_i^a \cdot X^b_j \rangle = 0,
$$

where $\vec{X}_i, \vec{X}_j$ are distinct steps, and $a, b$ labels
components.
Then, if $\vec{R} = \vec{X}_1 + \cdots + \vec{X}_n$, the random walk has variance

$$
\begin{align*}
\langle |\vec{R}|^2\rangle & = \langle (X_1^1 + X_2^1 + \cdots
X_n^1)^2 + \cdots + (X_1^n + X_2^n + \cdots X_n^n)^2 \rangle \\
	& = \langle [(X_1^1)^2 + (X_2^1)^2 + \cdots
(X_n^1)^2] + \cdots +  [(X_1^n)^2 + (X_2^n)^2 + \cdots +(X_n^n)^2]
\rangle \\
& \qquad \qquad + 2 \langle
[X_1^1 \cdot X_2^1 + \cdots + X_{n-1}^1\cdot X_n^1]+\cdots + [X_1^n \cdot X_2^n + \cdots + X_{n-1}^n\cdot X_n^n] \rangle\\
& = \langle [(X_1^1)^2 + (X_1^2)^2 + \cdots
(X_1^n)^2] + \cdots +  [(X_n^1)^2 + (X_n^2)^2 + \cdots +(X_n^n)^2]
\rangle \\
& = \langle [(X_1^1)^2 + (X_1^2)^2 + \cdots
(X_1^n)^2] + \cdots +  [(X_n^1)^2 + (X_n^2)^2 + \cdots +(X_n^n)^2]\\
& = \langle |\vec{X}_1|^2\rangle + \cdots +\langle
|\vec{X}_n|^2\rangle\\
& = n \ell^2,
\end{align*}
$$

where on the third line we used the fact that the components of
different steps are independent, on the fourth line we reorganised the
terms $(X_i^a)^2$ into individual steps, on the fifth line we used the
definition of length and the linearity of expectation, and on the
last line we used the assumption about average step length.
Taking square roots, we find the rms displacement

$$
\sqrt{\langle |\vec{R}|^2\rangle} = \ell\sqrt{n},
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

### 1.2. Equilibrium for pollen grains <a id="sec-1-1"name="sec-1-1"></a>

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
n(h) = n_0 e^{-mgh/k_B\mathcal{T}}.
$$

Consider a thin slice of the fluid at height $h$, with thickness
$\Delta h$.
This will lose particles as they fall down at the terminal velocity
$v_\text{term}$, but it can gain particles from the layer above

## 2. Solutions to exercises <a id="sec-2" name="sec-2"></a>

### 2.1. Interplanetary pumpkins <a id="sec-2-1" name="sec-2-1"></a>

### 2..2. Terminal raindrops <a id="sec-2-2" name="sec-2-2"></a>
