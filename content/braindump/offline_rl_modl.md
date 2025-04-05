+++
title = "Offline RL (Modl)"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:28:38-07:00
slug = "offline_rl_modl"
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

This is just a short document to go over some research that is relevant to Modl for offline RL. The main thrust is to give an overview of some methods for offline reinforcement learning we should look into further, and some ideas for offline RL methods that might fit with our data better.

First, lets just go over what offline reinforcement learning brings to the table over behavior cloning.

In behavior cloning (i.e. imitation learning) the main idea is to use supervised learning to match the predicted action distribution with the action distribution of the data. We have a data set with tuples \\(\ovec\_t, a\_{t+1}\\) with actions \\(a\_{t+1} \sim P\_a(a | s\_t, a \in \actions\\), observations \\(\ovec\_t = f\_o(s\_t) \in \observations\\) and states \\(s\_t \sim P\_s(s | s\_{t-1}, a\_{t}, s \in \states)\\) (i.e. states are Markov). In basic imitation learning we aim to minimize the cross-entropy between the two distributions

\\[
H(P\_a, \hat{y}) = -\expected\_{P\_a}[\log \hat{y}].
\\]

where \\(\hat{y} = f\_\theta(\ovec\_t, a\_{t-1})\\) is the learned distribution.

<aside>

In the above description we are focused on feed forward networks. For recurrent networks or any history dependent networks we can arbitrarily add history to the functions as needed.

</aside>

<aside>

Notice how we are separating state and observation. This is important when looking at literature to see whether or not algorithms assume they have a full Markovian state to work with, or if they are working with an observation which doesn't perfectly reflect this state. We use LSTMs/RNNs to attempt to bridge the gap, but not all methods will work as well with these approaches.

</aside>

As you can see above, the goal of behavior cloning is to match the policy from the data exactly. While this objective is straightforward, it has a number of drawbacks.

-   You are limited to the policy represented by the data. With data that has a mixture of expert and non-expert data the policy will be hard to verify and could have degenerate behavior that doesn't represent the actual desirable policy. There are potential ways around this:
    -   using player's MMR as an input: This is an interesting idea, but so far we have not had a reliable source of this information in our data.
    -   fine-tuning after training: this is problematic because NNs are known to loose plasticity/capacity as they are trained. This also means we have to label data to highlight behaviors we find "desirable".
    -   Only using a subset of the data we want: some of the same issues as above, as well as reducing the amount of data we can use from a data collection event.
    -
-   No easy way to use simpler methods (i.e. non-humans) to generate data to learn the basic parts of the network.

There are a number of ways around this issue. In this document, I'll go over two potential directions and discuss some papers which might be of immediate interest to Modl

-   Offline reinforcement learning
-   self-supervised learning


## Offline Reinforcement Learning {#offline-reinforcement-learning}

Offline reinforcement learning overcomes the mixture of expert and non-expert data through changing the objective. Instead of raw behavior cloning, the goal is to learn a policy which maximizes the sum of cumulated rewards. Rewards are defined as \\(r(s\_{t-1}, a\_t, s\_t) \in \reals\\) and the return is \\(g\_t = \sum\_{i=t} \gamma^i r\_(i+1)\\). We learn a policy which maximizes \\(\expected[g\_t]\\).

<aside>

Please be aware, the above introduction is an extremely simplified version and doesn't discuss the nuance that exists between all these moving parts. For brevity, I've removed these parts. See any of the below papers for a better introduction to offline reinforcement learning. I personally quite like (<a href="#citeproc_bib_item_17">Xiao et al. 2022</a>) for an introduction to offline reinforcement learning.

</aside>


### Why offline RL for our settings? {#why-offline-rl-for-our-settings}

There are two papers which lead me to believe offline reinforcement learning (even when using cleaned expert data) might outperform behavior cloning techniques.

<!--list-separator-->

-  (<a href="#citeproc_bib_item_9">Kumar et al. 2021</a>):

    This paper lays out the theoretical limits of how we should expect our algorithms to perform under different data characterizations. They then perform several experiments replicating these characterizations using a simulated robotics domain (Mujoco). The conclusions outlined are:

    -   Behavior Cloning does better when the set of starting conditions is small/not randomized and the expert data is not noisy.
    -   Offline RL tends to do better when the set of starting states is more randomized and there is noise in the expert data.

    The paper makes several other observations outlining the advantages offline RL can have, even when behavior cloning is

<!--list-separator-->

-  (<a href="#citeproc_bib_item_13">Schweighofer et al. 2022</a>)

    This paper shows similar obsevations as (<a href="#citeproc_bib_item_9">Kumar et al. 2021</a>) where datasets with larger variations/noise tend to favor offline reinforcement learning algorithms. Specifically (in this case) Critic Regularized Regression (<a href="#citeproc_bib_item_15">Wang et al. 2020</a>) and Conservative q-learning (<a href="#citeproc_bib_item_10">Kumar et al. 2020</a>). The ideas specified here are also interesting when thinking about self-supervised learning below.


### Some ORL algorithms I prefer {#some-orl-algorithms-i-prefer}

There are several algorithms worth considering in this direction:

-   TD3+BC: (<a href="#citeproc_bib_item_6">Fujimoto and Gu 2021</a>)
-   In-sample Actor Critic: (<a href="#citeproc_bib_item_17">Xiao et al. 2022</a>)
-   AWAC (Advantage weighted actor critic): (<a href="#citeproc_bib_item_11">Nair et al. 2021</a>)
-   InAC/AWAC + Tsallis Regulation (a bit better than InAC across different data mixtures) (<a href="#citeproc_bib_item_19">Zhu et al. 2024</a>).

These algorithms all have slightly different properties, and need to be compared on our datasets. My preference is on first trying (<a href="#citeproc_bib_item_17">Xiao et al. 2022</a>) and (<a href="#citeproc_bib_item_19">Zhu et al. 2024</a>) based on the results from (<a href="#citeproc_bib_item_19">Zhu et al. 2024</a>). These approaches are better suited for unknown/broad mixtures of data as compared to some of the others. I also am most familiar w/ them (for obvious reasons).


### The reward problem {#the-reward-problem}

A key issue with using offline reinforcement learning in our setting is the definition of a reward function. While I think hand designing a reward function could work for our needs, it is a difficult process and would require a longer iteration loop than we need for behavior cloning. The main way in literature around this issue is through inverse reinforcement learning (or other ways of learning a reward function). (<a href="#citeproc_bib_item_8">Ho and Ermon 2016</a>) (GAIL) is one version of this, but requires online interactions with the environment to work effectively (<a href="#citeproc_bib_item_20">Zolna et al. 2020</a>). Other more recent methods related to gail also use the environment (<a href="#citeproc_bib_item_16">Watson, Huang, and Heess 2023</a>), (<a href="#citeproc_bib_item_14">Viano et al. 2022</a>), etc...

There are a lot of approaches to try ranging from utilizing fully unlabeled data and some labeled data. Below I list several possible approaches we could look into, but don't go into too much detail. We should focus only on methods that **do not require environment interactions**. Why? This is because we can't properly simulate an environment without other players, which would complicate the methods considerably.

-   (<a href="#citeproc_bib_item_20">Zolna et al. 2020</a>): Uses labeled (with reward information) trajectories and contrasts these with unlabeled trajectories. They share three approaches. A naive (flat rewards) approach which can be applied almost immediately (similar to (<a href="#citeproc_bib_item_18">Yu et al. 2022</a>)). An approach which re-weights the objectives between the data, and a third advisarial approach which doesn't need to interact with the environment like gail. The naive approach seems to do quite well, outperforming the behavior cloning in several tests.
-   (<a href="#citeproc_bib_item_18">Yu et al. 2022</a>): This just labels the unlabeled data with zero rewards. We then just need to label a subset of the expert data with rewards (maybe naively) to get the benefit of data sharing.
-   (<a href="#citeproc_bib_item_1">Albaba et al. 2024</a>): This one does use the environment, but it seems like it would be a reasonable extension to learn multiple student agents (i.e. different playersq) in their framework.

Another interesting direction is known as example based control which usues a classifier to direct an agent towards trajectories which are successful. While this is not quite applicable for us as there is no "successful vs unsuccessful" in a complex game, might be worth pursuing using win vs loss (or some other metrics based on a subset of data) (<a href="#citeproc_bib_item_5">Eysenbach, Levine, and Salakhutdinov 2021</a>), (<a href="#citeproc_bib_item_7">Hatch et al. 2022</a>).


## Self-supervised learning {#self-supervised-learning}

Using self-supervised learning is much more straight forward than reinforcement learning. The main idea is to use contrastive learning objectives to create a base network and then fine-tune using imitation learning on expert behavior describing the policy we want to imitate (<a href="#citeproc_bib_item_2">Balestriero et al. 2023</a>) (<a href="#citeproc_bib_item_4">Endrawis et al. 2021</a>).

Avoiding the obvious examples from large models, there are not many examples (that I've found) yet showing the benefits of offline pre-training using self-supervised learning and then fine tuning using imitation learning. The main example I have is (<a href="#citeproc_bib_item_12">Schwarzer et al. 2021</a>) which pretrains representations for RL using a new set of objectives geared towards learning value functions/policies. While these are meant for reinforcement learning they give empirical evidence these work for behavior cloning as well. Another interesting paper is (<a href="#citeproc_bib_item_3">Carroll et al. 2022</a>) which shows the masking is a powerful device for sequential decision making pretraining just like in language models.

The goal of any work in this direction is to try and relate the work in pre-training back to imitation learning/offline reinforcement learning in a sensor based application. I think given the few papers we have, there is a really good chance the pre-training ideas from both offline RL and large models can generalize to our use cases.


## References {#references}

\printbibliography
