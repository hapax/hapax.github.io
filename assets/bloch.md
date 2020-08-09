---
Layout: post
mathjax: true
comments: true
title:  "The Bloch sphere and Hopf fibrations"
categories: [Physics, Mathematics]
date:  2020-08-09
---

**August 9, 2020.** *The Bloch sphere represents the geometry
  of single qubit states. Remarkably, it is equivalent
  to the Hopf fibration. I give a quick proof of this
  result, and discuss the generalization to pure states of two and
  three qubits, which (with a little more work) are equivalent to
  fibrations of the seven- and fifteen-sphere.* 

#### The Bloch sphere

A classical bit is $0$ or $1$.
A quantum bit, or *qubit*, is a *complex linear combination* of $0$ and $1$,
considered as vectors:

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle, \quad \alpha, \beta
\in \mathbb{C}^2.
$$

We would like to interpret $|\alpha|^2$ and $|\beta|^2$ as the
respective probabilities of measuring $0$ and $1$.
For this to make sense, they must satisfy the normalization condition
$|\alpha|^2 + |\beta|^2 = 1$.
But, writing this out in terms of the real and imaginary components
$\alpha = a + ib, \beta = c + id$, we have

$$
a^2 + b^2 + c^2 + d^2 = 1.
$$

This defines a *sphere* in four-dimensional space $\mathbb{R}^4$.
Since the sphere itself has three dimensions (it can be locally
parameterized by $a$, $b$ and $c$), we call this the three-sphere
$\mathbb{S}^3$.

There is one more ambiguity to worry about.
Suppose that we rotate our qubit $|\psi\rangle$ by a phase,
$e^{i\gamma}$.
Just making observations of the qubit alone, this phase is
unobservable, since the probabilities don't change,
i.e. $|e^{i\gamma}\alpha|^2 = |\alpha|^2$.
We call this the *global* phase ambiguity, and identify

$$
|\psi\rangle \sim e^{i\gamma}|\psi\rangle.
$$

We can view this ambiguity as identifying a *circle* of states on the
three-sphere $|\alpha|^2 + |\beta|^2 = 1$.
This seems likely to be a horrible mess.
But miraculously, it works out rather nicely!
We'll show this in an elementary way here, and do something more slick
in the next section.
