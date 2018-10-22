---
layout: post
mathjax: true
comments: true
title:  "The Basel trick"
date:   2015-07-04
---

The Basel problem (first posed in 1644) is the challenge of summing reciprocal squares, 

$$ 
\sum_{k=1}^\infty\frac{1}{k^2} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \cdots = \,\,? 
$$
 
The first person to solve it was Euler. His strategy is over-represented in expository math blogs, but I can't resist writing about it and describing a small extension Euler made. 
 
### The Basel problem
 
Euler started by representing the $\sin$ function as an infinite
product, something like a factorisation of the Taylor series. We can
write a polynomial $p(x)$ with roots $\{a_1, a_2, \ldots, a_n\}$ as 

$$ 
p(x) = C(x - a_1)(x - a_2)\cdots(x - a_n) = C\prod_{i = 1}^n(x - a_i) 
$$
 
for some constant $C$. Similarly, we can try to write $\sin(x)$ as a product of terms corresponding to its zeros at $\pi k \in \mathbb{Z}$: 

$$ 
\begin{align*} 
\sin(x) & = C \prod_{k\in\mathbb{Z}}(x - \pi k) \\ 
& = C x \prod_{k\geq 1}(x - \pi k)(x + \pi k) \\ 
& = C x \prod_{k\geq 1}(x^2 - \pi^2 k^2). 
\end{align*} 
$$
 
At this point, we run into a problem: this expression will never
converge for any finite $x$, since the factors blow up as $|k| \to
\infty$.
To stop this from happening, we divide the $k$th (quadratic)
term through by $-\pi^2k^2$. This gives us factors which approach $1$
as $k \to \infty$ (the infinite product version of the divergence
test) without changing the roots. (We imagine lumping all of these
terms into $C$.) Now, divide through by $x$ and then send $x \to 0$:

$$ 
\lim_{x\to 0}\frac{\sin(x)}{x} = 1. 
$$
 
This tells us we should set $C = 1$ (after dividing out the problematic terms). So, we have the heuristic relation 

$$ 
\frac{\sin(x)}{x} = \prod_{k\geq 1}\left(1 - \frac{x^2}{\pi^2 k^2}\right). 
$$
 
It turns out this identity is true, and can be proved using complex analysis. In general, convergence of these infinite products is a delicate matter, and we ignore it completely in what follows. 
 
Euler's ingenious trick was to identify the coefficient of $x^2$ on either side. On the left, the Taylor series for $\sin(x)/x$ 

$$ 
\frac{\sin(x)}{x} = \sum_{n\geq 0} \frac{(-1)^n x^{2n}}{(2n+1)!} = 1 - \frac{x^2}{6} + \mathcal{O}(x^4) 
$$
 
gives a coefficient $-1/6$. On the right, we can formally extend the result for polynomials 

$$ 
\prod_{i=1}^n (1 - a_i x) = 1 - x\sum_{i=1}^n a_i + \mathcal{O}(x^2) 
$$
 
to infinite series to obtain the coefficient 

$$ 
-\sum_{k\geq 1} \frac{1}{\pi^2k^2}= -\frac{1}{\pi^2}\sum_{k\geq 1} \frac{1}{k^2}. 
$$
 
Equating gives Euler's answer to the Basel problem, 

$$ 
\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}. 
$$
 
Cool! We can obtain the same result in other ways, notably the <a href="http://theruinedstar.blogspot.com.au/2011/08/cotangent-and-even-values-of-zeta.html">cotangent method</a>, the Fourier series for $f(x) = x$ and an elementary "Proofs from the Book" method, but Euler's approach is the original and (I think) the best. 
 
### Euler's trick for higher terms
 
At this point, it's natural to try the same trick for higher terms in the Taylor series. Let's look at $x^4$. On the left, we have 

$$ 
\frac{(-1)^2}{5!} = \frac{1}{120}. 
$$
 
On the right, we have something more complicated. Let's clean up our notation, and define 

$$ 
\prod_{i\geq 1}(1 + a_i x) = \sum_{n\geq 0}A_n x^n. 
$$
 
We have already used the result 

$$ 
A_1 = \sum_{i\geq0}a_i. 
$$
 
Generally, $A_n$ will be a sum of products of $n$ distinct $a_i$, since each will contribute a factor of $x$ and occurs by choosing the $x$ term in the corresponding factors and the $1$ term in all remaining factors. Conversely, this is the <i>only </i>way to get an $x^n$ term. Hence, 

$$ 
A_n = \sum_{i_1 < \cdots < i_n} a_{i_1}\cdots a_{i_n}. 
$$
 
This is complete and general, but hard to work with. Let's repackage $A_2$ in a useful way. We have 

$$ 
A_2 = \sum_{i < j} a_ia_j = \frac{1}{2}\sum_{i \neq j} a_ia_j = \frac{1}{2}\left(\sum_{i, j} a_ia_j - \sum_{i}a_i^2\right) = \frac{1}{2}\big(A_1^2 - A_1^{(2)}\big), 
$$
 
where $A_1^{(k)} = \sum_i a_i^k$. Finally, we go back to evaluating the coefficient of $x^4$ on the right hand side. Since $a_k = -1/(\pi k)^2$ and $A_1 = -1/6$, the coefficient on the right is 

$$ 
\begin{align*} 
\frac{1}{2}\big(A_1^2 - A_1^{(2)}\big) & = \frac{1}{2}\left(\frac{1}{36} - \frac{1}{\pi^4}\sum_{k\geq 0}\frac{1}{k^4}\right). 
\end{align*} 
$$
 
Setting this equal to $1/120$ and rearranging, we obtain 

$$ 
\sum_{k\geq 0}\frac{1}{k^4} = \frac{\pi^4}{90}. 
$$
 
We could go on in a similar way, producing ad hoc recurrences for $A_n$ in terms of smaller $A_m$ and $A_1^{(n)}$. In fact, Euler did so, calculating coefficients all the way up to $x^{26}$, but this ad hoc method is tedious and inefficient. 
 
It would be nice if one could find an expression for $A_n$ (which in our case is known) in terms of $A_1^{(k)}$ (which we would like to know). We would be hoping for something like the recurrence satisfied by the Bernoulli numbers, since with the benefit of hindsight, we know that $A_1^{(k)} \propto B_{2k}$. Sadly, the author has yet to undertake this endeavour!
