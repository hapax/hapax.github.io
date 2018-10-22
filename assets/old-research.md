---
layout: page
title: Old research projects
---

Here is a list of old research projects, with lay summaries and links
to technical details.

- [*Scalar-tensor inflation in the Jordan frame*]({{
  hapax.github.io}}/assets/msc-thesis.pdf) (2015--16), supervised by
  [Ray Volkas](https://www.findanexpert.unimelb.edu.au/display/person1809). To
  explain why the universe is flat and uniform at large scales, we need a period of
  rapid cosmic expansion at the beginning of time. Sounds great, but
  it begs the question: what caused the expansion? One possibility is
  that spacetime is actually a sort of rubber sheet, bunched in some
  places and stretched at others. Bunching increases the density of
  the sheet, while stretching reduces it. The mass distribution obeys
  gravity in the normal way, but the sheet has its own dynamics, with
  bunches propagating along the surface, and natural or "unstretched"
  states. (This setup sounds crazy but arises naturally in string
  theory.) In my masters project, I considered what sort of rubber
  sheet dynamics (more formally, <i>scalar-tensor theories of gravity</i>)
  could create rapid cosmic growth just after the big bang. If you're looking
  for something less dense than a thesis, try a
  [completion talk](/assets/jordan-completion.pdf),
  [conference poster](/assets/jordan-poster.pdf) or
  [lay summary](/assets/jordan-lay-summary.pdf).

<figure>
    <div style="text-align:center"><img src ="/images/frame-cartoon.jpg" width="400px" />
    <figcaption><i>Jordan vs Einstein frame in scalar-tensor gravity.</i></figcaption>
	</div>
	</figure>
	
- [*The Clairaut-Legendre method for slow differential rotation*]({{
  hapax.github.io}}/assets/rotation.pdf) (2014), supervised by
  [Bryn Haskell](http://users.camk.edu.pl/bhaskell/) and
  [Paul Lasky](http://users.monash.edu.au/~plasky/). A star is a big
  rotating ball of fluid. Gravity squeezes the star and pressure
  pushes outwards; when the two forces balance, we say that the star
  is in equilibrium. In simple models, the star is a rigidly rotating
  sphere. More interesting models split the star into spherical shells
  rotating around a common axis, but at different speeds. You can go
  further, splitting the rigid shells into lines of latitude, like a
  bunch of hula hoops, which rotate around the common axis. I
  determined equilibrium conditions for the hula hoop star.
- [*On multiplicative Sidon sets*](http://users.monash.edu.au/~davidwo/papers/MultSidon-Integers.pdf)
(2013), with [David Wood](http://users.monash.edu.au/~davidwo/); see
[this poster](/assets/sidon-poster.pdf) for a more accessible summary.
Let's play a game called double-free. From
  the set of all positive whole numbers, we independently pick an
  infinite sequence, with the constraint that we are not allowed to
  pick doubles, e.g. 3 and 6. Since no two numbers in my sequence can have
  quotient 2, and we call 2 a <i>forbidden quotient</i> for the game. Now,
  whoever picks the "most" numbers wins. Here, "most" means the
  largest fraction of the first <i>n</i> whole numbers, as <i>n</i> goes to
  infinity. Suppose I pick all odd numbers, which is double free and
  half of all numbers. Can you do better? It turns out you
  can! In fact, the greedy algorithm, starting with 1 and picking the
  smallest number which is not a double of something already in the
  sequence, gives roughly 2/3 of all numbers, and is provably
  optimal. This strategy for double-free is well understood. We
  considered two other forbidden quotient games: <i>q</i>-free, where <i>q</i> is a
  rational number, and {<i>a</i>/<i>b</i>, <i>c</i>/<i>b</i>}-free, where <i>a</i>, <i>b</i>, and <i>c</i> are whole
  numbers with no common factors. In the latter case, where we have
  two forbidden quotients, we developed a greedy strategy, along with
  an algorithm for calculating the optimal fraction of numbers. I
  was supervised by David Wood as part of the [vacation research
  program](https://ms.unimelb.edu.au/engage/vacation-scholarships) in
  the maths department at the University of Melbourne.

<figure>
    <div style="text-align:center"><img src ="/images/sidon.jpg" width="450px" />
    <figcaption><i>Components connected by forbidden quotients.</i></figcaption>
	</div>
	</figure>
	
- [*XIBD: software for inferring pairwise identity by descent on the X chromosome*](https://www.ncbi.nlm.nih.gov/pubmed/27153693)
  (2012--13), with Lyndal Henden and Melanie Bahlo in the
  [Bahlo lab](https://www.wehi.edu.au/people/melanie-bahlo) at the
  Walter and Eliza Hall institute. Like IKEA furniture,
  each person carries around their own building instructions; instead
  of a manual, we have DNA, a string of 3 billion nucleotides. When
  humans (or other diploid species) mate, the parent strings get
  randomly interlaced and turned into building instructions for the
  offspring. We can think about how chunks of genetic code, or
  substrings, get passed around a family tree by this process, and
  from looking at shared substrings, make guesses about how people are
  related. I helped develop a software package to do this, focusing
  particularly on how to get more mileage from sex-linked chromosomes,
  which get passed round in different ways between male and female
  offspring.
  I conducted this research under the aegis of the
  [Undergraduate Research Opportunities Program](https://biomedvic.org.au/biomed-programs/urop/).
  You can read more about my work in this
  [lab presentation](/assets/x-chromosome.pdf) from 2012, and play
  with some of the earlier code I wrote [here](https://github.com/hapax/genesim).

<figure>
    <div style="text-align:center"><img src ="/images/males.jpg" width="226px" />
    <figcaption><i>Correlations on the X chromosome.</i></figcaption>
	</div>
	</figure>
- *Teaching and learning* (2014--17). I was involved with various teaching
and learning initiatives in the
[School of Mathematics and Statistics](https://ms.unimelb.edu.au/home)
at the University of Melbourne. The main themes were active learning and feedback.
  - I designed and co-piloted a [study](https://fyimaths.files.wordpress.com/2014/07/morphett.pdf)
  using tagging/metadata on assignments to generate automatic
  feedback. With [Deb King](https://fyimaths.org.au/contact/) and [Anthony Morphett](http://morphett.info/).
  - I helped Anthony Morphett design and test [visualisations](http://www.mathsblocks.com/html/images/ICME%20poster.pdf) of logical syntax.
  - Finally, I wrote a couple of Geogebra applets introducing concepts in real analysis
    ([continuity](http://melbapplets.ms.unimelb.edu.au/?portfolio=convergence-and-continuity-of-a-function),
    [sequential convergence](http://melbapplets.ms.unimelb.edu.au/?portfolio=convergence-of-a-sequence)).
