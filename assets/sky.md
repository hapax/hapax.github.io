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

#### Wien's law

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
If air reflected all solar light equally, it would appear the same
colour as the sun.
It's a bit hard to tell what colour the sun actually is, since it's so
blindingly bright.
The simplest measure is to see what wavelength it emits most, $\lambda_{\text{max}}$.
We can guess this wavelength based on dimensional analysis.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/sky1.png"/>
	</div>
	</figure>

The surface temperature of the sun is around $\mathcal{T} = 5800 \text{ K}$, and
the hot atoms at its surface emit light.
The relevant physical constants are Boltzmann constant $k$ (since
temperature is involve), Planck's constant $h$ (since atoms are
involved), and the speed of light $c$ (since light is involved).
We want a wavelength $\lambda$, so we guess a relation of the form

$$
\lambda_{\text{max}} = h^a c^b k^d \mathcal{T}^e
$$

for some powers $a, b, d, e$.
Let $E = ML^2/T^2$ be dimensons of energy and $\Theta$ the dimension
of temperature.
Then our constants have dimensions $[h] = ET$, $[c] = L/T$, $[k] =
E/\Theta$, and hence

$$
L = [\lambda_{\text{max}}] = [h^a c^b k^d \mathcal{T}^e] = E^{a+c} T^{a-b}L^b \Theta^{d-c}.
$$

Since $M$ only appears in $E$ (on the RHS), we obtain the equations

$$
a+c = 0,\quad a- b = 0, \quad b = 1, \quad d - c = 0 \quad
\Longrightarrow \quad a = b = -c = -d = 1,
$$

and hence

$$
\lambda_{\text{max}} \sim \frac{hc}{kT}.
$$

Up to constants, this is called *Wien's law*.
The important point is that it is inversely proportional to
temperature!
If we would like to include constants, then as shown in the appendix,
we have

$$
\lambda_{\text{max}} \approx \frac{hc}{5kT}.
$$

If we substitute in constants and the surface temperature of the sun,
we get in SI units

$$
\lambda_{\text{max}} \approx \frac{(6.6 \times 10^{-34})(3 \times
10^8)}{5(1.4 \times 10^{-23})5800} \text{ m} \approx 480 \text{ nm}.
$$

This is right on the cusp between blue and green. You may not have
known that the sun is bluey-green, since when you look at it without
burning a hole in your retina, it looks yellow.
This turns out to be because the blue light is scattered by the
atmosphere, leaving a dominant yellow colour!
But the sky is blue, and not bluey-green, so something in our
explanation is missing.

#### Rayleigh scattering

The wavelength of visible light is a few hundred nanometres, a
thousand times larger than an air molecule.
Thus, to a light wave, a molecule is a tiny, structureless, point.
It does not interact with different parts of the molecule differently.
But its chances of colliding with the molecule are still proportional
to the molecule's volume.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/sky2.png"/>
	</div>
	</figure>

More precisely, suppose we fire $N_\text{in}$ photons at the air
molecule, and $N_\text{out}$ bounce off.
The probability $p = N_\text{out}/N_\text{in}$ that any given photon
hits the molecule is proportional to its volume $V$:

$$
p = \frac{N_\text{out}}{N_\text{in}} \propto V.
$$

Since the scattered photons are effectively emitted from the small
point where the air molecule is, they spread spherically outwards, and
at a distance $r$, the number of photons per unit area is

$$
n_\text{out} = \frac{N_\text{out}}{4\pi r^2} \propto \frac{p}{r^2}
\propto \frac{V}{r^2}.
$$



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
