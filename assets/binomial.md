---
Layout: post
mathjax: true
comments: true
title:  "Binomial blues"
categories: [Mathematics, Physics, Hacker]
date:  2021-02-06
---

**February 06, 2021.** *Sketchy hacker notes on the binomial approximation.*

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
(1 + x)^r = \lim_{n \to \infty} (1 + x)^{q_n},
$$

where $q_n$ is a sequence of rational numbers (e.g. the decimal
expansion) approximating $r$.
In this case, the binomial approximation gives

$$
(1 + x)^r = \lim_{n \to \infty} (1 + x)^{q_n} \approx 1 + x \lim_{n
\to \infty} q_n = 1 + rx,
$$

and so the result holds for all real numbers.

#### Higher terms

It's possible, if messy, to extend these methods to determine the next
term in the approximation.
We'll do the longcut, and use big-O notation, with $O(x^3)$ in this
context meaning "terms with powers of $x^3$ or higher".
The binomial theorem gives

$$
(1 + x)^n = 1 + nx + \frac{n(n-1)}{2} x^2 + O(x^3), \tag{2} \label{second}
$$

since the coefficient of the $x^2$ term is the number of ways of
choosing $2$ items (the $x$ terms) from $n$ items (the terms in the power).
For a rational $q = m/n$, we have

$$
(1 + x)^{qn} = (1 + x)^m = 1 + mx + \frac{m(m-1)}{2} x^2 + O(x^3),
$$

and if we assume

$$
(1 + x)^{q} = 1 + qx + \gamma x^2 + O(x^3),
$$

then the binomial theorem again gives

$$
(1 + x)^{qn} = \left[1 + qx + \gamma x^2 + O(x^3)\right]^n = 1 + nqx +
\left(n\gamma + \frac{n(n-1)}{2}q^2 \right)x^2 + O(x^3).
$$

The coefficient of the linear term $nq = m$ matches, but the quadratic
term requires more work. Comparing to (\ref{second}) and
rearranging for $\gamma$, we have

$$
\begin{align*}
\gamma  & = \frac{1}{n}\left[\frac{m(m-1)}{2}- \frac{n(n-1)}{2}q^2\right] \\
& =\frac{m(m-1)}{2n}- \frac{m^2(n-1)}{2n^2} \\
& =\frac{q(q - 1)}{2}.
\end{align*}
$$

Thus, we find that to second order,

$$
(1 + x)^q = 1 + qx + \frac{q(q-1)}{2} x^2 + O(x^3)
$$

The extention to real and negative powers is easy. The extension to
higher terms in $x$ is not.
These terms are described the binomial series,

$$
(1 + x)^\alpha = \sum_{k = 0}^\infty \frac{\alpha(\alpha - 1)\cdots
(\alpha-k +1)}{k!} x^k
$$

and I have no idea how to derive this without calculus.
