+++
title = "Markov Decisions Process"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:27-06:00
slug = "markov_decisions_process"
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

A Markov decision process (MDP), is a discrete-time [Stochastic Processes]({{<relref "stochastic_processes.md#" >}}), and are an extension of Markov chains for decision making theory.

An MDP is made up of

-   A set of states \\(S\\)
-   A set of actions \\(A\\)
-   A transition kernel \\(P\_a(s, s\prime) = Pr[s\_{t+1} = s\prime | s\_t = s, a\_t = a]\\)
-   And the immediate reward function \\(R\_a(s, s\prime)\\)

It is used in [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}}) as the core data generation process.


## Markov Chain {#markov-chain}

See [Probability course](https://www.probabilitycourse.com/chapter11/11%5F2%5F1%5Fintroduction.php) for more info.


## Properties {#properties}


### Aperiodic {#aperiodic}

The period of a state is the largest integer \\(d\\) such that \\(P(s\_i, s\_i)^n = 0\\) for every n not divisible by \\(d\\). The period of i is shown as \\(d(s\_i)\\). If \\(P(s\_i, s\_i)^n = 0\\) for all \\(d\\) then \\(d(s\_i) = \infty\\).

for a state \\(s\_i\\)

-   Periodic: if \\(d(s\_i) > 1\\)
-   Aperiodic: if \\(d(s\_i) = 1\\).

A [Markov Chain](#markov-chain) is said to be aperiodic if all its states are aperiodic.


### Irreducible {#irreducible}

An irreducible [Markov Chain](#markov-chain) or [Markov Decisions Process]({{<relref "markov_decisions_process.md#" >}}) is one in which the


### Positive Recurrent {#positive-recurrent}


### Ergodic {#ergodic}

An MDP is said to be ergodic if all its states are ergodic. A state \\(s\_i\\) is said to be ergodic if it is aperiodic and positive recurrent. In other words
