---
Layout: post
mathjax: true
comments: true
title:  "The unreasonable effectiveness of Fermi estimates"
categories: [Physics, Hacks, Mathematics, Statistics]
date:  2021-01-04
---

**January 4, 2021.** *Why are Fermi approximations so effective?*

#### Introduction

Fermi estimates are the art of order-of-magnitude approximation.
I've written about them
[extensively](https://hapax.github.io/assets/fermi-estimates.pdf)
[before](https://hapax.github.io/physics/teaching/hacks/napkin-hacks/#sec-3),
but I've never really found a satisfactory explanation for why they
are so effective.
It is not merely that order-of-magnitude is a forgiving notion of
correctness.
I have found that, time and time again, they are better than they have
any right to be!

Clearly, there must be an underlying statistical explanation for this
unreasonable effectiveness.
Interestingly, it seems to be the same mechanism underlying the
curious distribution of first digits in naturally occurring numbers,
called [Benford's law](https://en.wikipedia.org/wiki/Benford%27s_law),
which we'll review below.

<!-- https://arxiv.org/pdf/cond-mat/9808305.pdf -->
