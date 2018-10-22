---
Layout: post
mathjax: true
comments: true
title:  "Summing the natural numbers"
categories: [Mathematics, Teaching]
date:   2015-04-01
---

**April 1, 2015.** *According to a
  [now infamous Numberphile video](https://www.youtube.com/watch?v=w-I6XTVZXww),
  the sum of all natural numbers is -1/12. I explain two methods for
  getting this result, one rigorous and one non-rigorous, both due to Ramanujan.*

### Introduction

*Prerequisites: calculus, Stieltjes integration.*

Adding all the natural numbers together is grotesquely divergent, blowing up quadratically:

$$
1 + 2 + \cdots + n = \frac{1}{2}n(n + 1) = \mathcal{O}(n^2).
$$

Weirdly, though, this sum turns up in physical calculations such as the Casimir force in quantum field theory (and stringy extensions) where it is assigned the <i>finite</i> value<br />

$$
\sum_{n\geq 1} n = 1 + 2 + 3 + \cdots = -\frac{1}{12}.
$$

This seems like nonsense, but there are ways in which this is usefully true. For one thing, the Riemann zeta function $\zeta$ hints at this. Recall that, for $\Re(s) &gt; 1$, $\zeta$ is defined by<br />

$$
\zeta(s) = \sum_{n\geq 1}\frac{1}{n^s}.
$$

For $s = -1$, the formula above reduces to the sum of natural numbers. And it so happens that $\zeta(-1) = -1/12$ (as demonstrated in the first few pages of, e.g., Ivic's text on $\zeta$). Of course, the harmonic sum&nbsp;<i>isn't</i> valid there, but this result is suggestive.

Ramanujan discusses this series in one of his magical notebooks. We'll
look at his cute heuristic proof, and then a type of summation he
invented (<i>Ramanujan summation</i>) which makes the identity
true. Ramanujan summation hinges on a nice piece of classical analysis
called the <i>Euler-MacLaurin formula</i>.

### Ramanujan's heuristic proof
<div>
Ramanujan's first "proof" is similar in spirit to derivations of partial sums for the geometric series. The first move is to set</div>
<div>
\[<br />
\begin{align*}<br />
c &amp;= 1 + 2 + 3 + 4 \cdots \\<br />
4c &amp;= 4 + 8 + \cdots<br />
\end{align*}<br />
\]Subtracting the second from the first (matching to every second term) gives<br />
\[<br />
-3c = 1 - 2 + 3 - 4 + 5 - 6 + \cdots<br />
\]Now, look at the formal power series for $(1+ x)^{-2}$:<br />
\[<br />
\begin{align*}<br />
\frac{1}{(1+ x)^2} &amp; = -\frac{d}{dx}\frac{1}{1+x}\\<br />
&amp; = -\frac{d}{dx}(1 - x+ x^2 - x^3 + \cdots) \\<br />
&amp; = 1 + 2x - 3x^2 + 4x^3 - 5x^4 + \cdots<br />
\end{align*}<br />
\]If we substitute $x = 1$ on the right hand side, we get a divergent series equal to $-3c$. However, setting $x = 1$ on the left gives<br />
\[<br />
-3c = \frac{1}{(1 + 1)^2} = \frac{1}{4} \quad \Longrightarrow \quad c = -\frac{1}{12}.<br />
\]Again, we've broken some rules to get here (the power series doesn't converge for $x = 1$) but we're accumulating "moral" evidence.<br />

<h3>
The Euler-Maclaurin formula</h3>

The Euler-Maclaurin formula lets us rewrite summation over some function $f \in C^1[A, B]$ as integration plus some correction terms: a nice sum over derivatives of $f$ at the boundaries, and a remainder we can bound (or which will go away altogether). Assuming that $a, b \in \mathbb{Z}$ and $A \leq a &lt; b \leq B$, the formula states<br />
\[<br />
\begin{align*}<br />
\sum_{a \leq k \leq b} f(k) = &amp; \int_{a}^{b} f(t) \, dt + \tfrac{1}{2}(f(a) + f(b)) \\ &amp; + \sum_{m=1}^{n}\frac{B_{2m}}{(2m)!}(f^{(2m-1)}(b) - f^{(2m - 1)}(a)) + R_{2n+1}.<br />
\end{align*}<br />
\]where $B_m$ is the $m$th Bernoulli number. So, a sum may be replaced by an integral, up to some correction data which lives on the boundary (in $f$). The rest of this section is a proof of the formula, so you can skip it if you just want to see how Ramanujan did his magic.<br />
<br />
The proof is straightforward, but we need to introduce some polynomials. First, we define the&nbsp;<i>Bernoulli polynomials</i>, closed related to the Bernoulli numbers. The $m$th Bernoulli polynomial is the coefficient of a power series, defined by<br />
\[<br />
\frac{ze^{xz}}{e^z - 1} = \sum_{m \geq 0} B_m(x)\frac{z^m}{m!}.<br />
\]Since the Bernoulli numbers are defined by<br />
\[<br />
\frac{z}{e^z - 1} = \sum_{m \geq 0} B_m\frac{z^m}{m!}<br />
\]we see that $B_m(0) = B_m$. A little power series manipulation shows that<br />
\[<br />
B_1(x) = x - \tfrac{1}{2}.<br />
\]We now define the $m$th&nbsp;<i>periodic Bernoulli polynomial</i>&nbsp;$P_m(x) = B_m(x - \lceil x \rceil)$, where $\lceil \cdot \rceil$ denotes the roof function. Finally, we note that $B'_{m+1}(x) = (m+1)B_m(x)$, which can be obtained by identifying coefficients in\[<br />
\begin{align*}<br />
\sum_{m \geq 0} B'_m(x)\frac{z^m}{m!} &amp; = \frac{d}{dx}\sum_{m \geq 0} B_m(x)\frac{z^m}{m!}\\<br />
&amp; = \frac{d}{dx}\frac{ze^{xz}}{e^z - 1} \\&amp; = \frac{z^2e^{xz}}{e^z - 1} = \sum_{m \geq 1} B_{m-1}(x)\frac{z^m}{(m-1)!}.<br />
\end{align*}<br />
\]Note that we could also have defined the Bernoulli polynomials using $B_m(0) = B_m$ and the relation $B'_{m+1}(x) = (m + 1)B_m(x)$.<br />
<br />
Now we can prove the summation formula. A natural way to connect a sum and integral is to use <i>Stieltjes integration</i>, with integration measure<br />
\[<br />
dg = \frac{dg}{dx} \, dx.<br />
\]To get summation, we choose $g$ so the integration measure ends up being a periodic sum of Dirac delta functions. Thus, $g$ must be a step function with unit discontinuities at each integer, and a natural choice is $g(t) = \lceil t \rceil$. It follows that<br />
\[<br />
\begin{align*}<br />
\sum_{a \leq k \leq b} f(k) &amp; = \int_{a-}^{b+} f(t) \, d\lceil t\rceil \\<br />
&amp; = \int_{a}^{b} f(t) \, dt + \int_{a-}^{b+} f(t)\, d(\lceil t\rceil - t + \tfrac{1}{2}) \\<br />
&amp; = \int_{a}^{b} f(t) \, dt - \int_{a-}^{b+} f(t)\, dP_1(t)\\<br />
&amp; = \int_{a}^{b} f(t) \, dt + \tfrac{1}{2}(f(a) + f(b))+ \int_{a}^{b} f'(t)P_1(t)\,dt<br />
\end{align*}<br />
\]where on the last line we have integrated by parts. The periodic Bernoulli polynomials $P_m(x)$ satisfy the same differential equation as $B_m(x)$, so we can integrate the last term by parts as many times as we want:<br />
\[<br />
\begin{align*}<br />
\int_{a}^{b} f'(t)P_1(t)\,dt &amp; = \int_{a}^{b} f''(t)P_2(t)\,dt + \frac{1}{2}(P_2(b)f'(b) - P_2(a)f'(a)) \\<br />
&amp; = \int_{a}^{b} f^{(n+1)}(t)P_{n+1}(t)\,dt + \sum_{m=2}^{n+1}\frac{1}{m!}(P_{m}(b)f^{(m-1)}(b) -&nbsp;P_{m}(a)f^{(m-1)}(a)).<br />
\end{align*}<br />
\]Let's call the integral on the last line $R_{n+1}$. Since $P_m(a) = P_m(b) = B_m$ and $B_{2m + 1} = 0$ for $m \geq 1$, we can simplify the whole shebang to<br />
\[<br />
\begin{align*}<br />
\sum_{a \leq k \leq b} f(k) = &amp; \int_{a}^{b} f(t) \, dt + \tfrac{1}{2}(f(a) + f(b)) \\ &amp; + \sum_{m=1}^{n}\frac{B_{2m}}{(2m)!}(f^{(2m-1)}(b) - f^{(2m - 1)}(a)) + R_{2n+1}<br />
\end{align*}<br />
\] as claimed.<br />
<h3>
Ramanujan summation</h3>
Now, suppose the remainder $R_{2n+1}$ vanishes as $n \to \infty$. If we set $a = 0$ and let $b = x$ vary, and subtract $f(0)$ from both sides, we get<br />
\[<br />
\begin{align*}<br />
\sum_{k = 1}^x f(k) &amp; = \int_{0}^{x} f(t) \, dt + \tfrac{1}{2}(f(x) - f(0)) + \sum_{m=1}^{\infty}\frac{B_{2m}}{(2m)!}(f^{(2m-1)}(x) - f^{(2m-1)}(0)) \\<br />
&amp; = F(x) - \tfrac{1}{2}f(0) - \sum_{m=1}^{\infty}\frac{B_{2m}}{(2m)!}f^{(2m-1)}(0),<br />
\end{align*}<br />
\]where we've lumped all the $x$ dependence into some function $F$, and kept a constant term. Ramanujan <i>defined</i> the Ramanujan sum of $\{f(k)\}$ as this constant term:<br />
\[<br />
\sum_{k = 1}^\infty{}^{\![R]} f(k) = - \tfrac{1}{2}f(0) - \sum_{m=1}^{\infty}\frac{B_{2m}}{(2m)!}f^{(2m-1)}(0).<br />
\]His idea was that this constant term represented the finite part or
"centre of gravity" of the divergent series. Another way of thinking
about it is as what's left when you subtract enough terms to ensure
that the sum is finite at a point where it usually diverges. This way
of thinking suggests a connection to <i>renormalisation</i> techniques
from physics. For a great discussion of this point of view, see §16.3
of Matthew Schwartz's <a
href="https://schwartzqft.fas.harvard.edu/">QFT text</a>.<br />
<br />
Now, you might wonder what the Ramanujan sum of a&nbsp;<i>convergent&nbsp;</i>series is. Unfortunately, it's not usually the same as the convergent sum. Provided $f^{(k)}(x)$ vanishes for all $k \geq 0$ as $x \to \infty$, it's not hard to show that the relationship is<br />
\[<br />
\sum_{k = 1}^\infty{}^{\![R]} f(k) = \sum_{k = 1}^\infty f(k) - \lim_{n\to\infty}\int_1^n f(t)\,dt.<br />
\]Let's first check that it gives the right answer for the natural numbers, noting that $B_2 = -1/6$:<br />
\[<br />
\begin{align*}<br />
\sum_{k = 1}^\infty{}^{\![R]} k = - \tfrac{1}{2}f(0)- \sum_{m=1}^{\infty}\frac{B_{2m}}{(2m)!}f^{(2m-1)}(0) = -\frac{B_2}{2} = -\frac{1}{12}.<br />
\end{align*}<br />
\]Hooray! We'll finish by calculating the Ramanujan sum of another classical divergent series — the harmonic series — just for the heck of it. In this case, we can directly use the connection to convergent sum:<br />
\[<br />
\begin{align*}<br />
\sum_{k = 1}^\infty{}^{\![R]} \frac{1}{k} &amp; = \lim_{n\to\infty}\left[\sum_{k = 1}^n{}\frac{1}{k} - \int_1^n \frac{dt}{t}\right] = \lim_{n\to\infty}\left[\sum_{k = 1}^n{}\frac{1}{k} - \log(n) \right] = \gamma,<br />
\end{align*}<br />
\]where $\gamma$ is the <a href="http://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant">Euler-Mascheroni constant</a>, a much-neglected cousin of $e$ and $\pi$.</div>
