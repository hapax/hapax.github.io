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
   2. <a href="#sec-2-2">Deforming the equilateral</a>
   3. <a href="#sec-2-2">To $120^\circ$ and beyond</a>
3. <a href="#sec-3">Graphs</a>
   1. <a href="#sec-3-1">Trees</a>
4. <a href="#sec-A">Fermat points</a>

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
The triangular network has total length $L_\text{\Delta} = 3d$.

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
trident network, with a hub right in the middle of the triangle, is

$$
L_{\text{\texttt{Y}}} = \frac{3\sqrt{3}}{2}d.
$$

Since $\sqrt{3}/2 \approx 0.87 < 1$, the trident is indeed shorter
than the triangle.

*Hint.* To determine the length of a trident leg, the gray triangle in
 Figure 2 is useful.

---

We are going to argue not only that the trident network is better than
the triangle network, but that the best place to put the hub station
$D$ is right in the centre, using a simple line of symmetry-based reasoning.
Let's place $D$ anywhere we like, but now draw one of the *axes of
symmetry* of the triangle (the red line in Figure 2).

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner3.png" width="80%"/>
		    <figcaption><i>Figure 3. Wiggling the hub around an axis
    of symmetry.</i></figcaption>
	</div>
	</figure>

## 3. Graphs <a id="sec-3" name="sec-3"></a>

## 3.1. Trees <a id="sec-3-1" name="sec-3-1"></a>

## A. Fermat points <a id="sec-A" name="sec-A"></a>

#### References

https://thatsmaths.com/2015/01/29/the-steiner-minimal-tree/
https://www8.cs.umu.se/kurser/TDBAfl/VT06/algorithms/BOOK/BOOK4/NODE181.HTM
https://en.wikipedia.org/wiki/Steiner_tree_problem
