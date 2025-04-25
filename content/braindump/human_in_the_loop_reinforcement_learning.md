+++
title = "Human-in-the-Loop Reinforcement Learning"
author = ["Matthew Schlegel"]
lastmod = 2025-04-25T08:05:08-06:00
slug = "human_in_the_loop_reinforcement_learning"
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


## Projects {#projects}


## Questions/Thoughts {#questions-thoughts}


### In industrial settings the main competitor is optimal control. {#in-industrial-settings-the-main-competitor-is-optimal-control-dot}

When thinking about human in the loop RL for industrial control we must inevitably think about what is provided from optimal control. Optimal control provides guarantees because they are often able to provide an analytic framework to understand the steady state of their algorithm. RL doesn't have this benefit as our policies are ill-formed for this. Instead, could we estimate the PDE resulting from the interactions between


### Multiple agents vs one agent {#multiple-agents-vs-one-agent}

An interesting thought came up while I was thinking about [Power Systems Control]({{< relref "power_systems_control.md" >}}). Has anyone studied the overall impact on explainability/interactability/interpretability of two agents solving a joint problem w/ clear responsibilities vs one global agent jointly optimizing over the system?

What kinds of changes to the explainability algorithms need to be made to adjust for these two conditions?

What would a human trial look like? What problem could we use other than [Power Systems Control]({{< relref "power_systems_control.md" >}})?

How do I communicate this to Matt, Martha, and Mostafa?


## Notes and Literature {#notes-and-literature}

Human-in-the-loop RL is a large field with lots of players. The goal of this note is to get oriented, and start feeling out directions we can go in the [Power Systems Control]({{< relref "power_systems_control.md" >}}) projects. I think it would be beneficial to go about this in a few ways.

1.  I need to do some more reading and real categorization. I did some previously, but now need to sit down and unravel the bad practices I have done previously so I can come out with better understanding.
2.  I need to do deep thinking in relating current uses of HitL RL in industry to the use case of power systems and focus on developing a final "goal" platform that we can start making progress on.
3.  Answer and ask questions about papers on HitL RL. Build knowledge, interact with the issues and motivations, dig deeper and uncover where core issues lie and figure out the exact language used to discuss these issues.
4.  Create notes and build organization to understand how the literature fits together.


### <span class="org-todo todo IN_PROGRESS">IN-PROGRESS</span> Interaction centric (<a href="#citeproc_bib_item_3">Stanford Online 2022</a>). {#interaction-centric--dot}


### <span class="org-todo todo IN_PROGRESS">IN-PROGRESS</span> Human-in-the-Loop RL Survey (<a href="#citeproc_bib_item_2">Retzlaff et al. 2024</a>) {#human-in-the-loop-rl-survey}


### <span class="org-todo done DONE">DONE</span> Smart Control Room: (<a href="#citeproc_bib_item_1">Ghosh and Bequette 2020</a>) {#smart-control-room}


### <span class="org-todo done DONE">DONE</span> Closing the loop for power systems: (<a href="#citeproc_bib_item_4">Stiasny et al. 2022</a>) {#closing-the-loop-for-power-systems}


### [Explainable RL]({{< relref "explainable_rl.md" >}}) {#explainable-rl--explainable-rl-dot-md}
