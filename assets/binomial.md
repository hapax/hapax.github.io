---
Layout: post
mathjax: true
comments: true
title:  "Binomial blues"
categories: [Mathematics, Physics, Hacker]
date:  2021-01-28
---

**January 28, 2021.** *More sketchy hacker maths.*

#### Introduction

The binomial approximation is the result that, for any real $\alpha$,
and $|x| \ll 1$,

$$
(1 + x)^\alpha \approx 1 + \alpha x.
$$

The usual proof involves calculus.
Here, we present a sketchy shortcut and an elementary longcut, neither
of which involves calculus.

#### Sketchy shortcut

We begin with the shortcut.
In an
[earlier post](https://hapax.github.io/maths/physics/hacks/exponential/),
I derived the following result for the exponential, and $|x| \ll 1$:

$$
e^x \approx 1 + x.
$$

The natural logarithm is the inverse function, so

$$
x = \log e^x \approx \log(1 + x).
$$

Recall that

$$
x^n = (e^{\log x})^n = e^{n\log x} \quad \Longrightarrow \quad \log x^n = n \log x.
$$

Thus, taking the logarithm $(1 + x)^\alpha$, we have

$$
\log [(1+x)^\alpha] = \alpha \log (1+ x) \approx \alpha x,
$$

and hence

$$
(1+x)^\alpha \approx e^{\alpha x} \approx 1 + \alpha x.
$$

This works since all the corrections are at higher order in $x$.

#### Elementary longcut

There is a more elementary approach which effecitvely does the same
thing.
The basic point is first to note that, from the binomial theorem,

$$
(1 + x)^n = 1 + \binom{n}{1}x + \binom{n}{2}x^2 + \cdots x^n \approx
1 + nx
$$

for $|x| \ll 1$, since the higher order terms are much smaller.
So the binomial approximation is true for whole numbers $n$.
If we consider a fraction $q = m/n$, then $(1 + x)^q$ raised to the
power $n$ should equal

$$
(1 + x)^{qn} = (1 + x)^{m} \approx 1 + mx \tag{1}\label{m}
$$

by the binomial theorem.
Let's assume

$$
(1 + x)^{q} \approx 1 + \beta x,
$$

with some higher order terms we can ignore.
Raising to the power $n$, we can use the binomial approximation for
$n$ to get

$$
(1 + x)^{qn} \approx (1 + \beta x)^n \approx 1 + \beta n x.
$$

Comparing to (\ref{m}), we find that $\beta = m/n$, and hence the
binomial approximation is true for positive rationals.
We can add negative powers using the geometric series:

$$
\frac{1}{1 - x} = 1 + x + x^2 + \cdots \approx 1 + x,
$$

and hence for a negative rational $q = -m/n$,

$$
(1 + x)^q \approx (1 - x)^{m/n} \approx 1 - \frac{m}{n}x = 1 + qx,
$$

as required. Finally, there is arbitrary real $\alpha$. This is
actually trivial, in some sense.
Unlike whole numbers (repeated multiplication), fractions (roots), or
negative numbers (reciprocals), an irrational power has no obvious
interpretation. The most reasonable thing to do is define it as a
*limit* of rational powers that approximate it:

$$
(1 + x)^r = \lim_{n \to \inty} (1 + x)^{q_n},
$$

where $q_n$ is a sequence of rational numbers (e.g. the decimal
expansion) approximating $r$.
