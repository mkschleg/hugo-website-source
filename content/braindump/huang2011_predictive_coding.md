+++
title = "huang2011predictive: Predictive Coding"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:27:36-07:00
slug = "huang2011predictive"
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
: [Predictive Processing]({{< relref "predictive_processing.md" >}}), [Hierarchical Predictive Coding]({{< relref "hierarchical_predictive_coding.md" >}})

source
: [paper](https://onlinelibrary.wiley.com/doi/abs/10.1002/wcs.142?casa_token=pm63SatbadEAAAAA:LyhNDX5OM3rN3R5W9HvOIOCdGjB7wb1V4fBqJm57wXYFI28Waka3r0vDIma_oF5zjBkXOoSFhyb3EKg)

authors
: Huang, Y., &amp; Rao, R. P. N.

year
: 2011

This paper surveys the [Predictive Coding]({{< relref "hierarchical_predictive_coding.md" >}}) literature from the original (<a href="#citeproc_bib_item_2">Rao and Ballard 1999</a>) to work recent at original publication (i.e. 2011). As laid out by (<a href="#citeproc_bib_item_2">Rao and Ballard 1999</a>), predictive coding is a framework for describing several neural phenomenon in the visual cortex and other parts of the brain. The core idea is the use of top-down connections to predict incoming signals and only feed the residual information back through the feed-forward connections.


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

(<a href="#citeproc_bib_item_1">Hosoya, Baccus, and Meister 2005</a>)  describes how the retina encodes information through predictive coding, and that there are several phenomenon which are accurately described by a predictive coding scheme. There are not only spatial correlates but also temporal correlates.

"An efficient visual encoder should learn the statistical regularities of the input image and adapt its encoding strategy accordingly."

It has also been suggested that the LGN uses predictive coding to decorrelate the signal from the retina.

Finally, it was suggested by (<a href="#citeproc_bib_item_2">Rao and Ballard 1999</a>) that the visual cortex also implements a form of predictive coding (see [Hierarchical Predictive Coding]({{< relref "hierarchical_predictive_coding.md" >}})).


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Hosoya, Toshihiko, Stephen A. Baccus, and Markus Meister. 2005. “Dynamic Predictive Coding by the Retina.” <i>Nature</i> 436 (7047): 71–77. doi:<a href="https://doi.org/10.1038/nature03689">10.1038/nature03689</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Rao, Rajesh P. N., and Dana H. Ballard. 1999. “Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects.” <i>Nature Neuroscience</i> 2 (1): 79. doi:<a href="https://doi.org/10.1038/4580">10.1038/4580</a>.</div>
</div>
