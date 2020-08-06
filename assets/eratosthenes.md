---
Layout: post
mathjax: true
comments: true
title:  "Measuring the earth"
categories: [Physics, Mathematics, Hacks]
date:  2020-08-06
---

**August 6, 2020.** *Eratosthenes measured the size of the earth
  using three data points: two shadows and the distance between
  them. During the vernal equinox in March, I performed a (much less elegant)
  version of the same experiment, and discuss my results.*

#### Eratosthenes' elegant estimate

Eratosthenes (276--195 BC) was head librarian at the Library of
  Alexandria, and one of the great thinkers of the ancient world.
In a blow to civilization, the library was destroyed by invading Roman
  emperors, and most of Eratosthenes' work along with it.  Thankfully, his elegant method
  for calculating the size of the earth using only the shadow of a
  stick survives.

  On the summer solstice, locals in the Egyptian city of
  Syene noticed that, at noon, the sun hit the bottom of a deep well.
  Eratosthenes inferred that the sun must be directly overhead.
He also knew from Egyptian surveyors that Syene was roughly $5000$
  stadia (around $850 \,\mathrm{km}$) away from Alexandria.
  Eratosthenes performed a single experiment.  At noon on the summer
  solstice, he measured the shadow of a vertical rod in Alexandria.
  He found it was roughly $1/8$ of the length of the rod. 
Simple trigonometry shows this is enough to estimate the radius of the earth!

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/erat1.png"/>
		    <figcaption><i>Eratosthenes' elegant setup.</i></figcaption>
	</div>
	</figure>

We assume the earth is spherical, and the sun far enough away
  that the arriving rays are parallel.  The angle the sunlight makes
  with the stick is
  
$$
    \theta = \tan^{-1}
    \left(\frac{\mathrm{shadow}}{\mathrm{rod}}\right) \approx
    \tan^{-1} \left(\frac{1}{8}\right) \approx 7.1^\circ.
$$
	
  Here, we are making the reasonable assumption that the shadow is
  small enough to be modelled as a straight line. 
  From the diagram, we see that the angle the sunlight makes with the
  rod is the angle subtended by the arc of the great
  circle joining Alexandria and Syene. Since the the length of that
  great circle is the circumference of the earth, we have
  
$$
    \frac{\tan^{-1} \left(\frac{1}{8}\right)}{2\pi} \approx \frac{850
      \,\mathrm{km}}{\mathrm{circumference}}.
$$
	  
  We rearrange and divide the circumference by $2\pi$ to estimate the
  radius:
  
$$
    \mathrm{radius} = \frac{\mathrm{circumference}}{2\pi} \approx
    \frac{850 \,\mathrm{km}}{\tan^{-1} \left(\frac{1}{8}\right)}
    \approx 6800 \, \mathrm{km}.
$$
	
  The actual value is around $6300 \, \mathrm{km}$. Not a bad estimate
  from the shadow of a stick!

#### Two for the price of one
