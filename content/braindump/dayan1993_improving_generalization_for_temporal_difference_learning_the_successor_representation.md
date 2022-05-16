+++
title = "dayan1993: Improving Generalization for Temporal Difference Learning: The Successor Representation"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:16-06:00
slug = "dayan1993"
draft = false
notetype = "paper"
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

source
:


authors
: Dayan, P.

year
: 1993

This paper discusses temporal-dependent representations for [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}}). This is for the discrete state and action case.

The idea is to construct a matrix \\(\Xmat\\) where each row corresponds to a vector of the effective likelihoods of transitioning to a state (column) starting in a state (row). With \\(\eye\\) as the identity and \\(\Qmat\\) as the markov transition matrix

\\[
\Xmat\_{ij} = [\eye]\_{ij} + [\Qmat]\_{ij} + [\Qmat^2]\_{ij} + \ldots = [(\eye - \Qmat)^\inv]\_{ij}
\\]

This representation can be learned online through a TD prediction algorithm. Finally, when learning the vector of value functions we can easily see the optimal weights for the true value functions

\\[\vvec = \Xmat \wvec^\*\\]

where

\\[\wvec^{\*}\_i = \sum\_{k \in T} s\_{ik} \bar{r}\_k\\]

where \\(T\\) is the set of absorbing states, \\(s\_{ik}\\) is the probability of transitioning from state \\(i\\) to state \\(k\\), and \\(\bar{r}\_k\\) is the expected reward at the absorbing state \\(k\\).

They then go through and show this working well on a navigation tasks as compared to older representational schemes.


## Quotes {#quotes}

> As briefly reviewed in the next section, TD methods apply to  learning _framework_, which specifies the goal for learning and precisely how the system fails to attain this goal in particular circumstances.

<!--quoteend-->

> ... neighborliness is defined in terms of temporal succession. If the transition matrix of the chain is initially unknown, this representation will have to be learned directly through experience.


## References {#references}


</Users/Matt/GD/bib/full_library.bib>
