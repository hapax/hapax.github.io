---
Layout: post
mathjax: true
comments: true
title:  "The topology of minimal networks"
categories: [Mathematics, Teaching, Hacks]
date:  2020-02-010
---

**February 10, 2020.** *An elementary introduction to the topology of
  minimal networks.*

### Contents

1. <a href="#sec-1">Introduction</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

Suppose we have three towns $A$, $B$ and $C$, that we want to join up
by rail.
I should be able to use this railway to travel from one town to any
other, so we say that rail network is *connected*.
A simple example of a connected network is shown below.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner1.png" width="45%"/>
		    <figcaption><i>A simple rail network connecting A, B,
    and C.</i></figcaption>
	</div>
	</figure>
	
Building railway is very expensive, since we not only need to design and
build the rail itself, but acquire the land beneath it.
In contrast, stations are cheap: we just slap together some sidings, a
platform, and a bench or two, and we're done.
Our goal is therefore to *make the total length of the rail network as
short as possible*, adding extra stations if need be to reduce this
length.
This is called a *minimal network*.

Will our triangular rail network above be minimal?
It turns out that, to minimise the total amount of rail, we should
build a new station $D$ in between and connect each town to it.
Our goal in this post will be to see why, and how this generalises to
multiple stations.
Although the exact positions are hard to compute in general, we will
learn some simple facts about the *topology* and connectivity
structure of minimal networks.

#### References

https://thatsmaths.com/2015/01/29/the-steiner-minimal-tree/
https://www8.cs.umu.se/kurser/TDBAfl/VT06/algorithms/BOOK/BOOK4/NODE181.HTM
https://en.wikipedia.org/wiki/Steiner_tree_problem
