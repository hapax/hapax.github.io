---
Layout: post
mathjax: true
comments: true
title:  "Derivatives and fractals"
categories: Mathematics
date:  2020-07-06
---

**July 6, 2020.** *Derivatives as local approximation by fractals.*

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
as the limit of the secant line:

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
More precisely, a *fixed point* of zooming.
This is exactly what we mean by self-similarity, but it's useful to explain this fixed point idea.
A fixed point $\hat{x}$ of a function $g$ satisfies $g(\hat{x}) = \hat{x}$.
Applying the function to the point $\hat{x}$ does nothing.
We can define a zooming operation $Z_\lambda$, for $\lambda > 0$, which acts on real functions:

$$
Z_\lambda [f] = \lambda^{-1} f \circ \lambda, \quad Z_\lambda [f](x) =
\lambda^{-1}f(\lambda x).
$$

Here, we've overloaded $\lambda$ by making it stand for both a number
and the function which multiplies by $\lambda$, but hopefully that's
not confusing.
A self-similar function $\hat{f}$ is a fixed point of $Z_\lambda$, in the sense
that

$$
Z_\lambda[\hat{f}] = f, \quad Z_\lambda [f](x) =
\lambda^{-1}\hat{f}(\lambda x) = \hat{f}(x),
$$

just like the straight line, as we calculated above.

When we do a local linear approximation, we are zooming in until the
curve is approximately self-similar, at least when we centre the
coordinates at $x = x_0$ and $y = f(x_0)$.
In this case, we define

$$
\Delta f = f(x_0 + h) - f(x_0) \mapsto \lambda \Delta f, \quad h = (x_0 + h) -
x_0 \mapsto \lambda h,
$$

and our approximation

$$
\Delta f = L_m(h)
$$

Of course, we can locally approximate by other functions, and this
corresponds to a large part of mathematics.
But only the derivative really represents the function at "infinite
zoom", i.e. as an approximate
