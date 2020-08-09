---
Layout: post
mathjax: true
comments: true
title:  "The Bloch sphere and Hopf fibrations"
categories: [Physics, Mathematics]
date:  2020-08-09
---

**August 9, 2020.** *The Bloch sphere encodes the geometry
  of single qubit states. Remarkably, it is equivalent
  to the Hopf fibration. I give a quick proof of this
  result, and discuss the generalization to pure states of two and
  three qubits, which (with a little more work) are equivalent to
  fibrations of the seven- and fifteen-sphere.* 

#### The Bloch sphere

A classical bit is $0$ or $1$, or heads and tails on a coin.
A quantum bit, or *qubit*, is a *complex linear combination* of $0$ and $1$,
considered as vectors:

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle, \quad \alpha, \beta
\in \mathbb{C}^2,
$$

where we're using physicist notation for vectors, $|v\rangle$.
It's basically a quantum coin, with some probability of giving $0$
when we look at it, and a complementary probability of giving $1$.
We would like to interpret $|\alpha|^2$ and $|\beta|^2$ as the
respective probabilities of measuring $0$ and $1$ when we look at the
qubit.
For this to make sense, they must satisfy the normalization condition
$|\alpha|^2 + |\beta|^2 = 1$.
But, writing this out in terms of the real and imaginary components
$\alpha = a + ib, \beta = c + id$, we have

$$
a^2 + b^2 + c^2 + d^2 = 1.
$$

This defines a *sphere* in four-dimensional space $\mathbb{R}^4$.
The sphere itself has three dimensions, since it can be locally
parameterized by $a$, $b$ and $c$.
For this reason, we call it the three-sphere $\mathbb{S}^3$.

There is one more ambiguity to worry about.
Suppose that we rotate our qubit $|\psi\rangle$ by a phase,
$e^{i\gamma}$.
Just making observations of the qubit alone, this phase is
unobservable, since the probabilities don't change,
i.e. $|e^{i\gamma}\alpha|^2 = |\alpha|^2$.
We call this the *global* phase ambiguity, and identify

$$
|\psi\rangle \sim e^{i\gamma}|\psi\rangle.
$$

This ambiguity identifies a *circle* of equivalent
states on the three-sphere.
It seems likely the results of collapsing these circles will be a
horrible mess.
But a little miracle occurs, and you get a regular sphere!
We'll show this in an elementary way here, and do something more slick
in the next section.
The basic idea is to note that we can first fix the amplitudes
$|\alpha|, |\beta|$, defining

$$
|\alpha| = \cos\left(\frac{\theta}{2}\right), \quad |\beta| = \sin\left(\frac{\theta}{2}\right)
$$

for $\theta \in [0, \pi]$, with the range chosen to ensure the
functions are positive.
We can then choose the phase ambiguity so that $\alpha = |\alpha|$,
leaving an arbitrary phase $\beta = e^{i\phi}|\beta|$.
Thus, we have the following parameterisation of a qubit:

$$
|\psi(\theta,\phi)\rangle = \cos\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle,
$$

for $\theta \in [0,\pi]$ and $\phi \in [0,2\pi)$.
These angles look a heck of a lot like spherical coordinates, so we draw them on a sphere, and call it the *Bloch sphere*.

<figure>
    <div style="text-align:center"><img src ="/images/posts/bloch2.png" width="45%"/>
    <figcaption><i>The Bloch sphere.</i></figcaption>
	</div>
</figure> 

A few states of interest are the north pole
$|\psi(0,\phi)\rangle = |0\rangle$, the south pole $|\psi(\pi,\phi)\rangle = |1\rangle$, and the point on the equator of zero longitude,

$$
\bigg|\psi\left(\frac{\pi}{2}, 0\right)\bigg\rangle = \cos\left(\frac{\pi}{4}\right)|0\rangle + \sin\left(\frac{\pi}{4}\right)|1\rangle = \frac{|0\rangle+|1\rangle}{\sqrt{2}} = |+\rangle.
$$

Now, is this really a sphere?
Clearly, for fixed $\theta \in (0, 2\pi)$, we get circles due to the period of the complex exponential $e^{i\phi}$.
So, at worst, we have a *cylinder* $[0, \pi] \times \mathbb{S}^1$.
But north cap of the cylinder degenerates into a single point, since
$\sin 0 = 0$, leaving only $|0\rangle$, with no dependence on $\phi$.

At the south end, something subtler happens.
Naively, we have a whole circle of points $e^{i\phi}|\1\rangle$, but
$e^{i\phi}|\1\rangle  \sim |1\rangle$ by residual phase ambiguity.
Thus, we have a *topological* sphere (a cylinder with ends collapsed
to points), which we can put spherical coordinates on, but
*geometrically* we have the hemisphere

$$
\alpha^2 + |\beta|^2 = a^2 + c^2 + d^2 = 1,
$$

for $\alpha \geq 0$.

#### The Hopf fibration of $\mathbb{S}^3$

Let's define the Hopf fibration in its full glory and see if we can
understand this mismatch better.
For $(\alpha,\beta)  \in \mathbb{S}^3$, i.e. satisfying our
normalisation condition $|\alpha|^2 + |\beta|^2 = 1$, define the
circle map

$$
C(\alpha, \beta) = \overline{\alpha\beta^{-1}} \in \hat{\mathbb{C}},
$$

where $\hat{\mathbb{C}}$ is the Riemann sphere, i.e. the complex plane
with a compactifying "hat" at infinity.
The circle map tells us the image of a whole circle of equivalent states

$$
(\alpha,\beta) \sim e^{i\gamma}(\alpha,\beta)
$$

on the Riemann sphere, since $C(e^{i\gamma}(\alpha,\beta)) = C (\alpha,\beta)$.

The canonical way to identify points on the Riemann sphere with points
on the normal two-sphere $\mathbb{S}^2$ is *stereographic projection*.
Basically, we think of $\mathbb{C} \simeq \mathbb{R}^2$ as a plane,
place a unit sphere at the origin so it is sliced in half, and draw
lines from points on the plane to the north pole of the sphere.
Wherever they hit is the (inverse) projection onto the sphere.
In coordinates, the line from $\zeta = x + iy = r e^{i\phi'}$ to $(0, 0, 1)$ is
given by

$$
(\lambda x, \lambda y, 1-\lambda), \quad \lambda \in \mathbb{R},
$$

which intersects the unit sphere at

$$
\lambda^2 r^2 + (1-\lambda)^2 = 1 \quad \Longrightarrow \quad
\lambda = \frac{2}{1 + r^2} \quad \Longrightarrow \quad
\left(\frac{2x}{1 + r^2}, \frac{2y}{1 + r^2}, \frac{r^2-1}{1 + r^2}\right).
$$

The resulting coordinates on the sphere $(\theta, \phi)$ are easily
seen to be $\phi = \phi'$ and

$$
\cos\theta = \frac{r^2-1}{1 + r^2}.
$$

From the circle map, $r = |\alpha /\beta|$, so

$$
\cos\theta = \frac{|\alpha/\beta|^2-1}{1 + |\alpha/\beta|^2} =
\frac{|\alpha|^2 - |\beta|^2}{|\alpha|^2 + |\beta|^2} = |\alpha|^2 - |\beta|^2.
$$

#### References

https://www.physast.uga.edu/~mgeller/JPA34p10243.pdf
