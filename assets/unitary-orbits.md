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
where $I_n$ will denote the $n \times n$ identity matrix.

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

#### Orbital mechanics

Let's think about the Bloch ball in a little more detail.
Since any density matrix $\rho$ is unitarily diagonalizable,
i.e. $U^\dagger \rho U = \rho_{\text{diag}}$, each
orbit for a Hilbert space of dimension $d$ has a canonical
representative of the form

$$
\rho = \mathrm{diag}(p_1, p_2, \ldots, p_d),
$$

where the positivity of $\rho$ and unit trace condition imply

$$
\sum_{i=1}^d p_i = 1, \quad p_i \geq 0,
$$

and since the unitary matrices include permutation matrices $U_\sigma
= [\delta_{i\sigma(i)}]$, we can arrange these eigenvalues in
decreasing order:

$$
p_1 \geq p_2 \geq \cdots \geq p_d \geq 0.
$$

In the qubit case $d = 2$, we can write these canonical
representatives as

$$
\rho(x) =
\begin{bmatrix}
x & \\
& 1-x 
\end{bmatrix}, \quad x \geq 1/2.
$$
