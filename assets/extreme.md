---
Layout: post
mathjax: true
comments: true
title:  "Extreme statistics"
categories: [Mathematics, Statistics]
date:  2020-08-13
---

**August 13, 2020.** *A quick introduction to extreme values.*

#### Extreme values in politics and probability

I recently stumbled onto the
[beautiful lectures](https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB175818.xhtml)
of [Emil Gumbel](https://en.wikipedia.org/wiki/Emil_Julius_Gumbel) on
the statistics of extreme values, an area he helped
found along with R. A. Fisher and Leonard Tippett.
Gumbel was not only a mathematician, but also a prominent anti-Nazi
activist. In the 1920s, he documented political murders by the
*Sturmabteilung*, the Nazi paramilitary wing, and was one of the 33
signatories of the
[*Dringender Appell*](https://en.wikipedia.org/wiki/Urgent_Call_for_Unity),
calling on non-Nazi politicans to unite "in the rejection of fascism"
prior to the 1932 elections.
They did not unite, and the Nazis went on to consolidate their grip
on Weimar politics.
Gumbel was forced to leave his Professorship at Heidelberg shortly
afterwards, moving to France and then the US, where he taught at
Columbia until his death in 1966.

Gumbel's lectures were given, I guess, to the Applied
Mathematics Division at the National Bureau of Standards.
The basic idea is simple: if I take $n$
samples of a random variable with distribution $\mathcal{D}$, what
does the maximum look like?
From a practical perspective, outliers are sometimes more important
than the bulk of observations, for instance with extreme weather
events or fluctations of the financial market.
If your goal is flood management, you don't care about average
rainfall!
I'll discuss applications below.

This is related to a statistical error Gumbel calls the
"three $\sigma$ fallacy" (and I suspect, the main reason the Bureau called him in).
We are used to thinking that observations are "very likely" to fall
within some number of standard deviations of the mean, say three for the normal distribution.
But if I make enough observations, I will almost certainly get extreme
outliers!
If there is some small probability $p$ of being
outside $3\sigma$, then with $n \approx 1/p$ observations, I would
expect to get such an outlier.

My goal is to give a quick outline of some old ideas that were new to
me and that I found useful or cool.
I'll start with some basic results, expanding on the $n
\approx 1/p$ observation, and compute (asymptotically) the expected
largest sample for a Gaussian.
I'll then talk about an analogue of the central limit theorem for
maxima, due variously to Fisher, Tippett and Gnedenko, and end with
applications.

#### Exceedance and return

#### The max central limit theorem

#### Applications

#### References
