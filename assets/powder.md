---
Layout: post
mathjax: true
comments: true
title:  "Taking half a derivative"
categories: [Mathematics]
date:  2021-03-13
---

**March 13, 2021.** *Fractional derivatives can be defined in a couple
  different ways, one involving powers and a second involving
  exponentials. I'll present these and check they give the same
  answer!*

#### Introduction

In calculus, the regular derivative is defined as the local gradient
of a function:

$$
\frac{d}{dx} f(x) = \lim_{h\to 0}\frac{\Delta f}{\Delta x} = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}.
$$

We will abbreviatve this as $f' = f^{(1)} = Df$, understanding that $f$ is a function
of $x$ and $D$ differentiates with respect to $x$ (though we can add a
subscript $D_x$ if we want to be very careful).
We can always differentiate again, and again, and in fact as many
times as we want. Using our new notation, we can write the $n$th
derivative $f^{(n)}$ as

$$
f^{(n)} = D (D \cdots (Df)) = D^n f.
$$

This is well-defined as long as $n$ is a whole number.
But what if we could consider other types of derivatives, say half a
derivative? Let's call this $D^{1/2} = \sqrt{D}$. In the same way that
applying two ordinary derivatives gives the second derivative
$f^{(2)}$, it seems reasonable to hope that two half derivatives give
a full derivative:

$$
f' = \sqrt{D} \sqrt{D}f = Df \quad \Longrightarrow \quad \sqrt{D}
\cdot \sqrt{D} = D.
$$

What could half a derivative look like?

#### To be continued

The easiest way to go about this to use a trick called *analytic
continuation*.
This has a precise meaning in complex analysis, and we're going to do
something similar in spirit, but not truly rigorous.
The basic plan is just be to find nice, specific functions we can
differentiate $n$ times, and get in an answer in terms of $n$.
We'll define the *fractional derivative* $D^\alpha$ acting on these
functions by simply replacing $n$ with $\alpha$.
A sanity check will be that, for general $\alpha, \beta$, the
fractional derivatives obey

$$
D^\alpha \cdot D^\beta = D^{\alpha+\beta},
$$

so, e.g., two half-derivatives give a full derivative,
$\sqrt{D}\cdot \sqrt{D} = D$.
We call this the *multiplicative* property.
There are two issues with this approach.
First, how do we extend the definition to general functions?
And second, are the definitions for different functions in agreement?
We will answer both questions below, but for the moment, we will
simply push ahead and do our continuations.
Our first nice function is the exponential $e^{\omega x}$.
Differentiating simply pulls down a factor of $\omega$ each time, so

$$
D^n e^{\omega x} = \omega^n e^{\omega x}.
$$

It's very clear, then, how to define the fractional derivative acting
on this:

$$
D^\alpha e^{\omega x} = \omega^\alpha e^{\omega x}.
$$

Great! We can easily check the multiplicative property, assuming that
constants pass through the derivatives:

$$
D^\alpha D^\beta e^{\omega x} = \omega^\alpha D^\beta e^{\omega x} =
\omega^{\alpha + \beta} e^{\omega x} = D^{\alpha+\beta}e^{\omega x}.
$$

Now, you might think this is useless because we can only
take fractional derivatives of exponential functions.
But at this point, we introduce another assumption, namely that the
fractional derivatives are *linear*:

$$
D^\alpha (\lambda_1 f_1 + \lambda_2 f_2) = \lambda_1 D^\alpha f_1 + \lambda_2 D^\alpha f_2.
$$

where $f_1, f_2$ are functions and $\lambda_1, \lambda_2$ are constants.
In fact, let's suppose this linearity applies to an *infinite*
collection of functions $f$ and constants $\lambda$, arranged into an integral

$$
f(x) = \int_{-\infty}^\infty d\omega \, \lambda(\omega) e^{\omega x}.
$$

Then by linearity,

$$
D^\alpha f(x) = \int_{-\infty}^\infty d\omega \, \lambda(\omega) D^\alpha
e^{\omega x} = \int_{-\infty}^\infty d\omega \, \lambda (\omega)
\omega^\alpha e^{\omega x}. \tag{1} \label{exp}
$$

Functions which can be written this way are said to have a *Fourier
representation*, with the function $ \lambda (\omega)$ the *Fourier
transform*. It turns out most functions can be written this way!
But let's give a very simple example.
What is half a derivative of the familiar sine function?
We can write this in terms of exponentials as

$$
\sin(x) = \frac{1}{2i}(e^{ix} - e^{-ix}).
$$

Take a half-derivative using linearity gives

$$
\sqrt{D} \sin(x) = \frac{1}{2i}(\sqrt{D} e^{ix} - \sqrt{D} e^{-ix}) = \frac{1}{2i}(\sqrt{i} e^{ix} - \sqrt{-i} e^{-ix}).
$$

This is evidently not a real function!
It should also be clear there is some ambiguity about
which roots we choose.
This means that, even here, there are *different choices* of
fractional derivative.
But perhaps this isn't so surprising.
Our technique immediately gives an antiderivative operator,

$$
D^{-1} e^{\omega x} = \frac{1}{\omega}e^{\omega x}.
$$

Usually, we have an undetermined constant, which here is set to
zero.
So fractional derivatives are ambiguous in general, needing boundary
conditions to set constants and determine how to take roots.
That said, the ambiguity about roots will reappear importantly below!

#### Fractorials

But this isn't the only way to approach fractional derivatives. The
first function we encounter is usually the identity function $f(x) =
x$.
From there, we build up to polynomials $x^m$, and then arbitrary
powers $x^s$.
The derivative of a power has a very simple form:

$$
D x^s = s x^{s-1}.
$$

If we differentiate again, we bring down a factor of $s - 1$ and
reduced the index again. And so on. This leads to the expression for
$n$ derivatives:

$$
D^n x^s = s(s- 1) \cdots (s - n + 1) x^{s-n}.
$$

So far, this doesn't look nice.
But let's assume for a moment $s$ is an integer.
Then we can write

$$
s(s- 1) \cdots (s - n + 1) = \frac{s(s - 1) (s-2) \cdots 1}{(s -
n)(s-n - 1) \cdots 1} = \frac{s!}{(s -n)!},
$$

where we have introduced the factorial $s!$.
Thus, we can write

$$
D^n x^s = \frac{s!}{(s -n)!} x^{s-n}.
$$

To analytically continue this, we need a beautiful function called the
Gamma function $\Gamma$.
This gives us the factorial function at (shifted) integer values,

$$
\Gamma(k + 1) = k!
$$

but is defined elsewhere as well. I like to think of it as a
"fractorial" because it can take on these other values. Anyway, puns
aside, we can use the Gamma function to write

$$
D^n x^s = \frac{\Gamma(s + 1)}{\Gamma(s -n + 1)} x^{s-n},
$$

and immediately continue to the fractional derivative:

$$
D^\alpha x^s = \frac{\Gamma(s + 1)}{\Gamma(s -\alpha + 1)}
x^{s-\alpha}. \tag{2} \label{power}
$$

Too easy! (Note that this will be badly behaved for negative integer values of
$s$, so we'll ignore those.) Once again, we can check the multiplicative property:

$$
\begin{align*}
D^\alpha D^\beta x^s & = \frac{\Gamma(s + 1)}{\Gamma(s -\beta + 1)}
D^\alpha x^{s-\beta} \\
& = \frac{\Gamma(s + 1)}{\Gamma(s -\beta + 1)}
\cdot \frac{\Gamma(s - \beta + 1)}{\Gamma(s -\alpha - \beta + 1)}
x^{s-\beta - \alpha} \\
& = \frac{\Gamma(s + 1)}{\Gamma(s -\alpha -\beta + 1)}x^{s-\beta -
\alpha}  = D^{\alpha+\beta} x^s.
\end{align*}
$$

So this gives us another, evidently different way to define fractional
derivatives. It will apply to any sum or integral of powers of
$x$, for instance, infinite polynomials called *power series*:

$$
\sum_{k = 0}^\infty a_k x^k.
$$

These cover a lot of ground, but there is an even more general object
called the *Mellin transform*, analogous to the Fourier transform. But
we won't go there.
Instead, let's do another simple example.
One of the interesting properties of the Gamma function is that it
blows up to (minus) infinity for nonpositive integers:

$$
\Gamma(-n) = -\infty, \quad n = 0, 1, 2, \ldots.
$$

This is actually essential to get sensible answers!
For instance, let's take the derivative of a constant, $1 = x^0$.
Then according to our definition,

$$
D x^0 = \frac{\Gamma(0 + 1)}{\Gamma(0 -1 + 1)} x^{0 - 1} =
\frac{\Gamma(1)}{\Gamma(0)} x^{- 1} = 0,
$$

since the $\Gamma(0)$ in the denominator makes the whole thing vanish.

#### Gamma and tongs

Now we come to the crucial question: do these two methods agree?
Rather than give a fully general, rigorous proof, I'm going to content
myself with showing that the exponential definition (which I regard as
simpler) gives rise to the power definition.
At this point, it will become necessary to define the Gamma function:

$$
\Gamma(s) = \int_{0}^\infty dt\, t^{s-1} e^{-t}.
$$

This isn't looking particularly useful yet. But let's make the sneaky
change of variables $t = \omega x$.
This gives

$$
\Gamma(s) = x^{s} \int_{0}^\infty d\omega\, \omega^{s-1} e^{-\omega
x}.
$$

If we change $s \mapsto -s$, and rearrange, we get a formula for $x^s$
in terms of exponentials:

$$
x^{s} = \frac{1}{\Gamma(-s)}\int_{0}^\infty d\omega\, \omega^{-(1+ s)}
e^{-\omega x}. \tag{3} \label{gamma}
$$

Great! Now we just go ahead and use rule (\ref{exp}), with the hope we
will get rule (\ref{power}).
As usual, by linearity

$$
\begin{align*}
D^\alpha x^{s} & = \frac{1}{\Gamma(-s)}\int_{0}^\infty d\omega\,
\omega^{-(1+ s)} D^\alpha e^{-\omega x} \\
& = \frac{1}{\Gamma(-s)}\int_{0}^\infty d\omega\,
\omega^{-(1+ s)} (-\omega)^\alpha e^{-\omega x} \\
& = (-1)^\alpha\frac{1}{\Gamma(-s)}\int_{0}^\infty d\omega\,
\omega^{-(1+ s - \alpha)} e^{-\omega x} \\
& = (-1)^\alpha\frac{\Gamma(-(1+s-\alpha))}{\Gamma(-s)} x^{s-\alpha},
\end{align*}
$$

where on the last line we used (\ref{\label{gamma}}), but with $s
-\alpha$ instead of $s$.

#### Acknowledgments

Thanks to J.A. for provoking a discussion of fractional derivatives.
