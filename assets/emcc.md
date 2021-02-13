---
Layout: post
mathjax: true
comments: true
title:  "Surveying special relativity"
categories: [Physics, Hacks, Faves]
date:  2021-02-13
---

**February 13, 2021.** *A*

#### Introduction

#### Pythagoras for mismtached rulers

Pythagoras's theorem states that if we have a right triangle with
short sides $a$, $b$ and long side (hypotenuse) $c$, they obey

$$
a^2 + b^2 = c^2.
$$

This is a mathematical theorem proved by Pythagoras or one of his
followers.
But the result was known much earlier, for instance by Babylonian surveyors.
It's possible they thought of it as a mathematical result, but in many
ways, our ideas of what constitutes theorem and proof was invented by
the Greeks.
More likely, the surveyors regarded this as a useful
*empirical* fact about distance.

We're going to give a fanciful interpretation of this.
Suppose a surveyor has two perpendicular rulers, call them $X$ and
$Y$, with evenly spaced marks on each.
The spacing on $X$ need not equal the spacing on $Y$, a fact which
will actually be crucial.
Now, suppose we have a length of wood we want to measure.
First, we line up it up along the $X$ ruler and find the wood takes up
$\Delta x = L$ marks.
Then we line it up along the $Y$ ruler and obtain $\Delta y = L'$
marks.
It seems like each $y$ unit corresponds to $\Lambda$ units of $x$, where

$$
\Lambda = \frac{L'}{L}.
$$

If we any other arrangement of the wood, we'll find that the number of
marks always obeys

$$
\Delta x^2 + \Lambda^2 \Delta y^2 = L^2. \tag{1} \label{pythag}
$$

It seems reasonable to *define* the length of the wood as $L$.
The formula (\ref{pythag}) gives a rule for calculating it.

#### Rotations

This rule does not merely give us a definition for length, however.
It also gives us some hints about how to transform $x$ values into $y$
values generally.
We noted already that we can directly 
