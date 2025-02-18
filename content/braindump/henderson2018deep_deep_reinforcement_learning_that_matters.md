+++
title = "henderson2018deep: Deep Reinforcement Learning That Matters"
author = ["Matthew Schlegel"]
lastmod = 2023-03-21T11:26:50-06:00
slug = "henderson2018deep"
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
: [Reproducibility in Science]({{< relref "reproducibility_in_science.md" >}}), [Deep Reinforcement Learning]({{< relref "deep_reinforcement_learning.md" >}})

source
:


authors
: Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., &amp; Meger, D.

year
: 2018

The premise of the paper is that the RL-problem inherently has issues with measurement and comparisons given the current methodology used for experimentation. This issue is exacerbated in deep learning where little understanding exists on why methods may or may not improve on the existing suite of algorithms. In all, many of our comparisons are potentially flawed and effected by confirmation bias and positive design bias. As a community we should work together to fix these issues.

Contributing factors for misleading or incorrect results/claims:

-   Extrinsic factors (hyperparameters/codebases)
-   intrinsic factors (effects of random seeds or environment properties.)
-   Diversity of metrics
-   Lack of significance testing

Some other works which also look at this problem, providing several benchmarks for testing RL agents:

-   (<a href="#citeproc_bib_item_1">Duan et al. 2016</a>): Looks at several policy gradient methods and creates a massive comparison
-   (<a href="#citeproc_bib_item_3">Whiteson et al. 2011</a>): Propose several metrics that have been widely ignored by the community
-   (<a href="#citeproc_bib_item_2">Machado et al. 2018</a>): Look back at the research resulting from the introduction of the ALE and consider new experimental designs to address many of the issues in the community.


## Experimental Analysis {#experimental-analysis}

Some details:

-   Use OpenAI baseline implementations for most of the tests
    -   ACKTR, PPO, DDPG, TRPO
-   Environments: Hopper-v1, HalfCheetah-v1
-   Use neural networks in all cases.
-   Five experiment trials for each evaluation (each with a different preset random seed)


### Hyper-parameters {#hyper-parameters}

_What is the magnitude of the effect hyperparameter settings can have on baseline performance?_


### Network Architecture {#network-architecture}

_How does the choice of the network architecture for the policy and value function approximation affect performance?_

-   Dying relu problem


### Reward Scale {#reward-scale}

/How can the reward scale affect results? Why is reward rescaling used?


### Random Seeds and Trials {#random-seeds-and-trials}

_Can random seeds drastically alter performance? Can one distort results by averaging an improper number of trials?_


### Environments {#environments}

_How do the environment properties affect variability in reported RL algorithm performance?_


### Codebases {#codebases}

_Are commonly used baseline implementations comparable?_


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Duan, Yan, Xi Chen, Rein Houthooft, John Schulman, and Pieter Abbeel. 2016. “Benchmarking Deep Reinforcement Learning for Continuous Control.” In <i>International Conference on Machine Learning</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Machado, Marlos C., Marc G. Bellemare, Erik Talvitie, Joel Veness, Matthew Hausknecht, and Michael Bowling. 2018. “Revisiting the Arcade Learning Environment: Evaluation Protocols and Open Problems for General Agents.” <i>Journal of Artificial Intelligence Research</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Whiteson, S., B. Tanner, M. E. Taylor, and P. Stone. 2011. “Protecting against Evaluation Overfitting in Empirical Reinforcement Learning.” In <i>2011 IEEE Symposium on Adaptive Dynamic Programming and Reinforcement Learning (ADPRL)</i>.</div>
</div>
