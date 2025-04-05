+++
title = "bouthillier2019unreproducible: Unreproducible Research is Reproducible"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:25:44-07:00
slug = "bouthillier2019unreproducible"
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
: [Reproducibility in Science]({{< relref "reproducibility_in_science.md" >}})

source
:


authors
: Bouthillier, X., Laurent, C\\'esar, &amp; Vincent, P.

year
: 2019

This paper focuses on what it is meant for experimental procedures to be [reproducible]({{< relref "reproducibility_in_science.md" >}}). They clearly lay out the terminology of three types of reproducibility, and discuss current methodological practices (showing an upper and lower bound on "reproducibility" in the field). The main goal of the work is to propose a new methodology to empirically compare two models. They also discuss and define the differences (benefits and detriments) of exploratory and empirical research, advocating for balance between the two in the field at large.


## A discussion on reproducibility in Deep Learning {#a-discussion-on-reproducibility-in-deep-learning}

Before detailing the different types of reproducibility, the authors setup a typical [Deep Learning]({{< relref "deep_learning.md" >}}) experiment. From this they identify several sources of variations:

-   Initialization
-   The order of the data presented during training
-   Which particular finite data sample is used for training and testing.

While setting the random seed to a specific value can help fix one of these issues (primarily the initialization of the model), this can lead to a loss of generality of a conclusion drawn from the study.

There are two forms of reproducibility, which can interfere given haphazard experimental design.

1.  Reproduction of _results_: requires the conversion of a stochastic system into a deterministic one (e.g. the seeding process).
2.  Reproduction of _findings_: At odds with reproduction of _results_, where setting the seed to particular value dramatically weakens the generality of the conclusions.

The authors adopt language set out by (<a href="#citeproc_bib_item_1">Goodman, Fanelli, and Ioannidis 2016</a>) who define three types of reproducibility:

1.  **Methods Reproducibility**: A _method_ is reproducible if reusing the original code leads to the same results.
2.  **Results Reproducibility**: A _result_ is reproducible if a reimplementation of the method generates statistically similar values.
3.  **Inferential Reproducibility**: A _finding_ or a _conclusion_ is reproducible if one can draw it from a different experimental setup.

The authors claim, the current computer science literature focus on _methods_ reproducibility (the sharing of source code). This can also address _results_ reproducibility, given sufficient information. But _inferential_ reproducibility is still not addressed, and requires a modified methodology to determine well adjusted conclusions.


## Experiments {#experiments}

The field's current practices can be bounded by a biased and unbiased protocol for selecting hyper-parameters:

-   **Biased** scenario: The optimizer hyper-parameters that are best for one specific model on one specific dataset are applied to all models and datasets.
-   **UnBiased** scenario: Hyper-parameters are selected for each model and dataset independently with an equal budget for the selection.

These will be the two main methodologies tested in this paper.


### Setup {#setup}

They choose 10 SOTA models and several datasets to benchmark performance.

<!--list-separator-->

-  Seed Replicates

    They use 10 difference seeds for each model, and report the average over the performance.

<!--list-separator-->

-  Hyper-parameter tuning for unbiased

    They Use AHSA from: (<a href="#citeproc_bib_item_2">Li et al. 2018</a>)


### Results {#results}

**Performance distributions over seed replicates**:

They present histograms for the seed replicates for different models over each dataset. They find that the overlaps in distribution do not significantly increase between the unbiased and biased scenarios. This can be used to assume the current observations would also hold in a faithful simulation of common practices.

They also conclude that results on a single seed is too brittle, where a different seed will likely invalidate any prior ordering.

**Ranking stability over seed replicates**:

They next perform [Bootstrapping (statistics)]({{< relref "bootstrapping_statistics.md" >}}) with 1000 resamples over the seed replicates of each method to determine an ordering. This ranking makes it possible to compare model performances across several datasets.


## Limitations of the current work {#limitations-of-the-current-work}

-   They only do experiments using the image classification setting. So it is yet unknown if these findings extend past this setting.
-   The use of limited hyper-parameter optimization cycles could bias the final ordering in favor of easy-to-tune models.
-   They also specify a number of other sources of variation within the experimental setup:
    -   The sampling of the datasets
    -   The optimization procedure of the hyper-parameters (i.e. ASHA is a stochastic technique).


## Exploratory vs Empirical Science {#exploratory-vs-empirical-science}

**Empirical research**: Its goal is to test a hypothesis. It aims to build a robust corpus of knowledge. It favors a stable progress of the field.

**Exploratory research**: Its goal is to explore a new subject and gather new observations. Aims to expand the research horizon with new corpus of knowledge and favors fast progress of a field.

A too large proportion of the research devoted to exploratory research increases the risk of seeing lines of research collapsing. A too large proportion devoted to empirical research increases the risk of hampering the progress by limiting exploration. The proper balance is unknown to the field of machine learning at large.


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Goodman, Steven N., Daniele Fanelli, and John P. A. Ioannidis. 2016. “What Does Research Reproducibility Mean?” <i>Science Translational Medicine</i> 8 (341): 341ps12-341ps12. doi:<a href="https://doi.org/10.1126/scitranslmed.aaf5027">10.1126/scitranslmed.aaf5027</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Li, Liam, Kevin Jamieson, Afshin Rostamizadeh, Ekaterina Gonina, Moritz Hardt, Benjamin Recht, and Ameet Talwalkar. 2018. “Massively Parallel Hyperparameter Tuning.”</div>
</div>
