+++
title = "Mountain Car"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:29-06:00
slug = "mountain_car"
draft = false
notetype = "note"
+++

\\( \newcommand{\states}{\mathcal{S}}
\newcommand{\actions}{\mathcal{A}}
\newcommand{\observations}{\mathcal{O}}
\newcommand{\rewards}{\mathcal{R}}
\newcommand{\traces}{\mathbf{e}}
\newcommand{\transition}{P}
\newcommand{\reals}{\mathbb{R}}
\newcommand{\naturals}{\mathbb{N}}
\newcommand{\expected}{\mathbb{E}}
\newcommand{\by}{\times}
\newcommand{\partialderiv}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\defineq}{\stackrel{{\tiny\mbox{def}}}{=}}
\newcommand{\defeq}{\stackrel{{\tiny\mbox{def}}}{=}}
\newcommand{\eye}{\Imat}
\newcommand{\hadamard}{\odot}
\newcommand{\trans}{\top}
\newcommand{\inv}{{-1}}
\newcommand{\argmax}{\operatorname{argmax}}
\newcommand{\Prob}{\mathbb{P}}
\newcommand{\avec}{\mathbf{a}}
\newcommand{\bvec}{\mathbf{b}}
\newcommand{\cvec}{\mathbf{c}}
\newcommand{\dvec}{\mathbf{d}}
\newcommand{\evec}{\mathbf{e}}
\newcommand{\gvec}{\mathbf{g}}
\newcommand{\hvec}{\mathbf{h}}
\newcommand{\lvec}{\mathbf{l}}
\newcommand{\mvec}{\mathbf{m}}
\newcommand{\nvec}{\mathbf{n}}
\newcommand{\pvec}{\mathbf{p}}
\newcommand{\qvec}{\mathbf{q}}
\newcommand{\rvec}{\mathbf{r}}
\newcommand{\svec}{\mathbf{s}}
\newcommand{\uvec}{\mathbf{u}}
\newcommand{\vvec}{\mathbf{v}}
\newcommand{\wvec}{\mathbf{w}}
\newcommand{\xvec}{\mathbf{x}}
\newcommand{\yvec}{\mathbf{y}}
\newcommand{\zvec}{\mathbf{z}}
\newcommand{\Amat}{\mathbf{A}}
\newcommand{\Bmat}{\mathbf{B}}
\newcommand{\Cmat}{\mathbf{C}}
\newcommand{\Dmat}{\mathbf{D}}
\newcommand{\Emat}{\mathbf{E}}
\newcommand{\Fmat}{\mathbf{F}}
\newcommand{\Imat}{\mathbf{I}}
\newcommand{\Pmat}{\mathbf{P}}
\newcommand{\Umat}{\mathbf{U}}
\newcommand{\Vmat}{\mathbf{V}}
\newcommand{\Wmat}{\mathbf{W}}
\newcommand{\Xmat}{\mathbf{X}}
\newcommand{\Qmat}{\mathbf{Q}}
\newcommand{\thetavec}{\boldsymbol{\theta}}
\newcommand{\phivec}{\boldsymbol{\phi}}
\newcommand{\muvec}{\boldsymbol{\mu}}
\newcommand{\sigmavec}{\boldsymbol{\sigma}}
\newcommand{\jacobian}{\mathbf{J}}
\\)

A simple environment first introduced in <sup id="21888f2387daeed261c740a2efe1ede8"><a href="#sutton1996" title="Sutton, Generalization in {{Reinforcement Learning}}: {{Successful Examples Using Sparse Coarse Coding}}, in in: {Advances in {{Neural Information Processing Systems}} 8}, edited by Touretzky, Mozer \&amp; Hasselmo, {MIT Press} (1996)">sutton1996</a></sup>. It is a representation of a car stuck inbetween two hills and needs to get over the hill in front of it. The dynamics of the system are encapsulated as a differential equation:

\\[\dot{x} = \dot{x} + 0.001 a - 0.0025 cos(3x)\\]

with conditions that \\(x \in [-0.5, 1.2]\\) and \\(\dot{x} \in [-0.07, 0.07]\\). This environment was a challenge environment in the past, but has become a standard test environment to use to debug algorithms (if it doesn't work on mountain car, something is wrong).


## References {#references}


# Bibliography
<a id="sutton1996"></a>[sutton1996] Sutton, Generalization in Reinforcement Learning: Successful Examples Using Sparse Coarse Coding, in in: Advances in Neural Information Processing Systems 8, edited by Touretzky, Mozer & Hasselmo, MIT Press (1996) [↩](#21888f2387daeed261c740a2efe1ede8)
