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
There doesn't seem to be any analogous geometry, and we are forced to
do something fancy (like use the
[fundamental theorem of calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus))
if we want to find the area under the curve.

But it turns out we haven't tried hard enough!
There is a simple geometric approach to integrating $x^2$ and all the
higher monomials $x^n$.
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

This may seem like a convoluted reinterpretation, but it generalises
in a lovely way to help us integrate polynomials.

#### Pyramids and hypercubes

A hypercube or $n$-cube is a cube in $n$ dimensions.
Formally, we can view it as all points

$$
I^n = \{(x_1, x_2, \ldots, x_n) : x_i \in [0, 1]\} = [0, 1]^n.
$$

For instance, a $1$-cube is the unit interval $I = [0, 1]$, while a
$2$-cube is the unit square $[0 ,1]^2$.
The $3$-cube is what we usually mean by a "cube".
Now, the length of the unit interval is $1$, the area of the unit
square is $1^1 = 1$, and volume of the unit cube is $1^3 = 1$.
The pattern continues, with the volume simply given by the product of
the length of each side of the hypercube, $1^n = 1$.

Let us now divide a hypercube in the following way: draw a point at
the center, and from that point, draw a line to each corner.
These lines form the edges of a $(n-1)$-hypercube-based hyperpyramid,
which sounds a bit crazy but is actually very simple.
We illustrate for the simple cases below.
