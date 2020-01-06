---
Layout: post
mathjax: true
comments: true
title:  "The awesome power of simple physics"
categories: [Physics, Teaching]
date:  2020-01-06
---

**January 6, 2020.** *Physics is often presented as the most arcane,
  mathematically impenetrable of natural sciences. Here, we illustrate
  how some simple physics hacks, involving on pre-calculus
  mathematics, can still be awesomely powerful.*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Hacks</a>
   1. <a href="#sec-2-1">Dimensional analysis</a>
   2. <a href="#sec-2-2">Fermi estimates</a>
   3. <a href="#sec-2-3">Random walks</a>
   4. <a href="#sec-2-4">Scaling</a>
3. <a href="#sec-3">Caveat emptor</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

I've been heavily involved in running a
[high school physics circle](https://outreach.phas.ubc.ca/events/metro-vancouver-physics-circle/)
for over a year now.
I've learned a lot about logistics, leadership, and balancing leaning
towers of pizza.
But surprisingly, the biggest lesson has been about *physics itself*.
In a physics circle (or high school physics competition more
generally), the mandate is to write problems that high school students
will find challenging but fair given their limited background knowledge.
In particular, problems should avoid calculus, which is not part of
Canada's high school curriculum.
Judging from competition problems, this should restrict us to
tediously intricate mechanics problems, with a smattering of circuits,
optics, and other random elementary topics.

I decided to view this as a challenge: do more with less, i.e. find
ways to introduce advanced topics without pages of tedious algebra.
As a theoretical physicist used to employing a full arsenal of
mathematical tools, this was a strict constraint!
But perversely, creative outcomes are often optimised by *adding* constraints.
In trying to get at more advanced topics, I was led to reappraise
basic physics hacks like dimensional analysis.
Though I am not above writing tediously intricate mechanics problems,
it was much more exciting to use these simple tools to teach myself
something new, with the added benefits that genuine enthusiasm brings.

The goal of this post is to share a few of these hacks.
Hopefully, you'll be convinced of the awesome power of simple physics!
To keep things interesting, I've avoided overlap with my
[physics circle problems](https://hapax.github.io/assets/circle-probs.pdf)
and [notes](https://hapax.github.io/assets/dimensional-analysis.pdf),
though feel free to check these out if you want more examples than you
can dangle a plumb bob at.
I also recommend Sanjoy Mahajan's book
[*Street-Fighting Mathematics*](http://streetfightingmath.com/) (which
I only discovered recently!) which covers similar ground in greater depth.

## 2. Hacks <a id="sec-2" name="sec-2"></a>

The goal generally is not 

##### 2.1. Dimensional analysis <a id="sec-2-1" name="sec-2-1"></a>

Physics involve measuring physical systems.
The *dimension* of a measurement is the physical property of a system
probed by the measurement.
Basic examples include *length* ($L$), *time* ($T$) and *mass* ($M$).
We use brackets $[\cdot]$ to extract the dimension from a measurement,
so that for instance

\[
[1 \text{ cm}] = L, \quad [4 \text{ hours}] = T, \quad
[400 \text{ lb}] = M.
\]

Note that to find the dimension, we can throw away the number out
front and focus on the unit, asking: what aspect of the system does it
measure?

Other dimensions can be built from these basic dimensions, using
simple algebraic rules.
These are easier to show than to tell.
Area, for example, has dimensions $L^2$:

\[
[1 \text{ cm}^2] = [1 \text{ cm} \times 1 \text{ cm}] = [1 \text{ cm}]
\times [1 \text{ cm}] = L^2.
\]

A more direct way to see this is to use a general result, e.g. the
area of a rectangle:

\[
[\text{area}] = [\text{width}\times \text{height}] = [\text{width}]
\times [\text{height}] = L^2.
\]

More interesting examples are 

##### 2.2. Fermi estimates <a id="sec-2-2" name="sec-2-2"></a>

##### 2.3. Random walks <a id="sec-2-3" name="sec-2-3"></a>

##### 2.4. Scaling <a id="sec-2-4" name="sec-2-4"></a>

## 3. Caveat emptor <a id="sec-3" name="sec-3"></a>

## Extra

*Physics is often presented as the most arcane
  and mathematically challenging of natural sciences. But simple physical
  ideas, combined with pre-calculus mathematics, can be
  mind-bogglingly powerful. I give several examples.*

   5. <a href="#sec-2-5">Binomial approximation</a>
   6. <a href="#sec-2-6">Stefan-Boltzmann law</a>
   7. <a href="#sec-2-7">Randomness and entropy</a>
   8. <a href="#sec-2-8">Quantisation</a>
   9. <a href="#sec-2-9">Relativity</a>

##### 2.5. Binomial approximation <a id="sec-2-5" name="sec-2-5"></a>

##### 2.6. Stefan-Boltzmann law <a id="sec-2-6" name="sec-2-6"></a>

##### 2.7. Randomness and entropy <a id="sec-2-7" name="sec-2-7"></a>

##### 2.8. Quantisation <a id="sec-2-8" name="sec-2-8"></a>

##### 2.9. Relativity <a id="sec-2-9" name="sec-2-9"></a>

fractals, quantisation, entropy


Our best theories of nature seem to involve hard mathematics.
We have electromagnetism, formulated in the language of vector
\[
\begin{align*}
\nabla \cdot \mathbf{E} & = \frac{1}{\epsilon}\rho \\
\nabla \cdot \mathbf{B} & = 0 \\
\nabla \times \mathbf{E} & = -\mu\dot{\mathbf{B}} \\
\nabla \times \mathbf{B} & = \mu\mathbf{J} + \epsilon\dot{\mathbf{E}}
\end{align*}
\]
to Schrödinger
\[
i\frac{\partial}{\partial t}|\psi\rangle = \left(-\frac{\hbar^2}{2m}\nabla^2 + \hat{V}\right)|\psi\rangle
\]
to Einstein
\[
R_{\mu\nu} - \frac{1}{2}\Lambda R g_{\mu\nu} = 8 \pi G T_{\mu\nu},
\]
physics seems at its most powerful and exotic when expressed in
mathematical language.
The more opaque, the more powerful and exotic it seems.

**January 6, 2020.** *Physics is often presented as arcane and
  mathematically challenging. In this post, I try to counter this
  notion by showing that simple physical ideas, combined with
  pre-calculus mathematics, can be mind-bogglingly powerful.*

Physics is embedded in mathematics.
Our best theories of nature seem to require it, and are often stated in the
pithy but impenetrable form of *equations*.
For instance, we can summarise gravity with *Einstein's field equations*:
\[
R_{\mu\nu} -\frac{1}{2}R g_{\mu\nu} = 8\pi G T_{\mu\nu}.
\]
This is a startingly beautiful result, but requires years of training
to appreciate mathematically.
