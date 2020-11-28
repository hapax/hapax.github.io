---
Layout: post
mathjax: true
comments: true
title:  "Playing with exponentials"
categories: [Maths, Physics, Hacks]
date:  2020-11-28
---

**November 28, 2020.** *I discuss some of the key properties of the
  exponential function without (explicitly) invoking calculus.
  Starting with its relation to compound interest, we
  learn about its series expansion, Euler's formula, the sum of
  all positive numbers, and various other fun facts.*

#### An interesting limit

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
Proving this actually rather difficult, but it's easy to see with a
computer.
We can just plot $(1+r/n)^n$ for increasingly large $n$ and see that
it settles to a finite value.

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/exp-plot.png" width="50%"/>
	</div>
	</figure>

We show a few values for $r = 1$ above.
For large $n$, say a million, we get a number $2.71828...$.
Assuming it does converge, we use the $r =1$ limit to define the
famous mathematical constant $e$:

$$
e = \lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n \approx 2.781828.
$$

---

*Exercise 1.* Show that in the limit of "continuous" compound interest, i.e. large
$n$, the total value of our principal $I_0$ at the end of the year is

$$
I_{\text{comp}(n)} \to e^r I_0.
$$

*Hint.* Consider redefining $n$ so that the interest term looks more
 like the definition of $e$.

---
