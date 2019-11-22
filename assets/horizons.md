---
Layout: post
mathjax: true
comments: true
title:  "Horizons, partial orders and fatalism"
categories: [Physics, Mathematics, Philosophy]
date:  2019-10-28
---

**October 28, 2019.** *Black holes are regions you can enter but can't
  leave. It turns out you can define this notion for an arbitrary
  partial order, *

## Introduction

A *black hole* is a region you can enter, but can't leave.

## Black holes in partial orders

### Black holes and exteriors

### Horizons

## References

## EXTRA

What exactly distinguishes space inside and outside the black hole
won't concern us here.

In technical language, we would talk about *asymptotic* regions (like
future null/timelike infinity) so we think of these as a set of
events, and label them $\mathcal{A}$.
The black hole has a different destiny in store for those
who fall inside: they will encounter a *singularity*, a different (and
less pleasant) set of events $\mathcal{S}$.
In a space with multiple black holes, we of course have multiple
singularities $\mathcal{S}_i$.

In black hole physics, a *horizon* is a point of no return: pass the
horizon, and you can never escape from the black hole.
But there are different types of horizon.
An *absolute horizon* is a global, "teleological" notion, which may
contain regions of spacetime long before the black hole (which they
will inevitably fall into) actually forms.
In some cases, you may be "trapped", but luckily no singularity forms!
A more local notion is an *apparent horizon*.
As the name suggests, apparent horizons can be detected (in principle) by an observer with an array of laser pointers.
Unlike an absolute horizon, an apparent horizon always conceals a
singularity.

I'm not going to talk about black holes much more than this.
However, the notion of a horizon --- and these local and global
flavours --- are interesting in the more general context of
*partial orders*.
A partial order is a binary relation $\leq$ on a set $S$ with
the following RAT properties for all $x, y, z \in S$:

1. $x \leq x$ (*reflexive*);
2. $x \leq y$ and $y \leq x$ implies $x = y$ (*antisymmetric*);
3. $x \leq y$ and $y \leq z$ implies $z \leq z$ (*transitive*).

Examples include the $\leq$ relation on integers, inclusion of sets,
and causal relationships between events.
Our goal here will be to define horizons for any partial order, and
use them to (perhaps usefully) restate some old philosophical
problems.

In order for $\mathcal{A}$ and $\mathcal{S}$ to play the roles
ascribed to them here, they require two basic properties:

1. No event in $\mathcal{A}$ can influence any event in $\mathcal{S}$,
   or vice-versa.
2. The sets $\mathcal{A}$ and $\mathcal{S}$ contain all events they can influence.

Let $(\leq, S)$ be a partial order, as defined above.

A black hole is a region where any observer, once inside, has only one
future in store: collision with a singularity.
There must also be a region outside the black hole where luckier
observers can live out their days in comparative peace.
More generally, a *horizon* exists whenever there are some observers
who can never 

But while a black hole should have this property, it clearly isn't enough.
First of all, any observer $b$ inside the black hole has a future $F(b)$ with this property.
Since these different observers can meet up in the future, their futures should be part of the same black hole.
Let's formalise this notion of meeting in the future.

**Definition 2.** *The sets $A, B \subseteq S$* join *if $F(A) \cap F(B) \neq \varnothing$*.

It seems, then, like a black hole should be something like the union of sets $F(B) = B$ which join, or equivalently, such that any other such set does not meet $B$.
But this still isn't quite right, since this could be the whole set $S$!
If we exclude this by fiat, we should have a good notion of black hole.

A black hole is a region which an observer cannot
leave once entered: their future always lies inside the black hole.
There must also be region of space *outside* the black hole, where an
observer can choose to live out their days in comparative peace.
Some part of their future light cone lies outside the black hole.

To formalise these ideas, let's first define the *future* of a
point in a partial order $(S, \leq)$.
We think of $x \leq y$ as $y$ is in the future of $x$.

**Definition 1.** *The* future *of a set $A \subseteq S$ is the set of
points*
\[
F(A) := \{y \in S : \exists x \in A, y \geq x\} = \cup_{a \in A} F(a).
\]
*We can define the* past *of a set $P(A)$ similarly.*

In relativity, $P(x)$ is the future light cone of an event $x$.
For the real numbers, $P(x) =
[x, \infty)$ is the half-infinite line starting at $x$.

**Exercise 1.** Using RAT, show that:
1. A set is contained in its future $A \subseteq F(A)$.
2. The future function is "idempotent", $F(F(A)) = F(A)$.
3. If $A = F(A')$ and $A' = F(A)$, then all sets are equal, $A = A' = F(A) = F(A')$.

What is the equivalent of a black hole?
For every point in the black hole $B$, the future of the point should remain in the black hole, so $F(B) = B$.
This is the *trapping* property.
But we need more!
For instance, the future of any subset $B' \subseteq B$ has the same trapping property (trivially by idempotence), but is a strict subset of our black hole.
We need a completeness property.


**Definition 3.** *A* black hole *is a set $B \subseteq S$ with the following properties:*
1. $F(B) = B$ (trapping);
2. for any other $B'$ with $F()$ (complete);
3. $B \neq S$.
