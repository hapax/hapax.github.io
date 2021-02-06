---
Layout: post
mathjax: true
comments: true
title:  "Unitary orbits for density matrices"
categories: [Maths, Physics, QC]
date:  2021-02-05
---

**February 5, 2021.** *Some brief musings on the structure of unitary orbits
  for density matrices, attempting to generalise the nested spheres of
  the Bloch ball.*

#### Introduction

The [Bloch sphere](https://en.wikipedia.org/wiki/Bloch_sphere)
represents the space of pure states on a single qubit (see also
[this](https://hapax.github.io/physics/mathematics/bloch/) recent
post).
The "Bloch ball" is the space of all *density matrices* on the qubit.
It fills in the Bloch sphere with concentric spheres of increasing
mixedness, and at the centre is the maximally mixed state $I_2/2$,
where $I_d$ will denote the $d \times d$ identity matrix.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/unitary1.png"/>
	</div>
	</figure>

Spheres arise naturally.
They carry the structure of the unitary group $\mathrm{U}(2)$ acting
on qubits, once we have modded out by the phase ambiguity:

$$
\frac{\mathrm{U}(2)}{\mathrm{U}(1)} = \mathrm{SU}(2).
$$

This is a double cover of the rotation group $\mathrm{SO}(3)$, which
acts transitively on the sphere.
(The "double cover" part gives us spinors.)
Thus, spheres occur naturally as unitary orbits, and indeed, each
concentric sphere in the Bloch ball is such an orbit.
The question is whether this generalises nicely to higher dimensions.

#### The Bloch ball

Let's think about the Bloch ball in a little more detail.
Each density matrix $\rho$ is a $2\times 2$ matrix acting on the space
of qubits, which is positive and has unit trace.
Positivity just means that, for every state $|\psi\rangle$,

$$
\langle \psi | (\rho | \psi \rangle) \geq 0.
$$

Hence, $\rho$ is Hermitian, since the reality of this inner product implies

$$
\langle \psi | (\rho | \psi \rangle) = (\langle \psi | \rho^\dagger)
|\psi \rangle \quad \Longrightarrow \quad \rho = \rho^\dagger.
$$

In turn, this means that $\rho$ is unitarily diagonalisable,
i.e. $U^\dagger \rho U = \Lambda$ for some diagonal matrix $\Lambda$.
It's also clear these eigenvalues must be positive.
In fact, since the permutation matrices are unitary, we can arrange
the eigenvalues in decreasing size, so that every $2 \times 2$ density
matrix is unitarily equivalent to some matrix

$$
\Lambda(p) =
\begin{bmatrix}
p & \\
& 1-p 
\end{bmatrix}
$$

for $p \in [1/2, 1]$.
The maximally mixed density $I_2/2$ has a trivial orbit, since it
always gets mapped to itself:

$$
U^\dagger I_2 U = U^\dagger U = I_2.
$$

We can measure the distance from this matrix to $\Lambda(p)$ using the
Frobenius norm, aka Hilbert-Schmidt norm.
This is just the usual vector norm where we treat a matrix $A = [a_{ij}]$ as a big vector:

$$
||A||^2 = \sum_{ij} |a_{ij}|^2 = \mbox{Tr}[A^\dagger A].
$$

Hence,

$$
\begin{align*}
||\Lambda(p) - \tfrac{1}{2}I_2||^2 & = \left|\left| \begin{bmatrix}
p - 1/2 & \\
& 1/2-p 
\end{bmatrix} \right|\right|^2
\end{align*} = 2\left(p - \tfrac{1}{2}\right)^2.
$$

It's easy to see that any density in the unitary orbit of $\Lambda(p)$
has the same distance, since we can use $I_2 = U^\dagger I_2 U$:

$$
\begin{align*}
||U^\dagger \Lambda U - \tfrac{1}{2}I_2||^2 & =
\mbox{Tr}\left[(U^\dagger \Lambda U - \tfrac{1}{2}I_2)^\dagger (U^\dagger \Lambda U - \tfrac{1}{2}I_2)\right]\\
& =
\mbox{Tr}\left[U^\dagger (\Lambda - \tfrac{1}{2}I_2)^\dagger UU^\dagger (\Lambda - \tfrac{1}{2}I_2) U\right]\\
& =
\mbox{Tr}\left[(\Lambda - \tfrac{1}{2}I_2)^\dagger (\Lambda - \tfrac{1}{2}I_2) \right]
= ||\Lambda - \tfrac{1}{2}I_2||^2.
\end{align*}
$$

We can define distance between densities with a positive constant $C$
multiplied by the Hilbert-Schmidt norm.
We choose $C = \sqrt{2}$ so that for pure states with $p = 1$, the
associated distance is $r = 2(p - 1/2) = 1$.
In general, since each such $r$ is associated with a unique
$\Lambda(p)$, we conclude that the space of $2\times 2$ density
matrices is a ball consisting of concentric, transitive orbits of the
unitary group, with the pure states at $p = 1$, the maximally mixed
state at $p = 0$, and the sphere associated with $\Lambda(p)$ at
radius $r = 2(p - 1/2)$.

#### Orbital mechanics

A similar story holds in higher dimensions. Density matrices are
positive and unit trace, so orbits have dimension $d$ has a canonical
representative of the form

$$
\Lambda = \mathrm{diag}(p_1, p_2, \ldots, p_d),
$$

where the positivity of $\rho$ and unit trace condition imply

$$
\sum_{i=1}^d p_i = 1, \quad p_i \geq 0.
$$

Since the unitary matrices include permutation matrices $U_\sigma
= [\delta_{i\sigma(i)}]$, we can arrange these eigenvalues in
decreasing order:

$$
p_1 \geq p_2 \geq \cdots \geq p_d \geq 0.
$$

<!-- https://en.wikipedia.org/wiki/Bloch_sphere -->
