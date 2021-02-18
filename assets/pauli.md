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

This will be our key hack!

#### Humble Hadamard

One of the most important gates in universal quantum computing is the
Hadamard gate, since it is used to generate entanglement from
unentangled input states. Our basic observation is that

$$
H = \frac{1}{\sqrt{2}} = \begin{bmatrix}
1 & 1 \\
1 & -1 \\
\end{bmatrix} = \frac{1}{\sqrt{2}}(X + Z).
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

Another important property of $H$ is that it takes the basis states
$|0\rangle$ and $|1\rangle$ to eigenstates of $X$. To see this, we
first note from (\ref{ops}) that

$$
X(X + Z) = X^2 + XZ = Z^2 + XZ = (X + Z)Z.
$$

Hence, using the fact that $Z|n\rangle = (-1)^n|n\rangle$ for $n = 0,
1$, we get

$$
XH|n\rangle = \frac{1}{\sqrt{2}}X(X + Z)|n\rangle =
\frac{1}{\sqrt{2}}(X + Z)Z|n\rangle  = (-1)^nH|n\rangle.
$$

Thus, $H|n\rangle$ is an eigenstate of $X$ with eigenvalue $(-1)^n$,
with $|+\rangle = H|0\rangle$ and $|-\rangle = H|1\rangle$.
Since $H^2 = I$, we can run this argument backwards to conclude that
$H|\pm\rangle$ return the eigenstates of $Z$.
This may seem trivial, but combining these two results implies that
the eigenstates of $H$ itself can be written

$$
|H_\pm\rangle = \frac{1}{\sqrt{2}}(|+\rangle \pm |0\rangle).
$$

Let's check:

$$
H|H_\pm\rangle = \frac{1}{\sqrt{2}}(H|+\rangle \pm H|0\rangle) =
\frac{1}{\sqrt{2}}(|0\rangle \pm |+\rangle) = \pm|H_\pm\rangle.
$$

I think this algebraic approach is nicer than explicitly solving an
eigenvalue equation.
If we use $H$ to make observations, then it's also easy to check the
probability of observing $|H_\pm\rangle$ for a state written in terms
of the computational basis, $|\psi\rangle = \alpha |0\rangle +
\beta|1\rangle$.
We just use known overlaps:

$$
\begin{align*}
\langle H_\pm |\psi \rangle & =
\frac{1}{2}\left[\alpha\langle +|0\rangle \pm \langle 0|0\rangle + \beta \langle +|1\rangle \pm \langle 0|1\rangle \right]\\
& =
\frac{1}{2}\left[\frac{\alpha}{\sqrt{2}} + \frac{\beta}{\sqrt{2}} \pm 1\right]\\
\Longrightarrow \quad p(H = \pm 1) & = |\langle H_\pm |\psi \rangle|^2
= \frac{1}{4}(\alpha + \beta \pm \sqrt{2})^2.
\end{align*}
$$

And if you're wondering about the overlaps $\langle +|n\rangle$,
there's a shortcut for computing those too:

$$
\langle + | n\rangle = \langle 0 | H |n\rangle =
\frac{1}{\sqrt{2}}\langle 0|(X+Z)|n\rangle =
\frac{1}{\sqrt{2}}(\langle 1|n\rangle + (-1)^n\langle 0|n\rangle) = \frac{1}{\sqrt{2}}(-1)^n.
$$

#### Easy entanglement
