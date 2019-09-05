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
  give a precise criterion for interest based on the Rawlsian theory of fairness,
  and illustrate the approach for teaching derivatives.*

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
   3. <a href="#sec-3-3">Sand piles, slopes, and self-organisation</a>
4. <a href="#sec-4">Miscellaneous issues</a>
5. <a href="#sec-4">Conclusion</a>

## 1. Stuck in the scrubland <a id="sec-1" name="sec-1"></a>

In high school, I was one of those kids.
I thought maths class was about as boring as watching paint
dry, except that a fresh coat of paint can add colour to the world.
I harboured no such illusions about mathematics.
Would I use trigonometry on my tax returns?
Or solve simultaneous equations at the supermarket?
Finding $x$ was not my problem.
I scraped by with passes, aping textbook examples and cramming for
tests, but maths class was a meaningless game with rules I didn't need
to know beyond the next quiz.
The situation was so bad that, at age 15, I had to teach myself from
scratch how to add fractions and multiply negative numbers.
I had just never internalised those rules.

A few years later, taking a philosophy course, I
encountered set theory for the first time, and it blew my gourd.
First of all, there was the [wonderful paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox) of Bertrand Russell about
the set of all sets which don't contain themselves.
Is this big set a member of itself or not?
If it is a member of itself, by definition it's not a member of
itself; and if it's not a member of itself, by definition it is a
member of itself.
Neither can be true, so the big set can't exist without breaking logic
(i.e. generating a contradiction).

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/russell.png" width="45%"/>
		    <figcaption><i>The joy of sets: solid arrows indicate
    membership and dotted arrows non-membership. Set A is not a
    self-member while D is. The Russell set R contains all and only sets which do not
    contain themselves. Does it contain itself? </i></figcaption>
	</div>
	</figure>

This is more than a novelty: Russell's paradox can be jerry-rigged into [an
argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument) that there are different sorts of infinity!
This is the sort of power that philosophers, using mere words, could
only dream of.
I saw that maths could be deep and bewitchingly strange.

At the same time, I was reading pop science books about fun topics
like relativity, black holes and quantum mechanics.
The books were mysterious but inviting, filled with pictures and metaphors
and colourful examples that tantalised but did not, ultimately,
enlighten.
I began to suspect that I was missing something.
To paraphrase Galileo, if I wanted to speak with the universe, it
looked like I needed to learn its lanaguage, which was mathematics rather than colourful analogies.
These two developments led me to switch from philosophy to maths and
physics, and I never
looked back.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/universe.png" width="70%"/>
		    <figcaption><i>The Eldritch Dodecahedron speaks in maths and not analogies.</i></figcaption>
	</div>
	</figure>

I was lucky, stumbling later in life onto a hidden realm of
extraordinary beauty and power.
But how many students are unlucky?
How many go through high school, numbed by repetition, cramming and
copying just enough to pass tests, but never seeing that there's a
mathematical world out there which happens to exquisitely describe our
world too?
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
    width="90%" />
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
I propose that they fail the **shrub test**:

<span style="padding-left: 20px; display:block">
<i>Would anyone bother to read this in their own time?</i>
</span>

Would they read it if they didn't have to pass a quiz?
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
The students who are already involved and making progress have
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

If we were hiking, the maximin test would translate into the simple
requirement that the students at the back of the group want to hike,
and aren't left behind.
If interest, rather than inborn mathematical ability, is the key to
success, then instead of marching slowly through featureless terrain,
our best bet to get these students involved is to pick an exciting
destination with diversions and enticements along the way.

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
nobler use of inverse sine to provide a scheme for approximating
$\pi$.

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
    width="95%" />
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
Some students will savour this pathological dessert, while others will
not and be in good company. Mathematician
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
As with the blancmange, I think it's worth mentioning the convergence
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
climbing a mountain every now and again, and prepare accordingly.

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
It's as if we've entered a Dalí-esque scrubland of random, melting
objects, labelled by meaningless numbers.

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

Our next problem extends the classic pursuit puzzle first posed
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
His gravestone even bears the enigmatic Latin phrase

<span style="padding-left: 20px; display:block">
<i>Eadem mutato resurgo. (Although changed, I shall arise the same.)</i>
</span>

This is a clear reference to the marvellous spiral.

##### 3.3. Sand piles, slopes and self-organisation <a id="sec-3-3" name="sec-3-3"></a>

Our final revision is the sand pile, taking inspiration from the model of
[Bouchard, Cates, Prakesh and Edwards (1994)](https://jp1.journaldephysique.org/articles/jp1/abs/1994/10/jp1v4p1383/jp1v4p1383.html).
They split a pile of sand into two components: a *standing layer*, which is the
large blob of stable sand at the bottom of the pile, and a *rolling
layer* of loose grains running down the slope.

<figure>
    <div style="text-align:center"><img src ="/images/posts/sandpile.png"
    width="68%" />
		    <figcaption><i>A sand pile, consisting of a standing layer
    and a rolling layer.</i></figcaption>
	</div>
	</figure>

The height of the standing layer is denoted $S$, and the thickness of
the rolling layer on top is called $R$.
The total height of the sand pile is then

$$
H = S + R.
$$

The *angle of repose* $\theta_\text{rep}$ is the maximum angle of a stable
sand pile; for simplicity we use the *slope* $\alpha = \tan\theta_\text{rep}$.
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

To make life easy, we just deal with one-dimensional piles.
Zoom in on a patch of sand pile centred at $x$, width $w$, small enough
that both the standing and rolling layer have constant slope, $m$ and
$\kappa$ respectively.

Let's first see how the height of the standing layer changes with time. A
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
Now we turn to the rolling layer, and use our equations to solve for
the shape of a simple triangular sand pile.

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

   Conclude that the rolling layer of the patch thins out at rate

	$$
	\frac{dR}{dt} = -v\kappa + b-\gamma R(\alpha - m).
	$$


6. (Extension) Consider a triangular pile of sand on a base of width
   $B$, with a steep drop on either side so the rolling layer falls
   off rather than building up.
   Suppose the standing layer is at the angle of repose.
   We focus on the right side of the triangle by symmetry.

	(a) Show that when $b = 0$, the sand pile equations imply

	$$
    R(x, t) = R(x - vt).
    $$

	This dependence on $x-vt$ is the mathematical definition of a *wave*.

	(b) A child now pours a thin, time-dependent stream of sand onto the top of the
    pile.
	This sets the height of the rolling layer at the top of the pile for each time $t$:

	$$
	R(0, t) = C(t).
	$$

	Assuming $b = 0$ for $x > 0$, show that the profile of the sand
    pile for $B/2 \geq x \geq 0$ is

   $$
   \begin{equation}
   H(x, t) = \frac{1}{2}\alpha B - \alpha x+
   C(t-x/v).\label{tailings1}
   \end{equation}
   $$

---

The BCPE sand pile model shows how slopes in
time and space interact, and leads to the insight that the rolling
layer travels like a wave down a standing cone at the angle of repose.
I think this is rather nice, and clearly beyond the scrubland. But
there's a spectacular twist to the story of sand piles if we
consider *discrete* models.
I won't delve into the details, though I think they could form
the basis of a meaty programming project for a keen class.

Imagine dropping sand grains at random onto a discrete grid of points.
If too many grains build up at a single site, they spill onto neighbouring
sites.
If any of these neighbouring sites are full, they too can spill, with the result that a single grain can cause an *avalanche* which
redistributes some large portion of grains in the sand pile.
This is, in brief, the [Abelian sand pile](https://en.wikipedia.org/wiki/Abelian_sandpile_model)
of
[Bak, Tang and Weisenfeld (1987)](http://cqb.pku.edu.cn/tanglab/pdf/1987-8.pdf).
It has many remarkable properties, such as a pretty fractal structure
in the distribution of grains when run for long enough:

<figure>
    <div style="text-align:center"><img src ="/images/posts/bak-corner.png"/>
		    <figcaption><i>A corner of the Bak-Tang-Weisenfeld sand
    pile (from Wikipedia).</i></figcaption>
	</div>
	</figure>

This fractal is related to the deeper property of [*self-organised criticality*](https://en.wikipedia.org/wiki/Self-organized_criticality),
where the sandpile ["tunes" itself](http://nautil.us/issue/23/dominoes/the-amazing-autotuning-sandpile) to maintain a delicate balance
between total order (no avalanches) and disorder (too many avalanches).
The technical tool to assess this balance is the statistical relation
between size and frequency of avalanches, but this is once again this is beyond our scope.

Many other systems are (somewhat controversially) thought to exhibit
self-organised criticality, such as forest fires, earthquakes,
co-evolution, and
[even the human brain](https://www.quantamagazine.org/brains-may-teeter-near-their-tipping-point-20180614/).
According to mathematician [Steven Krantz](http://math.bu.edu/people/changer/teasem/w04.pdf),
there is an infamous MIT exam which simply reads:

<span style="padding-left: 20px; display:block">
You have a pile of warm metal shavings in the shape of a cone. Discuss.
</span>

I can think of worse topics than this extraordinary connection between
piles of granular matter and self-organising fractals.

## 4. Miscellaneous issues <a id="sec-4" name="sec-4"></a>

I've called this a manifesto since it is more a call to arms than a
detailed program.
But in this final section, I want to address some possible issues and
develop ideas about classroom implementation along the way.

#### Does this approach actually work?

The [JUMP math program](https://www.jumpmath.org), founded by John
Mighton, is a primary level mathematical enrichment
program running on similar principles to those I am advocating here,
namely [guided discovery](http://edutechwiki.unige.ch/en/Guided_discovery_learning), play, and the core ethic that *every child
can learn mathematics and love it*.
The [data unambiguously show](https://www.jumpmath.org/jump/en/research_reports) that, at least for primary students, this
approach works wonders.
I am proposing a change in how we teach *secondary* mathematics, with
various other tweaks in emphasis and technique.
There may be wrinkles that arise from this difference in emphasis, but I would be surprised if the results were dramatically different.

#### What about engaged students?

Maximin does not forbid writing questions for engaged students.
It only forbits questions which *only* engaged students can enjoy.
But bonus questions can help engage the class as a whole.
In the JUMP program, bonus questions are used as a carrot, dangled
just beyond the standard material, enticing students to finish that
material and move onto something "fun".
In his book [*The Myth of Ability*](https://jumpmath.org/jump/en/book_myth_ability),
John Mighton even recalls breaking up a fight by threatening to
withhold one of these bonus questions!
The point is that bonus questions can be for everyone, from the least
engaged (who will be incentivised) to the most enganged (who will be challenged).
There is no need for streaming!

#### Do your examples pass the maximin test?

The <a href="#sec-3">revised questions</a> seem challenging, but I
intend them to be taken in the spirit of JUMP's bonus questions, a
carrot for a globally engaged cohort who trust the teacher or text.
But bonus questions are not a blank cheque.
They only work once students have a basic level of self-efficacy and
engagement.
Even then, they still need to be designed carefully, building on skills the
students already have, and chunking a difficult passage of reasoning
into small, achievable steps, consistent with guided discovery.
I've tried to chunk the <a href="#sec-3">applied questions</a>, and
to aim for relatively low prerequisites.
But this raises the question: how *do* students develop basic skills,
if we are to abandon the scrubland?

#### How do students develop basic skills?

As with JUMP, we can treat the aesthetic and applied highlights as
bonus material, enticing students through more repetitious,
facility-building exercises.
But do these have to be shrubs?
The JUMP program shows that, with a careful [constructivist](https://en.wikipedia.org/wiki/Constructivism_(philosophy_of_education))
mindset, building basic skills need not be an interest-killing affair.
Let's try a similar thing with our <a href="#sec-1-2">earlier patch of
scrubland</a>.
Consider these two questions.

---

1. Differentiate the following and state the maximal domain:

	(a) $\sin^{-1}(x/3)\qquad$ (b) $\cos^{-1}(x^2)\qquad$ (c) $\tan^{-1}(\sqrt{x})$.

2. (a) Using the chain rule, find the derivative of $f(x) = \cos(\sin^{-1}(x))$.

	(b) Deduce from trigonometric identities that $f(x) =
    \sqrt{1-x^2}$.
	Do the domains match?
	Differentiate and check that your answer agrees with (a).

    (c) Implicitly differentiate $\cos^{-1} y = \sin^{-1} x$ and
    isolate the expression for $dy/dx$.
	Is this consistent with your previous answers?

---

Which is more interesting?
I would argue that the second passes the shrub test while the first
does not, though they develop the same skills: differentiating inverse
trigonometric functions, using the chain rule, and identifying domains.

Is there *any* virtue to the first question?
Doing many variations of the same thing make you good at doing the
thing, though you do not necessarily need to understand it.
This is the logic of drill.
But I think the usual methods of assessment place far too much
emphasis on quickly performing algorithms, and far too little on
understanding and genuine mathematical thinking.
The following assignment question appeared in a graph theory class I
took from [David Wood](http://users.monash.edu.au/~davidwo/):

---

Define a numeric measure of the complexity of a graph. Compute it for
several examples, and prove some properties about your measure. You
do not need to write more than 1 or 2 pages to get full marks.

---

This is exactly the sort of exploratory, open-ended thinking we need
to encourage.
A scrubland of drill trains students for the scrubland of assessment,
and not the variety, complexity, and open-endedness of real life.

#### Does this work for pre-calculus topics?

Of course!
I literally chose calculus at random from the textbook.
*Any* mathematical topic has gorgeous theorems, freakish specimens,
and a rich history of real-world motivation and use.
Teaching trigonometry?
Perhaps Euclid is a little dry, but what about *non-Euclidean* geometry?
This is a wonderful place for guided discovery and exploration.
And what could be more empowering than determining the size of the
earth from the shadow of a stick, as
[Eratosthenes](https://en.wikipedia.org/wiki/Eratosthenes#Measurement_of_the_Earth's_circumference)
did in 100 BC.
What about algebra?
Try the unsolvability of the quintic, compass and straightedge
constructions, and applications to dimensional analysis.
Logarithms?
Here we have the density of prime numbers, slide rules, algorithmic
complexity and Fermi estimates.
The list goes on.

Hopefully the idea is clear.
Pick a topic, any topic.
Figure out its history, where it comes from, what it's really used for
and what mathematicians or scientists find beautiful about it.
Now incorporate *that* material into the syllabus.
Mathematical skills live in a big constructivist framework, and
according to the maximin test, attention needs to be paid to
developing that framework so that all students can benefit.
But these goals are not at odds!

#### What is the teacher's role?

In the approach I'm suggesting, the role of the teacher seems to
be supplanted by a curriculum full of sparkling ideas and
fancy constructivist praxis.
But learning is a relational endeavour, and the teacher remains an
essential part of the process.
It is through the teacher that trust is established, students are
engaged, and the subject comes alive.
For all of this to happen, teachers need to be on top of the material.
If the syllabus now encompasses continuous but nowhere differentiable
functions, numerical approximation, diffusion, or self-organised
criticality, it seems like a huge ask unless they have scientific
training.

But here's the thing: if students can learn it, so can teachers!
And if the syllabus is designed in an inviting, constructivist fashion
to reduce
[maths anxiety](https://www.cne.psychol.cam.ac.uk/math-memory/what-is-mathematics-anxiety)
in students, it should also reduce anxiety in teachers.
Perhaps, once they've left the scrubland, more teachers will be genuinely
enthusiastic about what they are teaching.
And enthusiasm is infectious!

#### What's next?

A single blog post is not going to overthrow secondary maths
education.
Instead of *replacing* the curriculum (an ambitious and long-term
goal), paths into the landscape can be offered as enrichment for the
conventional curriculum.
I'm currently [busy with a PhD](https://hapax.github.io/research), but
in the future, I hope to start assembling a database of exciting topics,
carefully embedded in a constructivist understanding of how people
learn mathematics.
Watch this space!

## 5. Conclusion <a id="sec-5" name="sec-5"></a>

Teachers and curriculum writers are experts on modelling what students
know and how they come to know it.
Scientists and mathematicians are domain experts, with specialised
knowledge, taste, and judgment.
We need to stop marching students through the scrubland, and introduce
them to the vast topography of the real mathematical world, with its
majestic summits, calm valleys, and monsters lurking in the badlands.
From its fertile soil, they can grow new plants, or mine for old
patterns, which will answer the unknown mathematical needs of the 21st
century.

## Annotated bibliography

- ["Self-organised criticality: an explanation of 1/*f* noise"](http://cqb.pku.edu.cn/tanglab/pdf/1987-8.pdf)
  (1987), Per Bak, Chao Tang and Kurt Weisenfeld. The explosive paper
  that started a whole new field of study. Unfortunately, real sand
  piles don't seem to behave this way, but the model remains
  provocative and useful.
- ["A model for the dynamics of sandpile surfaces"](https://jp1.journaldephysique.org/articles/jp1/abs/1994/10/jp1v4p1383/jp1v4p1383.html)
  (1994), J.-P. Bouchard, M. E. Cates, J. Ravi Prakesh and
  S. F. Edwards. A simple model of sand piles, developing the insights
  of Nobel-prize winner [Pierre-Gilles de Gennes](https://en.wikipedia.org/wiki/Pierre-Gilles_de_Gennes).
- "Darwin's *Tree of Nature* and other images of wide scope" (1981),
  Howard Gruber. In *Aesthetics in Science*, ed. Judith Weschler. A
  beautiful essay about scientific imagery, intuition, and the aesthetics of complexity.
- [*A Mathematician's Apology*](https://www.math.ualberta.ca/mss/misc/A%20Mathematician%27s%20Apology.pdf)
  (1940), G. H. Hardy. The classic defense of pure mathematics.
- [*Problems in General Physics*](https://archive.org/details/IrodovProblemsInGeneralPhysics)
  (1981), Igor Irodov. Concise, elementary physics in the Soviet
  school of education.
- *Out of the Labyrinth* (2007), Ellen and Robert Kaplan. A playful
  book about the Harvard math circle and its philosophy, discovered
  near the end of writing this post. A very similar message about
  discovery and play.
- [*The Myth of Ability*](https://jumpmath.org/jump/en/book_myth_ability)
  (2003), John Mighton. An exposition of the JUMP method and the
  philosophy behind it, very similar (though at a primary level) to
  what I have suggested here. Also discovered midway through the post!
- ["Sublimation of moth balls"](https://eric.ed.gov/?id=EJ180235)
  (1978), M. G. C. Peiris and K. Tennakone. A cute AJP article on the
  thermodynamics of moth ball sublimation.
- *A Theory of Justice* (1971), John Rawls. Perhaps the most
  influential book on political philosophy of the 20th century.
- "The Mathematical Unconscious" (1981), Seymour Papert. In
  *Aesthetics in Science*, ed. Judith Weschler. A perceptive essay on
  aesthetics and mathematical intuition from one of the giants of
  old-school AI.
