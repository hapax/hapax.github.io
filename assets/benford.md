---
Layout: post
mathjax: true
comments: true
title:  "The CLT, Fermi estimates and Benford's law"
categories: [Physics, Hacks, Mathematics, Statistics]
date:  2021-01-04
---

**January 4, 2021.** *Bla*

#### A cheap proof of the usual central limit theorem

The central limit theorem (CLT) states that, if I sum up a bunch of
independent, identically distributed (iid) variables, the result tends to a
normal distribution.
More precisely, if $X$ has mean $\mu$ and variance $\sigma^2$, and
$X_i \sim X$ for $i = 1, \ldots, n$, then the sum converges to a normal:

$$
S_N := \frac{1}{\sqrt{N}}\sum_{i=1}^N (X_i - \mu) \to \mathcal{N}(0, 1).
$$

There is a simple heuristic proof we can give.
First, we need to define the *characteristic function* $\varphi_X$:

$$
\varphi_X(t) := \langle e^{itX}\rangle.
$$

This has various nice properties we will need. First of all, for $X,
Y$ independent, the characteristic function of the sum $X+Y$ factorises:

$$
\varphi_{X+Y}(t)  = \langle
e^{itX}e^{itY}\rangle = \langle e^{itX}\rangle \langle e^{itY}\rangle
= \varphi_X(t) \varphi_Y(t).
$$

Secondly, since derivatives and expectations commute, the derivative
at $t = 0$ gives moments:

$$
\frac{d^n}{d t^n}\varphi_{X}(0) = \left\langle \frac{d^n}{d t^n}
e^{itX}\right\rangle \bigg|_{t=0} = i^n\langle X^n\rangle.
$$

As a special case, $\varphi_X(0) = \langle 1\rangle = 1$.
The final property swaps constants from random variables to the
argument $t$:

$$
\varphi_{aX}(t) = \langle e^{itaX}\rangle = \varphi_{X}(at).
$$

The last ingredient in our cheap proof of the CLT is the
characteristic function for a normal distribution $\mathcal{N}(0, 1)$
itself. This is easily computed by completing the square:

$$
\begin{align*}
\varphi_X(t) & = \langle e^{itX}\rangle \\
& = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dx \,
\exp\left[-\frac{1}{2}x^2 + itx\right] \\
& = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dx \,
\exp\left[-\frac{1}{2}(x^2 - 2itx  - t^2) - \frac{1}{2}t^2\right] \\
& = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty dx \,
\exp\left[-\frac{1}{2}(x - it)^2 - \frac{1}{2}t^2\right] \\
& = \frac{1}{\sqrt{2\pi}} e^{-t^2/2} \int_{-\infty}^\infty dz \,
e^{-z^2/2} = e^{-t^2/2},
\end{align*}
$$

making the substitution $z = x - it$.
Now we can sketch a physicist's proof of the CLT.
Note that $Z := (X - \mu)/\sigma$ has mean $0$ and variance $1$, so that
if we expand its characteristic function as a power series, we have

$$
\varphi_Z(t) = 1 - \frac{t^2}{2} + O(t^4).
$$

Recall that the sum $S_N = \sum_i (Z_i/\sqrt{N})$, for $Z_i \sim Z$.
Thus, the characteristic function obeys

$$
\begin{align*}
\varphi_{S_N}(t) & = \left(\varphi_{Z/\sqrt{N}}(t)\right)^N \\
& = \left(\varphi_{Z}(t/\sqrt{N})\right)^N \\
& = \left[1 - \frac{t^2}{N} + O(t^4)\right]^N.
\end{align*}
$$

Assuming we can ignore the $O(t^4)$ terms, as $N \to \infty$, we have

$$
\varphi_{S_N}(t) \approx \left(1 - \frac{t^2}{N}\right)^N \to e^{-t^2/2}
$$

from the definition of the exponential.
This completes our sloppy heuristic proof!

#### A CLT for non-identical variables

The central limit theorem, in this form, is often invoked to explain
why common attributes like height and weight are normally distributed.
They are a sum of many small iid increments, and so should approach a
normal, or so the reasoning goes.
But why should heigh be a sum of iid increments?
At the end of the day, height is the phenotypic expression of our DNA.
Presumably, it arises from the sum of many small increments which are
neither independent nor identically distributed.
Even if we lump them into genes which are independent to a good
approximation, different increments are unlikely to have the same distribution.
The genes controlling the length of my legs contribute much
more than the ones controlling the thickness of my scalp.

One way to generalise the CLT is to consider independent but not
identically distributed variables $X_i$, with means $\mu_i$ and
variances $\sigma_i^2$.
In this case, we define

$$
\Sigma_N^2 = \sum_{i=1}^N \sigma_i^2, \quad S_N :=
\frac{1}{\Sigma_N}\sum_{i=1}^N (X_i - \mu_i).
$$

Then, under certain technical conditions we will discuss in a moment,
the sum $S_N$ approaches a normal as before:

$$
S_N \to \mathcal{N}(0, 1).
$$

The proofs are highly technical, but we can once again give a
heuristic flavour.
We can define the characteristic function $S_N$ as before, but since
it is made from different random variables, the expansion is a bit
more complicated:

$$
\begin{align*}
\varphi_{S_N}(t) & = \varphi_{X_1/\Sigma_N}(t)
\varphi_{X_2/\Sigma_N}(t)\cdots \varphi_{X_N/\Sigma_N}(t) \\
& = \varphi_{X_1}(t/\Sigma_N)
\varphi_{X_2}(t/\Sigma_N)\cdots \varphi_{X_N}(t/\Sigma_N) \\
& = \prod_{i=1}^N\left[1 - \frac{\sigma_i^2t^2}{2\Sigma_N^2} + O(t^4)\right].
\end{align*}
$$

We once again ignore the $O(t^4)$ terms.
Let's write $\alpha_i := - \sigma_i^2 t^2/2\Sigma_N^2$.
Then

$$
\begin{align*}
\varphi_{S_N}(t) & \approx
\prod_{i=1}^N(1 + \alpha_i)
\\
& = 1 + \sum_{i=1}^N \alpha_i + \sum_{i < j}\alpha_i \alpha_j + \cdots +
(\alpha_i \cdots \alpha_N) \\
& = 1 + A_1^{(N)} + A_2^{(N)} + \cdots + A_N^{(N)}.
\end{align*}
$$

The second term $A_1^{(N)}$ is secretly independent of $N$:

$$
\sum_{i=1}^N \alpha_i = - \sum_{i=1}^N \frac{\sigma_i^2
t^2}{2\Sigma_N^2} = -\frac{t^2}{2}.
$$

For the next term $A_2^{(N)}$, we can write

$$
\begin{align*}
\sum_{i < j}\alpha_i \alpha_j & = \frac{1}{2}\left(\sigma_i
\alpha_i\right)^2 - \sum_{i}\alpha_i^2 \\
& = \frac{t^4}{4} - \frac{t^4}{4}\sum_{i = 1}^N\frac{\sigma_i^4}{\Sigma_N^4}.
\end{align*}
$$

If the second sum vanishes as $N \to \infty$, then we get

$$
A_2^{(N)} = \sum_{i < j}\alpha_i \alpha_j \to \frac{1}{2}\left(\sigma_i
\alpha_i\right)^2 = \frac{t^4}{4}.
$$

Similarly, for the next term $A_3^{(N)}$, if we assume that

$$
\sum_{i = 1}^N\frac{\sigma_i^6}{\Sigma_N^6} \to 0
$$

as $N \to \infty$, then (along with the assumption used for
$A_2^{(N)}$) we will get

$$
A_3^{(N)} = \sum_{i < j < k} \alpha_i \alpha_j \alpha_k \to
\frac{1}{3!}\left(\sum_i \alpha_i\right)^3 = \frac{-t^6}{2^3\cdot 3!}.
$$

We can go on in this way, assuming that the "diagonal" sums vanish as
$N \to \infty$, leaving us with the result:

$$
A_k = \lim_{N\to \infty} A_k^{(N)} = \frac{1}{k!}\left(-\frac{t^2}{2}\right)^k.
$$

This means that the characteristic function for $S_N(t)$ approaches

$$
\begin{align*}
\varphi_{S_N}(t) \to 1 + A_1 + A_2 + \cdots
& = \sum_{k = 0}^\infty \frac{1}{k!}\left(-\frac{t^2}{2}\right)^k = e^{-t^2/2},
\end{align*}
$$

using the power series for the exponential.
To state things more carefully, our proof works provided that, for all
integers $p > 2$,

$$
\lim_{N\to \infty} \sum_{i=1}^N \frac{\alpha_i^p}{\Sigma_N^p} = 0.
$$

This vanishing of diagonal sums is precisely the *Lyapunov
condition*, so we have given a very simplified proof of what is called
the Lyapunov CLT.
The main technical difference is that the Lyapunov CLT only requires
this vanishing to hold for a single real number $p > 2$.

#### Lognormals and uniformity

<!-- https://arxiv.org/pdf/cond-mat/9808305.pdf -->
