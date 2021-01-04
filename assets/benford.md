---
Layout: post
mathjax: true
comments: true
title:  "The unreasonable effectiveness of Fermi estimates"
categories: [Physics, Hacks, Mathematics, Statistics]
date:  2021-01-04
---

**January 4, 2021.** *Why are Fermi approximations so effective? One
  mechanism is logarithmic uniformity, which occurs for products of
  many random variables. Interestingly, this is the same mechanism
  behind Benford's law.*

#### Introduction

Fermi approximation is the art of making good order-of-magnitude estimates.
I've written about them
[extensively](https://hapax.github.io/assets/fermi-estimates.pdf)
[before](https://hapax.github.io/physics/teaching/hacks/napkin-hacks/#sec-3),
but I've never really found a satisfactory explanation for why it is so effective.
It's not just that order-of-magnitude provides a charitable margin of
error.
Even given this latitude, I've found that time and time again, they
are better than they have any right to be!

Clearly, there must be an underlying statistical explanation for this
unreasonable effectiveness.
Roughly speaking, it is *logarithmic uniformity*, the same mechanism underlying the
curious distribution of first digits known as
[Benford's law](https://en.wikipedia.org/wiki/Benford%27s_law).
We'll talk about uniformity, then zero in on Fermi estimates and
Benford's law in turn.

#### Products and logarithmic uniformity

Suppose a random variable $F$ is a product of many independent random
variables,

$$
F = X_1 X_2 \cdots X_N.
$$

Then the logarithm of $F$ is a sum of many random variables $Y_i =
\log X_i$:

$$
\log F = \log X_1 + \log X_2 + \cdots + \log X_N = \sum_{i=1}^N Y_i.
$$

#### Extra

The Lyapunov condition holds for a sum of independent random
variables.
By taking an exponential, we can turn it into a result for a *product* of
independent variables.
Let $X_i, \mu_i, \sigma_i^2$ be as above, and $X_i = \log Y_i$.
Then

$$
\exp\left[\sum_{i=1}^N X_i\right] = \prod_{i = 1}^N Y_i \to \log
\mathcal{N}(\mu, \sigma^2).
$$

The distribution on the right is not a normal, but a *log-normal*.
It is simply what the normal distribution looks like when viewed in
terms of a variable $y > 0$ defined by $x = \log y$.
In order to plot the density, we use the fact that $dx =
dy/y$, and hence

$$
p(x)\, dx = \frac{dx}{\sqrt{2\pi}\sigma}
e^{-\frac{(x-\mu)^2}{2\sigma^2}} = \frac{dy}{\sqrt{2\pi}\sigma y}
e^{-\frac{(\log y-\mu)^2}{2\sigma^2}}.
$$

So, this is distribution that a product of many independent factors
converges to.

<!-- https://arxiv.org/pdf/cond-mat/9808305.pdf -->
