---
layout: post
mathjax: true
comments: true
categories: Philosophy
title:  "Cigarettes, hard labour and a box full of money"
date:   2017-08-11
---
	
**August 11, 2017**. *Three paradoxes of rational action --- the Prisoner's Dilemma (rational behaviour for you may not be collectively rational), Newcombe's paradox (correlation is not causation), and the Smoker's Dilemma (common cause is correlation) --- coincide in certain contexts. I explain in more detail what these paradoxes are and how they can be viewed as equivalent.*

### Introduction

Cooperation is a funny thing. Paying taxes, voting, and avoiding nuclear war, all depend on behaviour which may in some sense be *irrational*. Basically, if you default on cooperation, you tend to be better off. The problem is that if everyone defaults, we're all worse off. (The case with nuclear war is particularly vivid.) This is called the Prisoner's Dilemma: what's rational for an individual is bad for the group when everyone does it.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="https://upload.wikimedia.org/wikipedia/commons/b/bd/A_Dilemma%2C_by_Charles_Keene.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="800" data-original-width="677" height="400" src="https://upload.wikimedia.org/wikipedia/commons/b/bd/A_Dilemma%2C_by_Charles_Keene.jpg" width="336" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">A Dilemma, Charles Keene (1910).</td></tr>
</tbody></table>

As I'll explain below, this argument works when the defaulter has no influence on other actors. But although decisions may be *causally* independent, other people reason the same way as us and there may be *correlation* between decisions. Whether we should take this into account as rational actors leads to *Newcomb's Paradox*: non-causal correlations are confusing. The *Smoker's Dilemma* is a statistical instance of the paradox. Below, I'll describe these problems in more detail, and explain why, surprisingly, they are *the same* problem in different guises!
 
### Prisoner's Dilemma
 
The classic Prisoner's Dilemma involves two prisoners, A and B, suspected of jointly committing a crime. They are separated and given two options: 

1. *Cooperate* with each other by staying mum.
2. *Defect* by confessing to the crime and ratting on their partner.

If both defect, each gets 10 years hard labour; if one defects and the other doesn't, the defector goes free and the cooperator gets 15 years hard labour; and if both stay silent, each gets 1 year. We can summarise this payoff structure in a table, with outcome (*a*, *b*) indicating A gets *a* years and B gets *b* years: 
 
<table>
  <tbody>
<tr>
    <td> </td>
    <td>B1</td>
    <td>B2</td>
  </tr>
<tr>
    <td>A1</td>
    <td>(1, 1)</td>
    <td>(15, 0)</td>
  </tr>
<tr>
    <td>A2</td>
    <td>(0, 15)</td>
    <td>(10, 10)</td>
  </tr>
</tbody></table>
 
It seems rational for both prisoners to defect, *whatever the other prisoner does*. Take A for instance. If B defects, then A gets 10 years by defecting, and 15 years otherwise; if B cooperates, A goes free if they defect, but is sentenced to 1 year if they cooperate. Either way, defecting is the best option. Since the prisoners decide independently, each seems rationally compelled to defect, earning them 10 years hard labour. But here's the dilemma: if they cooperate, they both get 1 year, a significantly better outcome for all concerned! In the language of game theory, defection *dominates* cooperation, and the prisoners arrive at the conclusion to defect based on *dominance reasoning*. 
 
(*Technical note*: The double defection is a *Nash equilibrium*, since the prisoners' strategies are stable under learning of the other prisoner's strategy, but not *Pareto efficient*, since we could reallocate sentences to make both better off, i.e. if both cooperate. So, we can rephrase the Prisoner's Dilemma as the existence of Pareto inefficient Nash equilibria.) 
 
We can tweak the prisoner example a little and turn it into the *Free Rider Problem*. Suppose I can avoid paying tax without being fined (e.g. using an offshore bank account). Usually, my marginal contribution will be so small that it makes no effective difference to the tax-funded services provided by the government. Here, avoidance dominates paying tax: my contribution makes no real difference to government service provision, so I always prefer to avoid paying, leaving me with more money and no difference in services. Of course, in a society of rational free riders, there will be *no* public services, a bad situation for everyone. In general, whenever marginal contributions to a collective good are negligible, we get a Free Rider problem. For more on the application of game theory to public choice and institutional design, see Dennis Mueller's book. 
 
Note that we are assuming the payoffs are determined by a single game, or *one-shot* Prisoner's Dilemma. We are ignoring the possibility that the prisoners (or free riders) play subsequent games in which past behaviour can be punished or rewarded. Playing multiple repeated Prisoner's Dilemmas is called the *iterated* Prisoner's Dilemma, and is a fascinating and strategically much richer problem. Surprisingly, the most robust strategy is very simple: cooperate unless the other prisoner defected on the last turn. In the technical literature, this is called *tit-for-tat*. Nicky Case made <a href="http://ncase.me/trust/">this wonderful interactive guide</a> to the iterated Dilemma. 
 
### Symmetry and oracles
 
A very natural reply to the Prisoner's Dilemma is that, if both prisoners are rational and *know* they are both rational, they will end up making the same decision. So they can simply eliminate the possibility they make different decisions, leaving two options: both defect and get 10 years, or both cooperate and get 1 year. No dilemma now! They should obviously cooperate. 
 
There are various replies to the symmetry argument. For one thing, the choices are still not *causally* linked, so it's not clear that dominance reasoning doesn't still apply. Whatever B does, it is still better for A to defect, and this choice doesn't magically change B's decision. (The proponent of symmetry would say that it does.) The other problem is uncertainty. In the real world, you can't be 100% sure that the other prisoner is rational, or 100% sure that they know we're rational. 
 
(In general, dominance logic is most compelling under extreme uncertainty, when we have no information about what the other party will do. But if we have more data, such as a probability distribution over their strategies, I think it makes more sense to play the numbers and maximize expected utility.) 
 
Rather than try to resolve these problems, let's change perspective and view them in a different way. The mysterious relation between the prisoners' decisions indicates that it might be more helpful to treat the other prisoner as an *oracle*. For instance, A can think of B as *predicting* A's decision (via their own decision), and revealing their prediction afterwards. Any doubt is simply doubt about the reliability of the oracle, and causality doesn't come into play since the oracle is by nature spooky. 
 
So, we can reframe the Prisoner's Dilemma as a problem involving *one* prisoner (say A) and an oracle (B). I think this setup is an excellent <a href="https://en.wikipedia.org/wiki/Intuition_pump">intuition pump</a> to undermine our confidence in dominance reasoning. If the oracle correctly predicts A will defect, A gets 10 years; if the oracle correctly predicts A will cooperate, A gets 1 year. Otherwise, A gets 15 years (for cooperating) or goes free (for defecting). What should A do? (Naturally, that depends on the nature and reliability of the oracle, which I think pushes us towards the expected utility strategy mentioned earlier.) 
 
### Newcomb's Paradox
 
Take the extreme case of an oracle who is *100% reliable*. For instance, our oracle, prisoner B, may be clairvoyant, or a telepath who can read A's mind. Whatever the mechanism, Prisoner A knows the oracle has a perfect record. Let's reframe the choices slightly. Instead of deciding to cooperate or defect, A now gets a basic sentence of 15 years. To determine the final sentence, they are presented with two boxes, allowed to open any combination they please, and subtract whatever is in the box from their sentence. More about the boxes: 
<ol>
<li>The first box always contains a decrement of 1 year.</li>
<li>The contents of the second box depend on the oracle's prediction:</li>
<ol>
<li>If the oracle predicts the prisoner opens box 1, box 2 contains a decrement of 9 years.</li>
<li>If the oracle predicts the prisoner does not open box 1, box 2 contains a decrement of 14 years.</li>
</ol>
</ol>
You can easily check that the outcomes here match the earlier sentences, provided we interpret choosing boxes 1 and 2 as *defection*, and choosing only box 2 as *cooperation*. (It's clear that, if prisoner A wants to minimise their sentence, they always choose box 2, so the only real decision is whether or not to choose box 1.) 
 
This is almost identical to the canonical statement of *Newcomb's Paradox*. Instead of sentence decrements, the prisoner and oracle play a game where the boxes are filled with money. In box 1, there is a thousand dollars and in box 2, there is a million dollars, provided the oracle guesses they will only choose box 2, otherwise it is empty. The payoff structure is exactly the same as the Prisoner's Dilemma. In either case, the crux of the paradox is that, when the boxes are presented, the *contents are fixed*. The prisoner's decision does not affect what is in them. Thus, they can choose to pick box 1, and it will do nothing to the contents of box 2; that was determined earlier by the oracle's prediction. 
 
In this situation, regarding the contents of boxed as fixed, and trying to maximise your payoff, is analogous to using dominance logic. *Two-boxers* think we should pick both boxes, and by analogy, should regard defection as the rational strategy for rational prisoners (where rationality is common knowledge). *One-boxers* hold that we should should take the oracle's predictions seriously and only pick box 2 to maximise payoff. By analogy, we would expect one-boxers to cooperate in the Prisoner's Dilemma, at least if the prisoners are rational. The crux of the issue, for both Newcomb's Paradox and the (rational) Prisoner's Dilemma, is how to think about non-causal correlations. 
 
### Cigarettes may kill you
 
The last avatar of the Prisoner's Dilemma involves nothing fancier than a *common cause*. Suppose that both smoking and lung cancer are caused by a gene G. This leads to a correlation (with correlation coefficient $\rho$, say), rather than a direct causal relationship, between smoking and cancer. Here is the dilemma: should you smoke? I don't know if this version has its own name, but I think the *Smoker's Dilemma* is reasonably punchy. 
 
Since smoking doesn't affect your DNA, it doesn't affect the presence of G and hence your chance of getting cancer. So, if you enjoy cigarettes, it seems like you should smoke whether or not you have the gene! This is just the familiar dominance logic in action. But now we can think of G as an oracle, and cancer as equivalent to no money in the second box. Without belabouring the analogy, setting $\rho = 1$ yields Newcomb's Paradox, with nothing supernatural about the correlations. A weaker correlation is the equivalent to a less reliable oracle. 
 
### Conclusion
 
That concludes our whirlwind tour of the paradoxes of rational choice! I think it's cool that these superficially very different problems are essentially the same. However, it's worth noting that they have different parameters and generalise in different directions. The Prisoner's Dilemma leads naturally to iterated games and multiplayer dilemmas, with the associated bugbears of collective action (Mueller's book has much more on this). Newcomb's Paradox connects to traditional philosophical issues like free will and determinism (and even time travel if the oracle uses a time machine to send information back in time). Finally, the Smoker's Dilemma is related to the broader problem of what causation means operationally, particularly when we have a big network of interrelated random variables. 
 
I haven't spent too much time talking about solutions to these problems, but I think that a good rule of thumb (stated earlier) is that dominance logic applies under extreme uncertainty, for instance, when you know *nothing* about the other prisoner. If we have more information at our disposal, then maximising expected utility seems like a better strategy. Indeed, it's not clear why you *wouldn't* want to maximise your expected utility! Two-boxers/defectors will argue that dominance logic always guarantees a better outcome, but I think that's only persuasive if we ignore the oracular (or for the two-player versions, symmetric) nature of these problems. 
 
### References

- *Paradoxes of Rationality and Cooperation* (1985), ed. Richmond Campbell.
- "Prisoners' Dilemma is a Newcomb Problem", *Philosophy and Public Affairs* 8:3 (1979), David Lewis.
- *Public Choice* (2003), Dennis Mueller.
