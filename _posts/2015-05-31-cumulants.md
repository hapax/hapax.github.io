---
layout: post
mathjax: true
comments: true
title: "Cumulants from Möbius inversion"
categories: [Mathematics, Statistics]
date:   2015-05-31
---

**May 31, 2015.** *Cumulants are like the moments of a probability distribution, but
 better. I discuss a nice technique for calculating them in terms of
 Möbius functions on partition lattices, and use it to prove a famous
 result about Gaussian moments attributed to Wick/Isserlis. These are more or
 less just my notes on a
 [paper by Terry Speed](http://onlinelibrary.wiley.com/doi/10.1111/j.1467-842X.1983.tb00391.x/abstract).*

## Introduction

*Prerequisites: basic probability theory, some mathematical maturity.*

For a continuous random variable $X$, the *moment-generating function* $M_X(t)$ is defined by

$$
M_X(t) = \mathbb{E}(e^{tX}) = \sum_{k=0}^\infty \mathbb{E}(X^k)\frac{t^k}{k!} = \sum_{k=0}^\infty m_k\frac{t^k}{k!}.
$$

The Taylor coefficient $m_k$ is called the $k$th *moment* of the distribution. Integral combinations of moments give us the mean, variance, skew, kurtosis, etc, of the distribution. A closely related object is the *cumulant-generating function* $g_X(t)$, given by

$$
g_X(t) = \log M_X(t) = \sum_{k=0}^\infty \kappa_k\frac{t^k}{k!}.
$$

The Taylor coefficient $\kappa_k$ is called the $k$th *cumulant* of
$X$. Cumulants are used in statistics, but as we will see, also have
interesting applications to diagrammatic methods in physics. This
first post is going to explain a nice formalism for calculating joint
cumulants using set partitions due to Terry Speed (1983), and follows
Speed's paper closely (though I include some details Speed omits). In
a sequel, I hope to explain how cumulants are used in statistical
physics and quantum field theory.

## Cumulants

*Joint cumulants* are cumulants for jointly distributed random variables. Say we have $m$ random variables $X_1, \ldots, X_m$. Use the vector notation $\mathbf{r} = (r_1, \ldots, r_m) \in \mathbb{Z}^m$, with $\mathbf{r} \geq 0$ meaning each $r_i \geq 0$, and

$$
\begin{align*}
\mathbf{X}^\mathbf{r} & = X_1^{r_1}\cdots X_m^{r_m}, \quad \mathbf{\theta}^\mathbf{r} = \theta_1^{r_1}\cdots \theta_m^{r_m},  \\
\mathbf{r}! & = r_1!\cdots r_m!, \quad r = |\mathbf{r}|_1 = r_1 + \cdots+ r_m.
\end{align*}
$$

By analogy with the single-variable case, we can define the joint cumulants via

$$
\sum_{\mathbf{r} \geq 0} \kappa_\mathbf{r}\frac{\mathbf{\theta}^\mathbf{r}}{\mathbf{r}!} = \log \sum_{\mathbf{r} \geq 0} \mathbb{E}(X^\mathbf{r})\frac{\mathbf{\theta}^\mathbf{r}}{\mathbf{r}!}.
$$

Quite simply, joint cumulants are the coefficients of the *multivariable* Taylor expansion of log of the multivariable moment generating function. It's convenient to have a way of writing the cumulant $\kappa_\mathbf{r}$ with the random variables it depends on made explicit:

$$
\kappa_\mathbf{r} = \mathcal{C}(\overset{r_1 \text{ times}}{\overbrace{X_1, \ldots, X_1}}, \ldots, \overset{r_m \text{ times}}{\overbrace{X_m, \ldots, X_m}}) = \mathcal{C}(X'_1, \ldots, X'_{r}).
$$

Here, the $X_i$ are the specific jointly distributed random variables we started with, while the $X'_i$ are possibly repeated RV inputs to $\mathcal{C}$. Setting the $X'_i$ as above, it turns out that we can define

$$
\begin{align*}
\kappa_\mathbf{r} &=  \mathcal{C}(X'_1, \ldots, X'_{r}) \\
&= \sum_{\sigma\in P_r}(-1)^{b(\sigma) - 1}(b(\sigma)-1)!\prod_{a=1}^{b(\sigma)} \mathbb{E}\left(\prod_{i\in\sigma_a} X'_i\right),
\end{align*}
$$

where $P_{r}$ is the set of *partitions* of the set $[r] := \{1, \ldots, r\}$, and $\sigma \in P_r$ splits into $b := b(\sigma)$ disjoint *blocks* $\sigma_1, \ldots, \sigma_b$ satisfying

$$
\bigcup_i \sigma_i = \{1, \ldots, r\}, \quad \sigma_i \cap \sigma_j = \varnothing \text{ for } i\neq j.
$$

It's not at all obvious that this definition of joint cumulant is useful, or even equivalent, but we'll show that both are true below.

Before we go on, we do a calculation to illustrate the utility of the second definition. For three jointly distributed random variables, $\kappa_{111} = \mathcal{C}(X_1, X_2, X_3)$ can be calculated in terms of expectations using the alternative definition. We can simplify our partitions by concatenating numbers in the same block and separating blocks with bars:

$$
P_3 = \{123, 1|23, 2|13, 3|12, 1|2|3\}.
$$

The corresponding blocks numbers are $\{1, 2, 2, 2, 3\}$. We sum over the partitions with the prefactor $(-1)^{b(\sigma)-1}(b(\sigma)-1)!$ and take the product of expectations over products within blocks:

$$
\begin{align*}
\mathcal{C}(X_1, X_2, X_3) & = \mathbb{E}(X_1X_2X_3) - \mathbb{E}(X_1)\mathbb{E}(X_2X_3) \\ & \qquad - \mathbb{E}(X_2)\mathbb{E}(X_1X_3) - \mathbb{E}(X_3)\mathbb{E}(X_1X_2) + 2\mathbb{E}(X_1)\mathbb{E}(X_2)\mathbb{E}(X_3).
\end{align*}
$$

We can set $X_1 = X_2 = X_3 = X$ to obtain a result for the *single-variable* cumulant $\kappa_3$:

$$
\kappa_3 = \mathbb{E}(X^3) - 3\mathbb{E}(X)\mathbb{E}(X^2) + 2\mathbb{E}(X)^3 = m_3 - 3m_1m_2 + 2m_1^3.
$$

## Partition lattices

Let's be more explicit about partitions. A *partition* $\sigma$ of a set $S$ is a collection of disjoint subsets of $S$ whose union is $S$, i.e.

$$
\sigma = \{\sigma_i\}_{i\in I}, \quad \bigcup_{i\in I} \sigma_i = S, \quad \sigma_i \cap \sigma_j = \varnothing \text{ for } i\neq j.
$$

We call the $\sigma_i$ the *blocks* of $\sigma$. We label the collection of all such partitions $P(S)$. If $\sigma, \tau \in P(S)$, and each $\sigma_i \subseteq \tau_j$ for some $j$ (so each block of $\sigma$ is in a block of $\tau$) we say that $\sigma$ is *finer* than $\tau$, or $\tau$ is *coarser* than $\sigma$, and write $\sigma \leq \tau$. This relation turns $P(S)$ into a special algebraic object called a lattice.

A *lattice* $(\mathcal{L}, \leq)$ is a partially ordered set where any
two elements have a greatest lower bound and a least upper bound, also
called the *meet* and *join* respectively. We recall that a partial order $\leq$ is *reflexive*, *transitive* and *antisymmetric:*

$$
\begin{align*}
(\textrm{R}) \,\,&x \leq x, \\
(\textrm{T}) \,\,&x \leq y, \quad y\leq z  \quad\Longrightarrow\quad x \leq z, \\
(\textrm{A}) \,\,&x \leq y, \quad y\leq x  \quad\Longrightarrow\quad x = y.
\end{align*}
$$

The *meet* $x \wedge y$ and *join* $x \vee y$ of $x, y \in \mathcal{L}$ are defined (if they exist) as

$$
\begin{align*}
x \vee y & := \max \{z : z \leq x, z \leq y\} \\
x \wedge y & := \min \{z : x \leq z, y \leq z\}.
\end{align*}
$$

In a lattice, the meet and join exist for arbitrary elements. A familiar example of a lattice is the two-element boolean algebra $\{0, 1\}$ with the usual partial order $0 \leq 1$, and meet and join are the logical operations "and" and "or" (hence the notation). Another example is the power set $2^A$ of any set $A$ ordered by the subset relation, where meet and join are intersection and union.

So, I claim that using the "finer than" relation $\leq$ on $P(S)$ turns it into a lattice. First of all, it's clear that $\leq$ is a partial order since it obviously satisfies (R), (T) and (A). The meet of $\sigma$ and $\tau$ is the coarsest partition of $S$ finer than both, which is easily seen to be the non-empty intersections of the blocks of $\tau$ and $\sigma$. For instance, in $P_3$,

$$
1|23 \wedge 12|3 = 1|2|3.
$$

Thought of a different way, it is the "union" of the bars. Similarly, the join is the "intersection" of bars, so

$$
1|23 \vee 12|3 = 123.
$$

We can picture any finite partial order with a graph called a *Hasse diagram*. These are graphs with no horizontal edges, and an edge $xy$ ($x$ higher) indicates that $y < x$ and there are no $z$ such that $y < z < x$. Each Hasse diagram gives a partial order on the vertices, but not necessarily a lattice. For instance, in a disconnected diagram, vertices in different components cannot have a meet or join.

**Exercise 1.** (a) Draw the partition lattice for $P_4$. [Solution](http://upload.wikimedia.org/wikipedia/commons/thumb/5/53/PartitionLattice.svg/480px-PartitionLattice.svg.png). (b) Find a partial order with a *connected* Hasse diagram which is not a lattice. (c) Find the *smallest* answer to (b), and prove that this is so.

## Zeta and Möbius functions

Given a finite partially ordered set $(A, \leq)$, there are two associated functions that will prove useful. The first is the enigmatically named *zeta* *function* $\zeta_A: A\times A \to A$, defined by

$$
\zeta_A(x, y) = \begin{cases}
1 & x \leq y \\
0 & \text{else.}
\end{cases}
$$

The second is the *Möbius function* $\mu_A$, which can be defined as

$$
\mu_A(x, y) = \begin{cases}
1 & x = y \\
-\sum_{x\leq z < y} \mu_A(x, z) & x &< y \\
0 & \text{else.}
\end{cases}
$$

We can think of the Möbius function as returning $1$ for equal arguments, $0$ for arguments which are not comparable according to $\leq$, and otherwise walking down the path in the Hasse diagram from $y$ to $x$, adding $-\mu_A(x, z)$ for each vertex $z$ it visits along the way (including $x$ but not $y$). In fact, thinking of $\mu_A$ and $\zeta_A$ as matrices

$$
\mu_{xy} = \mu_A(x, y), \quad \zeta_{xy} = \zeta_A(x, y),
$$

we have $\mu\zeta = \zeta\mu = I$. Let's check. First of all,

$$
\begin{align*}
(\mu\zeta)_{xz} & = \sum_y \mu_A(x, y)\zeta_A(y, z) = \sum_{y\leq z} \mu_A(x, y) = \sum_{x\leq y< z}\mu_A(x, y) + \mu_A(x, z).
\end{align*}
$$

If $x = z$, then the summation vanishes (no $y$ terms) and we are left with $\mu_A(x, z) = 1$. If $x &gt; z$ or they are not comparable, then both terms vanish. Finally, if $x < z$, then

$$
(\mu\zeta)_{xz} = \sum_{x\leq y< z}\mu_A(x, y) + \mu_A(x, z) = -\mu_A(x, z) + \mu_A(x, z) = 0.
$$

It follows that $\mu\zeta = I$.
By linear algebra, $\zeta\mu = I$. Now suppose we have a function $f: A \to \mathbb{R}$, and define the "partial sum" by

$$
F(x) = \sum_{y\leq x}f(y) = \sum_{y}f(y)\zeta_A(y, x) = \sum_{y}f_y\zeta_{y, x},
$$

thinking of $f_x = f(x)$ as a row matrix. Thinking of $F_x = F(x)$ the same way, we have $F = f\zeta$. Hence,

$$
f = f I = f \zeta\mu = F\mu.
$$

This is *Möbius inversion*: using the Möbius function to go back and forth between a function on the lattice and its partial sum. It turns out that $\mu_A$ is often easy to calculate. In the case of lattice partitions, it turns out that

$$
\mu_{P(S)}(\sigma, \hat{S}) = (-1)^{b(\sigma)-1}(b(\sigma)-1)!
$$

where $\hat{S} = \{S\}$, the partition of $S$ into a single block.

**Exercise 2.** (a) Show that for a finite poset and any $x, y$,

$$
0 = \sum \{\mu(w,z) : x \leq w \leq z \leq y \}.
$$

Conclude that

$$
\mu_{A}(x, y) = -\sum_{x < z \leq b} \mu_A(z, b).
$$

(b) Using part (a) and induction on $b(\sigma)$, prove that $\mu_{P(S)}(\sigma,\hat{S}) = (-1)^{b(\sigma)-1}(b(\sigma)-1)!$ for any finite set $S$.


## Cumulants via Möbius inversion

We now return to our lattice of interest, the partition lattice $P_r$.
We would like to use Möbius inversion to show that the definition of cumulants based on partitions, $\mathcal{C}$, is equivalent to the standard definition in terms of the power series, $\kappa$.
Consider a partition $\sigma \in P_r$, written in terms of its $b$ blocks $\sigma = \sigma_1 | \cdots | \sigma_b$. Write

$$
\bar{\kappa}_\sigma = \prod_{a=1}^b \kappa_{\mathbf{r}(\sigma_a)},
$$

where $\mathbf{r}(\sigma_a) = (r_i(\sigma_a))$ is an $r$-vector defined by $r_i(\sigma_a) = 1$
if $i \in \sigma_a$ and $0$ otherwise. If $\sigma = 12|3|4$ for instance, then

$$
\bar{\kappa}_\sigma = \kappa_{1100}\kappa_{0010}\kappa_{0001}.
$$

If we exponentiate the multivariable Taylor expansion defining $\kappa$, we get

$$
\begin{align*}
\sum_{\mathbf{r} \geq 0} \mathbb{E}(X^\mathbf{r})\frac{\mathbf{\theta}^\mathbf{r}}{\mathbf{r}!} & = \exp\left[ \sum_{\mathbf{r} \geq 0} \kappa_\mathbf{r}\frac{\mathbf{\theta}^\mathbf{r}}{\mathbf{r}!}\right]\\&=\sum_{n\geq 0}\frac{1}{n!}\left[ \sum_{\mathbf{r} \geq 0} \kappa_\mathbf{r}\frac{\mathbf{\theta}^\mathbf{r}}{\mathbf{r}!}\right]^n\\
& = \sum_{n\geq 0}\frac{1}{n!}\sum_{\mathbf{r}_1,\ldots, \mathbf{r}_n \geq 0} \kappa_{\mathbf{r}_1}\cdots \kappa_{\mathbf{r}_n}\frac{\mathbf{\theta}^{\mathbf{r}_1 + \cdots +\mathbf{r}_n}}{\mathbf{r}_1!\cdots \mathbf{r}_n!}.
\end{align*}
$$

Equating coefficients of $\mathbf{\theta}^\mathbf{r}$, we see that

$$
\mathbb{E}(X^\mathbf{r}) = \sum_{n\geq 0}\sum_{\mathbf{r}_1+\cdots+\mathbf{r}_n = \mathbf{r}} \frac{1}{n!}\prod_{k=1}^n \frac{\kappa_{\mathbf{r}_k}}{\mathbf{r}_k!}.
$$

The summation is effectively over integer partitions of $\mathbf{r}$, with $n$ the number of blocks. These are genuine integer partitions, not just partitions of the index set. However, matters are simplified if we specialise to the case where $r_i \leq 1$, i.e., at most linear powers of a random variable appear in the expectation $\mathbb{E}(X^\mathbf{r})$. Then $\mathbf{r}_k! = 1$ and the sum

$$
\mathbf{r}_1 + \cdots +\mathbf{r}_n = \mathbf{r}
$$

can be thought of as a partition of the occurrences of $1$ in $\mathbf{r}$ into $n$ blocks, i.e. an element $\sigma \in P_r$ with $b(\sigma) = n$. Reordering gives a factor of $n!$, but this is nicely cancelled by the $1/n!$ in the summation over the number of blocks, so we end up with

$$
\begin{align*}
\mathbb{E}(X^\mathbf{r}) & = \sum_{n\geq 0}\sum_{\mathbf{r}_1+\cdots+\mathbf{r}_n = \mathbf{r}} \frac{1}{n!}\prod_{k=1}^n \kappa_{\mathbf{r}_k} = \sum_{\sigma \in P_r}\prod_{k=1}^n \kappa_{\mathbf{r}(\sigma_k)} = \sum_{\sigma \in P_r}\bar{\kappa}_{\sigma}.
\end{align*}
$$

Now consider an arbitrary partition of the original $m$ random variables into $b$ blocks, $\tau \in P_m$ with $b(\tau) = b$. Applying the foregoing result, we get

$$
\begin{align*}
\prod_{a=1}^b \mathbb{E}\left(\prod_{k\in\tau_a} X_k\right) & = \prod_{a=1}^b \sum_{\sigma_a\in P(\tau_a)} \bar{\kappa}_{\sigma_a}.
\end{align*}
$$

Note that we sum over *partitions of the blocks of* $\tau$, with $\sigma_a \in P(\tau_a)$ standing for some partition of the set of elements in $\tau_a$. We can assemble the smaller blocks $\sigma_a$ into a partition $\sigma$ of $m$ which is finer than $\tau$, so $\sigma \leq \tau$. It is not hard to see that *every* finer partition than $\tau$ arises in this way. In other words,

$$
\prod_{a=1}^b \mathbb{E}\left(\prod_{k\in\tau_a} X_k\right) = \sum_{\sigma\leq \tau}\bar{\kappa}_{\sigma}.
$$

Here's an example:

$$
\mathbb{E}(X_1X_2)\mathbb{E}(X_3X_4) = (\bar{\kappa}_{12} + \bar{\kappa}_{1|2})(\bar{\kappa}_{34} + \bar{\kappa}_{3|4}) = \bar{\kappa}_{12|34} + \bar{\kappa}_{12|3|4} + \bar{\kappa}_{1|2|34} + \bar{\kappa}_{1|2|34}.
$$

Now we simply use Möbius inversion on our formula to get an expression for $\bar{\kappa}$:

$$
\begin{align*}
\bar{\kappa}_{\tau} = \sum_{\sigma \in P_m} \mu_{P_m}(\sigma, \tau)\prod_{a=1}^b \mathbb{E}\left(\prod_{k\in\tau_a} X_k\right).
\end{align*}
$$

Finally, using the formula for $\mu_{P(S)}(\sigma, \hat{S})$ above, we have

$$
\begin{align*}
\bar{\kappa}_{\hat{S}} = \kappa_{1\cdots 1} = \sum_{\sigma \in P_m} (-1)^{b(\sigma)-1}(b(\sigma)-1)!\prod_{a=1}^b \mathbb{E}\left(\prod_{k\in\tau_a} X_k\right)
\end{align*}
$$

as claimed. The general result follows by thinking of any repeated random variables as *new* (but identically distributed) random variables. For simplicity, we will continue assuming that random variables are distinct.

## Isserlis' theorem

We can apply these results to quickly prove *Isserlis' theorem*. Suppose we have a zero mean, multivariate normal $\mathbf{X} = (X_1, \ldots, X_{m}) \sim \mathcal{N}_m(0, \mathbf{\Sigma})$, where $\mathbf{\Sigma}$ is the *covariance matrix*

$$
\mathbf{\Sigma} = [\mathrm{Cov}(X_i, X_j)] = [\mathbb{E}(X_iX_j)].
$$

It turns out (see a proof [here](http://turing.une.edu.au/~stat354/notes/node33.html)) that the moment generating function is

$$
\begin{align*}
M_{\mathbf{X}}(\mathbf{t}) & = \mathbb{E}(e^{\mathbf{t}^{\mathrm{T}}\mathbf{X}}) = \exp\left(\frac{1}{2}\mathbf{t}^{\mathrm{T}}\mathbf{\Sigma}\mathbf{t}\right).
\end{align*}
$$

So the cumulant generating function is

$$
\log M_{\mathbf{X}}(\mathbf{t}) = \frac{1}{2}\mathbf{t}^{\mathrm{T}}\mathbf{\Sigma}\mathbf{t} = \frac{1}{2}\sum_{i,j}\mathbb{E}(X_iX_j)t_i t_j.
$$

Comparing to the vector notation, it's not hard to see that

$$
\mathbb{E}(X_iX_j) = \kappa_{\mathbf{r}}
$$

where $r_i = r_j = 1$, $r_k = 0$ for $k \notin \{i, j\}$. Thus, only cumulants of order $2$ are non-vanishing. Using our result for expectations in terms of $\bar{\kappa}$,

$$
\begin{align*}
\mathbb{E}(X_1\cdots X_m) & = \sum_{\sigma \in P_m} \bar{\kappa}_\sigma = \sum_{\sigma \in W} \bar{\kappa}_\sigma
\end{align*}
$$

where $W$ is the subset of $P_m$ where each block is a pair, since the product of cumulants associated with any other permutation vanishes. Thus, if $m$ is odd,

$$
\mathbb{E}\left(\prod_{i=1}^m X_i\right) = 0.
$$

On the other hand, if $m = 2n$, then

$$
\mathbb{E}\left(\prod_{i=1}^m X_i\right) = \sum_{\sigma \in W}\prod_{a=1}^n \mathbb{E}(X_{i_a}X_{j_a}), \quad \sigma_a = \{i_a, j_a\}.
$$

Leon Isserlis proved these last two results in 1916, using induction. They were proved in a slightly different form by the physicist Gian-Carlo Wick in 1950, so in quantum field theory the same result is called *Wick's theorem*. I hope to discuss the theorem of Isserlis/Wick in greater depth in a subsequent post.

## A theorem of Leonov and Shiryaev

We now apply our lattice theoretic expression to prove a result due to Leonov and Shiryaev (1959). Consider an array $[X_{ij}]$ of real random variables, $ i \in [m], j \in [n_i]$, so the length of a row may vary. Any partition $\pi \in P_m$ of the row indices partitions the full set $S = \{(i, j): i\in[m], j\in[n_i]\}$, partitioning the corresponding rows. Denote the induced partition of $S$ by $\tilde{\pi}$. A partition $\sigma \in P(S)$ is *decomposable relative to* $\pi \in P_m$ if $\sigma \leq \tilde{\pi}$, and *indecomposable* if $\sigma$ is not decomposable with respect to any row partition other than $\hat{[m]}$. In other words, an indecomposable partition has a block with an element from each row.

The general result is

$$
\mathcal{C}\left(\prod_{j_1\in[n_1]}X_{ij_1}, \ldots, \prod_{j_m\in[n_m]}X_{ij_m}\right) = \sum_{\sigma}^* \prod_{a=1}^{b(\sigma)}\mathcal{C}(X_{ij}: (i, j) \in \sigma_a).
$$

The asterisk over the sum on the right indicates the restriction to *indecomposable* partitions of $S$. Let's prove this. Let $\pi \in P_m$. By our earlier result for cumulants,

$$
\prod_{a=1}^{b(\pi)}\mathbb{E}\left(\prod_{i\in\pi_a}\prod_{j_i\in [n_i]} X_{ij_i}\right) = \sum_{\sigma \leq \tilde{\pi}} \prod_{a=1}^{b(\sigma)}\mathcal{C}(X_{ij}: (i,j) \in \sigma_a),
$$

where we made the replacements

$$
\begin{align*}
\mathbb{E}\left(\prod_{k\in\tau_a} X_k\right) \quad & \longrightarrow \quad \mathbb{E}\left(\prod_{i\in\pi_a}\prod_{j_i\in [n_i]} X_{ij_i}\right),\\
\sum_{\sigma\leq \tau}\bar{\kappa}_{\sigma} \quad & \longrightarrow \quad \sum_{\sigma \leq \tilde{\pi}} \prod_{a=1}^{b(\sigma)}\mathcal{C}(X_{ij}: (i,j) \in \sigma_a).
\end{align*}
$$

The first replacement is just an explicit product over the partition $\tilde{\pi}$, and the second uses the definition of $\bar{\kappa}$, summing over the partitions $\sigma \in P(S)$ decomposable relative to $\pi$. Define $F(\pi)$ and $f(\rho)$ via

$$
\begin{align*}
F(\pi) & = \sum_{\sigma \leq \tilde{\pi}} \prod_{a=1}^{b(\sigma)}\mathcal{C}(X_{ij}: (i,j) \in \sigma_a) \\
& = \sum_{\rho}\zeta_{P_m}(\rho, \pi)\sum_{\sigma \prec \rho} \prod_{a=1}^{b(\sigma)}\mathcal{C}(X_{ij}: (i,j) \in \sigma_a)\\
& = \sum_{\rho}\zeta_{P_m}(\rho, \pi)f(\rho),
\end{align*}
$$

where $\sigma \prec \rho$ indicates that $\sigma$ is decomposable with respect to $\rho$ but no finer row partition. Using Möbius inversion over $P_m$, we find

$$
f(\pi) = \sum_\rho \mu_{P_m}(\rho, \pi)F(\rho).
$$

Set $\pi = \hat{[m]}$. Using this expression, our formula from Exercise 2, and the definition of $\mathcal{C}$, we obtain

$$
\begin{align*}
\mathcal{C}\left(\prod_{j_1\in[n]_1}X_{ij_1}, \ldots, \prod_{j_m\in[n]_m}X_{ij_m}\right) & = \sum_{\rho}(-1)^{b(\rho) - 1}(b(\rho)-1)!\prod_{a=1}^{b(\rho)} \mathbb{E}\left(\prod_{i\in\rho_a}\prod_{j_i\in [n_i]} X_{ij_i}\right)\\
&= \sum_{\rho}\mu_{P_m}(\rho, \hat{[m]})F(\rho)\\
& = f(\hat{[m]}) \\
& = \sum_{\sigma \prec \hat{[m]}} \prod_{a=1}^{b(\sigma)}\mathcal{C}(X_{ij}: (i,j) \in \sigma_a).
\end{align*}
$$

Since $\sigma \prec \hat{[m]}$ means that $\sigma$ is decomposable with respect to $\hat{[m]}$ but no finer row partition, by definition it is indecomposable. This completes the proof.

### References

- [*Cumulants and partition lattices*](http://onlinelibrary.wiley.com/doi/10.1111/j.1467-842X.1983.tb00391.x/abstract) (1983), Terry Speed.
