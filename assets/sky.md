---
Layout: post
mathjax: true
comments: true
title:  "Why is the sky blue?"
categories: [Physics, Everyday]
date:  2020-12-26
---

**December 26, 2029.** *Why is the sky blue? The answer involves *

#### Rayleigh scattering

When light passes through the atmosphere

#### Rayleigh scattering

The Rayleigh scattering cross-section falls off with wavelength as
$\sigma = A/\lambda^4$.
The spectral radiance $R(\lambda, T)$ at temperature $T$, which is the
radiant intensity per unit wavelength, obeys Planck's law

$$
R(\lambda, T) = \frac{B}{\lambda^5} \frac{1}{e^{h c/kT\lambda} - 1},
$$

where $h$ is Planck's constant and $k$ is Boltzmann's constant.
Define $x = h c/kT\lambda$.
The colour of the sky will maximize the product of the blackbody
radiance spectrum coming from the sun and the Rayleigh scattering
cross-section:

$$
f_T(x) = \frac{C x^9}{e^{x} - 1}
$$

for some constant $C$.
To find the maximum $x^*$, we simply differentiate and set to $0$:

$$
f'_T(x) = C
\left[\frac{9x^8}{e^{x} - 1} - \frac{x^9 e^x}{(e^x - 1)^2}\right] = 0
\quad \Longrightarrow \quad (x^* - 9) e^{x^*} + 9= 0.
$$

This is a transcendental equation with no closed-form solution.
But we can use a sneaky approximation method, and for the heck of it,
solve the more general problem

$$
(x^* - n) e^{x^*} + n = 0.
$$

Our inspired guess is that there is a solution near $n$, so we rewrite
in terms of $y = x^* - n$:

$$
y e^y + e^{-n} n = 0.
$$

We then Taylor expand $e^y$. For something tractable, let's just
go to first order in $y$:

$$
0 = y e^y + e^{-n} n \approx y(1 + y) + e^{-n}n.
$$

The quadratic formula gives the self-consistently small solution

$$
y = \frac{1}{2}\left(\sqrt{1 - 4n e^{-n}} - 1\right) \approx - n e^{-n},
$$

where we used the binomial approximation.
So the maximum wavelength is roughly

$$
x^* = y + n \approx n(1 - e^{-n}) \quad \Longrightarrow \quad \lambda^* \approx \frac{h
c}{kT n(1 - e^{-n})} \approx \frac{hc}{kT n}.
$$

#### References

https://application.wiley-vch.de/books/sample/3527403205_c01.pdf
http://homepages.wmich.edu/~korista/colors_of_the_sky-Bohren_Fraser.pdf
https://www.oceanopticsbook.info/view/photometry-and-visibility/luminosity-functions

<!-- maximum e^(-(x-550*5/480)^2/(2*(50*5/480)^2))x^9/(e^x - 1)-->
