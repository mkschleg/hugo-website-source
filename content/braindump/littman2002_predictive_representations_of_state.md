+++
title = "littman2002predictive: Predictive Representations of State"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:28:18-07:00
slug = "littman2002predictive"
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
: [PSR]({{< relref "psr.md" >}})

source
: [link](https://www.google.com/search?client=safari&rls=en&q=predictive+representation+of+state&ie=UTF-8&oe=UTF-8)

authors
: Littman, M. L., &amp; Sutton, R. S.

year
: 2002

This paper introduces a new mechanism for learning state in a partially observable MDP. The main mechanism is related to generative approaches to building state (i.e. POMDPs) in that it recursively updates it's state, but also incorporates the benefits of history based approaches in that the states are built from the observed data stream.

Consider a dynamical system with the underlying structure of an MDP:

-   actions from a discrete set \\(a\_i \in \actions\\)
-   observations from a discrete set \\(o\_i \in \observations\\)

A history is considered a test forming an initial stream of experience. We characterize an environment by a probability distribution over all possible histories, \\(P: \\{\observations | \actions\\}^\* \mapsto [0,1]\\) where \\(P(o\_1, o\_2, \ldots, o\_t | a\_1, a\_2, \ldots, a\_t)\\) is the probability of observations being generated (in the specified order) if the actions are taken (in the specified order). The probability of a test t conditioned on a history h is \\(P(t|h) = \frac{P(th)}{P(h)}\\) is a prediction.

A [PSR]({{< relref "psr.md" >}}) is a set of q core-tests that is sufficient information to determine the prediction for all possible other tests (a sufficient statistic).

The core-tests are a [sufficient statistic]({{< relref "sufficient_statistic.md" >}}) when for any test and history there exists some _prediction function_ \\(f\_t: [0,1]^q \mapsto [0,1]\\) s.t.
\\[
P(t|h) = f\_t([P(t\_1|h), P(t\_2|h), \ldots, P(t\_q|h)]) = f\_t(P(h))
\\]

You can construct a [PSR]({{< relref "psr.md" >}}) from a [POMDP]({{< relref "pomdp.md" >}}) (i.e. a PSR is no more complex than a POMDP). This is discussed as the main result:

<div class="theorem">

For any environment that can be represented by a finite POMDP model, there exists a linear PSR with number of tests no larger than the number of states in the minimal POMDP model.

</div>

<div class="proof">

This proof has three parts. They first review how probabilities are assigned to tests given the POMDP. They then define an algorithm which takes the n-state POMDP model to produce a set of n or fewer tests. They then show that the PSR induces the same probability distribution over histories. To see the proof in full, please see the paper.

</div>


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
</div>
