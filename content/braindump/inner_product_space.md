+++
title = "Inner Product Space"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:22-06:00
slug = "inner_product_space"
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
: [Math]({{<relref "math.md#" >}}), [Linear Algebra]({{<relref "linear_algebra.md#" >}})

source
: <https://en.wikipedia.org/wiki/Inner%5Fproduct%5Fspace>

An inner product space is a [Vector Space]({{<relref "vector_space.md#" >}}) \\(V\\) over a field \\(F\\) which is equipped with an inner product \\(\langle \cdot, \cdot \rangle: V \times V \mapsto F\\) and satisfies the following for \\(u, v \in V\\) and \\(c \in F\\):

1.  [Conjugate]({{<relref "conjugate.md#" >}}) symmetry:
    \\[ \langle \uvec, \vvec \rangle = \overline{\langle \vvec, \uvec \rangle}\\]
2.  [Linearity]({{<relref "linear_map.md#" >}}) in the first argument:

    \begin{align\*}
    \langle c\uvec, \vvec \rangle &= c \langle \uvec, \vvec \rangle \\\\\\
    \langle \uvec + \xvec, \vvec \rangle &= \langle \uvec, \vvec \rangle + \langle \uvec, \vvec \rangle\\\\\\
    \end{align\*}
3.  Positive Definite:
    \\[\langle \uvec, \uvec \rangle > 0 \quad \forall \uvec \in V/\\{\mathbf{0}\\} \\]

You can have an inner product space without positive definiteness, but that criteria makes the IPS strict.

Given the inner product, we can define a norm,

\\[\\|{\uvec}\\|\_2 = \sqrt{\langle \uvec, \uvec \rangle}\\]
