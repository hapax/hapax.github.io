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
Here, we present a sketchy shortcut and an elementary longcut.

#### Sketchy shortcut

We begin with the shortcut.
In an
[earlier post](https://hapax.github.io/maths/physics/hacks/exponential/),
I derived the following result for the exponential, and $|x| \ll 1$:

$$
e^x \approx 1 + x.
$$

The natural logarithm is the inverse of this, so

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
