+++
title = "byrd2019: What is the Effect of Importance Weighting in Deep Learning?"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:12-06:00
slug = "byrd2019"
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

tags
: [Machine Learning]({{<relref "machine_learning.md#" >}})

source
: <https://arxiv.org/abs/1812.03372>

authors
: Byrd, J., & Lipton, Z.

year
: 2019

**Main Question:** what is the impact of importance weights on over-parameterized deep neural networks?


## Main Findings: {#main-findings}

-   While importance weighting impacts deep nets early in training, so long as the nets are able to separate the training data, its effect diminishes over successive epochs.
-   L2 regularization and batch norm (but not dropout) restore some of the impact of importance weighting, they express the effect via the wrong abstraction.
-   Empirical results are replicated across a number of datasets and networks
-   These results call into question the application of importance weighting when applied to deep networks.


## Experiments {#experiments}

They used two data sets. The first was with examples drawn from a gaussian distribution, with counter-examples rotated and translated from the true examples. The major hallmark of this set is that the data is linearly separable, and any ANN will be an over-parameterized model. These results show poor performance in early learning when weighting the classes losses, but the change in decision plane is as expected (i.e. the error is distributed towards the lower weighted examples). As training progresses, the effects of the weighting completely vanish, where the network accurately specifies all points.

They also used the CIFAR-10 datasets in a number of experiments to show similar effects using the Dog and Cat classes.


## Conclusions: (highlights) {#conclusions--highlights}

-   The effects from importance weighting on deep networks may only occur in conjunction with early stopping, disappearing asymptotically.
-   The learned solution may be determined solely by the location of training examples, independent of their density.
-   These findings should raise concerns on the impact of importance weighting in deep learning as a standard tool.
-   Weighting the loss function of deep networks fails to correct for training set class imbalance. However, sub-sampling a class in the training set clearly affects the network's predictions.
