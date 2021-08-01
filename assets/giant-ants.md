---
Layout: post
mathjax: true
comments: true
title:  "From giant ants to biological fractals"
categories: [Physics, maths, hacks]
date:  2021-07-31
---

If aliens ever visit the earth, might they take the particularly
schlocky form of giant ants? Or could radioactive waste create
[*kaiju*](https://en.wikipedia.org/wiki/Kaiju) like Godzilla and
Mothra, duking it out in the Japanese sea while the puny humans watch
on in terror?
And might the king of Skull Island one day clamber up the Empire State
Building, Ann Dwarrow in one hand and a military helicopter in the other?

<figure>
    <div style="text-align:center"><img src
    ="/images/giant-ant-pics/giant-ant.png" width="450px"/>
	</div>
	</figure>

For better or worse (depending on how you feel about giant ants) the
answer is no.
All of these creatures are essentially normal terrestrial organisms,
scaled up to ridiculous sizes, and when we scale things up to
ridiculous sizes, they simply collapse under their own weight.
So if giant ants from outer space invade earth, we can just sit back
and relax as they struggle unsuccesffuly to prop themselves up in the
earth's gravity.

To see why the giant ants or lizards or gorillas collapse under their
own weight, we'll need to understand the maths and physics of
*scaling*, in other words, how things change with size.
But we're going to do much more than simply rule out the existence of
giant ants.
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
simple as a heartbeat, or the diet of a chipmunk, we'll be
led to the startling hypothesis that animals are *biological fractals*: they are
built out of structures which look the same when you zoom in.
Running an organism involves a bunch of interesting design problems,
and nature evolved fractals in order to solve them. Pretty damn cool.

### No giant ants

To start with, let's imagine a strange organism which looks like a cube.
The *scale* of this cube-shaped creature is something we can
conveniently measure with a ruler, say the side length.
To *change the scale* of the cube (we also say "to scale up" or "to
scale down") means to change the side length but
keep the shape and proportions fixed; the cube remains a cube.
Different properties of the cube will change in different ways as we
scale up and down.
Let's call the side length $L$.
The volume of the cube $V$ is the product of the length, the width and
the height, just like any box, but since length, width and height are
equal for a cube, the volume is just

$$
V = L \times L \times L = L^3.
$$

Suppose we scale up the cube by a factor of two, or in other words,
double the side length, $L \to 2L$. Then the volume increases, not
by a factor of $2$, but by three factors of two or $2^3 = 8$, one for
each factor of $L$:

$$
V \to 2L \times 2L\times 2L = 8 L^3 = 8V.
$$
