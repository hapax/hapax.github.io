---
Layout: post
mathjax: true
comments: true
title:  "Needles, noodles, wheels and woodles"
categories: [Maths, Hacks]
date:  2020-12-23
---

**December 23, 2020.** *Buffon asked how likely it is that a randomly
  thrown needle will cross a line on ruled paper. Barbier's elementary
  solution is well-known, but less well-known is the elementary
  extension to noodles, and a simple consequence for funny shaped
  wheels or "woodles".*

#### Buffon's needle

Suppose we throw a needle of length $\ell$ onto an infinitely large
page, with lines ruled horizontally with separation $D$.
If the needle has length $\ell < D$, it can intersect at most one
line.
How likely is it to intersect a line?
Following
[Joseph-Émile Barbier](https://en.wikipedia.org/wiki/Joseph-%C3%89mile_Barbier),
we can split the randomness into two parts: the vertical position $y$ of the
needle's lower end, and it's angle to the horizontal, $\theta$.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/buffon1.png"/>
	</div>
	</figure>

We therefore take $y \in [0, D)$, and $\theta \in [0, \pi)$.
To see what the probability of hitting a line is, we note that the lower end of the needle will reach the upper line provided

$$
y \leq \ell \sin \theta.
$$

It's easy to see that, assuming the parameters $(\theta, y)$ for the random throw take a uniform distribution in the rectangle below, the probability is just the area of the region
below the line $y \leq \ell \sin \theta$, divided by the total area of the rectangle, $\pi D$.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/buffon2.png"/>
	</div>
	</figure>

The area $A$ below the line (green) can be calculated using calculus:

$$
\int_0^{\pi} \ell \sin \theta \, \text{d}\theta = \left[-\ell \cos\theta\right]^\pi_0
= \ell (\cos 0 - \cos \pi) = 2\ell.
$$

There is another way to see this without using calculus.
Thus, the probability of intersecting a line is

$$
P = \frac{2\ll}{\pi D}.
$$
