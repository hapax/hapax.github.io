---
Layout: post
mathjax: true
comments: true
title:  "A visual approach to the QFT"
date:  2020-11-27
---

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Polygons</a>
   1. <a href="#sec-2-1">Form and function</a>
   2. <a href="#sec-2-2">A better basis</a>

### 1. Introduction <a id="sec-1" name="sec-1"></a>

*Prerequisites: basic quantum mechanics and linear algebra.*

In quantum mechanics, a system is describe by a vector in a Hilbert
space.
These Hilbert spaces are huge, and this is in some sense the main
reason quantum computers are more powerful than classical ones.
But this leads to two problems: how can we effectively take advantage
of a these big Hilbert spaces?
And how can we picture what's going on?
It turns out that, sometimes, these questions have the same answer.
In seeking a convenient way to visualize high-dimensional Hilbert
spaces, we will stumble onto the *quantum Fourier transform* (QFT), a
workhorse protocol in quantum computing that underlies some of the
most dramatic quantum speedups, such as Shor's algorithm.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qubit.png"/>
	</div>
	</figure>

To be a little more precise, let's consider a classical computer which
stores $n$ bits, $b_1, b_2, \ldots, b_n$.
There are $2^n$ possible states of the computer, consisting of all
$n$-bit strings $b_1b_2\cdots b_n$.
For the purposes of analogy, we can view these strings as vectors in
an $n$-dimensional vector space over the field with two elements $\mathbb{F} = \\{0, 1\\}$.
In quantum mechanics, the corresponding vector space of $n$ quantum
bits, or *qubits*, is *exponentially* bigger, since *each $n$-bit
string* is now a basis element, $|b_1 b_2\cdots b_n\rangle$.
The vector space is exponentially bigger.
(It's also over the complex numbers, $\mathbb{C}$, rather than a finite
field, but this turns out to be less useful than the increase in
dimension.)
If Hilbert space is huge, we must learn to navigate it.
<!-- So, Hilbert space is huge.
Our task is to see it, reason about it, and make use of it. -->

##### 2. Polygons<a id="sec-2" name="sec-2"></a>

To make our problem sharp, let's consider the simplest nontrivial
system: a single qubit.
The classical bit can be in states $b = 0, 1$, so each of these is a
basis state of the qubit, $|b\rangle$.
A general vector in this Hilbert space is

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle, \quad \alpha, \beta
\in \mathbb{C}.
$$

Without further work, the space of states lives in $\mathbb{C}^2
\simeq \mathbb{R}^4$, which is already impossible to picture.
Our visual cortex evolved for three dimensions only!
There are some tricks that mean we *can* draw directly draw the space
of sinqle qubit states on a sphere (as above), but as soon as we have a bigger
Hilbert space, this method fails.
It is radically non-scaleable.
Clearly, we cannot approach this problem directly!
The question becomes: is there useful a way to visualize points in an
arbitrary Hilbert space?

##### 2.1. Form and function<a id="sec-2-1" name="sec-2-1"></a>

The answer is a resounding yes, and in fact, you probably (secretly) already know how.
Consider a graph $y = f(x)$ on the Cartesian plane.
You can add functions together and multiply them by real numbers, and
this turns them into a vector space!
Moreover, it's an *infinite-dimensional* vector space, since we can
think of each point $x$ as a basis vector.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft1.png"/>
	</div>
	</figure>

We certainly don't need all of those dimensions!
Instead of a continuous variable $x$, we can imagine a finite number
of points labelled by $k \in I, I = \\{0, 1, \ldots, d- 1\\}$.
Then we can represent a vector in $\mathbb{R}^d$ as a map $f: I \to
\mathbb{R}$.
We can add and multiply these maps as usual, $f  +g, \lambda f$.
To figure out which $k \in I$ is responsible for which point on the plane, we simply project
onto the $x$ axis.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft2.png"/>
	</div>
	</figure>

What about a *complex* vector with $d$ components?
A hack is simply to treat $\mathbb{C}^d \simeq \mathbb{R}^{2d}$, but
then multiplying a vector a complex number looks very unnatural.
Instead, we once again take inspiration from a familiar
infinite-dimensional trick: drawing the image of a parametrized curve
$f: I \to \mathbb{C}$, where $I \subseteq \mathbb{R}$.
We lose the information about *which* element of $I$ is associated
with a point on the curve, as the image below shows.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft3v1.png"/>
	</div>
	</figure>

Of course, we could stack copies of $\mathcal{C}$ on top of each
other, but this is harder to draw.
More importantly, it is unnecessary in finite dimensions!
We can recover the information about which $k$ maps to which complex
number as long as the function is into, i.e. there are no overlaps.
We simply draw a chain of points, and mark the first some way,
e.g. with a black dot.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft4v2.png"/>
	</div>
	</figure>

We now have a way to represent any vector in any finite-dimensional
Hilbert space.
If $I$ labels the basis, then we can think of a vector as a map $f: I
\to \mathbb{C}$ and draw its image on the complex plane.
These maps add component-wise, and scalar multiply by complex numbers
in a natural way.
If we write an arbitrary scalar as $z = \lambda e^{i\theta}$,
multiplication by $z$ scales the whole figure by $\lambda$ and rotates
it an angle $\theta$ counterclockwise, both with respect to the origin.

Before we move on, there is a loose end here---or rather, two loose ends!
The first and last point on the chain are unattached, but if we
connect them, the chain becomes a closed loop.
There is no law against this, but it does make the correspondence
between points and arguments ambiguous unless we specify a
direction to go around the loop.
We can do this by making edges directed:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft5.png"/>
	</div>
	</figure>

So rather than a chain with one marked end, vectors are now marked,
directed polygons.

##### 2.2. A better basis <a id="sec-2-2" name="sec-2-2"></a>

Now we have a nice representation, let's see what we can do with it.
Our first task is to picture the computational basis states, $|k\rangle$ for
$k \in I$, since (as the name suggests) this is a nice basis for doing
computations.
Unfortunately, our method does terribly!
Here's what most of the basis vectors look like:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft6.png"/>
	</div>
	</figure>

We start at $0$, stay there for a while, go to $1$ when we hit $k$,
then return to the origin.
To even tell what state we're in, we need to introduce more labels!
