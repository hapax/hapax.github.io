---
Layout: post
mathjax: true
comments: true
title:  "The statistical basis of Fermi estimates"
categories: [Physics, Hacks, Mathematics, Statistics]
date:  2021-02-12
---

**February 12, 2021.** *Why are Fermi approximations so effective? One
  important factor is log normality, which occurs for large random
  products. <!--, also related to the mechanism underlying
  the Newcomb-Benford law for first digits.--> Another element is
  variance-reduction through judicious subestimates. I give some
  tips for the latter.*

#### Introduction

Fermi approximation is the art of making good order-of-magnitude estimates.
I've written about them
at greater length
[here](https://hapax.github.io/assets/fermi-estimates.pdf) and
[here](https://hapax.github.io/physics/teaching/hacks/napkin-hacks/#sec-3),
but I've never really found a satisfactory explanation for why they work.
Order-of-magnitude is certainly a charitable margin of 
error, but time and time again, I find they are better than they have any right to be!
Clearly, there must be an underlying statistical explanation for this apparently
unreasonable effectiveness.

<!-- We will try to explain the first using logarithmic uniformity, which is
the same mechanism underlying the anomalous distribution of first
digits known as the
[Newcomb-Benford law](https://en.wikipedia.org/wiki/Benford%27s_law).
We give a looser but related explanation of the second in terms of strategies for
variance-reduction in human error. -->

#### Products and log-normality

There are two key techniques: the use of geometric means, and the
factorisation into subestimates.
We start with geometric means.
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

where the $Y_i$ have mean $\mu_i$ and variance $\sigma_i^2$.
We say that $F$ has a *log-normal* distribution, since its log is
normal.

<!-- To get uniformity into the picture, we can zoom in on the region near
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
This is what we mean when we say that $F$ is logarithmically uniform. -->

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
Incidentally, this also illustrates the
[wisdom of the crowd](https://hapax.github.io/physics/mathematics/statistics/crowd/),
also called "diversity of prediction".
The individual errors from a broad spread of guesses tend to cancel
each other out, leading to a better-behaved average, though in this case
in logarithmic space.

In general, Fermi estimates work best for numbers which are large
random products (this is how we try to solve them!), so the problem
domain tends to enforce the statistical properties we want.
For many examples of log-normal distributions in the real world, see
[Limpert, Stahel and Abbt (2001)](https://academic.oup.com/bioscience/article/51/5/341/243981).
It's worth noting that not everything we can Fermi estimate is
log-normal, however.
Many things in the real world obey power laws, for instance, and
although you can exploit this to make better Fermi estimates (as
lukeprog does in
[his tutorial](https://www.lesswrong.com/posts/PsEppdvgRisz5xAHG/fermi-estimates#Example_4__How_many_plays_of_My_Bloody_Valentine_s__Only_Shallow__have_been_reported_to_last_fm_)),
we can happily Fermi estimate power-law distributed numbers without
this advanced technology.

Are Fermi estimates unreasonably effective in this context?
Maybe.
But the estimates work best in the high-density core where things look
uniform, not out at the tails, and it's not until we get to the tails that the difference
between the log-normal and power law (or exponential, or Weibull, or
your favourite skewed distribution) becomes pronounced.
So the unreasonable effectiveness here can probably be explained by
the resemblance to the log-normal, though this is something I'd like
to check more carefully in future.

<!-- In general, we only expect Fermi estimates to work for numbers which
are the product of many factors.
But this is precisely the sorts of things we use Fermi estimates for!
In a sense, the problem domain naturally leads to logarithmic
uniformity.
Incidentally, I've talked about "uniformity", but the geometric mean
is still a measure of central tendency for any distribution, and is
particularly nice for a lognormal one, which arise for products of
random variables.
The magic of geometric means manifests most
strongly in the near-uniform blob at the centre. -->

<!-- #### The Newcomb-Benford law

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
of a big random product, then $\log_b X$ is uniformly
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

Here is the Python code to generate it.
You can check it for other numbers besides $2$ as well by simply
changing the `power` variable:

```python
import matplotlib.pyplot as plt
import math

maxpower = 10000 # Number of powers to check
power = 2 # Change to check other powers

nums = '1', '2', '3', '4', '5', '6', '7', '8', '9',
benford = [(math.log(10, d+1) - math.log(10, d+1))
    for d in range(1, 10)]
firstdig = [0 for i in range(9)]
for i in range(maxpower):
	ind = int(str(power**i)[0]) - 1
	firstdig[ind] = firstdig[ind] + 1

fig, ax = plt.subplots()
fig.set_facecolor('white')
ax.pie(firstdig, labels=nums, autopct='%1.1f%%', startangle=90)
    # Change 'firstdig' to 'benford' for probabilities
ax.axis('equal')
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
logarithmic uniformity, and the Newcomb-Benford law results. -->

#### The philosophy of subestimates

Now we've dealt with geometric means and log-normality, we
turn to the effectiveness of factorising a Fermi estimate.
If we take logarithms, factors become summands, and we'll reason about those since they are simpler.
If $Z = X + Y$ is a sum of independent random variables, the variance
is additive, so that

$$
\text{var}(Z) = \text{var}(X) + \text{var}(Y).
$$

Thus, splitting a sum into estimates of the summands and adding them
should not change the variance of the guess.
Of course, there is a fallacy in this reasoning: humans are not
sampling from the underlying distribution!
When we guess, we introduce our own random errors.
For instance, my estimate for $Z$ will have some human noise $\varepsilon_Z$:

$$
\hat{Z} = Z + \varepsilon_Z.
$$

Similarly, my guesses for $X$ and $Y$ have some random errors
$\varepsilon_X$ and $\varepsilon_Y$.
There is no reason for the variances of $\varepsilon_X$ and $\varepsilon_Y$
to add up to the variance of $\varepsilon_Z$.
The sum could be bigger, or it could be smaller.
But a good decomposition should reduce the combined variance:

$$
\text{var}(\varepsilon_X) + \text{var}(\varepsilon_Y) < \text{var}(\varepsilon_Z).
$$

If log-normality is the science of Fermi estimates, picking
variance-reducing subestimates is the art.
<!-- But there is a connection to our earlier discussion.
I think the human error $\varepsilon_X$ will roughly mimic the
empirical distribution of $Z$ we have seen in the world.
If it is biased, so is $\varepsilon_X$; it we have only seen a few
examples, the variance of $\varepsilon_X$ will probably be large, and
decrease roughly as $1/k$ with $k$ examples.
So the general strategy for variance reduction is to factorise into
things we have seen before.
We can even use these data points to generate subestimates by geometric averaging.-->
But I suspect that $\hat{Z}$ roughly speaking behaves like a *test
statistic* for $Z$, with the number of samples corresponding to how
many data points for $Z$ we have encountered.
So we expect that $\text{var}(\varepsilon_Z)$ will vanish roughly as
$1/k$ with $k$ samples.
If we have more exposure to the distributions for $X$ and $Y$,
the combined error will probably be smaller.
This is why we carve into subfactors we understand!

#### Variance reduction in practice

I'll end with a speculative rule of thumb for when to factor: try generating over- and
underestimates for the factors and the product, which in additive
notation give

$$
(\Delta X)^2 + (\Delta Y)^2, \quad (\Delta Z)^2
$$

where $\Delta$ refers to the difference of the (logarithm of the) over-
and underestimate.
Factorise if the first estimated error is smaller than the second.
Let's illustrate by returning to the population of Chile.
I can try factoring it into a number of regions multiplied by the
average number of people per region.
Taking logs (in base $10$) of the over- and underestimate of Chile's
population I gave above, I get

$$
(\Delta Z)^2 = (\log_{10} 10^8 - \log_{10} 10^6)^2 = 4.
$$

On the other hand, for regions I would
make a lower guess of $5$ and an upper guess of $30$, with a difference in logs of $(\Delta X)^2 = 0.6$.
For regional population, I would make a lower guess of $5\times 10^5$ and an
upper guess of $5\times 10^6$, with $(\Delta Y)^2 = 1$.
Thus,

$$
(\Delta X)^2 + (\Delta Y)^2 = 1.6 < 4 = (\Delta Z)^2.
$$

The guess from the factorisation (taking geometric means) is

$$
\sqrt{5 \times 30 \times (5\times 10^5) \times (5\times 10^6)} \approx 19 \text{
million}.
$$

This is even better than the crowdsourced estimate!
For reference, the number of regions is $16$, while our estimated mean is around
$12$, and the average population per region is a bit over a million,
which we've mildly overestimated at $1.6$ million.
The two balance out and give a better overall estimate.
<!-- This suggests a diversity of prediction mechanism is at play with -->
<!-- subestimates, but I haven't worked out the details. -->

#### Conclusion

From a statistical perspective, Fermi estimates are based on two
techniques: geometric means and splitting into subfactors.
We usually estimate things which can be expressed as a product of many
factors. These will tend towards a log-normal distribution by the (log
of the) central limit theorem, so that geometric means provide a good
estimator, exactly like the usual mean for normally distributed variables.
Subestimates, on the other hand, carve guesses into factors we
understand, i.e. have more data points for, so that (assuming they
behave like test statistics) variance is reduced.
The effectiveness of Fermi estimates is quite reasonable after all!
<!-- They're not so unreasonable after all! -->

<!-- There is an art to making over- and underestimates
that accurately reflect the variance of our error random variables,
which are involved both in taking geometric means for single
quantities, and reducing variance through subestimates. 
Still, it's cool that there is a statistical basis for the different
aspects of the effectiveness of Fermi estimates.
It's not so unreasonable after all! -->

<!-- For instance, if $e^Z$ is the population of Chile, I can factor it
into number of provinces $e^X$ multiplied by the average number of people per province $e^Y$.
But this is likely to *increase* the error, since I know less about
provinces of Chile than I do about Chile compared to other countries.
I suspect that there is a nice quantitative connection to be made
between the variance of $\varepsilon_X$ and the prior data I have on
it. -->

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
