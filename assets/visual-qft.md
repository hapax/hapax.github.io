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

In quantum mechanics, the state of a physical system is a vector
$|\psi\rangle$ living in a Hilbert space $\mathcal{H}$.
The main reason that quantum computers are more powerful than
classical computers is that *Hilbert space is huge*.

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

### 2. Polygons<a id="sec-2" name="sec-2"></a>

But there are various hacks and workarounds, and one of the most
powerful you already (secretly) know about.
Using Cartesian axes, we can draw 

### 2.1. Form and function<a id="sec-2-1" name="sec-2-1"></a>