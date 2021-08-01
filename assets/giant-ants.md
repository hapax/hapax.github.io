---
Layout: post
mathjax: true
comments: true
title:  "Giant ants from outer space"
categories: [Physics, maths, hacks]
date:  2021-07-31
---

If aliens ever visit the earth, might they take the particularly
schlocky form of giant ants?
Should we be worried about the ape king of Skull Island clambering up
the Empire State Building, Hollywood starlet in one hand and a military
helicopter in the other?
And can we look forward to the exciting prospect of enormous radioactive
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
scaled up to a ridiculous size, and when you scale a normal animal up
to a ridiculous size, it simply collapses under its own weight.
We don't need to worry about getting invaded by giant ants from outer
space, or having our landmark buildings ruined by oversized
primates. It's not going to happen.

To see why a giant ant or lizard or gorilla collapses under its own
weight when you make it big enough, we'll need to understand the maths
and physics of *scaling*, in other words, how things change with size.
And in fact, we're going to do a lot more than simply rule out the
existence of giant monsters.
We'll turn our understanding of scaling into a *predictive tool*,
something you can use to learn positive facts about the
world, and not just negative, sort of boring facts, like "King Kong
vs. Godzilla is physically implausible". I mean, we already
knew that.
Instead, we can do cool things like estimate the weight of the largest
tree in the world.

<figure>
    <div style="text-align:center"><img src
    ="/images/giant-ant-pics/kong-godzilla.jpeg" width="450px"/>
	</div>
	</figure>

But here's the really cool thing. If we want to explain something as
simple as a heartbeat, or the diet of a chipmunk, we'll actually be
led to the startling conclusion that animals are *biological fractals*: they are
built out of structures that look the same when you zoom in.
Maintaining a living organism comprises a bunch of interesting design problems,
and nature evolved fractals in order to solve them. This is pretty damn cool.

### No giant ants

To start with, let's imagine a strange organism which looks like a cube.
The *scale* of this cube-shaped creature is anything we can
conveniently measure with a ruler, say the side length, which I'll call $L$.
To *change the scale* of the cube (to "scale up" or "scale down") means to change the side length but
keep the shape and proportions fixed; the cube remains a cube.

Different properties of the cube will vary in different ways as we
vary the size.
For instance, the volume of the cube is the product of the length, the width and
the height, just like any box. But since length, width and height are
all equal for a cube, the volume is just

$$
L \times L \times L = L^3.
$$

Suppose we scale up the cube by a factor of two, in other words,
we double the side length. Then the volume increases, not
by a factor of $2$, but by three factors of two, one for each factor
of $L$. So the volume increases by an overall factor of $2 \times 2
\times 2 =8$:

$$
L \times L \times L \to 2L \times 2L\times 2L = (2 \times 2 \times 2)L^3 = 8 L^3.
$$

In general, if we scale up or down some factor $f$, the volume will change
by that factor cubed,

$$
f \times f \times f = f^3.
$$
