---
Layout: post
mathjax: true
comments: true
title:  "Painless Paulis"
categories: [Physics, Mathematics, Hacks, QC]
date:  2021-02-18
---

**February 18, 2021.** *Quick tips for avoiding nasty
  algebra with Pauli matrices.*

#### Introduction

In elementary quantum computing, you spend a lot of time
doing messy, explicit calculations with $2\times 2$ matrices.
Sometimes this is unavoidable, but sometimes, there are shortcuts
which let us bypass this mess.
Let's remind ourselves of the basic objects, the Pauli matrices:

$$
\sigma_1 = X = \begin{bmatrix}
0 & 1 \\
1 & 0 \\
\end{bmatrix}, \quad
\sigma_2 = Y = \begin{bmatrix}
0 & -i \\
i & 0 \\
\end{bmatrix}, \quad
\sigma_3 = Z = \begin{bmatrix}
1 & 0 \\
0 & -1 \\
\end{bmatrix}.
$$

We won't really need these! Instead, we'll only be using the algebraic
relations

$$
\sigma_a \sigma_b = \delta_{ab}I + i \epsilon_{abc}\sigma_c,
$$

where $I$ is the $2\times 2$ identity matrix, $\delta_{ab}$ is $1$ if
$a = b$ and $0$ otherwise, and $\epsilon_{abc}$ is $1$ when $abc$ is
an even permutation of $123$, $-1$ if it's odd, and $0$ otherwise.
We are also using the Einstein summation notation, where the repeated
index $c$ is summed over.
As special cases, we have

$$
X^2 = Z^2 = I, \quad XZ = -XZ. \tag{1} \label{ops}
$$

This will be our key result!

#### Hadamard made easy

One of the most important gates in universal quantum computing is the
Hadamard gate, since it is used to generate entanglement from
unentangled input states. Our basic observation is that

$$
H = \frac{1}{\sqrt{2}} = \begin{bmatrix}
1 & 1 \\
1 & -1 \\
\end{bmatrix} = \frac{1}{\sqrt{2}}(X + Z). \tag{2} \label{had}
$$

We can first check that the inverse of $H$ is itself, i.e. $H^2 = I$.
This follows from (\ref{ops}), since

$$
\begin{align*}
H^2 & = \frac{1}{2}(X + Z)^2 \\
& = \frac{1}{2}(X^2 + XZ + ZX + Z^2) \\
& = \frac{1}{2}(X^2 + XZ - XZ + Z^2) = \frac{1}{2}(X^2 + Z^2) = I.
\end{align*}
$$
