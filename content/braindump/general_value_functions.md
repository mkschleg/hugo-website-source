+++
title = "General Value Functions"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:26:26-07:00
slug = "general_value_functions"
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

General value functions (GVFs) are a generalization of value functions to predict signals other than the reward. They were introduced in (<a href="#citeproc_bib_item_3">Sutton et al. 2011</a>)  and further explored in (<a href="#citeproc_bib_item_1">Modayil, White, and Sutton 2014</a>; <a href="#citeproc_bib_item_4">White 2015</a>), where the authors demonstrated their capabilities on a robot system (the [critterbot]({{< relref "critterbot.md" >}})). The goal of this demonstration was to show what can be learned using GVFs, and how the prediction making capabilities scale computationally.

A GVF is defined as the expected discounted return of a cumulant:

\\[
v\_{c, \gamma, \pi}(s) = \expected\left[\sum\_{k=t}^\infty \left(\prod\_{i=t+1}^k \gamma(S\_i)\right) c\_{k+1} \middle| S\_t = s, A\_{t:\infty} \sim \pi\right].
\\]

-   Cumulant (\\(c\\))

    The cumlant is a function of any real-valued signal the agent has access to. Some possible values

    -   Observations
    -   Reward
    -   Other predictions
    -   Agent-state.

    This is like the reward function, and details what signal the GVF is predicting.

-   Continuation function (\\(\gamma\\))

    The continuation function (also known as the discount or termination function) and defines the temporal horizon of the prediction. This function should have values \\(\in [0,1]\\), and for at least one state the value must be \\(<1\\).

-   Policy (\\(\pi\\))

    The policy determines the prediction's target policy. Off-policy prediction is an important factor in GVFs, and when thinking about the predictions in terms of knowledge off-policy predictions can be seen as a form of counter-factual reasoning as it enables the agent to "think" or make predictions about different ways of acting.


## Uses {#uses}

General value functions are relatively new. Unfortunately, there have not been a lot of uses of GVFs explored in literature.


### General Value Function Networks (GVFNs) {#general-value-function-networks--gvfns}

This work was spearheaded by me in (<a href="#citeproc_bib_item_2">Schlegel et al. 2021</a>). The main idea is to constrict the hidden state of an [RNN]({{< relref "recurrent_neural_network.md" >}}) to GVFs.


### General Value Functions for Auxiliary Tasks {#general-value-functions-for-auxiliary-tasks}


### Predicting Surprise {#predicting-surprise}


### Estimating variance {#estimating-variance}


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Modayil, Joseph, Adam White, and Richard Sutton. 2014. “Multi-Timescale Nexting in a Reinforcement Learning Robot.” <i>Adaptive Behavior</i> 22 (2): 146–60. doi:<a href="https://doi.org/10.1177/1059712313511648">10.1177/1059712313511648</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Schlegel, Matthew, Andrew Jacobsen, Zaheer Abbas, Andrew Patterson, Adam White, and Martha White. 2021. “General Value Function Networks.” <i>Journal of Artificial Intelligence Research</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Sutton, Richard, Joseph Modayil, Michael Delp, Thomas Degris, Patrick M. Pilarski, Adam White, and Doina Precup. 2011. “Horde: A Scalable Real-time Architecture for Learning Knowledge from Unsupervised Sensorimotor Interaction.” In <i>The 10th International Conference on Autonomous Agents and Multiagent Systems - Volume 2</i>, 761–68. International Foundation for Autonomous Agents and Multiagent Systems.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>White, Adam. 2015. “Developing a Predictive Approach to Knowledge.” University of Alberta.</div>
</div>
