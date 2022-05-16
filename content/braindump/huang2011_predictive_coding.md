+++
title = "huang2011: Predictive Coding"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:21-06:00
slug = "huang2011"
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
: [Predictive Processing]({{<relref "predictive_processing.md#" >}}), [Hierarchical Predictive Coding]({{<relref "hierarchical_predictive_coding.md#" >}})

source
: [paper](https://onlinelibrary.wiley.com/doi/abs/10.1002/wcs.142?casa%5Ftoken=pm63SatbadEAAAAA:LyhNDX5OM3rN3R5W9HvOIOCdGjB7wb1V4fBqJm57wXYFI28Waka3r0vDIma%5FoF5zjBkXOoSFhyb3EKg)

authors
: Huang, Y., & Rao, R. P. N.

year
: 2011

This paper surveys the [Predictive Coding]({{<relref "hierarchical_predictive_coding.md#" >}}) literature from the original <sup id="7b979f5b998905dc446bf66499306a20"><a href="#rao1999" title="Rao \&amp; Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, {Nature Neuroscience}, v(), (1999).">rao1999</a></sup> to work recent at original publication (i.e. 2011). As laid out by <sup id="7b979f5b998905dc446bf66499306a20"><a href="#rao1999" title="Rao \&amp; Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, {Nature Neuroscience}, v(), (1999).">rao1999</a></sup>, predictive coding is a framework for describing several neural phenomenon in the visual cortex and other parts of the brain. The core idea is the use of top-down connections to predict incoming signals and only feed the residual information back through the feed-forward connections.


## Predictive coding in space {#predictive-coding-in-space}

The main idea here is to use the surrounding intensity information of a pixel in an image to encode the information of the current pixel. Mathematically, they model this as a linear weighting of \\(2N\\) pixel intensities \\(x\_{-N}, x\_{-N+1}, \ldots x\_{N}\\),

\\[
\hat{x}\_0 = \sum\_i w\_i x\_i.
\\]

Supposing we have k pixels we are doing this weighting for, we can find the optimal linear weighting through the usual linear least squares solution (also including regularization if needed)

\\[
\Wmat = (\Bmat^\trans \Bmat)^\inv \Bmat^\trans \avec
\\]

where \\(\avec \in \reals^{k \times 1}\\) is the stacked pixel intensities (of the pixels of interest), \\(\Bmat \in \reals^{k \times 2N}\\) is the stacked neighboring pixel intensities.


## Predictive coding in time {#predictive-coding-in-time}

The main difference here is the "neighboring" intensities from the spatial predictive coding scheme are instead based on the history of the pixel.


## Predictive Coding in the Nervous System {#predictive-coding-in-the-nervous-system}

<sup id="8c0df6e004a59bbb491cb14582298625"><a href="#hosoya2005" title="Hosoya, Baccus \&amp; Meister, Dynamic Predictive Coding by the Retina, {Nature}, v(), (2005).">hosoya2005</a></sup> describes how the retina encodes information through predictive coding, and that there are several phenomenon which are accurately described by a predictive coding scheme. There are not only spatial correlates but also temporal correlates.

"An efficient visual encoder should learn the statistical regularities of the input image and adapt its encoding strategy accordingly."

It has also been suggested that the LGN uses predictive coding to decorrelate the signal from the retina.

Finally, it was suggested by <sup id="7b979f5b998905dc446bf66499306a20"><a href="#rao1999" title="Rao \&amp; Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, {Nature Neuroscience}, v(), (1999).">rao1999</a></sup> that the visual cortex also implements a form of predictive coding (see [Hierarchical Predictive Coding]({{<relref "hierarchical_predictive_coding.md#" >}})).


## References {#references}


# Bibliography
<a id="rao1999"></a>[rao1999] Rao & Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, <i>Nature Neuroscience</i>,  (1999). [↩](#7b979f5b998905dc446bf66499306a20)

<a id="hosoya2005"></a>[hosoya2005] Hosoya, Baccus & Meister, Dynamic Predictive Coding by the Retina, <i>Nature</i>,  (2005). [↩](#8c0df6e004a59bbb491cb14582298625)
