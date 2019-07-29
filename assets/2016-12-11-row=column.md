---
layout: post
mathjax: true
comments: true
title:  "Row rank = column rank"
categories: [Mathematics, Teaching]
date:   2016-12-11
---

**December 11, 2016.** *A quick basis-free proof that row rank = column rank. Extension material for
  a [second course on linear algebra](https://handbook.unimelb.edu.au/subjects/mast20022).*

### Introduction

*Prerequisites: basic linear algebra, inner product spaces.*

The usual proof that row rank equals column rank involves Gaussian
elimination, a basis-dependent algorithm. Here, I'll present an
amusingly overpowered
basis-free proof. (It's somewhat trivial, but I haven't seen in
anywhere.) The proof may not require a basis, but it does require an
inner product; for a finite-dimensional vector space, we can always
<i>choose</i> an inner product, but this is a little like choosing a
basis. We start with a few exercises to connect inner products to
elementary linear algebra, but readers should feel free to skip to the
main result if they are familiar with inner product spaces. In fact, the proof is a single diagram, explained below. 
 
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="https://1.bp.blogspot.com/-Myv5SXrt8FM/WEzakAUMxvI/AAAAAAAAChU/27YydKMzJwc5haR-gD6_bEc8FW5go3YhQCLcB/s1600/rank-square.png" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="160" src="https://1.bp.blogspot.com/-Myv5SXrt8FM/WEzakAUMxvI/AAAAAAAAChU/27YydKMzJwc5haR-gD6_bEc8FW5go3YhQCLcB/s200/rank-square.png" width="200" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;"><i>A diagrammatic proof: use the inner product structure and consider duals.</i></td></tr>
</tbody></table>

### Preliminary results on inner products

Let $V$ be an $m$-dimensional inner product space, with inner product $\langle\cdot,\cdot\rangle$. Similarly, let $W$ be an $n$-dimensional inner product space. If $T: V \to W$ a linear operator, the <i>rank</i> of $T$ is just the dimension of the image: 

$$ 
\mbox{rank} \, T := \mbox{dim}\, \mbox{im} \, T. 
$$
 
The set of all such linear maps is denoted $\mathcal{L}(V, W)$. For a finite set of vectors $S$, the <i>linear span of</i> $S$ is the set of linear combinations 

$$ 
\langle S \rangle := \left\{ \sum_{v\in S} \lambda_v v \, \bigg|\, \lambda_v \in \mathbb{R} \right\}. 
$$
 
The next result we need is to do with inner products and <i>dual
spaces</i>. The dual space of $V$ is the collection of all linear maps
from $V$ to $\mathbb{R}$, so we define $V^* := \mathcal{L}(V, \mathbb{R})$. If $V$ is a finite-dimensional inner product space, there is in fact a simple isomorphism $\iota_V: V \to V^*$, given by 

$$ 
\iota_V(v) = \langle v, \cdot \rangle. 
$$
 
(This is a very simple version of the <a href="https://en.wikipedia.org/wiki/Riesz_representation_theorem">Riesz representation theorem</a>.) It's important to note that the result $V \simeq V^*$ no longer holds when $V$ is infinite-dimensional. 
 
<b>Exercise 1.</b> (a) Show that $\iota_V$ is linear and injective. 
(b) Consider a linear map $\phi \in V^*$. By choosing a basis for $V$, construct a $v_\phi \in V$ such that $\iota_V (v_\phi) = \phi$. $\square$ 
 
Next, we need to define the <i>transpose</i>. In elementary linear algebra, the transpose of a matrix $A = [a_{ij}]$ just swaps row and column indices, $A^t := [a_{ji}]$. We will give a different definition, more useful for our purposes. For an arbitrary linear map $T : V \to W$, we define the transpose $T^t: W \to V$ by 

$$ 
\langle w, Tv\rangle := \langle T^t w, v\rangle. 
$$
 
The reader is invited to check that $T^t$ exists and is equivalent to the usual definition. 
 
<b>Exercise 2.</b> (a) Show that the transpose map always exists. <i>Hint:</i> Define $T^t$ using bases for $V$ and $W$ and the relation above. 
(b) Prove that, for fixed bases of $V$ and $W$, if $A$ is the matrix representing the linear map $T$, then $A^t$ represents $T^t$. Hence, the two definitions are equivalent. 
(c) Show that we can also naturally define $T^t: V^* \to W^*$ by 

$$ 
(T^t \phi) w := \phi(T^t w). 
$$
 
We will use this result in the proof below. $\square$ 
 
Our last set of results connects the row and column rank of a matrix to rank of the linear map it represents. 
 
<b>Exercise 3.</b> Suppose that, with respect to particular bases for $V$ and $W$, the linear map $T$ is represented by a matrix 

$$ 
A := [\mathbf{c}_1 \cdots \mathbf{c}_m] := [\mathbf{r}_1 \cdots \mathbf{r}_n]^t, 
$$
 
where the $\mathbf{c}_i \in \mathbb{R}^n$ and $\mathbf{r}_i \in
\mathbb{R}^m$.

(a) Demonstrate that

$$\mbox{rank} \, T = \text{dim } \langle \mathbf{r}_1, \ldots,
\mathbf{r}_n \rangle := \mbox{row rank}\, A.
$$

In other words, the span
of rows of $A$ has the same dimension as the image of $T$.

(b) Show that $\mbox{rank} \, T^t = \text{dim } \langle \mathbf{c}_1, \ldots, \mathbf{c}_m \rangle := \mbox{column rank}\, A$. In other words, the span of columns of $A$ has the same dimension as the image of $T^t$. $\square$ 

### Proof that row rank equals column rank

Now we know enough about inner product spaces to prove our result very quickly. 
 
<b>Claim. </b>For any linear map $T: V \to W$, 

$$ 
\mbox{row rank} \, T = \mbox{column rank} \, T. 
$$
 
 From Exercise 3, this is equivalent to the usual claim that row and column spaces of an arbitrary matrix have the same dimension. 
 
<b>Proof.</b> The following square commutes: 
 
<div class="separator" style="clear: both; text-align: center;">
</div>
<div class="separator" style="clear: both; text-align: center;">
<a href="https://1.bp.blogspot.com/-Myv5SXrt8FM/WEzakAUMxvI/AAAAAAAAChU/27YydKMzJwc5haR-gD6_bEc8FW5go3YhQCLcB/s1600/rank-square.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="160" src="https://1.bp.blogspot.com/-Myv5SXrt8FM/WEzakAUMxvI/AAAAAAAAChU/27YydKMzJwc5haR-gD6_bEc8FW5go3YhQCLcB/s200/rank-square.png" width="200" /></a></div>
 
 
In other words, $\iota_W \circ T = T^T \circ \iota_V$. To see this, just note for arbitrary $v \in V$, $w\in W$,

$$
[\iota_W \circ T (v)](w) = \langle Tv, w \rangle = \langle v, T^t w \rangle = [T^t \circ \iota_V (v)](w).
$$
 
Taking the rank of each side, and noting that $\iota_{V, W}$ are full-rank, we are done. $\blacksquare$
 
 
### References
 
- *Linear Algebra Done Right* (2014), Sheldon Axler.
