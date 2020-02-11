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
4. <a href="#sec-A">Fermat points</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

Suppose we have three towns $A$, $B$ and $C$, that we want to join up
by rail.
I should be able to use this railway to travel from one town to any
other, so we say that rail network is *connected*.
A simple example of a connected network is shown below.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner1.png" width="45%"/>
		    <figcaption><i>Figure 1: A simple rail network connecting A, B,
    and C.</i></figcaption>
	</div>
	</figure>
	
Building railway is very expensive, since we not only need to design and
build the rail itself, but acquire the land beneath it.
In contrast, stations are cheap: we just slap together some sidings, a
platform, and a bench or two, and we're done.
Our objective is to make the total length of the rail network as
short as possible, adding extra stations if they help us do this.
This results in the *minimal network* connecting $A$, $B$ and $C$.

We can consider the same problem for $n$ stations, and seek minimal
networks of smallest total length that allow us to travel from a
station to any of the others.
Although finding the minimal network exactly is very difficult, we can
use simple reasoning to learn some important features of the
connectivity and layout of minimal networks.

---

*Exercise 1.* In Figure 1, we have two networks: a triangular network,
and a "star-shaped" network with a new station $D$ in the middle.
Which is shorter?

*Hint.* You can measure the lines with a ruler and add up the lengths.

---

## 2. Triangles <a id="sec-2" name="sec-2"></a>

The three-town train network is already surprising.
The simplest possibility, the triangular network, is not minimal, and
instead, we should place a new station $D$ somewhere in the middle.
The best place to put it is called the *Fermat* or *Torricelli point*,
and if you are very keen, check out the appendix on <a
href="#sec-A">Fermat points</a>.
But for the rest of the post, we just going to think about *when* it
goes in the middle, rather than precisely *where* it goes.
This saves us some hard trigonometry!
But we can determine the position for an important special case: the
equilateral triangle.

## 2.1. Equilateral triangles <a id="sec-2-1" name="sec-2-1"></a>

The first and most important case is when our three towns lie at the
corners of an equilateral triangle.
This is 
Call the distance between towns $d$.

## 3. Graphs <a id="sec-3" name="sec-3"></a>

## A. Fermat points <a id="sec-A" name="sec-A"></a>

#### References

https://thatsmaths.com/2015/01/29/the-steiner-minimal-tree/
https://www8.cs.umu.se/kurser/TDBAfl/VT06/algorithms/BOOK/BOOK4/NODE181.HTM
https://en.wikipedia.org/wiki/Steiner_tree_problem
