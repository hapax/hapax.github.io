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

### Contents

1. <a href="#sec-1">Compound interest</a>
2. <a href="#sec-2">An infinite polynomial</a>
3. <a href="#sec-3">From compound interest to small change</a>
4. <a href="#sec-4">Euler's formula</a>
5. <a href="#sec-5">Ramanujan's mysterious sum</a>

#### 1. Compound interest <a id="sec-1" name="sec-1"></a>

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

#### 2. An infinite polynomial <a id="sec-2" name="sec-2"></a>

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
We can view the exponential function as $p_\infty(x)$, a sort
of infinitely large polynomial with these coefficients:

$$
e^x = p_\infty(x) = 1 + x + \frac{x^2}{2!} + \cdots +
\frac{x^k}{k!} + \cdots.
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

#### 3. From compound interest to small change<a id="sec-3" name="sec-3"></a> 

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
This even gives another way to define the exponential!
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

#### 4. Euler's formula<a id="sec-4" name="sec-4"></a>

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
specify the angle $\theta$ (in radians) from the positive $x$ axis and distance $r$
from the origin.
These give the $x$ and $y$ components using the usual rules of
trigonometry:

$$
\begin{align*}
x & = r \cos \theta, \quad y = r \sin\theta \\
r = \sqrt{x^2 + y^2}, \quad \theta = \tan^{-1}\left(\frac{y}{x}\right).
\end{align*}
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
Great! Now we can make magic happen.
Without stopping to worry too much, let's just plug an *imaginary*
number into the exponential function, and use our formula for compound interest:

$$
e^{i\theta} = \lim_{n\to\infty} \left(1 + \frac{i\theta}{n}\right)^n.
$$

We know about complex multiplication, so we can understand $e^{i\theta}$ by analyzing the term in brackets:

$$
z_n = 1 + \frac{i\theta}{n} = z_n(r_n, \theta_n).
$$

Then

$$
e^{i\theta} = z(r_\infty, \theta_\infty), \quad r_\infty =
\lim_{n\to\infty} r_n^n, \quad \theta_\infty = \lim_{n\to\infty} n\theta_n.
$$

From the formulas for converting from Cartesian to polar coordinates,
we have a radius

$$
r_n^2 = 1 + \frac{\theta^2}{n^2}.
$$

When $n$ gets large, this gets very close to $1$. In fact, you can
prove in Exercise 4 below that

$$
r_\infty = \lim_{n\to \infty} r_n^{n} = 1.
$$

So $e^{i\theta}$ lies a unit distance from the origin.
The angle $\theta_n$ is a bit trickier. The conversion formula tells
us that

$$
\theta_n = \tan^{-1}\left(\frac{y_n}{x_n}\right) = \tan^{-1}\left(\frac{\theta}{n}\right).
$$

For large $n$, $\theta/n$ is very small, so the small angle
approximation $\tan^{-1} x \approx x$ tells us that

$$
\theta_n \approx \frac{\theta}{n},
$$

and this approximation becomes better and better as $n$ increases.
But then

$$
\theta_\infty = \lim_{n \to \infty} n\theta_n = \theta.
$$

Hence, $e^{i\theta} = z(1, \theta)$, or

$$
e^{i\theta} = \cos\theta + i \sin\theta.
$$

This result was first derived by [Leonhard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler) and hence is called *Euler's
formula.*
It is nothing short of a miracle, and yields an equation often said to be the most beautiful in
mathematics:

$$
e^{i\pi} = \cos\pi + i \sin\pi = -1.
$$

There are many wonderful things that can be done with Euler's
formula, most of which we leave for another time.
Our one example will be Exercise 5, where we use it to give "infinite polynomial" versions of sine and cosine.

---

*Exercise 4.* We will step through a (heurist) proof that $r_\infty = 1$.

<span style="padding-left: 20px; display:block">
(a) Use the binomial theorem to show that
</span>

$$
\left(1 + \frac{\theta^2}{n^2}\right)^n = 1 +
\binom{n}{1}\left(\frac{\theta}{n}\right)^2 +
\binom{n}{2}\left(\frac{\theta}{n}\right)^4 + \cdots + \binom{n}{n}\left(\frac{\theta}{n}\right)^{2n}.
$$

<span style="padding-left: 20px; display:block">
(b) From this answer, deduce that the coefficient of
$\theta^{2k}$, for $k \geq 1$, can be written
</span>

$$
\frac{n!}{(n-k)!n^{k}} \cdot \frac{1}{n^k} \cdot \frac{1}{k!}.
$$

<span style="padding-left: 20px; display:block">
(c) Use the fact that the first term approaches $1$ (which we argued
loosely above) to conclude that the whole term vanishes as
$n\to\infty$.
</span>

In other words, in the limit $n \to \infty$, only the first term $1$
of the infinite polynomial survives. Hence, $r_\infty = 1$.

<p align="center">
  ⁂
  </p>

*Exercise 5.* Let's suppose that the infinite polynomial expression
still holds for $e^{i\theta}$, so that

$$
e^{i\theta} = p_\infty(i\theta) = 1 + i\theta + \frac{(i\theta)^2}{2!} + \cdots +
\frac{(i\theta)^k}{k!} + \cdots.
$$

Euler's formula tells us that the real part of this formula is
$\cos\theta$ and the imaginary part (multiplying $i$) is $\sin\theta$.

<span style="padding-left: 20px; display:block">
(a) By simplifying the factors of $i$ in $p_\infty(i\theta)$, argue
that
</span>

$$
\cos\theta = 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} + \cdots +
\frac{(-1)^k\theta^{2k}}{(2k)!} + \cdots.
$$

<span style="padding-left: 20px; display:block">
(b) Similarly, by consider the part proportional to $i$, argue that
sine can be written as an infinite polynomial:
</span>

$$
\sin\theta = \theta - \frac{\theta^3}{3!} + \cdots +
\frac{(-1)^k\theta^{2k+1}}{(2k+1)!} + \cdots.
$$

<span style="padding-left: 20px; display:block">
(c) Create numerical routines to calculate $\cos\theta$
and $\sin\theta$, like you did for $e$ in Exercise 2.
</span>

---

#### 5. Ramanujan's mysterious sum <a id="sec-1" name="sec-1"></a>

As miraculous as Euler's formula is, when we make the connection
between compound interest and compound angles, it becomes clear why it
works.
An equation which seems so miraculous as to be blatantly wrong is the
following:

$$
1 + 2 + 3 + 4 + \cdots = -\frac{1}{12}.
$$

It is a paradox: the sum of all the positive natural numbers is
apparently not only finite, but negative!
Although it seems insane, there is a rigorous way to interpret this
statement.
Some speculate that Euler may have known about it, but the first
person to write it down and clearly understand it was
[Srinivasa Ramanujan](https://en.wikipedia.org/wiki/Srinivasa_Ramanujan).
Our approach, which differs from Ramanujan's, is the one used by
physicists, and we will focus on a "physical" understanding of the equation.

We need one more elementary fact to get started.
Recall the *geometric series*, stating that if $|r| < 1$, then
the sum of its powers is

$$
1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r}.
$$

The argument, if you haven't seen it, is simplicity itself.
Let $s$ be the series.
Then

$$
s - 1 = r + r^2 + r^3 + \cdots = r (1 + r + r^2 + \cdots ) = rs \quad
\Longrightarrow \quad s = \frac{1}{1-r}.
$$

Now we can begin our magic show.
First, set $r = e^{-x}$ in the geometric series:

$$
s_x = 1 + e^{-x} + e^{-2x} + e^{-3x} + \cdots = \frac{1}{1-e^{-x}}.
$$

Consider a small change, $x \to x + \delta$ for $\delta \ll 1$:

$$
s_{x+\delta} = 1 + e^{-(x+\delta)} + e^{-2(x+\delta)} + e^{-3(x+\delta)} + \cdots = \frac{1}{1-e^{-(x+\delta)}}.
$$

To compare to the first the terms on the LHS, we can use the formula for small changes:

$$
e^{-kx} - e^{-k(x+\delta)} \approx k \delta e^{-kx}.
$$

Hence, we can write

$$
s_{x} - s_{x+\delta} \approx \delta e^{-x} + 2 \delta e^{-2x} + 3
\delta e^{-3x} + \cdots.
$$

On the right, we have a sum which is looking potentially helpful,
since the natural numbers now appear out the front of the exponential
powers.
But to evaluate the LHS more explicitly, we can sum the two geometric
series:

$$
\begin{align*}
s_{x} - s_{x+\delta} & = \frac{1}{1-e^{-x}} -
\frac{1}{1-e^{-(x+\delta)}}\\
& = \frac{e^{-x}-e^{-(x+\delta)}}{(1-e^{-x})(1-e^{-(x+\delta)})} \\
& \approx \frac{\delta e^{-x}}{(1-e^{-x})(1-e^{-(x+\delta)})}.
\end{align*}
$$

Equating our two expressions, dividing by $\delta$, and setting
$\delta = 0$ (where the approximation becomes exact) we get the equation

$$
\frac{e^{-x}}{(1-e^{-x})^2} = e^{-x} + 2 e^{-2x} + 3
e^{-3x} + \cdots.
$$

To get the sum of natural numbers on the RHS, we would like to take
$x \to 0$, so that $e^{-x} = 1$.
On the LHS, the denominator will go to zero, so the whole expression
will blow up, which is what we expect.
But we will do this a bit more carefully, keeping track of powers of
$x$.
First, observe that

$$
1 - e^{-x} = 1 - \left(1 - x + \frac{x^2}{2} - \frac{x^3}{6} + \cdots \right) =
x\left(1 - \frac{x}{2} + \frac{x^3}{6} \cdots\right),
$$

and hence, using the geometric series in reverse,

$$
\begin{align*}
\frac{1}{1 - e^{-x}} & = \frac{1}{x\left(1 - x/2 + x^2/6
\cdots\right)} \\
& =
\frac{1}{x}\left[1 + \left(x/2 - x^2/6\right) + \left(x/2 - x^2/6\right)^2 + \cdots\right] \\
& =
\frac{1}{x}\left[1 + \frac{x}{2} - \frac{x^2}{6} + \frac{x^2}{4} + \cdots\right] =
\frac{1}{x}\left[1 + \frac{x}{2} + \frac{x^2}{12} + \cdots\right].
\end{align*}
$$

Finally, we can combine all these terms together in the expression

$$
\begin{align*}
\frac{e^{-x}}{(1-e^{-x})^2} & = \frac{1}{x^2}\left(1 - x +
\frac{x^2}{2} + \cdots\right)\left(1 + \frac{x}{2} + \frac{x^2}{12} +
\cdots\right)^2.
\end{align*}
$$

We can multiply out all the terms in brackets (or use
[WolframAlpha](https://www.wolframalpha.com/input/?i=expand+%281+-+x+%2B+x%5E2%2F2%29%281+%2B+x%2F2+%2B+x%5E2%2F12%29%5E2)),
and find that

$$
\begin{align*}
\frac{e^{-x}}{(1-e^{-x})^2} & = \frac{1}{x^2}\left(1 -\frac{x^2}{12} +
\cdots \right) \\
& = \frac{1}{x^2} - \frac{1}{12} + \cdots.
\end{align*}
$$

where the $\cdots$ stand for positive powers of $x$.
So, all in all, we have

$$
\frac{1}{x^2} - \frac{1}{12} + \cdots = e^{-x} + 2 e^{-2x} + 3
e^{-3x} + \cdots.
$$

As we take $x \to 0$, $e^{-kx} \to 1$ and hence the RHS gives us the
sum of natural numbers.
On the LHS, the powers of $x$ (in the $\cdots$) vanish, and the
$1/x^2$ term blows up.
