+++
title = "white2017unifying: Unifying Task Specification in Reinforcement Learning"
author = ["Matthew Schlegel"]
lastmod = 2022-11-08T14:23:59-07:00
slug = "white2017"
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
\newcommand{\complexs}{\mathbb{C}}
\newcommand{\field}{\mathbb{F}}
\newcommand{\numfield}{\mathbb{F}}
\newcommand{\expected}{\mathbb{E}}
\newcommand{\var}{\mathbb{V}}
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
\newcommand{\fvec}{\mathbf{f}}
\newcommand{\gvec}{\mathbf{g}}
\newcommand{\hvec}{\mathbf{h}}
\newcommand{\ivec}{\mathbf{i}}
\newcommand{\jvec}{\mathbf{j}}
\newcommand{\kvec}{\mathbf{k}}
\newcommand{\lvec}{\mathbf{l}}
\newcommand{\mvec}{\mathbf{m}}
\newcommand{\nvec}{\mathbf{n}}
\newcommand{\ovec}{\mathbf{o}}
\newcommand{\pvec}{\mathbf{p}}
\newcommand{\qvec}{\mathbf{q}}
\newcommand{\rvec}{\mathbf{r}}
\newcommand{\svec}{\mathbf{s}}
\newcommand{\tvec}{\mathbf{t}}
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
\newcommand{\Gmat}{\mathbf{G}}
\newcommand{\Hmat}{\mathbf{H}}
\newcommand{\Imat}{\mathbf{I}}
\newcommand{\Jmat}{\mathbf{J}}
\newcommand{\Kmat}{\mathbf{K}}
\newcommand{\Lmat}{\mathbf{L}}
\newcommand{\Mmat}{\mathbf{M}}
\newcommand{\Nmat}{\mathbf{N}}
\newcommand{\Omat}{\mathbf{O}}
\newcommand{\Pmat}{\mathbf{P}}
\newcommand{\Qmat}{\mathbf{Q}}
\newcommand{\Rmat}{\mathbf{R}}
\newcommand{\Smat}{\mathbf{S}}
\newcommand{\Tmat}{\mathbf{T}}
\newcommand{\Umat}{\mathbf{U}}
\newcommand{\Vmat}{\mathbf{V}}
\newcommand{\Wmat}{\mathbf{W}}
\newcommand{\Xmat}{\mathbf{X}}
\newcommand{\Ymat}{\mathbf{Y}}
\newcommand{\Zmat}{\mathbf{Z}}
\newcommand{\Sigmamat}{\boldsymbol{\Sigma}}
\newcommand{\identity}{\Imat}
\newcommand{\epsilonvec}{\boldsymbol{\epsilon}}
\newcommand{\thetavec}{\boldsymbol{\theta}}
\newcommand{\phivec}{\boldsymbol{\phi}}
\newcommand{\muvec}{\boldsymbol{\mu}}
\newcommand{\sigmavec}{\boldsymbol{\sigma}}
\newcommand{\jacobian}{\mathbf{J}}
\newcommand{\ind}{\perp\!\!\!\!\perp}
\newcommand{\bigoh}{\text{O}}
\\)

tags
: [Reinforcement Learning]({{< relref "reinforcement_learning.md" >}}), [Theory]({{< relref "theory.md" >}})

source
: [paper](https://dl.acm.org/citation.cfm?id=3306068)

authors
: White, M.

year
: 2017

The main contribution of this paper is the formalization of a unified task specification for reinforcement learning. Specifically, this paper unifies our concept of episodic and continuing tasks, and bridges our understanding of options and general value functions.

**Generalized problem formulation**

The environment an agent interacts with is formalized as a Markov decision process (MDP): \\((\states, actions, \mathcal{P})\\) where

-   \\(\states\\) is the set of states
-   \\(\actions\\) is the set of actions
-   \\(\mathcal{P}: \states \times \actions \times states \rightarrow [0,1]\\) is the transition probability function.

A **reinforcement learning task** is specified on top of the dynamics as \\((\Pi, r, \gamma, \mathbf{i})\\) where

-   \\(\Pi\\) is a set of policyes \\(\pi: \states \times \actions \rightarrow [0,1]\\)
-   the reward function \\(r: \states\times\actions\times\states \rightarrow \reals\\) specifies reward received from \\((s,a,s^\prime)\\)
-   \\(\gamma: \states \times \actions \times \states \rightarrow [0,1]\\) is a transition-based discount function
-   \\(\mathbf{i}: \states \rightarrow [0,\infty)\\) defines an interest function

For either control or prediction, we evaluate a value function which is the expected discounted return:

\\[ G\_t = \sum\_{i=0}^\infty \left( \prod\_{j=0}^{i-1} \gamma(s\_{t+j}, a\_{t+1}, s\_{t+1+j})\right) R\_{t+1+i} \\]

where \\(\prod\_{j=0}^{-1} \gamma(\cdot) = 1\\). This formulation subsumes both the episodic and continuous cases (when the discount is some constant). We can even define an option in terms of an RL task.

An option is typically defined as \\((\pi, \beta, \mathcal{I})\\) with _policy_ \\(\pi: \states \times \actions \rightarrow [0,1]\\), _termination function_ \\(\beta: \states \rightarrow [0,1]\\), and an _initiation set_ \\(\mathcal{I} \subset \states\\). We can redefine these in terms of an RL tasks as \\(\gamma(s,a,s^\prime) = 1 - \beta(s^\prime)\\) for all \\(s,a,s^\prime\\) specifies termination, and \\(\mathbf{i}(s) = 1\\) if \\(s\in\mathcal{I}\\) and \\(\mathbf{i}(s) = 0\\) otherwise.
