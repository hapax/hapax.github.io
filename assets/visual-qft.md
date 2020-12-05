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
   3. <a href="#sec-2-3">That's a wrap!</a>
2. <a href="#sec-3">The Quantum Fourier Transform</a>
   1. <a href="#sec-3-1">Overlaps and linkages</a>
   2. <a href="#sec-3-2">The magic of factorization</a>
   3. <a href="#sec-3-3">Algorithms</a>

### 1. Introduction <a id="sec-1" name="sec-1"></a>

*Prerequisites: basic quantum mechanics, linear algebra, and some
 background in quantum computing.*

In quantum mechanics, a system is described by a vector in a Hilbert
space.
Hilbert space is very, very large, and this is the main reason quantum
computers are more powerful than classical ones. But this leads to two
problems: how can we effectively use a big Hilbert space?
And how can we picture what's going on?
It turns out that, sometimes, the answers coincide.
In this tutorial, we will see that, in seeking a convenient way to
visualize high-dimensional Hilbert spaces, we will naturally arrive at
the *quantum Fourier transform* (QFT), a workhorse protocol in quantum
computing which underlies dramatic quantum speedups like Shor's algorithm.

<!-- Let's consider a classical computer which
stores $n$ bits, $b_1, b_2, \ldots, b_n \in \\{0, 1\\}$.
There are $2^n$ possible states of the computer, consisting of all
$n$-bit strings $b_1b_2\cdots b_n$.
For the purposes of comparison, we can view these strings as vectors in
an $n$-dimensional vector space over the field with two elements, $\mathbb{F}_2 = \\{0, 1\\}$.
For $n$ *quantum bits*, or *qubits*, each $n$-bit string is now a basis element, $|b_1 b_2\cdots b_n\rangle$.
Thus, the vector space is exponentially bigger.
(It's also a vector space over the complex numbers, $\mathbb{C}$,
rather than a finite field, but this turns out to be less useful than the increase in
dimension.)
If Hilbert space is huge, we must learn to navigate it.
<!-- So, Hilbert space is huge.
Our task is to see it, reason about it, and make use of it. -->

##### 2. Polygons<a id="sec-2" name="sec-2"></a>

To make our problem sharper, let's consider the problem of visualizing
the simplest nontrivial system, a single qubit.
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
Luckily, the global phase ambiguity and normalization constraint mean
we can directly draw the space of sinqle qubit states on a sphere, as
below:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qubit.png"/>
	</div>
	</figure>

<!-- Similarly, there is a way to directly visualize the states of a qutrit, with $d
= 3$. -->
But any bigger, and the method fails!
So trying to directly visualize things does not scale at all.
<!-- Clearly, we cannot approach this problem directly. -->
The question becomes: is there useful indirect way to picture points in an
arbitrary Hilbert space, and help us navigate the hugeness?

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qubit2.png"/>
	</div>
	</figure>

##### 2.1. Form and function<a id="sec-2-1" name="sec-2-1"></a>

The answer is a resounding yes, and in fact, you probably (secretly)
already know the solution.
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
of points labelled by $k \in I, I = \\{0, 1, \ldots, d- 1\\} =: [d]$.
Then we can represent a vector in $\mathbb{R}^d$ as a map $f: I \to
\mathbb{R}$.
We can add and multiply these maps as usual, $f  +g, \lambda f$.
To figure out which $k \in [d]$ is responsible for which point on the plane, we simply project
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

Of course, we could stack copies of $\mathbb{C}$ on top of each
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

There is a loose end here---or rather, two loose ends!
The first and last point on the chain are unattached. If we
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
This gives us a way to represent any vector in any finite-dimensional
Hilbert space.
<!-- If $I$ labels the basis, then we can think of a vector as a map $f: I
\to \mathbb{C}$ and draw its image on the complex plane.-->
These polygons add component-wise, and scalar multiply by complex numbers
in a natural way.
If we write an arbitrary scalar as $z = \lambda e^{i\theta}$,
multiplication by $z$ scales the whole figure by $\lambda$ and rotates
it an angle $\theta$ counterclockwise, both with respect to the
origin. We give examples below:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/transform.png"/>
	</div>
	</figure>

All of this holds for open chains as well. But polygons are preferable
for reasons we will discover shortly.

##### 2.2. A better basis <a id="sec-2-2" name="sec-2-2"></a>

Let's see what we can do with all this pictorial power at our disposal.
A warm-up task is simply to draw the computational basis states, $|k\rangle$ for
$k \in [d]$, since (as the name suggests) this is a good basis for doing
computations.
Unfortunately, our method fails at the first hurdle!
Here's what most of the basis vectors look like:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft6.png"/>
	</div>
	</figure>

It starts at $0$, stays there for a while, goes to $1$ at the $k$th
node, then returns to the origin.
We can't even tell what state we're in unless we introduce more
labels!

There are two ways we could see this: a failing of our method, or a
failing of the basis.
We will, of course, take the partisan viewpoint that the basis is at
fault, and look for a better one.
If we were dealing with chains, the way forward would be decidedly
ugly and non-unique.
But our choice of polygons pays off, since the uniquely nice objects
to use are the *regular* polygons!
These consist of points equally spaced around the circle, or

$$
\vec{v} = \sum_k r e^{ik\theta} |k\rangle,
$$

for some constant $r$ and angle $\theta$.
To ensure we end up back where we started after $d$ points, we require
$d\theta$ to be a multiple of $2\pi$, or $\theta = 2\pi s/d$ for some
integer $s$.
The $r$ is irrelevant for choosing a basis, so we set it to $1$, and
normalize later to get states.
We define the resulting regular polygonal vectors and eigenstates by

$$
\vec{\chi}^s_d := \sum_{k=0}^{d-1} e^{2\pi i s/d} |k\rangle, \quad
|\chi^s_d\rangle := \frac{1}{\sqrt{d}}\vec{\chi}^s_d.
$$

We can directly check that these not only form a basis, but that the
eigenstates are orthonormal.
Assuming $t \neq s$ (modulo $d$), we have

$$
\begin{align*}
\langle \chi^{t}_d |\chi^s_t\rangle & = \frac{1}{d}\sum_{k=0}^{d-1} e^{2\pi i
(s-t)/d}  = \frac{1}{d} \cdot \frac{1 - e^{2\pi i d (s-t)/d}}{1 - e^{2\pi i (s-t)/d}} = 0,
\end{align*}
$$

where we summed using a geometric series and used the fact that $s -
t$ is an integer.
Thus, the $|\chi^s_d\rangle$ form an orthonormal basis.
We give a slightly more elegant group-theoretic motivation below.

---

*Group theory aside.* Our choice of representation is guided by the
structure we put on the index set $I$ itself. When we draw vectors as
marked chains, we are effectively thinking of $I$ as an ordered set.
When we draw it as a polygon, we are implicitly thinking of $I$ as a *cyclic
group*, say $I = \mathbb{Z}/d\mathbb{Z}$.
This group is generated by the operation of subtracting $1$, or $S: |k\rangle \mapsto
|k-1\rangle$ modulo $d$.
This corresponds to a unitary matrix

$$
S = \left[
\begin{matrix}
0 & 0 & 0 & \cdots & 0 & 1 \\
1 & 0 & 0 & \cdots  & 0 & 0\\
0 & 1 & 0 & \cdots  & 0 & 0\\
&&&\ddots& \\
0 & 0 & 0 & \cdots & 1 & 0
\end{matrix}
\right].
$$

We will choose our basis to be eigenstates of $S$.
The first thing to note is that $S^d = \mathbb{I}$,
since after $d$ shifts we end up where we started.
For any eigenstate $|\psi\rangle$ with eigenvalue $\omega$, it follows that

$$
S^d |\psi\rangle = \omega^d |\psi\rangle = |\psi\rangle,
$$

and hence $\omega^d = 1$.
Thus, $\omega$ must be a root of unity, and $|\psi\rangle$ is mapped
to itself up to a global phase.
For a polygon, $S$ shifts the black dot along a polygon.
If $|\psi\rangle$ is an eigenstate, we can undo this by a rotation,
which means precisely that $|\psi\rangle$ is regular!
We illustrate for an equilateral triangle below:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft7.png"/>
	</div>
	</figure>

Let's now find the eigenstate of $S$ associated with a $d$th root of
unity $\omega$.
Writing $|\psi\rangle = \sum_k \alpha_k |k\rangle$, we have

$$
(S - \omega) |\psi\rangle = \sum_k (\alpha_k |k-1\rangle -
\omega\alpha_k |k\rangle) = \sum_k (\alpha_{k+1} - \omega
\alpha_k)|k\rangle = 0,
$$

where we relabelled the dummy index $k \to k +1$ in the first term.
This means we have a relation $\alpha_{k+1} = \omega\alpha_{k}$ for
all $k$, modulo $d$.
Without loss of generality (and ignoring normalization for the
moment), we can set $\alpha_0 = 1$ and iterate, so that $\alpha_k =
\omega^k$. If we choose a primitive root of unity $\omega_d = e^{2\pi i/d}$, then
all roots of unity have the form $\omega_d^{s}$ for $s \in [d]$.
This gives rise to the $d$ unnormalized eigenvectors, and
corresponding eigenstates, we found above:

$$
\vec{\chi}^s_d := \sum_{k=0}^{d-1} e^{2\pi i s/d} |k\rangle, \quad
|\chi^d_s\rangle := \frac{1}{\sqrt{d}}\vec{\chi}^s_d.
$$

These automatically form a basis, and in fact are orthogonal, since
they are eigenstates of a unitary operator.

<!-- More generally, if $I$ is interpreted as some other finite group $G$,
symmetries act as unitary matrices.
Figuring out how to draw the maps $G \to \mathbb{C}$, and choosing a
basis, is an interesting problem we leave for another time! -->

---

##### 2.3. That's a wrap! <a id="sec-2-3" name="sec-2-3"></a>

When picturing these regular polygons, there are a few peculiarities
to keep in mind.
First, when $s = 0$, all the points lie at $1$.
This is, in a sense, a sort of degenerate regular polygon where,
between each node, we execute a full revolution around the origin:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft8.png"/>
	</div>
	</figure>

There is a less extreme degeneracy where regular polygons
overlap themselves.
We give the example of $d = 8, s = 2$ above, where a "regular octagon"
has degenerated into two squares sitting on top of each other.
But although points can degenerate into each other, the basis elements
are always distinct, provided you know $d$: you simply see where the
first arrow goes.
If it arrives at a point $e^{i\theta}$, then $s = d\theta/2\pi$.
Thus, we have indeed eliminated the ambiguity that plagued the
computational basis, without any need for additional labels.

Let's give a simple example.
For a qubit, $d = 2$, and the two polygonal states are

$$
\begin{align*}
|\chi^0_2\rangle & = \frac{1}{\sqrt{2}}\sum_{k=0}^1 e^{2\pi i
0 \cdot k/d}|k\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle \\
|\chi^1_2\rangle & = \frac{1}{\sqrt{2}}\sum_{k=0}^1 e^{2\pi i 1 \cdot
k/d}|k\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = |-\rangle.
\end{align*}
$$

These are just the familiar eigenstates $|\pm\rangle$ of the $X$
observable!
We draw them below:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft9.png"/>
	</div>
	</figure>

You can generate polygons for arbitrary $s$ and $d$ using the
[polygon applet](https://hapax.github.io/assets/polygon1/).
For instance, we can enter $d = 17$ and $s = 7$, and the corresponding
basis element will be displayed:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/poly1.png"/>
	</div>
	</figure>

You can toggle arrow tips with "t":

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/poly2.png"/>
	</div>
	</figure>

The wrapped polygons obey a simple pattern.
For any $d$, there are only two convex, non-degenerate regular
polygons, i.e. regular $d$-gons, occurring at $s = 1$ and $s = d-1$.
For other values of $s$ which are relatively prime with $d$, we get *stellated* non-degenerate
polygons, which have $d$ sides but intersecting edges.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft10.png"/>
	</div>
	</figure>

To understand the general case, note that if $f$ is a common divisor of
$d$ and $s$ (written $f | d$, $f | s$), then $k = d/f$ is an integer such that

$$
\frac{2\pi ks}{d} = \frac{2\pi ds}{df} = \frac{2\pi s}{f} \in 2\pi \mathbb{Z}.
$$

Thus, at the $k$th node the polygon wraps back to $1$.
If $g = \text{gcd}(s, d)$ is the *greatest* common divisor, then $k =
d/g$ is the first node at which the polygon $\vec{\chi}^s_d$ returns
to $1$.
Hence, $\vec{\chi}^s_d$ is a polygon with $d/g$ sides which wraps
itself $g$ times.
This has an amusing (and optionally readable) consequence for number theory.

---

*Number theory aside.*
 The count of $s \in [d]$ relatively prime to $d$ is given by Euler’s
 totient function $\phi(d)$. Similarly, $\phi(d/f)$ counts the
 values $s$ for which $\text{gcd}(d, s) = f$, since

$$
\text{gcd}(d, s)  = f \quad \Leftrightarrow \quad \text{gcd}(d/f, s)
= 1.
$$

Thus, $\phi(d/f)$
 counts the regular polygons wrapping $f$ times. Since $d/f = f'$ is
 just another way of enumerating factors of $d$, and every polygon
 must wrap $f$ times for some factor $f$, we deduce that

$$
\sum_{f|d} \phi(f) = d.
$$

This identity was first proved by Gauss in his *Disquisitiones Arithmeticae*.

---

### 3. The Quantum Fourier Transform <a id="sec-3" name="sec-3"></a>

The purpose of the last section was to introduce a way to draw vectors
in big Hilbert spaces.
The computational basis is ill-adapted to this representation, so we
came up with a new basis which jived better.
But we shouldn't throw out the computational basis altogether!
It's the closest thing we have to working with bit strings, and hence
a natural place to do many quantum information-processing tasks.

We can have our basis and eat it too if we find a way to *convert*
between the computational and polygonal vectors.
This is where the Quantum Fourier Transform (QFT) comes from.
It is simply the active change of basis from computational states to
regular-polygonal states,

$$
\text{QFT}_d: |s\rangle \mapsto |\chi^s_d\rangle,
$$

extended linearly to the full Hilbert space.
As a simple example, our $d =2$ example above shows that $\text{QFT}_2
= H$, the Hadamard matrix.
We show the action on the basis for $d = 5$ below:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft11.png"/>
	</div>
	</figure>

In general, it is a matrix (also called the *Walsh-Hadamard matrix*)
with elements

$$
\langle j|\text{QFT}_d |k\rangle = \langle j|\chi^k_d\rangle =
\frac{1}{\sqrt{d}}\omega_d^{jk}.
$$

We could finish the tutorial here if we liked, but in the next few
sections, we'll outline some fun features of the QFT,
including a neat geometrical interpretation, the magic of
factorization, and algorithmic aspects.

##### 3.1. Overlaps and linkages<a id="sec-3-1" name="sec-3-1"></a>

The QFT is, by definition, an active change of basis.
In the context of linear algebra, it's slightly more natural to think
of a *passive* change of basis, which finds the coefficients $A_s$ in
the polygonal basis,

$$
|\psi\rangle = \sum_k \alpha_k |k\rangle = \sum_s A_s |\chi^s_d\rangle.
$$

Since $|\chi^s_d\rangle$ is an orthonormal basis, it's easy to extract $A_s$
from an overlap:

$$
\begin{align*}
A_s = \langle \chi^s_d |\psi\rangle & = \sum_k \alpha_k \langle
\chi^s_d|k\rangle = \frac{1}{\sqrt{d}}\sum_k \alpha_k \omega_d^{-ks}.
\end{align*}
$$

This passive operation is called the Discrete Fourier Transform
(DFT).
The DFT and QFT are just inverses of each other, in the sense that the
coefficients of a quantum Fourier-transformed vector, in the
computational basis, are given by the DFT:

$$
\text{QFT}|\psi\rangle = \sum_k \alpha_k \text{QFT}|k\rangle = \frac{1}{\sqrt{d}}\sum_s
\sum_k \alpha_k \omega_d^{ks} |s\rangle = \sum_s A_{-s}|s\rangle.
$$

It turns out that the coefficients $A_s$ have a simple geometric
interpretation.
We can take a vector $\vec{v} = \sum_k v_k |k\rangle$, and concatenate the
complex numbers $v_k$, tip-to-tail, on the complex plane.
We'll call this a *linkage*.
The *value* $V(\vec{v})$ is the point at which the last arrow of the linkage ends.
We give an example for a qutrit below, with the usual polygon in red,
the linkage in cyan, and the value in purple.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/linkage1.png"/>
	</div>
	</figure>

The overlap $(\vec{\chi}^s_d)^\dagger \vec{v}$ is just the value of
the vector

$$
\vec{v}_s = \sum_k v_k \omega_d^{-ks} |k\rangle.
$$

Mechanically, we can think of $\vec{v}_s$ as a hinged motion of the
linkage associated with $\vec{v}$.
We leave the first arrow in the linkage alone, then rotate the rest
by $\omega_d^{-s}$.
Then we move along and rotate all but the first two by
$\omega_d^{-s}$.
We continue in this way until $v_k$ has been rotated by
$\omega_d^{-ks}$.
Finally, to get the overlap with $|\chi^s_d\rangle$, we simply divide
by $\sqrt{d}$.

You can gain intuition for how the Fourier transform is related to hinged motion in this
[linkage applet](https://hapax.github.io/assets/polygon1/).
Click to create the points in the vector, which are now displayed as
complex numbers, i.e. arrows from the origin:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/linkage2.png"/>
	</div>
	</figure>

You can toggle a faint polygon with "p":

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/linkage3.png"/>
	</div>
	</figure>

To see the corresponding linkage, press "l":

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/linkage4.png"/>
	</div>
	</figure>

You can also display the value using "v":

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/linkage6.png"/>
	</div>
	</figure>

Finally, you can enter the parameter $s$ for the Fourier transform in
the box above left:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/linkage5.png"/>
	</div>
	</figure>

In fact, you can enter *arbitrary* $s$ to see a "continuous" hinged
motion, though the QFT only involves integer $s$.
The Fourier coefficient $A_{-s}$ is divided by a factor
of $\sqrt{d}$, but we have omitted this for visual clarity.

##### 3.2. The magic of factorization<a id="sec-3-2" name="sec-3-2"></a>

It turns out that the QFT and the DFT are tremendously important
operations in their own right.
For instance, if we take the limit of a continuous curve on the
complex plane, with $d \to \infty$, we recover Fourier series.
We will focus our efforts in a different direction, however.
A quantum computer is a large quantum system, with Hilbert space of
size $d$ built out of $n$ smaller
quantum systems of size $d_i$.
The Hilbert spaces are related by the tensor product:

$$
\mathcal{H}_{d} \simeq \mathcal{H}_{d_0} \otimes \mathcal{H}_{d_1} \otimes
\cdots \otimes \mathcal{H}_{d_{n - 1}},
$$

where $d = d_0 d_1 \cdots d_{n - 1}$, and $\simeq$ indicates that
these spaces are isomorphic, but in a way we have to specify.
As a special but important case, a quantum computer made from $n$
qubits, with $d_i = 2$, has a Hilbert space of dimension $2^n$.
Interesting things happen for the QFT when the Hilbert space factorizes.
Consider the simple case $d = ab$, with

$$
\mathcal{H}_d \simeq \mathcal{H}_a \otimes \mathcal{H}_b.
$$

In order to canonically identify states on the left and right, we
define

$$
|k(m, n)\rangle = |na + m\rangle \simeq |m\rangle \otimes |n\rangle
$$

for $m \in [a], n \in [b]$. It's easier to see what's going on using a
picture.
Without factorization, we imagine the indices $s \in [d]$ arranged in
a single column of length $d$, and read downwards.
When we factorize, we rearrange this column into a $b \times a$ grid
or *index matrix*, and read like English, left-to-right and down:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/tensor1.png"/>
	</div>
	</figure>

Let's see what this implies for the QFT.
For a regular polygon $\vec{\chi}^s_d$, the coefficient of
$|k(m,n)\rangle$ is

$$
e^{2\pi i ks/d} = e^{2\pi i (na + m)s/ab} = e^{2\pi i ms/ab}e^{2\pi i ns/b} = \omega_a^{sm/b}\omega_b^{sn}.
$$

In the tensor product basis,

$$
\vec{\chi}^s_d \simeq \sum_{mn} \omega_a^{sm/b}\omega_b^{sn}|m\rangle\otimes|n\rangle = \sum_{m}\omega_a^{sm/b}|m\rangle \otimes \sum_n
\omega_b^{sn} |n\rangle = \vec{\chi}^{s/b}_a \otimes \vec{\chi}^s_b.
$$

Here, $\vec{\chi}^s_b$ is a regular polygonal basis element, but $\vec{\chi}^{s/b}_a$ is an odd beast.
Despite the notation, it is not a regular polygon at all, but rather
serves to make *copies* of $\vec{\chi}^s_b$, offset by angles $\theta
= 2\pi s/d$.
For this reason, we call it a copygon.
As a simple example, we can factorize a regular hexagon
$\vec{\chi}^1_6$ in two ways, as two triangles or three digons:

$$
\vec{\chi}^1_6 \simeq \vec{\chi}^{1/3}_2 \otimes \vec{\chi}^{1}_3
\simeq \vec{\chi}^{1/2}_3 \otimes \vec{\chi}^{1}_3.
$$

We picture the decompositions into copies of the second factor below:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/tensor6.png"/>
	</div>
	</figure>

The coloured node indicates the first node of the copy.
Once more, you can play with your own examples and build up intuition using the
[polygon applet](https://hapax.github.io/assets/polygon1/).
Suppose you are interested in $d = 12, s = 5$.
Without factorizing, it looks like:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/tensor2.png"/>
	</div>
	</figure>

To exploit $12 = 3 \times 4$, in the applet, replace $12$ by $3, 4$:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/tensor3.png"/>
	</div>
	</figure>

The dark figure is the copygon $s = 5/3, d= 4$, while the grey
triangle is the regular polygon $s = 5, d = 3$.
Pressing "c" will perform the copying:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/tensor4.png"/>
	</div>
	</figure>

The triangles are arrayed around the circle, according to the
instructions of the copygon.
In the index matrix, triangles correspond to columns and copygon
entries to rows, so we read "across" triangles to generate
$\vec{\chi}^5_{12}$.
We can demonstrate the correspondence (without recourse to a matrix) by
toggling "f" for "full polygon":

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/tensor5.png"/>
	</div>
	</figure>

In the general case $d = d_0 d_1\cdots d_{n-1}$, we can simply iterate this procedure:

$$
\vec{\chi}^s_{d} \simeq
\vec{\chi}^{d_{n-1}s/d}_{d_{n-1}} \otimes \cdots \otimes \vec{\chi}^{s/d_0}_{d_1} \otimes \vec{\chi}^{s}_{d_0}.
$$

We can view this as decomposing $d$ into a higher-dimensional index
tensor, which iterates over the tensor product basis, but the details
won't concern us here.

##### 3.3. Algorithms<a id="sec-3-3" name="sec-3-3"></a>

Crudely speaking, a quantum computer is a bunch of small, easily
manipulable modules joined together into a big system which does
complicated things.
Typically, these smaller systems have the same Hilbert space dimension, which we
will take to be $d_i = a$.
For $n$ such systems, the quantum computer has a Hilbert space of size
$d = a^n$, with regular polygonal states

$$
|\chi^s_{d}\rangle \simeq
|\chi^{sa^{1-n}}_{a}\rangle\otimes \cdots \otimes |\chi^{s/a}_{a}\rangle \otimes |\chi^{s}_{a}\rangle.
$$

##### Extra

This is precisely the case for a quantum computer made from $n$ qudits of dimension $a$.
We can use this factorization to quickly implement the QFT.
Here is a first pass which doesn't work.
Suppose we can construct the initial copygon, and we also have an
*expansion* operator, mapping

$$
|\chi^{x}_{a}\rangle \mapsto |\chi^{ax}_{a}\rangle.
$$

Then we simply build $n$ copies of the initial copygon, labelled by
$j \in [a]$, apply the expansion operator $j$ times to copy $j$, then tensor the
results together.
Assuming we can create initial copygons at fixed cost, the total
number of operations is

$$
n + \sum_{j=0}^{n-1}j = n + \frac{1}{2}n(n-1) = \frac{1}{2}n(n+1).
$$

The issue is that expansion is not a linear, let alone a unitary, operation.
More explicitly,

$$
|\chi^{x}_a\rangle = \frac{1}{\sqrt{a}}\sum_k \omega^{kx}_a |k\rangle \mapsto \sum_k
\frac{1}{\sqrt{a}}\omega^{(a-1)kx}_a \cdot \omega^{kx}_a |k\rangle
$$

acts on basis vectors in a way that depends on $x$.
But once $x$ is fixed, it acts via a matrix

$$
E^{(x)}_a = \mbox{diag}(\omega^{kx(a-1)}_a).
$$

This *is* unitary, since it has pure phases along the
diagonal. Similarly, the map which
constructs the initial copygon, defined by

$$
C^{(x)}_a|0\rangle = |\chi^x_a\rangle = \mbox{diag}(\omega^{kx}_a)
\circ \text{QFT}_a|0\rangle
$$

is unitary, since it composes a unitary matrix with the QFT, which is
also unitary.
Then we have

$$
E^{(a^{j-1}x)}_a \cdots E^{(ax)}_a E^{(x)}_aC^{(x)}_a |0\rangle =
|\chi^{xa^{j}}_a\rangle.
$$

Assuming all these operations are hardcoded, we can perform
the QFT with $O(n^2)$ gates.
By the linearity of quantum mechanics, we can use the same circuit to
yield the QFT of an arbitrary vector.

##### References and acknowledgments
