---
Layout: post
mathjax: true
comments: true
title:  "Bathroom physics"
categories: [Physics]
date:  2020-12-13
---

**December13, 2029.** *A short, equation-free post on two bathroom
  phenomena with surprising physical explanations: the shadow cast by hair on water, and the tendency of
  shower curtains to billow out during use.*

#### A follicular folly

Place a human hair on a body of water in a well-lit bathroom.
Any part of the hair which pierces the water will cast an ordinary geometric shadow.
But any part that floats on the surface will cast a strangely large
shadow, surrounded by bright fringes.
I decided to investigate after my brother asked me why it happens.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/hair1.png"/>
	</div>
	</figure>

The short answer is surface tension.
The molecules at the surface of the water are more strongly attracted
to each other than the molecules in the middle, since they have
nothing to attach to above.
So they form a sort of elastic membrane on which the hair can sit.
Often, the explanations of how surface tension works are confusing
and wrong.
If the membrane is unbroken, how can it pull on an object?
Basically, it's a spring, and stretching it will produce a restoring
force along the spring.
This can generate an upwards force on the object if it sits in a dip,
as the angled arrows indicate below left.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/hair2.png"/>
	</div>
	</figure>

But when we displace water, as in this dip, buoyancy forces due to the
weight of displaced water trying to push its way back also play a
role.
They provide an upward force, also shown above left.
The force due to buoyancy is the volume of the hair beneath the water
level (the dotted line above right).
But we have displaced some extra water, shown in purple, and this
turns out to precisely equal the effects of surface tension.
In other words,

<span style="padding-left: 20px; display:block">
The force on an object supported by surface tension is the weight of displaced water.
</span>

Now we can explain the odd shadow.
The dip creates a concave lens which makes the light diverge, leading
to a larger shadow.
To return to a flat, level surface, it must undo some of the concave
curvature with some convex curvature at the edges.
This is what causes the bright fringe for the larger shadow.
We draw a cartoon below, with edges of the concave and convex sections
represented by dots:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/hair3.png"/>
	</div>
	</figure>

But this isn't the end of the story. I noticed that if I grabbed the
hair at either end, and dipped one end in the water and held another
in the air, the point it pierces the water casts a peculiar shadow I
call a "jellyfish":

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/hair4.png"/>
	</div>
	</figure>

The dark part we can explain using the concave dip as above, but what
about the white tail of the jellyfish?
This suggests that the hair is pulling the water up with it.
This doesn't make sense if we interpret the surface as an unbroken
membrane.
A more reasonable picture is the following largely convex lump:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/hair5.png"/>
	</div>
	</figure>

Once again, the hair in this position will be subject to a force equal
to the weight of the water pulled up. I counteract that force with my
own, by suspending one end in the air.
So have been missing a piece of physics: the attraction between the
water and the substance (keratin) making the hair.
This leads to an angle of contact between the hair and the water, most
convenient to visualise by placing a drop of water on a surface of
hair (rather than the other way round):

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/hair6.png"/>
	</div>
	</figure>

Our earlier pictures with the unbroken membrane assume the contact
angle is $\theta = 180^\circ$, corresponding to a droplet with an
unbroken surface, as above.
In general, a surface with $90^\circ < \theta < 180^\circ$ is said to
be hydrophobic, or "water-fearing".
A material with $\theta < 90^\circ$ is hydrophilic, or "water-loving".
In the extreme limit of $\theta = 0^\circ$, the drop completely
spreads out over the surface, as we would expect for a maximally
hydrophilic material.

Let's return to our follicular focus.
The jellyfish tells us that the contact angle for hair is smaller than
$180^\circ$.
To tell whether it's hydrophilic or hydrophic, we can conduct a simple
experiment.
If we place the hair vertically into the water, we are doing some
similar to our contact angle picture.
The water will form a sort of reverse meniscus around the hair:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/hair7.png"/>
	</div>
	</figure>

Since there is no up or down force, the volume of water above the
water line should balance the water below the hair.

If the contact angle is greater than $90^\circ$, and the hair is
hydrophobic, then it will form a convex lens and create a bright spot.
If the contact angle is less than $90^\circ$, and the hair is
hydrophilic, it will form a concave lens make a larger dark shadow.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/hair8.png"/>
	</div>
	</figure>

The experiment reveals a bright spot, suggesting the hair is
hydrophobic! For confirmation, I looked for the contact angle online
and found that, according to the industrial scientists who design
shampoo, it has a contact angle of around $\theta \approx 100^\circ$,
though it varies depending on the colour and age of hair.

#### Drawing the curtain
