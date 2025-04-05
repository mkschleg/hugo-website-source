+++
title = "kostas2019asynchronous: Asynchronous Coagent Networks: Stochastic Networks for Reinforcement Learning without Backpropagation or a Clock"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:28:08-07:00
slug = "kostas2019asynchronous"
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
: [Reinforcement Learning]({{< relref "reinforcement_learning.md" >}}), [Representation]({{< relref "representation.md" >}})

source
: [paper](http://all.cs.umass.edu/pubs/2019/Kostas%20et%20al%20-%20Asynchronous%20Coagent%20Networks.pdf)

authors
: Kostas, J., Nota, C., &amp; Thomas, P. S.

year
: 2019

This paper continues the line of research into coagent networks, primarily looking at how these networks can be trained in an asynchronous way. Policy gradient coagent networks (PGCN) already have removed back-propagation as a requirement, meaning the updates require only information local to a particular coagent (or neuron in an ANN).

Some literature connected to this work is:

-   _stochastic computation graphs_ - proposed to describe networks with a mixture of stochastic and deterministic nodes, with supervised, unsupervised, and RL applications.
-   _Stochastic neural networks_ - A type of ANN which builds in random variations to the network, either through a stochastic transfer function, or stochastic weights.
-   Multi-agent RL - (<a href="#citeproc_bib_item_1">Liu et al. 2014</a>): showed that multi-agent systems sometimes learn more quickly when agents are given individualized rewards.


## Background {#background}

Consider the MDP, \\((M=(\states, \actions, \rewards, \transition, R, d\_0, \gamma))\\). where the \\(\states\\) is all possible states, \\(\actions\\) set of all possible actions, and \\(\rewards\\) the set of all possible rewards (All finite sets). \\(\transition: \states \by \actions \by \states \rightarrow [0,1], R: \states \by \actions \by \states \rightarrow [0,1], d\_0(s) \triangleq Pr(S\_0=s)\\) are the transition function, reward distribution, and initial state distribution respectively.

The paper defines a parameterized policy as \\(\pi: \states \by \actions \by \mathbb{R}^n \rightarrow [0,1]\\)., such that for all \\(\theta \in \reals^n\\), \\(\pi(\cdot, \cdot, \theta)\\) is a policy. Assume \\(\partialderiv{\pi(s,a,\theta)}{ \theta}\\) exists for all \\(s\in\states, a\in\actions\\).

An agents goal is to maximize the objective

\\[J(\pi) = \mathbb{E}[\sum\_{t=0}^\infty \gamma^t R\_t|A\_t \sim \pi(\cdot, \cdot, \theta)]\\]


### How coagent networks function {#how-coagent-networks-function}

We can consider an acyclic network of nodes, where each node is an independently acting coagent

The ith coagent has parameters \\(\theta\_i \in \reals^{n\_i}\\), where the remaining parameters of the network are \\(\bar{\theta}\_i \in \reals{n - n\_i}\\).

We model the output of the previous coagents in the network through a parameterized distribution \\(U\_t^\text{pre} \sim \pi\_i^{\text{pre}}(S\_t, \cdot, \bar{theta}\_i)\\). The output of the previous coagents is a random variable \\(U\_t^\text{pre}\\), which takes some discrete values in a set \\(\mathcal{U}^\text{pre}\\).

The \\(i^\text{th}\\) coagent takes \\(S\_t\\) and \\(U\_t^\text{pre}\\) as input and produces \\(U\_t^i\\), the conditional distribution of \\(U^i\_t\\) is given by \\(\pi(X\_t^i, \cdot, \theta\_i)\\) where \\(X\_t^i = (S\_t, U^\text{pre}\_t)\\). \\(A\_t\\) is sampled according to a distribution \\(\pi\_i^\text{post}(X\_t, U\_t^i, \cdot, \bar{\theta\_i})\\).

Each agents environment is modeled as a CoMDP (_conjugate Markov decision process_).


## The Coagent Policy Gradient Theorem {#the-coagent-policy-gradient-theorem}

If we were to simpley implement an unbiased policy gradient algorithm (say REINFORCE), the expected update or the _local policy gradient_ \\(\Delta\_i\\) for the \\(i^\text{th}\\) coagent would be:

\begin{equation}
\Delta\_i(\theta\_i) \triangleq \expected\left[\sum\_{t=0}^\infty \gamma^t G\_t \partialderiv{\ln(\pi\_i(X\_t, U\_t, \theta\_i))}{\theta\_i} \vert \theta\right] \label{eqn:kostas2019:local-policy-gradient}
\end{equation}

What would happen if all coagents updated according to the local policy gradient updates?

**Coagent policy gradient theorm (CPGT)**: If \\(\theta\\) is fixed and all coagents update their parameters following unbiased estimates of <eqn:kostas2019:local-policy-gradient> then the entire network will follow an unbiased estimator of \\(\nabla J(\theta)\\), or the _global policy gradient_.


### Conjugate Markov Decision Process (CoMDP) {#conjugate-markov-decision-process--comdp}

The CoMDP (or environment) of the \\(i^\text{th}\\), \\(M^i \triangleq (\mathcal{X}^i, \mathcal{U}^i, \rewards^i, \transition^i, R^i, d\_0^i, \gamma\_i)\\). Each component follows the normal MDP scheme laid out above. Here we will denote all random variables of the CoMDP with a tilde to clarify the distinction, for example \\(\tilde{X}^i\_t\\) is the state of coagent \\(i\\) at time \\(t\\). The reward set and discount are the same as the MDP. We also define the transition and reward dynamics as

\\[\transition^i(x, u, x', \bar{\theta}\_i) \triangleq \pi\_i^\text{pre}(x'.s, x'.u\_\text{pre}) \sum\_{a \in \actions} \transition(x.s, a, x'.s) \pi\_i^\text{post}(x, u, a)\\]

\\[R^i(x, u, x', r, \bar{\theta}\_i) \triangleq
    \sum\_{a\in\actions} R(x.s, a, x'.s, r) \frac{\transition(x.s, a, x'.s) \pi\_i^\text{post}(x, u, a)}{\sum\_{\hat{a} \in \actions}\transition(x.s, \hat{a}, x'.s) \pi\_i^\text{post}(x,u,\hat{a})}\\]

They assume that given the same parameters \\(\theta\_i\\), the \\(i^\text{th}\\) coagent has the same policy in both the original MDP and the \\(i^\text{th}\\) CoMDP.

The properties of the CoMDP are relatively straightforward from basic probability and algebraic manipulations. Something to keep in mind is the notion that the objective functions are equivalent (i.e. \\(J(\theta) = J\_i(\theta\_i)\\)). How this plays out in the network makes some amount of sense, as each coagent needs to act in such a way the whole agent can maximize the return.

I wonder if:

-   Does the network ever collapse where each agent is selecting the same action? This could be a problem as it will force the network into a local optima, with no way out. If the policies are stochastic this should be avoidable.
-   If the agents are dependent on the prior agents output, how can this be asynchronous? I'm still a bit confused on how the forward pass is being performed.
-   Can this go beyond each node being an agent? How else can we construct asynchronous networks?


## Asynchronous Recurrent Networks {#asynchronous-recurrent-networks}

They allow for cyclic and asynchronous firings in straightforward ways. The cyclic structure is placed in \\(\mathcal{X}\_t\\) which can contain prior firings of the coagent. The asynchronous firings are done through discritizing time into _atomic time steps_ or really time steps which can be arbitrarily fine. Each coagent then has a probability of firing and any given _atomic time step_.

They provide theoretical evidence these extensions are valid, which will not be discussed in detail here.


## Case Study: Option Critic {#case-study-option-critic}

They show the CGPT can be applied to an option critic framework. This allows detailed analysis of several multi-component algorithms to be analyzed using a more general policy gradient algorithm.

The details of this are skipped here.


## Empirical Support of CPGT {#empirical-support-of-cpgt}

They provide some empirical evidence on a toy problem that the gradient estimates are similar to the back prop example. They show the directions are relatively similar as the number of estimate episodes increases.


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Liu, Bingyao, Satinder Singh, Richard L. Lewis, and Shiyin Qin. 2014. “Optimal Rewards for Cooperative Agents.” <i>IEEE Transactions on Autonomous Mental Development</i> 6 (4): 286–97. doi:<a href="https://doi.org/10.1109/TAMD.2014.2362682">10.1109/TAMD.2014.2362682</a>.</div>
</div>
