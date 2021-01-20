---
Layout: post
mathjax: true
comments: true
title:  "Deterministic dice"
categories: [Mathematics, Physics, Statistics]
date:  2021-01-19
---

**January 19, 2021.** *Why are dice and coins good sources of
  randomness? Symmetry is not enough to explain why starting with the
  same initial conditions still seems to lead to randomness. I explore
  the relevant forces (chaos and jitter) in simple examples, and build
  deterministic dice from scratch.*

#### Introduction

Each time I roll a dice, my muscles try to do the same thing. But even
if I hold the dice the same way, and throw in what feels like the same
way, I seem to get any side of the dice with equal probability.
If you ask why a mathematician why any face is equally probable
despite the apparent similarity of the roll, they might say
*symmetry*. Apart from the pips indicating the
value
[<sup><a id="fnr.1" name="fnr.1" class="footref" href="#fn.1">1</a></sup>],
the sides are indistinguishable and therefore must have equal probability of landing right side up.
This is true and sounds like a nice explanation.
But it's only half the story!

To see why, suppose I take a very large dice, so heavy that I can only
drop it.
In this case, it's unlikely to roll, and whatever side happens to be
facing up when I "roll" will be facing up when it stops [<sup><a id="fnr.2" name="fnr.2" class="footref" href="#fn.2">2</a></sup>].
If I pick this face randomly, I will get a random outcome, but the
point of the dice is to outsource the randomness!
Symmetry is important, as we will see, but dice is fundamentally a roll-playing game.

#### The Butterfly Effect

To illustrate our ideas, we'll use the even simpler example of
flipping a coin.
Once again, ignoring the small effect of markings, the coin has a
symmetry between the two sides, heads and tails.
And similarly, if I have a very large coin I can only drop, then I
will need to randomly choose the initial conditions for tossing if I
want the coin flip to be random.
This defeats the purpose of the coin!
So, how does a deterministic process like throwing a coin generate an
*effectively random* and *equiprobably* outcome?
There are two main ingredients, as I see it: *chaos* and *jitter*.

We'll focus on chaos first, and a particular characterisation of chaos
called the "butterfly effect", aka *sensitivity to initial
conditions*.
Suppose a system has some space $\mathcal{C}$ of configurations $x(t)
\in \mathcal{C}$, where $t$ is time.
We'll restrict ourselves to systems which
evolve according to some deterministic rule, i.e. the state $x(t)$ at time $t$
determines the state $x(t')$ for any $t' > t$ [<sup><a id="fnr.3" name="fnr.3" class="footref" href="#fn.3">3</a></sup>].
Finally, we imagine that $\mathcal{C}$ has a notion of distance
between configurations, denoted by the absolute value sign, $|x_1 - x_2|$.
Then the system is chaotic (in the butterfly sense) if the distance
between nearby configurations get exponentially magnified by evolving
in time:

$$
|x(t) - y(t)| = e^{\lambda t}|x(0) - y(0)|.
$$

Time here need not be continuous, but could come in discrete steps,
with $t = 0, 1, 2, \ldots$, but in this case we'll write $x(n) = x_n$
to minimise clutter.
The rate of exponential divergence is controlled by $\lambda$, called
the *Lyapunov exponent* after
[Aleksandr Lyapunov](https://en.wikipedia.org/wiki/Aleksandr_Lyapunov).
<!-- There are all sorts of generalisations and subtleties, but all the
important ideas can be seen with a single Lyapunov exponent. -->
We can see how this operates in a very simple chaotic system called
the *doubling map*.
The configuration space $\mathcal{C} = [0, 1]$ is just the unit
interval.
Time is discrete, and at each step, we simply *double* the
configuration and keep only the fractional part, denoted by "mod
$1$". So we can describe the system by

$$
x_{n+1} = 2x_n \text{ mod } 1.
$$

It's easy to see this system is chaotic, since if we take two nearby
points $x_0, y_0$, then

$$
|x_n - y_n| = 2^n|x_0 - y_0| = e^{n\log 2} |x_0 - y_0|,
$$

provided the difference remains smaller than $1$.
Thus, the Lyapunov exponent for this system is $\lambda = \log 2$.

#### Exploring configuration space

At some point the doubling means that the difference gets so large
that the difference is no longer doubling with each step, since we are
throwing away whole numbers.
To see how this happens, let's do a specific example.
Set $x_0 = 0.1$ and $y_0 = 0.2$.
Then

$$
|x_4 - y_4| = 2^4 |x_0 - y_0| \text{ mod } 1 = 1.6 \text{ mod } 1 = 0.6.
$$

This does not mean the butterfly effect has "stopped". Rather, this is
the point at which the effect has fanned the two trajectories out so
they explore the whole system!
We can estimate the time this happens as follows.
Suppose the configuration space $\mathcal{C}$ has some effective
linear size $L$, and chaotic evolution with Lyapunov exponent
$\lambda$.
Then two trajectories with initial separation $\ell$ should spread
throughout the whole system in a time $T$ given by

$$
L \sim |x_T - y_T| = e^{\lambda T} \ell \quad \Longrightarrow \quad T
\sim \frac{1}{\lambda}\log \left(\frac{L}{\ell}\right).
$$

In our example, $\ell = |0.2 - 0.1| = 0.1$, and $L = 1$, so

$$
T \sim \frac{\log (1/0.1)}{\log 2} = \log_2 10 \approx 3.3,
$$

which is consistent with our discrete-time result $T = 4$.

We'll call $T$ the *exploration timescale*, since this is roughly how
long it takes for trajectories to fan out and explore the whole space.
In fact, if we choose a collection of initial
conditions in some region of size $\ell$, the exploration timescale
should still tell us roughly how long elements of this set need to
spread throughout all of configuration space.
Because of chaos, unless we know precisely which trajectory we picked,
predictability should totally break down, since initially nearby
points (order $\ell$) are now separated by distances on the order of the whole
system (order $L$).
This breakdown leads to an *effectively randomisation* over
configuration space.
<!-- We might expect that at this point, the butterfly effect has turned
these trajectories into *effectively random* samples of
configuration space. -->

#### Symmetry and chaos

This effective randomness is why we roll dice and throw coins.
Symmetry is still important, since it splits the configuratio space
$\mathcal{C}$ into regions of equal size, into which chaos threads
trajectories in a roughly uniform way.
<!-- plays the following role: it splits $\mathcal{C}$ into
equally sized patches, and then chaos spreads trajectories throughout
the system, and into these patches with roughly equal measure. -->
If the system doesn't get to evolve for long enough, like dropping the
large dice, trajectories don't spread and the result is strongly
biased by the initial conditions.
But after a few exploration timescales, we should be equally likely to
be in any of these symmetrically defined regions, when averaged over
the initial conditions.

This sounds like a mathematical theorem, and perhaps there is
something we can rigorously prove here.
But technical results about probability, dynamics and mixing involve
averaging over *very long times*, $T\to \infty$, rather than the exploration timescales we've
introduced here, and I'm not sure what tools we could use [<sup><a id="fnr.4" name="fnr.4" class="footref" href="#fn.4">4</a></sup>].
<!-- I expect also that we could "fine tune" the division of configuration
space so that, or the initial rolls -->
Instead of proving a theorem, however, we can use our concepts to
*design* coins and dice from scratch and check they behave correctly.
We'll just use the doubling map!
To start with, let's make a coin.
Heads will correspond to $\mathcal{C}_H =
[0, 0.5)$ and tails to $\mathcal{C}_T = (0.5, 1]$.

---

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum"
href="#fnr.1">Footnote 1</a></sup> <p class="footpara">
The pips do create a bias unless they are drilled, then filled with
black paint of the same density as the dice. This is standard
practice for "precision" dice used at casinos.
</p></div>

<div class="footdef"><sup><a id="fn.2" name="fn.2" class="footnum"
href="#fnr.2">Footnote 2</a></sup> <p class="footpara">
In physics parlance, the choice of initial condition—the way you
hold the dice—"spontaneously breaks" the symmetry of the dice
itself. This is the fancy reason that symmetry of the dice
isn't enough to explain the symmetry of the outcomes.
</p></div>

<div class="footdef"><sup><a id="fn.3" name="fn.3" class="footnum"
href="#fnr.3">Footnote 3</a></sup> <p class="footpara">
Note that this evolution may not be deterministic in reverse,
i.e. $x(t')$ may not be determined by $x(t)$ for any $t' < t$. This
asymmetry is intentional, since our main examples will throw away
information in a deterministic but irreversible fashion.
</p></div>

<div class="footdef"><sup><a id="fn.4" name="fn.4" class="footnum"
href="#fnr.4">Footnote 4</a></sup> <p class="footpara">
Specifically, I'm referring to *ergodic theory*, which concerns how
long time averages mimic probability distributions. There are
[many flavours](https://plato.stanford.edu/entries/ergodic-hierarchy/)
of ergodicity, and although there are some connections to chaos,
rigorous results on short time averages seem very hard. The
model I'm describing here is more of a physical ansatz.
</p></div>
