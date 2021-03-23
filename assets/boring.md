---
Layout: post
mathjax: true
comments: true
title:  "Boring numbers and set theory"
categories: [Mathematics]
date:  2021-03-23
---

**March 23, 2021.** *Stuff*

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
Thankfully, we could just define the smallest boring number as the
element which minimises *absolute value*, i.e.

$$
b = \text{argmin}_{k\in B_\mathbb{Z}} |k|.
$$

This might actually give us two numbers, $\pm b$, so the negative one
is the smallest. So there are no boring integers.
What about boring rational numbers?
This is somewhat more elaborate, but if $B_\mathbb{Q}$ is the set of
boring rationals, we can define the "smallest" boring numbers as those

$$
b = \text{argmin}_{a/b\in B_\mathbb{Q}} (|a| + |b|)
$$

where $a/b$ is a fraction in lowest terms.
Once again, there may be multiple minimisers, but only a finite number
so we can choose the smallest.
We conclude there are no boring rationals.
This may suggest there are no boring real numbers.
We should be able to find some function with a finite number of
minima, and then choose the smallest, right?
I'm going to argue that *no such function exists*. Then I'm going to
explain why it might exist, depending on which axioms of set theory we
use.

#### Most real numbers are boring

"Boring" and "interesting" are of course subjective terms.
We'll use something a bit more well-defined, and replace
"interesting" with *describable*.
A number is describable if it has some finite description, using
words, mathematical symbols, maybe even a computer program, which
uniquely single out that number.
For instance, $\sqrt{2}$ is the positive solution of $x^2 = 2$, $\pi$
is the ratio of a circle's circumference to its diameter, and $e$ is
the limit

$$
e = \lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n.
$$

It turns out that *almost every* real number is indescribable, or
"boring", in our official translation of that term.
The argument is very simple.
