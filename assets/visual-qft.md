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
an $n$-dimensional vector space of $b_i \in \mathbb{F}_2 = \{0, 1\}$.
In quantum mechanics, the corresponding Hilbert space of $n$ quantum
bits, or *qubits*, is exponentially bigger, since *each $n$-bit
string* is now a basis element, $|b_1 b_2\cdots b_n\rangle$.
The vector space is exponentially bigger.
It's also over the complex numbers, $\mathbb{C}$, rather than a finite
field, but this turns out to be less useful than the increase in
dimension.



##### 2. Polygons<a id="sec-2" name="sec-2"></a>

But there are various hacks and workarounds, and one of the most
powerful you already (secretly) know about.
Using Cartesian axes, we can draw 

##### 2.1. Form and function<a id="sec-2-1" name="sec-2-1"></a>

##### Extra

A set of $n$ classical bits can be viewed as an $n$-dimensional
vectors space (over a finite field $\mathbb{F}_2$), with $n$ basis vectors.
A set of $n$ *quantum* bits also gives rise to vector space, but every
single $n$-bit string is now a basis vector, so it has $2^n$ basis
vectors and is exponentially larger.
(It also is over an infinitely bigger field $\mathbb{C}$, but the rules
of quantum mechanics make this less useful than the exponential increase in dimension.)
Figuring out how to best make use of this exponentially larger vector
space is a subtle and ongoing question.

But even a 
We have evolved in a three-dimensional world to see three-dimensional
things.
Our visual cortex just isn't designed for anything more than that!

We will start with a simpler question --- how to *visualize* the
higher dimensional vectors and operations --- and find that, in
answering, we end up building a robust computational tool called the
*quantum Fourier transform* (QFT).
