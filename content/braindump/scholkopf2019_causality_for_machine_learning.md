+++
title = "scholkopf2019causality: Causality for Machine Learning"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:29:08-07:00
slug = "causality_for_machine_learning"
tags = ["Causality"]
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
: [Causality]({{< relref "causality.md" >}})

source
: <https://arxiv.org/abs/1911.10500>

authors
: Scholkopf, B.

year
: 2019

    This paper is going through the arguments on why [Causality]({{< relref "causality.md" >}}) is important for machine learning. I'll only go into detail on a few.


## ML disregards information that animals rely on heavily {#ml-disregards-information-that-animals-rely-on-heavily}

The key properties that Scholkopf cites are:

-   Interventions in the world
-   Domain shifts
-   Temporal structure

While it is true that the core of supervised learning research doesn't interact with these properties, there are several parts of the community which do.

To start the most obvious is [Reinforcement Learning]({{< relref "reinforcement_learning.md" >}}). An RL agent generates its own data through interacting with its world. It must deal with domain shifts of the underlying environment as well as distributional shifts which occur from its own policy. The agent must, especially when the markov assumption isn't meet, abstract temporally and build up beliefs about its current state. While causality does change the problem specification, it doesn't do so in as satisfying a way as RL. In RL an agent builds a policy by maximizing the reward function. It is unclear where behaviour is derived in a causal AI system. In all likelihood, RL agents should be making causal assumptions about the underlying dynamcis and testing these through interventions. It is possible (<a href="#citeproc_bib_item_1">Zhang et al. 2021</a>) has something to say about this, in that we can generate causal belief states which can be explored through causal mechanisms. While this is an interesting directions, building behaviour around this type of approach seems difficult but might be done through an intrinsic mechanism.

Temporal forecasting is also a well established part of the ML community. While not interacting with the data streams generation process, they still generate beliefs about the process to make future predictions.


## The IID assumption {#the-iid-assumption}

The IID assumption is problematic, and that is well known. Some take this an mean all of deep learning is useless, while others try and make the best of the tools we have. Often these arguments are propped up by human's/animal's abilities to "domain shift" or to "generalize". While it is true that organisms w/ a nervous system can often generalize well, that is ignoring a significant amount of priors underneath the policy building process. Now this can be taken to mean that animals are building causal graphs of the underlying world or uncovering statistical correlations. I'm not sure which, and an argument attacking the issues with one while ignoring the issues of the other are slightly disingenuous. Causal methods have issues in that they can only work if there are strong priors on the causal model. These priors can't always be derived by data (i.e. the observed distributions can be equivalent for different causal structures), while only focusing on correlations means the agent may make many egregious mistakes in the meaning of a prediction.


## The adversarial issues w/ ML {#the-adversarial-issues-w-ml}

It is known that certain transformations of observations can cause issues with deep learning agents. This is seen as bad as the changes are "imperceptible to humans". While likely problematic for future applications, these issues are failing to understand how this relates back to human falability. While humans will see this and believe it is something we and other organics don't suffer, I argue it is something we suffer from as well. Not only are there many ways to fool the human eye, but the changes we make to trick humans can't interact with the human visual system as the DL adversarial attacks can. For example the imperceptible noise is often derived from directly differentiating through the model giving detailed information about the agent. These algorithms are also making changes at a different layer in the perceptual process. They aren't working in the light emitting properties, but after the first layer in the brain. I'd argue that if we could attack this part of the human perceptual process we would also be deeply fallible. A better place to test if these networks are vulnerable for robotics/RL/deployed systems on hardware would be to play with the light generation process not an intermediate representation of that.


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Zhang, Amy, Zachary C. Lipton, Luis Pineda, Kamyar Azizzadenesheli, Anima Anandkumar, Laurent Itti, Joelle Pineau, and Tommaso Furlanello. 2021. “Learning Causal State Representations of Partially Observable Environments.”</div>
</div>
