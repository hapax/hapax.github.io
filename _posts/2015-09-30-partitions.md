---
layout: post
mathjax: true
comments: true
title:  "Partitions, pentagons and products"
categories: Mathematics
date:   2015-09-30
---

**September 30, 2015.** *Partitions are the additive equivalent of
  primes, telling us how many ways we can add (rather than multiply)
  smaller numbers to get a given natural number. Euler proved a lovely
  result about the number of partitions which, surprisingly, involves
  pentagons. I'll show one way to obtain this result from Jacobi's
  triple product formula.*

### Introduction

*Prerequisites: calculus, power series.* 
 
A *partition* of a natural number $n \in \mathbb{N}$ is a multiset of natural numbers which add up to $n$. (By "multiset", I mean elements can be repeated but order is unimportant.) For instance, the number $4$ has $5$ partitions: 
\begin{align} 
4 &= 3 + 1 = 2+2 = 2 + 1 + 1 = 1 + 1 + 1 + 1. 
\end{align}Like prime numbers, the study of partitions connects different aspects of number theory in a deep way. Also like prime numbers, many problems involving partitions are simple to state but very hard to solve. The simplest problem is just counting partitions: how many ways can we partition $n$? A 1937 result due to Hans Rademacher (improving on a related formula of Hardy and Ramanujan) is close to the state of the art today: 

$$ 
p(n) = \frac{1}{\pi\sqrt{2}}\sum_{k=1}^\infty \sqrt{k}A_k(n)\frac{d}{dn}\left[\frac{1}{\sqrt{n-1/24}}\sinh\left(\frac{\pi}{k}\sqrt{\frac{2}{3}\left(n-\frac{1}{24}\right)}\right)\right], 
$$

where the coefficient 

$$ 
A_k(n) = \sum_{0\leq m<  k, \,\gcd(m,k)=1}e^{\pi i [s(m, k) - 2nm/k]} 
$$

and $s(m, k)$ denotes another function called the <a href="https://en.wikipedia.org/wiki/Dedekind_sum">Dedekind sum</a>. We won't be interested in this formula. I mainly wanted to point out that the *simplest* question in partition theory has a very complicated answer! Despite that, we can prove *Euler's pentagon identity*, a rather neat result about partitions, using the elementary machinery of generating functions and infinite products. On the way, we will need to prove *Jacobi's triple product identity*, a deep and interesting result in its own right. We follow Andrews' approach in *Number Theory*. 

### Two product-sum lemmas
 
We start with two lemmas connecting infinite products and sums; we'll use these to show Jacobi's identity in the next section. 
 
**Lemma 1.** If $|q|<1$
,

$$ 
\sum_{n=0}^\infty \frac{q^{n(n-1)/2}z^n}{(1-q)(1-q^2)\cdots(1-q^n)} = \prod_{n=0}^\infty (1+zq^n). 
$$

(The denominator for the $n=0$ term on the left is by definition $1$.) To see this, let 

$$ 
f(z) \equiv \prod_{n=0}^\infty (1+zq^n). 
$$

Note that $f(z)$ satisfies a functional equation 

$$ 
f(z) = \prod_{n=0}^\infty (1+zq^n) = (1+z)\prod_{n=0}^\infty (1+(zq)q^{n}) = (1+z)f(qz). 
$$

Now, consider the Maclaurin expansion of $f(z)$: 

$$ 
\prod_{n=0}^\infty (1+zq^n) \equiv \sum_{n=0}^\infty A_n z^n. 
$$

For a proof that the expansion exists, see Andrews. Since the constant
term in each factor is $1$, we have $A_0 = 1$. From the functional
equation,

$$
\begin{align} 
\sum_{n=0}^\infty A_n z^n & = f(z) \\ 
& = (1+z)f(qz) \\ 
& = (1+z)\sum_{n=0}^\infty A_n (qz)^n \\ 
& = \sum_{n=0}^\infty (A_n q^n + A_n q^n z) z^n = \sum_{n=0}^\infty (A_n q^n + A_{n-1} q^{n-1}) z^n. 
\end{align}
$$

From the uniqueness of the Maclaurin coefficients, we find the recurrence 

$$ 
A_n = A_n q^n + A_{n-1} q^{n-1} \quad \Longrightarrow \quad A_n = \frac{q^{n-1}}{(1-q^n)}A_{n-1}. 
$$

We can easily use the recurrence to express $A_n$ in terms of $A_0 = 1$: 
\begin{align} 
A_n = A_0\prod_{k=1}^{n}\frac{q^{k-1}}{(1-q^{k})} = \frac{q^{1+2+\cdots (n-1)}}{(1-q)\cdots (1-q^n)} = \frac{q^{n(n-1)/2}}{(1-q)\cdots (1-q^n)} 
\end{align}using the identity 

$$ 
1 + 2 + \cdots + (n-1) = \binom{n}{2} = \frac{n(n-1)}{2}. 
$$

Finally, you can check the ratio of terms 

$$ 
\frac{A_{n+1}}{A_n} = \frac{q^{n(n+1)/2}}{(1-q)\cdots (1-q^{n+1})}\frac{(1-q)\cdots (1-q^n)}{q^{n(n-1)/2}} = \frac{q^n}{1-q^{n+1}} \to 0 
$$

for $|q|<1$.
Hence, the power series converges for all values of $z$ by the ratio test. 
 
 **Lemma 2.** Similarly, provided $|q|,|z|<1$
 ,

$$ 
\sum_{n=0}^\infty \frac{z^n}{(1-q)(1-q^2)\cdots(1-q^n)} = \prod_{n=0}^\infty \frac{1}{1-zq^n}. 
$$

The proof is similar is Lemma 1. We define 

$$ 
g(z) \equiv \prod_{n=0}^\infty \frac{1}{1-zq^n} \equiv \sum_{n=0}^\infty B_n z^n. 
$$

The functional equation is now 

$$ 
g(qz) = (1-z)g(z), 
$$

and as before this leads to a recurrence: 

$$ 
B_n q^n = B_n - B_{n-1} \quad \Longrightarrow\quad B_n = \frac{1}{1 - q^n}B_{n-1}. 
$$

Since $B_0 = 1$, we clearly have 

$$ 
B_n = \frac{1}{(1 - q)\cdots(1-q^n)}. 
$$

You can check that $B_{n+1}/B_n \to 1$
for $|q| < 1\~$
,
and so the power series converges for $|z| < 1\~$
.
 
### Jacobi's triple product identity
 
We can combine the lemmas to prove the *triple product identity*: for $z \neq 0$ and $|q| < 1$, 

$$ 
\prod_{n=0}^\infty (1-q^{2n+2})(1+zq^{2n+1})(1+z^{-1}q^{2n+1}) = \sum_{n=-\infty}^\infty q^{n^2}z^n. 
$$

To begin with, we assume that $|z| > |q|$
and $|q| < 1$.
In Lemma 1, make the replacements $z\to qz$ and $q \to q^2$. (Note
that constraint on $q$ is still $|q| < 1$.)
This gives 

$$ 
\sum_{n=0}^\infty \frac{q^{n^2}z^n}{(1-q^2)\cdots(1-q^{2n})} = \prod_{n=0}^\infty (1+zq^{2n+1}). 
$$

We can trivially rewrite the denominator on the left as 

$$ 
\frac{1}{(1-q^2)\cdots(1-q^{2n})} = \prod_{m=0}^\infty \frac{1 - q^{2m + 2n + 2}}{1 - q^{2m + 2}}. 
$$

We can factor this into two distinct products:

$$
\begin{align} 
\prod_{n=0}^\infty (1+zq^{2n+1}) &= \sum_{n=0}^\infty q^{n^2}z^n\prod_{m=0}^\infty \frac{1 - q^{2m + 2n + 2}}{1 - q^{2m + 2}}\\ 
& = \prod_{m=0}^\infty \frac{1}{1-q^{2m+2}}\sum_{n=0}^\infty q^{n^2}z^n \prod_{l=0}^\infty(1 - q^{2l + 2n + 2}). 
\end{align}
$$

If $n$ is negative, the corresponding term in the sum vanishes, since the $l = -n$ factor in the product vanishes. So we can extend the summation to negative integers to get 

$$
\begin{align} 
\prod_{n=0}^\infty (1+zq^{2n+1}) & = \prod_{m=0}^\infty \frac{1}{1-q^{2m+2}}\sum_{n=-\infty}^\infty q^{n^2}z^n \prod_{l=0}^\infty(1 - q^{2l + 2n + 2}). 
\end{align}
$$

We can rewrite the last product on the right by making the replacements $q\to q^2$, $z \to -q^{2n+2}$ in Lemma 1 to get 

$$ 
\prod_{l=0}^\infty (1-q^{2l+2n+2}) = \sum_{l=0}^\infty \frac{(-1)^lq^{l^2 + 2nl+l}}{(1-q^2)\cdots(1-q^{2l})}. 
$$

Thus, we get

$$
\begin{align} 
\prod_{n=0}^\infty (1+zq^{2n+1}) &= \prod_{m=0}^\infty \frac{1}{1-q^{2m+2}}\sum_{n=-\infty}^\infty q^{n^2}z^n \prod_{l=0}^\infty(1 - q^{2l + 2n + 2})\\ 
& = \prod_{m=0}^\infty \frac{1}{1-q^{2m+2}}\sum_{n=-\infty}^\infty q^{n^2}z^n\sum_{l=-0}^\infty\frac{(-1)^lq^{l^2+2nl+l}}{(1-q^2)\cdots(1-q^{2l})} \\ 
& = \prod_{m=0}^\infty \frac{1}{1-q^{2m+2}}\sum_{l=-0}^\infty\sum_{n=-\infty}^\infty \frac{(-1)^lq^l q^{(l+n)^2}z^n}{(1-q^2)\cdots(1-q^{2l})}\\ 
& = \prod_{m=0}^\infty \frac{1}{1-q^{2m+2}}\sum_{n=-\infty}^\infty q^{n^2}q^n \sum_{l=-0}^\infty \frac{(-qz^{-1})^l}{(1-q^2)\cdots(1-q^{2l})}, 
\end{align}
$$

where in the second last step we simply shifted the $n$ dummy variable $n \to n - l$. This only works since the summation is over all of $\mathbb{Z}$! To simplify the $l$ summation, we appeal to Lemma 2 with the formal replacements $q \to q^2$, $z \to -qz^{-1}$: 

$$ 
\sum_{l=0}^\infty \frac{(-qz)^l}{(1-q^2)\cdots(1-q^{2l})} = \prod_{l=0}^\infty \frac{1}{1+z^{-1}q^{2l+1}}. 
$$

According to the conditions of the lemma, this only holds for
$|qz^{-1}| = |q|/|z| < 1$, or $|z| > |q|$, which we've assumed is
true. Finally, we have

$$
\begin{align} 
\prod_{n=0}^\infty (1+zq^{2n+1}) & = \prod_{m=0}^\infty \frac{1}{1-q^{2m+2}}\sum_{n=-\infty}^\infty q^{n^2}q^n \prod_{l=0}^\infty \frac{1}{1+z^{-1}q^{2l+1}}. 
\end{align}
$$

Shifting all the products onto the left and labelling with a single
index, we have the triple product identity for $|z| > |q|$: 

$$ 
\prod_{n=0}^\infty (1-q^{2n+2})(1+zq^{2n+1})(1+z^{-1}q^{2n+1}) = \sum_{n=-\infty}^\infty q^{n^2}z^n. 
$$

The left-hand side is invariant under $z \to z^{-1}$. For the
right-hand side, we note that if we make the change $z \to z^{-1}$, we
just change the dummy variable $n\to -n$, so the right-hand side is
also invariant. In other words, the result also holds for $|z| <|q|$.
You can check that the right hand side converges for $|z| = |q|$
and $|q| < 1$
(compare with a geometric series), and since this is a
Laurent series for the left-hand side, the left also converges for
$|z| = |q|$. The one case we haven't covered so far is $z = 0$, for
which Jacobi's identity clearly doesn't work: the right hand side
vanishes but the left does not.
 
### Euler's pentagonal number theorem
 
Euler's theorem follows almost trivially from Jacobi's
identity. Working out its significance takes a bit more effort! Let $0
< |q| < 1$. In the product identity, make the substitutions $q \to
q^{3/2}$ and $z \to -q^{-1/2}$. I'll let you check that these values
of $q$ and $z$ satisfy the conditions. Then 

$$ 
\prod_{n=0}^\infty (1-q^{3n+3})(1-q^{3n+1})(1-q^{3n+2}) = \sum_{n=-\infty}^\infty (-1)^nq^{n(3n - 1)/2}. 
$$

Note that the indices of $q$ in the infinite product on the left hit
each nonnegative integer precisely once: it iterates over them in
groups of three. In other words, for $0 < |q| < 1$,

$$ 
\sum_{n=-\infty}^\infty (-1)^nq^{n(3n - 1)/2} = \prod_{n=0}^\infty (1-q^{n}). 
$$

This is Euler's pentagonal number theorem, which Euler first proved
with different methods in 1748. To see the significance of the result,
we need to relate it to pentagons and partitions.
 
#### Pentagons
 
The powers of $q$ appearing in the sum are <a href="https://en.wikipedia.org/wiki/Pentagonal_number" style="font-style: italic;">generalised pentagonal numbers</a>. Ordinary pentagonal numbers are illustrated below: 
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-8HYAA5Bd4wE/VgvS2cOWOZI/AAAAAAAABX0/OOkCiiEPbhU/s1600/pentagonal.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://1.bp.blogspot.com/-8HYAA5Bd4wE/VgvS2cOWOZI/AAAAAAAABX0/OOkCiiEPbhU/s1600/pentagonal.jpg" /></a></div>
In other words, $P_n$ is the number of points in a figurate pentagonal lattice of side length $n$. From the geometry, we get a recurrence 

$$ 
P_{n+1} = (3n+1) + P_{n}. 
$$

Thus, 
\begin{align} 
P_n & = 1 + \sum_{k=1}^{n-1} (3k + 1) = 1 + \frac{3}{2}n(n - 1) + n - 1 = \frac{1}{2}n(3n-1). 
\end{align} Of course, this only works for $n \geq 0$. *Defining* $P_k \equiv k(3k-1)/2$ for $k \leq 0$ gives the generalised pentagonal numbers. 
 
#### Partitions
 
Now we see how partitions enter the picture. First, consider the
infinite product for $-1 < q < 1$, 

$$ 
\prod_{n=0}^\infty \frac{1}{1-q^{n}} = \prod_{n=0}^\infty \sum_{k=0}^\infty q^{nk} \equiv \sum_{n=0}^\infty a_n q^n, 
$$

where I've defined the Maclaurin expansion coefficients $a_n$. It turns out that $a_n = p(n)$, the number of partitions of $n$. To see this, just note that in order to get a summand of $1$ in the Maclaurin coefficient of $q^n$, we have to pick $q$ factors on the left which add up to $n$. The number of ways of doing this is precisely the number of partitions of $n$. But the infinite product is just the reciprocal of the infinite product that occurs in Euler's identity. It's helpful to rewrite this as 

$$ 
\prod_{n=0}^\infty (1-q^{n}) = \sum_{k=-\infty}^\infty (-1)^kq^{k(3k - 1)/2} \equiv \sum_{n=0}^\infty b(n) q^n, 
$$

where $b(n) = (-1)^k$ if $n = P_k$ and $0$ otherwise. Then, using the
<a href="https://en.wikipedia.org/wiki/Cauchy_product">Cauchy
product</a> for two power series,

$$
\begin{align} 
1 & = \prod_{n=0}^\infty (1-q^{n}) \cdot \prod_{n=0}^\infty \frac{1}{1-q^{n}} \\ 
& = \sum_{n=0}^\infty b(n) q^n \cdot \sum_{n=0}^\infty p(n) q^n\\ 
& = \sum_{n = 0}^\infty q^n \sum_{j=0}^n b(j)p(n-j). 
\end{align}
$$

Matching coefficients, we find that for $n &gt; 1$, 

$$ 
\sum_{j=0}^n b(j)p(n-j) = 0. 
$$

Since $b(0) = 1$, we can rewrite this as a simple, beautiful recurrence: 

$$ 
p(n) = -\sum_{j=1}^n b(j)p(n-j) = -\sum_{k = -\infty}^\infty (-1)^{P_k}p(n - P_k) 
$$

or even more explicitly 

$$ 
p(n) = p(n-1) + p(n - 2) - p(n - 5) - p(n - 7) \pm \cdots 
$$

The ellipses terminate, since by definition $p(k) = 0$ for $k < 0$ and there are only a finite number of pentagonal numbers less than $n$. And there you have it! Another stunning result courtesy of Euler. 

### References

- *Number Theory* (1971), George Andrews.
- ["On Euler's Pentagonal Theorem"](http://www.mathpages.com/home/kmath623/kmath623.htm), Mathpages.
