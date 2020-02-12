---
Layout: post
mathjax: true
comments: true
title:  "A minimal introduction to minimal networks"
categories: [Mathematics, Teaching, Hacks]
date:  2020-02-11
---

**February 11, 2020.** *An elementary introduction to the topology and
  geometry of minimal networks. (First two sections finished.)*

### Contents

1. <a href="#sec-1">Introduction</a>
2. <a href="#sec-2">Triangles</a>
   1. <a href="#sec-2-1">Equilateral triangles</a>
   2. <a href="#sec-2-2">Deforming the triangle</a>
   3. <a href="#sec-2-3">Hubs and spokes</a>
3. <a href="#sec-3">Graphs</a>
   1. <a href="#sec-3-1">Trees</a>
   2. <a href="#sec-3-2">Counting hubs</a>
4. <a href="#sec-A">Fermat points*</a>

## 1. Introduction <a id="sec-1" name="sec-1"></a>

Suppose we want to join up three towns ($A$, $B$ and $C$) by rail.
If I can use this railway to travel from one town to any
other, we say that rail network is *connected*.
Two simple examples of connected networks are shown below.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner1.png" width="70%"/>
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
We will step through the reasoning in bite-sized chunks, starting with
the problem of connecting three cities.

---

*Exercise 1 (choosing sides).* Suppose $A$, $B$ and $C$ are separated
by distances $AB = c$, $AC = b$ and $BC = a$.
A triangular network consists of two sides of the triangle.
Which ones should we choose?

<p align="center">
  ⁂
</p>

*Exercise 2 (triangle or trident).* In Figure 1, we have two networks connecting the same towns: a triangular network,
and a trident-shaped network with a hub station $D$ in the middle.
Which is shorter?
See if you can do better than either.

*Hint.* Measure lengths on the screen with a ruler. You may
 feel like your grandparents, but it works!

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

### 2.1. Equilateral triangles <a id="sec-2-1" name="sec-2-1"></a>

Suppose that the towns $A$, $B$ and $C$ are now equally spaced,
and sit on the corners of an equilateral triangle of side length $d$.
The triangular network has total length $L_\Delta = 2d$.

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

*Exercise 3 (equilateral trident).* Show that the length of the
trident network, with a hub in the centre of the triangle, is

$$
L_{\text{Y}} = \sqrt{3}d.
$$

Since $\sqrt{3} \approx 1.7 < 2$, the trident is indeed shorter
than the triangle.

*Hint.* Use the grey triangle in Figure 2.

---

We are going to argue not only that the trident network is better than
the triangle network, but that the best place to put the hub station
$D$ is right in the centre, using *symmetry*.
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
		    <figcaption><i>Figure 4. Length is an even function, so
    zero wiggle is a maximum or a minimum.</i></figcaption>
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
    ="/images/posts/steiner5.png" width="70%"/>
		    <figcaption><i>Figure 5. The trident network gets long for large $x$.</i></figcaption>
	</div>
	</figure>

This suggests that $L$ is a *minimum* and not a *maximum* at $x=
0$, so the top graph in Figure 4 is the correct one.
If it was a maximum, then length would get smaller at large $x$!

---

*Exercise 4 (exact length).* Although this argument is plausible,
 it doesn't rule out the possibility that $x=0$ is actually a maximum,
 with the true minimum at some symmetrically spaced points $\pm
 x_\text{min}$, before length increases again as $|x|$ gets larger.
 If you are worried, you can calculate the length exactly and check!

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner6.png" width="35%"/>
		    <figcaption><i>Figure 6. Calculating the exact network length.</i></figcaption>
	</div>
	</figure>

<span style="padding-left: 20px; display:block">
(a) Show that, for the triangle in Figure 6, the length of the network is
</span>

$$
\begin{align*}
L(x) &= L_1 + L_2 + L_3 \\ & = \sqrt{\left(\sqrt{3}d - h\right)^2 + x^2} +
\sqrt{h^2 + (d-x)^2} + \sqrt{h^2 + (d+x)^2}.
\end{align*}
$$

<span style="padding-left: 20px; display:block">
*Note.* We choose side length $2d$ rather than $d$ to simplify the algebra.
</span>

<span style="padding-left: 20px; display:block">
(b) Check this function is even, i.e. $L(x) = L(-x)$.
</span>

<span style="padding-left: 20px; display:block">
(c) For simplicity, we can set $d= 1$.
Plot $L(x)$ for various values of $h$ between $0$ and its
maximum value $\sqrt{3}$, and verify that $x=0$ is indeed a minimum of length.
</span>

---

We have established that, in order to minimise the length, the hub $D$
should lie on the red axis of symmetry associated with vertex $A$.
But of course, we can repeat this argument for $B$ and $C$ as well!
There are three axes of symmetry, and they happen to intersect in a
point at the centre of the triangle.
Since $D$ should lie on each of these lines, it must lie at the centre
of the triangle, as depicted in Figure 7.
This solves the minimal network problem on an equilateral triangle!

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner7.png" width="40%"/>
		    <figcaption><i>Figure 7. The minimal network on an
    equilateral triangle.</i></figcaption>
	</div>
	</figure>

Before we go on, we note a couple of features of this trident graph.
We have a point in the centre, with three incoming edges separated by
angle $120^\circ$.
Remarkably, this is a completely general feature of minimal networks!
Any time we add a hub, it will have three spokes separated by equal
angles.
To see why, read on!

### 2.2. Deforming the triangle <a id="sec-2-2" name="sec-2-2"></a> 

We are now going to take our solution to the equilateral triangle and
slowly deform it.
In other words, we imagine slowly moving the corners of the triangle
so it is no longer equilateral.
What will happen to the optimal position of the hub $D$?
Since everything is being smoothly modified, the position of the hub
should change smoothly as well.
In Figure 8, the smooth paths of the corners are depicted in purple,
and the corresponding smooth change of hub in green.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner8.png" width="35%"/>
		    <figcaption><i>Figure 8. The optimal hub position changes smoothly
    as we deform the corners.</i></figcaption>
	</div>
	</figure>

Since the hub position changes smoothly, it should stay inside the
triangle for small deformations of the corners.
But for triangles which are very far from equilateral, you might
imagine that the hub actually *intersects* one of the corners, and our
trident network becomes a simpler triangular network, formed from two
sides of the triangle.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner9.png" width="45%"/>
		    <figcaption><i>Figure 9. At some critical angle, the trident
    network becomes a triangular one.</i></figcaption>
	</div>
	</figure>

We picture this in Figure 9 above.
In this diagram, $B$ remains fixed in position, but $A$ and $C$ slowly
lower and open out the angle of the triangle, and the optimal hub $D$
moves down as they do so.
At some critical angle $\theta_\text{crit}$ (coloured olive in Figure 9), it
will coincide with $B$.
The question is: what is the angle?

It turns out this critical angle is $\theta_\text{crit} = 120^\circ$. Although we won't provide a watertight
proof, we can give a plausibility argument.
Let's return to the equilateral triangle.
Instead of adding a hub in the middle, suppose that $D$ is in fact a
fourth city fixed in place.
Clearly, the solution in Figure 7 is still optimal, since if adding
more hubs reduced the total length, we could add more hubs in our
original three city problem to reduce length!
If I now remove any of the corner cities $A$, $B$ or $C$, the optimal
network simply removes the corresponding leg of the trident (Figure 10).

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner10.png" width="40%"/>
		    <figcaption><i>Figure 10. Removing a corner city removes a
    leg from the equilateral trident.</i></figcaption>
	</div>
	</figure>

I'll let you explore why we only remove a leg, rather than adding a
whole new hub, in the next problem.

---

*Exercise 5 (cutting corners).* Suppose that in Figure 10, we can add
a new hub $E$ which reduces the length of the network.
Explain how adding $E$ could reduce the length of the network in
Figure 7, and thereby improve our solution for the equilateral
triangle.
Since we have already argued that Figure 7 is minimal, we clearly
cannot find such a hub $E$!

*Note.* This is an example of a
 [proof by contradiction](https://en.wikipedia.org/wiki/Proof_by_contradiction). To
 show something is false, we assume it is true and use it to derive a
 contradiction with known facts.
 We then reason backwards to
 conclude that it cannot be true!

---

So, we should be satisfied that for an angle of $\theta = 120^\circ$,
the trident collapses into a triangular network.
But could it happen earlier, with $\theta_\text{crit} < 120^\circ$?
We can actually run Figure 9 in reverse to see this won't happen.
Imagine that $A$ and $C$ move *up* along the purple curves from the
initial angle of $120^\circ$.
Then the hub $D$ should smoothly move up as well.
Thus, we conclude that $\theta_\text{crit} = 120^\circ$.
This is not a fully rigorous proof, but I hope a plausible one.

### 2.3. Hubs and spokes <a id="sec-2-3" name="sec-2-3"></a>

All this work with triangles pays off with a powerful result about
minimal networks for *any* number of cities:

<span style="padding-left: 20px; display:block">
In any minimal network, all hubs have three incoming legs separated by angles of $120^\circ$.
</span>

By "hub", we mean an additional point on the network (like a train
station) we added to reduce the total length.
The argument is beautiful and simple, though like Exercise 5, it
involves a proof by contradiction.

---

*Proof.*
Our first step is to show that it is impossible for a hub to have
incoming edges separated by less than $120^\circ$.
Suppose we have cities $A_1, A_2, \ldots, A_n$ connected by a
minimal rail network.
Also suppose there is a hub station $H$ with incoming rail lines
separated by less than
$\theta_\text{crit} = 120^\circ$, as on the left in Figure 11.
There may be other incoming lines (the horizontal lines in Figure 11),
but these will play no role in our proof and can be ignored.

We can build two new stations on these outgoing legs, $h_1$ and $h_2$,
which are (for simplicity) the same distance from $H$.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner11.png" width="80%"/>
		    <figcaption><i>Figure 11. Left: A hub with incoming
    angle less than 120°. Right: A shorter network.</i></figcaption>
	</div>
	</figure>

It's easy to see that every angle in this triangle is less than
$120^\circ$, since the angles at $h_1$ and $h_2$ are at most
$90^\circ$, and we've assume the angle at $H$ is less than
$120^\circ$.
Thus, from our work in the previous section, we know that the minimal
network connecting $h_1$, $h_2$ and $H$ is not the triangle we have
drawn, but a trident with another hub $h_3$ in the middle!
This strictly decreases the length of the network (shown right in
Figure 11), and hence, our original network must not have been
minimal.
There's our contradiction!

So, we know that any hub must have spokes separated by at least
$120^\circ$.
How do we know that there are three, separated by exactly $120^\circ$?
This is very simple.
Suppose two lines enter $H$, separated by more than $120^\circ$.
Then there can only be two incoming edges, joining $H$ to some cities
$A$ and $B$, since any additional lines would have to be closer than
$120^\circ$ to one of these lines, given the result we
just proved.
So, we have the situation depicted on the left of Figure 12:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner12.png" width="80%"/>
		    <figcaption><i>Figure 12. Left: A hub with incoming
    angle greater than 120°. Right: A shorter network.</i></figcaption>
	</div>
	</figure>

Hopefully you can see what goes wrong. If there is a "kink" in the
line, with separating angle $\theta \neq 180^\circ$, then we can obtain a shorter
network be deleting $H$ and directly connecting $A$ and $B$.
Once again, we have a contradiction!

---

Now, strictly speaking, we can have hubs with only two incoming edges,
separated by $180^\circ$.
But such a hub is always unnecessary, since all it does is sit on a
straight line.
In real life, hubs do cost some money (even if it is dramatically less
than spokes) so we will never build unnecessary ones!
If we always delete these useless hubs, we have the general result advertised
above, namely that any hub in a minimal network has three equally
spaced spokes.

---

*Exercise 6 (outer rim).* Our proof applies to hubs only, but the same style of argument allows you to deduce properties of
the cities or *fixed nodes* $A_1, A_2, \ldots, A_n$.
To pursue the hub/spokes analogy, these form the rim of a
strangely-shaped wheel!
Prove the following properties:

<span style="padding-left: 20px; display:block">
(a) No incoming edges can be separated by less than $120^\circ$.
</span>

<span style="padding-left: 20px; display:block">
(b) The number of incoming edges is between $1$ and $3$.
</span>

<span style="padding-left: 20px; display:block">
(c) A city has three edges only if it lies at the centre of an equilateral triangle of cities.
</span>

The upshot is that the fixed nodes will in general have one or two
incoming edges, and three only in very special circumstances.

---

## 3. Graphs <a id="sec-3" name="sec-3"></a>

In this section, we will learn more about the connectivity and layout
of minimal networks.
The geometric facts we learned in the last section will definitely come in handy!

### 3.1. Trees <a id="sec-3-1" name="sec-3-1"></a>

In a minimal rail network, how many ways can I get from $A$ to $B$?
If the network is connected, then the answer is at least one.
That's the definition of connected!
But if the network is *minimal*, the answer is *exactly* one!
If there is more than one way to get from $A$ to $B$, the network has
unnecessary edges and can be pruned to get something shorter.
We might worry that pruning redundant paths between $A$ and $B$ could
disconnect other cities, but this is never the case.
Figure 13 shows why.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner13.png" width="70%"/>
		    <figcaption><i>Figure 13. Pruning an unnecessary path,
    e.g. path 2, cannot disconnect a network.</i></figcaption>
	</div>
	</figure>

Suppose $A$ and $B$ are connected by two paths, labelled
$1$ and $2$.
The green blob to the left is all the nodes whose paths to $B$ go
through $A$ first, and similarly, nodes on the right connect to $A$
through $B$.
If two nodes are in the same blob, such as $C$ and $E$, then pruning
path $2$ has no effect on whether they are connected.
If two are in different blobs, like $C$ and $D$, they can still reach
each other using path $1$.
So, pruning redundant paths between $A$ and $B$ does not affect
whether other nodes connect.

---

*Exercise 7 (path pruning).* Generalise the argument above to account
for nodes that lie between $A$ and $B$.
More precisely, these are nodes which can connect to either $A$ or $B$
without passing through the other, and schematically lie on paths $1$
or $2$.

---

Once we have completely pruned the network, there is only a single
path connecting any two nodes $A$ and $B$.
Such a network is called a *tree* because of the way it branches.
An example is shown in Figure 14.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner14.png" width="35%"/>
		    <figcaption><i>Figure 14. A tree network, with unique
    paths between each node.</i></figcaption>
	</div>
	</figure>

Our reasoning shows that minimal networks are trees.
The number of nodes in the network is $N = n + h$, where $n$ is the
number of fixed nodes and $h$ counts the hubs we add to make the
network as short as possible.
For instance, in Figure 14 we have $N = 9$.
The number of edges is $E = 7$, which is $N - 1$, and is no
coincidence.
For *any* tree, it turns out that $E = N - 1$.
To prove this, we first need to know that (unlike real life), in
network theory, every tree has leaves.

---

*Exercise 8 (trees and leaves).*
A *leaf* is a node with a single edge, e.g. the nodes $J$, $D$, $G$,
and $I$ in Figure 14.
Part (a) will show what we need, namely that every tree has a leaf,
and parts (b) and (c) probe this question a little more deeply.
To begin, we will choose a node at random (red in Figure 15) and count
the number of steps to each other node.
Since there is a unique path between two nodes in a tree, this is well-defined.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/steiner15.png" width="80%"/>
		    <figcaption><i>Figure 15. Finding leaves in a tree.</i></figcaption>
	</div>
	</figure>

<span style="padding-left: 20px; display:block">
(a) Consider the node or nodes furthest from our selected node (orange
nodes in Figure 15). Argue that these must be leaves.
*Hint.* If they are not, what are the distances of the neighbours?
</span>

<span style="padding-left: 20px; display:block">
(b) Take the further node and now find the node or nodes furthest
away. Argue that these are also leaves.
</span>

<span style="padding-left: 20px; display:block">
(c) Conclude that every tree has at least two leaves.
Show, using an example, that a tree need not have more than two.
</span>

---

### 3.2. Counting hubs <a id="sec-3-2" name="sec-3-2"></a>

## 4. Applications and algorithms <a id="sec-4" name="sec-4"></a>

## A. Fermat points* <a id="sec-A" name="sec-A"></a>

#### References

https://thatsmaths.com/2015/01/29/the-steiner-minimal-tree/
https://www8.cs.umu.se/kurser/TDBAfl/VT06/algorithms/BOOK/BOOK4/NODE181.HTM
https://en.wikipedia.org/wiki/Steiner_tree_problem
