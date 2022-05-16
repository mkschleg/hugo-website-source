+++
title = "badia2020: Agent57: Outperforming the Atari Human Benchmark"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:10-06:00
slug = "badia2020"
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

tags
: [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}})

source
: <https://deepmind.com/blog/article/Agent57-Outperforming-the-human-Atari-benchmark>

authors
: Badia, Adri\\\`a Puigdom\\\`enech, Piot, B., Kapturowski, S., Sprechmann, P., Vitvitskyi, A., Guo, D., & Blundell, C.

year
: 2020

This paper proposes a new agent which extends "Never Give Up" (NGU) <sup id="384c8f08fa32faba0f6404c133e4bba6"><a href="#badia2019" title="Badia, Sprechmann, Vitvitskyi, Guo, Piot, Kapturowski, Tieleman, Arjovsky, Pritzel, Bolt \&amp; Blundell, Never {{Give Up}}: {{Learning Directed Exploration Strategies}}, in in: {International {{Conference}} on {{Learning Representations}}}, edited by (2019)">badia2019</a></sup> in several ways:

1.  They separate the learning of the intrinsic and extrinsic rewards into two separate networks:
    \\[
       Q(x, a, j; \theta) = Q(x, a, j; \theta^e) + Q(x, a, j; \theta^i)
       \\]
    where \\(\theta^e, \theta\_i \in \reals^N\\) are the parameterization of the extrinsic and intrinsic value functions respectively.

2.  The addition of a meta-controller which adaptively selects which policies (learned in the same way as NGU) to prioritize throughout training. NGU uses its explore exploit policies with equal consideration, but parameterizing and learning a strategy for selecting amongst these policies allows the agent to adaptively control the explore/exploit trade-off.

They then show their Agent at or above human level performance for all games, and advocate for new analysis strategies when comparing agents in Atari.


## Background {#background}

They have some nice background bits summing up some important hurdles for RL agents in Atari. They categorize the important issues into two categories.


### Long-term credit assignment {#long-term-credit-assignment}

There have been two types of long-term credit assignment

1.  Ensuring that gradients correctly assign credit.
2.  Using values or targets to ensure correct credit assignment.


### Exploration {#exploration}

Exploration strategies have several approaches.

1.  Randomized value functions
2.  Unsupervised policy learning
3.  Intrinsic motivation/reward functions.


## References {#references}


# Bibliography
<a id="badia2019"></a>[badia2019] Badia, Sprechmann, Vitvitskyi, Guo, Piot, Kapturowski, Tieleman, Arjovsky, Pritzel, Bolt & Blundell, Never Give Up: Learning Directed Exploration Strategies, in in: International Conference on Learning Representations, edited by (2019) [↩](#384c8f08fa32faba0f6404c133e4bba6)
