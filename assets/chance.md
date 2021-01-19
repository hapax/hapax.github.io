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
But it's actually irrelevant!

To see why, suppose I take a very large dice, so heavy that I can only
drop it.
In this case, it's unlikely to roll, and will most likely just land on
the side that I drop it [<sup><a id="fnr.2" name="fnr.2" class="footref" href="#fn.2">2</a></sup>].
Now, if I pick which side I want to drop it on randomly, then I will
get a random outcome, but the point of the dice is to outsource
randomness!
The symmetry is important, but dice is fundamentally a roll-playing game.

#### Chaos

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
hold the dice—*spontaneously breaks* the symmetry of the dice
itself. This is the fancy way of saying that symmetry of the dice
isn't enough to explain the symmetry of the outcomes.
</p></div>
