---
Layout: post
mathjax: true
comments: true
title:  "From giant ants to biological fractals"
categories: [Physics, maths, hacks]
date:  2021-07-31
---

If aliens ever visit the earth, might they take the particularly
schlocky form of giant ants?
Should we be worried about the ape king of Skull Island clambering up
the Empire State Buidling, Ann Dwarrow in one hand and a military
helicopter in the other?
Can we look forward to radioactive
[*monsters*](https://en.wikipedia.org/wiki/Kaiju) like Godzilla and
Mothra duking it out in the Japanese sea?

<figure>
    <div style="text-align:center"><img src
    ="/images/giant-ant-pics/giant-ant.png" width="450px"/>
	</div>
	</figure>

For better or worse (depending on how you feel about giant monsters)
the answer is no.
All of these creatures are essentially normal terrestrial animals
scaled up to ridiculous sizes, and when you scale a normal animal up
to ridiculous sizes, it will collapse under their own weight.

But to see why a giant ant or lizard or gorilla collapses under its
own own weight when you make it big enough, we'll need to understand
the maths and physics of *scaling*, in other words, how things change
with size.
And in fact, we're going to do a lot more than simply rule out the
existence of giant ants.
We'll turn our understanding of scaling into a *predictive tool*,
something you can use to learn positive facts about the
world, and not just negative, sort of boring facts, like "King Kong
vs. Godzilla is physically implausible". I mean, we already
knew that.
Instead, we can do cool things like estimate the walking speed of a
spider, or the weight of the largest tree in the world.

<figure>
    <div style="text-align:center"><img src
    ="/images/giant-ant-pics/kong-godzilla.jpeg" width="450px"/>
	</div>
	</figure>

But here's the really cool thing. If we want to explain something as
simple as a heartbeat, or the diet of a chipmunk, we'll actually be
led to the startling conclusion that animals are *biological fractals*: they are
built out of structures which look the same when you zoom in.
Running an organism involves a bunch of interesting design problems,
and nature evolved fractals in order to solve them. This is pretty damn cool.

### No giant ants

To start with, let's imagine a strange organism which looks like a cube.
The *scale* of this cube-shaped creature is something we can
conveniently measure with a ruler, say the length length $L$.
To *change the scale* of the cube (to "scale up" or "scale down") means to change the side length but
keep the shape and proportions fixed; the cube remains a cube but its
size change.

Different properties of the cube will change in different ways as we
changes its size.
For instance, the volume of the cube $V$ is the product of the length, the width and
the height, just like any box, and since length, width and height all
equal the side length $L$ of the cube, the volume is just

$$
L \times L \times L = L^3.
$$

Suppose we scale up the cube by a factor of two, in other words,
we double the side length. Then the volume increases, not
by a factor of $2$, but by three factors of two, one for each factor
of $L$:

$$
L \times L \times L \to 2L \times 2L\times 2L = 8 L^3.
$$

In general, if we scale up or down some factor, the volume will change
by that factor cubed, i.e., multiplied three times. In math, if
$L \to f L$ for a factor $f$, then the volume becomes

$$
fL \times fL \times fL = f^3 L^3.
$$
