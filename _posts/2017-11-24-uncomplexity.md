---
Layout: post
mathjax: true
comments: true
categories: Physics
title:  "Safely falling into black holes"
date:  2017-11-24
---

**November 24, 2017.** *If I entangle two quantum computers, I sometimes get a wormhole, with each end associated to a computer.
The amount of useful computation left on each system equals the volume
of black hole spacetime left to safely jump into!
"Safe" means you don't get fried by a [firewall](https://en.wikipedia.org/wiki/Firewall_(physics)) or collide with junk thrown in from the other end of the wormhole.
A summary of [Uncomplexity and black hole geometry](https://arxiv.org/pdf/1711.03125.pdf)
(Ying Zhao, 2017) for a group meeting.*

Loosely speaking, <i>uncomplexity </i>is<i>&nbsp;</i>a measure of the amount of useful computation a quantum system can still perform. It is to computers what free energy is to thermodynamic systems. Zhao's goal is to give an operational definition of uncomplexity when you only have access to part of the system. In this case, the part of the system we can access is in a&nbsp;<i>mixed state</i>.<br />
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="https://upload.wikimedia.org/wikipedia/commons/d/db/Hard_drive-bottom.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="693" data-original-width="800" height="277" src="https://upload.wikimedia.org/wikipedia/commons/d/db/Hard_drive-bottom.jpg" width="320" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;"><i>A slightly more familiar computational resource.</i> Source: Wikimedia Commons.</td></tr>
</tbody></table>
For quantum information theorists, an operational notion of mixed-state uncomplexity might be useful, but I'm not sure what for.&nbsp;For holographers, though, Zhao gives a compelling gravitational interpretation when the quantum system is an asymptotically anti-De Sitter wormhole. In this case, the subsystem we control is one side of the wormhole. There is an older holographic story (reviewed below) suggesting that uncomplexity is dual to the volume of the black hole you can dive into, but Zhao goes further, identifying&nbsp;subregions dual to various interesting boundary operations. Let's "dive into" the details!<br />

<h3>
Introduction</h3>
<div>
I'll start by quickly reviewing some background on complexity, based on the following:</div>
<div>
<ul>
<li><a href="https://arxiv.org/pdf/hep-th/0106112.pdf"><b><i>Eternal black holes in Anti-de-Sitter</i></b></a>&nbsp;(2001), Juan Maldacena.</li>
<li><b><i><a href="http://xxx.lanl.gov/pdf/0808.2096v1">Fast Scramblers</a></i></b>&nbsp;(2008), Yasuhiro Sekino and L. Susskind.</li>
<li><b><i><a href="https://arxiv.org/abs/1607.05256">The Complexity of Quantum States and Transformations: From Quantum Money to Black Holes</a></i></b>&nbsp;(2016), Scott Aaronson.</li>
<li><a href="https://arxiv.org/pdf/1608.02612.pdf"><i><b>Quantum Complexity and Negative Curvature</b></i></a>&nbsp;(2016), Adam R. Brown, Leonard Susskind, and Ying Zhao.</li>
<li><b><i><a href="https://arxiv.org/pdf/1701.01107.pdf">The Second Law of Quantum Complexity</a></i></b>&nbsp;(2017), Adam R. Brown and Leonard Susskind.</li>
</ul>
<div>
(I have used images from Zhao's paper and papers by Susskind.) First of all, what the heck is "complexity"? In computer science, complexity usually has something to do with resource use. In this case, it's the number of basic gates needed to simulate some target unitary dynamics. Put more colourfully, it's the smallest number of quantum lego pieces needed to build a given model. There is an <a href="https://arxiv.org/pdf/1607.05256.pdf">interesting connection</a>&nbsp;to complexity classes, but it won't come up here.</div>
<div>
<br /></div>
<div>
Let's be more precise. To define complexity, we need to specify two things:</div>
<div>
<ul>
<li>a universal set of gates $\mathcal{G}$, i.e. a finite set we can use to build any unitary operator to desired precision; and</li>
<li>a choice of precision $\epsilon$.</li>
</ul>
</div>
<div>
The (circuit) <i>complexity</i> of a unitary operator $U$ is just the minimum number of gates from $\mathcal{G}$ needed to approximate $U$ to the desired precision:</div>
<div>
\[<br />
\mathcal{C}(U) \equiv \min \#\{\text{$\mathcal{G}$-circuits
$\epsilon$-approximating } U\}.
\]Morally speaking, we can define <i>the complexity of a pure state</i>&nbsp;$|\psi\rangle$ as the complexity of the unitary which prepares $|\psi\rangle$ from some reference state. If we are only interested in states connected by unitary time evolution, this naive definition works: the reference state is just the initial state $|\psi(0)\rangle$, and the unitary "preparing" the state at time $t$ is $U = e^{-iHt}$, so<br />
\[<br />
\mathcal{C}|\psi(t)\rangle = \mathcal{C}(e^{-iHt}).<br />
\]This doesn't help us define the complexity of a mixed state. Typically, we care about mixed states that arise from tracing out a subsystem when the full state is pure, so we might think that we can just consider the state complexity of the purification. But we can get the <i>same</i> reduced density from different pure states, and in general, these pure states will have different complexities!<br />
<h3>
Fast scramblers and a second law</h3>
Now for some dynamics. Suppose you have $N$ qubits and want to build a quantum circuit model of a black hole. According to the standard lore&nbsp;black holes are <i>fast scramblers</i>, i.e. a local disturbance spreads exponentially and infects the whole system in the <i>scrambling time</i> $\tau_* \sim \log N$. There is a cute cartoon model of fast scramblers: the <i>random circuit model</i>, where we discretise time $\tau$, and at each time step, we choose a random element from our gate set $\mathcal{G}$ and a random subset of qubits for it to act on. Then we add this random gate it a chain of random gates. The near horizon region of the black hole performs computations approximately described by this circuit.<br />
<br />
So, at time $\tau$, we have a circuit $U(\tau)$ made of $\tau$ gates, and we can ask how its complexity $\mathcal{C}(\tau) \equiv \mathcal{C}[U(\tau)]$ changes with time.

The current state of the art is numerology. The space of unitaries has dimension $\sim 4^N$, so an $\epsilon$-net
spanning the space (which is specified by our approximation) has $\epsilon^{4^N} \sim e^{4^N}$ elements.
It is large, and early on, the probability of "short circuits"
(i.e. more efficient descriptions of the circuit) is basically zero. Thus, the complexity grows linearly, $C(\tau) \sim \tau$.
Since the number of possible circuits grows exponentially with the
number of gates, the maximum complexity is<br />
\[<br />
C_\text{max} \sim 4^N,<br />
\]
and hence the linear growth maxes out around $\tau \sim 4^N$. In the language of probability theory, adding random gates is a random walk in a high-dimensional circuit space. Initially, this space looks infinite, and hence non-recurring, to the walker; but walk long enough and you hit the boundary, where complexity starts to saturate. You can get recurrences which reset the complexity to near zero, but the <i>Second Law of Quantum Complexity</i>&nbsp;states that complexity almost always increases, or more precisely<br />
<blockquote class="tr_bq">
If the complexity is less than maximum, it will most likely be in a
<i>local</i> minimum.</blockquote>
As the name suggests, there is a strong analogy between complexity and entropy. The big difference is that we have replaced combinatorics over <i>states</i> with combinatorics over <i>operators</i>. This means that the quantum complexity of a system with $N$ qubits behaves like the entropy of a classical system with $2^N$ degrees of freedom; this parallel can be made more precise using Nielsen's complexity geometry, which you can read about in Brown and Susskind's paper. Entropy can be expended uselessly, as when a gas expands in a box without a turbine; similarly, a black hole generates useless complexity, squandering its computational power on, well, simulating a black hole. Turning things around, in the same way that an entropy gap can be harnessed to deliberately move a system between macroscopic states, Brown and Susskind conjecture that a complexity gap can be harnessed to do quantum computations.<br />
<br />
They give the concrete example of how adding a single "clean" qubit to a dirty old maxed out system allows to perform a useful computational task (in their example, computing a trace). Thus, we are led to define the <i>uncomplexity</i><br />
\[<br />
\mathcal{UC}(\tau) \equiv \mathcal{C}_\text{max} - \mathcal{C}(\tau).<br />
\]It should quantify the amount of <i>useful</i> computation the system can do.<br />
<h3>
Complexity = action, uncomplexity = interior</h3>
If the random circuit is a toy model for a black hole, what is the gravity dual of complexity?<br />
For illustrative purposes, suppose we have a one-sided AdS black hole,
with an observer Alice stationed on the boundary. The proposed dual to
complexity is the <i>Einstein-Hilbert action of the Wheeler-deWitt</i>
(WDW) patch. The WDW patch consists of all spacelike surfaces anchored
at boundary time $t$:<br />
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-zis3uRSiMG4/Wn_bYsbiwZI/AAAAAAAAM6c/KiuRQYFAkJINPdtFScBqsCfQPfXAGnjfQCK4BGAYYCw/s1600/susskind-brown-1.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" src="https://2.bp.blogspot.com/-zis3uRSiMG4/Wn_bYsbiwZI/AAAAAAAAM6c/KiuRQYFAkJINPdtFScBqsCfQPfXAGnjfQCK4BGAYYCw/s1600/susskind-brown-1.png" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">The (regulated) WDW patch for Alice.</td></tr>
</tbody></table>
<br />
This proposed duality goes by the slogan "Complexity = Action". The
action is of the same order as the volume $V(t)$, and a classical
calculation shows that $V(t)$ does indeed grow linearly. For reasons I
don't fully understand, at some late time $t_\text{cutoff}$, this
classical linear growth stops, the black hole develops a firewall, and
the interior spacetime breaks down. This defines a WDW patch of
maximal complexity.<br />
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-4Mx3KiOOOa0/Wn_bp5zk2rI/AAAAAAAAM6k/1pJSQww8ZHk1v8jofzX6k2zZZFlsbWe5QCK4BGAYYCw/s1600/susskind-brown-2.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" src="https://1.bp.blogspot.com/-4Mx3KiOOOa0/Wn_bp5zk2rI/AAAAAAAAM6k/1pJSQww8ZHk1v8jofzX6k2zZZFlsbWe5QCK4BGAYYCw/s1600/susskind-brown-2.png" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">The maximal complexity patch.</td></tr>
</tbody></table>
<br />
So, the uncomplexity (difference between the maximal WDW patch and
Alice's current patch) is the volume of the blue patch in the
following picture:<br />
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-WCC-_Y5XK1c/Wn_cGJnhnKI/AAAAAAAAM6s/Aa4xpYibkzEJ5HeRWn-nUDmfHaSBgsr-gCK4BGAYYCw/s1600/susskind-brown-3.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" src="https://3.bp.blogspot.com/-WCC-_Y5XK1c/Wn_cGJnhnKI/AAAAAAAAM6s/Aa4xpYibkzEJ5HeRWn-nUDmfHaSBgsr-gCK4BGAYYCw/s1600/susskind-brown-3.png" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">The interior spacetime available to Alice.</td></tr>
</tbody></table>
<br />
But if Alice can ride along on the thin blue null line (e.g. encode herself into laser pulses), the blue patch is precisely the interior region of the black hole she can visit! So the uncomplexity is the <i>interior spacetime</i>&nbsp;available for Alice to visit when she hops into the black hole.<br />
<h3>
Uncomplexity for mixed states</h3>

With that preamble out of the way, let's finally start discussing the paper! As I said earlier, the idea of the paper is to define the uncomplexity of a mixed state in terms of the computational resources of a subsystem. In particular, we don't need to define the complexity of a mixed state; we do require some notion of pure state complexity however. Consider a bipartite system $AB$ in a pure state $|\psi\rangle_{AB}$, with reduced density matrices $\rho_A$ and $\rho_B$ belonging to Alice and Bob respectively. What sort of computations can Bob do with his density matrix? Well, Bob can apply unitaries $U_B$, and these generically <i>increase</i>&nbsp;the overall complexity of the state. So as a first try, we might think of the uncomplexity as the maximal increase in complexity of the state:<br />
\[<br />
&nbsp; \mathcal{UC}(\rho_B) \overset{?}{\equiv} \max_{U_B}<br />
&nbsp; \mathcal{C}(U_B|\psi\rangle) - \mathcal{C}|\psi\rangle.<br />
\]But not every unitary is a useful computation for Bob. For instance, if Alice and Bob share a bunch of maximally entangled Bell pairs, then under a unitary $U_B$, Bob's density stays the same:<br />
\[<br />
\rho_B \to \rho_B \mapsto U^{\dagger}\rho_B U = \rho_B.<br />
\]Bob's operation $U_B$ may perform computations, but the results are <i>invisible</i> to Bob. To capture useful computations, we subtract off the <i>maximum complexity</i> of these useless computations, rather than the current state complexity:<br />
\[<br />
&nbsp; \mathcal{UC}(\rho_B) \equiv \max_{U_B}<br />
&nbsp; \mathcal{C}(U_B|\psi\rangle) - \max_{U_B^\dagger\rho_B{U_B} =<br />
&nbsp; \rho_B}\mathcal{C}|\psi\rangle. \tag{1}<br />
\]There is a neat way of thinking about this in terms of the Schmidt decomposition. In the Schmidt basis, $\rho_B$ is a diagonal matrix with $k$ distinct eigenvalues (including possibly zero):<br />
\[<br />
\rho_B = \lambda_i I_{N_1} \oplus \cdots \oplus \lambda_k I_{N_k} \oplus 0_{N_0}.<br />
\]Call these components <i>Schmidt blocks</i>. Any "useless" computations $U_B$ by Bob that don't change $\rho_B$ are just <i>separate rotations</i> of the Schmidt blocks, or <i>Schmidt rotations</i>:<br />
\[<br />
U_B \in SU(N_1)\times \cdots\times SU(N_0).<br />
\]These are precisely the unitaries that Alice can undo (by performing the inverse rotations). So we can also think of useful computations for Bob as those <i>that Alice can't undo</i>.<br />
<h3>
Black hole examples</h3>
A nice sanity check is the one-sided black hole (formed from a collapsing shell of photons), where the "subsystem" is in fact the <i>whole</i> system. We've already seen that, in this situation, uncomplexity can be interpreted as the volume of spacetime left for a boundary observer (now Bob rather than Alice) to jump into. We can interpret the terms of formula (1) geometrically:<br />
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-Jt3uNRbyBlA/Wn_dd3HjOoI/AAAAAAAAM68/sBpFtg-dhjMtvkEqAwPcLXRWMp4ygeEagCK4BGAYYCw/s1600/1711.0312-9.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" src="https://4.bp.blogspot.com/-Jt3uNRbyBlA/Wn_dd3HjOoI/AAAAAAAAM68/sBpFtg-dhjMtvkEqAwPcLXRWMp4ygeEagCK4BGAYYCw/s1600/1711.0312-9.png" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Bob's uncomplexity for the one-sided black hole.</td></tr>
</tbody></table>
<br />
Bob's only unitary is time evolution. He maximise complexity by evolving to the cutoff time<br />
$t_\text{cutoff}$ (the first diagram), and the only way to leave his density matrix alone is to stay put (second diagram). The difference between the corresponding WDW patches in the interior<br />
spacetime left for him to jump into.<br />
<br />
The next example is the unperturbed two-sided black hole in AdS, <a
href="https://arxiv.org/pdf/hep-th/0106112.pdf">dual to the
thermofield double</a>. The left side belongs to Alice and the right
side belongs to Bob; we'll focus on Bob's subsystem. The idea here is
that, if Bob's coarse-grained entropy is $S$, then he shares $S$ Bell
pairs with Alice (they are involved in near-horizon computation):<br
/>
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-dnZitxDNXNY/Wn_d0aH4b-I/AAAAAAAAM7E/qQ5kg6wAbwodnOUIZ1VllpvXIBrQQVOwwCK4BGAYYCw/s1600/1711.0312-7.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" src="https://3.bp.blogspot.com/-dnZitxDNXNY/Wn_d0aH4b-I/AAAAAAAAM7E/qQ5kg6wAbwodnOUIZ1VllpvXIBrQQVOwwCK4BGAYYCw/s1600/1711.0312-7.png" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Penrose and circuit pictures of the two-sided black hole.</td></tr>
</tbody></table>
<br />

If they share $S$ Bell pairs, the density matrices are maximally mixed, and the uncomplexity is zero. Geometrically, Bob can go foward in time $t_R \to t_R + \Delta$, but Alice can go forward the same amount $t_L \to t_L + \Delta$ (where Alice's time goes <i>down</i>&nbsp;on the LHS) so that by <a href="https://arxiv.org/pdf/1702.03957.pdf">boost symmetry</a>, the WDW patch has the same size. Geometrically, we see that any change in complexity by Bob can be undone by Alice, which geometrically confirms that Bob has no uncomplexity.<br />
<br />
But aren't we supposed to think of uncomplexity as interior spacetime? It seems like there is plenty of room in the wormhole. The lesson here (which will be made more precise below) is that uncomplexity is interior spacetime <i>that you exclusively control</i>. No one else can mess with it. So we might describe the wormhole as ER = EPR, and uncomplexity with the dorky slogan<br />
\[<br />
\mathcal{UC} = \text{U Control}.<br />
\]

<h3>
Perturbing the TFD</h3>

To understand things a bit better, let's perturb the thermofield double with a thermal photon, first on Alice's side and then on Bob's. Geometrically, if we throw in a photon, it gets seriously blueshifted and create a shockwave geometry, which tilts one side of the Penrose diagram. If we throw it in on Alice's side, she can still undo any operations by Bob by evolving an appropriate time forward. So Bob's uncomplexity is still zero.<br />
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-qNCe0U0kpcI/Wn_enJw7EyI/AAAAAAAAM7U/RaB4Q6mz0SwbVo2t6-KycA0r_wLD26tbACK4BGAYYCw/s1600/1711.0312-8.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="177" src="https://1.bp.blogspot.com/-qNCe0U0kpcI/Wn_enJw7EyI/AAAAAAAAM7U/RaB4Q6mz0SwbVo2t6-KycA0r_wLD26tbACK4BGAYYCw/s640/1711.0312-8.png" width="640" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Adding a thermal photon on Alice's side.</td></tr>
</tbody></table>
<br />
What about if we give it to Bob instead? Since the thermal photon is the gravity dual of a <i>single clean&nbsp;</i><i>qubit</i>, we expect it should buy Bob some uncomplexity. We can freely choose the left time (Bob can always undo that time evolution with his own unitary, as Alice could for him), so we can place it at a cutoff near the top of the Penrose diagram. The maximum complexity Bob can induce is given by some large cutoff time $t_R = t_\text{cutoff}$. If we throw in the photon at time $t_R = t_w$, we have to wait a scrambling time before the photon is incorporated into the quantum circuit. Before then, we can more or less ignore the perturbation, and the situation is basically the same as the two-sided black hole, with right time-evolution leaving Bob's density matrix unaffected. Thus, the second term in (1) is just given by the WDW patch anchored at whichever is bigger of the current time $t_R$, or the time when the photon is scrambled, $\max\{t_w+t_*, t_R\}$. Geometrically, we can picture the two possibilities as follows:<br />
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-Az_h6vpln80/Wn_fnGXuf1I/AAAAAAAAM7g/RQjqeiqsHnouYiklDfOoyhpanqFk0kSUQCK4BGAYYCw/s1600/1711.0312-11.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="133" src="https://4.bp.blogspot.com/-Az_h6vpln80/Wn_fnGXuf1I/AAAAAAAAM7g/RQjqeiqsHnouYiklDfOoyhpanqFk0kSUQCK4BGAYYCw/s640/1711.0312-11.png" width="640" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Correct uncomplexity equation for $t_R &gt; t_w + t_*$.</td></tr>
</tbody></table>
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-nOoldTh3B58/Wn_ftvdJC5I/AAAAAAAAM7o/xi6DNk_iemY6kGp-Do6suAEYIvWJq1KoACK4BGAYYCw/s1600/1711.0312-12.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="168" src="https://1.bp.blogspot.com/-nOoldTh3B58/Wn_ftvdJC5I/AAAAAAAAM7o/xi6DNk_iemY6kGp-Do6suAEYIvWJq1KoACK4BGAYYCw/s640/1711.0312-12.png" width="640" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Not quite correct.</td></tr>
</tbody></table>
<br />
This second diagram is not quite right because we ignored the thermal photon while it was scrambling. We will treat it more carefully in a moment! But the point is that the uncomplexity added to Bob's system is geometrically realised as a region inside the horizon that Bob exclusively controls, i.e. in his entanglement wedge.<br />

<h3>
Subregion duality</h3>

By now, we can see that computations changing Bob's density matrix are connected to the growth of his "one-sided black hole", that is, the interior spacetime in his entanglement wedge. So we would expect the computations which <i>don't</i> change his density matrix, i.e. the Schmidt rotations, fuel the growth of the <i>entanglement region</i>&nbsp;between Alice and Bob. Thus, there is a <i>subregion duality</i>&nbsp;connecting types of operations to regions of space. To check this, it's possible to do a more precise matching between the volume growth of different regions as the photon gets scrambled, creating an "epidemic" of "sick" gates in the quantum circuit.<br />
<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-fZLkqOFSyck/Wn_gHxBnY8I/AAAAAAAAM70/2nvLNB9fHaE90bPzqaFStGj8-XYlPSlIQCK4BGAYYCw/s1600/1711.0312-14.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" src="https://4.bp.blogspot.com/-fZLkqOFSyck/Wn_gHxBnY8I/AAAAAAAAM70/2nvLNB9fHaE90bPzqaFStGj8-XYlPSlIQCK4BGAYYCw/s1600/1711.0312-14.png" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Different regions store different gates.</td></tr>
</tbody></table>
<br />
Up to some minor technical differences, the growth of the entanglement region (orange) matches the operations that can still be undone by Alice, i.e. healthy gates, while the the growth of Bob's entanglement wedge (yellow) matches the number of sick gates. In some sense, the Schmidt rotations are "stored" in the orange entanglement region, while Bob's useful (detectable) computations are<br />
stored in the yellow region.<br />
<br />
This lets us draw the correct geometries for uncomplexity while the
photon is being scrambled. We have to redraw the second diagram slightly in our earlier picture:<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-SWgiZuUiacg/Wn_gUzmPCVI/AAAAAAAAM78/zgG5fMbHOb42l1IdA97_KeYhGznM7tvKwCK4BGAYYCw/s1600/1711.0312-15.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="133" src="https://4.bp.blogspot.com/-SWgiZuUiacg/Wn_gUzmPCVI/AAAAAAAAM78/zgG5fMbHOb42l1IdA97_KeYhGznM7tvKwCK4BGAYYCw/s640/1711.0312-15.png" width="640" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Correct for $t_w &lt; t_R &lt; t_w+ t_*$.</td></tr>
</tbody></table>
<br />
Basically, we leave the operations in the entanglement region alone since this where Schmidt rotations are stored, and shouldn't be affected by the scrambling of the photon. However, within Bob's entanglement wedge, the epidemic growth leads to operations that cannot be undone by Alice; hence can be detected by Bob; and hence <i>do not</i>&nbsp;contribute to computations which don't change Bob's density matix. So we have to excise part of the patch in Bob's entanglement wedge beyond the null line emanating from $t_R$.<br />
<h3>
Recent activity (update August 2018)</h3>
There hasn't been much movement in the subject this year, with only two papers (by my count) on mixed state complexity. Earlier this year,&nbsp;Cesar Agón, Matt Headrick, and Brian Swingle had a crack at the complexity of density matrices in&nbsp;<a href="https://arxiv.org/abs/1804.01561"><b><i>Subsystem complexity and holography</i></b></a>&nbsp;(2018). They present a couple of different recipes. More recently, Henry Stoltenberg surveyed definitions of mixed state complexity and uncomplexity in <a href="https://arxiv.org/pdf/1807.05218.pdf"><b><i>Properties of the (Un)Complexity of Subsystems</i></b></a> (2018). He connected the work of Zhao and Agón et al., showing that degeneracy of the spectrum plays an important role both in complexity of preparation (it reduces spectral complexity) and Zhao's conjectured subregion dual (i.e. Schmidt degeneracy).<br />
<h3>
Conclusion</h3>
A fun paper! The area is young and rapidly evolving, so it will be interesting to see how the mixed state complexity story changes. But I think Zhao has a pretty compelling operational story about the meaning of <i>uncomplexity</i> in mixed states.</div>
</div>
