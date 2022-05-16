+++
title = "james2004: Learning and Discovery of Predictive State Representations in Dynamical Systems with Reset"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:23-06:00
slug = "james2004"
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
: [link](https://dl.acm.org/doi/abs/10.1145/1015330.1015359?casa%5Ftoken=4Wf-cJMQg-4AAAAA:JNGqd4FcbU3M4Oz5SqqOJ0FYKpK5inq%5FyE4dHIPiH5naFtmMymEIPkeJ6u42c1Q5X0-aUZ4KMnQ)

authors
: James, M. R., & Singh, S.

year
: 2004

This paper provides a new algorithm for learning linear-PSRs in partially observable dynamical systems w/ reset and a new algorithm for the discovery of PSRs from data. Overall, the algorithm works better than previous attempts (i.e. <sup id="da72af3035258ab5a90f8e22e1e57a1f"><a href="#singh2004" title="Singh, James \&amp; Rudary, Predictive {{State Representations}}: {{A New Theory}} for {{Modeling Dynamical Systems}}, in in: {Proceedings of the 20th {{Conference}} on {{Uncertainty}} in {{Artificial Intelligence}}}, edited by {AUAI Press} (2004)">singh2004</a></sup>, <sup id="878156a260e44ebcdafc197af6811a6c"><a href="#singh2003learning" title="Singh, Littman, Jong, Pardoe \&amp; Stone, Learning Predictive State Representations, in in: {Proceedings of the 20th International Conference on Machine Learning ({{ICML}}-03)}, edited by (2003)">singh2003learning</a></sup>).

While the algorithm does better than previously and the discovery algorithm is definitely a start, relying on a reset action seems to be a hard limitation in many more interesting dynamical systems. Particularly the examples used (i.e. the classic POMDP suite of experiments) had to be altered for the algorithm to work.


## References {#references}


# Bibliography
<a id="singh2004"></a>[singh2004] Singh, James & Rudary, Predictive State Representations: A New Theory for Modeling Dynamical Systems, in in: Proceedings of the 20th Conference on Uncertainty in Artificial Intelligence, edited by AUAI Press (2004) [↩](#da72af3035258ab5a90f8e22e1e57a1f)

<a id="singh2003learning"></a>[singh2003learning] Singh, Littman, Jong, Pardoe & Stone, Learning Predictive State Representations, in in: Proceedings of the 20th International Conference on Machine Learning (ICML-03), edited by (2003) [↩](#878156a260e44ebcdafc197af6811a6c)
