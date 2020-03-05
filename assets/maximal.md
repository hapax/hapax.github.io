---
Layout: post
mathjax: true
comments: true
title:  "From twins to "
categories: [Physics, Teaching, Hacks]
date:  2020-03-??
---

**March ?, 2020.** *Stuff*

### Contents

1. <a href="#sec-1">Einstein and Pythagoras</a>
   1. <a href="#sec-1-1">The Joker</a>

## 1. Einstein and Pythagoras <a id="sec-1" name="sec-1"></a>

### 1.1. The Joker <a id="sec-1-1" name="sec-2-1"></a>

When you rotate a piece of wood, the length doesn't magically change,
right?
To check this, you can take a ruler and line it up along the wood.
As you rotate both ruler and wood together, you'll see the length
doesn't change.
But what if some Joker comes along and tells you that rotating not only
changes the wood, but the ruler too!
They will stretch by exactly the same factor, so you can never
actually tell from ruling if the length is changed.

How could you refute the joker's claim?
One option is to keep your ruler fixed in place, since if you don't
rotate it, you don't need to worry about length changing.
But now it's hard to measure things unless they line up with the ruler.
To get around this, you can devise a system with two identical rulers,
for convenience placed at right angles.
For a rotated piece of wood, you can take a measurement on each ruler
(see below) and call them $x$ and $y$.
Our goal is to cobble these together to get a length.

We can try lining the wood up with the first ruler.
This gives a measurement of $x = \ell$ and $y = 0$, which we write as
the pair

$$
(x, y) = (\ell, 0).
$$

Similarly, if we line the wood up with the second ruler, we will find that

$$
(x, y) = (0, \ell).
$$

Looks like length is the same! In both cases, it's $\ell$. But of
course it looks that way, the Joker says, laughing, because the second
ruler stretches just so in order to compensate for the change in
length of the wood.

Undeterred, you now place the wood halfway between the two rulers, and
get the measurements

$$
(x, y) = \left(\frac{1}{\sqrt{2}}\ell, \frac{1}{\sqrt{2}}\ell\right).
$$

This is a funny measurement, and after playing around with it for a
bit, you realise that these measurements are related to the apparent
length, $\ell$, by

$$
x^2 + y^2 = \frac{1}{2}\ell^2 + \frac{1}{2}\ell^2 = \ell^2.
$$

In fact, *any* way you choose to orient the ruler, you find that this
relation $x^2 + y^2 = \ell^2$ is true!
Congratulations, you've just discovered Pythagoras' theorem.
But what does it mean?
