+++
title = "Lagrange multipliers"
author = ["Matthew Schlegel"]
lastmod = 2022-11-09T14:05:35-07:00
slug = "lagrange_multipliers"
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
: [Math]({{< relref "math.md" >}}), [Calculus]({{< relref "calculus.md" >}}), [Optimization]({{< relref "optimization.md" >}})

source
: (<a href="#citeproc_bib_item_1">Bishop 2006</a>)

**Lagrange multipliers** (sometimes referred to as **undetermined multipliers**) are used to find [Stationary Point]({{< relref "stationary_point.md" >}})s of a function \\(f\\) of several variables subject to one or more constraints. Given a function \\(f(\xvec)\\) with domain \\(\numfield^D\\) we want to find the maximum (or any [Stationary Point]({{< relref "stationary_point.md" >}})) subject to the constraint relating the elements of \\(\xvec\\) in the form

\\[g(\xvec) = 0.\\]

Given a D-dimensional vector space, the constraint \\(g(\xvec)=0\\) represents a (D-1)-dimensional surface in the space. Any point on the constraint surface will have a gradient \\(\nabla g(\xvec)\\) which is orthogonal to the surface.

<aside>

If it doesn't make intuitive sense why the gradient of any point on the constrained surface will be zero, consider \\(\xvec\\) on the surface and another point nearby also on the surface \\(\xvec + \epsilonvec\\). If we make a [Taylor expansion]({{< relref "taylor_expansion.md" >}}) around \\(\xvec\\),
\\[g(\xvec + \epsilonvec) \approx g(\xvec) + \epsilonvec^\trans \nabla g(\xvec).\\]

Because both \\(\xvec\\) and \\(\xvec + \epsilonvec\\) lie on the constraint surface, we have \\(g(\xvec) = g(\xvec + \epsilonvec)\\) which means \\(\epsilonvec^\trans \nabla g(\xvec) \approx 0\\) and in the limit \\(\lVert \epsilonvec \rVert \rightarrow 0\\) we can say \\(\epsilonvec^\trans \nabla g(\xvec) = 0\\). Because \\(\epsilonvec\\) is parallel to the constrain surface, the gradient must be orthogonal.

</aside>

Next we seek a point \\(\xvec^\*\\) on the constraint surface such that \\(f(\xvec)\\) is maximized. This point must have the property that the gradient \\(\nabla f(\xvec^\*)\\) is also orthogonal to the surface. Thus \\(\nabla f(\xvec^\*)\\) and \\(\nabla g(\xvec\*)\\) are parallel at this point meaning there exists some parameter \\(\lambda\\)

\\[\nabla f + \lambda \nabla g = 0.\\]

This brings us to the **Lagrangian function**.

<div title="Lagrangian Function" class="definition">

The **Lagrangian function** is defined by
\\[L(\xvec, \lambda) \defeq f(\xvec) + \lambda g(\xvec)\\]

</div>

Finding a [Stationary Point]({{< relref "stationary_point.md" >}}) of \\(L(\xvec, \lambda)\\) with respect to both \\(\xvec\\) and \\(\lambda\\) will find the value \\(\xvec^\*\\) satisfying the constraint.


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Bishop, Christopher M. 2006. <i>Pattern Recognition and Machine Learning</i>. Information Science and Statistics. New York: Springer.</div>
</div>
