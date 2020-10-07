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
There is a more elegant proof using *expectations*.
Let $x$ be a random variable, with $\langle f(x)\rangle$ the
expectation operator (a sum of outcomes weighted by probability) for
any function $f(x)$.
This operator is linear.
For any constant $C$, we therefore have

$$
\langle (x - C)^2 \rangle = \langle x^2 - 2Cx + C^2 \rangle = \langle x^2 \rangle - 2 C\langle x
\rangle + C^2.
$$

Define $X = \langle x\rangle$. Setting $C = X$ in the expression
above, and then subtracting from the above, we find 

$$
\langle (x - C)^2 \rangle - \langle (x - X)^2 \rangle = X^2 - 2CX +
X^2 = (C - X)^2.
$$

This is precisely the parallel axis theorem in one dimension, where we
identify $X$ with the centre of mass, $I = m\langle (x - C)^2
\rangle$ with the inertia around $C$, and $d = |C - X|$.
For a vectorial random variable $\mathbf{x}= (x_i)$, and constant vector
$\mathbf{C} = (C_i)$, the proof immediately generalizes. In the plane
for instance, we have

$$
\langle |\mathbf{x} - \mathbf{C}|^2 \rangle = \langle (x_1 - C_1)^2
\rangle + \langle (x_2 - C_2)^2 \rangle.
$$

This interpretation makes sense provided we view the normalised mass
density $\rho(\mathbf{x})/m$ as a *probability* density.

#### Diversity of prediction

The one-dimensional parallel axis theorem has a remarkable *social* application.
