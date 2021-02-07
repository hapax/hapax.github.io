---
Layout: post
mathjax: true
comments: true
title:  "Binomial party tricks"
categories: [Mathematics, Physics, Hacker]
date:  2021-02-06
---

**February 06, 2021.** *Sketchy hacker notes on the binomial
  approximation, paying off in some party trick arithmetic.*

#### Introduction

The binomial approximation is the result that, for any real $\alpha$,
and $|x| \ll 1$,

$$
(1 + x)^\alpha \approx 1 + \alpha x.
$$

The usual proof involves calculus.
Here, we present a sketchy shortcut and an elementary longcut, neither
of which involves calculus, strictly speaking.
We also derive the quadratic term, and end with a fun application to
finding roots.

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

#### Rooting out answers

The applications are many and various, but the most obvious and fun is
to quickly calculating roots.
For instance, suppose someone asks you to find the square root of $8$.
You look for a nearby perfect square, in this case $9$, then factor
eight into $9$ times one minus something small:

$$
\sqrt{8} = \sqrt{9\left(1 - \frac{1}{9}\right)} = 3 \left(1 - \frac{1}{9}\right)^{1/2}.
$$

We can take $\alpha = 1/2$ and $x = -1/9$ in the binomial
approximation, and see how we go, noting that

$$
\sqrt{1 - x} = 1 - \frac{1}{2}x - \frac{1}{8}x^2 + O(x^3).
$$

To first order, we get

$$
3 \left(1 - \frac{1}{9}\right)^{1/2} \approx 3\left[1 - \frac{1}{2} \cdot \frac{1}{9}\right]
= \frac{17}{6} \approx 2.83.
$$

To second order,

$$
3 \left(1 - \frac{1}{9}\right)^{1/2} \approx
3\left[1 - \frac{1}{2} \cdot \frac{1}{9} - \frac{1}{8} \cdot \frac{1}{9^2}\right]
= \frac{611}{216} \approx 2.829.
$$

The actual answer is $\sqrt{8} = 2.828$, so even the first term in the
binomial approximation is very good! We'll finish with a somewhat more
involved example.
Let's approximate the fifth root of six, $6^{1/5}$.
I only know one fifth power of the top of my head, $2^5 = 32$, and
this happens to be near $6^2 = 36$.
We can chain these observations together as follows:

$$
\begin{align*}
6^{1/5} & = 36^{1/10} \\
	& = 32^{1/10}\left(1 + \frac{1}{9}\right)^{1/10} \\
	& =\sqrt{2}\left(1 + \frac{1}{9}\right)^{1/10} \\
	& \approx \sqrt{2} \cdot \frac{91}{90}.
\end{align*}
$$

At this point, we could separately approximate $\sqrt{2}$, but I
happen to know it's about $1.414$, so I can plug this in and get the
estimate

$$
\sqrt[5]{6} \approx 1.43.
$$

Consulting a calculator, I find this is correct to two decimal places!
