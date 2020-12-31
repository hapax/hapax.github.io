---
Layout: post
mathjax: true
comments: true
title:  "Why is the sky blue?"
categories: [Physics, Everyday]
date:  2020-12-30
---

**December 30, 2020.** *Why is the sky blue? The answer involves a
  surprising combination of elements, including but not limited to
  particle physics, dimensional analysis, thermodynamics, and biology.*

#### Rayleigh scattering

Raising your eyes on a sunny day, you will be confronted by one of
those elemental mysteries of everyday life: the blueness of the sky.
Why is it blue?
Although this may be baby's first physics question, the answer is a
bit subtler than most physics textbooks make out.
The first qualitatively correct explanation is due to Leonardo Da
Vinci, who realised that blue is not the colour of the air
itself, but rather, light reflected by air. He wrote that

<span style="padding-left: 20px; display:block">
....the blueness we see in the atmosphere is not intrinsic color, but is caused
by warm vapor evaporated in minute and
insensible atoms on which the solar rays
fall, rendering them luminous against the
infinite darkness of the fiery sphere which
lies beyond and includes it...
</span>

In other words, space is black, and without intrinsic colour.
Air reflects the light of the sun, and appears blue.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/sky1.png"/>
	</div>
	</figure>

But if the air reflected all solar light equally, it would appear the same
colour as the sun.
It's a bit hard to tell what colour the sun actually is, since it's so
blindingly bright.
This turns out to be a subtle question, but a simple measure is to
look at the whole spread of light emitted and pick out the frequency
which emits 

#### Appendix: a transcendental approximation

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
