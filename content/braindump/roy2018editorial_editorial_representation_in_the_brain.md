+++
title = "roy2018editorial: Editorial: Representation in the Brain"
author = ["Matthew Schlegel"]
lastmod = 2023-03-20T12:38:13-06:00
slug = "roy2018editorial"
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
:


source
:


authors
: Roy, A., Perlovsky, L., Besold, T. R., Weng, J., &amp; Edwards, J. C. W.

year
: 2018

The [Representations in the Brain](https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01410/full) is a collection of articles detailing theory on representations in the brain. This editorial is a brief overview of this topic and provides a synopsis of the papers provided in the collection.

Roy talks about four main topics:


## Abstract concepts exist (or have to exist) at the single cell level. {#abstract-concepts-exist--or-have-to-exist--at-the-single-cell-level-dot}

The main argument here is that there are two types of representations in the brain: distributed and local.

-   A distributed representation occurs on the input side of a neuron, (i.e. many dendrites/connections to other neurons).
-   A local representation is the neuron itself (i.e. the receiver and interpreter of signals

This requires a "consumer" of the signals, a separate party which must establish meaning and interpretation to the collection of signals. Without the consumer, there is nowhere for the signals to be used or received. You can consider other neurons to be the consumers of the signals, where new (potentially more abstract) information is generated up and down the neural hierarchy.

Another account by Tsotsos looks to complexity analysis to decide on the types of representation needed in the confines of the computational resources available to the brain. Much of his work is centered on vision. He has quite a bit of empirical evidence showing "abstract representations" reduce computational complexities in the brain.  The complexity of the vision problem, he claims, tells us there is no single solution and the problem must be reframed into sub-spaces where each may be solvable.

One of the most interesting quotes (which he took from Zucker 1981) is " _One of the strongest arguments for having explicit abstract representations is the fact that they provide explanatory terms for otherwise difficult (if not impossible) notions._"

Feldman claims that the term "representation" presupposes a seperation of process and data, which is fine for books and computers, but hopeless for the brain. Brains are not in the storage or truth business, but compute actions and actionability.

Roy also presents some arguments and evidence for single-cell based simple and complex abstractions from neurophysiological studies. According to roy these neurophysiology studies reveal the existence of a purely abstract cognitive system in the brain encoded by single cells.


## Sparse distributed representation (population coding) of abstract concepts {#sparse-distributed-representation--population-coding--of-abstract-concepts}

They talk about three approaches to sparse representations here.


### Topographic Representations {#topographic-representations}

Topographic representations are essentially projections from high-dimensional space to lower dimensional spaces. The low-dimensional representations are reported to be widely used in the brain: retinotopy in the visual system, tonotopy in the auditory system, and somatotopy in the somatosensory system.


### Remote Associates Test (RAT) {#remote-associates-test--rat}

This is a specific test to determine a persons "creativity". Kajic presented a model using spiking neurons, which showed significant correlation with human performance on the RAT task. Tye used a distributed representation in their model, but each neuron in such a representation has a <span class="underline">preferred stimuli</span> (similar to the vision system). This could suggest a sparse representation is how the human brain solves tasks such as RAT.


### Information compressions at different levels of the hierarchy {#information-compressions-at-different-levels-of-the-hierarchy}

Here Balkenius and Gardenfors explain how the brain can abstract from neurocognitive representations to psychological spaces and show how population coding at the neural level can generate these abstractions. They use radial-basis function networks to map population codes to such lower dimensional spaces. One aspect of their theory is that the coding of the low-dimensional spaces need not be explicitly expressed in individual neurons but the spatial structures are emergent properties.


## Symbolic models {#symbolic-models}

This section talks about moving symbols around, which I'm going to skip...


## Learning motor skills from imagery vs. actual execution. {#learning-motor-skills-from-imagery-vs-dot-actual-execution-dot}

Frank and Schack look at several studies on the learning of motor skills by imagery and execution from three perspections:

-   Performance
    Actual change in motor behavior
-   Brain
    Changes in the neurophysiological representation of motor action
-   Mind
    Changes in the perceptual cognitive representation of motor action (maybe how well the participant believes they'll perform).

From these studies, they conclude that very little is known about how actual learning takes place under these different forms of practice.


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
</div>
