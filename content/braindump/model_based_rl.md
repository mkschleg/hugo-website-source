+++
title = "Model-based RL"
author = ["Matthew Schlegel"]
lastmod = 2022-10-27T20:20:04-06:00
slug = "model_based_rl"
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
\newcommand{\thetavec}{\boldsymbol{\theta}}
\newcommand{\phivec}{\boldsymbol{\phi}}
\newcommand{\muvec}{\boldsymbol{\mu}}
\newcommand{\sigmavec}{\boldsymbol{\sigma}}
\newcommand{\jacobian}{\mathbf{J}}
\newcommand{\ind}{\perp\!\!\!\!\perp}
\newcommand{\bigoh}{\text{O}}
\\)

tags
: [Reinforcement Learning]({{< relref "reinforcement_learning.md" >}})

Model-based reinforcement learning is the combination of planning and reinforcement learning. An agent constructs a world model which is used to simulate expected experience. This, in theory, can be significantly more sample efficient than model-free reinforcement learning as an agent can learn behaviours through interacting with the internal world model while avoid the, potentially, costly data collection from the real environment. While there are many model-based approaches which have shown promise with known models (<a href="#citeproc_bib_item_14">Silver et al. 2016</a>) (<a href="#citeproc_bib_item_15">Silver et al. 2017</a>), approaches with learned models have only recently become competitive with model-free approaches (<a href="#citeproc_bib_item_13">Schrittwieser et al. 2020</a>) (<a href="#citeproc_bib_item_5">Hafner et al. 2021</a>). This is because of several failure modes which can occur when learning a model leading to samples which do not represent the real world.

In the below section, I will go over the general approach to MBRL, and then discuss some of the considerations which need to be made when building a world model.


## Background {#background}

   For a more detailed explanation of mbrl please see (<a href="#citeproc_bib_item_10">Moerland, Broekens, and Jonker 2021</a>) or chapter 8 of (<a href="#citeproc_bib_item_16">Sutton and Barto 2018</a>). We focus on the problem of learning an optimal policy for a Markov decision process, from on-policy interaction.
A Markov decision process consists of \\((\states, \actions, \transition, \rewards,\gamma)\\) where
\\(\states\\) is the set of states;
\\(\actions\\) is the set of actions;
\\(\transition: \states \times \actions \times \states \rightarrow [0,\infty)\\) provides the transition probabilities;
\\(\rewards: \states \times \actions \times \states \rightarrow \reals\\) is the reward function;
and \\(\gamma:  \states \times \actions \times \states \rightarrow [0,1]\\) is the transition-based discount function which enables either continuing or episodic problems to be specified \citep{white2017unifying}.
On each step, the agent selects action \\(A\_t\\) in state \\(S\_t\\),  and transitions to \\(S\_{t+1}\\), according to \\(\transition\\), receiving reward
\\(R\_{t+1} = \rewards(S\_t, A\_t, S\_{t+1})\\) and discount \\(\gamma\_{t+1} = \gamma(S\_t, A\_t, S\_{t+1})\\).
For a policy \\(\pi: \states \times \actions \rightarrow [0,1]\\), where \\(\sum\_{a\in \actions} \pi(s,a) = 1 \\; \forall s \in \states\\),
the value at a give state \\(s\\), taking action \\(a\\),
is the expected discounted sum of future rewards, with actions selected according to \\(\pi\\) into the future,

\begin{align\*}
\\!\\!\\!\\! Q^\pi\\!(s, a) \\!=\\! \expected\Big[\\!R\_{t+1} \\!+\\! \gamma\_{t+1} \\!\\!\sum\_{a \in \actions} \\!\\!\pi\\!(S\_{t+1}, \\!a) Q^\pi\\!(S\_{t+1}, \\!a) \Big| S\_t \\!=\\! s,\\! A\_t \\!=\\! a \Big]
\end{align\*}

In model based RL, our goal is the same as model free. We wish to learn a value function or a policy which maximizes the cumulative discounted sum of rewards into the future. Unlike model-free RL, we have access to a model (which is either learned or known) which provides functions \\(\tilde{p}(\approx \transition): \states \times \actions \rightarrow \states\\) and \\(\tilde{r} (\approx\rewards): \states \times \states \rightarrow \reals\\) which approximate the dynamics of the environment. There are several types of models, but in this document we will focus on this specification (which is known as a _forward_ model). The specific type of forward model discussed here is also known as a generative model (i.e. where we generate new examples sampled over a distribution). While there exists algorithms for planning over descriptive models, the focus of the current literature is often on generative models (<a href="#citeproc_bib_item_13">Schrittwieser et al. 2020</a>; <a href="#citeproc_bib_item_5">Hafner et al. 2021</a>).

This model is used for _planning_, which is (to over anthropomorphize) the agent imagining experience using its world model to learn behaviours or do policy evaluation. One well known algorithm to do this is known as Dyna, which simply samples transitions from its world model and uses them to directly.


## Some issues well known in the literature for MBRL {#some-issues-well-known-in-the-literature-for-mbrl}

Below are some known issues with learning a world model to use in planning for an RL agent.


### Stochasticity {#stochasticity}

If the MDP is stochastic--i.e. for any given state action pair there is a distribution over next states instead of a single returned state--then the learned prediction of a model using a non-distribution based loss will learn the mean of the next state distribution. While this is not necessarily bad--and in fact can be used to plan for linear value functions--an approach which models the full distribution (i.e. a generative approach) would provide more options when planning.


### Uncertainty {#uncertainty}

Uncertainty due to limited data (or epistemic uncertainty) is a large problem for models in MBRL. As environments grow, it is unlikely to have many samples throughout the state space to train a model. Thus it would be beneficial to estimate the model's uncertainty in parts of the state space: see (<a href="#citeproc_bib_item_1">Abbas et al. 2020</a>). This uncertainty can be used to determine whether we should use the model to plan or avoid planning in the current state.


### Partial-observability {#partial-observability}

Partial observability is when the agent only observes incomplete information about the environment (i.e. a non-markov state of the environment). This is a property of almost any non-trivial task, and ignoring this property often leads to failure cases.

There have been several ways to deal with partial observability:

-   Windowing
-   Belief States and Pred Reps of State
-   **Recurrency**
-   External Memory


### Non-stationarity {#non-stationarity}

When the graph of the mdp change over time. This can be changes in the transition dynamics or in the reward function. If the agent trusts its model when the environment changes this could lead to the agent learning wrong policies (see (<a href="#citeproc_bib_item_16">Sutton and Barto 2018</a>) section 8).


### Multi-step prediction {#multi-step-prediction}

When planning, using trajectories beyond a single step by feeding the generated state vector into the model has been shown to be beneficial when the model is accurate. Unfortunately, because many models aren't built with multi-step prediction in mind errors can compound when making multi-step predictions.


### State abstraction {#state-abstraction}

Representations are important for all parts of a ML/RL system. This is no different for building a model to predict/generate transitions. But there are several additional considerations beyond what model-free approaches need to account.

1.  How do we ensure that we can plan at a latent level?
2.  How may we better structure our models to emphasize objects and their physical interactions?
3.  How may we construct loss functions that retrieve more informative representations?


### Temporal abstraction {#temporal-abstraction}

Much like state abstraction, we can have representations/abstractions which span the temporal axis of an MDP.


## State of the Art in MBRL: (<a href="#citeproc_bib_item_4">Hafner et al. 2020</a>), (<a href="#citeproc_bib_item_5">Hafner et al. 2021</a>) {#state-of-the-art-in-mbrl}

The so called DreamerV1 and DreamerV2 architectures use a latent distribution model to reach human performance on the Atari domain for the first time for a MB approach.


## Other notable models {#other-notable-models}


### (<a href="#citeproc_bib_item_11">Oh et al. 2015</a>) {#c268b0}


### (<a href="#citeproc_bib_item_3">Goyal et al. 2020</a>) {#6fd2b9}


### (<a href="#citeproc_bib_item_7">Kipf, van der Pol, and Welling 2020</a>) {#9e2979}


## Approaches to MBRL through a causal lens {#approaches-to-mbrl-through-a-causal-lens}


### (<a href="#citeproc_bib_item_2">Gasse et al. 2021</a>) {#5fbf00}

In this paper, the focus is on learning a world model for MBRL from both interventional (online) and observational (offline) data. The main idea is to use a formulation of RL in terms of do-calculus to analyze the viability of incorporating both interventional (online) and observational (offline) data. The problem with incorporating these two data sets is the observational data may be making decisions on components not available to the learning agent (think a column left off for privacy).


### (<a href="#citeproc_bib_item_6">Ke et al. 2021</a>) {#a4d653}

This paper does a systematic study over different inductive biases introduced in learning world models. Specifically they look at two types of structured networks--graph neural networks (<a href="#citeproc_bib_item_7">Kipf, van der Pol, and Welling 2020</a>), and modular networks (<a href="#citeproc_bib_item_3">Goyal et al. 2020</a>)-- and monolithic networks which contain no inductive bias other than the layers used.

In these experiments, they learn the world models and test their ability to perform as causal induction for MBRL. They use two environments to test this, see the paper for details.

They show that structured networks can have a positive effect on the world models ability to predict and perform causal inference, with modular networks being best, which is exasperated as the causal graphs of the underlying problems become more complicated.

While they test these models on their ability to perform causal inference, none of the models seem to use causality explicitly in their derivation.


### (<a href="#citeproc_bib_item_12">Rezende et al. 2020</a>) {#71f3f4}

In MBRL, one type of model looked at is a set partial models (i.e. smaller models each focused on a subset of the observational space). This paper shows these models are causally incorrect, with their predictions relying on parts of the observational space not considered in the local model. They propose a Causal Partial Model, which accounts for changes in the agent's behaviour when making predictions (but not other forms of transfer).


### (<a href="#citeproc_bib_item_9">Mesnard et al. 2020</a>) {#bc1359}

While principally a model-free approach to learning policy gradients, this paper details a new way to take advantage of hindsight for counterfactual credit assignment. The algorithm can be viewed in the lens of the environment being constructed as an SCM, and the principle algorithm can be recovered through successive relaxations of the assumption that the agent must know the model the environment (and have access to the RNG) until the agent is completely model-free (recovering their algorithm). This is mostly of interest for this document for its description of MDPs in terms of SCMs (appendix E and F).


### (<a href="#citeproc_bib_item_8">Luczkow 2021</a>) {#e347b1}
