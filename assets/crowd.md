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
I = I_\text{cm} + Md^2,
$$

where $M$ is the total mass.
The usual proof involves some distracting and lamentable integrals.
A more elegant approach uses *expectations*.
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
above gives the variance $\sigma^2 = \langle
(x-X)^2\rangle$. Subtracting from the expression involving $C$, we find 

$$
\langle (x - C)^2 \rangle - \langle (x - X)^2 \rangle = X^2 - 2CX +
X^2 = (C - X)^2.
$$

To connect to mass distributions, we identify
the probability $p(x)$ of outcome $x$ with a normalized mass $m(x)/M$.
Then $X$ with the centre of mass, $I = m\langle (x - C)^2
\rangle$ is the inertia around $C$, and setting $d = |C - X|$, we
obtain the parallel axis theorem in one dimension.
For a vectorial random variable $\mathbf{x}= (x_i)$, and constant vector
$\mathbf{C} = (C_i)$, the proof immediately generalizes. In the plane
for instance, we have

$$
\langle |\mathbf{x} - \mathbf{C}|^2 \rangle = \langle (x_1 - C_1)^2
\rangle + \langle (x_2 - C_2)^2 \rangle.
$$

We won't worry about the generalizations here.
Instead, we'll focus on the one-dimensional theorem, due to a
remarkable application in the social sciences: it explains the *wisdom
of the crowd*.

#### Wisdom of the crowd

Suppose that, at a country fair, we ask a group of onlookers to
estimate the weight of the prize pig.
The crowd volunteers some estimates, which we can view as a random
variable $x$, with average $X$.
Suppose $C$ is the correct weight for the pig.
Then the parallel axis theorem gives

$$
(C - X)^2 = \langle (x - C)^2 \rangle - \langle (x - X)^2 \rangle.
$$

The LHS measures the crowd's (squared) error.
The RHS is the average *individual* (squared) error, minus the variance of the
crowd's guess.
In other words, difference of opinion improves the estimate!
The more variance, the better, and in the extreme case, the variance
of guesses cancels individual error so that $X = C$.

The crowd is not wise when individuals are off the mark, but agree
with each other, and the first term is not cancelled by the second.
This makes the peril of groupthink clear in a precise statistical
sense.
In the social sciences, this is called the *diversity of prediction
theorem*, though I personally feel that the *groupthink theorem* is
snappier.

#### Fermi estimates
