---
Layout: post
mathjax: true
comments: true
title:  "The Psychology of the present"
categories: Philosophy
date:  2019-07-28
---

**July 28, 2019.** *??*

## Introduction

If physics is to be believed, there is nothing special about the
present.
"Right now" is similar to the statement "right here", but it refers to
*when* the speaker is.
But what is privileged about the moment of utterance?
Is it any more privileged than the bath tub or the park next to the
subway where the speaker happens to declare they are located?
In physical terms, the "present" is just a projection function on
spacetime coordinates,

$$
(t, x, y, z) \mapsto t.
$$

On the other hand, time *feels* different from space.
Unlike space, where I can travel at will between the park and the
bath tub, I cannot choose to return to last Tuesday.
We seem to go in one direction through time, at a fixed speed.
Of course, physics does not contradict this.
Relativity teaches us that time is, indeed, different from space, and
closely bound up with *causation*.
Since experience is a causal affair, with earlier brain states
influencing later ones and not the other way round, this is as it
should be.

But there is more to the peculiar psychology of the present.
While the direction of our movement through time is easily explained,
the sensation of *being in a particular moment* takes more work.
Our qualia seem to be attached to *now*; there is a sort of folk
Cartesianism which takes this as proof that the present is special and
perhaps the only "time" which really exists.
This view is called *presentism*.
As I will argue below, despite its folk appeal, I don't think presentism is a viable
metaphysics of time.

Nevertheless, I think there is an
explanatory gap between common psychological experience and the
physics of time.
I will argue that the gap can be filled by carefully considering what
a person is, and how this is linked to time and causation.
Ultimately, we will need to resolve a variant of Zeno's *arrow
paradox*: what property of an arrow's time slice explains its motion?
Similarly, what properties of a person's time slice explains their
sensation of being trapped in a moving window of experience?

## Time and the present

First, let's discuss some important properties of time, and see why
(in my view) they more or less rule out presentism.
Einstein taught us that *simultaneity is relative*.
Any time two observers move relative to each other, they will disagree
about which events occur at the same time.
However, whatever your reference frame, you will get the same answer
for the following quantity:

$$
s^2(P(t_1,\vec{x}_1), Q(t_2,\vec{x}_2)) = - (t_1-t_2)^2+|\vec{x}_1-\vec{x}_2|^2.
$$

Here, $P$ and $Q$ are points in spacetime, and $(t, \vec{x})$ are
spacetime coordinates in an inertial (non-accelerating) reference frame.
The point is that, by virtue of the principle of relativity, whatever
reference frame we use to define the coordinates, the function $s^2$,
called the *invariant spacetime interval*, is the same.

The spacetime interval has the follow physical interpretation:
- If $s^2(P, Q) = 0$, and $t_1 < t_2$ ($t_2 < t_1$), then $P$ and $Q$
are *null-separated*, and we can send a light ray from $P$ to $Q$ ($Q$ to $P$).
- If $s^2(P, Q) < 0$, and $t_1 < t_2$ ($t_2 < t_1$), then $P$ and $Q$
are *timelike-separated* and a massive observer, or message, can travel from $P$ to $Q$ ($Q$ to $P$).
- If $s^2(P, Q) > 0$, then $P$ and $Q$ are *spacelike-separated*, and
cannot influence each other causally.

Note that the time-ordering in the first two cases does not change,
whatever the reference frame.
For instance, if $t_1 < t_2$, then $t_1' < t_2'$ in any other inertial
reference frame.
The spacetime interval induces a *partial order* $\prec$ on events.
If $P$ can influence $Q$ (they are either null- or timelike-separated), we write $P \prec Q$, and note that this
relation is
- *reflexive*, $P \prec P$;
- *antisymmetric*, $P \prec Q$ and $Q \prec P$ implies $P = Q$; and
- *transitive*, $P \prec Q$ and $Q \prec R$ implies $P \prec R$.
But two points are not comparable, or causally ordered, just in case
they are spacelike separated.

What has this got to do with the present?
If I understand the notion properly, presentism is the view that only
some time slice of the universe really exists.
By "time slice", I mean some collection of events $\Sigma$ which are
mutually spacelike separated.
I think that this notion is incoherent, for two reasons.

First of all, how does the slice "change"?
We might imagine there is some sort of "universal proper time"
$\lambda$ (more generally, a globally hyperbolic time coordinate)
which labels the present slice, $\Sigma(\lambda)$.
How quickly does $\lambda$ change?
I guess at a rate of 1 unit of $\lambda$ per 1 unit of $\lambda$.
For instance, we seem to go into the future at a rate of 1 second per
second, correct?
Something about this answer seems wrong, because *of course* time,
measured by $\lambda$, "changes" at that rate.
The "change" has nothing to do with the present or what exists though,
it is just a tautology about coordinates.


## References

## Extra

Which moment we are "in" seems to changed at some fixed rate, a kind
of "shifting window" which is not, prima facie, dictated by physics.
In the face of these sensations, it is tempting to argue that our *qualia* are
bound to the present moment in special ways, and they show,
incorrigibly, that there is something special about *now*.

I think there are some serious explanatory problems here, real
quandaries about the psychology of time that the folk wisdom highlights.
I will argue that the resolution lies in carefully considering what a
person is, what time is, and what causation is.
In many ways, this is analogous to solving Zeno's *arrow
paradox*, where we must explain what properties of the time slice of a
moving arrow explain its motion.
The solution will perhaps be surprising, but its ingredients are not.
