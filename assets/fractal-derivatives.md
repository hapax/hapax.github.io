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

A straight line is the simplest fractal. If you pick any point on the
line and zoom in, it looks the same! In other words, it is
*self-similar*. Let's check. A straight line passing through the
origin has equation

$$
y = L_m(x) = mx.
$$

"Zooming in" is the same as *rescaling* the $x$ and $y$ axis by the
same amount:

$$
x \maps to x' = \lambda x, \quad y\mapsto y' = \lambda y.
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
as

$$
m = f'(x_0) = \lim_{h\to 0} \frac{f(x_0+h)-f(x_0)}{h},
$$

if this limit exists. We can rewrite this as

$$
f(x_0+h) - f(x_0) = mh + o(h) = L_m(h) + o(h),
$$

where $o(h)$ stands for a function which shrinks faster than $h$ as $h
\to 0$, $o(h)/h \to 0$.
So, the "local" is in the fact that is a statement about behaviour in
a neighbourhood of $x_0$, the "linear" is in $L_m(h)$, and the
"approximation" in $o(h)$.

#### Zooming in

What has this got to do with fractals?
Linear approximations are natural since they are what you see at
"infinite zoom".
More precisely, a *fixed point* of zooming.
This is exactly what we mean by self-similarity, but it's useful to explain this fixed point idea.
A fixed point $x^*$ of a function $g$ satisfies $g(x^*) = x^*$.
Applying the function to the point $x^*$ does nothing.
We can define a zooming operation $Z_\lambda$, for $\lambda > 0$, which acts on real functions:

$$
Z_\lambda [f] = \lambda^{-1} f \circ \lambda, \quad Z_\lambda [f](x) =
\lambda^{-1}f(\lambda x).
$$

Here, we've overloaded $\lambda$ by making it stand for both a number
and the function which multiplies by $\lambda$, but hopefully that's
not confusing.
A self-similar function is a fixed point of $Z_\lambda$, in the sense
that

$$
Z_\lambda[f] = f, \quad Z_\lambda [f](x) =
\lambda^{-1}f(\lambda x) = f(x),
$$

just like the straight line, as we calculated above.
This is what 
