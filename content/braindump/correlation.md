+++
title = "Correlation"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:26:03-07:00
slug = "correlation"
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

The correlation/dependence is any statistical relationship between two random variables or bivariate data. It usually refers to the degree the pair of variables are linearly related.

The most common measure of dependence is the Pearson product-moment correlation coefficient (PPMCC).

\\[\rho\_{X,Y} = \text{corr}(X, Y) = \frac{\text{cov}(X,Y)}{\sigma\_X \sigma\_Y}= \frac{\expected[(X-\mu\_X)(Y-\mu\_Y)]}{\sigma\_X \sigma\_Y}.\\]
