---
Layout: post
mathjax: true
comments: true
title:  "Indescribably boring numbers"
categories: [Mathematics]
date:  2021-03-23
---

**March 23, 2021.** *We turn the old joke about boring numbers into a
  proof that while most real numbers are indescribably boring, all are
  relatively interesting assuming the axiom of choice.*

#### Introduction

It's a
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

The joke implicitly uses the fact that "numbers" refers to "positive
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

can be converted into [(decimal) unicode](http://www.tamasoft.co.jp/en/general-info/unicode-decimal.html) as

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
But the contradiction here does not imply $B_\mathbb{R}$ is
non-empty. After all, most of $\mathbb{R}$ is indescribable for
simple set-theoretic reasons.
Instead, it means that there *cannot be any explicit function*
$f$. More generally, there cannot be any explicit rule which, given a
subset of $\mathbb{R}$, explicitly gives some unique number. If there
was, we could apply it to $B_\mathbb{R}$ and get the same
contradiction.

#### An existential aside

But there's a weird loophole here. Our argument doesn't establish that
$f$ doesn't exist, just that it has no *finite, explicit description*. And
although it might seem weird to trust in the existence of something
that we can't really talk about, we do just this with the real
numbers!
I believe in all the real numbers, even the ones I can never describe.
Is this reasonable?
It depends who you ask.
There is a philosophy of mathematics called
[intuitionism](https://plato.stanford.edu/entries/intuitionism/) which
tells us that mathematics is a human invention, and therefore enjoins
us to only reason about the things we can construct ourselves. No
indescribable real numbers if you please!

I'm not sure about this "mathematical creationism", and think there
are more things in the mathematical heavens than are dreamt of in
our finite human philosophy.
Why should human limitations be mathematical ones?
That said, it's not the case that anything goes. We should have some
firm basis for believing in the existence of those things we can't
discuss, and for the real numbers, the firm basis is drawing a
continuous line on a piece of paper, or thinking about infinite
decimal expansions. These are *models* of the real numbers,
concrete-ish objects which capture the essence of the abstract entity
$\mathbb{R}$. They convince us (or at least me) that there is nothing
magical stopping someone from drawing certain points on the line, or
continuing certain expansions forever.

Similarly, the indescribable things we would like to exist and reason
about in set theory might depend on our *models* of set theory!
I won't get into the specifics, but an important point is there are
*many different models* of set theory, with different properties, and
it seeks unlikely that any one model is right.
These properties are abstracted into *axioms*, formal rules about what
exists and what you can or can't do with sets.
Because models of set theory are deep, highly technical constructions,
most of the time we go the other way round, and play around with
axioms instead. Only later do we go away and find models which support
certain sorts of behaviour.
The point of all this is to make it a bit less counterintuitive when I
say that the existence and properties of boring numbers depend on which axioms
we decide to use.

#### All real numbers are relatively interesting

So, let's return to our problem of boring real numbers.
We argued there was no explicit, finitely describable rule for picking
an element out of $B_\mathbb{R}$.
But we can always make the *existence* of such a rule an axiom!
There are two ways to go about doing this.
Note that in first example of boring natural numbers, we use the
*minimum* of the set.
We had to be a bit more clever with the integers and rationals, but it
essentially boiled down to creating a special sort of *ordering* on
the set, so that any subset (including the boring numbers) has a
*smallest element*.
We wrote this is in a complicated way as

$$
b = \min \text{argmin}_{x \in B} f(x)
$$

for some function $f$, but we could just as well write

$$
b = \min_{\mathcal{W}} B,
$$

where $\mathcal{W}$ denote this ordering on the big set.
To be clear, for the integers it is

$$
0, -1, 1, -2, 2, -3, 3, \ldots
$$

and for the rationals it is

$$
0, -\frac{1}{1}, \frac{1}{1}, -\frac{2}{1}, -\frac{1}{2}, \frac{1}{2},
\frac{2}{1}, \ldots.
$$

This is called a *well-ordering*. Although it may not be describable,
we could simply require, as an axiom of set theory, that any set can
be well-ordered! More explicitly,

<span style="padding-left: 20px; display:block">
Any set $A$ has a well-ordering $\mathcal{W}_A$ such that any subset
of $A$ has a unique minimum element with respect to $\mathcal{W}_A$.
</span>

Although it doesn't spoil our conclusion that most real numbers are
boring, such an axiom would allow us to turn the old joke into an
argument that all real numbers are *relatively interesting*, where
"relatively interesting" means that there is a finite description
where we are allowed to use the well-ordering $\mathcal{W}$.
The proof goes as you might expect: let $B^{\mathcal{W}}_\mathbb{R}$ be the set of relatively boring
numbers, i.e. numbers with no finite explicit description, even when
allowed to use the well-ordering $\mathcal{W}$.
Since $\mathcal{W}$ is a well-ordering, we can define

$$
b = \min_{\mathcal{W}} B^{\mathcal{W}}_\mathbb{R}.
$$

End of proof!
So, although most real numbers are strictly boring, with a
well-ordering all of them are relatively interesting.

#### Choosing an order

Well-ordering is not usually treated as an axiom.
Historically, set theorists prefer to use a simpler rule called the
*axiom of choice*, which is logically equivalent, as we will loosely
show in a moment, but somehow less suspect.
As Jerry Bona joked,

<span style="padding-left: 20px; display:block">
The axiom of choice is obviously true and the well-ordering principle
obviously false.
</span>

(Actually, Bona's joke mentions a third equivalent form called *Zorn's
lemma*, but it would confuse matters too much to explain.)
Loosely, the axiom of choice just says we can pick an element from a
non-empty set:

<span style="padding-left: 20px; display:block">
Given a nonempty set $A$, we can choose an element $f \in A$.
</span>

Pretty reasonable huh? If a set is nonempty, it has an element, so
we can pluck one out.
In fact, it's usually stated in terms of a *family* of sets $A_i$,
where the subscript $i$ ranges over some indexing set $I$:

<span style="padding-left: 20px; display:block">
Given a family of nonempty set $A_i$, $i \in I$, we can collect a
representative from each set, labelled $f_i \in A_i$.
</span>

The well-ordering principle implies the axiom of choice, since I can
just take the union of all the sets $A_i$, well-order it with
$\mathcal{W}$, and then define $f_i = \min_{\mathcal{W}} A_i$.
That's my set of representatives!
The other way round is conceptually straightforward.
To well-order a set $A = A_0$, start by choosing an element $f_0 \in
A_0$ by the axiom of choice. Then remove it to define a new set $A_1 =
A_0 - \{f_0\}$, and select another element $f_1 \in A_1$. Continue in
this way, at each stage simply deleting the element from the previous
stage and choosing a new one, using

$$
A_{n+1} = A_n - \{f_n\} = A_{n-1} - \{f_n, f_{n-1}\} = \cdots = A_0 -
\{f_i : i < n\}
$$

as long as the set is nonempty.
The well-ordering is simply the elements in the order we made the
choice:

$$
\mathcal{W}_A = \{f_0, f_1, f_2, \ldots \} = \{f_n \in A_n : A_n \neq \varnothing\}.
$$

There are two issues with this construction.
The first is that it might feel sketchy to use the axiom of
choice "as we go" to build the sets, rather than starting with a
pre-defined family. But no one said this wasn't allowed!
Second, our method only seems to work for sets as most as large as the
natural numbers, since we indexed elements with $n \in \mathbb{N}$.
But we can extend it to an *arbitrary* set using a generalisation of
natural numbers called
[ordinals](https://en.wikipedia.org/wiki/Ordinal_number).
We loosely sketch how this is done in the appendix.
Once the dust settles, we learn that the axiom of choice is equivalent
to well-ordering, and thus implies that every real number is
relatively interesting.
In fact, the same argument shows us that *any object that can live in
a set* is relatively interesting!

#### Conclusion

I'll end with a puzzle.
Consider the phrase

<span style="padding-left: 20px; display:block">
The smallest real number with no finite, explicit description.
</span>

If "smallest" refers to an explicitly definable well-ordering of the
reals, then this would seem to pick out a unique number with a finite,
explicit description. Contradiction!
We used this to argue no explicit well-ordering exists.
But let's compare this to the
[Berry paradox](https://en.wikipedia.org/wiki/Berry_paradox), which
asks us to consider the phrase

<span style="padding-left: 20px; display:block">
The smallest positive integer not definable in under sixty letters.
</span>

This phrase clocks in under sixty letters, and would seem to define a
number.
Contradiction!
The original joke about boring numbers really has the same form.
We 

#### Acknowledgments

As usual, thanks to J.A. for stimulating questions, and also
suggesting a form of unicoding.

#### Appendix: ordinals and the axiom of choice

Ordinals are *sets* which we use to stand in for numbers.
The smallest ordinal is $0$, which is defined as the empty set
$\varnothing = \{\}$.
Each ordinal $\alpha$ has a unique successor $\alpha + 1$, defined by
simply appending a copy of $\alpha$ to itself:

$$
\alpha + 1 = \{\alpha, \{\alpha\}\},
$$

To illustrate, we apply the successor operation to $0 = \varnothing$ a
few times:

$$
1 = 1 + 0 = \{0\}, \quad 2 = 1 + 1 = \{0,
1\}, \quad 3 = 2 + 1 = \{0, 1, 2\}.
$$

Going on in this way gives us all the finite ordinals, but there are
also *infinite* ordinals. The smallest infinite ordinal, conventionally
denoted $\omega$, can be identified with the natural numbers:

$$
\omega = \{0, 1, 2, 3, 4, \ldots\}.
$$

It is called a *limit* ordinal since it is not the successor of any
finite ordinal. It is bigger than all the finite ones, $n <
\omega$. The successor is defined as before,

$$
\omega + 1 = \{\omega, \{\omega\}\},
$$

thereby giving a precise meaning to "infinity plus one"!
We won't say more about the structure of these ordinals. The main
point is that we can always "count" the elements in a set $A$ using
ordinals, no matter how big it is!
Let's now return to the problem of proving the axiom of choice
implies that any set $A$ can be well-ordered.
The basic idea is to start with $0$, but keep on counting up "past
infinity", defining

$$
A_{\alpha+1} = A_0 - \{f_\beta : \beta < \alpha\}
$$

for any ordinals $\alpha$ and $\beta$. The resulting set of
representatives is labelled by ordinals up to the ordinal of the set
$A$,

$$
\mathcal{W}_A = \{f_\alpha \in A_\alpha: A_\alpha \neq
\varnothing\},
$$

with $f_\alpha < f_\beta$ just in case the ordinals $\alpha < \beta$.
This is a well-ordering since the cardinals are themselves
well-ordered.
Now, we've skipped many important technical details, but the main
point was that the argument looks the same as the finite case, but we
replace finite counting numbers with potentially infinite ones!

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
