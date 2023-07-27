---
Layout: post
mathjax: true
comments: true
title:  "A kernel trick for integrals"
categories: [Math, Hacks]
date:  2022-11-10
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script> <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

**November 10, 2022.** *I present a simple trick for doing integrals by swapping
  the argument of a kernel.*

## Overview
---

Consider an integral transform with kernel $K(x, y)$.
In general, this gives two distinct transforms,

$$
T_1f(y) = \int_{\Omega_1} f(x) K(x, y) \, \text{d}x, \quad T_2f(x) = \int_{\Omega_2} f(y) K(x, y) \, \text{d}y,
$$

where $T_i$ integrates over argument $i$, and $\Omega_i$ denotes the
corresponding domain of integration.
If everything is smooth enough to swap integrals (i.e. Fubini's theorem), then

$$
\begin{align*}
\int_{\Omega_1} f(x)\cdot  T_2g(x) \,\text{d}x & = \int_{\Omega_1}
f(x)\left[\int_{\Omega_2} g(y) K(x, y) \, \text{d}y\right] \text{d}x \\
& = \int_{\Omega_2}
g(y)\left[\int_\Omega f(x) K(x, y) \, \text{d}x\right] \text{d}y \\
& = \int_{\Omega_2} T_1f(y) \cdot g(y)\, \text{d}y.
\end{align*}
$$

For a symmetric kernel $K(x, y) = K(y, x)$ and $\Omega_1 = \Omega_2
= \Omega$, we have $T_1 = T_2 = T$, and our result simplifies to:

<div style="background-color: #cfc ; padding: 10px; border: 1px
solid green; line-height:1.5">
<b>The symmetric kernel trick.</b> <br>

For an integral transform $T$ defined by a symmetric kernel,

$$
\int_{\Omega} f(x) \cdot Tg(x)\, \text{d}x = \int_{\Omega} Tf(y) \cdot g(y)\,
\text{d}y.
$$
</div>

From a pure math standpoint, we've basically just observed that the integral transforms
$T_1$ and $T_2$ are dual,

$$
\langle f, T_2 g\rangle = \langle T_1 f, g\rangle,
$$

with respect to a suitably defined inner product $\langle \cdot, \cdot\rangle$.
But this turns out to be a useful trick for doing real-life integrals!

*Full disclosure.* I didn't come up with this hack, but stole it
(with some customizations) from Ramanujan.
Also, I'm ignoring many mathematical subtleties! The joys of
being a physicist.

## The Voigt integral
---

Let's take everyone's favourite example, the 1D Fourier transform:

$$
T_\text{F} f(\omega) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty
f(x)e^{-i\omega x} \, \text{d}x.
$$

We can consult a table and pick out, for instance, the pairs

$$
\begin{align*}
f(x) & = e^{-\alpha x^2}, \quad T_\text{F}f(\omega) =
\frac{1}{\sqrt{2\alpha}} e^{-\omega^2/4\alpha} \\
g(x) & = e^{-\beta |x|}, \quad T_\text{F}g(\omega) =
\sqrt{\frac{2}{\pi}} \cdot \frac{\beta}{\beta^2 + \omega^2}.
\end{align*}
$$

Then our kernel trick gives

$$
\begin{align*}
\int_{-\infty}^\infty \sqrt{\frac{2}{\pi}}\frac{\beta e^{-\alpha^2 x^2}}{\beta^2 + x^2} \,
\text{d}x
& =\frac{1}{\sqrt{2\alpha}} \int_{-\infty}^\infty e^{-x^2/4\alpha^2 + \beta|x|} \, \text{d}x.
\end{align*}
$$

The RHS is straightforward to express in terms of the complementary error
function:

$$
\text{erfc}(z) = \frac{2}{\sqrt{\pi}}\int_z^\infty e^{-x^2}\, \text{d}x.
$$

We complete the square, defining $2\alpha u = x +
2\alpha^2\beta$ to find

$$
\begin{align*}
\int_{-\infty}^\infty e^{-x^2/4\alpha^2 - \beta|x|} \, \text{d}x
& = 2\int_{0}^\infty e^{-x^2/4\alpha^2 - \beta x} \, \text{d}x\\
& = 4\sqrt{\alpha} e^{(\alpha\beta)^2}\int_{2\alpha^2\beta}^\infty
e^{-u^2} \, \text{d}u\\
& = 2\sqrt{\pi\alpha} e^{(\alpha\beta)^2}\text{erfc}(\alpha\beta).
\end{align*}
$$

We can finally conclude that 

$$
\int_{-\infty}^\infty \frac{ e^{-\alpha^2
x^2}}{\beta^2 + x^2} \, \text{d}x = \frac{\sqrt{2}\pi \alpha}{\beta}
e^{(\alpha\beta)^2}\text{erfc}(\alpha\beta).
$$

I call this the
"Voigt integral"after
the
[related convolution in spectroscopy](https://en.wikipedia.org/wiki/Voigt_profile).

<div style="background-color: #EAD1DC ; padding: 10px; border: 1px solid
purple; line-height:1.5">
<b>Exercise 1.</b> The <i>Hankel transform</i>

$$
\mathcal{H}^{(\nu)}f(k) = \int_0^\infty f(r) rJ_\nu(kr) \, \text{d}r
$$

is defined by an asymmetric
kernel $K(r, k) = rJ_\nu(kr)$, where $J_\nu$ is a <i>Bessel function of
the first kind</i> of order $\nu$.
<br>

<span style="padding-left: 20px; display:block">
(a) Using the kernel trick, show that

$$
\int_0^\infty k \mathcal{H}^{(\nu)}\left[\frac{f(r)}{r}\right](k) g(k)
\, \text{d}k = \int_0^\infty f(k)\mathcal{H}^{(\nu)}g (k)\,
\text{d}k. \tag{1} \label{hankel}
$$

(b) Apply $(\ref{hankel})$ to a judicious choice of Hankel transform
pairs to derive the expression

$$
\int_0^\infty e^{-\alpha^2 u/2} K_0(\beta\sqrt{u})\, \text{d}u =
-\frac{1}{\alpha^2} e^{-\beta^2/2\alpha^2}\text{Ei}\left(-\frac{\beta^2}{2\alpha^2}\right),
$$

where $K_0$ is a <i>modified Bessel function of the second kind</i> and
$\text{Ei}$ is the <i>exponential integral</i>, a special function defined by

$$
\text{Ei}(z) = -\int_{-z} \frac{e^{-t}}{t} \, \text{d}t.
$$
</span>
</div>

## Mordell integrals
---

Here's a fancier example, again using the Fourier transform.
Consider the *Mordell integral*

$$
h(z; \tau) = \int_{-\infty}^\infty \frac{e^{\pi i \tau x^2 - 2\pi
zx}}{\cosh(\pi x)} \, \text{d}x,
$$

with $\Im(\tau) > 0$ to ensure convergence.
Note that this is a product of functions which are *self-dual* under
the Fourier transform, up to a change in their parameters:

$$
\begin{align*}
f(x) & = e^{i\alpha x^2 - \beta x}, \quad T_\text{F}f(\omega) =
\frac{1}{\sqrt{-2i\alpha}} e^{i(\beta-i\omega)^2/4\alpha} \\
g(x) & = \frac{1}{\cosh(\gamma x)}, \quad T_\text{F}g(\omega) =
\sqrt{\frac{\pi}{2}} \frac{1}{\gamma\cosh(\pi\omega/2\gamma)}.
\end{align*}
$$

The kernel trick (and the change of variable $x = 2\pi u$) now gives

$$
\begin{align*}
h(z; \tau) & = \frac{\sqrt{\pi}}{\sqrt{-i\alpha}}\int_{-\infty}^\infty
\frac{e^{i(2\pi z-ix)^2/4\pi\tau}}{\cosh(x/2)} \, \text{d}x \\
& = \frac{\sqrt{\pi}e^{i\pi z^2/\tau}}{\sqrt{-i\alpha}}\int_{-\infty}^\infty
\frac{e^{-ix^2/4\pi\tau+zx/\tau}}{\cosh(x/2)} \, \text{d}x \\
& = \frac{2\pi^{3/2}e^{i\pi z^2/\tau}}{\sqrt{-i\alpha}}\int_{-\infty}^\infty
\frac{e^{-i\pi u^2/\tau+2\pi zu/\tau}}{\cosh(\pi u)} \, \text{d}u \\
& = \frac{2\pi^{3/2}e^{i\pi z^2/\tau}}{\sqrt{-i\alpha}}
h\left(-\frac{z}{\tau};
-\frac{1}{\tau}\right). \tag{2}\label{h}
\end{align*}
$$

This seems like a neat result!

<div style="background-color: #EAD1DC ; padding: 10px; border: 1px solid purple; line-height:1.5">
<b>Exercise 2.</b> Ramanujan defined the related integral

$$
F_\omega(z) = \int_{-\infty}^\infty \frac{e^{-\pi\omega x^2 + 2\pi
x}\sin(\pi x z)}{e^{2\pi x}-1} \, \text{d} x.
$$

We'll end with a few exercises on this theme. <br>

<span style="padding-left: 20px; display:block">
(a) Define $\varphi$ by

$$
h(z; \tau) = -\frac{2i}{\tau}e^{-(\pi i\tau/4 + \pi i
z)}\varphi\left(z + \frac{\tau-1}{2}, \tau\right).
$$

Prove that $F_\omega(z)$ and $h(z; \tau)$ are
related by

$$
F_{-i\tau}(2iz) =
\frac{1}{2i\tau}\left[\varphi(z, t) - \varphi(-z, \tau)\right]. \tag{3} \label{varphi}
$$

(b) Using equation $(\ref{h})$ and $(\ref{varphi})$ or otherwise, show that

$$
F_\omega(z) = -\frac{i}{\sqrt{\omega}} e^{-\pi z^2/4\omega} F_{1/\omega}\left(\frac{iz}{\omega}\right).
$$

(c) Set $\omega = \alpha^2$ and $z \to \alpha
z/\sqrt{\pi}$.
Deduce from part (b) that, for $\alpha\beta = 1$ and $\alpha, \beta > 0$,

$$
\sqrt{\alpha}e^{z^2/8}\int_{-\infty}^\infty
\frac{e^{-\pi^2\alpha^2x^2}\sin(\sqrt{\pi}\alpha x z)}{e^{2\pi x}-1} \text{d}x = \sqrt{\beta}e^{-z^2/8}\int_{-\infty}^\infty
\frac{e^{-\pi^2\beta^2x^2}\sinh(\sqrt{\pi}\beta x z)}{e^{2\pi x}-1} \text{d}x.
$$
</span>
</div>

<!-- https://webpages.charlotte.edu/aroy15/image/drz5-err.pdf -->
