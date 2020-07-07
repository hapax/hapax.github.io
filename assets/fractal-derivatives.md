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
Z_\lambda [f] = \lambda^{-1} \circ f \circ \lambda, \quad Z_\lambda [f](x) =
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
\Delta f = f(x_0 + h) - f(x_0) \mapsto \Delta f' = \lambda \Delta f, \quad h = (x_0 + h) -
x_0 \mapsto h' = \lambda h,
$$

and our approximation

$$
\Delta f = L_m(h) + o(h) \mapsto \lambda^{-1}
\left[ L_m(\lambda h) + o( \lambda h)\right] = L_m(h) + \lambda^{-1}o( \lambda h).
$$

It's not hard to see that the last term is also $o(h)$, since

$$
\lim_{h\to 0} \frac{o( \lambda h)}{\lambda h} = \lim_{h'\to 0}
\frac{o(h')}{h'} = 0.
$$

where we defined $h' = \lambda h$.
So, local linear approximation could also be thought of as local
approximation by a self-similar function.
This is naturally associated to the function at "infinite zoom", since
self-similar functions are fixed points of scaling.

#### Fractal approximation

Large tracts of mathematics are devoted to approximating functions.
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

Rather than consider these other approximation, we will simply ask:
is the straight line the only thing that can happen at infinite zoom?
The answer, of course, is no.
