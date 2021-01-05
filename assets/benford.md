---
Layout: post
mathjax: true
comments: true
title:  "Logarithmic uniformity and Fermi estimates"
categories: [Physics, Hacks, Mathematics, Statistics]
date:  2021-01-04
---

**January 4, 2021.** *Why are Fermi approximations so effective? One
  important factor is logarithmic uniformity, which occurs for products of
  many random variables. Interestingly, this is the same mechanism
  behind the Newcomb-Benford law for first digits.*

#### Introduction

Fermi approximation is the art of making good order-of-magnitude estimates.
I've written about them
at greater length
[here](https://hapax.github.io/assets/fermi-estimates.pdf) and
[here](https://hapax.github.io/physics/teaching/hacks/napkin-hacks/#sec-3),
but I've never really found a satisfactory explanation for why it is so effective.
It's not just that order-of-magnitude provides a charitable margin of
error.
Even given this latitude, I've found that time and time again, they
are better than they have any right to be!

Clearly, there must be an underlying statistical explanation for this
unreasonable effectiveness.
Roughly speaking, it is *logarithmic uniformity*, the same mechanism underlying the
curious distribution of first digits known as the
[Newcomb-Benford law](https://en.wikipedia.org/wiki/Benford%27s_law).
We'll talk about uniformity, then zero in on Fermi estimates and
Newcomb-Benford law in turn.

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

By the central limit theorem for unlike variables (see
e.g. [this post](https://hapax.github.io/hacks/mathematics/statistics/clt/)),
for large $N$ this approaches a normal distribution:

$$
\log F \to \mathcal{N}(\mu, \sigma^2), \quad \mu := \sum_i \mu_i,
\quad \sigma^2 = \sum_i \sigma_i^2,
$$

where the $Y_i$ has mean $\mu_i$ and variance $\sigma_i^2$.
We say that $F$ has a *log-normal* distribution, since its log is
normal.
To get uniformity into the picture, we can zoom in on the region near
$F = e^\mu$ where the probability density is approximately uniform.
More carefully, the density is

$$
p(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-(x-\mu)^2/2\sigma^2}.
$$

Taylor-expanding near $x = \mu$ gives

$$
p(x) = \frac{1}{\sigma\sqrt{2\pi}}
\left[1 - \frac{(x-\mu)^2}{2\sigma^2} + O(x^4)\right].
$$

This looks uniform provided $(x - \mu)^2 \ll \sigma^2$.
For instance, at a third of a standard deviation, $x = \mu + \sigma/3$,
we have

$$
1 - \frac{(x-\mu)^2}{2\sigma^2} = 1 - \frac{1}{18} \approx 0.94,
$$

and $\text{erf}(1/\sqrt{18}) \approx 0.26$, about a quarter of the
probability mass, lies underneath.
This is what we mean when we say that $F$ is logarithmically uniform.

#### Geometric means

In Fermi estimates, one of the basic techniques is to take geometric
means of estimates, typically an overestimate and an underestimate.
For instance, to Fermi estimate the population of Chile, I could
consider a number like one million which seems much too low, and a
number like one hundred million which seems much too high, and take
their geometric mean:

$$
\sqrt{(1 \text{ million}) \times (100 \text{ million})} = 10 \text{ million}.
$$

Since population is a product of many different factors, it is
reasonable to expect it to approximate a log-normal distribution.
Then, after logs, the geometric mean $\sqrt{ab}$ becomes the
arithmetic mean of $\log a$ and $\log b$:

$$
\log \sqrt{ab} = \frac{1}{2}(\log a + \log b).
$$

Taking the mean $\mu$ of the distribution as the true value, these
geometric means provide an
[unbiased estimator](https://en.wikipedia.org/wiki/Bias_of_an_estimator)
of the mean.
Moreover, the error of the estimate will decrease as $1/k$ for $k$
samples (assuming human estimates sample from the distribution), so more is better.
To see how much better I could do on the Chile population estimate, I
solicited guesses from four friends, and obtained $20, 20, 30$ and $35$
million.
Combining with my estimate, I get a geometric mean

$$
(10 \times 20 \times 20 \times 30 \times 35)^{1/5} \text{ million}
\approx 21 \text{ million}.
$$

The actual population is around $18$ million, so the estimate made
from more guesses is indeed better!
This is also better than the arithemetic average, $23$ million.
This also illustrates the
[wisdom of the crowd](https://hapax.github.io/physics/mathematics/statistics/crowd/),
also called "diversity of prediction".
The individual errors from a broad spread of guesses tend to cancel
each other out, lead to a better-behaved average, though in this case
in logarithmic space.

#### The Newcomb-Benford law

Logarithmic uniformity also explains an odd pattern in the first
digits of naturally occurring numbers like tax returns, stock market
prices, populations, river lengths, physical constants, and even
powers of $2$.
The pattern, called the *Newcomb-Benford law* after
[Simon Newcomb](https://en.wikipedia.org/wiki/Simon_Newcomb) and
[Frank Benford](https://en.wikipedia.org/wiki/Frank_Benford), is as
follows: for base $b$, the digit $d \in \\{1, 2, \ldots, b-1\\}$
occurs with relative frequency

$$
p_b(d) = \log_b \left(\frac{d+1}{d}\right) = \frac{1}{\log b}\log \left(\frac{d+1}{d}\right).
$$

It initially seems bizarre that digits do not occur with equal
frequency.
But as neatly explained by
[Pietronero et al. (1998)](https://arxiv.org/pdf/cond-mat/9808305.pdf),
it follows immediately if the relevant numbers are logarithmically uniform.
Let $X$ be our random number.
Then the first digit is $d$ if

$$
db^k \leq X < (d+1)b^{k} \quad \Longrightarrow \quad \log_b d + k \leq
\log_b X < \log_b(d+1) + k
$$

for some integer $k$.
If $X$ is logarithmically uniform, for instance sitting near the mean
of a product of man variables, then $\log_b X$ is uniformly
distributed, and lies in the interval $I_d :=
[\log_b d, \log_b (d+1)]$ with probability

$$
(\log_b (d+1) + k) - (\log_b d + k) = \frac{1}{\log b}\log \left(\frac{d +
1}{d}\right) = p_b(d).
$$

This provides a simple way to check for fraud on tax returns, for
instance.
Just compute relative frequencies of first digits in different bases
and check they obey Newcomb-Benford!
You might wonder why something totally deterministic, like the first
digit of a power of $2$, also obeys Benford's law.
Here is a pie chart of initial decimal digits for the first $10,000$ binary
powers, which follows the Newcomb-Benford law exactly:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/benford1.png"/>
	</div>
	</figure>

Here is the Python code to generate it:

```python
import matplotlib.pyplot as plt
import math

maxpower = 10000 # Change for more or less powers
power = 2 # Change for different powers

labels = '1', '2', '3', '4', '5', '6', '7', '8', '9',
benford = [(math.log(10, d+1) - math.log(10, d+1))
    for d in range(1, 10)]
firstdig = [0 for i in range(9)]
for i in range(maxpower):
	ind = int(str(power**i)[0]) - 1
	firstdig[ind] = firstdig[ind] + 1

plt.figure(0)
fig1, ax1 = plt.subplots()
ax1.pie(firstdig, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)
    # Change 'firstdig' to 'benford' if you
	# want check match to Newcomb-Benford
ax1.axis('equal')
plt.show()
```

The mechanism for logarithmic uniformity here is slightly different,
and discussed in depth in Serge Tabachnikov's
[book on geometric billiards](http://www.personal.psu.edu/sot2/books/billiardsgeometry.pdf).
In this case, $X = 2^n$, so the first digit is $d$ just in case

$$
\log_{10}d + k \leq n\log_{10} 2 < \log_{10}(d + 1) + k.
$$

Let $\text{frac}(x)$ denote the fractional part of $x$, and define
$x_n := \text{frac}(n\log_{10} 2)$.
Taking fractional parts gives

$$
\log_{10}d \leq x_n < \log_{10}(d + 1).
$$

It turns out that, since $x_1 = \log_{10} 2$ is irrational,
$x_n$ jumps randomly around the unit interval, and forms an
"equidistribution" which spends equal times in equal areas.
For a proof, see Tabachnikov's book.
But although the fundamental cause is different, the outcome is still
logarithmic uniformity, and the Newcomb-Benford law results.

#### Subestimates

<!--
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
converges to. -->

<!-- https://arxiv.org/pdf/cond-mat/9808305.pdf -->
