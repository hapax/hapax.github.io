---
Layout: post
mathjax: true
comments: true
title:  "A visual approach to the QFT"
date:  2020-11-27
---

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Bla</a>

### 1. Introduction <a id="sec-1" name="sec-1"></a>

*Prerequisites: basic quantum mechanics.*

In quantum mechanics, the state of a physical system is a vector
$|\psi\rangle$ living in a Hilbert space $\mathcal{H}$, equipped with
an inner product and other goodies.
The computational magic of the quantum arises from multiple sources,
but chief among these is the fact that *Hilbert space is huge*.
A set of $n$ classical bits can be viewed as an $n$-dimensional
vectors space (over a finite field $\mathbb{F}_2$), with $n$ basis vectors.
A set of $n$ *quantum* bits also gives rise to vector space, but every
single $n$-bit string is now a basis vector, so it has $2^n$ basis
vectors and is exponentially larger.

Figuring out how to use this exponential increase for physics and
computer science is an ongoing question.
We will start with a simpler question --- how to *visualize* the
higher dimensional vectors and operations --- that ends up giving us a
robust computational tool called the *quantum Fourier transform* (QFT).

### 2. Grover search <a id="sec-2" name="sec-2"></a>
