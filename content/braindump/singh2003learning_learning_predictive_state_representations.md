+++
title = "singh2003learning: Learning Predictive State Representations"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:35-06:00
slug = "singh2003learning"
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
: [PSR]({{<relref "psr.md#" >}})

source
: <https://www.aaai.org/Papers/ICML/2003/ICML03-093.pdf>

authors
: Singh, S. P., Littman, M. L., Jong, N. K., Pardoe, D., & Stone, P.

year
: 2003

The first algorithm for learning [PSR]({{<relref "psr.md#" >}})s. The algorithm is built around minimizing the error function:

\\[
\mathcal{L\_t} = \sum\_{x \in X\_t} \left[ p(x|h\_{t-1}) - \hat{p}(x|h\_{t-1}) \right]^2
\\]

But this loss function is intractable to use the true gradient of the loss function(i.e. \\(p(x | h\_{t-1})\\) is difficult to procure). They instead used a simplified learning rule:

\begin{array}{ll}
\forall x \in E\_{t}, & \hat{m}\_{x} \leftarrow \hat{m}\_{x}+\alpha\_{t} \frac{1}{w\_{x, t}^{\pi}}\left[\chi\_{x, t}-\hat{p}\_{t}^{T} \hat{m}\_{x}\right] \hat{p}\_{t} \\\\\\
\forall x \notin E\_{t}, & \hat{m}\_{x} \leftarrow \hat{m}\_{x}
\end{array}

Where \\(E\_t\\) are the set of extension tests ran at time step t.


## References {#references}


</Users/Matt/GD/bib/full_library.bib>
