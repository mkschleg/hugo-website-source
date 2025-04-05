+++
title = "Upperbound 2023"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:29:49-07:00
slug = "upperbound_2023"
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


## Continual RL Workshop {#continual-rl-workshop}


### Questions {#questions}

<!--list-separator-->

-  Do the dynamics of the environment change?

    no. The dynamics are hugely complex, but there is regularity in those dynamics the agent can use to predict.
    The dynamics aren't unstationary, the world is just partially observable. The reward is what changes.

    How do you differentiate between.

<!--list-separator-->

-  Is a changing environment enough?

    Are we going to run into the trap of "we want to solve every problem with one agent."

<!--list-separator-->

-  I think the hesitation and desire to pull off the shelf comes from the lack of experience building purpose built simulations.


### Adam {#adam}

<!--list-separator-->

-  Does the agent need to get better over time? Is this too much of an expectation? Learning something new may disrupt old knowledge? <span class="tag"><span class="question">question</span></span>

<!--list-separator-->

-  How to compare algorithms other than ranking through return? -&gt; Emergent behavior?

<!--list-separator-->

-  Need more than grid world. What do we want to show in our agents? Without ranking we care a lot about behavior. But what kind of behavior do we care about?

    Are there general classes of behavior we want to see? Putting pieces together. working towards a goal, self directed adaptation.

    -   Goal directed?
    -   curious/exploration behavior
    -


### Marlos "What's wrong w/ ALE?" {#marlos-what-s-wrong-w-ale}

<!--list-separator-->

-  "ALE became a benchmark"

<!--list-separator-->

-  Domain/Game specific progress? Is this wrong? Only if you are claiming general progress.

<!--list-separator-->

-  How do we move on from atari?

    -   More games?
    -   Focused research on specific domains? Maybe real world problems are the correct answer.

    <!--list-separator-->

    -  Agent-centric domains:

        -   [DeepMind Lab]({{< relref "deepmind_lab.md" >}})
        -   Lunar Lander, maybe needs to be updated/modified.
        -   Many other robotic domains/Mujoco etc...

<!--list-separator-->

-  How do we build an environment with enough complexity that does have a prescriptive search order? <span class="tag"><span class="question">question</span></span>

    -   Games, BoTW's creative design platform (2d, filled with world complexity).


### Peter Stone {#peter-stone}

<!--list-separator-->

-  Automated curriculum learning <span class="tag"><span class="topic">topic</span></span>

<!--list-separator-->

-  LIBERO-not really a from scratch domain.

    -   Knowledge transfer benchmark? Says it is for lifelong learning
    -   Sequence of tasks...
    -   How is this better than something like proc gen, the env farial uses, etc...?
    -   Try and get data from the McGill lab.

<!--list-separator-->

-  Highway domain

<!--list-separator-->

-  Should we be thinking about a stream of tasks?

    I think it is a useful abstraction. Not because it will produce algorithms/ideas which will push to the "full problem" but because it is a reasonable place where clear applications can be made. Not about solving intelligence, about producing useful algorithms/techniques for an applied problem.

    But much of psychology is done in a task environment. You do study animals in their habitat, but when going to try to understand the animal and the underlying mechanisms you study individual controlled tasks. Both arguments reek of what-aboutism.


### Martha White "Continual RL Environments" {#martha-white-continual-rl-environments}


### Doina {#doina}

-   Environment: Induction is important.
-   Apperature modification. Minigrid?
