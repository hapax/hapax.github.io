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

To be a little more precise, let's consider a classical computer which
stores $n$ bits, $b_1, b_2, \ldots, b_n$.
There are $2^n$ possible states of the computer, consisting of all
$n$-bit strings $b_1b_2\cdots b_n$.
For the purposes of analogy, we can view these strings as vectors in
an $n$-dimensional vector space over the field with two elements $\mathbb{F} = \{0, 1\}$.
In quantum mechanics, the corresponding vector space of $n$ quantum
bits, or *qubits*, is *exponentially* bigger, since *each $n$-bit
string* is now a basis element, $|b_1 b_2\cdots b_n\rangle$.
The vector space is exponentially bigger.
(It's also over the complex numbers, $\mathbb{C}$, rather than a finite
field, but this turns out to be less useful than the increase in
dimension.)
So, Hilbert space is huge, and we have to learn some ways to navigate it.
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
of sinqle qubit states on a sphere, but as soon as we have a bigger
Hilbert space, this method fails.
It is radically non-scaleable.
Clearly, we cannot approach this problem directly!
The question becomes: is there useful a way to visualize points in an
arbitrary Hilbert space?

##### 2.1. Form and function<a id="sec-2-1" name="sec-2-1"></a>

The answer is a resounding yes, and in fact, you probably (secretly) already know it.
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
of points labelled by $i \in I, I = \{0, 1, \ldots, d- 1\}$.
Then we can represent a vector in $\mathbb{R}^d$ as a map $I \to \mathbb{R}$.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/qft2.png"/>
	</div>
	</figure>
