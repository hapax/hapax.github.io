---
layout: post
mathjax: true
comments: true
title:  "Fun with elementary linear algebra"
date:   2014-01-29
---

In the process of tutoring a linear algebra course, students have asked some "elementary" questions I couldn't answer and which turned out to be quite interesting:<br />
<ul>
<li>If $A$ and $B$ are square matrices and $AB = I$, how much machinery do we need to show that $BA = I$?</li>
<li>If $C$ is a square matrix, then $\det(C) = \det(C^T)$: the transpose preserves determinant. This is geometrically hard to interpret! Thinking of the determinant as the volume of a parallelepiped (the image under $C$ of the unit $n$-cube), what is the "transpose parallelepiped" and why does it have the same volume?</li>
</ul>
<div>
<!--more--><hr />
To answer the first question, the determinant (or equivalently, elementary row operations) give an upper bound on the machinery required. If $AB = I$, then</div>
<div>
<br /></div>
<div style="text-align: center;">
$\displaystyle \det(AB) = \det(A)\det(B) = 1.$</div>
<div>
<br /></div>
<div>
In particular, $\det(A) \neq 0$ so $A^{-1}$ exists. Thus,</div>
<div>
<br /></div>
<div style="text-align: center;">
$\displaystyle B = IB = (A^{-1}A)B = A^{-1}(AB) = A^{-1}I = A^{-1}.$</div>
<div>
<br /></div>
<div>
From the definition of inverse, this implies $BA = I$. The determinant is a bit high-powered, though. Is there a more elementary proof? Somewhat surprisingly, there is! (Kudos to <a href="http://math.stackexchange.com/questions/3852/if-ab-i-then-ba-i">Bill Dubuque</a>, whose answer on the relevant math stackexchange post was the nicest.)</div>
<div>
<br /></div>
<div>
Let $A, B \in M_n(\mathbb{R}) = V$. Since $\dim(V) = n^2$, there is a dependent combination of the $n^2 + 1$ matrices</div>
<div style="text-align: center;">
$\displaystyle I, B, B^2, \ldots, B^{n^2}.$</div>
<div>
<br /></div>
<div>
In other words, there is a polynomial $p \in \mathbb{R}[x]$ of order $\leq n^2$ with $p(B) = 0$. If $p(x) = xq(x)$ for some $q$, then, using $AB = I$, we have</div>
<div>
<br /></div>
<div style="text-align: center;">
$\displaystyle 0 = p(B) = Bq(B) \quad \Longrightarrow \quad 0 = A\cdot 0 = ABq(B) = q(B).$</div>
<div>
<br /></div>
<div>
So $q(B) = 0$. Continuing in this fashion, we can choose $p(x) = \sum_{k=0}^{n^2}a_kx^k$ such that $p(0) = a_0 \neq 0$. Now, $AB = I$ also implies, for any $n &gt; 0$,</div>
<div>
<br /></div>
<div style="text-align: center;">
$\displaystyle &nbsp;(BA - I)B^n = B(AB)B^{n-1} - B^n = B^n - B^n = 0.$</div>
<div>
<br /></div>
<div>
We combine these two as follows:</div>
<div>
<br /></div>
<div style="text-align: center;">
$\displaystyle \begin{align*} (BA - I)p(B) &amp; = (BA - I)\sum_{k=0}^{n^2}a_kB^k \\
&amp; = (BA - I)a_0I + \sum_{k=1}^{n^2}a_k(BA - I)B^k \\
&amp; = a_0(BA - I) = 0. \end{align*}$
</div>
<div>
<br /></div>
<div>
For the last equality, we have used $p(B) = 0$. Since $a_0 \neq 0$, it follows that $BA = I$. $\square$<br />
<br />
Pete Clark's post on the same question shows that the finite-dimensionality of $M_n(\mathbb{R})$ is essential. Let's look at the (infinite-dimensional) vector space of polynomials with real coefficients, $\mathbb{R}[x]$. We have the familiar derivative map $D: \mathbb{R}[x] \to \mathbb{R}[x]$, and the "anti-derivative" map $A: \mathbb{R}[x] \to \mathbb{R}[x]$, where we choose $A(0) = 0$ (no constant term). Both maps are linear, and $D \circ A = I$ since<br />
<br />
<div style="text-align: center;">
$\displaystyle D \circ A \left(\sum_{k=0}^n a_kx^k\right) = D\sum_{k=0}^n \frac{a_k}{k+1}x^{k+1} = \sum_{k=0}^n a_kx^k.$</div>
<br />
However, $A \circ D \neq I$, since $A \circ D$ kills the constant term:</div>
<div>
<br />
<div style="text-align: center;">
$\displaystyle A \circ D \left(\sum_{k=0}^n a_kx^k\right) = &nbsp;\sum_{k=1}^n a_kx^k.$<br />
<br /></div>
<hr />
<br />
I found a great answer to the second question in another <a href="http://math.stackexchange.com/questions/598258/determinant-of-transpose/636198#636198">StackExchange post</a>. To see the geometric significance of the transpose, we need something called the <i><a href="http://en.wikipedia.org/wiki/Singular_value_decomposition">singular value decomposition</a></i>&nbsp;(SVD). I won't prove it, but for a square matrix $C \in M_n(\mathbb{R})$, we can always find orthogonal matrices $U, V \in M_n(\mathbb{R})$ such that<br />
<br />
<div style="text-align: center;">
$\displaystyle C = U\Lambda V$</div>
<br />
for some diagonal matrix $\Lambda = \mbox{diag}(\lambda_1, \ldots, \lambda_n)$. So we can think of the action of $C$ on $\mathbb{R}^n$ as follows:<br />
<ul>
<li>Rotate by $V$.</li>
<li>Scale by factors $\lambda_i$ along the coordinate axes.</li>
<li>Rotate by $U$.</li>
</ul>
<div>
This is how we get the parallelepiped associated with $C$ from the unit $n$-cube. Now, $\det(C)$ is just the product of the scaling factors $\lambda_i$, since the rotations preserve volume:</div>
<br />
<div style="text-align: center;">
$\displaystyle \det(C) = \det(U)\det(\Lambda)\det(V) = 1\cdot\det(\Lambda)\cdot 1 =&nbsp;\lambda_1\cdots\lambda_n.$
</div>
<div>
<br /></div>
<div>
If we take the transpose of $C$, we get</div>
<br />
<div style="text-align: center;">
$\displaystyle C^T = V^T\Lambda^T U^T =&nbsp;V^{-1}\Lambda U^{-1}$</div>
<br />
<div>
since the transpose of a diagonal matrix is itself, and the transpose of an orthogonal matrix is it's inverse. These are still orthogonal matrices! So we can think of $C^T$ as a composition of three maps as above:</div>
<ul>
<li>Rotate by $U^{-1}$.</li>
<li>Scale by factors $\lambda_i$ along the coordinate axes.</li>
<li>Rotate by $V^{-1}$.</li>
</ul>
<div>
The transpose inverts the rotations and swaps the order in which they're performed, but the <i>coordinate scaling factors are the same</i>. Hence, the determinant (aka the volume of the associated parallelepiped) is unchanged. We also see how a parallelepiped is related to it's "transpose": invert and swap the SVD rotations.</div>
</div>
