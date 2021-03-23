---
Layout: post
mathjax: true
comments: true
title:  "Indescribably boring numbers"
categories: [Mathematics]
date:  2021-03-23
---

**March 23, 2021.** *Stuff*

#### Introduction

It is a
[running joke](https://en.wikipedia.org/wiki/Interesting_number_paradox)
among mathematicians that there are no boring numbers. Here's the
proof. Let $B$ be the set of boring numbers, and suppose for a
contradiction it is non-empty. Define $b = \min B$ as
the smallest boring number. Since this is a highly unusual property, $b$ is
interesting after all!
Joke it may be, but there is a sting in the tail. By thinking
about how the joke works, we will be led to some rather deep (and
perhaps disturbing) insights into set theory and what it can and
cannot tell us about the mathematical world.

#### Integers and rationals are interesting

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

#### Most real numbers are boring

<!-- https://en.wikipedia.org/wiki/Definable_real_number -->

"Boring" and "interesting" are subjective.
We'll use something a tad more well-defined, and replace
"interesting" with *describable*.
A number is describable if it has some finite description, using
words, mathematical symbols, even a computer program, which uniquely singles out that number.
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

Imagine some "super unicode" which lets us converts *any* symbol
into a number.
The super unicode alphabet may be arbitrarily large, so we will take it to
consist of *every* natural number $\mathbb{N}$.
Then a finite description any symbols can be written as a sequence of
the corresponding natural numbers, a trick I will call "unicoding".
To find the number of finite descriptions, we just count the sequences!
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
sequences of natural numbers and the natural numbers themselves.
This basically completes the proof, for the simple reason that there
are *infinitely more* real numbers than there are natural numbers.
This is established by Cantor's beautiful
[diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument),
which I won't repeat here.
The point is that we see, via unicoding and then the binary
correspondence, that finite descriptions only capture an
infinitesimally small fragment of the real numbers.
They literally cannot be talked about.

<!-- https://en.wikipedia.org/wiki/Berry_paradox -->

So, we conclude that most real numbers boring, i.e. indescribable.
The set $B_\mathbb{R}$ includes almost every real number, though
quite definitely *not* every real number you can think of.
But, armed with our previous jokes, it's tempting to think that we can
simply waltz in and make the same joke about $\mathbb{R}$, simply
plucking out the smallest element of $B_\mathbb{R}$.
Of course, that won't quite work, because the set need not be bounded
below. So instead, suppose there is some explicit function $f$ such
the $b \in B_\mathbb{R}$ is the smallest minimizer of $f$, i.e.

$$
b = \min \text{argmin}_{x \in B_\mathbb{R}} f(x).
$$

If I knew $f$ explicitly, we'd have a description of $b$ after all. Contradiction!
But the contradiction here does not mean that $B_\mathbb{R}$ is
non-empty. After all, most of $\mathbb{R}$ is indescribable for
the set-theoretic reasons given above.
Instead, it means that there *cannot be any explicit function*
$f$. More generally, there cannot be any explicit rule which, given a
subset of $\mathbb{R}$, explicitly gives some unique number. If there
was, we could apply it to $B_\mathbb{R}$ and get the same
contradiction.

#### A philosophical aside

But there's a weird loophole here. Our argument doesn't establish that
$f$ doesn't exist, just that it *can't be finitely described*. And
although it might seem weird to trust in the existence of something
that we can't really talk about, we do just this with the real
numbers!
I belive that all the real numbers exists, even though only a tiny
fraction will ever be singled out by mathematical activity.
Is this reasonable?
It depends who you ask.
There is a philosophy of mathematics called
[intuitionism](https://plato.stanford.edu/entries/intuitionism/) which
tells us that mathematics is a human invention, and therefore enjoins
us to only reason about the things we can construct ourselves. No
indescribable real numbers if you please!
I'm not sure about this "mathematical creationism", and think there
are more things in the mathematical heavens than are dreamt of in
finite human descriptions.
Why should human limitations be mathematical ones?

That said, it's not the case that anything goes. We should have some
firm basis for believing in the existence of those things we can't
discuss, and for the real numbers, the firm basis is drawing a
continuous line on a piece of paper, or thinking about infinite
decimal expansions. These are *models* of the real numbers,
concrete-ish objects which capture enough of the abstract entity
$\mathbb{R}$ to convince us that nothing magical stops us from drawing
certain points on the line, or continuing certain expansions.
Similarly, the indescribable things we would like to exist and reason
about might *depend on our models of set theory itself*.

<!-- You may wonder if the contradiction here is coming from ambiguity in
the notion of "explicit describability".
That this can cause deep problems is illustrated by the
[Berry paradox](https://en.wikipedia.org/wiki/Berry_paradox), which
asks us to consider the following:
<span style="padding-left: 20px; display:block">
The smallest positive integer not definable in under sixty letters.
</span>
If $B_{60}$ is the set of positive integers not definable in under
sixty letters, it seems we have just defined its smallest elements in
fifty seven! This too is a contradiction. Many people try to resolve
this by arguing that it does not constitute a "definition"; I think it
is much simpler to following the boring number argument, and conclude
that $B_{60}$ doesn't exist. -->
