---
Layout: post
mathjax: true
comments: true
title:  "Zeta regularisation black magic"
categories: [Mathematics, Physics]
date:  2019-08-03
---

**August 4, 2019.** *A quick, technical post on zeta function regularisation.*

Define the *Hurwitz function* by

$$
\zeta(s, a) = \sum_{k \geq 0}\frac{1}{(k+a)^s}, \quad a > 0, \quad |\Re(s)| > 1.
$$
	
We can analytically continue so that this is defined at $s = 0$, and from the [DLMF](https://dlmf.nist.gov/25.11) (or otherwise), it obeys

$$
\zeta(0, a)= \frac{1}{2} - a, \quad \zeta'(0, a) = \ln
\left(\frac{\Gamma(a)}{\sqrt{2\pi}}\right).\tagl{1}
$$
	
Consider an operator $\mathcal{X}_{\xi,a}$ with spectrum $\lambda_k = \xi(k+a)$, $k \in \mathbb{Z}_{\geq 0}$.
We can define the associated \emph{spectral zeta function}

$$
  \begin{align}
    \zeta_\mathcal{X}(s) & = \sum_{k \geq 0} \lambda_k^{-s}\tag{2}\\
   & = \sum_{k \geq 0}\frac{1}{\xi^s(k+s)^s} =
      \xi^{-s}\zeta(s, a). \tag{3}
  \end{align}
$$
  
We can differentiate (2), (3) with respect to $s$, and equate them
to get

$$
  \begin{align}
    \zeta'_\mathcal{X}(s) & = -\sum_{k \geq 0}
                            \lambda_k^{-s}\log\lambda_k \tag{4}\\ 
   & = \xi^{-s}\zeta'(s,a) - \xi^{-s}\log \xi \cdot \zeta(s,
     a). \tag{5}
  \end{align}
$$
  
From (4) and the elementary identity $\det A = e^{\mathrm{Tr} \log A}$, we also have

$$
\begin{equation}
    \zeta'_\mathcal{X}(0) = -\sum_{k \geq 0} \log \lambda_k = -\log
    \det \mathcal{X}. \tag{6}
\end{equation}
$$
	
Setting $s = 0$ in (5), using (1), and equating with (6), we find

$$
\begin{align}
    \det \mathcal{X}_{\xi,a} & = \prod_{k=a}  \xi (k+a) \notag \\& = \exp \left[\zeta'(0, a) -
                                     \log \xi
                                \cdot \zeta(0,a)\right] \notag \\
  & = \exp \left[-\ln \left(\frac{\Gamma(a)}{\sqrt{2\pi}}\right) +\log
    \xi\left(\frac{1}{2} - a\right) \right] \notag \\
  & = \frac{\sqrt{2\pi}}{\Gamma(a) }\xi^{1/2-a}. \tag{7}
  \end{align}
$$
  
We can now use (\ref{final}) to regularise the constants $\mathcal{N}$ in part (b) and $\mathcal{M}$ in part (d):

$$
\begin{align}
    \mathcal{N} & = \big[\det \mathcal{X}_{2\pi/\beta, 1}\big]^4 =
    \left[\sqrt{2\pi}\cdot\sqrt{\beta/2\pi}\right]^4 = \beta^2 \label{N}\\
\mathcal{M} & = \big[\det \mathcal{X}_{2\pi/\beta, 1/2}\big]^2 =
              \left(\frac{\sqrt{2\pi}}{\sqrt{\pi}}\right)^2 = 2.\label{M}
  \end{align}
$$
