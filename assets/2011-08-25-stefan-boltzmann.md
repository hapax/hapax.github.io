---
layout: post
mathjax: true
comments: true
title:  "A cute integral and the Stefan-Boltzmann law"
date:   2011-08-25
---

**August 25, 2011.** *A quick post on the beautiful integral appearing
  in the Stefan-Boltzmann law (how much power is given off by a hot
  object) and its relation to special functions.*

Consider the integral<br />
<br />
<div style="text-align: center;">
$\displaystyle \int_0^\infty \frac{x^k}{e^x - 1} dx$</div>
<br />
for $k \in \mathbb{N}$. Though it looks a bit hairy, it actually boils down to a beautiful closed-form expression involving special functions. Not only is it beautiful, but physically relevant: we can use it to derive the Stefan-Boltzmann law for a black body,<br />
<br />
<div style="text-align: center;">
$\displaystyle j^* = \sigma T^4,$</div>
<br />
where $j^*$ is the total radiant power per unit area, $T$ the temperature in Kelvin of the black body, and $\sigma$ a number called <i>Stefan's constant</i> whose value (in terms of fundamental constants) we will determine below.<br />
<!--more--><br />
First, observe that&nbsp;$x &gt; 0$ and therefore $|e^{-x}| &lt; 1$. So we can&nbsp;expand $1/(e^x - 1)$ as the geometric series<br />
<br />
<div style="text-align: center;">
$\displaystyle \frac{1}{e^x - 1} =&nbsp;\displaystyle \frac{e^{-x}}{1 -&nbsp;e^{-x}}&nbsp;= \sum_{n=1}^\infty e^{-nx}.$<br />
<br /></div>
We substitute the series and exchange the sum and integral, since the convergence is uniform:<br />
<br />
<div style="text-align: center;">
$\displaystyle \int_0^\infty \frac{x^k}{e^x - 1} dx = \displaystyle \int_0^\infty \sum_{n=1}^\infty&nbsp;x^ke^{-nx} \, dx =&nbsp;\sum_{n=1}^\infty&nbsp;\int_0^\infty x^ke^{-nx} \, dx.$</div>
<br />
Let $f_n(k)$ denote the integral<br />
<br />
<div style="text-align: center;">
$\displaystyle&nbsp;\int_0^\infty x^ke^{-nx} \, dx.$</div>
<br />
Then $f_n(0) = 1/n$, and for $k &gt; 0$, integration by parts yields the recursion relation<br />
<br />
<div style="text-align: center;">
$\displaystyle \begin{align*}&nbsp;f_n(k) &amp; = \int_0^\infty x^ke^{-nx} \, dx \\ &amp; = \left[-\frac{1}{n}x^ke^{-nx}\right]_0^\infty + \frac{k}{n}\int_0^\infty x^{k-1}e^{-nx} \, dx \\ &amp;&nbsp;= \frac{k}{n}f_n(k-1). \end{align*}$</div>
<br />
By induction, $f_n(k) = k!n^{-(k+1)}$. Hence,<br />
<br />
<div style="text-align: center;">
$\displaystyle \int_0^\infty \frac{x^k}{e^x - 1} dx =&nbsp;\sum_{n=1}^\infty&nbsp;f_n(k) =&nbsp;\sum_{n=1}^\infty&nbsp;\frac{k!}{n^{k+1}}.$</div>
<br />
In fact, we can generalise further. For convenience, we consider the exponent $k-1$ for complex $k$ with $\Re(k)&gt;1$. Note that $\zeta(k)$ and $\Gamma(k)$ have the standard integral representation, where&nbsp;$\zeta$ is the <a href="http://en.wikipedia.org/wiki/Riemann_zeta_function">Riemann zeta function</a>&nbsp;and $\Gamma$ is the <a href="http://en.wikipedia.org/wiki/Gamma_function">Gamma function</a>. We have<br />
<br />
<div style="text-align: center;">
$\displaystyle \int_0^\infty \frac{x^{k-1}}{e^x - 1} dx =&nbsp;\sum_{n=1}^\infty&nbsp;\int_0^\infty x^{k-1}e^{-nx} \, dx$</div>
<br />
as before. Making the change of variable $u=nx$, we obtain<br />
<br />
<div style="text-align: center;">
$\displaystyle \begin{align*}&nbsp;\sum_{n=1}^\infty&nbsp;\int_0^\infty x^{k-1}e^{-nx} \, dx&nbsp;&amp; =&nbsp;\sum_{n=1}^\infty \frac{1}{n^k}\int_0^\infty u^{k-1}e^{-u} \, du \\ &amp; =&nbsp;\sum_{n=1}^\infty \frac{1}{n^k}\Gamma(k) \\ &amp; =&nbsp;\Gamma(k)\sum_{n=1}^\infty \frac{1}{n^k} \\ &amp; = \Gamma(k)\zeta(k). \end{align*}$</div>
<br />
Since $\Gamma(k+1)=k!$ for $k\in \mathbb{N}$, this is consistent with our earlier result.<br />
<br />
Now, suppose we have a <i>black body</i> at temperature $T$. Such a body absorbs <i>all</i> incident radiation. The intensity distribution of radiated energy (as a function of frequency and temperature) was correctly given by Planck as<br />
<br />
<div style="text-align: center;">
$\displaystyle I(\nu, T) = \frac{2h\nu^3}{c^2}\frac{1}{e^{h\nu/kT} - 1}$</div>
<br />
where $k$ is the Boltzmann constant, $h$ is Planck's constant, and $c$ is the speed of light. (This can also be derived using <a href="http://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_statistics">Bose-Einstein statistics</a>.) Now, the total radiated energy is<br />
<br />
<div style="text-align: center;">
$\displaystyle \begin{align*} j^* &amp; = \pi\int_0^\infty I(\nu, T) \, d\nu \\ &amp; = &nbsp;\int_0^\infty&nbsp;\frac{2\pi h\nu^3}{c^2}\frac{1}{e^{h\nu/kT} - 1}&nbsp;\, d\nu \\ &amp; = \frac{2\pi h}{c^2}&nbsp;\int_0^\infty \frac{\nu^3}{e^{h\nu/kT} - 1}&nbsp;\, d\nu \\ &amp; = \frac{2\pi h}{c^2} \cdot\frac{k^4T^4}{h^4}\int_0^\infty \frac{s^3}{e^{s} - 1}&nbsp;\, d\nu \\ &amp; =\frac{2\pi k^4T^4}{c^2h^3}\Gamma(4)\zeta(4)\end{align*}$</div>
<br />
where we have made the substitution $s = h\nu/kT$ and used the result above. (The factor of $\pi$ is due to an integral over the angle of radiation which we have omitted.) We note that $\Gamma(4) = 3! = 6$, while $\zeta(4) = \pi^4/90$. Hence,<br />
<br />
<div style="text-align: center;">
$\displaystyle j^* = \frac{2\pi k^4T^4}{c^2h^3}\cdot6\cdot\frac{\pi^4}{90} = \frac{2\pi^5k^4}{15c^2h^3}T^4 = \sigma T^4$<br />
<div style="text-align: left;">
<br /></div>
<div style="text-align: left;">
as claimed.
