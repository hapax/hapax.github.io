---
Layout: post
mathjax: true
comments: true
title:  "Zeta regularisation voodoo"
categories: [Mathematics, Physics]
date:  2019-08-13
---

**August 13, 2019.** *A technical post on path integrals, zeta function
  regularisation of determinants, and an application to hot oscillators.*

## Motivation

*Prerequisites: quantum field theory, path integrals.*

In physics, mathematics, and life in general, we often need to
evaluate Gaussian integrals.
The simplest integral is one-dimensional:

$$
\int_{-\infty}^\infty \frac{dx}{\sqrt{2\pi}} \, e^{-\tfrac{1}{2}\alpha x^2}  = \frac{1}{\sqrt{\alpha}}
$$

We have written an extra factor of $1/\sqrt{2\pi}$ in the measure $dx$
for reasons that will become clear in a moment.
In $n$ dimensions, we can replace $\alpha x^2$ with any bilinear $x_i
A_{ij} x_j$, where $A_{ij}$ is a diagonalisable matrix.
By going to the eigenbasis of $A$, the one-dimensional result immediately
generalises to

$$
\int_{-\infty}^\infty \frac{dx}{(2\pi)^{n/2}} \,e^{-x_i A_{ij} x_j} =
\frac{1}{\sqrt{\det A}} = \prod_i \lambda_i^{-1/2},
$$

where the $\lambda_i$ are eigenvalues of $A$.
In quantum field theory, we take
things even further, and evaluate the integral for an
*infinite-dimensional* vector space.
In this case, we replace the discretely indexed vector $x_i$ with a
continously indexed function $x(\tau)$, for say $\tau \in [0, L]$, and the integral over all
vectors $x_i$ becomes an integral over all *paths* $x(\tau)$.
This is called a *path integral*.

Let's define the integral measure for the path as the limit of the discretisations of the
path $x(\tau)$ into chunks evaluated at $\tau_n := nL/N$, or

$$
\mathcal{D}x(\tau) := \lim_{N\to\infty}(2\pi)^{-N/2}\prod_{n=1}^N
dx(\tau_n).
$$

We might cross our fingers and hope that the infinite-dimensional
Gaussian path integral, for a bilinear operator $A(\tau, \tau')$, has exactly the
same expression as above:

$$
\int \mathcal{D}x \,
\exp\left[-\int_0^L d\tau\, d\tau'\, x(\tau)A(\tau,\tau') x(\tau')\right] =
\frac{1}{\sqrt{\det A}} = \prod_i \lambda_i^{-1/2}.
$$

We now see why we shifted the $\sqrt{2\pi}$ onto the left: in the
infinite-dimensional limit, it is a nuisance factor which blows up
unless absorbed into the path integral.
But we can still get infinities!
In general, the infinite product of eigenvalue $\lambda_i$ will not converge.

But quantum physicists are not cowed by infinities.
The usual trick is to *regulate* the divergence in some way,
essentially, finding some way to smoothly ignore the behaviour of very
large eigenvalues which are typically non-physical (i.e. they
occur where we expect the model, or the experiment, to break down).
Here, we will consider a class of infinite products,

$$
\det \mathcal{X}^a_{\xi} = \prod_{k=a}  \xi (k+a),
$$

and show how to regulate them using a generalisation of the Riemann
zeta function.
We finish with some simple applications to quantum statistical mechanics.

## The maths

Define the *Hurwitz function* by

$$
\zeta(s, a) = \sum_{k \geq 0}\frac{1}{(k+a)^s}, \quad a > 0, \quad |\Re(s)| > 1.
$$
	
This is a generalisation of the
[Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function)
$\zeta_\text{R}$,
since $\zeta_\text{R}(s) = \zeta(s, 1)$.
Although the definition of the Hurwitz function above blows up at $s = 0$, we can analytically
continue so that it is defined at $s = 0$. From the [DLMF](https://dlmf.nist.gov/25.11) (or otherwise), it obeys

$$
\begin{align}
\zeta(0, a)= \frac{1}{2} - a, \quad \zeta'(0, a) = \ln
\left(\frac{\Gamma(a)}{\sqrt{2\pi}}\right),\label{zeta0}\tag{1}
\end{align}
$$

where $\Gamma$ is the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function).
Consider an operator $\mathcal{X}^a_\xi$
with spectrum $\lambda_k = \xi(k+a)$, $k \in \mathbb{Z}_{\geq 0}$.
We can define the associated *spectral zeta function*

$$
  \begin{align}
    \zeta_\mathcal{X}(s) & = \sum_{k \geq 0} \lambda_k^{-s}\label{zeta1}\tag{2}\\
   & = \sum_{k \geq 0}\frac{1}{\xi^s(k+s)^s} =
      \xi^{-s}\zeta(s, a). \label{zeta2}\tag{3}
  \end{align}
$$
  
We can differentiate (\ref{zeta1}), (\ref{zeta2}) with respect to $s$, and equate them
to get

$$
  \begin{align}
    \zeta'_\mathcal{X}(s) & = -\sum_{k \geq 0}
                            \lambda_k^{-s}\log\lambda_k \label{zeta3}\tag{4}\\ 
   & = \xi^{-s}\zeta'(s,a) - \xi^{-s}\log \xi \cdot \zeta(s,
     a). \label{zeta4}\tag{5}
  \end{align}
$$
  
  From (\ref{zeta3}) and the elementary identity

$$
\det A = \prod_i a_i = e^{\sum_i \log a_i} =  e^{\mathrm{Tr} \log A},
$$

where $a_i$ are the eigenvalues of $A$, we also have

$$
\begin{equation}
    \zeta'_\mathcal{X}(0) = -\sum_{k \geq 0} \log \lambda_k = -\log
    \det \mathcal{X}. \label{zeta5} \tag{6}
\end{equation}
$$
	
Setting $s = 0$ in (\ref{zeta4}), using (\ref{zeta0}), and equating with (\ref{zeta5}), we find

$$
\begin{align}
    \det \mathcal{X}^a_{\xi} & = \prod_{k=a}  \xi (k+a) \notag \\& = \exp \left[\zeta'(0, a) -
                                     \log \xi
                                \cdot \zeta(0,a)\right] \notag \\
  & = \exp \left[-\ln \left(\frac{\Gamma(a)}{\sqrt{2\pi}}\right) +\log
    \xi\left(\frac{1}{2} - a\right) \right] \notag \\
  & = \frac{\sqrt{2\pi}}{\Gamma(a) }\xi^{1/2-a}. \label{final}\tag{7}
  \end{align}
$$

This is our nice, simple final result!

## Hot harmonic oscillators

A simple example is a single boson in a thermal state.
The physics is governed by the *partition function* for the system,

$$
Z[\beta] = \mathrm{Tr}[e^{\beta \hat{H}}].
$$

One can show that this is equivalent to a weighted sum over paths
which are [periodic in imaginary time]({{
hapax.github.io }}/physics/imaginary-time/),

$$
Z[\beta] = \int_{x(0)=x(\beta)}
\mathcal{D}x(\tau) \, e^{-S_E[x(\tau)]}
$$

where $S_E$ is the action in Euclidean signature.
To specialise, we can consider the simplest case of a bosonic harmonic
oscillator, with

$$
S_E[x(\tau)] = \int_0^\beta d\tau\,
\frac{1}{2}\left(\dot{x}(\tau)^2+\omega^2 x^2\right) = \int_0^\beta d\tau\,
\frac{1}{2}x(\tau)\mathcal{J} x(\tau),
$$

where $\mathcal{J} =-\partial_\tau^2 + \omega^2$ after integrating by parts.
The partition function is a Gaussian:

$$
Z[\beta] =
\exp\left[-\int_0^L d\lambda\, d\mu\, x(\lambda)\mathcal{J} x(\mu)\right]
= \frac{1}{\sqrt{\det \mathcal{J}}}.
$$

Let's calculate the regulated determinant of the operator $\mathcal{J}$.
To find the eigenvalues, we first determine the eigenfunctions $f$,
recalling they are subject to the periodicity constraint $f(0) = f(\beta)$:

$$
\begin{align}
\mathcal{J} f(\tau) & = -\ddot{f} + \omega^2 f = \lambda f, \quad f(0) =
f(\beta) \notag \\
\Longrightarrow \quad f_k(\tau) &= e^{2\pi k \tau/\beta}, \quad
\lambda_k = \left(\frac{2\pi k}{\beta}\right)^2+\omega^2 \notag
\end{align}
$$

for any integer $k$.
But then

$$
\begin{align}
\det \mathcal{J} &= \prod_{k\in\mathbb{Z}} \lambda_k =
	\omega^2\prod_{k\geq 1}\left(\frac{2\pi k}{\beta}\right)^4 \cdot \prod_{k\geq 1}\left[1 + \left(\frac{\beta\omega}{2\pi k}\right)^2\right]^2,\notag
\end{align}
$$

where we pick up the $\omega^2$ from the $k = 0$ term.
The second product can be evaluated using the result from residue calculus,

$$
\prod_{k\geq 1}\left[1 + \left(\frac{z}{n\pi}\right)^2\right] =
\frac{\sinh z}{z}.
$$

The first product diverges, but can be evaluated by voodoo for
$\xi = 2\pi/\beta$ and $a = 1$:

$$
\prod_{k\geq 1}\left(\frac{2\pi k}{\beta}\right) = \det
\mathcal{X}^1_{2\pi/\beta} = \sqrt{2\pi}\cdot \sqrt{\beta/2\pi} = \sqrt{\beta}.
$$

Combining these results, we find

$$
Z[\beta] = \frac{1}{\sqrt{\det \mathcal{J}}} =
    \frac{1}{\beta\omega}\prod_{k\geq 1} \left[1 +
      \left(\frac{\beta\omega}{2\pi k}\right)^2\right]^{-1} =
    \frac{1}{2\sinh (\beta\omega/2)}.
$$

Of course, it is much simpler to go the traditional route!
We have

$$
Z[\beta] = \sum_{n\geq 0} e^{-\beta E_n} =
    e^{-\beta\omega/2}\sum_{n\geq 0} e^{-\beta \omega n} =
\frac{e^{-\beta\omega/2}}{1-e^{-\beta \omega}} =
    \frac{1}{2\sinh(\beta\omega/2)}.
$$

While this is not exactly an advertisment for path integrals, it is a
small advertisment for voodoo.
Usually, one has to insert factors by hand to get the Hamiltonian and
path integral method to agree.
Now the two approaches agree automatically!

---

**Exercise 1.** *Hot fermionic oscillator.*

A Fermionic oscillator has the "square root" Lagrangian

$$
L_E = -\bar{\psi}\mathcal{Q}\psi, \quad \mathcal{Q} = \partial_\tau + \omega,
$$

where $\bar{\psi}$ and $\psi$ are *Grassman* (anticommuting)
classical coordinates for the fermion.

1. Starting with the one-dimensional Gaussian integral for Grassman
   numbers $\bar{\theta}, \theta$,

   $$
   \int d\bar{\theta} \, d\theta \, e^{-\alpha \bar{\theta}\theta} =
   \alpha,
   $$

   argue that

   $$
   Z[\beta] = \int \mathcal{D}\bar{\psi}(\tau)\, \mathcal{D}\psi(\tau)\, e^{-S_E[\bar{\psi},\psi]} = \det\mathcal{Q}.
   $$
  
2. What are the boundary conditions for the fields $\bar{\psi}, \psi$?
   *Hint*. Consider two identical fermions on the thermal circle. What
   happens if they are exchanged?
3. Find the eigenvalues of $\mathcal{Q}$, subject to the boundary
   conditions you found in the previous question, and write a product expression for
   $Z[\beta]$.
4. Simplify using voodoo and the product formula

   $$
    \cosh \left(\frac{x}{2}\right) = \prod_{k \geq 0}
    \left[1+ \frac{x^2}{\pi^2(2n+1)^2}\right].
   $$
	
5. Check your result agrees with the fermionic oscillator Hamiltonian,
  which has energy eigenvalues $E_\pm = \pm \omega/2$.
  You should find in both cases that

  $$
  Z[\beta]=2\cosh \left[\frac{\beta\omega}{2}\right].
  $$

---

**Exercise 2.** (For the author) *Anyone for anyons?*

Anyons are particles with *fractional* spin $a$.
This means that after going around the thermal loop, they pick up a
phase $e^{2\pi i a}$.

1. Determine the natural boundary conditions for spin $a$, and
   reproduce the result of
   [Boschi-Filho and Farina (1994)](https://arxiv.org/pdf/hep-th/9410098.pdf)
   for the determinant of $\mathcal{J}$ with these boundary
   conditions,

   $$
	\det\mathcal{J} = 4
	\left[\cosh^2 \left(\frac{\beta\omega}{2}\right) - \sin^2(\pi a)\right]
   $$

   using voodoo rather than Green's functions.

2. (Open) Determine whether the anyonic path integral can be written

   $$
   Z_a[\beta] = [\det \mathcal{J}]^{p(a)}
   $$

   for some power $p(a)$. For bonus points, what is $p(a)$?

---

## References

- *Geometry, Topology and Physics* (2003), Mikio Nakahara.
- *An Introduction to Quantum Field Theory* (1995), Michael Peskin and
Daniel Schroeder.
- *Quantum Field Theory and the Standard Model* (2013), Matthew Schwartz.
