---
layout: post
mathjax: true
comments: true
title:  "Groups, spectra and particles"
date:   2015-10-06
---

<i>This post is aimed at students of </i>MAST20022 Group Theory and Linear Algebra<i>.
<br />
<h3>
Introduction</h3>
<br />
The two big topics of our course — advanced linear algebra and group theory — are unified in deep, elegant and surprising ways by quantum mechanics. In this first post, I'll give a brief and non-rigorous precis of quantum mechanics, focusing on the spectral theorem. In the next, I'll discuss how&nbsp;<i>symmetries</i>&nbsp;get represented in quantum systems, and finish by combining these ideas to get the basic building blocks of nature:&nbsp;particles.<br />
<h3>
Quantum mechanics</h3>

Like classical physics, the goal of quantum physics is to describe physical systems and understand how they evolve. In classical physics, the state of the system can generally be specified by a finite number of coordinates. For instance, a single particle moving around in $\mathbb{R}^3$ and subject to a force field $\mathbf{F}(\mathbf{x})$ can be described by a pair of $3$-vectors: position $\mathbf{x}(t)$ and momentum $\mathbf{p}(t)$. The evolution of the system obeys Newton's second law of motion:

$$
\mathbf{F}(\mathbf{x}) = \frac{d}{dt}\mathbf{p}(t).
$$

The vectors $\mathbf{x}(t)$ and $\mathbf{p}(t)$ are called <i>dynamical variables</i> since they change with time. In quantum mechanics, the description of the state and its evolution is governed by five rules:<br />
<ol>
<li>The state of a system at time $t$, aka the wavefunction $\Psi(t)$, is a unit vector in some&nbsp;<i>complex inner product space</i>&nbsp;$V$. There are other technical conditions on $V$ we will ignore for the time being.</li>
<li>Every physical property of the system corresponds to a Hermitian operator $\hat{A}: V \to V$. (To distinguish them from classical variables, these operators usually have hats.) Physical properties are also called <i>observables</i>, with typical examples being position $\hat{x}$, momentum $\hat{p}$, and energy $\hat{H}$.</li>
<li>The state of the system satisfies a differential equation (famously due to&nbsp;Schrödinger)\[i\hbar\frac{d}{dt}\Psi(t)&nbsp;=&nbsp;\hat{H}\Psi(t),\] where $\hbar$ is <i>the reduced&nbsp;Planck constant</i>. In SI units, $\hbar \sim 10^{-34} \text{ J s}$.</li>
<li>For an observable $\hat{A}$, the values you can obtain when measuring $\hat{A}$ are precisely the eigenvalues of $\hat{A}$.</li>
<li>If you measure $\hat{A}$ at time $t_0$, the system will <i>subsequently</i> be in a (normalised) $\lambda$-eigenstate $v_\lambda$ of $\hat{A}$ with probability \[\mathbb{P}(\Psi \to v_\lambda) = |\langle&nbsp;v_\lambda, \Psi(t_0)\rangle|^2.\]</li>
</ol>
<div>
I'll make a few comments about these rules, and leave further elaboration to a quantum mechanics course. First, recall that Hermitian operators have real eigenvalues. This means that we can only measure real values! This is physically sensible, and in fact, is the motivation for making observables Hermitian in the first place.<br />
<br />
Secondly, rule 3 and rule 5 tell totally different stories about how the system evolves. Rule 5, often called the "collapse of the wavefunction", rudely interrupts the Schrödinger evolution and resets the system to an eigenvector of the observable. This seems very strange, and very ugly, and it is. </div>
<h3>
Observables and the spectral theorem</h3>
<div>
Let's talk more about the spectrum of values we can measure for an observable $\hat{A}$. From rule 4, these are just the eigenvalues of $\hat{A}$. (By the way, this is where the name of the <i>spectral</i> theorem comes from.) To begin with, suppose $V$ is finite-dimensional. We can use the second version of the spectral theorem to deduce that there exist self-adjoint Hermitian operators $P_i$ and scalars $\lambda_i$ for $i=1, \ldots, k$, such that:<br />
<ol>
<li>$\lambda_i \neq&nbsp;\lambda_j$ if $i\neq j$;</li>
<li>$P_i^2 = P_i$;</li>
<li>$\sum_{i=1}^k P_i = 1_V$; and</li>
<li>$\sum_{i=1}^k \lambda_i P_i = 1$.</li>
</ol>
</div>
More concretely, the eigenvalues of $\hat{A}$ are the $\lambda_i$, and the operators $P_i$ project onto the $\lambda_i$-eigenspace. So we are guaranteed to have a nice set of measurable values! Suppose we measure $\lambda_i$, and in addition, the $\lambda_i$-eigenspace is $1$-dimensional, with a normalised eigenvector $v_i$. Then

$$
P_i \Psi = \langle v_{i}, \Psi \rangle v_{i} \quad \Longrightarrow \quad \mathbb{P}(\Psi \to v_{i}) = ||P_i \Psi||^2.
$$

What if the $\lambda_i$-eigenspace is $&gt;1$-dimensional? This is called <i>degeneracy</i>, and a bit more work is needed, which again I'll leave to a quantum mechanics course.<br />
<br />
Now, in reality, $V$ is never finite-dimensional. But the extra condition I mentioned in rule 1 is that $V$ must be very well-behaved complex inner product space called a <i>Hilbert space</i>. You will learn much more about these in third year. Hilbert spaces have the marvellous property that, even in the infinite-dimensional case, a version of the spectral theorem applies. In fact, this is the <i>motivation</i> for the technical condition on $V$ in formulating quantum mechanics.<br />
<br />
So, I'll close the section by stating the general spectral theorem for Hilbert spaces. Suppose $V$ is a Hilbert space, and $\hat{A}: V \to V$ is a Hermitian operator. Then for each $\lambda \in \mathbb{R}$, there is an operator $E(\lambda)$ satisfying:<br />
<ol>
<li>$E(\lambda)E(\lambda') = E(\min\{\lambda,&nbsp;\lambda'\})$;</li>
<li>$\lim_{\lambda\to-\infty} E(\lambda) = 0$ and $\lim_{\lambda\to \infty} E(\lambda) = 1$;</li>
<li>$\int_{-\infty}^\infty dE(\lambda) = 1_V$; and</li>
<li>$\int_{-\infty}^\infty \lambda\, dE(\lambda) = \hat{A}$.</li>
</ol>
<div>
In the finite-dimensional case, let's check this reduces to the familiar spectral theorem. Set<br />
\[<br />
E(\lambda) \equiv \sum_{\lambda_i &lt; \lambda} P_i<br />
\]and interpret the integrals in properties 3 and 4 using<br />
\[<br />
\int_{-\infty}^\infty f(\lambda)\, dE(\lambda) \equiv \sum_{i}f(\lambda_i) P_i.<br />
\]I'll leave it as an exercise to check that this has properties 1-4. In the infinite-dimensional case, we would make the sum an integral, so heuristically we have something like<br />
\[<br />
E(\lambda) = \int_{-\infty}^\lambda P(\lambda') \, d\lambda'.<br />
\]I won't tell you how to integrate an infinite-dimensional operator (this requires <a href="https://en.wikipedia.org/wiki/Functional_analysis">functional analysis</a>), but hopefully it doesn't seem too far removed from the finite-dimensional case. The moral is that even in infinite dimensions, we can "diagonalise" a Hermitian operator (write it as a sum of projection operators) and interpret the projection operators in quantum mechanical terms.<br />
<h3>
Quantising classical systems</h3>
So far I haven't discussed the link between the classical and the quantum description of a system. It turns out you need such a link in order to figure out the operators $\hat{A}$ corresponding to observables; we can't deduce them from the rules alone. The process of going from a classical to a quantum description of the same system is called <i>quantisation</i>. Again, I'll leave most of the details to a quantum mechanics course. However, since the evolution of the system is governed by the energy operator $\hat{H}$ (also called the <i>Hamiltonian</i>) let's see how we calculate it, in principle.<br />
<br />
In the classical setup, there is an energy operator $H$ which takes the state of the system and spits out its energy (a real number). For the single particle system described above, it's just the sum of kinetic energy (associated with motion) and potential energy (to do with moving around in the force field $\mathbf{F}(\mathbf{x})$). If the force is conservative, i.e. satisfies<br />
\[<br />
\mathbf{F}(\mathbf{x}) = - \nabla V(\mathbf{x})<br />
\]for some scalar potential $V(\mathbf{x})$, and the particle has mass $m$, then the energy operator is<br />
\[<br />
H(\mathbf{x}, \mathbf{p}) = \frac{|\mathbf{p}|^2}{2m} + V(\mathbf{x}).<br />
\]The energy operator in the <i>quantum </i>description is related very simply to this: it is just<br />
\[<br />
\hat{H} = \frac{\hat{\mathbf{p}}^2}{2m} + V(\hat{\mathbf{x}}),<br />
\]where $\hat{\mathbf{x}}$ and $\hat{\mathbf{p}}$ are the operators associated to the position and momentum observables. In other words, just replace dynamical variables with their operators! So the usual form of Schrödinger's equation,<br />
\[<br />
i\hbar \frac{d}{dt}\Psi = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi<br />
\]just comes from replacing $\mathbf{p}$ with its quantum counterpart $\hat{\mathbf{p}} = -i\hbar \nabla$. (It's not at all obvious that momentum should become a differential operator, but it turns out to be right. Consult your local quantum mechanics course for details on how to find $\hat{\mathbf{x}}$ and $\hat{\mathbf{p}}$.)<br />
<h3>
Classical symmetries</h3>
Finally, it's time for group theory to make an entrance. Recall that we can describe a classical particle in 3D using position $\mathbf{x}$ and momentum $\mathbf{p}$. We can smush them together into a vector $v \equiv (\mathbf{x}, \mathbf{p}) \in&nbsp;\mathbb{R}^3\times\mathbb{R}^3$. The combined position-momentum space $M \equiv \mathbb{R}^3\times\mathbb{R}^3$ is called <i>phase space</i>. A symmetry of the system will be an invertible transformation of phase space $T: M \to M$ that leaves it "invariant", that is, unchanged with respect to an equivalence relation of our choice. We choose "invariant" to mean "the energy of the system isn't changed by $T$, whatever state it's in".<br />

Formally, for all $v \in M$,<br />
\[<br />
H(Tv) = H(v).<br />
\]The collection of all the symmetries forms a group $\mathcal{G}$, as you can check. [<i>Technical comment</i>: The evolution of the system can be related to the derivatives of the energy function by <a href="https://en.wikipedia.org/wiki/Hamiltonian_mechanics">Hamilton's equations</a>. This guarantees that the physics will be the same under a symmetry transformation, given the way we've defined it.]<br />
<h3>
Some examples</h3>

Nature seems to favour groups which are simple enough for us to figure out, but mathematically non-trivial. A few physically important examples:<br />
<ul>
<li>rotations of $\mathbb{R}^n$, also known as <i>the orthogonal group</i>&nbsp;$\mathrm{O}(n)$, which arise in systems with rotational invariance;</li>
<li>rotations of $\mathbb{C}^n$, also known as&nbsp;<i>the unitary group</i>&nbsp;$\mathrm{U}(n)$, which often come from&nbsp;<i>conservation of probability</i> in quantum mechanics;</li>
<li>translations, spatial rotations, and Newtonian "boosts" of&nbsp;$\mathbb{R}^4$, also called&nbsp;<i>the Galilean group</i>, which connect (Newtonian) physics in different inertial frames;</li>
<li>rotations and relativistic "boosts" of&nbsp;$\mathbb{R}^4$, also called the <i>Lorentz group</i>&nbsp;$\mathrm{SO}(1,3)$, which connect inertial frames in relativistic mechanics;</li>
<li>the&nbsp;<i>Poincaré&nbsp;group</i>, which just adds translations to the&nbsp;Lorentz group<i>.</i></li>
</ul>
Note that "translations and rotations" includes pure translations, pure rotations, and combinations of the two; the same remark applies to boosts.<br />
<h3>
Quantum symmetries and representations</h3>
Now, suppose we want to quantise a classical system with symmetry group $G$. Symmetries are not <i>always</i> preserved when we quantise, but if they are, what should they look like? Well, before $G$ acted on the phase space $M$. Now it should act on the Hilbert space of the <i>quantum</i> theory, $G \hookrightarrow V$. Since $V$ is a&nbsp;<i>vector space</i>, and we want symmetries to preserve the vector space structure, they&nbsp;should act as linear transformations.<br />
<br />
Thus, each group element $T \in G$ should be assigned a matrix, $\rho(T) \in \mathrm{GL}(V)$, where $\mathrm{GL}(V)$ denotes the invertible linear operators on $V$. To ensure that these matrices define a group action, we require the matrix assignment function $\rho: G \to \mathrm{GL}(V)$ to be a <i>homomorphism</i>:<br />
\[<br />
\rho(T\cdot S) = \rho(T) \cdot\rho(S).<br />
\]Since "matrix assignment homomorphism" is a bit of a mouthful, $\rho$ is instead called a <i>representation</i> of $G$<i>.</i> In fact, we've already seen representations in the guise of <i>matrix groups</i>, e.g., the general linear group $\mathrm{GL}_n(\mathbb{F})$, the orthogonal group $\mathrm{O}(n)$, and the unitary group $\mathrm{U}(n)$. Finally, instead of leaving the energy invariant, the closest condition in quantum mechanics is that $\rho(G)$ not interfere with the measurement of energy. More formally, each $\rho(g)$ should <i>commute</i> with the energy operator $\hat{H}$:

$$
[\hat{H}, \rho(g)] = \hat{H} \rho(g) - \rho(g)\hat{H} = 0.
$$

Note that a group $G$ may act on $V$ without commting with $\hat{H}$, but it is not then a symmetry of the system.<br />
<h3>
Particles</h3>
<div>
If the matrices $\rho(G) \subset \mathrm{GL}(V)$ have a common invariant subspace, the representation $\rho$ is&nbsp;<i>reducible</i>. Just to remind you, an invariant subspace of a linear operator $L: V \to V$ is a nontrivial, proper subspace $W \subset V$ such that $L(W) \subset W$. A representation which is not reducible is <i>irreducible</i>. We can think of a reducible representation as a set of block diagonal matrices with compatible block structures. In other words, we can factor $\rho(g)$ into block diagonal matrices $A_1(g), A_2(g), \ldots, A_n(g)$ where $A_i$ is a representation on an $m_i$-dimensional subspace of $V$:<br />
\[<br />
\rho(g) = \left[<br />
\begin{array}{cccc}<br />
A_1(g)&amp;&amp;&amp;\\<br />
&amp;A_2(g)&amp;&amp;\\<br />
&amp;&amp;\ddots&amp;\\<br />
&amp;&amp;&amp;A_n(g)<br />
\end{array}<br />
\right].<br />
\]We can keep breaking a reducible representation down into blocks until we can't go any further. In many cases (for instance, a finite group $G$), this process will lead to a <i>unique</i> decomposition into irreducible blocks.</div>
<div>
<br />
What is the physical significance of these blocks? Well, in the classical case, orbits of the symmetry group $G$ are things which look the same. I could be in one state, or any of the other states connected by symmetries, and the energy operator can't tell. Since they are physically indistinguishable, they are probably related. When we quantise, the irreducible subspaces are the equivalent of these orbits of indistinguishable states. They consist of vectors which are mixed together by the symmetries (acting as linear operators on $V$), and which cannot be split into smaller sets of vectors which mix amongst themselves. Generally, vectors correspond to <i>degrees of freedom</i> of our system. But a lump of inextricably linked degrees of freedom has a natural interpretation: a particle! So, a particle is irreducible representation $A$ of $G$ on a $k$-dimensional subspace<br />
\[<br />
A(g) = \overset{\text{mixed together under $G$}}{\overbrace{\left[<br />
\begin{array}{ccc}<br />
a_{11}(g)&amp;\cdots&amp;a_{1k}(g)\\<br />
\vdots&amp;\ddots&amp;\vdots\\<br />
a_{k1}(g)&amp;\cdots&amp;a_{kk}(g)<br />
\end{array}<br />
\right]}}.<br />
\]But what group $G$ should we use? When we say that an electron is a particle, we mean it is a fundamental degree of freedom of the universe. The fundamental symmetry group of space (provided we can ignore gravity) is the <i>Poincaré group</i> of special relativity. Thus, a fundamental particle is usually defined as an irreducible representation of the Poincaré group.
<br />
<h3>
Summary</h3>

We started by defining a classical symmetry as a transformation of phase space that always left the energy invariant. We then argued that in quantising, symmetries should act as linear transformations on the Hilbert space of the quantum theory with commute with the energy operator. Finally, we saw that irreducible subspaces (under the representation) are just directions in Hilbert space that inextricably mix under symmetries. We interpret them as the degrees of freedom of a <i>particle</i>. For physical reasons, we are often thinking specifically of the Poincaré group of special relativity. So, that completes our GTALA-motivated crash course in quantum mechanics and particle physics. Hope you learnt something!<br />
<br /></div>
<div>
<b>References</b><br />
<ul>
<li><i>Lie Algebras in Particle Physics</i> (1982), Howard Georgi.</li>
<li><i>Mathematics of classical and quantum physics</i> (1969), Byron and Fuller.</li>
<li><i>The Quantum Theory of Fields: Volume 1</i>&nbsp;(2005), Steven Weinberg.</li>
</ul>
</div>
</div>
