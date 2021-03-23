---
Layout: post
mathjax: true
comments: true
title:  "Most numbers are indescribably boring"
categories: [Mathematics]
date:  2021-03-23
---

**March 23, 2021.** *Stuff*

#### Introduction

It is a
[running joke](https://en.wikipedia.org/wiki/Interesting_number_paradox)
among mathematicians that there are no boring numbers. Here's the proof. Let $B$ be the set of boring numbers. Define $b = \min B$ as
the smallest boring number. But this is a highly unusual property, so $b$ is
interesting after all!
Joke it may be, but there is a sting in the tail.
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
Does this cause a problem? Not really. We can just define the smallest
boring number as the smallest element minimising the *absolute value*, i.e.

$$
b = \min \text{argmin}_{k\in B_\mathbb{Z}} |k|.
$$

(The $\text{argmin}$ might actually give us two numbers, $\pm b$, so the negative one
is the smallest.) Thus, there are no boring integers.
What about boring rational numbers?
This is somewhat more elaborate, but if $B_\mathbb{Q}$ is the set of
boring rationals, we can define the "smallest" boring numbers as

$$
b = \min \text{argmin}_{a/b\in B_\mathbb{Q}} (|a| + |b|),
$$

where $a/b$ is a fraction in lowest terms.
Once again, there may be multiple minimisers of $|a| + |b|$, but only
a finite number, so we can choose the smallest.
We conclude there are no boring rationals.
This may suggest there are no boring real numbers.
We should be able to find some function with a finite number of
minima, and then choose the smallest, right?
I'm going to argue that no such function can be explicitly
described. Then I'm going to explain why it might still exist,
depending on which axioms of set theory we use.

#### A modest infinity

<!-- https://en.wikipedia.org/wiki/Definable_real_number -->

"Boring" and "interesting" are subjective terms.
We'll use something a tad more well-defined, and replace
"interesting" with *describable*.
A number is describable if it has some finite description, using
words, mathematical symbols, maybe even a computer program, which
uniquely singles out that number.
For instance, $\sqrt{2}$ is the positive solution of $x^2 = 2$, $\pi$
is the ratio of a circle's circumference to its diameter, and $e$ is
the limit

$$
e = \lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n.
$$

It turns out that *almost every* real number is indescribable, or
"boring", in our official translation of that term.
The argument is very simple, and proceeds by simply counting the
number of finite descriptions.
Each such description consists of a finite sequence of symbols
(letters, mathematical squiggles, algorithmic instructions), each of
which could be elements of some very large alphabet of symbols.
For instance, the text

$$
\sqrt{2} \text{ is the positive solution of $x^2 = 2$.}
$$

can be converted into (decimal) unicode as

```
8730 50 32 105 115 32 116 104 101 32 112 111 115 105 116 105 118 101
32 115 111 108 117 116 105 111 110 32 111 102 32 120 94 50 61 50 46
```

Imagine some "super unicode" which converts any symbol into a number.
The super unicode (sunicode) alphabet may be arbitrarily large, so large, in
fact, that it may as well *consist of every natural number*
$\mathbb{N}$.
Then a finite description in sunicode is just a finite sequence
of natural numbers.
So we have to count these!
There is a nice scheme for showing that these are in one-to-one
correspondence with the natural numbers themselves, and hence
*countably infinite*.
We take a sequence, say

$$
(6, 2, 0, 5)
$$

and convert the first bracket and all commas into $1$s, and each number into
the corresponding number of $0$s:

$$
10000001001100000_2.
$$

In turn, this can be converted to decimal, $66144$.
Going in the other direction, any whole number can be written in
binary and then converted into sequence:

$$
14265092 = 110110011010101100000100_2
$$

becomes $(0,1,0,2,0,1,1,1,0,5,2)$.
Thus, we have a simple, explicit correspondence between finite
sequences of natural numbers and the natural numbers!
<!-- We will call this "sunicoding" for "super unicode encoding".-->
This basically completes the proof, for the simple reason that there
are *infinitely more* real numbers than there are natural numbers.
This is established by Cantor's beautiful
[diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument),
which I won't repeat here.
The point is that finite descriptions can only capture an
infinitesimally small fragment of all real numbers.

#### Unwritten laws

<!-- https://en.wikipedia.org/wiki/Berry_paradox -->

I've just argued that the set of boring, i.e. indescribable, real
numbers $B_\mathbb{R}$, includes almost every real number (though
quite definitely *not* every real number you can think of).
But armed with the previous examples, it's tempting to think
that we can simply waltz in and pluck out the smallest element of
$B_\mathbb{R}$.
Of course, that won't quite work, because the set need not be bounded
below, so instead, suppose there is some explicit function $f$ such
the $b \in B_\mathbb{R}$ is the smallest minimizer of $f$, i.e.

$$
b = \min \text{argmin}_{x \in B_\mathbb{R}} f(x).
$$

If I knew $f$ explicitly, I could convert the last few paragraphs into
sunicode, and we'd have a description of $b$ after all. Contradiction!
But the contradiction here does not mean that $B_\mathbb{R}$ is
non-empty. After all, most of $\mathbb{R}$ is indescribable for
set-theoretic reasons.
Instead, it means that there *cannot be any explicit function*
$f$. More generally, there cannot be any explicit rule which, given a
subset of $\mathbb{R}$, explicitly gives some unique number. If there
was, we could apply it to $B_\mathbb{R}$ and get the same contradiction.

<!-- But that does not mean there is no such functon; rather, the law must
remain unwritten.
This is similar to
[Berry's paradox](https://en.wikipedia.org/wiki/Berry_paradox), which
asks us to consider the phrase
<span style="padding-left: 20px; display:block">
The smallest positive integer not definable in under sixty letters.
</span>
-->
