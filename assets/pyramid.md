---
Layout: post
mathjax: true
comments: true
title:  "Integrals from pyramids"
categories: [Mathematics]
date:  2021-01-22
---

**January 22, 2021.** *I present an elementary, first-principles
  approach to integrating polynomials, which involves splitting a
  hypercube into congruent pyramids.*

#### Introduction

Derivatives compute slopes at a point.
Integrals compute areas under curves.
The first is a local operation, involving only information in a
neighbourhood of a point, while the latter is *global*, involving the
value of the function at different points.
This makes integration a lot harder than differentiation!

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/pyramid1.png"/>
	</div>
	</figure>

However, sometimes we have a shortcut for integrating: identifying an
integral with the volume of a solid.
A simple example is a linear function, $f(x) = mx$. When we integrate
from $x = 0$ to $x = b$, the area under the curve is just a triangle,
obeying $A = bh/2$ for height $h = mb$.
We can represent this reasoning in a picture:

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/pyramid1.png"/>
	</div>
	</figure>

You might think this simple geometric reasoning only applies to a
linear function.
But it turns out you can use it for any polynomial!

#### Pyramids and hypercubes
