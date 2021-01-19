---
Layout: post
mathjax: true
comments: true
title:  "Deterministic dice"
categories: [Mathematics, Physics, Statistics]
date:  2021-01-19
---

**January 19, 2021.** *Why are dice and coins good sources of
  randomness? Symmetry is not enough to explain why starting with the
  same initial conditions still seems to lead to randomness. I explore
  the relevant forces (chaos and jitter) in simple examples, and build
  deterministic dice from scratch.*

#### Introduction

Each time I roll a dice, my muscles try to do the same thing. But even
if I hold the dice the same way, and throw in what feels like the same
way, I seem to get any side of the dice with equal probability.
If you ask why a mathematician why any side appears with the same
odds, they might say *symmetry*. Apart from the pips indicating the
value [<sup><a id="fnr.1" name="fnr.1" class="footref" href="#fn.1">1</a></sup>], the sides are indistinguishable and therefore must have equal
probability of landing right side up.
This is true and sounds like a nice explanation.
But it's only half the story!

To see why, suppose I take a very large dice, so heavy that I can only
drop it.
In this case, it's unlikely to roll, and whatever side happens to be
facing up when I "roll" will be facing up when it stops [<sup><a id="fnr.2" name="fnr.2" class="footref" href="#fn.2">2</a></sup>].
If I pick this face randomly, I will get a random outcome, but the
point of the dice is to outsource the randomness!
Symmetry is important, as we will see, but dice is fundamentally a roll-playing game.

#### Chaotic coins

To illustrate our ideas, we'll use the even simpler example of
flipping a coin.
Once again, ignoring the small effect of markings, the coin has a
symmetry between the two sides, heads and tails.
And similarly, if I have a very large coin I can only drop, then I
will need to randomly choose the initial conditions for tossing if I
want the coin flip to be random.
This defeats the purpose of the coin!
So, how does a deterministic process like throwing a coin generate an
*effectively random* and *equiprobably* outcome?
There are two main ingredients, as I see it: *chaos* and *jitter*.
We'll focus on chaos first.

Chaos

---

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum"
href="#fnr.1">Footnote 1</a></sup> <p class="footpara">
The pips do create a bias unless they are drilled, then filled with
black paint of the same density as the dice material. This is standard
procedure for "precision" dice used at casinos or by professional gamblers.
</p></div>

<div class="footdef"><sup><a id="fn.2" name="fn.2" class="footnum"
href="#fnr.2">Footnote 2</a></sup> <p class="footpara">
In physics parlance, the choice of initial condition—the way you
hold the dice—"spontaneously breaks" the symmetry of the dice
itself. This is the fancy way of saying that symmetry of the dice
isn't enough to explain the symmetry of the outcomes.
</p></div>
