+++
title = "Current Learning Objectives"
author = ["Matthew Schlegel"]
lastmod = 2023-08-08T13:15:03-06:00
slug = "current_learning_objectives"
draft = false
notetype = "research-topic"
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

This note serves as a place for me to track my current learning objectives. It is partially an agenda file and partially a note file.


## Projects {#projects}


### [Incentive Salience]({{< relref "incentive_salience.md" >}}) {#incentive-salience--incentive-salience-dot-md}

This is an alternative to [RPEH]({{< relref "reinforcement_learning_in_the_brain.md#reward-prediction-error-hypothesis-of-dopamine" >}}), and could potentially explain some data better.


### [Developmental Reinforcement Learning]({{< relref "developmental_reinforcement_learning.md" >}}) and [Curiosity]({{< relref "curiosity.md" >}}) and [Pretraining for Reinforcement Learning]({{< relref "pretraining_for_reinforcement_learning.md" >}}) {#developmental-reinforcement-learning--developmental-reinforcement-learning-dot-md--and-curiosity--curiosity-dot-md--and-pretraining-for-reinforcement-learning--pretraining-for-reinforcement-learning-dot-md}

<!--list-separator-->

-  Initial

    I want to know more about learning how to behave to learn.

    <div class="chatbot">

    Some papers suggested by [ChatGPT]({{< relref "chatgpt.md" >}}):

    1.  "Curiosity-driven Exploration by Self-supervised Prediction" by Pathak et al. (2017) introduces a DRL method that uses curiosity-driven exploration to discover new behaviors and skills.
    2.  "Emergence of Grounded Compositional Language in Multi-Agent Populations" by Mordatch and Abbeel (2018) demonstrates how DRL can be used to enable multi-agent populations to develop their own compositional language for communication.
    3.  "Open-ended Learning in Symmetric Zero-sum Games" by Lerer et al. (2019) proposes a DRL approach to enable agents to learn in open-ended environments without a predefined task or reward function.
    4.  "Reinforcement Learning with Unsupervised Auxiliary Tasks" by Jaderberg et al. (2016) introduces a DRL method that uses unsupervised auxiliary tasks to learn a diverse set of skills that can be useful in a wide range of environments.
    5.  "Meta-Reinforcement Learning" by Finn et al. (2017) proposes a DRL approach that enables agents to learn how to adapt to new environments more efficiently by learning to learn.

    </div>

<!--list-separator-->

-  <span class="timestamp-wrapper"><span class="timestamp">[2023-08-02 Wed]</span></span>

    This project has most recently started tearing into some pre-training literature (i.e. [Pretraining for Reinforcement Learning]({{< relref "pretraining_for_reinforcement_learning.md" >}})). There is a lot of interesting work in that direction, and I think it might be a good place to start in terms of developing a pre-training agent, and then playing around with the data distributions used to train such an agent.

    This makes for many more ideas to read about:

    <!--list-separator-->

    - <span class="org-todo todo TODO">TODO</span>  (<a href="#citeproc_bib_item_5">Xie et al. 2022</a>) <span class="tag"><span class="READ">READ</span></span>

    <!--list-separator-->

    - <span class="org-todo todo TODO">TODO</span>  (<a href="#citeproc_bib_item_1">Balestriero et al. 2023</a>) <span class="tag"><span class="READ">READ</span></span>

    <!--list-separator-->

    - <span class="org-todo todo TODO">TODO</span>  [schwarzer2021pretraining: Pretraining Representations for Data-Efficient Reinforcement Learning]({{< relref "schwarzer2021pretraining_pretraining_representations_for_data-efficient_reinforcement_learning.md" >}}) <span class="tag"><span class="READ">READ</span></span>

    <!--list-separator-->

    - <span class="org-todo todo TODO">TODO</span>  (<a href="#citeproc_bib_item_4">Sontakke et al. 2021</a>) <span class="tag"><span class="READ">READ</span></span>

    <!--list-separator-->

    - <span class="org-todo todo TODO">TODO</span>  (<a href="#citeproc_bib_item_3">Pathak et al. 2017</a>) <span class="tag"><span class="READ">READ</span></span>

    <!--list-separator-->

    - <span class="org-todo todo TODO">TODO</span>  (<a href="#citeproc_bib_item_2">Berlyne 1960</a>) <span class="tag"><span class="READ">READ</span></span>


## Topics {#topics}


### More on the different research areas of [Reinforcement Learning in the Brain]({{< relref "reinforcement_learning_in_the_brain.md" >}}) {#more-on-the-different-research-areas-of-reinforcement-learning-in-the-brain--reinforcement-learning-in-the-brain-dot-md}

While [niv2009reinforcement: Reinforcement learning in the brain]({{< relref "niv2009reinforcement_reinforcement_learning_in_the_brain.md" >}}) is a good start, there is much more to do and learn here. Really the focus should be on the [Reward Prediction-Error Hypothesis of Dopamine]({{< relref "reinforcement_learning_in_the_brain.md#reward-prediction-error-hypothesis-of-dopamine" >}}) and how it applies more or less generally. This also relates to [Incentive Salience]({{< relref "incentive_salience.md" >}}) and where these two hypotheses differ/merge on similar explanations.


### Transformers {#transformers}


### Self-Supervised Learning Objectives {#self-supervised-learning-objectives}


### Offline Reinforcement Learning {#offline-reinforcement-learning}


## Unorganized Topics {#unorganized-topics}


### <span class="org-todo todo TODO">TODO</span> Banach Spaces and Convergence {#banach-spaces-and-convergence}


### <span class="org-todo todo TODO">TODO</span> [Pretraining for Reinforcement Learning]({{< relref "pretraining_for_reinforcement_learning.md" >}}) {#pretraining-for-reinforcement-learning--pretraining-for-reinforcement-learning-dot-md}


### <span class="org-todo todo TODO">TODO</span> Basic Inequalities <code>[0/3]</code> {#basic-inequalities}

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  [Hoeffding Inequality]({{< relref "hoeffding_inequality.md" >}})

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  [Markov's Inequality]({{< relref "markov_s_inequality.md" >}})

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  Chebyshev


### <span class="org-todo todo TODO">TODO</span> Bayesian Vs Frequentists {#bayesian-vs-frequentists}


### <span class="org-todo todo TODO">TODO</span> [colombo2014deep: Deep and beautiful. The reward prediction error hypothesis of dopamine]({{< relref "colombo2014deep_deep_and_beautiful_the_reward_prediction_error_hypothesis_of_dopamine.md" >}}) {#colombo2014deep-deep-and-beautiful-dot-the-reward-prediction-error-hypothesis-of-dopamine--colombo2014deep-deep-and-beautiful-the-reward-prediction-error-hypothesis-of-dopamine-dot-md}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_6">Zhang et al. 2009</a>) {#795aeb}


### <span class="org-todo todo TODO">TODO</span> [Neurotransmitter]({{< relref "neurotransmitter.md" >}}) {#neurotransmitter--neurotransmitter-dot-md}


### <span class="org-todo todo TODO">TODO</span> [Dopaminergic Neurons]({{< relref "dopaminergic_neurons.md" >}}) {#dopaminergic-neurons--dopaminergic-neurons-dot-md}


### <span class="org-todo todo TODO">TODO</span> [Dopamine]({{< relref "dopamine.md" >}}) {#dopamine--dopamine-dot-md}


### <span class="org-todo todo IN_PROGRESS">IN-PROGRESS</span> [niv2009reinforcement: Reinforcement learning in the brain]({{< relref "niv2009reinforcement_reinforcement_learning_in_the_brain.md" >}}) {#niv2009reinforcement-reinforcement-learning-in-the-brain--niv2009reinforcement-reinforcement-learning-in-the-brain-dot-md}


### <span class="org-todo todo IN_PROGRESS">IN-PROGRESS</span> Recurrent Neural Networks {#recurrent-neural-networks}

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  GRU


### <span class="org-todo todo TODO">TODO</span> Actor-critic algorithms {#actor-critic-algorithms}


### <span class="org-todo todo TODO">TODO</span> Policy Gradient Methods {#policy-gradient-methods}


### <span class="org-todo todo TODO">TODO</span> Derive the [Bellman Equation]({{< relref "bellman_equation.md" >}}) for general decision problems. {#derive-the-bellman-equation--bellman-equation-dot-md--for-general-decision-problems-dot}


### <span class="org-todo todo TODO">TODO</span> [Value Function]({{< relref "value_function.md" >}}) {#value-function--value-function-dot-md}


### <span class="org-todo todo TODO">TODO</span> [Dynamic Programming]({{< relref "dynamic_programming.md" >}}) {#dynamic-programming--dynamic-programming-dot-md}


### <span class="org-todo todo TODO">TODO</span> [Backpropagation]({{< relref "backpropagation.md" >}}) {#backpropagation--backpropagation-dot-md}

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  [Backpropagation Through Time]({{< relref "backpropagation_through_time.md" >}})


### <span class="org-todo todo TODO">TODO</span> Spiking neural networks {#spiking-neural-networks}

<span class="timestamp-wrapper"><span class="timestamp">[2021-07-30 Fri]</span></span>
<https://cnvrg.io/spiking-neural-networks/>


### <span class="org-todo todo TODO">TODO</span> [Visual System]({{< relref "visual_system.md" >}}) {#visual-system--visual-system-dot-md}


### <span class="org-todo todo TODO">TODO</span> [Control Theory]({{< relref "control_theory.md" >}}) {#control-theory--control-theory-dot-md}


### <span class="org-todo todo TODO">TODO</span> Free-Energy Principle {#free-energy-principle}


### <span class="org-todo todo TODO">TODO</span> Neuron {#neuron}


### <span class="org-todo todo TODO">TODO</span> Integral [Calculus]({{< relref "calculus.md" >}}) {#integral-calculus--calculus-dot-md}


### <span class="org-todo todo TODO">TODO</span> Cerebellum {#cerebellum}


### <span class="org-todo todo TODO">TODO</span> Moment Generating Function {#moment-generating-function}


### <span class="org-todo todo TODO">TODO</span> Chernoff Bounds {#chernoff-bounds}


### <span class="org-todo todo TODO">TODO</span> Scientific Method {#scientific-method}


### <span class="org-todo todo TODO">TODO</span> Kernel Functions {#kernel-functions}


### <span class="org-todo todo TODO">TODO</span> Neuro/Psych background reading. <span class="tag"><span class="RESOURCE">RESOURCE</span></span> {#neuro-psych-background-reading-dot}

<https://docs.google.com/document/d/111-4SPQ1kEg_yrMfud_26rK7fBHpol59iDnZ9BYuzNc/edit>


## Questions {#questions}


### How does loss of plasticity affect exploration? {#how-does-loss-of-plasticity-affect-exploration}

-   <https://arxiv.org/pdf/2204.09560.pdf>
-   <https://proceedings.mlr.press/v162/nikishin22a.html>
-
