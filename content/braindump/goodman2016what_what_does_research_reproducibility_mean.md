+++
title = "goodman2016what: What Does Research Reproducibility Mean?"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:26:31-07:00
slug = "goodman2016what"
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
: Goodman, S. N., Fanelli, D., &amp; Ioannidis, J. P. A.

year
: 2016

Goodman sets out to better define the ambiguous terms of scientific "reproducibility". Taking prior efforts to define reproducibility (NSF, Computer Scientist Jon Claerbout, and others), Goodman defines reproducibility under three umbrella terms:

-   _Methods_ reproducibility
-   _Results_ reproducibility
-   _Inferential_ reproducibility


## _Methods_ reproducibility {#methods-reproducibility}

Methods reproducibility encompasses the original meaning of reproducibility (i.e. the ability to implement, as exactly as possible, the experimental and computational procedures). This typically means the authors of a paper must provide enough detail of the study procedures and data so the same procedures could, in theory or in actuality, be exactly repeated. In computer science or machine learning this would mean the sharing of source code and data, while also reporting the hyper-parameters used in the study.


## _Results_ reproducibility {#results-reproducibility}

Results reproducibility refers to obtaining the same results from the conduct of an independent study whose procedures are as closely matched to the original experiment as possible. This primarily is an issue under experiments with random processes inside (i.e. with random results), as a deterministic experiment will share the methods reproducibility criteria.


## _Inferential_ reproducibility {#inferential-reproducibility}

Inferential reproducibility is the highest bar thus far. This refers to the drawing of qualitatively similar conclusions from either an independent replication of a study or a reanalysis of the original study. This means the same conclusions can be drawn devoid of sharing the same procedures, data, or experimental settings. This can be viewed as a proxy for "how true is this conclusion" or "how general is the conclusions drawn in this study". This interacts with both the assumptions made by the experimenters **and** the conclusions they draw (i.e. are their conclusions to broad?).


### Bayesian perspectives {#bayesian-perspectives}

This perspective goes beyond the frequentist view. He frames the probability of a claim being true in terms of prior and posterior probabilities. The prior probability is the likelihood a claim will be true. For example claims of the presence of extrasensory perception requires a large amount of evidence to effect the posterior in the positive because the claim is initially implausible. The more evidence provided, the more likely the claim becomes. In other words, the amount of evidence required for a claim to be inferentially reproducible (or "true") is relative to the prior plausibility of the claim given current understanding.


### Multiplicity {#multiplicity}

This comes in many different flavors, and usually involves the absence of complete reporting. One example of this is testing multiple hypotheses with data gathered from a single experiment. This occurs often in computer science. Another example is p-hacking or HARKing (hypothesizing after the results are known). Another version is the classic file-drawer publication (or the positive bias publishing) problem where results only deemed significant or interesting are published, where those insignificant or uninteresting are left unpublished. This results in a reporting bias where multiple studies are being produced independently but a biased sample is published.


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
</div>
