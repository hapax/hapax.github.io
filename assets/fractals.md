---
Layout: post
mathjax: true
comments: true
title:  "Derivatives, fractals and randomness"
categories: Mathematics
date:  2020-10-20
---

**October 20, 2020.** *A derivative is a local linear
  approximation. Linear approximations are natural candidates for the
  function at "infinite zoom" since they are self-similar, i.e. fixed
  points of scaling. Here, I make the natural generalization to local
  approximation by an arbitrary self-similar curve. I finish with
  stochastic derivatives, here interpreted as random fractals, and
  introduce Brownian motion as a simple example.*

#### Straight line are fractals

A straight line is the simplest fractal, since if you pick any point on the
line and zoom in, it looks the same. In other words, it is
*self-similar*. Let's check! A straight line passing through the
origin has equation

$$
y = L_m(x) = mx.
$$

"Zooming in" is the same as *rescaling* the $x$ and $y$ axis by the
same amount:

$$
x \mapsto x' = \lambda x, \quad y\mapsto y' = \lambda y.
$$

For any function $f$, rescaling both axes gives $y' = f(x')$, or

$$
y = \lambda^{-1} f(\lambda x).
$$

After this rescaling, most functions change, with $\lambda^{-1}f(\lambda
x)  \neq f(x)$.
But a line does not change under this rescaling:

$$
\lambda^{-1} L_m(\lambda x) = \lambda^{-1} (m (\lambda x)) = mx = L_m(x).
$$

This is what we mean by self-similarity.

#### Local linear approximations

Derivatives are sometimes called *local linear approximations*.
Let's unpack that.
If $f(x)$ is a real function, then its derivative at $x_0$ is defined
as the limit of the slope of the secant line:

$$
m = f'(x_0) = \lim_{h\to 0} \frac{f(x_0+h)-f(x_0)}{(x_0 + h)-x_0} =
\lim_{h\to 0} \frac{\Delta f}{h},
$$

if this limit exists. We can rewrite this as

$$
f(x_0+h) - f(x_0) = L_m(h) + o(h),
$$

where $o(h)$ stands for a function which shrinks faster than $h$ as $h
\to 0$, $o(h)/h \to 0$.
So, the "local" is in the fact that is a statement about behaviour in
a neighbourhood of $x_0$, the "linear" is in the choice of function
$L_m(h)$, and the "approximation" in $o(h)$.

#### Zooming in

What has this got to do with fractals?
Linear approximations are natural since they are what you see at
"infinite zoom".
More precisely, we can think of infinite zoom as producing *fixed points* of zooming.
This is exactly what we mean by self-similarity, but it's useful to
explain in terms of the language of fixed points.
A fixed point $\hat{x}$ of a function $g$ satisfies $g(\hat{x}) = \hat{x}$.
Applying the function to the point $\hat{x}$ does nothing.
We can define a zooming operation $Z_\lambda$, for $\lambda > 0$,
which acts on real functions as follows:

$$
Z_\lambda [f] = \lambda^{-1} \circ f \circ \lambda, \quad Z_\lambda [f](x) =
\lambda^{-1}f(\lambda x).
$$

Here, we've overloaded $\lambda$ by making it stand for both a number
and the function which multiplies by $\lambda$, but hopefully that's
not confusing.
A self-similar function $F$ is a fixed point of $Z_\lambda$, in the sense
that

$$
Z_\lambda[F] = F, \quad Z_\lambda [F](x) =
\lambda^{-1}F(\lambda x) = F(x),
$$

just like straight lines as we calculated above.

When we do a local linear approximation, we are zooming in until the
curve is approximately self-similar, at least when we centre the
coordinates at $x = x_0$ and $y = f(x_0)$.
In this case,

$$
\Delta f = f(x_0 + h) - f(x_0) \mapsto \Delta f' = \lambda \Delta f, \quad h = (x_0 + h) -
x_0 \mapsto h' = \lambda h,
$$

while our local linear approximation changes as

$$
\Delta f = L_m(h) + o(h) \mapsto \lambda^{-1}
\left[ L_m(\lambda h) + o( \lambda h)\right] = L_m(h) + \lambda^{-1}o( \lambda h).
$$

It's not hard to see that the last term is also $o(h)$, since

$$
\lim_{h\to 0} \frac{o( \lambda h)}{\lambda h} = \lim_{h'\to 0}
\frac{o(h')}{h'} = 0.
$$

So, local linear approximation could also be thought of as local
approximation by a self-similar function.
This is naturally associated to the function at "infinite zoom", since
self-similar functions are fixed points of scaling.

#### Fractal approximation

<!-- Large tracts of mathematics are devoted to approximating functions.
But these are not usually at "infinite zoom".
Instead, they are within some small but finite neighbourhood, and the
functions are not self-similar.
One familiar example is Taylor series, where we take polynomial
approximations of higher and higher order.
A quadratic Taylor expansion, for instance, takes the form

$$
\Delta f = f'(x_0) h + \frac{1}{2}f''(x_0)h^2 + o(h^2).
$$

As we zoom in, what happens?
We now get

$$
\Delta f \mapsto
\lambda^{-1}\left[ f'(x_0) \lambda h + \frac{1}{2}f''(x_0) \lambda^2 h^2 + o(\lambda^2 h^2)\right].
$$

It's clear that the presence of terms of different order in $h$ spoils
the invariance under zooming, so this is not a self-similar
approximation.

So, let's forget about these other approximations and return to
straight lines.-->
Local linear approximation is a natural thing to do because lines look
the same when you zoom in.
But they are not the only functions with this property!
We could replace a line with *any* self-similar function.
It is therefore natural to consider *local approximation by a
self-similar fractal* $F$, when

$$
\Delta f = F(h) + o(h).
$$

This is unique up to terms which vanish as $o(h)$, simply because

$$
\Delta f = F(h) + o(h) = G(h) + o(h) \quad \Longrightarrow \quad
F(h) - G(h)= o(h).
$$

As a trivial example, a self-similar function $F(x)$ is locally
approximated by $F(x)$.
So the Koch curve, made by iteratively adding snowflake-like
stellae, is locally approximated by a Koch curve!
To get an interesting local approximation, we can deform the star at
large scales, but leave it alone (or deform in some $o(h)$ way) as we
zoom in.

<figure>
 <div style="text-align:center"><img src
 ="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/KochFlake.svg/800px-KochFlake.svg.png" width="72%"
 />
 <figcaption><i>Iterating the snowflake. From Wikipedia.</i></figcaption>
 	 </div>
	 </figure>

Here, we obviously have a curve rather than a function per se, but the
same idea holds.

<!-- #### Lines are special-->

You may have noticed that I left $\lambda$ ambiguous when defining self-similarity.
Is a function $F$ self-similar if $Z_\lambda[F] = F$ for *any*
$\lambda> 0$, or just a certain fixed $\lambda$?
The straight line has the distinction of looking the same at any
scale, so $Z_\lambda[L_m] = L_m$ for any $\lambda$.
In fact, a straight line is the only "nice" curve with this property.
For instance, if we assume that our self-similar curve itself has a
(normal linear) derivative at some point $x$, then

$$
F'(x) = \lambda^{-1} \frac{d}{dx}F(\lambda x) = F'(\lambda x).
$$

If this is true for any $\lambda$, the slope at any two points is the
same, and we get a straight line.
Note that we only need a derivative at *one* point to get a straight
line from self-similarity under arbitrary zooms.
This shows that if there are other curves with this property, they are
nowhere differentiable.

#### Random fractals*

What if zoomed in differently on the $x$ and $y$ axes?
In other words, let's consider a generalization of the $Z_\lambda$
operator, $Z_{(\alpha,\beta)}$, which is defined by

$$
Z_{(\alpha,\beta)}[f] = \alpha^{-1} \circ f \circ \beta,
$$

which obeys $Z_{(\lambda,\lambda)} = Z_\lambda$.
This can also have fixed points, $Z_{\lambda_1, \lambda_2}[F] = F$,
fractals which scale differently in different directions.
As an example, polynomials are fractals in this sense.
For instance, consider $F(x) = x^2$.
Then

$$
Z_{(\alpha,\beta)}[F] = \alpha^{-1} (\beta x)^2 = (\alpha^{-1}\beta^2) x^2,
$$

and hence $F$ is a fixed point of $Z_{(\alpha, \sqrt{\alpha})}$ for
any $\alpha$.

The last ingredient in this pot-pourri of ideas is *randomness*.
Instead of a fixed, deterministic function $f$, I can imagine some
function $\hat{f}$ which fluctuates randomly.
It could be stock market data, dice rolls, or the position of a
bacterium motoring around in search of nutrients.
Whatever the source of randomness, it may make the function jumpy
enough to be non-differentiable, i.e. jagged when you zoom in, but not
describable by a *deterministic* fractal either.
But perhaps it can be described by a random fractal!

First, let's see what a local random approximation means (also called
*stochastic derivatives*).
A natural guess is

$$
\hat{f}(x_0 + h) - \hat{f}(x_0) = \Delta f \sim \mathcal{P}(h) + o(h),
$$

where $\mathcal{P}(h)$ is some probability distribution depending on
$h$ and possiby the value at $\hat{f}(x_0)$, and which is well-defined
in the limit $h \to 0$.
We will use *random fractal* as a clickbait term for "self-similar
probability distribution", i.e. such that $\mathcal{P}(h)$ is a
fixed-point of some $Z_{(\alpha,\beta).}$
More precisely, we mean that

$$
\alpha^{-1}\Delta f \sim \mathcal{P}(\beta h) + o(h).
$$

Let us try to build an example.
We will *construct* $\hat{f}$ by starting the function at some point
and simply letting it evolve randomly using the local approximation,
i.e. a random fractal of choice.
The simplest example is a normal distribution.
It should probably have mean zero so it has a chance of being
continuous, and the variance (spread) should also decrease as some
polynomial in $h$, say $\mathcal{N}(0, h^n)$.
Then as $h\to 0$, we will get $\Delta f \to 0$ almost certainly, and
continuity is guaranteed.

What is a reasonable choice of $n$?
A hugely important observation is that *variances add*, i.e. if $X$
and $Y$ are indepenent random variables, then $\text{var}(X+Y) =
\text{var}(X)+\text{var}(Y)$.
And we can split a step $h$ into many small changes whose variances
add.
Hence, 

$$
\begin{align*}
\Delta f(h) & = \Delta f(h/2) + \Delta f(h/2) \\
& \sim \mathcal{N}(0, (h/2)^n) +
\mathcal{N}(0, (h/2)^n) + o(h) \\ & \sim \mathcal{N}(0, h^n) + o(h),
\end{align*}
$$

where the last equation follows from the local random approximation to
$\Delta f(h)$.
From additivity of variances, the last equation is only consistent if

$$
2\left(\frac{h}{2}\right)^n = h^n \quad \Longrightarrow \quad n = 1.
$$

We have just constructed Brownian motion!
It obeys

$$
\Delta f
$$

<!--Is this useful? Not as far as I can see. For instance, defining a -->
<!--second derivative seems to be unnatural, since even though I can -->
<!--define finite differences in the usual way, there is no equivalent -->
<!--of Taylor’s theorem I can use to guarantee the error shrinks as -->
<!--o(h2). So it remains a curiosity. But it’s nice to notice that -->
<!--functions can exhibit all sorts of interesting behaviour at -->
<!--infinite zoom. Put differently, the notion of a local self-similar -->
<!--approximation is not as “straightforward” as you might think! -->

<!-- #### Higher derivatives

Can we take higher derivatives?
The second derivative is just the derivative of $f'$, which can be
written as

$$
\Delta F = f''h^2 + o(h^2).
$$ -->

<!--#### Scaling semigroups

But it's important to note that if $F$ is fixed under a certain
$\lambda$, it's also fixed under all powers of $\lambda$, since

$$
Z_\lambda \circ \cdots \circ Z_\lambda = Z_{\lambda^n}.
$$

In fact, more generally, these scalings form a *semigroup* under the product

$$
Z_\lambda \circ Z_\mu = Z_{\lambda \mu}.
$$

A semigroup is just like a group, in that it's closed under an
associative product and has an identity, but it doesn't necessarily
have inverses. The identity of course is $Z_1$.

Now, if a fractal $F$ is invariant under scalings $\lambda_1, \cdots,
\lambda_n$, it's invariant under the semigroup generated by their
products.
These semigroups can be horrendously complicated, but we can focus on
nice scaling semigroups associated to the curves themselves.
We denote these by $\mathcal{G}(F)$.
So, for instance, the semigroup associated with a straight line is
$\mathcal{G}(L_m) = \mathbb{R}^+$, the whole set of positive reals.
The Koch curve $K$ has $\mathcal{G}(L_m) = \langle 3\rangle$, the
set of perfect powers of $3$.

In fact, in general I guess that fractals can only give
$\mathcal{G}(F) = \langle g\rangle$ for some number $g$.
Roughly speaking, the argument would go something like this.
The only additive subgroups of the real line are of the form $a
\mathbb{Z}$ or *dense* in $\mathbb{R}$.
We can map these onto multiplicate subgroups of $\mathbb{R}^+$
homomorphically using the exponential, with the former giving rise to
the perfect powers $\langle e^a\rangle$, and the latter giving rise to
some dense multiplicative subgroup.
We can presumably constrain the sub-semigroups in the same way.
Consider a fractal $F$ invariant under zoom $\lambda$.
If $F$ has any local features, e.g. at some fixed zoom there is
a feature with length $\ell$, then under a zoom $Z_{\lambda+\epsilon}$, for
$\epsilon \ll \\lambda$, this feature is spoiled.
But in a dense sub-semigroup, there will be some element $Z_{\lambda
+\epsilon}\in \mathcal{G}(F)$, a contradiction.

Of course, this is far from rigorous, but it explains why I can't
construct anything else! -->

<!--#### Higher derivatives -->

<!--It seems naively as if we can define higher derivatives. Let's -->
<!--start with the second derivative. Suppose $F_{x_0}$ denotes the -->
<!--local fractal approximation at $x_0$, with 
$$
f(x_0 + h) - f(x_0) = F_{x_0}(h) + o(h).
$$
The local fractal at $x_0+h$ is naturally defined by -->
<!--$$ f(x_0 + 2h) - f(x_0 + h) = F_{x_0+h}(h) + o(h). $$ -->
<!--Then the difference is $$ \begin{align*}F_{x_0+h}(h) - F_{x_0}(h) -->
<!--&= f(x_0 + 2h) - f(x_0 + h) - f(x_0 + h) + 
f(x_0) + o(h) \\ &= f(x_0 + 2h) - 2f(x_0 + h) + f(x_0) + o(h).
\end{align*}$$ -->
<!--  It's clear that this difference is still self-similar, since $$Z_\lambda [F_{x_0+h} - F_{x_0}](h) = \lambda^{-1}F_{x_0+h}(\lambda
h) - \lambda^{-1}F_{x_0}(\lambda h) = F_{x_0+h}(h) - F_{x_0}(h). $$
This is similar to, but not quite, the ("second order forward") finite -->
<!--  difference for the second derivative:
$$ f''(x_0)h^2 = f(x_0 + 2h) - 2f(x_0 + h) + f(x_0) + o(h^2). $$
$$ F^{(2)}_{x_0} = F_{x_0+h}(h) - F_{x_0}(h) = f(x_0 + 2h) - 2f(x_0 + h) + f(x_0) + o(h).$$ -->
