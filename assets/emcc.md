---
Layout: post
mathjax: true
comments: true
title:  "Why does E = mc²?"
categories: [Physics, Hacks]
date:  2021-02-13
---

**February 13, 2021.** *A*

#### A Pythagorean prelude

Relativity is really just the bizarro version of trigonometry.
To make this clear, we start by presenting Pythagoras' theorem in a
slightly odd way.
Suppose we have rulers, $x$ and $y$, oriented at right angles
[<sup><a id="fnr.1" name="fnr.1" class="footref" href="#fn.1">1</a></sup>],
and which both have evenly spaced marks.
An $x$ division need not equal a $y$ division, and in general will
correspond to $\Lambda$ units of $y$.
We can measure lengths, say of a plank of wood, in this system, by
simply recording the number of marks it takes up on ruler $x$, call it
$\Delta x$, and the number of marks taken up on $y$, called $\Delta
y$.
Then however we choose to orient the plank of wood, we find that

$$
\Delta x^2 + \Lambda^2 \Delta y^2 = L^2,
$$

for some number $L$.
Since it doesn't change with orientation, it seems reasonable to define
$L$ as the length of the wood.

Relativity is almost exactly the same.
Michelson and Morley's
[famous experiment](https://en.wikipedia.org/wiki/Michelson%E2%80%93Morley_experiment)
in 1887 suggested that the speed of light does not depend on how you
go when you measure it.
Einstein arrived at the same conclusion by thinking long and hard
about electrodynamics.
To measure the speed of light, we use two rulers, $x$ and $t$, though
the latter ruler is usually called a "clock".

---

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum"
href="#fnr.1">Footnote 1</a></sup> <p class="footpara">
Or if you prefer, a grid of such rulers.
</p></div>


Recall Pythagoras's theorem: if you have a right-angled triangle with
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
