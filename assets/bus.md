---
Layout: post
mathjax: true
comments: true
title:  "A quick proof of the bus paradox"
categories: [Mathematics, Statistics]
date:  2021-01-26
---

**January 26, 2021.** *The bus paradox states that, if buses arrive
  randomly every ten minutes on average, the average waiting time is
  ten minutes rather than five. I give a simple, geometric proof and
  generalise in various directions.*

#### Introduction

The bus paradox (also called the waiting time or
[inspection paradox](https://en.wikipedia.org/wiki/Renewal_theory#Inspection_paradox))
is a counterintuitive result about waiting times between random events.
Suppose buses arrive randomly, with an average period of $\lambda$
between arrivals.
If you go to catch a bus, you might expect to wait a period
$\lambda/2$, since if a bus arrives $\lambda/2$ after you arrive, and
$\lambda/2$ before you arrive (by symmetry), then the gap between them
is $\lambda$.
This reasoning is wrong, and rather unexpectedly, the expected wait
time is $\lambda$.
The goal of this post is to share a quick geometric proof which does
not require any integrals or formal probability theory at all, and
makes the role of various assumptions manifest.
It is novel to the best of my knowledge.

#### The bus loop

We start by considering a circle of total length $L$, on
which we place $k$ points at random.
This models a length of time, such as the day, and the random arrival
of $k$ buses.
The average distance between points (going clockwise, for instance) is clearly

$$
\lambda = \frac{L}{k}.
$$

Let us place another point on the circle at random.
This represents the patron who wishes to catch a bus.
Since we now have $k + 1$ points placed at random, the same reasoning
as above tells us that the average distance is

$$
\frac{L}{k +1} = \left(\frac{k}{k+1}\right)\lambda.
$$

Translating into the language of bus schedules, this means that if
buses have a fixed but random schedule over some length of time, with
average interarrival time $\lambda$, the expected wait time is *not*
$\lambda$, but rather, smaller than $\lambda$ by a factor of
$k/(k+1)$, where $k$ is the total number of buses over the period.

#### The bus paradox

The bus paradox applies to a schedule which does not repeat.
Let us take $L, k \to \infty$ but leave $\lambda = L/k$ fixed.
Then the expected waiting time is

$$
\left(\frac{k}{k+1}\right)\lambda \to \lambda.
$$

Thus, the patron is equivalent to adding another random bus, but since
there are so many buses, the interarrival time is the same.
This completes is our simple proof of the bus paradox.
