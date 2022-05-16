+++
title = "wang2017: Learning to reinforcement learn"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:41-06:00
slug = "wang2017"
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
: [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}}), [Meta-Learning]({{<relref "meta_learning.md#" >}})

source
: <https://arxiv.org/abs/1611.05763>

authors
: Wang, J. X., Kurth-Nelson, Zeb, Tirumala, D., Soyer, H., Leibo, J. Z., Munos, R., Blundell, C., …

year
: 2017

This paper introduces a new learning paradigm coined _deep meta-reinforcement learning_, where they combine a recurrent architecture and a meta-reinforcement learning procedure to learn how to interact with various tasks pulled from a distribution of tasks.

In its simplest form, the recurrent network receives the observations \\(\xvec\_t\\) at the current time step (or an encoding of the observation), the reward \\(\reward\_{t-1}\\) and action \\(\action\_{t-1}\\) of the previous time step. For some of the experiments (the bandit experiments) the time step is used as input as well, which is an odd choice. The reward information is then fed to a separate RL system which is used to tune the parameters of the recurrent network.

The goal of this architecture is to create agents which can learn and explore a new MDP/bandit problem pulled from the same distribution used for training. This means developing a policy contingent on history which explores and then exploits in new MDPs.

Their proof of concept seems compelling, but there are some missing bits on how the architecture is actually working that I need to dig into a little bit.


## References {#references}


</Users/Matt/GD/bib/full_library.bib>
