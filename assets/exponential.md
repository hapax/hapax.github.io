---
Layout: post
mathjax: true
comments: true
title:  "The continually interesting exponential"
categories: [Maths, Physics, Hacks]
date:  2020-11-28
---

**November 28, 2020.** *I discuss some of the key properties of the
  exponential function without (explicitly) invoking calculus.
  Starting with its relation to compound interest, we
  learn about its series expansion, response to small changes, Euler's
  formula, and the sum of all positive numbers.*

#### Many returns

Suppose you make an investment $I_0$ which promises a return rate $r$ per
year.
The simplest possibility is that, at the end of the year, you generate
some interest $r I_0$, so the total value of the investment is $I_\text{simp} = (1+r)I_0$.
This is called *simple* interest.
But what if, instead, you get paid in six month instalments?
At the end of the first six months, you should get paid half your
interest, or $I_0 (r/2)$, so the total value is

$$
I_1 = \left(1 + \frac{r}{2}\right) I_0.
$$

If the interest is simple, you get the same amount of interest
$(r/2)I_0$ at the end of the year. But if instead of simple interest
you have *compound interest*, then the interest for the second half of
the year is recalculated based on its value after six months.
In other words, the second interest payment will be $(r/2) I_1$ rather
than $(r/2) I_0$, leading to a total value

$$
I_{\text{comp}(2)} = \left(1 + \frac{r}{2}\right) I_1 = \left(1 + \frac{r}{2}\right)^2 I_0.
$$

For a positive interest rate, $I_1 > I_0$, so you will get more
interest in the compound scheme.
Mathematically, $I_{\text{comp}(2)} > I_\text{simp}$ because

$$
\left(1 + \frac{r}{2}\right)^2 = 1 + r + \frac{r^2}{4} > 1 + r.
$$

Of course, I chose six months arbitrarily.
I could split the year into $n$ equal lengths, and use those to
compound interest, i.e. recalculate the next instalment based on the
current value, including the interest generated so far.
Let's call this value $I_{\text{comp}(n)}$.
As $n$ increases, so will the total value $I_{\text{comp}(n)}$ of
our investment, and in fact it has the value

$$
I_{\text{comp}(n)} = \left(1 + \frac{r}{n}\right)^n I_0
$$

since the interest rate for any period is $r/n$, so we multiply by
$1 + r/n$ at the end of each period.
A natural question is: how big can the interest at the end of the year
get?
Will it get infinitely large as I make $n$ large, or will it approach
some finite value?
Mathematically, this is just the question:

$$
\lim_{n\to \infty}\left(1 + \frac{r}{n}\right)^n = \,\,?
$$

It turns out this has a finite limit!
Proving this is actually rather difficult, but it's easy to see with a
computer.
We can just plot $(1+r/n)^n$ for increasingly large $n$ and see that
it settles to a finite value.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/exp-plot.png"/>
	</div>
	</figure>

We show a few values for $r = 1$ above.
For large $n$, say a million, we get a number $2.71828...$, plotted as
the horizontal black line.
Assuming it does converge, we use the $r =1$ limit to define the
famous mathematical constant $e$:

$$
e = \lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n \approx 2.781828.
$$

We'll return to the mathematical question of convergence below.

---

*Exercise 1.* Show that in the limit of "continuous" compound interest, i.e. large
$n$, the total value of our principal $I_0$ at the end of the year is

$$
\lim_{n\to\infty} I_{\text{comp}(n)} = e^r I_0.
$$

*Hint.* Consider redefining $n$ so that the interest term looks more
 like the definition of $e$.

---

Assuming this limit of continuous compounding exists, we define the
*exponential function* as

$$
e^x = \lim_{n\to\infty} p_n(x), \quad p_n(x) = \left(1 + \frac{x}{n}\right)^n,
$$

where for convenience, we've defined the polynomial $p_n(x) =
(1+x/n)^n$.
Thus, if the interest rate per annum is $r$, and we compound with $n$
intervals, the total value at the end of the year is $p_n(r)I_0$.
In the rest of this post, we will explore some of the remarkable
properties and applications of the exponential function, but from an
elementary, pre-calculus point of view.

#### An infinite polynomial

Above, we expanded the term $p_2(x)$:

$$
p_2(x) = \left(1 + \frac{x}{2}\right)^2 = 1 + x + \frac{x^2}{4}.
$$

With a bit more labour, we can expand out the expression for three periods, $p_3(x)$:

$$
p_3(x) = \left(1 + \frac{x}{3}\right)^3 = 1 + x + \frac{x^2}{3} + \frac{x^3}{27}.
$$

These are different polynomials, but the first two terms are the same.
More generally, we can ask: what do the polynomials $p_n(x) = (1+x/n)^n$ look
like?
And like the $1$ multiplying $x$, do coefficients in the polynomial $p_n(x)$ "stabilize" as $n$
gets large?
Our tool to explore this will be the *binomial theorem*.
This states that

$$
(1 + X)^n = 1 + \binom{n}{1}X + \binom{n}{2}X^2 + \cdots + \binom{n}{n}X^n,
$$

where

$$
\binom{n}{k} = \frac{n!}{(n-k)! k!}
$$

is the number of ways of choosing $k$ from $n$ objects, also called a
*binomial coefficient*.
I'm going to assume you know about binomial coefficients, but not
necessarily the binomial theorem.
But if you know about binomial coefficients, the theorem is easy!

When we expand $(1+X)^n$, we can generate terms by choosing either $1$
or $X$ in each factor.
To obtain a term $X^k$, in $k$ factors we choose $X$, and in the
remaining factors we choose $1$.
We add all our choices together to get the final answer, so the total
number of ways to get $X^k$ (and hence the coefficient) is just the
number of ways we can choose $k$ from a total of $n$ factors,
$\binom{n}{k}$.
Done!
Now we can figure out what the coefficient of $x^k$ looks like in
$p_n(x)$.
Setting $X = x/n$ in the binomial theorem, we find that

$$
p_n(x) = \left(1 + \frac{x}{n}\right)^n = 1 +
\binom{n}{1}\frac{x}{n} + \binom{n}{2}\frac{x^2}{n^2} + \cdots +
\binom{n}{n}\frac{x^n}{n^n}.
$$

For $k \leq n$, the coefficient of $x^k$ is

$$
\binom{n}{k}\frac{x^k}{n^k} = \left[\frac{n!}{(n-k)! n^k}\right] \frac{x^k}{k!},
$$

where we've separated it into a part which depends on $n$ and a part
which doesn't.
Let's focus on the stuff which depends on $n$, and see if we can
understand what happens when $n$ gets large.
We can write

$$
\begin{align*}
\frac{n!}{(n-k)! n^k} & = \frac{n \times (n-1) \times \cdots \times
(n-k+ 1)}{n^k} \\ & = \left(\frac{n}{n}\right) \times
\left(\frac{n-1}{n}\right) \times \cdots \times \left(\frac{n-k +
1}{n}\right),
\end{align*}
$$

where we've paired the factors of $n$ downstairs with factors of
$n!/(n-k)!$ upstairs.
If we fix $k$, and let $n$ get very large, each of these terms gets
very close to $1$. For instance, each term is bigger than

$$
\frac{n-k}{n} = 1 - \frac{k}{n},
$$

and as $n \to \infty$ with $k$ a fixed number, this approaches $1$.
So each term approaches $1$, and hence the product approaches $1$ as
$n$ gets large.
So we conclude that, as we take $n \to \infty$, the coefficient of
$x^k$ in $p_n(x)$ approaches $1/k!$.
In fact, we can view the exponential function as $p_\infty(x)$, a sort
of infinitely large polynomial with these coefficients:

$$
e^x = p_\infty(x) = 1 + x + \frac{x^2}{2!} + \cdots +
\frac{x^k}{k!} + \cdots
$$

This formula can rigorously established, and the infinite polynomial
$p_\infty(x)$ is called a *power series*. But
we will continue to play fast and loose with the rules, ignoring the
messy (and distracting) business of formal proof.

---

*Exercise 2.* The numerical approximation to $e$ from evaluating
$p_n(1)$ is very slow.
We present a much quicker algorithm here.

<span style="padding-left: 20px; display:block">
(a) Express $e$ in terms of the power series $p_\infty(x)$.
</span>

<span style="padding-left: 20px; display:block">
(b) From your answer to (a), create a method for approximating $e$
using $k$ rather than $n$. Use this to estimate $e$ to $10$ decimal places.
</span>

---

#### From compound interest to small change

Another unique property of the exponential is how it responds to
small changes.
Consider some tiny $\delta \ll 1$.
The usual index laws and the power series tell us that

$$
e^{x + \delta} = e^x e^{\delta} = e^x \left(1 + \delta +
\frac{\delta^2}{2!} + \cdots\right).
$$

If $\delta$ is very small, then most of the change is captured by
the linear term in the polynomial, $e^\delta \approx 1 + \delta$,
since all the higher terms, proportional to $\delta^2, \delta^3$,
and so on, are miniscule. More precisely, taking $\delta \ll 1$ and multiplying
both sides by $\delta$, we find that $\delta^2 \ll \delta$, and hence
$\delta^3 \ll \delta^2 \ll \delta$, and so on.
For instance, if $\delta = 0.001$, then

$$
e^\delta = 1.00100050\ldots \approx 1.001 = 1 + \delta.
$$

Our linear approximation has an error of less than one part in a
million.
Thus, under a very small change $\delta$,

$$
e^{x+\delta} - e^x \approx e^x
\left[(1 + \delta) - 1\right] = \delta e^x.
$$

So the response to a small change is *proportional to the function
itself*.
In fact, this gives another way to define the exponential!
But more importantly, it underlies the many application of the
exponential to real-world phenomena.

---

*Exercise 3.* A sample of Uranium-235 awaits testing. It has a
 *half-life* of $\lambda = 700$ million years, meaning that if there is a lump
 of $N$ Uranium-235 atoms, half of it will disappear after a time $\lambda$.

<span style="padding-left: 20px; display:block">
(a) Suppose we start with $N_0$ atoms. Using the analogy to compound
interest, argue that the number of atoms after time $t$ is
</span>

$$
N(t) = N_0 e^{-t/\lambda}.
$$

<span style="padding-left: 20px; display:block">
(b) If there are $10^{26}$ atoms in a lump, roughly how long does it
take for a single atom to decay? *Hint.* Use the formula for small changes.
</span>

---

#### Euler's formula

At this point, we are going to propose a remarkable reinterpretation
of the exponential in the complex plane $\mathbb{C}$.
In order to see how this comes about, we first have to review a few
facts about complex multiplication.
The one crazy idea, from which you can build everything else, is that
there is some "imaginary" number $i$ such that $i^2 = -1$.
A *complex number* has the form $z = x + iy$, where $x$ and $y$ are
real numbers.
We can picture these numbers as coordinates $(x, y)$ on the Cartesian
plane.
But unlike points on the Cartesian plane, there is now a natural way
to multiply two complex numbers, based on $i^2 = -1$:

$$
\begin{align*}
z_1 z_2 & = (x_1 + iy_1)(x_2 + iy_2) \\ & = x_1 x_2 + i(x_1 y_2 + y_2 x_1) +
i^2 y_1 y_2 \\
& = (x_1 x_2 - y_1 y_2) + i(x_1 y_2 + y_2 x_1).
\end{align*}
$$

This rule seems a bit fiddly, but becomes much more transparent in
*polar* coordinates on the plane.
Recall that instead of specifying the $x$ and $y$ components, we can
specify the angle $\theta$ from the positive $x$ axis and distance $r$
from the origin.
These give the $x$ and $y$ components using the usual rules of
trigonometry:

$$
x = r \cos \theta, \quad y = r \sin\theta.
$$

We denote the corresponding complex number $z(r, \theta)$.
Let's multiply two such complex numbers:

$$
\begin{align*}
z(r_1, \theta_1) z(r_2, \theta_2) & = r_1 (\cos\theta_1 + i\sin
\theta_1) \cdot r_2 (\cos\theta_2 + i\sin \theta_2) \\
& = r_1 r_2
[(\cos\theta_1 \cos\theta_2 - \sin\theta_1 \sin\theta_2) + i (\cos\theta_1 \sin\theta _ 2 + \sin\theta_1 \cos\theta _ 2)].
\end{align*}
$$

This still looks like a mess, but we can simplify dramatically using
the compound angle formulas:

$$
\begin{align*}
\cos(\theta_1 + \theta_2) & = \cos\theta_1 \cos\theta_2 - \sin\theta_1
\sin\theta_2\\
\sin(\theta_1 + \theta_2) & = \cos\theta_1 \sin\theta _ 2 +
\sin\theta_1 \cos\theta _ 2.
\end{align*}
$$

Applying these to $z(r_1, \theta_1)z(r_2,\theta_2)$ immediately gives

$$
z(r_1, \theta_1) z(r_2, \theta_2) = r_1 r_2
[\cos (\theta_1 + \theta_2) + i \sin (\theta_1 + \theta_2)] = z(r_1
r_2, \theta_1+\theta_2).
$$

In other words, a product of two complex numbers simply multiplies the
lengths and adds the angles.

#### Ramanujan's mysterious sum
