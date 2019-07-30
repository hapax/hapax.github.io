---
Layout: post
mathjax: true
comments: true
title:  "Four-dimensionalism and the psychology of time"
categories: Philosophy
date:  2019-07-29
---

**July 29, 2019.** *Modern physics suggests a view of time called
  four-dimensionalism: just as all places exist simultaneously, all
  times should exist simultaneously. I examine some consequences for
  the psychology of time, and contrast with the (more intuitive but
  ultimately incoherent) philosophy of time called presentism.*

## Introduction

If physics is to be believed, there is nothing special about the
present.
"Right now" is similar to the statement "right here", but it refers to
*when* the speaker is.
But what is privileged about the moment of utterance?
Is it any more privileged than the bath tub or the park next to the
subway where the speaker happens to declare they are located?
In physical terms, the "present" is just a projection function:

$$
P(t, x, y, z) \mapsto t.
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
Our qualia seem to be attached to *now*; there is a folk
Cartesian argument which takes this as incorrigible proof that the present is special and
perhaps the only "time" which really exists.
This view is called *presentism*.

I will argue below that, despite its folk appeal, presentism is not a
viable metaphysics of time.
Nevertheless, there is an explanatory gap between common psychological
experience and four-dimensionalism.
I will argue that the gap can be filled by thinking carefully about
how sensation arises from brain states.
Ultimately, we will need to resolve a variant of Zeno's *arrow
paradox*.
Zeno asked: how can we explain the motion of an arrow from its
"stationary" time slice?
Similarly, we must ask what properties of a brain state explain the sensation of moving through time.

## No time like the present

I'll recap some properties of time, before defining (and arguing
against) presentism.
This will leave us with some explaining to do!

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
some *time slice* of the universe really exists.
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
(In fact, in the presence of a black hole there can be global
obstructions to the definition of $\Sigma$, but I will ignore these.
I do not want my objections to presentism to depend on exotic
features of spacetime.)

One suspects that, in asking these questions about the person falling
into a black hole, language has "gone on holiday" (Wittgenstein).
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
have a time $t^{(1)}$ (once again discrete for simplicity).
But of course, we then need *another* demiurge $D_2$ with time $t^{(2)}$ to
program the slices for the demiurge $D_1$.
And so on.
I think this a bad regress since no demiurge explains what "present"
actually means.
Perhaps, like the choice of spacelike slices, the
presentist can appeal to God, in this case as a sort of limit or union of demiurges, $D =
\lim_{n\to\infty} \cup_n D_n$.

I don't think this helps, but let us suppose for the sake of argument
that it is possible to fix the regress.
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

(These faulty demiurges are partially inspired by Greg Egan's
["dust theory"](https://www.gregegan.net/PERMUTATION/FAQ/FAQ.html),
from his excellent novel *Permutation City*.
The demiurge argument also has a similar flavour to Augustine's argument
against duration in the *Confessions*.)

## Brain states and sensations

Perhaps, as I have argued, presentism is not a sensible picture of
time.
But the claims of our qualia are not lightly dismissed.
An infinite tower of demiurges creating and destroying one another may
be absurd, but the related convictions that *I am experiencing right
now*, and that *change is real*, are not absurd.
How can we explain these in the framework of four-dimensionalism?

#### Experience and "nowness"

Conscious experience is famously
difficult explain from the physicalist viewpoint.
But whatever qualia are, I assume they are the result of physical
processes in the brain, and supervene on brain states.
Run the process, or set up the state (a subtle distinction we return
to later), and the associated conscious experience should appear.

It is then straightforward to explain why we feel like we are always
"in the present moment" from the four-dimensionalist perspective.
If the time slice of the brain $B(t_n) = B_n$ always exists, it is always in a
particular state; it is therefore always producing the sensations
$S_n$ associated with that state.
Of course, those sensations are attached to a specific time and place,
and the sensation of being "experiencing things right now" is no
different, fundamentally, from "experiencing things right here".
The novelty or strangeness of these time indexicals is that we do not
feel like we control our motion in time, so there is perhaps something
surprising about being "at this present moment".
How did we get there?
It is not due to some deep ontology that our brains are somehow
enabled to track.
It is simply a result of causal relations between brain states.

Before I elaborate on this last statement, let me be clear.
I think that brain states $B_n$ always exist; this is what
four-dimensionalism dictates.
If they always exist, they are always producing the associated qualia
$S_n$ and so a brain state leads to a permanent state of feeling.
You may ask how it is possible to always be "feeling" $S_n$ when the
sensations feel temporary.
I will discuss this at length in the next section, but the point of
the demiurge example is that *the ontology of time slices has nothing
to do with conscious experience*.
This is why presentism is tempting but wrong.
It conflates properties of conscious experience with properties of time.

#### The arrow of Zeno

It is not clear that brain states that are permanently feeling have
anything to do with our everyday experience.
Sensations last a moment, and are quickly succeeded by new ones,
almost as if they are being created and destroyed by particularly
reliable demiurge.
The question, then, is whether the content of the sensation $S_n$ can account
both for the feeling of duration and succession.

There is a helpful pre-Socratic analogue to the problem we are
considering here.
Zeno's third paradox of motion involved an arrow in flight.
We can state the paradox as follows:
- The arrow, at any moment of time, is stationary.
- Time is composed of moments.
- Stationary objects remain stationary.

Combining these three, we seem forced to conclude that the arrow can
never move.
Similarly, one might imagine that a brain state $B_n$, always
producing the qualia $S_n$, can never give rise to the "flow" of
conscious experience.
(A similar argument was put forward independently by Le Poidevin,
building on Broad's [*Scientific Thought*](http://www.stafforini.com/broad/Broad%20-%20Scientific%20thought.pdf).)

The answer to the paradox is simple.
There is a difference between a stationary arrow and a moving arrow
examined at an instant of time.
The moving arrow has properties the stationary arrow lacks, which not
only explain the difference in subsequent motion but have measurable
effects on the slice itself.

Similarly, intrinsic properties of the brain state $B_n$ must generate the
feelings of duration and succession.
Let's first consider the simpler of the two, succession.
At a physical level, "succession" reflects the fact that earlier
brain states $B_{m<n}$ are part of the causal input to the brain state $B_n$.
The previous states $B_{m<n}$ are in fact stored and represented in
$B_n$ via *memory*, but at an abstract level, succession is just the
statement that causal relations are mirrored in cognitive ones.

Duration is trickier, but not so different from the velocity
of an arrow.
The velocity is the rate at which the arrow acquires distance, but
both the distance and time must be given units, i.e. a physical basis
for measurement.
Similarly, the duration of an experience cannot make any sense without
units.
Luckily, our brains are naturally equipped with physiological process
(such as circulation) which can be used to measure time, and input
channels (with thresholds, capacities, and so forth) which can be used
to measure intensity.
It seems plausible that the subjective "rate" of experience
is some function of the strength, nature and speed of sensory input,
relative to these physiologically defined units of measurement, along
with how efficiently they can stored in sensory and short-term memory.

## Conclusion

To reconcile our experience of time with four-dimensionalism, we seem
to be driven to some strange conclusions.
Every brain state $B_n$ in the history of a thinking being always
exists, by four-dimensionalism.
If we are physicalists about sensation, then those brain states are
*always* accompanied by sensations.
The brain states always feel.
Four-dimensionalism therefore suggests an extreme version of
Nietzsche's doctrine of eternal recurrence: we are, and will always,
live all moments of our life simultaneously, but with the impression
of "nowness" and temporal succession by virtue of the physical
properties of brain states.

But "always feeling" does not mean "feeling always".
We should not confuse the properties of the time slices with
properties of the sensations they give rise to (fallacy of composition).
This is the fundamental error of the presentist.
Still, some work is required to see where the duration and succession
of our experience of time comes from.
I have sketched some arguments, and hope to fill out the details in
the future.

#### Arrest

For a different take on these issues, see my sci-fi short story
["Arrest"]({{hapax.github.io}}/assets/arrest.pdf).
It was originally submitted to the
[Ubyssey sci-fi competition 2019](https://www.ubyssey.ca/science/arrestee-sci-fi-winner-2019/)
under a different name.

## References

- [*Permutation City*](https://www.gregegan.net/PERMUTATION/Permutation.html)
  (2007), Greg Egan.
- ["Zeno’s Paradoxes"](https://plato.stanford.edu/entries/paradox-zeno/#Arr)
  (2018), Nick Huggett. *Stanford Encyclopedia of Philosophy*.
- ["The Experience and Perception of Time"](https://plato.stanford.edu/entries/time-experience/) (2019), Robin Le Poidevin. *Stanford Encyclopedia of Philosophy*.
