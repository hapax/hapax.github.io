---
Layout: post
mathjax: true
comments: true
title:  "A minimal introduction to minimal networks"
categories: [Mathematics, Teaching, Hacks]
date:  2020-02-010
---

**February 10, 2020.** **

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Triangles</a>
   1. <a href="#sec-2-1">Equilateral triangles</a>
   2. <a href="#sec-2-2">To $120^\circ$ and beyond</a>
   3. <a href="#sec-2-3">The Gilbert-Pollack conjecture*</a>
3. <a href="#sec-3">Graphs</a>
   1. <a href="#sec-3-1">Trees</a>
4. <a href="#sec-A">Fermat points*</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

Suppose we want to join up three towns ($A$, $B$ and $C$) by rail.
If I can use this railway to travel from one town to any
other, we say that rail network is *connected*.
Two simple examples of connected networks are shown below.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner1.png" width="80%"/>
		    <figcaption><i>Figure 1. Rail networks (triangle and
    trident) connecting three towns.</i></figcaption>
	</div>
	</figure>
	
Building railways is expensive, since we not only need to design and
build the rail itself, but acquire the land beneath it.
In contrast, stations are cheap: we just slap together some sidings, a
platform, and a bench or two, and we're done.
If we want to minimise cost, we should therefore make the total length
of the rail network as short as possible, adding extra stations if they
assist us in this goal.
The resulting layout is called the *minimal network* connecting $A$, $B$ and $C$.

We can consider the same problem for $n$ stations, and seek rail
networks of smallest total length.
Although finding the exact solution is difficult in
general, we can use simple reasoning to learn some important features
of the connectivity and layout of these minimal networks.

---

*Exercise 1 (triangle or trident).* In Figure 1, we have two networks connecting the same towns: a triangular network,
and a trident-shaped network with a hub station $D$ in the middle.
Which is shorter?
See if you can do better than either.

*Hint.* Measure lengths on the screen with a ruler. You may
 feel like you've turned into your grandparents, but it works!

---

## 2. Triangles <a id="sec-2" name="sec-2"></a>

The three-town problem is already surprising.
The simplest possibility is the triangular network, but it is not
minimal; to minimise length, a trident-shaped network with a new
station $D$ is optimal.
The best place to put the hub station is called the *Fermat point*, and if you are keen, you can learn how to
determine this point in the <a href="#sec-A">appendix</a>.
But for the rest of the post, we will only worry about *when* we
should build a hub, rather than *where* it goes exactly.
This will save us some hard trigonometry!
Our first and only exception will be an important special case: the
equilateral triangle.

## 2.1. Equilateral triangles <a id="sec-2-1" name="sec-2-1"></a>

So, imagine that the towns $A$, $B$ and $C$ are now equally spaced,
and sit on the corners of an equilateral triangle of side length $d$.
The triangular network has total length $L_\Delta = 3d$.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner2.png" width="80%"/>
		    <figcaption><i>Figure 2. Rail networks on an equilateral triangle.</i></figcaption>
	</div>
	</figure>

We might imagine that a trident network with a station in the middle
does better, but instead of checking with a ruler, let's do a little
trigonometry.

---

*Exercise 2 (equilateral trident).* Show that the length of the
trident network, with a hub in the centre of the triangle, is

$$
L_{\text{Y}} = \frac{3\sqrt{3}}{2}d.
$$

Since $3\sqrt{3}/2 \approx 2.6 < 3$, the trident is indeed shorter
than the triangle.

*Hint.* To determine the length of a trident leg, the gray triangle in
 Figure 2 is useful.

---

We are going to argue not only that the trident network is better than
the triangle network, but that the best place to put the hub station
$D$ is right in the centre, using a simple line of symmetry-based reasoning.
Let's place $D$ anywhere we like, but now draw one of the *axes of
symmetry* of the triangle, represented by the red line in Figure 3.
We are going to move the hub side to side in a normal direction to the
axis of symmetry, drawn as a dark blue line in Figure 3.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner3.png" width="40%"/>
		    <figcaption><i>Figure 3. Wiggling the hub around an axis
    of symmetry.</i></figcaption>
	</div>
	</figure>

As we wiggle the hub left or right of the axis, the total length of
the network (the lengths of the light blue legs) will change.
But symmetry places strong constraints on how it changes.
If we shift $D$ a distance $x$ to the left of the axis, this
should give exactly the length as shifting to the right by $x$, since
the triangle is left-right symmetric around the red line.
Thus, the function is *even*, with $L(x) = L(-x)$, where $x$ is the
shift away from the axis, with $x < 0$ to the left and $x > 0$ to the
right.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner4.png" width="35%"/>
		    <figcaption><i>Figure 4. Length as a function of wiggle
    $x$ away from the axis.</i></figcaption>
	</div>
	</figure>

In Figure 4, we have drawn two possibilities for an even length
function $L(x)$.
It can either be a *minimum* at the point of symmetry $x = 0$, or a
*maximum*. A function which is even around $x= 0$ has no other choice!
But it's clear from Figure 5 that if we make $x$ very large, the
length will get very large as well.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner5.png" width="60%"/>
		    <figcaption><i>Figure 5. The trident gets long for large $x$.</i></figcaption>
	</div>
	</figure>

This suggests that $L$ is a *minimum* and not a *maximum* at $x=
0$, so the top graph in Figure 4 is the correct one.
If it was a maximum, then length would get smaller at large $x$!

---

*Exercise 3 (global vs local).* Although this argument is plausible,
 it doesn't rule out the possibility that $x=0$ is actually a maximum,
 with the true minimum at $\pm x_\text{min}$, before length increases
 again as $|x|$ gets larger.
 If you are worried, you can check explicitly this doesn't happen!

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner6.png" width="40%"/>
		    <figcaption><i>Figure 4. Calculating the exact network length.</i></figcaption>
	</div>
	</figure>

<span style="padding-left: 20px; display:block">
(a) Show that, for the triangle in Figure 6, the length of the network is
</span>

$$
L(x) = L_1 + L_2 + L_3 = \sqrt{\left(\sqrt{3}d - h\right)^2 + x^2} +
\sqrt{h^2 + (d-x)^2} + \sqrt{h^2 + (d+x)^2}.
$$

<span style="padding-left: 20px; display:block">
*Note.* We are now dealing with a triangle of side length $2d$, since
it makes the algebra a bit neater.
</span>

<span style="padding-left: 20px; display:block">
(b) Choose $d=1$ for simplicity.
</span>

---

## 2.2. To $120^\circ$ and beyond <a id="sec-2-2" name="sec-2-2"></a> 

## 3. Graphs <a id="sec-3" name="sec-3"></a>

## 3.1. Trees <a id="sec-3-1" name="sec-3-1"></a>

## A. Fermat points* <a id="sec-A" name="sec-A"></a>

#### References

https://thatsmaths.com/2015/01/29/the-steiner-minimal-tree/
https://www8.cs.umu.se/kurser/TDBAfl/VT06/algorithms/BOOK/BOOK4/NODE181.HTM
https://en.wikipedia.org/wiki/Steiner_tree_problem
