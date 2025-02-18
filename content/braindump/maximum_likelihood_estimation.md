+++
title = "Maximum Likelihood Estimation"
author = ["Matthew Schlegel"]
lastmod = 2022-11-09T14:05:18-07:00
slug = "maximum_likelihood_estimation"
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

tags
: [Statistics]({{< relref "statistics.md" >}}), [Machine Learning]({{< relref "machine_learning.md" >}}),

source
: (<a href="#citeproc_bib_item_1">Goodfellow, Bengio, and Courville 2016</a>; <a href="#citeproc_bib_item_2">Wasserman 2004</a>)

The maximum likelihood estimator (MLE) denoted by \\(\hat{\theta}\_n\\), is the value which maximizes the likelihood (or log-likelihood) function defined as

\begin{align\*}
\mathscr{L}\_n(\theta) &= \prod\_i f(\xvec\_i;\theta) &\quad \triangleright \textbf{Likelihood Function} \\\\
l\_n(\theta) &= \log \mathscr{L}\_n(\theta) = \sum\_i \log f(\xvec\_i; \theta) &\quad \triangleright \textbf{Log-Likelihood Function}
\end{align\*}

where instances \\(\xvec\_1, \xvec\_2, \ldots, \xvec\_n\\) are IID with PDF \\(f(\xvec; \theta)\\). We can take the log of the product because the function will have the same stationary points and will have less numerical issues with under/overflow.

The MLE estimator \\(\thetavec\_{\text{MLE}}\\) is one which maximizes the likelihood function:

\\[\thetavec\_{\text{MLE}} = \text{argmax}\_\thetavec \sum\_{i} \log p\_{model}(\xvec\_i).\\]

This can be viewed as minimizing the the dissimilarity between the empirical distribution \\(\hat{p}\_data\\) and the model distribution \\(p\_{model}\\) by minimizing the [KL Divergence]({{< relref "kl_divergence.md" >}}). Because we only have control over the model distribution, this is the same as minimizing

\\[-\expected\_{X\sim\hat{p}(data)} [\log p\_{model}(X)]\\]

This corresponds exactly with minimizing the [Cross-Entropy]({{< relref "cross_entropy.md" >}}).


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Goodfellow, Ian, Yashua Bengio, and Aaron Courville. 2016. <i>Deep Learning</i>. MIT Press.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Wasserman, Larry. 2004. <i>All of Statistics: A Concise Course in Statistical Inference Brief Contents</i>. Springer.</div>
</div>
