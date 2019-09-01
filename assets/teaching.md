---
Layout: post
mathjax: true
comments: true
title:  "The scrubland manifesto"
categories: [Maths, Teaching]
date:  2019-08-03
---

**August 13, 2019.** *In the 21st century, higher-order mathematical
  skills are more important than ever before, but high school maths
  classes are dull, alienating and disempower students. How do we improve them, and plug some
  of the holes in the pipeline? I propose we make maths interesting! I
  illustrate this approach with differentiation.*

### Contents

1. <a href="#sec-1">Stuck in the scrubland</a>
   1. <a href="#sec-1-1">A preamble</a>
   2. <a href="#sec-1-2">A patch of scrubland</a>
   3. <a href="#sec-1-3">Shrubs and maximin</a>
   4. <a href="#sec-1-4">Roads to nowhere</a>
2. <a href="#sec-2">Views of the summit</a>
   1. <a href="#sec-2-1">The mean value theorem</a>
   2. <a href="#sec-2-2">A kink in the argument</a>
   3. <a href="#sec-2-3">Slice of pi</a>
3. <a href="#sec-3">Mining for patterns</a>
   1. <a href="#sec-3-1">Sublime moth balls</a>
   2. <a href="#sec-3-2">Irodov's triangle</a>
   3. <a href="#sec-3-3">Slopes and sand piles</a>

## 1. Stuck in the scrubland <a id="sec-1" name="sec-1"></a>

In high school, I was one of those kids.
I thought maths class was about as boring as watching paint
dry, except that a fresh coat of paint can in some cases be useful
and add a bit of colour to the world.
I harboured no such illusions about mathematics.
Would I use trigonometry on my tax returns?
Or solve simultaneous equations at the supermarket?
Finding $x$ was somebody else's business.
I scraped by with passes, aping textbook examples and cramming for
tests, but maths class was a meaningless game with rules I didn't need
to know beyond the next quiz.
The situation was so bad that, at age 15, I remember realising that I
didn't know how to add fractions or multiply negative numbers.
I had just never internalised those rules.

A few years later, taking a philosophy course, I
encountered set theory for the first time.
It totally blew my gourd.
First of all, there was this wonderful paradox of Bertrand Russell about
the set of all sets which don't contain themselves.
Is this big set a member of itself or not?
If it is a member of itself, by definition it's not a member of
itself; and if it's not a member of itself, by definition it is a
member of itself.
Neither can be true, so the big set can't exist without breaking the universe.
This is more than a novelty; Russell's paradox can be jerry-rigged into an
argument that there are different sorts of infinity!
This is the sort of power that philosophers, using mere words, could
only dream of.
I saw that maths could be deep and bewitchingly strange.

At the same time, I was reading pop science books about physics,
fun things like relativity, black holes and quantum mechanics.
These pop science books were great, filled with pictures and metaphors
and colourful examples.
But I began to suspect that I was missing something, and that to
really get to the bottom of things, I would need to know some mathematics.
To paraphrase Galileo, if I wanted to speak with the universe, to
become "conversant", then I needed to learn its language, which seemed
to be maths and not colourful analogies.
Eventually, I switched from philosophy to maths and physics and never
looked back.

I was lucky, stumbling later in life onto a hidden realm of
extraordinary beauty and power.
But how many students are unlucky?
How many go through high school, numbed by repetition, cramming and
copying just enough to pass tests, never seeing that there's a
mathematical world out there, which happens to exquisitely describe
the real world?
The problem, I'll argue, is that maths education is stuck in a sort of
*scrubland* with no views into this enchanted realm.

##### 1.1. A preamble <a id="sec-1-1" name="sec-1-1"></a>

To make the problem more vivid, imagine a
 reality where, instead of maths, you were forced to take *hiking classes* in high school.
Every day, you and your classmates would trudge through a barren,
featureless scrubland, with no views, no peaks, and no apparent goal
other than the hike itself.
Whenever the class complained that the walk was boring or pointless
(and who hikes in real life anyway?) the teacher would recite the
dictum that *walking was an important life skill*.
Heck, if you can't walk, how do you expect to get a job!
Privately, teach had to admit: two monotonous hours in the
scrubland, every day for six years, did seem excessive.
But that's just the way things things were done.

<figure>
    <div style="text-align:center"><img src ="/images/posts/scrubland.png"
    width="100%" />
		    <figcaption><i>The scrubland, far from the mountains of real mathematics.</i></figcaption>
	</div>
	</figure>

Would you have enjoyed this hiking class?
Or would you have lost interest and started lagging behind?
Maybe, in time, you would have come to proudly identify as a bad hiker.
The problem with these classes is clear.
For most of us, walking is not an intrinsically interesting
activity; there needs to be a motivation to walk, something to walk
towards or to look at en route.
That's what *hiking* proper is all about.
But if there's no motivation, it becomes a chore, and rather than being trained to
hike, you will be trained to *avoid hiking*.

Why have hiking classes anyway?
Why don't we ditch the hikes, and teach students how to walk to the
corner store, the bus stop, or around the block with a dog in tow, the
sort of walking most adults actually do?
This would have made sense a hundred years ago.
But let's imagine that there's now a whole sector of the economy which
depends on advanced hiking
skills, a need for wayfarers, explorers and hunters to meet the
needs of society as a whole.
We need hiking classes to act as an intake mechanism, drawing students
into the field and equipping them to explore.

Some students seem to have a natural yen for walking.
They can walk faster, and for longer distances; some hike outside of
class, run the school club, and participate in competitions.
Maybe we should channel our resources towards these "natural walkers"
and let the rest opt out.
But walking is a skill that can be developed, and most of these
"natural walkers" are in fact *motivated by non-scrubland experiences*.
Their parents took them out into nature, or they read about inspiring
walks in a book with pictures, something like the pop science books I mentioned.
They don't visit the scrubland in their free time!
These non-scrubland experiences, rather than natural ability, pushed
them to develop their walking skills.

The fix is clear: we should stop marching students through the scrubland.
Instead, we should guide them into varied and stimulating terrain,
through forests, along canyons, and towards the strange rock
formations in the distance.
With time, they could learn to camp in the wilderness, explore
uncharted wastes and conquer summits.
I think interest would blossom in unexpected places.
By going on real hikes, we would stop wasting student time, improve
social outcomes by attracting more students into the hiking sector, and
perhaps most importantly, show them that there's a whole world out
there, waiting to be relished and explored.

##### 1.2. A patch of scrubland <a id="sec-1-2" name="sec-1-2"></a>

The analogy to maths education and its shortcomings is fanciful but hopefully clear.
Walking is the ability to manipulate
symbols.
Some people are naturally drawn to playing with symbols, some people
aren't.
But maths is not symbol manipulation any more than hiking is walking!
Manipulating symbols is *how* mathematics is done, but it's not *why* we
do it.
And like walking, symbol manipulation is a skill that can be developed.

Then again, if you look at most high school textbooks, you could be forgiven for thinking otherwise.
What should be a journey into
the mathematical world is, in most cases, a joyless plod through a
scrubland without context, without use, and without beauty.
Here's a patch of scrubland, courtesy of an anonymous Australian textbook:

<figure>
    <div style="text-align:center"><img src ="/images/posts/specialist1.png"
    width="80%" />
		    <figcaption><i>Calculus "shrubbified".</i></figcaption>
	</div>
	</figure>

The topic is calculus, one the great milestones of Western thought.
And here, we're finding... rates of change of ... some functions, I
guess.
What do these functions do?
Who is inverse sine on a Saturday?
Why do I care?
These questions are unforgivably dull when there is literally hundreds
of years of material to draw on.
I wish I was cherry picking, but we will see below that the rest of the chapter is the same.
This is what I mean by the scrubland: no landmarks, nothing for the eye to latch onto, just an
endless plain of withered, ankle-height shrubs.

##### 1.3. Shrubs and maximin <a id="sec-1-3" name="sec-1-3"></a>

What makes these questions so bad?
To help capture this, I'm going to propose that they fail the **shrub test**:

<span style="padding-left: 20px; display:block">
<i>Would anyone bother to read this in their own time?</i>
</span>

In other words, would they read it, and do the problems, if they
didn't have to in order to pass the next quiz.
If not, you have shrubs, and shrubs kill interest.
No one wants to spend hours looking at shrubs.
If you force them to, you're wasting their time.

The shrub test is a pretty low bar.
All we ask is that *somebody* might conceivably read it for fun.
And this leads to a different failure mode: when questions only appeal
to a minority of students.
I think this is the pedagogical "wisdom" behind the scrubland: write
material which is *uniformly unappealing* so that nobody is left out.
We can all share in the joy of shrubs!

How do we pass the shrub test but remain fair to students?
I think we should borrow some ideas from political theory.
American philosopher
[John Rawls](https://en.wikipedia.org/wiki/John_Rawls) was the 20th century's
pre-eminent theorist of *fairness* in the political context.
Instead of using average utility (roughly, average personal good) as an
organising social principle, he
suggested something called the [**maximin rule**](https://plato.stanford.edu/entries/original-position/#ArgMaxCriTJSec262):
maximise the outcomes for those who are least well-off.
He argued this would lead to a "trickle up" effect where everyone
benefited; from a game theory perspective, maximin (maximising the
minimum outcome) is the right strategy when there is extreme
uncertainty and you can't play the numbers.

Of the various design principle we could adopt, I think the **maximin
test** should supersede the shrub test:

<span style="padding-left: 20px; display:block">
<i>Would the least-engaged students bother to read this in their own time?</i>
</span>

This is extremely stringent, but I think it's right.
Why?
First of all, it's *fair*.
The students who are already already involved and making progress have
a basic level of a particular social good, engagement, that students
on the margins don't. And as Rawls argues for social goods generally, by making
maths engaging, there should be a "trickle up" effect across the
board.
Making maths class more interesting for the least-engaged will make it
more interesting for everyone!

Secondly, teaching is a wildly complex business.
Besides the choice of material (which I'm emphasising here), there's
a whole host of other variables to consider, from pedagogy and lesson planning,
demographics, classroom management, technology,
and so on, which all play a role in the effectiveness of a class.
How do you optimise average student outcomes in this multidimensional
landscape?
It looks intractable for any class which isn't also a research project.
Given the uncertainties, game theory tells us we should focus on
maximising the minimum outcome.
I think the worst outcome is permanently turning students off
mathematics and its sister sciences.
Hence, we should address the students at greatest risk, and leaving
the scrubland is the first step.

##### 1.4. Roads to nowhere <a id="sec-1-4" name="sec-1-4"></a>

Of course, you need to practice walking before you can wander off
into the foothills, armed only with a compass and a sense of adventure.
Similarly, you need to get good at basic manipulations before you can
do really interesting mathematics.
But if we head towards interesting things, and tell the students where
we're headed and all the amazing things they'll be able to see when
they get there, maybe they won't mind practicing.
And this is the real problem: not that students drill, but that *the
scrubland never ends*.
They drill in order to keep drilling.
They study shrubs here, so they can classify some other shrubs down the road.

The truth is that scrubland is easy for everyone but the students.
You don't need to be a good hiker to guide a class through the
scrubland, and if you want to write a textbook, just
fill it with lifeless, shrub-like variants of the same problem,
sprinkled from that bag of shrub seeds you got at the nursery.
But the responsibility for getting us out of the scrubland doesn't lie
with teachers, or even textbook writers, but the people who write the curriculum.
And from their perspective, it's much easier to maintain the
scrubland, and maybe ride around in a pickup truck painting shrubs different
colours, than to chart a new course into the mathematical world.
I'll talk later about efforts at curricular reform, but the bottom
line is that it takes time, money, and vision, and these are
perennially in short supply.

But as in the hiking analogy, good mathematical skills are important to society as a whole.
I'm not talking about basic numeracy, e.g. the ability to calculate a
tip or scale up a recipe.
I'm talking about dealing with the ongoing effects of climate change,
big data, artificial intelligence, or personalised medicine, issues which
call for explorers with higher-order hiking skills and a taste for the unknown.
The stakes couldn't be higher.
Curriculum writers need to get out of their pickup trucks,
drop their paintbrushes, and start talking to professional hikers, people who
know the landscape and use the trails.
Together, they can move mathematics out of the scrubland, and into the 21st
century with all its challenges and complexities.

## 2. Views of the summit <a id="sec-2" name="sec-2"></a>

I want to suggest two directions out of the scrubland.
The first direction is *pure mathematics*, towards
abstraction, generalisation, proof, and most importantly, *beauty*.
Aesthetic considerations are famously important to pure mathematicians.
The philosopher [Bertrand Russell](https://en.wikipedia.org/wiki/Bertrand_Russell) said that pure maths had a "beauty cold
and austere, like that of sculpture", and was "capable of a stern
perfection such as only the greatest art can show".
English mathematician [G. H. Hardy](https://en.wikipedia.org/wiki/G._H._Hardy) elevated this to a *requirement*,
stating that "beauty is the first test: there is no permanent place in the world
for ugly mathematics."

Sound like any high school maths class you ever took?
It's almost as if people got the Hardy quote backwards: there seems to
be no permanent place in the classroom for *beautiful* mathematics.
Let me show you what passes for pure mathematics in our advanced
textbook:

<figure>
    <div style="text-align:center"><img src ="/images/posts/specialist2.png"
    width="80%" />
		    <figcaption><i>Painting shrubs blue.</i></figcaption>
	</div>
	</figure>

This looks different from the earlier patch of scrubland until you
notice these are more or less the *same* questions with letters
replacing numbers. The shrubs are painted blue, but they are still
shrubs.

Instead of dressing up shrubs, we should find a mountain to scale.
Now, some mountains can only be scaled by professionals.
But we don't always need to scale a mountain to appreciate important
results; with a bit of ingenuity, we can usually find a nearby hill
with a gentler slope and a partial view of the summit.
In pure mathematics, mountains are things like theorems (important
proven results), conjectures (important unproven results), and non-trivial examples.
"Important" and "non-trivial" mean a variety of things, but as Hardy and
Russell suggest, *beauty* is perhaps the principal criterion.
Beauty in maths, as in art, is subjective, so we are left with the enviable
task of choosing *multiple beautiful things* for students to look at.
Hopefully one of them sticks!

Since we have spent a little time looking at calculus, I will
illustrate a way out of the scrubland here: a neat little summit of
generalisation called the *mean value theorem*; a monster dwelling in
the badlands called the *blancmange function*; and finally, a much
nobler use of inverse sine to provide a scheme for approximating $\pi$.

##### 2.1. The mean value theorem <a id="sec-2-1" name="sec-2-1"></a>

Our first example will be the *mean value theorem* (MVT).
Instead of scaling the mountain and giving a fully rigorous proof, we
will content ourselves with a good prospect from lower elevations
using heuristics and visual aids.
Suppose we have a function $f(x)$ defined for $a \leq x \leq b$.
This is pictured on the Cartesian plane below.

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt1.png"
    width="60%" />
		    <figcaption><i>Graphing a function $f(x)$ for $a \leq x
    \leq b$.</i></figcaption>
	</div>
	</figure>

Now draw a line between the endpoints of the graph.

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt2.png"
    width="60%" />
		    <figcaption><i>Drawing a line (purple) between the endpoints
    of the graph.</i></figcaption>
	</div>
	</figure>

What happens if we shift the purple line (without tilting) up or down?
In this example, there are two shifts where the line *just touches* (is tangent to)
the curve.

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt3v2.png"
    width="60%" />
		    <figcaption><i>There are two points at which the line just
    touches the curve.</i></figcaption>
	</div>
	</figure>

Is it possible to draw a different graph so the purple line is tangent
at *one* point?
If you give students some time to experiment, they should find
examples like the following:

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt4.png"
    width="60%" />
		    <figcaption><i>An example where the purple line is tangent
    at a single point.</i></figcaption>
	</div>
	</figure>

What about *no points* where the graphs are tangent?
With some time to play around, students should come to doubt that such
curves exist.
How can they prove it?
One approach lies in the definition of "just touching".
Imagine zooming in infinitely close to the point of tangency, so the blue curve becomes
straight (more or less what we mean by the derivative).
You can convince students that the blue and purple lines
must have the *same slope* at this point of intersection.
If they had different slopes, they would cross each other rather than
being tangent!

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt5.png"
    width="35%" />
		    <figcaption><i>At infinite magnification, the purple and
    blue lines must coincide.</i></figcaption>
	</div>
</figure>

This suggests a visual proof, which students could discover for
themselves with a little guidance.
First of all, it's clear that some of the blue curve should lie above
the purple line, or below the purple line, otherwise it *is* the
purple line and we have (infinitely) many points of tangency.
But let's assume that some of the blue curve lies below the original
purple line.
Now, move the purple line down until it can't go further without
missing the blue curve altogether.
If the purple line wasn't tangent to the blue at this extreme point,
the blue would cross *through* the purple and we could continue moving
it down.
From our earlier discussion, this means they have to be tangent!

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt6.png"
    width="65%" />
		    <figcaption><i>A visual proof that
    the translated purple line is tangent to the blue curve.</i></figcaption>
	</div>
	</figure>

Since the purple line is straight, we can easily calculate
its slope:

$$
\text{slope} = \frac{\text{rise}}{\text{run}} = \frac{f(b)-f(a)}{b-a}.
$$

For a function $f(x)$ on $a\leq x \leq b$, there is a point $c$ where
the derivative equals the "mean" slope between its endpoints:

$$
f'(c) = \frac{f(b)-f(a)}{b-a}.
$$

This statement is the MVT!
A nice feature of our proof is that (combined with root-finding
methods) it can be turned into an algorithm for finding the point $c$.
We didn't need real analysis or anything fancy, just some pictures and
a solid feeling for what the definitions *mean*.

Let's return to inverse sine, and see if we can do better than
palette-swapped shrubs.
With the MVT in hand, students can prove it always increases the
distance between its arguments:

$$
|\sin^{-1}(x) - \sin^{-1}(y)| > |x-y|,
$$

assuming $x \neq y$, since the derivative $f'(c) = 1/\sqrt{1-c^2} > 1$.
This elegant and nontrivial result is pictured below.

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt12.png"
    width="70%" />
		    <figcaption><i>The MVT implies inverse sine is distance-increasing.</i></figcaption>
	</div>
	</figure>

Here's a more practical application: *cheap traffic enforcement*.
Suppose traffic police monitor a stretch of highway of length $L$.
They clock a car entering the stretch and leaving a time $T$ later.
Without using a radar gun, they know from the MVT (see graph below) that the car was
travelling at speed $v = L/T$ at some point along the stretch.
If this is greater than the speed limit, they can issue a fine!

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt13.png"
    width="63%" />
		    <figcaption><i>The MVT replaces a radar gun
    with a watch.</i></figcaption>
	</div>
	</figure>

##### 2.2. A kink in the argument <a id="sec-2-2" name="sec-2-2"></a>

As fun as the MVT is to prove, it's even more fun to break.
If the students draw a sharp kink in the curve, they will find that the theorem fails:

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt7.png"
    width="60%" />
		    <figcaption><i>The proof fails for "kinks".</i></figcaption>
	</div>
	</figure>

Although the blue curve lies entirely on one side of the
purple line, the two never coincide, even when we zoom in.
Put a different way, since the tangent to the blue curve isn't even
well defined, it cannot equal the purple line!
This places an important technical constraint on the mean value
theorem: at every point, the curve must be differentiable, aka
*straight at infinite zoom*.

We could leave it there, but for kicks, let's try and *maximally
break* the theorem.
In the single-kink case, we can simply shift on the endpoints to
define the function on a subinterval $a' \leq x \leq b'$ where the
mean value theorem *does* hold. We just avoid the kink!

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt8.png"
    width="60%" />
		    <figcaption><i>Shifting an endpoint to avoid the kink.</i></figcaption>
	</div>
	</figure>

So here is the challenge: define a continuous curve where the
mean value theorem is not applicable in any subinterval.
Since we can apply the theorem to any subinterval
without kinks, we need *every subinterval to contain a kink*.
In technical parlance, the kinks must be *dense* in $[a, b]$.

It's hard to imagine (or draw) an infinitely jittery curve.
But it's easier if we proceed step-by-step.
First, let's set $a = 0$ and $b= 1$; we lose nothing by making this
choice, since we can always scale and shift our answer to recover the
result for an arbitrary interval.
We can start with a trangle-shaped function possessing a single kink at $x =
1/2$, though most functions with a single kink will do.
For the triangle, we can apply the MVT to any subinterval entirely to the left of the midpoint,
or entirely the right of the midpoint.
Call these intervals, where the MVT applies, *good subintervals*.
They have maximum length $1/2$.

Our strategy will be to iteratively add kinks, and reduce the length
of good subintervals by half each time, until they disappear altogether!
To begin with, let's place kinks at $x = 1/4, 3/4$ so that the
maximum length is $1/4$.
A simple way to do this is to *scale down* the triangle function by a
factor of 2, put two copies side by side, and add them to the big
triangle, as depicted below.
We label steps in the process by $n$, with $n = 0$ the big triangle
with a single kink, and $n = 1$ the sum of big triangle and two
smaller triangles.

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt9.png"
    width="90%" />
		    <figcaption><i>Baking a blancmange.</i></figcaption>
	</div>
	</figure>

We can repeat this to obtain the $n = 2$ curve, shrinking the big
triangle by a factor of $4 = 2^2$, making four copies, and adding to the $n = 1$ result.
Now the maximum length of a good subinterval is $2^{-3} = 1/8$.
Continuing in this fashion, at step $n$, we shrink the original triangle by a factor of $2^n$,
spam $2^n$ copies, and add them to the results of the previous step.
This iteratively builds up a fractal called the *blancmange function*,
since it resembles the jellied mounds of the French dessert.

Good subintervals have maximum length $2^{-(1+n)}$.
As $n$ gets larger and larger, this allowed length gets smaller and smaller, and in the limit
$n \to \infty$, they have no length at all!
Informally, this shows that for the blancmange function, there are no good subintervals.
To make this slightly neater, we can label with their "decimal"
expansions in base 2.
The initialy kink is at $x = 0.1$.
The kinks for $n = 1$ are at $x = 0.01, 0.10, 0.11$.
The kinks for $n= 2$ are at

$$
n = 0.001, 0.010, 0.011, 0.100, 0.101, 0.110, 0.111.
$$

You get the idea: at stage $n$, there are kinks at all numbers $x\in
(0, 1)$ with binary expansions of length $n+1$.
In the limit $n \to \infty$, there will be a kink at every number $x
\in (0,1)$ with a finite binary expansion.
Like the finite decimal expansions we are used to working with, these
binary expansions are indeed dense in the reals.

There are a few loose ends here.
First, there is the question of *pointwise convergence*: is the
blancmange function well-defined?
If the students know the geometric series and the comparison test,
they can prove this.
A more delicate question is whether the function is *continuous*,
requiring the [M-test](https://en.wikipedia.org/wiki/Weierstrass_M-test).
In a classroom setting, I think it's probably best to raise both
problems, but answer them "experimentally": simply graph the function
at different values of $n$, or get the students to program it
themselves.
They should see the function settle down to something continuous as as $n$ gets large.
(See [this Geogebra applet](https://www.geogebra.org/m/BTRh89uH)
by David Richeson for example.)
This is not a proof, but it does give a convincing numerical
demonstration both of convergence and continuity.

Another question is why we bother *adding* the triangles.
Why don't we just take the limit of small triangles spammed together?
This will have kinks at the same places as the blancmange.

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt10.png"
    width="70%" />
		    <figcaption><i>The limit of spammed triangles is a straight
    line.</i></figcaption>
	</div>
	</figure>

It turns out that an infinitely small triangle is just a
point, and $2^n$ small triangles make a *line* as $n\to\infty$.
The technical tool to prove this is the
[Hausdorff limit](https://en.wikipedia.org/wiki/Hausdorff_distance) of
sets, but a simple intuition pump is simply to ask: how tall are the
triangles as $n\to\infty$?
If $f_n$ is the function consisting of $2^n$ triangles scaled down by
$2^n$, what is the value of $f_n(x)$, for any $x$, as $n$ gets large?
Everything just gets squished onto the red line.

To summarise, the blancmange function is *continuous but nowhere
differentiable*, and a similar iterative construction for any single-kink curve
gives a function with the same property.
Some students will savour this pathological dessert, while others will not.
The latter will be in good company; mathematician
[Charles Hermite](https://en.wikipedia.org/wiki/Charles_Hermite), for 
instance, wrote: "I turn with terror and horror from this lamentable
scourge of functions with no derivatives".
But the moral is that, by trying to break theorems, ask bold
questions, and follow loose
threads, we often find something amazing lurking in the undergrowth.
In their own way, monsters can be beautiful.

##### 2.3. Slice of pi <a id="sec-2-3" name="sec-2-3"></a>

I'll do one more example, unrelated to the MVT, but returning to inverse sine and its derivative.
This requires a little more symbolic facility from students, but the
payoff is a beautiful infinite series identity.
I think infinite series are one of the great propaganda tools for
calculus, and deserve a greater place in the high school syllabus.
When I first encountered them, I was astounded: they were beautiful
but otherworldly, like a glittering chunk of meteorite found in the middle
of a corn field.
For instance, how could the formula

$$
\frac{\pi^2}{6}  = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \cdots
$$

possibly be true? And who could dream up a gewgaw like

$$
\frac{1}{\pi} = \frac{2\sqrt{2}}{9801}\sum_{n=0}^\infty
\frac{(4n)!(1103+26390n)}{(n!)^4 396^{4n}},
$$

which [Ramanujan](https://en.wikipedia.org/wiki/Srinivasa_Ramanujan)
seemed to do on a daily basis?

Although Ramanujan's work still strikes me as
semi-mystical, many results on infinite series, equally baffling and exciting to
the outsider, are easy pickings with the long arm of calculus.
In our case, we'll cook up an infinite series for $\pi$ based on the
inverse sine.
First, recall the derivative:

$$
\frac{d}{dx} \sin^{-1} x = \frac{1}{\sqrt{1-x^2}}.
$$

The RHS can be expanded using the
[binomial series](https://en.wikipedia.org/wiki/Binomial_series) discovered by [Isaac Newton](https://en.wikipedia.org/wiki/Isaac_Newton):

$$
(1-x^2)^{-1/2} = 1 + \frac{1}{2}x^2 + \frac{1\cdot 3}{2\cdot 4} x^4 +
\cdots = \sum_{n-0}^\infty
\frac{(2n)!}{2^{2n}(n!)^2} x^{2n}.
$$

Is this too advanced for students?
I don't think so.
It can be motivated as an extension of the usual binomial theorem, and
"proved" (without worrying too much about convergence) via the
[Maclaurin series](https://en.wikipedia.org/wiki/Taylor_series):

$$
(1+x)^\alpha = \sum_{n=0}^\infty \binom{\alpha}{n} x^n, \quad
\binom{\alpha}{n} = \frac{1}{n!}
\frac{d^n}{dx^n}(1+x)^\alpha\big|_{x=0} =
\frac{\alpha\cdot(\alpha-1)\cdots (\alpha-n+1)}{n!}.
$$

Now "anti-differentiate" term-by-term:

$$
\sin^{-1}x = x + \frac{1}{2}\frac{x^3}{3} + \frac{1\cdot 3}{2\cdot 4} \frac{x^5}{5} +
\cdots = \sum_{n-0}^\infty \frac{(2n)!}{2^{2n}(n!)^2} \frac{x^{2n+1}}{2n+1}.
$$

Here, the constant of integration is set to zero since inverse sine
vanishes at $x = 0$.
Finally, we plug in a specific value, $x = 1/2$:

$$
\sin^{-1}(\tfrac{1}{2}) = \sum_{n-0}^\infty \frac{(2n)!}{2^{2n}(n!)^2}
\frac{1}{2^{2n+1} (2n+1)}.
$$

So what? Well, we know from "special triangles" that $\sin^{-1}(1/2) = \pi/6$.
This yields the pleasing formula

$$
\pi = 6\left[1 + \frac{1}{2}\left(\frac{1}{3\cdot 2^3}\right) + \frac{1\cdot
3}{2\cdot 4}\left(\frac{1}{5\cdot 2^5}\right) + \frac{1\cdot 3 \cdot 5}{2\cdot 4\cdot
6}\left(\frac{1}{7\cdot 2^7}\right) + \cdots\right].
$$

As students can check themselves, this formula converges extremely
rapidly.
Below, I've plotted the first six partial sums.

<figure>
    <div style="text-align:center"><img src ="/images/posts/pi-inverse-sine.png"
    width="70%" />
		    <figcaption><i>The series converges to π ≈ 3.14 rapidly.</i></figcaption>
	</div>
	</figure>

Newton derived this formula (using geometry rather than calculus) and
exploited the rapid convergence to compute $\pi$ to $15$ decimal
places in 1666.
He later wrote, "I am ashamed to tell you to how many figures I carried these
computations, having no other business at the time."
Students can reproduce this feat themselves!
In fact, you can explore precisely *how many* terms are needed for a
given number of digits.

<figure>
    <div style="text-align:center"><img src ="/images/posts/pi-inverse-sine-2.png"
    width="77%" />
	</div>
	</figure>

For $15$ decimal places in $\pi$, you need only $19$ terms in the
sum.
More generally, the relationship between terms and decimal places is
*linear*, as the graph above shows.
You can get students to fit a line and predict how many terms they
need for, say, the first $1000$ digits.
They can add up terms and check that it's right!

To derive Newton's formula for $\pi$, we have thrown rigour to the
wind.
As with the blancmange, I think it is worth mentioning the convergence
issues at play (power series radius of convergence, uniform
convergence for term-by-term differentiation) without belabouring them.
On a first exposure, a quagmire of technical conditions will spoil the magic!
A numerical check can be just as convincing.

Is this pedagogically sound?
I find the hiking analogy helpful here.
Rigour is something like a heavy *safety harness* for mountain climbing.
From the sheltered vantage of our hill, we can mention rigour and explain
why the professional climbers need it, but do not ourselves need to
gear up.
There are other ways to orient students in the landscape and protect
them from misadventure.
That said, I see no reason that an advanced class should not try
climbing a mountain here or there, and prepare accordingly.

## 3. Mining for patterns <a id="sec-3" name="sec-3"></a>

A second direction out of the scrubland is *applied mathematics*,
understood broadly as the use of mathematics to solve problems in the
real world.
Unlike beauty, which never gets much of a rhetorical look in, the term
"real world" is bandied about almost recklessly by maths teachers.
In particular, the "real world" is the home (or perhaps graveyard) of *word problems*.
Here are some examples from our textbook:

<figure>
    <div style="text-align:center"><img src ="/images/posts/specialist3.png"
    width="80%" />
		    <figcaption><i>Problems from the real world?</i></figcaption>
	</div>
	</figure>

We have a shrinking moth ball, a growing triangle, and sand being
poured into a conical pile.
This is promising subject matter: objects in the real world
which change with time.
But nothing passes the shrub test!
Why does the moth ball decrease at a constant rate?
What causes the triangle to get bigger?
Why is the conical angle of the sand pile precisely $71.57^\circ$?
We're now in a Dalí-esque scrubland of random objects.

Maths comes from the real world, and we should connect
students to its living, breathing sources of inspiration and
application.
They should see where it all comes from!
In the same way that the material needs of civilisation spur an explorer
and frame her quest, the needs of science, industry, and
everyday life spur mathematicians to go out into the landscape and dig
up patterns fit for purpose.
From compound interest to chaos, planetary motion to poker, and soap bubbles to
ciphers, mathematics arises from real world needs.
Why not let students in on the secret?

There is an even grander secret.
*Almost everything* has pattern and structure on which mathematical
tools can be brought to bear.
For maximum rhetorical impact, I'm going to show this by redoing each
of the three calculus word problems above.
Afterwards, I'll comment on the somewhat obvious tension with the
maximin test.

##### 3.1. Sublime moth balls <a id="sec-3-1" name="sec-3-1"></a>

We start with moth balls, adapting and simplifying the lovely article by
[Tennakone and Pieris (1978)](https://eric.ed.gov/?id=EJ180235).
We'll see how the size of spherical moth balls really changes with
time.
Students can use this information to experimentally determine
microscopic properties of air, just by waiting for a moth ball to decay!

<figure>
    <div style="text-align:center"><img src ="/images/posts/moth-ball2.png"
    width="70%" />
		    <figcaption><i>A moth ball generates a cloud of napthalene
    as it sublimes.</i></figcaption>
	</div>
	</figure>

Moth balls are made out of a chemical called napthalene
($\text{C}_{10}\text{H}_8$).
A sphere of napthalene will shrink as the molecules on the surface
layer *sublime*, i.e. turn directly from solid to gas.
Assuming the rate of sublimation is uniform over the surface, the moth
ball remains approximately spherical.

The sublimed napthalene forms a spherical cloud of gas around the moth
ball, spreading outward or *diffusing* due to the random motion of the molecules.
Let $c(r)$ be the concentration of gas (number of
molecules per unit volume) around the ball, defined as a function of
radial distance $r$ from the ball's centre.
For a very thin spherical shell of width $w$ (where $c$ is effectively
constant over the shell), the rate at which molecules diffuse out of
the shell is proportional to the concentration $c(r)$ and the velocity $v$.

---

1. Consider two thin shells, one at radius $r$ and another at
    radius $r + w$.
	Assuming the velocity of molecules is fixed for all shells,
    explain why the *net* rate $F$ of molecules leaving the
    second shell (at radius $r+w$), per unit area, is proportional to

   $$
   F(r+w) \propto \frac{c(r+w)-c(r)}{w}.
   $$

2. By taking the limit of zero width, show that the
   net outward flow of molecules from the shell at radius $r$, per
   unit area, is

   $$
   F(r) = D \frac{dc(r)}{dr},
   $$

	where $D>0$ is a constant of proportionality called the *diffusion
    constant*.

3. Suppose the napthalene cloud diffuses very slowly, with a steady
   outward flow of molecules. Argue that, for this steady flow, the function

   $$
   G(r) = 4\pi r^2 F(r)
   $$

   must be constant.

4. Let $R$ be the radius of the moth ball. From Problem 3, deduce that

   $$
   c(r) = \frac{c(R) R}{r}.
   $$

	Since the rate of sublimation is uniform, the concentration $c(R)=
    c_\text{sub}$ at the surface of the moth ball is *independent* of $R$.

5. Since the moth ball is gradually turning into gas, the radius
   $R(t)$ depends on time.
   It is a little easier to calculate how the *mass* of the ball changes
   with time.
   Show that if $m_\text{N}$ is the mass of a napthalene molecule, and
   $M$ the mass of the moth ball, then

   $$
   \frac{dM}{dt} = -m_\text{N}G(R) = -4 \pi m_\text{N} c_\text{sub}D R.
   $$

6. If $\rho$ is the mass density of the moth ball, show that we can
   rewrite the rate of change of mass in Problem 5 as a rate of change
   of radius:

   $$
   \frac{dR}{dt} = -\frac{D c_\text{sub} m_\text{N}}{\rho R}.
   $$

7. By explicit differentiation, check that the equation in Problem 6
   is solved by

   $$
   R(t) = \sqrt{R_0^2 - \left(\frac{2D c_\text{sub} m_\text{N}}{\rho}\right) t}.
   $$

	where $R_0$ is the radius at time $0$.
	Infer that the lifetime of the moth ball is

   $$
   t_\text{life} = \frac{\rho R_0^2}{2D c_\text{sub} m_\text{N}}.
   $$

8. (Experiment) A single molecule of napthalene weighs around
	$m_\text{N} = 2.1 \times 10^{-22} \text{ g}$.
	At room temperature, the surface concentration of napthalene is
	$c_\text{sub} = 3.3 \times 10^{22} \text{ m}^{-3}$.
    Buy some moth balls, and measure their initial radius $R_0$ and
	density $\rho$.
    Leave them in a cool dry place and see how long they take to
	disappear, i.e. determine $t_\text{life}$.
	From Problem 7, estimate the diffusion constant for napthalene in air.

----

##### 3.2. Irodov's triangle <a id="sec-3-2" name="sec-3-2"></a>

Our next problem elaborates on a classic pursuit puzzle, first posed
in [Igor Irodov's](https://en.wikipedia.org/wiki/Igor_Irodov)
[*Problems in General Physics*](https://archive.org/details/IrodovProblemsInGeneralPhysics)
and later
[popularised](http://www.cambridgeblog.org/2008/10/win-a-new-martin-gardner-book-5/)
by [Martin Gardner](https://en.wikipedia.org/wiki/Martin_gardner).
Three homing missiles $M_1, M_2, M_3$ are fired at each
other from the vertices of an equilateral triangle.
The triangle has side $\ell$, and missile $M_1$ homes in on $M_2$, $M_2$ on $M_3$, and
$M_3$ on $M_1$.

<figure>
    <div style="text-align:center"><img src ="/images/posts/missiles.png"
    width="68%" />
		    <figcaption><i>Three homing missiles lock onto each other
    and eventually collide.</i></figcaption>
	</div>
	</figure>

Assume the missiles move have the same speed profile over time, $v_1(t)=v_2(t)=v_3(t)=v(t)$.
The *danger zone* is the triangle formed by three missiles.
This is where you might get hit!

#### Part I: Meeting in the middle
----

1. Argue that the danger zone (pictured above) is always an equilateral triangle.
   
2. Using Problem 1, explain why the missiles always point in
   directions separated by angle $\theta = 2\pi/3$.

3. From Problem 2, show that the relative speed at which $M_1$ and
   $M_2$ approach each other is

   $$
   v_{12}(t) = [1 - \cos\theta]v(t).
   $$

4. How far does each missile travel before colliding at the centre?
   (No calculus needed.)

5. Extending your observation in Problem 4, explain why the paths
   traced by the missiles do not depend on their velocity (provided
   the speed profiles agree).

6. (Extension) Generalise your result to $n$ homing missiles on the vertices of an
    equilateral polygon, with $n$ sides of length $\ell$.
	What happens in the limit as $n\to\infty$?
	Does you answer make sense?

----

The fact that the danger zone remains equilateral tells us a beautiful
fact about the path of the missiles: it is *self-similar*, in the
sense that as we zoom in, the shape is the same.
Set up polar coordinates $(r, \phi)$ with the origin at the centre of
the danger zone.
A path $r = f(\phi)$ in polar coordinates is self-similar if
zooming in (multipling $r$ by a constant) only shifts the angle:

$$
\begin{equation}
\alpha r = f(\phi - c),\label{self}
\end{equation}
$$

where $c = c(\alpha)$ depends on $\alpha$.
This allows us to actually work out the curves!

#### Part II: Self-similar spirals
---

6. Differentiate both sides of (\ref{self}) with respect to $\alpha$,
    and set $\alpha = 0$, to find that

   $$
   f(\phi) = -f'(\phi) c'(0).
   $$

7. Verify directly (or solve a separable DE to show) that this
   equation is
   solved by

   $$
   f(\phi) = C e^{-c'(0)\phi}
   $$

   for some constant $C$.
   Thus, any self-similar curve in polar coordinates takes the form of
   a *logarithmic spiral*,

   $$
   r = C e^{-k\phi},
   $$

   for constants $C$ and $k$.

8. Choose coordinates so that the missiles initially lie at angles
    $\phi = 0, 2\pi/3, 4\pi/3$.
	Show that the curve associated to the first missile (at $\phi =
    0$) is a logarithmic spiral with $C = \ell/\sqrt{3}$ and $k =
    \sqrt{3}$.
	The remaining two curves are simply rotated by $\pm 2\pi/3$ around the
    origin.

    *Hint*. The derivative $r'(\phi)$ at $\phi = 0$ tells us the
    direction the missile points.

9. (Extension) Determine the spirals for a polygon of $n$ homing missiles.

---

This problem is beautiful because symmetry (rotational and scaling)
solves the problem for us.
We still need derivatives, but they now have the nontrivial role of
extracting the
[logarithmic spiral](https://en.wikipedia.org/wiki/Logarithmic_spiral)
from self-similarity, and determining parameters for the path of
the missiles.
Swiss mathematician
[Jacob Bernoulli](https://en.wikipedia.org/wiki/Jacob_Bernoulli)
called this curve the *spira mirabilis* ("marvellous spiral") since he
was so struck by its property of self-resemblance.
His gravestone even bears the enigmatic Latin reference

<span style="padding-left: 20px; display:block">
<i>Eadem mutato resurgo.</i>
</span>

This translates to "Although changed, I shall arise the same".
In a carving snafu, an Archimedean ($r = C\phi$) rather than a logarithmic
spiral was inscribed next to it!

##### 3.3. Slopes and sand piles <a id="sec-3-3" name="sec-3-3"></a>

Our final redo is the sand pile, taking inspiration from "Dynamical
models for granular matter" by
[Hadeler and Kuttler (1999)](https://link.springer.com/article/10.1007/s100350050029).
A pile of sand has two components: a *standing layer*, which is the
large blob of stable sand at the bottom of the pile, and a *rolling
layer* of loose grains running down the slope.

<figure>
    <div style="text-align:center"><img src ="/images/posts/sandpile.png"
    width="68%" />
		    <figcaption><i>A sand pile, consisting of a standing layer
    and a rolling layer.</i></figcaption>
	</div>
	</figure>

We work with sand piles in the plane, rather than in three
dimensions. The height of the standing layer is denoted $S$, and the additional
thickness of the rolling layer is $R$.
The total height of the sand pile is then

$$
H = S + R.
$$

The *angle of repose* $\alpha$ is the maximum slope of a stable
sand pile.
If a patch on the standing layer has slope greater than $\alpha$, it
will shed grains into the rolling layer.
If it has slope less than $\alpha$, a rolling layer can deposit
grains onto the pile.

<figure>
    <div style="text-align:center"><img src ="/images/posts/sandpile2.png"
    width="60%" />
		    <figcaption><i>A small patch of sand pile. The
    rolling layer moves to the right at speed $v$, with slope κ defined with
    respect to a horizontal standing layer.</i></figcaption>
	</div>
	</figure>

Zoom in on a patch of sand pile centred at $x$, width $w$, small enough
that both the standing and rolling layer have constant slope, $m$ and
$\kappa$ respectively.
Let's see how the height of the standing layer changes with time. A
reasonable guess is that sand grains move between the layers at a rate
proportional to (a) the current thickness $R$ of the rolling layer,
and (b) the difference between the standing slope and the angle of
repose.
This means we can write the rate of change of $S$ as

$$
\begin{equation}
\frac{dS}{dt} = \gamma r(\alpha - m), \label{ds/dt}
\end{equation}
$$

 for some constant of proportionality $\gamma$ depending on the properties of the sand.
Note that the value of $R$ here is evaluated in the middle
of the patch at $x$, as is the value of $S$.

#### Part I: Simple sand piles

---

1. Assume the density of sand is the same in the standing and rolling layer.
   Explain physically why a change in $S$ doesn't affect the *total* height $H$. 

2. Let $\kappa$ be the slope of the rolling layer, defined as in the
	picture.
	In a short time $\Delta t$ (short enough that $\kappa$ remains
	approximately constant), show that the area of rolling
    sand above our patch changes by $\Delta A = -vw\kappa\Delta t$.

3. Given the result of Problem 1, the only way to change $H$ is for
    the size of the rolling layer to change.
	Show that $H$ is related to the total area of sand above the patch
    by $A = Hw$.

4. Using Problems 2 and 3, argue that the *total* height of the sand pile at $x$ changes according to

   $$
   \frac{dH}{dt} = -v\kappa.
   $$

5. Suppose we begin pouring sand from a bucket into the patch
    at some rate $bw$.
	If this sand starts rolling immediately, show that the change in height becomes

   $$
   \begin{equation}
   \frac{dH}{dt} = -v\kappa + b. \label{dh/dt}
   \end{equation}
   $$

   In this case, demonstrate that the rolling layer in the patch thins out at rate

	$$
	\frac{dR}{dt} = -v\kappa + b-\gamma R(\alpha - m).
	$$

---

The sand pile equations (\ref{ds/dt}) and (\ref{dh/dt}) are hard to
solve in general, and even when you can solve them, they are too
simplistic to capture the behaviour of real sand piles!
Hadeler and Kuttler discuss some improvements to this simple model,
but we'll just try to understand the easiest case.

   <figure>
    <div style="text-align:center"><img src ="/images/posts/sandpile5.png"
    width="45%" />
		    <figcaption><i>Gangue from a copper mine, slowly forming a triangular
    mound.</i></figcaption>
	</div>
	</figure>

The equations apply to any *granular material* made of small, rigid
objects, so they apply just as well to crushed rock as sand.
In a copper mine, ore is crushed to extract the metal, with
the remaining material, or *gangue* (pronounced "gang"), dumped from a chute into a
triangular pile of tailings.
Suppose the tailings sit in the middle of a base of width $B$, with a large drop
to either side limiting the maximum size of the standing layer.
We'll first consider slowly building a triangular standing layer, and
then see how the rolling layer moves over it.

#### Part II: Triangular tailings

---

1. At first, material is dumped from the chute at a constant rate $V$
	(volume per unit time).
	Suppose the triangle forms slowly enough that there is effectively no
	rolling layer, with sides always at the angle of repose $\alpha$.

   (a) If gangue starts piling up at $t = 0$, at what time $t_\text{edge}$ do the sides hit
   the edge of the base?

   (b) Write the profile of the tailings, $H(x, t)$, as a function of time $t$ and position
   $x$ for $t < t_\text{edge}$.

2. After $t_\text{edge}$, any additional gangue will form a
    rolling layer travelling at speed $v$.
	We now focus on the right side of the triangle, since the left side will
    be the same by symmetry.
	Show that when $b = 0$ (away from the chute), the sand pile
    equations imply

	$$
    R(x, t) = R(x - vt).
    $$

	In other words, the height of the rolling layer is not a function
    of position and time independently, but only the combination
    $x-vt$.

	*Hint*. The slope is given by $\kappa = dR/dx$.

3. Consider a point on the rolling layer with *fixed* $\xi=x - vt$.
   Prove that this moves to the right with speed $v$ as time evolves.
   This is the mathematical definition of a *wave*: a profile which,
   over time, translates without changing.
   

4. The chute dumps a small column of gangue, height $C(t)$, onto the
   top of the pile at time $t$.
	Note that, unlike the formation of the stable pile in Problem 1,
   we will now let the height depend on time.
	If the column splits evenly into two cascades down either side of
    the triangle, the initial height of the rolling layer is

   $$
   R(0, t) = \frac{1}{2}C(t).
   $$
   
	Show using the preceding problems that the height profile of the
    tailings is

   $$
   \begin{equation}
   H(x, t) = \left(\frac{1}{2}B - |x|\right) \tan\alpha +
   \frac{1}{2}C(t-|x|/v)\label{tailings1}
   \end{equation}
   $$

    for $|x| \leq B/2$.
	The column height $C(t)$ is a bit like the moving needle on a lie
	detector or a seismograph, tracing a curve on paper moving at
	speed $v$ down the triangle.

5. (Extension) The product $C(t) \, dx$ can be viewed as the volume
    of a very thin column dumped on top of the column at time $t$.
	Show that in (\ref{tailings1}), the volume of gangue is
    *conserved* as it flows down the pile.

6. (Extension) Instead of a triangle, we can increase the dimension and
    consider a cone of tailings at the angle of repose $\alpha$ on a circular base of diameter $B$.
	If it falls precisely at the apex of the cone, the column $C(t)$
    splits into a symmetric *ring* of material that rolls down at speed $v$.
	If $r$ is the radial variable on the plane, with $r = 0$ the
    centre of the tailings, argue from
    conservation of volume that

   $$
   H(r, t) = \left(\frac{1}{2}B - r\right) \tan\alpha +
   \frac{1}{2\pi r}C(t-r/v)
   $$

   for $r \leq B/2$.
   In this case, the rolling gangue spreads as a *circular wave*.

---

According to mathematician [Steven Krantz](http://math.bu.edu/people/changer/teasem/w04.pdf),
there is an infamous MIT exam which simply reads:

<span style="padding-left: 20px; display:block">
You have a pile of warm metal shavings in the shape of a cone. Discuss.
</span>

This may be a ridiculous exam.
But I can think of worse things to write about than the granular dynamics of metal shavings!

## 4. Research <a id="sec-4" name="sec-4"></a>

- Final section on pedagogy. First section on drill, chunking, anxiety, whether my problems really satisfy minimax. Look at jump stuff?
- Second subsec on existing curricular reform.
- Last subsec on (my ignorance of) how best to implement this in a
classroom, discussion of strengths/weaknesses.
- Guided discovery, chunking, anxiety, bonus questions
- "Need to know math well"

##### 4.1. Chunking <a id="sec-4-1" name="sec-4-1"></a>

##### 4.2. The evidence <a id="sec-4-2" name="sec-4-2"></a>

In the US, the
[Common Core](http://www.corestandards.org/wp-content/uploads/Math_Standards1.pdf) math standards
represent a major effort at curricular reform, though the notion of
"real world problem" being used here does not seem to correspond to
what people ordinarily mean by "real world".
The [Australian Council for Education Research](https://www.acer.org/au/) is
[aware of issues with STEM education](https://research.acer.edu.au/cgi/viewcontent.cgi?article=1028&context=policy_analysis_misc),
but the vagueness of the 2018 recommendations suggests that curricular
change is a ways off.

##### The role of the teacher

Adroit guide

##### Active learning and other pedagogical improvements

## References


## Extra

Sure, you can't hike without walking, and you need plenty of practice
if you want to become a good hiker.
The best way to bring students along is to provide motivation, to
provide interest, and to empower them.

Hopefully, by now you've realised this is a thinly veiled analogy for
maths class.
For so many students, it feels like a pointless trudge through a
landscape without interest, without life, which is stuck in the
scrubland, with a guide who can't explain where they're going or why
they're doing it.
I know because that was my experience in high school.

Of course, this is a thinly veiled analogy to high school maths class.
Doing maths, by itself, for itself, is not intrinsically interesting
to most people.
Just like walking, it can get boring quickly.
And hours of math drill, every day, every week, for years, seems like
overkill to develop basic numeracy.
When was the last time you used the quadratic formula on your tax
return?
Or trigonometry to assess the merits of a lease-purchase scheme?
My point is not that trigonometry or the quadratic formula are
useless, but that the stated aim of basic numeracy doesn't match what
we teach in the curriculum.
Clearly, there's some other value system at play.

<span style="padding-left: 20px; display:block">
The eye is the best of artists.
</span>

<div style="text-align: right"><i> Ralph Waldo Emerson</i> </div>

The teacher is going to find it hard to justify.

We would have less carbon dioxide in the air, and perhaps our
culture would be less frantic, less shallow, and more curious.
But if we wanted more people to walk, hiking class

Let's say the teacher is an avid hiker.
Why do they like hiking?
Maybe it's the chance to commune with nature, or to get away from the
bustle of every life.
Perhaps it's the lure of exploration, or the call of that mountain
summit in the distance.
Whatever it is, when a students asks: why are we doing this?

And the students could legitimately object that in the future, I'm just
going to be walking from my house to the my car.
Why do I need to spend hours doing this each week?
Heck, I'm going to avoid jobs that require a lot of walking.

They plan to walk from the house to the car, and from the car to work,
and maybe take the dog around the block every now and again.
A job that requires hours of walking? No thank you!

Without the longer classes, schools
will not produce walkers of the calibre needed to fill those
roles. There are good economic reasons, in this case, to provide
students with opportunities to develop advanced hiking skills.

There may also be benefits to a society where more people hike for
fun. For instance, it would reduce carbon emissions, and might make
for a less frantic, more contemplative culture. This involves some
value judgements, but teachers and curricular authorities are in the
position to make this, and make similar judgements when they put
Shakespeare on the syllabus.

We need to change hiking classes so that walks go through interesting
terrain, from meadows to swamps and valleys to forests; at first, along the comfortable and well-trodden routes. But
by degrees, they should conquer summits, explore uncharted wastes, and
camp in the wilderness.
At the end of the day, hiking is not about the act of walking, but a
way to experience the world. The walking is a means to this end. And
the class will remain a dead letter, pure trudgery, until it gets out
of the scrubland and owns its purpose.

Would you blame most students for losing interest and lagging behind,
and later identifying as people who hated hiking?
Of course not!

Unless they are taught to love hiking, they'll have no thought of
walking for hours every day.
Not to mention if it becomes a joyless chore, in which case they'll do
everything they can to avoid it!

Perhaps, also, there are general cultural benefits when everyone
enjoys hiking, for instance, a higher level of average physical fitness, or a
closer connection to nature.

That makes it easier to motivate the whole enterprise, and less likely
to lead to resentment.

Not everywhere can be reached by car.

These natural walkers trudge without complaint, they have stamina,
they have grit.
But sometimes they trudge without purpose, almost too willing to
follow the path, or the teacher, gazing contentedly at their own feet.
These people may make the best hikers, who knows?
But it is more credible that people

At the end of the day, hiking is not about the act of walking itself,
which can be pure drudgery, but rather, to use walking as a way of experiencing
the world.

Perambulatory parable

And these hiking classes will remain a dead letter until they get out
of the scrubland and own their purpose.


Do we really expect them to become devotees of the deductive method
after fifteen theorems abut triangles?
Of course, there will be people who naturally love Euclid.
But proving facts about plane figures leaves most of us cold.

which is all about
playing with formal structures and discovering their
properties

skill, and you needed it to get by as an adult.

The first is to lower our ambitions and go on short walks.
The connection between practice and real life is then clear, and less
likely to lead to resentment; the teacher can justify the whole
enterprise.

If we lower our sights, society as a whole could lose out.

Perhaps, then, we should restrict hiking classes to those who naturally enjoy
walking and don't mind the drudgery.

These people, one could reason, will obviously become the best hikers.
We can get them running laps through the scrubland and they'll love it!
But is it true that they'll become the best hikers?

be great hikers, if only they developed the walking skills.

Really, we should *make things interesting*, and let the students
decide for themselves whether they want to hike.
This is the solution the astute reader will have guessed immediately.

into valleys and up mountains, at dawn and sunset when the prospects are good.

They would learn that, at the end of the day, hiking was not about the
act of walking, but rather, using walking to
experience the world.

into valleys and
up mountains, through meadows, swamps and forests.
,
while students found their feet

What if, by restricting our attention to natural walkers, we
miss out on a huge pool of talent, namely those with the potential to
be great hikers if they practice walking?

For most people, this is not an intrisically interesting activity.
In fact, it's particularly boring for mathematicians!
This is because maths is not walking; it's hiking.
It's a way of encountering and understanding and exploring the world
using formal systems.
But maths curricula, at least in Australia and North
America, insist on marching students through the scrubland.

Both of these solutions are unsatisfying because the answer is obvious.

past swamps and
meadows, into forests, along streams and canyons.

This would not only turn natural walkers into good hikers, but
identify others with hiking talent who need more motivation.

The greatest success, in this new paradigm, would be the moment a
student realised that hiking was not about walking, but rather, using
walking to experience and understand the world.

I'm going to pick on an Australian textbook for the most advanced high
school subject.
But, in its defense, all of the textbooks are like this.

But this all depends on whether walking is a skill that can be developed.
If so, then by focusing on natural walkers, we lose access to a huge
pool of talent, namely those with the potential to be great hikers
if only they had the motivation to walk.

The scrubland is an empty philosophy.
We are best served, as individuals and as a society, by showing
students that hiking is not about walking, but rather, using
walking to experience and understand the world.

Walking takes you to interesting places, if you do some planning and
follow your nose.

We should take them through varied and stimulating terrain, into
forests, along streams, down canyons, and up slopes.


Perhaps, then, we should focus on training *natural walkers*
those who walk tirelessly and without complaint through the scrubland.

But maths curricula, at least in Australia and North
America, insist on marching students through the scrubland, turning

These are repetitive, mindless, plug-and-chug problems, and students are
forced to do hundreds of them.

I don't know about you, but these problems fill me with existential horror.
Why do I care about the derivative of $\sin^{-1}(5x/4)$?
Let alone its second derivative?
What is this for?
Why am I doing any of this?
Why am I even here?
This is what I mean by the scrubland.
There are no landmarks, nothing for the eye to latch onto, just an
endless plain of withered, ankle-height shrubs.

Maybe there are some landmarks in the distance after all, once we get past
the dead shrubs.
What could they look like?

hike into the foothills, armed
only with a compass and a sense of adventure.

There are two directions we could go, which reflect the structure of
mathematics itself.

Perhaps we should show our students some beautiful mathematics.
In my analogy, this could a mountain peak with a particularly glorious view of sunrise.
You need to be a good walker to get there, and the trail may wind
through some shrubby foothills.
More generally, pure mathematicians are like Indiana Jones, venturing
into trackless realms and finding objects of great beauty, before,
almost as an afterthought, bringing them back to civilisation.
This is an activity we should be modelling and advertising and making accessible.


But this is not what happens.
Here's an example of what passes for pure mathematics in our "advanced" textbook:

This is more scrubland, but the shrubs are coloured differently.
There is nothing beautiful about these results, nothing surprising.
They are presented as brute formal facts, with no aesthetic value.

These sort of look like the other problems; in fact, I have a sneaking
suspicion that they are *exactly* the same, but they've replaced numbers with
letters.
These are just shrubs of a different color.

Once again, there is some conventional wisdom at work here.
Students find proofs hard.
If you've ever tried to teach Euclid at a high school level, as many
countries do, you might have noticed this.
You feel like a dentist.
But I don't think it's because proofs are inherently difficult.
Rather, I think it's because throwing Euclid at them, without any
preparation, is a terrible idea.
Most people are not excited by sundry factoids about triangles.
It's a steep learning curve if you don't care about what's at the top
of the hill.

So we need to teach proofs better.
We need to use examples which pique student interest, and teach them
how to reason mathematically step by step.
Start with examples, visual proofs, intuition pumps, heuristics, and
judiciously cut corners.
If you start with Euclid's axioms, that's probably where the student's
relationship with the deductive method is going to end.

We don't usually need to scale the mountain to appreciate some of what
makes these things beautiful.
If the mountain is too steep, find a nearby hill with a gentler slope
and a partial view of the summit.

you could either tell the students, or
let them discover (with some prompting) for themselves.

This is a beautiful result, which is within the means of ordinary
students to discover for themselves with some judicious guidance.
It illustrates some basic principles of mathematical reasoning ---
play, building intuition from examples, induction from the specific to
the general, posing and answering questions.
The proof appears as a sort of *mechanism* which takes any input and
guarantees a tangency point as output.
(The idea that a proof treats an *infinite* number of examples is, I
think, a good way to introduce it in these contexts.)

Conventional wisdom states that students
need to master basic skills by drill before they can move on to more
interesting tasks.
This sounds reasonable, and I'll come back to drill below, but one can
ask: what are the landmarks they're meant to hike towards, now that
they differentiate inverse sine with their eyes closed?

That's the end of my little preamble, and by now you've probably realised
that I'm not really talking about hiking. I'm
talking about *maths*.
In this thinly-veiled analogy, walking is the ability to manipulate
symbols, to follow rules, to find your way around a formal structure.

Mathematics has its own world, a vast topography of features and
landforms, that can only be traversed and navigated by manipulating
symbols; but manipulating symbols is not itself the goal.

To help convey this boredom, let me give you a
snapshot of the scrubland.

There are two different paths heading off into the
mathematical landscape.

it's easy to generate minor variants of the same
question, the same two or three ideas, and make that a chapter of your
textbook.

It's true that students need to practice symbol manipulation somehow,
and I'll say more below about how to do that in a way that doesn't
inspire existential horror.

The traditional claim that students
need to drill in order to *get somewhere interesting* is usually made in bad
faith.

You can take anything and shrubbify it, because all you do is generate
minor variants of the same problem.
Find 15 distinct problems, and you have yourself a textbook.

and a lot of
collaboration with the professional navigators, people who know the
landscape and use the trails.

It looks like we need to prepare some students to do advanced hiking.
But if most students hate walking through scrubland, maybe we should
restrict advanced classes to those who enjoy it, the "natural walkers"
who trudge tirelessly and without complaint for hours.

Mathematics has its own world, a vast topography of features and
landforms that must be traversed by manipulating
symbols, but manipulating symbols is not itself the goal.

I scraped by with passes, but I didn't understand or care about it.

Here are some calculus exercises from a popular Australian textbook for the
most advanced maths class.

two different roads winding off into the mathematical distance.

I mean, what is inverse sine on a Saturday?
Could I get a beer with it?

But wait a second!
Conventional pedagogical wisdom tells us that drill is
necessary to develop basic walking skills, for students to find their
feet before they walk off into the foothills.
Maybe we can disagree about the best way to learn to walk, but the
bottom line is that if students *never get anywhere*, this claim is made
in bad faith.

Or would you have lost interest, and started lagging behind?

There are a few different ways we could fix this situation.
The first is to make the connection between practice and real life closer,
exchanging hikes for small, unambitious strolls.

But what if a whole sector of the economy
depends on advanced hiking skills?

If we lower our sights, everyone loses.

Perhaps we should restrict classes to the "natural walkers", the
students who trudge tirelessly and without complaint through the scrubland.
They appear to have the most potential.
But what if walking is a skill that can be *developed*, rather than a
natural ability, like double-jointedness, you're either born with or not?
If so, then just taking natural walkers cuts us off from a huge reservoir of
talent: the students who could become good hikers if they were motivated to walk.

There is a simple way to develop good hikers and maximise access to
talent: stop marching students through the scrubland!
We should take them through varied and stimulating terrain, into the
forest, or towards
the strange rock formations in the distance.
At first, lessons would be along well-marked trails, but with time,
they could learn to camp in the wilderness, explore uncharted wastes
and conquer summits.
This would turn natural walkers into good hikers, and bring others
along who may, with practice, become just as good or better.
By taking them on real hikes, students would learn that hiking is not
about the act of walking, but rather *using walking* to experience and
understand the world.

I don't debate this, though I think there are better ways to do it
than walking through scrubland, and a lot of newfangled pedagogy is
focused on trying to make this process more engaging and inclusive.

So where does this claim come form?

There is nothing beautiful or deep here, just the same manipulations
in disguise!
It is the wrong sort of generalisation.

What should be a voyage of discovery and empowerment, a journey into
the mathematical world, is a joyless plod for most students.

In other words, these hiking classes effectively kill interest in hiking.

For a fuller discussion of the role of aesthetics in mathematics, see
for instance
["Aesthetic Considerations in Mathematics" (2011)](https://pdfs.semanticscholar.org/c01f/1b7cdbe2b9a649d09311f7b3e5e1bcb88310.pdf) by Nathalie Sinclair.

In this slightly tortured analogy, 

(I'm hoping this is starting to ring bells, but let's continue with
the fable.)

I want you to imagine a reality, not so different from our own, where
you were forced to take *hiking classes* in high school.

(In fact, it seemed like a sort of toy version of philosophy where
everything really obeyed its definition.)

If classes are boring, the only people to stick around will
be the ones who naturally love walking, who trudge
tirelessly and without complaint across miles of scrubland.

we should stop marching student through the scrubland, even if that's
what's been done for time immemorial.

At first, hikes would be along well-marked trails, but with time,
they could learn to camp in the wilderness, explore uncharted wastes
and conquer summits.

But that's how they'd been doing things forever, so that's the way
things were.

That's what *hiking* (as opposed to *walking*) should be about.

If classes are boring, only the kids with endurace and a natural yen
for walking will stick around.
And many teachers will say: good!
These are the students with talent and real potential for hiking.
But walking is a skill that be developed, and if hiking looks like
fun, it will motivate students to get better at walking.
And what do you know?
The pool of talent feeding into our hiking sector just got a lot
bigger, the pipeline less leaky.
Everyone wins.

The way to fix these classes, and make hiking fun, is obvious:
we should stop marching student through the scrubland, even if that is
what tradition dictates.

To help make the problem more vivid, and its solution clearer,
consider an analogy to *hiking*.

But what if we were to learn that walking was a skill that could be
developed, and natural ability mattered much less than the
motivation to develop it?
What if studies revealed that most of these "natural walkers" had
pivotal experiences of non-scrubland hiking?

We would stop dividing the class into those with and without ability,
but rather, those with and without *interest*, since we would see that
this is the primary determinant of walking skill.

By going on real hikes, students would discover that hiking is not
about the act of walking, but rather using walking to experience and
understand a world rich in wonder.

And they don't need to become a professional hiker to enjoy the odd
stroll, any more than they need to be a professional writer to read
the odd book.


Put a different way, the mathematical world, with its vast topography
of features and landforms, must be traversed by manipulating symbols,
but manipulating symbols is not itself the goal.

I know because that was my experience in high school.
I was not a natural symbol manipulator, and scraped by with passes
until learning that maths could be *used* for things.

Let's look at an example.
These calculus exercises are taken from a popular Australian textbook.
Calculus is, without exaggeration, one of the great landmarks of human thought.
What does the textbook make of it?

That's how indistinguishable and repetitive these questions are.

In a way, it's perversely impressive how these textbooks take a
milestone of Western thought and "shrubbify" it.

I mean, what is inverse sine on a Saturday?
I may as well be looking at a barcode.

The topic, calculus, is like a jewelled diamond in a precision watch:
both gorgeous and supremely useful.

But they also fill me with existential horror.

Perhaps I'm being unfair.
First of all, you might say it's the role of the teacher to enliven the lesson, to
provide context and motivation.
But if these aren't hardcoded into the curriculum and the textbooks,
then every class with a teacher who is inexperienced, underqualified,
or lazy, gets shortchanged.
It's a recipe for massive inequality.
Spicing up the textbook won't solve this problem, but it can alleviate it.

A second objects is that students need to walk before they can hike,
or in mathematical terms, to become handy symbol manipulators before
they can do real maths.
There are better ways to do this than looking at shrubs.
But the real problem is that *the scrubland never ends*.
What appear to be features on the horizon are just shrubs of a
different colour.
And if students *never get anywhere*, the claim that they have to
drill, before they can go somewhere interesting, is made in bad faith.
They drill in order to keep drilling.

This is the sad reality underneath a lot of conventional wisdom.

Physically drawing the curve, it seems impossible to avoid graphs a
finite number of kinks connected by short smooth segments ("piecewise
differentiable").
But we can proceed by steps.

This will maximally break the theorem in the sense that it holds for *no
subinterval* of $[a, b]$.

##### 2.3. Adding natural numbers <a id="sec-2-3" name="sec-2-3"></a>

##### 2.4. Arithmetic-geometric inequality <a id="sec-2-4"
name="sec-2-4"></a>

   3. <a href="#sec-2-3">Adding natural numbers</a>
   4. <a href="#sec-2-4">Arithmetic-geometric inequality</a>

Well, whatever height $h$ the first triangle is, at the $n$th step
they are height $h/2^n$.
As $n$ gets large, this goes very quickly to $0$. 

Using binary expansions, the argument which told us there were kinks
at each rational number in the blancmange function, now tells us that
the function $D(x)$ will equal the original height of the triangle,
$h$, at every rational $x$, and cannot be $h$ anywhere else.
What is it elsewhere?
Once again, use the intutition pump of "infinitely thin" triangles.
The sides will become vertical as $n \to \infty$, and so 

$$
D(x) =
\begin{cases}
   h & x \in \mathbb{Q} \\
	0 & x \notin \mathbb{Q}.
\end{cases}
$$

This is the
[Dirichlet function](https://en.wikipedia.org/wiki/Nowhere_continuous_function#Dirichlet_function).
Unlike the blacmange, it is not continuous *anywhere* and
therefore doesn't meet our original criteria.
But like the blancmange, it is infamously "pathological", an entry in
a sort of Gothic Victorian garden of monstrous functions.
Students may or may not find these aesthetically appealing.
Mathematician Charles Hermite wrote, “I turn with terror and horror from this
lamentable scourge of functions with no derivatives.”

Another loose end you can pose to students is whether this procedure
can be simplified.
The $2^n$ small triangles have the *same kinks* as the $n$th step of the
blancmange, so why do we need to add them?
Couldn't we just take the shrunken triangles in the limit $n\to\infty$
and use those instead?
Let students play around and see what happens.

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt10.png"
    width="70%" />
		    <figcaption><i>The limit of small triangles is a straight
    line made of points.</i></figcaption>
	</div>
	</figure>

They should come to suspect one of two things: first, it is somehow
made of infinitely small, jagged triangles; or the subtler, correct view that is just a straight line.
The technical tool to address this is the
[Hausdorff limit](https://en.wikipedia.org/wiki/Hausdorff_distance) of
sets, but you can make do with a simple intuition pump: how tall are
the triangles in the $n\to\infty$ limit?
Put a different way, what does an infinitely small triangle look like?
It is just a point.

<figure>
    <div style="text-align:center"><img src ="/images/posts/mvt11.png"
    width="70%" />
		    <figcaption><i>A limit of squeezed triangles?</i></figcaption>
	</div>
	</figure>

Similarly, if a student tries to get around this problem by squeezing
triangles horizontally, but leaving them height $h$, it is a nice
exercise to check that this function is not well-defined (except at
numbers with finite binary expansions, where it will be $0$).
Roughly, as we zoom in, the "tail" of the expansion will cause the
value to jump around with a limit as $n$ increases.

As a simple application, we can show something a little more
interesting about inverse sine.
Since the derivative of $\sin^{-1}x$ is $1/\sqrt{1-x^2}$, the MVT
tells us that, for $-1 \leq a \leq b \leq 1$, we have

$$
\frac{b-a}{\sqrt{1-c^2}} = \sin^{-1}(b)-\sin^{-1}(a).
$$

Since $1/\sqrt{1-c^2}$ is increasing for $c \geq 0$, it follows that
for $a \geq 0$,

$$
\frac{b-a}{\sqrt{1-a^2}} \leq \sin^{-1}(b)-\sin^{-1}(a).
$$

This is the sort
b-a \leq \sqrt{1-a^2} \left[\sin^{-1}(b)-\sin^{-1}(a)\right].

In contrast to pure mathematics, we now choose mathematical objects
which represent or *model* non-mathematical objects, and use our
powers of symbolic manipulation to try and learn things about the real
world.
While pure mathematics seems to have privileged access to truth,
applied mathematics is more contingent; in
[the words of George Box](https://en.wikipedia.org/wiki/All_models_are_wrong),
"all models are wrong, but some are useful".
But

(On a different propagandistic note, the history of mathematics is a
wonderful source of motivation, colour, and character, and we do
students a disservice by not telling them more.)

They feature objects, like mothballs and sandpiles, which students
We have "world problems": contrived, lifeless exercises which provide
no insight or motivation.
They grow in a region of the scrubland, unironically marked by a
little cardboard sign saying "real world".

since it's the lair
of many a dreaded *word problem*.

But the objects and the numbers are chosen arbitrarily, and the questions are uninsightful, they feel contrived and lifeless.
We're still in a scrubland of unmotivated drill, where instead of
replacing numbers with letters, we've replaced them with words about
randomly chosen objects.

The natural world isn't just beautiful; it's also chock full of
resources, from basic things like air and food and shelter, to rarer
materials like gold or petroleum.
Similarly, the mathematical world is full of resources.
And in the same way that the material needs of civilisation can
inspire the explorer and shape her quest, the needs of other
scientists have long been a source of inspiration for mathematics.
Instead of writing confusing problems about random objects in a world
of dead facts, we should connect students to the living, breathing
sources of mathematical inspiration.

Calculus is a case in point, since Newton invented it to formulate his
laws of mechanics!

I will give concrete examples, based on the (randomly selected)
snippet of calculus above.
This is a topic for advanced students, and my examples will be chosen accordingly.
But to provide evidence that the simple-minded approach of making maths
fun works at other grade levels, I'll give a supplementary
set of examples for trigonometry.

Why not tell them where algebra, trigonometry, or calculus
really come from?
And show them how powerful these tools are?

I'm a theoretical physicist, which means that I use mathematics on a
daily basis, and love it; I'm a big fan.

Some students would probably still hate hiking.
But so many more would be enriched.

This is different from trying to include "weak" students by making
things dull and easy!
No one benefits, since it reinforces stereotypes and turns everyone off.

This is more conceptually challenging than the first moth ball question,
but we are not straying from mathematics since the physics and chemistry has been "precomputed".
It's a related rates problem embedded in a real world application.
