+++
title = "General Value Functions"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:18-06:00
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

General value functions (GVFs) are a generalization of value functions to predict signals other than the reward. They were introduced in <sup id="da5cbde783710a32df63b84e8f26841e"><a href="#sutton2011" title="Sutton, Modayil, Delp, Degris, Pilarski, White \&amp; Precup, Horde: {{A Scalable Real}}-Time {{Architecture}} for {{Learning Knowledge}} from {{Unsupervised Sensorimotor Interaction}}, in in: {The 10th {{International Conference}} on {{Autonomous Agents}} and {{Multiagent Systems}} - {{Volume}} 2}, edited by {International Foundation for Autonomous Agents and Multiagent Systems} (2011)">sutton2011</a></sup> and further explored in <sup id="6fceb69e8c4a6a5252651a794873ca9f"><a href="#modayil2014" title="Modayil, White \&amp; Sutton, Multi-Timescale {{Nexting}} in a {{Reinforcement Learning Robot}}, {Adaptive Behavior}, v(), (2014).">modayil2014</a></sup> and <sup id="4ab499feaa94f45a15c71f81805a132c"><a href="#white2015" title="White, Developing a Predictive Approach to Knowledge, {University of Alberta}, v(), (2015).">white2015</a></sup>, where the authors demonstrated their capabilities on a robot system (the [critterbot]({{<relref "critterbot.md#" >}})). The goal of this demonstration was to show what can be learned using GVFs, and how the prediction making capabilities scale computationally.

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

This work was spearheaded by me in <sup id="74f08b054b2897fd17312dc85196f769"><a href="#schlegel2020" title="Schlegel, Jacobsen, Abbas, Patterson, White \&amp; White, General {{Value Function Networks}}, {Journal of Artificial Intelligence Research}, v(), (2020).">schlegel2020</a></sup>. The main idea is to constrict the hidden state of an [RNN]({{<relref "recurrent_neural_network.md#" >}}) to


### General Value Functions for Auxiliary Tasks {#general-value-functions-for-auxiliary-tasks}


### Predicting Surprise {#predicting-surprise}


### Estimating variance {#estimating-variance}


## References {#references}


# Bibliography
<a id="sutton2011"></a>[sutton2011] Sutton, Modayil, Delp, Degris, Pilarski, White & Precup, Horde: A Scalable Real-Time Architecture for Learning Knowledge from Unsupervised Sensorimotor Interaction, in in: The 10th International Conference on Autonomous Agents and Multiagent Systems - Volume 2, edited by International Foundation for Autonomous Agents and Multiagent Systems (2011) [↩](#da5cbde783710a32df63b84e8f26841e)

<a id="modayil2014"></a>[modayil2014] Modayil, White & Sutton, Multi-Timescale Nexting in a Reinforcement Learning Robot, <i>Adaptive Behavior</i>,  (2014). [↩](#6fceb69e8c4a6a5252651a794873ca9f)

<a id="white2015"></a>[white2015] White, Developing a Predictive Approach to Knowledge, <i>University of Alberta</i>,  (2015). [↩](#4ab499feaa94f45a15c71f81805a132c)

<a id="schlegel2020"></a>[schlegel2020] Schlegel, Jacobsen, Abbas, Patterson, White & White, General Value Function Networks, <i>Journal of Artificial Intelligence Research</i>,  (2020). [↩](#74f08b054b2897fd17312dc85196f769)
