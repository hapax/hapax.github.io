---
layout: post
mathjax: true
comments: true
categories: [Mathematics, Biology]
title:  "Replicators and Fisher's Fundamental Theorem"
date:   2017-11-30
---

**November 30, 2017.** *One of the basic tenets of evolution is that different organisms (or genes) have different rates of reproduction. Simple models treating these organisms as replicators, competing for population dominance, are surprisingly rich. I give a simple proof in this context of Fisher's "fundamental theorem" that average fitness increase equals genetic variance.*

### Introduction

Natural selection, as put forward by Darwin and Alfred Russell Wallace in 1858, is a simple set of ideas:
 
- Organisms pass down traits to their offspring.
- There is random variation in the inherited traits.
- This variation leads to differential reproductive success.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Darwin's_finches_by_Gould.jpg/1200px-Darwin's_finches_by_Gould.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="603" data-original-width="800" height="301" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Darwin's_finches_by_Gould.jpg/1200px-Darwin's_finches_by_Gould.jpg" width="400" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;"><a
href="https://en.wikipedia.org/wiki/Darwin%27s_finches">Darwin's
finches</a>, drawn by 19th century zoologist John Gould.</td></tr>
</tbody></table>

The combination of heritability, randomness, and differences in reproduction rate explain how and why species change. But this mechanism is extremely general, so general that it's tempting to view as a theorem about some simpler formal system than Mendelian genetics. In this post, I'll talk about one attempt to formalise natural selection, using the abstract dynamics of *replicators*. We'll derive a few results, including Fisher's infamous *Fundamental theorem of natural selection*.

### Replicators and fitness

In 1930, the great statistician R. A. Fisher published a seminal textbook on evolution, *The Genetical Theory of Natural Selection*. His *fundamental theorem of natural selection* states that

> The rate of increase of fitness of any organism is equal to its genetic variance in fitness at that time.

Fisher likened the result to the second law of thermodynamics, but
there is an amusing amount of disagreement about what Fisher meant and
whether he was correct. Rather than look at Fisher's tortuous proof
(or the only slightly less tortuous results of latter-day
interpreters) I'm going to look at <a
href="http://math.ucr.edu/home/baez/information/information_geometry_16.html">a
simpler setup</a> due to John Baez, and (unlike Baez) use it to derive
the original version of Fisher's theorem.
 
Here is the setup. Suppose we have a bunch of objects $i = 1, \ldots, n$ which can *replicate*, described by a population size $P_i$. These could describe genes, species, are any other objects whose rates of growth are connected. In general, the rate of growth of population $i$ will be proportional to the current population size $P_i(t)$, with some coefficient which will depend on the other populations, and possibly on time. We define the *fitness* $f_i$ as that coefficient, so that 

$$ 
\frac{dP_i}{dt} \equiv f_i(t, P_1, \ldots, P_n)P_i(t). \tag{1} 
$$
 
The fitness function is very general: it can incorporate competition between populations, *within* populations (e.g. <a href="https://en.wikipedia.org/wiki/Carrying_capacity">carrying capacity</a>), and time-dependent effects like environmental change. In the evolutionary context, we are typically interested in *relative* rather than absolute population size; in other words, we want to see which replicators are thriving. The relative size of the $i$th population is 

$$ 
p_i(t) \equiv \frac{P_i(t)}{\sum_j P_j(t)} \equiv \frac{P_i(t)}{P_\text{tot}(t)}. 
$$
 
We picture $P_i$ and $p_i$ below: 
 
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-F1YHfzqg5rs/WiDci0UnfoI/AAAAAAAAKGc/iNqgdWZVNQMFl6_S2ELs1Kdh-JuJsWnPgCK4BGAYYCw/s1600/replicators.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="158" src="https://1.bp.blogspot.com/-F1YHfzqg5rs/WiDci0UnfoI/AAAAAAAAKGc/iNqgdWZVNQMFl6_S2ELs1Kdh-JuJsWnPgCK4BGAYYCw/s400/replicators.png" width="400" /></a></div>
 
Now, $p_i(t)$ is equal to the probability that a randomly chosen individual will be of type $i$, and we can therefore calculate the mean for objects $A_i$ associated with replicators, viewed as discrete random variables: 

$$ 
\langle A(t, P)\rangle \equiv \sum_i p_i(t) A_i(t, P). 
$$
 
The rate of change of the relative size is then 

$$ 
\begin{align*} 
\frac{d p_i(t)}{dt} & = \frac{1}{P_\text{tot}(t)}\frac{dP_i(t)}{dt}-\frac{P_i(t)}{P^2_\text{tot}(t)}\sum_j\frac{dP_j(t)}{dt}\\ 
& = f_i p_i(t) - p_i(t)\sum_j f_j p_j(t) \\ & = (f_i-\langle f\rangle)p_i(t), 
\end{align*} 
$$
 
or simply 

$$ 
\frac{d\ln p_i}{dt} = f_i-\langle f\rangle. \tag{2} 
$$
 
This is called the *replicator equation*. It says that the success of a replicator (measured as the growth of the log probability $\ln p_i$) is the difference between its fitness and the *mean* fitness. 
 
While the logarithmic growth of a replicator is related to the replicator mean, it turns out that the *variance* of the replicator fitness tells about how the overall probability distribution is changing. A quick calculation shows that 

$$ 
\left\langle\left(\frac{d\ln p}{dt}\right)^2 \right\rangle = \sum_i p_i\left(\frac{d\ln p_i}{dt}\right)^2 = \sum_i (f_i-\langle f\rangle)^2 p_i, \tag{3} 
$$
 
We can think of the LHS as the *squared speed* of the probability distribution $p_i$ (see Baez's article for more on this). This squared speed equals the variance of the fitness. Again, this makes sense! If there is a large spread of fitness, then the probability distribution will be moving quickly to adjust. If the fitnesses $f_i$ are all equal, then the populations will be in equilibrium. We can summarise these two results: 
<ul>
<li>Replicator success is the difference between fitness and mean fitness.</li>
<li>The rate of change of the replicator distribution is the standard deviation of replicator fitness.</li>
</ul>
Baez's article shows how this is connected to the *Fisher information metric* and *relative entropy*. I'll leave that as homework for the interested reader, though I've put a couple of related exercises below. 
 
**Exercise 1.** *Entropy and relative entropy.* 
(a) Derive result (3). 
(b) The *entropy* of a probability distribution $p_i$ is defined by 

$$ 
S(p) \equiv -\sum_i p_i \ln p_i = \langle \ln p\rangle. 
$$
 
This quantifies the amount of information in the distribution $p_i$. Show that 

$$ 
\frac{d}{dt}S[p(t)] = - \langle (f-\langle f\rangle) \ln p\rangle. 
$$
 
Qualitatively, consider what happens to entropy when low probability populations have above or below average fitness. Do your results this make sense? 
(c) The *relative entropy* of a probability distribution $q_i$ relative to $p_i$ is the quantity 

$$ 
S(q|p) \equiv \sum_i q_i \ln\left(\frac{q_i}{p_i}\right). 
$$
 
This is a measure of how different the distribution $q_i$ and $p_i$ are; put a different way, it tells us how much additional information we get if we update to $q_i$ from $p_i$. Show that 

$$ 
\left\langle\left(\frac{d\ln p}{dt}\right)^2 \right\rangle = \frac{d^2}{dt^2}S[p(t)|p(t_0)]\bigg|_{t=t_0}. 
$$
 
Thus, the second derivative of relative entropy equals the variance of replicator fitness. 
 
### Fisher's Fundamental Theorem
 
Of course, Fisher's fundamental theorem is about the change in the fitness. 

$$ 
\begin{align} 
\frac{d\langle f\rangle}{dt} & = \sum_i \bigg[\frac{df_i}{dt} p_i(t) + f_i(f_i-\langle f\rangle)p_i\bigg]\\ 
&= \sum_i \bigg[\frac{df_i}{dt} p_i(t) + (f_i-\langle f\rangle)^2p_i\bigg]\\ 
%&= \left\langle \frac{df}{dt} \right\rangle + \left\langle (f-\langle f\rangle)^2\right\rangle \\ 
& = \left\langle \frac{df}{dt} \right\rangle + \text{var}(f), 
\end{align} 
$$
 
where we used the fact that $\langle f - \langle f\rangle\rangle = 0$ on the second line. But this is (a slightly more general) version of Fisher's theorem! We see that the rate of change in mean fitness is a sum of two terms: the variance of the fitness, as Fisher originally stated, plus the average time derivative. This latter can incorporate environmental factors, competition, and other things that Fisher specifically excluded from his result. From the previous section, we know the former captures the rate of change (squared) of the probability distribution. To sum up, 
<blockquote class="tr_bq">
The rate of change of mean replicator fitness is the mean rate of change plus the variance.</blockquote>
In particular, if the mean rate of change vanishes, the mean fitness will not decrease, since variance is positive. The intuition here is clear: if there are no external forces acting on the fitness parameters, then more fit replicators will grow faster and the mean fitness will get bigger. But if these successful replicators *already* dominate, the mean fitness will be close to the fitness of the successful replicators, and the rate of change will be slow, since there is little room for improvement. Mean fitness increases quickly when there is plenty of probability concentrated in less fit replicators, i.e. the variance of the fitness is large. So, roughly speaking, we would expect the mean fitness to look like a <a href="https://en.wikipedia.org/wiki/Sigmoid_function">sigmoid</a>. We can check for a simple example! See Exercise 2. 
 
Where is the mutation is in the replicator picture? In fact, we can think of the replicators as representing the distribution of <a href="https://en.wikipedia.org/wiki/Allele">alleles</a> at a particular genetic locus, among members of a given species; the change in the distribution of alleles *is* the mutation. Clearly, this is not terribly realistic. And although we can use the replicator model to treat both species *and* genes, with populations $P_{sg}$ (species $s$ and gene $g$), it would clearly be nicer to use a framework with a hierarchical distinction between the two. That said, replicators are possibly the simplest model satisfying Fisher's theorem, and therefore a nice playground for looking at the dynamics of natural selection. 
 
**Exercise 2.** *Two replicators.* Let's do a simple model to get some intuition. Suppose we have two replicators $P_1(t), P_2(t)$, with *constant* fitness $f_2 > f_1$, and $\Delta \equiv f_2 - f_1 > 0$. 
(a) Show that 

$$ 
p_1(t) = \frac{P_1(0)}{P_1(0)+P_2(0)e^{\Delta t}}, \quad p_2(t) = \frac{P_2(0)e^{\Delta t}}{P_1(0)+P_2(0)e^{\Delta t}}. 
$$
 
 
(b) Calculate $\langle f\rangle$, and show that as $t \to \infty$, $\langle f\rangle \to f_2$. Plot your results for some particular values. You should obtain a sigmoid, like the plot below. 
 
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-xnW1iloOnvo/Wh-c4_H84NI/AAAAAAAAKFo/Ei6j2zCBWqYWe8VAXcTxt4cSqIaluqxqgCK4BGAYYCw/s1600/Screen%2BShot%2B2017-11-29%2Bat%2B9.52.56%2BPM.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="90" src="https://1.bp.blogspot.com/-xnW1iloOnvo/Wh-c4_H84NI/AAAAAAAAKFo/Ei6j2zCBWqYWe8VAXcTxt4cSqIaluqxqgCK4BGAYYCw/s400/Screen%2BShot%2B2017-11-29%2Bat%2B9.52.56%2BPM.png" width="400" /></a></div>
(c) Verify that 

$$ 
\frac{d\langle f \rangle}{dt} = \frac{\Delta^2 P_1(0)P_2(0) e^{\Delta t}}{[P_1(0)+P_2(0)e^{\Delta t}]^2}, 
$$
 
and show this agrees with the variance 

$$ 
\text{var}(f) = p_1(t)(f_1 - \langle f\rangle)^2 + p_2(t)(f_2 - \langle f\rangle)^2. 
$$
 
 
(d) Finally, show that the rate of growth of $\langle f\rangle$ is largest when 

$$ 
t_\text{max} = \frac{1}{\Delta}\log\left[\frac{P_1(0)}{P_2(0)}\right]. 
$$
 
We can treat $t_\text{max}$ as a proxy for how long it takes for the fitter replicator $P_2$ to "win out". This result makes the sensible prediction that the process is slower when $f_2$ and $f_1$ are closer, or when the initial population of $P_1$ is made larger. 
