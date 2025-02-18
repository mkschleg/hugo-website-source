+++
title = "Linear Regression"
author = ["Matthew Schlegel"]
lastmod = 2022-11-10T16:45:22-07:00
slug = "linear_regression"
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

Linear regression is the simplest form of regression and is used to minimize the mean squared error (MSE). More specifically, we model the labels as a linear function with error
\\[
\yvec = \Xmat \wvec + \boldsymbol{\varepsilon}
\\]
where,

\\[\begin{align\*}
\yvec &= \begin{bmatrix}
y\_1 \\\\
y\_2 \\\\
\vdots \\\\
y\_n
\end{bmatrix} \\\\
\Xmat &= \begin{bmatrix}
1 & x\_{11} & x\_{12} & \ldots & x\_{1p} \\\\
1 & x\_{21} & x\_{22} & \ldots & x\_{2p} \\\\
1 & x\_{31} & x\_{32} & \ldots & x\_{3p} \\\\
\vdots & \vdots & \vdots & \ddots & \vdots \\\\
1 & x\_{n1} & x\_{n2} & \ldots & x\_{np} \\\\
\end{bmatrix} \\\\
\boldsymbol{\varepsilon} &= \begin{bmatrix}
\varepsilon\_1 \\\\
\varepsilon\_2 \\\\
\vdots \\\\
\varepsilon\_n
\end{bmatrix},
\wvec = \begin{bmatrix}
w\_1 \\\\
w\_2 \\\\
\vdots \\\\
w\_n
\end{bmatrix}
\end{align\*}\\]

<aside title="Ordering of Features">

Make note of the ordering of the features and the added bias bit in the features. The bias bit allows the linear equation to be affine (i.e. change the intersection of the decision plane). Each row is now an example, although we usually assume examples to be column vectors. This can be easily re-written, but it is a choice made likely because \`c\` (and many linear algebra packages) is row-major.

</aside>

We should also note that there are several assumptions that are taken on when using linear regression:

1.  **Independence**: This is such a common assumption throughout statistics. This means all the data in our design matrix are sampled from the underlying distribution independently.
2.  **Normal Distribution**: The data is distributed according to \\(y\_i \sim \mathcal{N}(\xvec\_i^\trans \wvec, \sigma^2)\\)
3.  (**homoscedasticity**) where the variance of the distribution \\(\sigma^2\\) is independent of the features or targets
4.  and the expectation of the target has a **linear relationship** with the features \\(\expected[y\_i] = \xvec\_i^\trans \wvec\\).
5.  No or very little **multicolinearity**: This means there is no exact relationship amongst "exploratory" variables, or the columns of the design matrix are not very correlated.


## Ordinary Least Squares {#ordinary-least-squares}

The most commonly used technique is that of linear least squares. This procedure finds the global minima of the objective function

\begin{align\*}
L(D, \wvec) &= \lVert \Xmat\wvec - \yvec \rVert\_2^2 \\\\
            &= (\Xmat\wvec - \yvec)^\trans (\Xmat\wvec - \yvec) \\\\
            &= \yvec^\trans\yvec - \yvec^\trans\Xmat\wvec - \wvec^\trans\Xmat^\trans\yvec + \wvec^\trans\Xmat^\trans\Xmat\wvec
\end{align\*}

Now taking the derivative and setting to zero we can find the global minimum at
\\[\wvec = (\Xmat^\trans \Xmat)^\inv \Xmat^\trans \yvec.\\]

With the condition that \\(\Xmat^\trans\Xmat\\) is not singular (i.e. the determinant is \\(0\\)).


### [Maximum Likelihood Estimation]({{< relref "maximum_likelihood_estimation.md" >}}) Derivation {#maximum-likelihood-estimation--maximum-likelihood-estimation-dot-md--derivation}

A natural question is "why should we minimize the MSE?" Where does this loss function come from? The Ordinary Least Squares solution is an excellent example of the application of [Maximum Likelihood Estimation]({{< relref "maximum_likelihood_estimation.md" >}}) with a gaussian distribution!

More exactly, lets start with the following distribution assumption on the targets
\\[y\_i \sim \mathcal{N}(x\_i^\trans w, \sigma^2).\\]

We want to maximize the likelihood of our target variable

\\[\prob[Y | X] &= \frac{1}{\sqrt{2\pi\sigma^2}} e^{\frac{\lVert Y - X^\trans \wvec \rVert^2}{2\sigma^2}}\\]
