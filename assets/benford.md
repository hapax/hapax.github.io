---
Layout: post
mathjax: true
comments: true
title:  "The CLT, Fermi estimates and Benford's law"
categories: [Physics, Hacks, Mathematics, Statistics]
date:  2021-01-04
---

**January 4, 2021.** *Adding many independent random variables
  together tends to produce a normal distribution. Multiplying many
  random variables tends to produce a lognormal distribution. This not
  only explains Benford's law (that first digits in naturally
  occurring numbers are not distributed equally), but also the
  robustness of Fermi estimates.*

#### A cheap proof of the usual central limit theorem

The central limit theorem (CLT) states that, if I sum up a bunch of
independent, identically distributed variables, the result tends to a
normal distribution.
More precisely, if $X$ has mean $\mu$ and variance $\sigma^2$, and
$X_i \sim X$ for $i = 1, \ldots, n$, then

$$
S_n := \frac{1}{\sqrt{N}}\sum_{i=1}^n (X_i - \mu) \to \mathcal{N}(0, 1),
$$

where the limit means convergence in distribution () as $n \to \infty$.
There is a simple heuristic proof we can give.
First, we need to define the *characteristic function* $\varphi_X$:

$$
\varphi_X(t) := \langle e^{itX}\rangle.
$$

This has various nice properties we will need. First of all, for $X,
Y$ independent, the characteristic function of the sum $X+Y$ factorises:

$$
\varphi_{X+Y}(t)  = \langle
e^{itX}e^{itY}\rangle = \langle e^{itX}\rangle \langle e^{itY}\rangle
= \varphi_X(t) \varphi_Y(t).
$$

Secondly, since derivatives and expectations commute, the derivative
at $t = 0$ gives moments:

$$
\frac{d^n}{d t^n}\varphi_{X}(0) = \left\langle \frac{d^n}{d t^n}
e^{itX}\right\rangle \bigg|_{t=0} = i^n\langle X^n\rangle.
$$

As a special case, $\varphi_X(0) = \langle 1\rangle = 1$.
Finally, the characteristic function for a normal distribution
$\mathcal{N}(0, 1)$ is easily computed by completing the square:

$$
\begin{align*}
\varphi_X(t) & = \langle e^{itX}\rangle \\
& = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dx \,
\exp\left[-\frac{1}{2}x^2 + itx\right] \\
& = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dx \,
\exp\left[-\frac{1}{2}(x^2 - 2itx  - t^2) - \frac{1}{2}t^2\right] \\
& = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dx \,
\exp\left[-\frac{1}{2}(x - it)^2 - \frac{1}{2}t^2\right] \\
& = \frac{1}{\sqrt{2\pi}} e^{-t^2/2} \int_{-\infty}^\infty dz \,
e^{-z^2/2} = e^{-t^2/2},
\end{align*}
$$

making the substitution $z = x - it$.
Now we can sketch a physicist's proof of the CLT.
Note that $Z := (X - \mu)/\sigma$ has mean $0$ and variance $1$, so that
if we expand its characteristic function as a power series, we have

$$
\varphi_Z(t) = 1 - \fra
$$

#### A CLT for non-identical variables

#### Lognormals and uniformity

<!-- https://arxiv.org/pdf/cond-mat/9808305.pdf -->
