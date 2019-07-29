---
Layout: post
mathjax: true
comments: true
title:  "Presentism and the psychology of time"
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
Our qualia seem to be attached to *now*; folk
Cartesianism which takes this as incorrigible proof that the present is special and
perhaps the only "time" which really exists:
"I can only tell that *right now* exists, and since I cannot
experience any other times, they must not exist".
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

## No time like the present

First, let's discuss some important properties of time, and see why
(in my view) they more or less rule out presentism.

#### Simultaneity and causal order

Einstein taught us that *simultaneity is relative*.
Any time two observers move relative to each other, they will disagree
about which events occur at the same time.
However, whatever your reference frame, you will get the same answer
for the following quantity:

$$
s^2\big(P(t_1,\vec{x}_1), Q(t_2,\vec{x}_2)\big) = - (t_1-t_2)^2+|\vec{x}_1-\vec{x}_2|^2.
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
The last requirement, that spacelike separated observers cannot
influence each other, is not only an empirical observation, but
needed to ensure that *cause and effect are ordered*.
This is due to the relativity of simultaneity.
If I could send messages faster than light, it is easy to set up
situations where, bouncing signals off a moving mirror, I could send
communicate with myself in the past.
We then run into all the paradoxes of time travel.
To me, this suggests that the ordering of cause and effect is a basic
consistency requirement for the universe.

If you want to be a little more precise about cause and effect, you
can use the
spacetime interval to define a *partial order* $\prec$ on events.
If $P$ can influence $Q$ (they are either null- or timelike-separated), we write $P \prec Q$, and note that this
relation is
- *reflexive*, $P \prec P$;
- *antisymmetric*, $P \prec Q$ and $Q \prec P$ implies $P = Q$; and
- *transitive*, $P \prec Q$ and $Q \prec R$ implies $P \prec R$.

Two points are not comparable, or causally ordered, just in case
they are spacelike separated.

#### Presentism defined

What has this got to do with the present?
If I understand the notion properly, presentism is the view that only
some time slice of the universe really exists.
By "time slice", I mean some collection of events $\Sigma$ which are
mutually spacelike separated, or equivalently, *mutually incomparable*
according to the causal partial order.
I used to think that the relativity of simulaneity was knock-down
argument against presentism.
Since being simultaneous is not an equivalence relation, and the
notion of being co-present (existing together) is, surely presentism is wrong?
No: all this shows is that being co-present is not the same
as being simultanous according to each other's clocks.
If we define the "present" as a slice $\Sigma$, which will have a
transitive notion of co-presence after all.

One issue with $\Sigma$ is that it is not unique.
That is, any event $P$ is contained in an infinite number of spacelike
slices $\Sigma$.
Which is the "real" one?
At large scales, our universe has a preferred cosmological time $t$,
and perhaps (the presentist could argue) this naturally singles out a
slice $\Sigma(t)$.
This solution is somewhat ad-hoc, but more importantly, doesn't
explain how to "pick out" the right slice locally, for instance in the
presence of a black hole.
A friend falls into the event horizon, and I wonder "Which slice is
real?"
I don't think the presentist can help, since the natural operational
definitions (e.g. I can send a message to the slice) are *causal*, and
therefore take me out of the set of timelike slices $\Sigma$.
(Here, I am ignoring the issue of global hyperbolicity, but it is not
really relevant since the same issues arises near a star.)

One suspects that, in asking these questions about the person falling
into a black hole, language has gone on holiday (Wittgenstein).
But the presentist can simply assert that the slice exists, and leave
the problem of selecting the correct $\Sigma$ to the axiom of choice,
or God, or some comparable higher power.
What can we say then?

#### Demiurges and the reality of change

A subtler problem is *change*.
Presentism claims that *what is real*, i.e. the present slice
$\Sigma$, is changing.
But changing with respect to what?
If I label or define slices with respect to some type of
"universal proper time" $\lambda$ (e.g. cosmological time), the
answer seems to be: with respect to $\lambda$, at a rate of 1 unit of
$\lambda$ per unit of $\lambda$.
As people often joke, we are moving into the future at 1 second per
second.

The answer is of course tautological.
But it is worse than that for the presentist.
To see why, let's discretise time into steps $t_n$.
Presentism suggests that, ontologically, a slice $\Sigma(t_0) =
\Sigma_0$ is brought into being, then destroyed and replaced by
$\Sigma_1$.
We repeat the process with $\Sigma_2$, and so forth.
How long do these slices exist?
It seems like there is no way to measure this, since $t_n$ is attached
to the slices themselves.
But to ask what exists "now" presupposes some sort of time in our
creation and destruction process!

We have the following infinite regress problem.
Suppose a demiurge $D_1$ is running this "program" of creating and
destroying the slices $\Sigma_n$.
To even ask which slice is currently loaded, the demiurge also needs to
have a time (once again discrete for simplicity) $t^{(1)}_n$.
But of course, we then need *another* demiurge $D_2$ with time $t^{(2)}$ to
program the slices for the demiurge $D_1$.
And so on.
I think this a bad regress since no demiurge explains what "present"
actually means.
Perhaps, like the choice of spacelike slices, the
presentist can appeal to God, in this case as a sort of limit or union of demiurges, $D =
\lim_{n\to\infty} \cup_n D_n$.

But what if our demiurges make errors, as demiurges are wont to do?
Perhaps they slices $\Sigma_4$ and $\Sigma_5$ actually coexist for
at some time $t^{(1)}$, or different slices of the demiurge
themself coexist at some time due to a lapse of attention in one of
the higher demiurges!
Even worse, demiurges could get the order *wrong*, making $\Sigma_9$ before $\Sigma_3$.
Can observers living in the slice $\Sigma$ tell how long in demiurge
time it is running for?
Or somehow feel "present" in both $\Sigma_4$ and $\Sigma_5$ when they
are run at the same time?
Or "sense" the reversal of causal order when $\Sigma_3$ comes before
$\Sigma_9$?

Of course not.
Observers living in $\Sigma$ have no access to any of this data, since
this would give them super-causal powers.
In fact, I think this means we cannot tell what *any* demiurge is
doing, including $D_1$.
The ability to tell which slice is present is unreasonably powerful
for a creature causally bound to the slices.
In other words, even if presentism is a correct picture of the
ontology of time, there is every reason to think that we would be
*unable to distinguish* this state of affairs from the more
conventional, four-dimensional picture where all the slices $\Sigma_n$
exist at the same time.

## Personhood and causation

But the folk Cartesian 

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

Perhaps there is some "universal proper time" $\lambda$, labelling the
current slice $\Sigma(\lambda)$.
How quickly does it change?
I suppose 1 unit of $\lambda$ per unit of $\lambda$, just as we seem
to go forward in time 1 second per second.
But clearly, this answer is just a tautology about our coordinates!
If presentism is correct, we can only say that the *things change* but
there is no non-tautological way of saying how quickly.

Of course, we could define some secondary time which measures "how
long" the slices exist, but it is clearly unobservable, leads to a
infinite regress (since we now need to consider the "present" in our
creation and destruction process), and is in any event unnecessary for
presentism.
All that matters is that existence uniquely specifies a slice.


Perhaps the process is something like a computer program.
