---
Layout: post
mathjax: true
comments: true
title:  "Needles, noodles, and woodles"
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
If the needle is short, with $\ell < D$, it can cross at most one
line.
How likely is this?
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

The area $H$ below the line (green) can be calculated using calculus:

$$
H = \int_0^{\pi} \ell \sin \theta \, \text{d}\theta = \left[-\ell \cos\theta\right]^\pi_0
= \ell (\cos 0 - \cos \pi) = 2\ell.
$$

There is another very simple way to see this without using calculus.
Suppose you swing a slingshot around so that it executes a full revolution
every $2\pi$ seconds.
If the circle has radius $\ell$, the velocity (calculated by consider
a full revolution) is

$$
v = \frac{\text{distance}}{\text{time}} = \frac{2\pi \ell}{2\pi} = \ell.
$$

The velocity has two sinusoidally varying components: a horizontal
component, $v_x = \ell \sin \theta$ and a vertical component $v_y =
\ell \cos \theta$.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/buffon3.png"/>
	</div>
	</figure>

The horizontal velocity is exactly the curve of interest. The region
underneath the curve is the total *horizontal* distance covered in
half a revolution, since we are adding contributions of the form

$$
v_x \, \Delta \theta \approx \Delta x.
$$

But if we add up all the small changes $\Delta x$ in a
half-revolution, the total horizontal distance $A$ is obviously twice the
radius, or $H = 2\ell$. So no need for calculus!
Either we get there, the probability that the short needle hits the
line is

$$
P = \frac{2\ell}{\pi D}.
$$

#### Long needles and noodles

The above reasoning only works for short needles ($\ell < D$).
When $\ell > D$, the green curve will exceed the grey rectangle, and
the part outside does not contribute to the probability.
We can calculate its area and subtract, but its a bit tedious.
Let's see what we can do with the result we already have.
First, we can reformulate it a little.
Let $N$ be the number of times a short needle hits a line.
Our work above shows that the *expectation* is

$$
\langle N \rangle = 0 \cdot P(N = 0) + 1 \cdot P(N = 1) = P(N = 1) = \frac{2\ell}{\pi D}.
$$

Let's now consider a long needle, with $\ell > D$.
We can break it into some number of segments, say $n$, such that each is
shorter than $D$, with length $\ell_i$.
Let $N_i$, $i = 1, 2, \ldots, n$, label the number of times that
segment $i$ hits a line, and $N$ the *total* number of lines that the
long needle hits.
Then we have

$$
N = N_1 + N_2 + \cdots + N_n,
$$

and hence, by the linearity of averages and our results for short
needles,

$$
\begin{align*}
\langle N \rangle & = \langle N_1\rangle + \langle N_2 \rangle +
\cdots + \langle N_n \rangle \\
& = \frac{2\ell_1}{\pi D} + \frac{2\ell_2}{\pi D} + \cdots +
\frac{2\ell_n}{\pi D} \\
& = \frac{2(\ell_1 + \ell_2 + \cdots + \ell_n)}{\pi D} =
\frac{2\ell}{\pi D}.
\end{align*}
$$

So what do you know! The formula for the expected number of
crossings is the same, even though the probabilities will change
(the longer needle can hit multiple lines for instance).
But something even more remarkable is true.
This result was independent of the relative orientation of the
segment, so it holds for an any curve in the plane, such as a
twisty-turny noodle. The result

$$
\langle N \rangle = \frac{2\ell}{\pi D}
$$

for an arbitrary curve of length $\ell$ is called *Buffon's noodle*.

#### Random noodles

In general, for a fixed curve the probabilities will be related in a
complicated way.
But we can also consider a noodle which is randomly generated as a *random walk*.
Physically, this would give the expected number of crossings for a
polymer.

\langle N^2 \rangle = \langle\rangle

#### Wheels and woodles

There is a final twist of the noodle comes from thinking about shapes which
have constant width.
