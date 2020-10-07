---
Layout: post
mathjax: true
comments: true
title:  ""
categories: [Physics, Mathematics, Statistics]
date:  2020-10-07
---

**October 7, 2020.** *Bla bla bla Fermi estimates bla bla diversity of
  prediction*

#### The parallel axis theorem

In a first-year mechanics course, one is usually obliged to prove the
*parallel axis theorem* that the moment of inertia $I_\text{cm}$
around the centre of mass, and the moment $I$ around any parallel axis
a distance $d$ away, are related by

$$
I = I_\text{cm} + md^2.
$$

The proof usually involves some lamentable sequence of integrals.
There is a quick and much more general proof using *expectations*.
Let $x$ be a random variable, with $\langle f(x)\rangle$ the
expectation operator (a sum of outcomes weighted by probability) for
any function $f(x)$.
This operator is linear.
For any constant $C$, we therefore have

$$
\langle (x - C)^2 \rangle = \langle x^2 \rangle - 2 C\langle x
\rangle + C^2.
$$

Define $X = \langle x\rangle$. Setting $C = X$ in the expression
above, and then subtracting from the above, we find 

$$
\langle (x - C)^2 \rangle - \langle (x - X)^2 \rangle = X^2 - 2CX +
X^2 = (C - X)^2.
$$
