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
    ="/images/posts/pyramid2.png"/>
	</div>
	</figure>

But what happens if we want to integrate $x^2$?
There doesn't seem to be any analogous reasoning, and we are forced to
do something fancier (like use the
[fundamental theorem of calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus))
if we want to find the area under the curve.

#### Pyramids and hypercubes

It turns out we haven't tried hard enough, and there is a simple
geometric approach to integrating $x^2$ and all the higher monomials
$x^n$.
This lets us integrate any polynomial by simply adding monomial terms.
To see how to do this, let's first think of the integral of a linear
function in a slightly different way.
Rather than as half a square, let's slide the "height" of the triangle
down so it becomes isosceles.
The area is unchanged since $b$ and $h$ have now swapped roles.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/pyramid3.png"/>
	</div>
	</figure>

Now we double this triangle, and see it covers half of a square of
area $2bh$. Since twice the area of the triangle equals half the area
of this square,

$$
2A = \frac{1}{2} \cdot 2bh \quad \Longrightarrow \quad A = \frac{1}{2}bh.
$$

This may seem like a convoluted reinterpretation, but 
