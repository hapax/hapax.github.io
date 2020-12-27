---
Layout: post
mathjax: true
comments: true
title:  "The case of the contrary curtain"
categories: [Physics, Everyday]
date:  2020-12-27
---

**December 27, 2020.** *Another bathroom-themed post, this time
  on the mysterious billowing of shower curtains. This is related to
  the fact that planes can fly upside down!*

#### The shower curtain effect

A few days ago, I was taking a shower when I noticed the bottom of the
shower curtain nipping at my heels. The bathroom window was closed,
and the house was not particularly drafty, so I began to wonder if
there was another explanation.
Before I left the shower, I had arrived at a hypothesis: the hot water
of the shower is lighter than the cold air outside, so it rises over
the top of the shower curtain, cools, and pushes the column of cold
air down. The cold bottom of this column slips in under the curtain.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/shower1v2.png"/>
	</div>
	</figure>

I mentioned the phenomena and proposed buoyancy mechanism to my
partner.
She told me she had noticed the same effect in a *cold* shower! In
this case, there is no obvious reason for air to rise over the top of
the curtain, since it's all at the same temperature.
Something else is at play!

#### Einstein's wonky wing

If temperature isn't relevant, the stream of water coming down is.
Presumably, this generates a steam of air moving in the same
direction, and the question becomes: why does this air result in air
being pushed in under the curtain?
Since the air is moving, it is tempting to invoke Bernoulli's
principle, which states that in a stream of moving fluid, the sum of
gravitational potential energy, pressure, and speed, is constant:

$$
\frac{1}{2}\rho v^2 + \rho g + P = \text{const}.
$$

Since the air is moving inside of the shower curtain, and
the density should be the same, the pressure should drop inside the
shower. This will result in air rushing in under the curtain.
We draw a cross-section of this explanation below.
On the left is the stationary air.
On the right is the moving air at lower pressure, with the
low-pressure region in grey.
The blue arrow is the resulting force.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/shower2v2.png"/>
	</div>
	</figure>

This same reasoning is used to explain why holding a piece of paper in
your hand and blowing over the top of it causes the paper to rise.
It's also the conventional explanation for why planes fly.
The idea is that the top surface of a wing or aerofoil is longer than
the bottom, so assuming that air takes the same time to travel over
the top and bottom surface, it must travel faster over the top, and
once again Bernoulli's equation seems to predict a lower pressure
above and hence an upwards lift.

All of these explanations are wrong.
As [this xkcd](https://xkcd.com/803/) succinctly points out, planes
can fly upside down, while the Bernoulli explanation predicts that
lift now points in the wrong direction.
This is a subtle problem, and deceived no lesser a scientist than
Albert Einstein,
[who was hired](http://users.df.uba.ar/sgil/physics_paper_doc/papers_phys/fluids/coanda_effect_94.pdf)
by a German aircraft manufacturer during WWI to design a better
aerofoil.
He added a hump in the middle of the wing to increase the surface
area, assuming this would increase lift due to the conventional
Bernoulli explanation, but it flopped in wind tunnel experiments.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/shower3.png"/>
	</div>
	</figure>

Similarly, if you blow too closely to the piece of paper, it doesn't
rise, which is hard to explan using Bernoulli's equation.
I couldn't repeat this experiment with the showerhead, but Australian
physics teacher
[Peter Eastwell did](https://files.eric.ed.gov/fulltext/EJ1050910.pdf),
finding that if the stream of water is too close to the curtain, it
does not billow.
Once again, it's back to the drawing board!

#### Entrainment and the Coandă effect

Bernoulli's equation only applies when *viscosity*---"stickiness"
between layers of fluid---is negligible.
But in all the situations above, viscosity plays a key role.
The basic idea is very simple.
A narrow stream of air will tend to pull nearby air along with it due
to stickiness.
Carrying off air particles will create a partial vacuum, i.e. a region
of reduced pressure.
If you want to be precise, you can note that the ideal gas law

$$
PV \propto NT
$$

tells us that, if volume $V$ and temperature $T$ are kept fixed, then
reduced particle number $N$ reduces pressure $P$.
The process of glomming nearby air onto the stream is called
*entrainment*.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/shower4.png"/>
	</div>
	</figure>
	
Nature will try to fill up these low-pressure regions with air at
atmospheric pressure.
But if there is an obstruction on one side, this side cannot equalise
to atmospheric pressure, since the air can't pass through the obstruction.
So the region between the obstruction and the air stream remains at
low pressure.
There are two things that can happen, and they are not mutually
exclusive.
If the surface is flexible, the air on the other side can push it
towards the low pressure region.
This is what we see with the shower curtain and the piece of paper.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/shower5.png"/>
	</div>
	</figure>

But if the surface cannot come to the air stream, the air stream will
go to the surface.
This phenomenon is called the *Coandă effect*, though it was first
described in 1800 by polymath Thomas Young:

<span style="padding-left: 20px; display:block">
The lateral pressure which urges the flame of a candle towards the
stream of air from a blowpipe is probably exactly similar to that
pressure which eases the inflection of a current of air near an
obstacle. Mark the dimple which a slender stream of air makes on the
surface of water. Bring a convex body into contact with the side of
the stream and the place of the dimple will immediately show the
current is deflected towards the body; and if the body be at liberty
to move in every direction it will be urged towards the current...
</span>

Henri Coandă was a Romanian inventor, who rediscovered it while
working on an airplane design.
Although Coandă's claims to have designed the first jet are
controversial,

#### References

In a little more detail, the idea is that as we pile molecules onto
the column, hydrostatic pressure (due to the weight of the column
above) increases. This provides the force that pushes the air
under the curtain.

When I mentioned this to my partner, she informed me she had observed
the same effect --- but in a *cold* shower! Clearly, my buoyancy hypothesis was
wrong, or at least, not the only effect in play.

I mentioned this to my partner, who said she had observed the same
effect in a *cold* shower.
Clearly, my hypothesis was wrong! Some other mechanism is at play.
I did some googling, and discover that this phenomenon, called the
*shower curtain effect*, is actually surprisingly complex and not
fully understood!
Fluid dynamics simulations by UMass professor
[David Schmidt](https://mie.umass.edu/faculty/david-schmidt) suggest
that a horizontal vortex forms.
Like a hurricane, this rotation leads to lower pressure in the middle,
with the centripetal force due to a pressure difference.

Schmidt's explanation is appealing exotic.
But it is hard for the ordinary person to test, and there is another
mechanism which seems just as important, and leads to a surprising
analogy between shower curtains and plane wings.

https://repository.arizona.edu/bitstream/handle/10150/347509/AZU_TD_BOX112_E9791_1965_171.pdf
http://users.df.uba.ar/sgil/physics_paper_doc/papers_phys/fluids/coanda_effect_94.pdf
https://www.discoverhover.org/infoinstructors/guide8.htm
