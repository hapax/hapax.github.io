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
independent, identically distributed (iid) variables, the result tends to a
normal distribution.
More precisely, if $X$ has mean $\mu$ and variance $\sigma^2$, and
$X_i \sim X$ for $i = 1, \ldots, n$, then the sum converges to a normal:

$$
S_N := \frac{1}{\sqrt{N}}\sum_{i=1}^N (X_i - \mu) \to \mathcal{N}(0, 1).
$$

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
The final property swaps constants from random variables to the
argument $t$:

$$
\varphi_{aX}(t) = \langle e^{itaX}\rangle = \varphi_{X}(at).
$$

The last ingredient in our cheap proof of the CLT is the
characteristic function for a normal distribution $\mathcal{N}(0, 1)$
itself. This is easily computed by completing the square:

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
\varphi_Z(t) = 1 - \frac{t^2}{2} + O(t^4).
$$

Recall that the sum $S_N = \sum_i (Z_i/\sqrt{N})$, for $Z_i \sim Z$.
Thus, the characteristic function obeys

$$
\begin{align*}
\varphi_{S_N}(t) & = \left(\varphi_{Z/\sqrt{N}}(t)\right)^N \\
& = \left(\varphi_{Z}(t/\sqrt{N})\right)^N \\
& = \left[1 - \frac{t^2}{N} + O(t^4)\right]^N.
\end{align*}
$$

Assuming we can ignore the $O(t^4)$ terms, as $N \to \infty$, we have

$$
\varphi_{S_N}(t) \approx \left(1 - \frac{t^2}{N}\right)^N \to e^{-t^2/2}
$$

from the definition of the exponential.
This completes our sloppy heuristic proof!

#### A CLT for non-identical variables

The central limit theorem, in this form, is often invoked to explain
why common attributes like height and weight are normally distributed.
They are a sum of many small iid increments, and so should approach a
normal, or so the reasoning goes.
But why should heigh be a sum of iid increments?
At the end of the day, height is the phenotypic expression of our DNA.
Presumably, it arises from the sum of many small increments which are
neither independent nor identically distributed.
Even if we lump them into genes which are independent to a good
approximation, the height increments due to different genes are
unlikely to have the same distribution.
The genes controlling the length of my legs contribute much
more than the ones controlling the thickness of my scalp.

One way to generalise the CLT is to consider independent but not
identically distributed variables $X_i$, with means $\mu_i$ and
variances $\sigma_i^2$.
In this case, we define

$$
\Sigma_N^2 = \sum_{i=1}^N \sigma_i^2, \quad S_N :=
\frac{1}{\Sigma_N}\sum_{i=1}^N (X_i - \mu_i).
$$

Then, subject to certain technical conditions (usually Lyapunov or
Lindeberg, neither of which we will spell out), the sum $S_N$
approaches a normal as before,

$$
S_N \to \mathcal{N}(0, 1).
$$

The proofs are highly technical, but we can give a heuristic
flavour for them, since they proceed more or less as the proof above,
up to all the technicalities.
We can define the characteristic function $S_N$ as before, and note
that

$$
\begin{align*}
\varphi_{S_N}(t) & = \varphi_{X_1/\Sigma_N}(t)
\varphi_{X_2/\Sigma_N}(t)\cdots \varphi_{X_N/\Sigma_N}(t) \\
& = \varphi_{X_1}(t/\Sigma_N)
\varphi_{X_2}(t/\Sigma_N)\cdots \varphi_{X_N}(t/\Sigma_N) \\
& = \prod_{i=1}^N\left[1 - \frac{\sigma_i^2t^2}{2\Sigma_N^2} + O(t^4)\right].
\end{align*}
$$

We once again ignore the $O(t^4)$ terms.
Let's write $\alpha_i := - \sigma_i t^2/2\Sigma_N^2$.
Then

$$
\begin{align*}
\varphi_{S_N}(t) & \approx
\prod_{i=1}^N(1 + \alpha_i)
\\
= 1 + \sum_{i=1}^N \alpha_i + \sum_{i < j}\alpha_i \alpha_j + \cdots.
\end{align*}
$$

#### Lognormals and uniformity

<!-- https://arxiv.org/pdf/cond-mat/9808305.pdf -->
