---
Layout: post
mathjax: true
comments: true
title:  "Portfolio optimization"
categories: [Math, Probability, Finance]
date:  2022-12-05
---

**December 5, 2022.** *A quick, first-principles derivation of
  optimal portfolios with risk.*

## Introduction
---

Suppose there are $n$ bets I can make, with the return per dollar for
bet $k$ represented by a random variable $B_k$
with expected value $\mu_k = \mathbb{E}[B_k]$.
If I invest $\omega_k$ on bet
$k$, and have a fixed total $\Omega$, then I can view the value of my
portfolio as a random variable

$$
P(\omega_k) = \sum_{k = 1}^n \omega_k B_k.
$$

If I try to optimize the expected return $\mu_P = \mathbb{E}[P]$, I get a boring linear function

$$
\mu_P(\omega_k) = \sum_{k =
1}^{n} \omega_k \mu_k.
$$

To maximize this, introduce a Lagrange multiplier
$\gamma$ to enforce the fixed total:

$$
\mu_P(\omega_k, \gamma) = \sum_{k =
1}^{n} \omega_k \mu_k + \gamma \left(\Omega - \sum_{k=1}^{n-1}\omega_k\right).
$$

This is linear and has no local maxima, so the maximal return must lie at the edge of the
feasible region. In fact, it's clear that we just invest all our money in
the bet with maximum return:

$$
P^* = \Omega B_{k^*}, \quad k^* = \text{argmax}_k\,\mu_k.
$$

But putting all your eggs in one basket seems like a bad idea.
My intuition is that to optimize my portfolio, my investment should
include a spread of high-risk, high-return and low-risk, low-return
bets.
What have we missed?

<div style="background-color: #EAD1DC ; padding: 10px; border: 1px
solid purple; line-height:1.5">
<b>Portfolio optimization.</b> <br>

How do we assess the value of a portfolio so the optimum can
accomodate risk-aversion?
</div>

## Derisky business
---

<div style="background-color: #cfc ; padding: 10px; border: 1px
solid green; line-height:1.5">
<b>Derisked return.</b><br>

We can maximize a convex combination of expected return and (negative)
variance.
</div>

Maximizing expected return ignores the *risk* altogether!
The simplest way to measure the risk of our portfolio is the total variance,

$$
\sigma^2_P = \mathbb{E}[(P - \mu_P)^2].
$$

If the bets are independent random variables, then the variance is
additive, with

$$
\sigma^2_P(\omega_k) = \sum_{k =
1}^{n} \omega_k^2 \sigma^2_k,
$$

where $\sigma^2_k$ is the variance of $B_k$.
If they are not independent, then we add covariance terms:

$$
\sigma^2_P(\omega_k) = \sum_{k = 1}^{n} \omega_k^2 \sigma^2_k + \sum_{j \neq k}
\omega_j\omega_k\text{cov}(B_j, B_k), \quad \text{cov}(B_j, B_k) =
\mathbb{E}[(B_j - \mu_j)(B_k - \mu_k)].
$$

Instead of just maximizing expected return, we should balance return
and risk. A simple way to do this is to maximize the convex
combination of $\mu_k$ and $-\sigma^2_P$, which we'll call the
*$\lambda$-derisked return*:

$$
R_\lambda(\omega_k) = (1 - \lambda) \mu_P(\omega_k) - \lambda \sigma^2_P(\omega_k).
$$

The expected return is $0$-derisked, while $1$-derisked
return minimizes the variance of the portfolio and ignores the return
completely.

## Distributing eggs
---

<div style="background-color: #cfc ; padding: 10px; border: 1px
solid green; line-height:1.5">
<b>Derisking limits.</b><br>

In the $\lambda \to 0$ derisked limit, optimal investments are proportional to
expected return and inverse variance, but as $\lambda \to 1$, to
inverse variance only.
</div>

For simplicity, let's assume our bets are independent.<label for="sn-1"
       class="margin-toggle sidenote-number">
</label>
<input type="checkbox"
       id="sn-1"
       class="margin-toggle"/>
	   <span class="sidenote">Otherwise, we simply diagonalize the
	   covariance matrix and go to a basis of orthogonal bets.</span>
Then adding a Lagrange multiplier as above, we get

$$
\begin{align*}
R_\lambda(\omega_k, \gamma) & = \sum_{k=1}^n
\left[(1-\lambda) \omega_k\mu_k - \lambda \omega_k^2\sigma_k^2\right] +
\gamma \left(\Omega - \sum_{k=1}^n\omega_k\right).
\end{align*}
$$

The partial derivatives are

$$
\partial_{\omega_k} R_\lambda = (1-\lambda)\mu_k + \gamma - 2\lambda
\omega_k \sigma_k^2,
$$

so we have an extremum at

$$
\omega_k = \frac{(1-\lambda)\mu_k + \gamma}{2\lambda \sigma_k^2}.
$$

To determine the value of $\gamma$, note from our constraint that

$$
\begin{align*}
\Omega & = \sum_{k=1}^n\omega_k \\
& = \sum_{k=1}^n\frac{(1-\lambda)\mu_k +
\gamma}{2\lambda \sigma_k^2} \\
\Longrightarrow \quad \gamma
& = 2\lambda\left(\sum_{k=1}^n\frac{1}{\sigma_k^2}\right)^{-1}\left[\Omega -
\sum_{k=1}^n\frac{(1-\lambda)\mu_k}{2\lambda \sigma_k^2}\right].
\end{align*}
$$

Since $\gamma \simeq \lambda$, for small $\lambda$ (a return-oriented investor) we can ignore that
$\gamma$ term. Then the investments

$$
\omega_k \approx \frac{(1 - \lambda)\mu_k}{2\lambda\sigma^2_k} \propto
\frac{\mu_k}{\sigma^2_k},
$$

so we weight investments proportional to expected return, but
inversely to variance. Sounds sensible!
On the other hand, when $\lambda \to 1$ (a risk-averse investor), the Lagrange multiplier
$\gamma \gg (1 - \lambda)\mu_k$, so that the investment is
proportional to the inverse variance only:

$$
\omega_k\approx \frac{\gamma}{2\lambda\sigma_k^2} \propto \frac{1}{\sigma_k^2}.
$$

Intermediate values of $\lambda$ interpolate between these two regimes, with a
degeneracy at $\lambda = 0$ where only expected return matters.
Thus, we have a whole one-parameter family of risk-sensitive ways to value a
portfolio!
