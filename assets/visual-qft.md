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
   3. <a href="#sec-2-3">Peculiar polygons</a>
2. <a href="#sec-3">The Quantum Fourier Transform</a>
   1. <a href="#sec-3-1">Overlaps and linkages</a>
   2. <a href="#sec-3-2">Tensor products</a>

### 1. Introduction <a id="sec-1" name="sec-1"></a>

*Prerequisites: basic quantum mechanics, linear algebra, and group
 theory (optional).*

In quantum mechanics, a system is describe by a vector in a Hilbert
space.
Hilbert space is very, very large, and this is the main reason quantum
computers are more powerful than classical ones. But this leads to two
problems: how can we effectively use a big Hilbert space?
And how can we picture what's going on?
It turns out that, sometimes, the answers coincide.
In this tutorial, we will see that, in seeking a convenient way to
visualize high-dimensional Hilbert spaces, we will naturally arrive at
the *quantum Fourier transform* (QFT), a workhorse protocol in quantum
computing underlying dramatic quantum speedups like Shor's algorithm.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qubit.png"/>
	</div>
	</figure>

To be a little more precise, let's consider a classical computer which
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
for reasons we will discover in the next section.

##### 2.2. A better basis <a id="sec-2-2" name="sec-2-2"></a>

Let's see what we can do with all this pictorial power at our disposal.
A warm-up task is simply to draw the computational basis states, $|k\rangle$ for
$k \in I$, since (as the name suggests) this is a good basis for doing
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

for some radius $r$ and angle $\theta$.
To ensure we end up back where we started after $d$ points, we require
$d\theta$ to be a multiple of $2\pi$, or $\theta = 2\pi s/d$ for some
integer $s$.
The $r$ is irrelevant for choosing a basis, so we set it to $1$, and
normalize later to get states.
We define the resulting regular polygonal vectors and eigenstates by

$$
\vec{\chi}^s_d := \sum_{k=0}^{d-1} e^{i 2\pi s/d} |k\rangle, \quad
|\chi^d_s\rangle := \frac{1}{\sqrt{d}}\vec{\chi}^s_d.
$$

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
\omega^k$. If we choose a primitive root of unity $\omega = e^{i 2\pi/d}$, then
all roots of unity have the form $2^{i 2\pi s/d}$ for $s = 0, 1, 2,
\ldots, d- 1$.
This gives rise to the $d$ unnormalized eigenvectors, and
corresponding eigenstates, we found above:

$$
\vec{\chi}^s_d := \sum_{k=0}^{d-1} e^{i 2\pi s/d} |k\rangle, \quad
|\chi^d_s\rangle := \frac{1}{\sqrt{d}}\vec{\chi}^s_d.
$$

More generally, if $I$ is interpreted as some other finite group $G$,
figuring out how to draw the maps $G \to \mathbb{C}$ and choose a
basis is an interesting problem.
But we leave that for another time!

---

##### 2.3. Peculiar polygons<a id="sec-2-3" name="sec-2-3"></a>

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

You can enter your own values of $s$ and $d$, and see the
corresponding polygons using [this doodad](https://hapax.github.io/assets/polygon1/).
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

But although degeneracy is unavoidable, in this basis the degeneracy is
patterned in a useful way.
If $(a, b)$ denotes the greatest common divisor of $a$ and $b$, then
$\vec{\chi}^s_d$ will wrap around itself $(s, d)$ times, and hence have

$$
[s, d] := \frac{d}{(s, d)}
$$

sides.
This includes $s = 0$, since $(0, d) = d$.
In fact, this has an amusing (optional) consequence for number theory.

---

*Number theory aside.*

---

### 3. The Quantum Fourier Transform <a id="sec-3" name="sec-3"></a>

##### 3.1. Overlaps and linkages<a id="sec-3-1" name="sec-3-1"></a>

##### 3.2. Tensor products<a id="sec-3-2" name="sec-3-2"></a>
