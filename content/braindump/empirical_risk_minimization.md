+++
title = "Empirical Risk Minimization"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:26:21-07:00
slug = "empirical_risk_minimization"
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
: [Machine Learning]({{< relref "machine_learning.md" >}}), [Statistics]({{< relref "statistics.md" >}})

source
: <http://www.cs.cmu.edu/~aarti/Class/10704_Fall16/lec11.pdf>

Empirical risk minimization is a fundamental building block of modern machine learning, and almost every paper is (either explicitly or implicitly) using the idea to learn a function. In a simple machine learning task, there is a dataset \\(\mathcal{Z} = (X, Y)\\) sampled from some distribution \\(p\\), where \\(X\\) are the features and \\(Y\\) are the targets. The goal of this task is to learn an approximation of the map \\(X\_i \mapsto Y\_i\\). To do this, we minimize the risk

\\[
R(f) = \expected\_{\mathcal{Z} \sim p} [ l(f(X\_i), Y\_i)]
\\]

Well we don't have access to the underlying distribution (and if we did the problem would already be solved), so we can only minimize the empirical risk

\\[
\hat{R}(f) = \expected\_{\mathcal{Z} \sim p} [ l(f(X\_i), Y\_i)].
\\]

If we were to find a function which minimizes \\(\hat{R}(f)\\) without restricting the class of functions, we would likely completely overfit to the data set (i.e. create a lookup table) which leads to a poor predictor. Instead we want to find the function which minimizes the empirical risk from a class of functions

\\[
\hat{f}^{ERM} = \text{argmin}\_{f\in\mathcal{F}} \hat{R}(f).
\\]

The easiest way to justify this concept is to bound how bad the empirical approximation might be. This is easily done through the [Hoeffding Inequality]({{< relref "hoeffding_inequality.md" >}}), assuming \\(l(f(x), y) \in [0, 1] \forall (x, y) \in \mathcal{Z}\\)

\begin{align\*}
P(|\hat{R}(f) - R(f))| \geq \epsilon) &\leq 2e^{-2n\epsilon^2} \leq \delta(f)\\\\
\epsilon &= \sqrt{\frac{\ln(\frac{2}{\delta(f)})}{2n}}
\end{align\*}

So we can say with probability \\(1-\delta(f)\\), \\(|\hat{R}(f) - R(f)| < \sqrt{\frac{\ln(\frac{2}{\delta(f)})}{2n}}\\). This can also be rewritten (assuming \\(R(f) \leq \hat{R}(f)\\) which is reasonable) as

\\[
R(f) \leq \hat{R}(f) + \sqrt{\frac{\ln(\frac{2}{\delta(f)})}{2n}} \quad \triangleright \text{with probability } 1-\delta(f).
\\]

The confidence \\(\delta(f)\\) can be thought of as the acceptable "failure" rate for our operation and the accuracy \\(\epsilon\\) dictates the accuracy guaranteed as a "success". The confidence can be thought of as a function of the function class.
