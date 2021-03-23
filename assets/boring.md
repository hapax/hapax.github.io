---
Layout: post
mathjax: true
comments: true
title:  "Boring numbers and the axiom of choice"
categories: [Mathematics]
date:  2021-03-22
---

**March 22, 2021.** *Stuff*

#### Introduction

It is a
[running joke](https://en.wikipedia.org/wiki/Interesting_number_paradox)
among mathematicians that, not only are there are no boring numbers, but you can
prove it. Here's the proof. Let $B$ be the set of boring numbers. Define $b = \min B$ as
the smallest boring number. But this is a unique property, so $b$ is
interesting after all!
This is a joke, but there is a sting in the tail.
We are implicitly using the fact that "numbers" refers to "positive
whole numbers"

$$
\mathbb{N} = \{0, 1, 2, 3, \ldots\}.
$$

If we weren't, then the *minimum* we used to get our contradiction
wouldn't always work!
For instance, say we work with the integers

$$
\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}.
$$

The set of boring integers $B_\mathbb{Z}$ may be unbounded below.
Thankfully, we could just consider *absolute values*, and define the
smallest boring number(s) as

$$
b = \argmin_{k\in \mathbb{Z}} |k|.
$$

This might actually give us two numbers, $\pm b$, but both of these
numbers are interesting, so there are no boring integers.

#### Boring real numbers

Perhaps we can go on in this way to 
