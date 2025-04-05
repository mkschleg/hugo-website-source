+++
title = "mohamed2019monte: Monte Carlo Gradient Estimation in Machine Learning"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:28:30-07:00
slug = "mohamed2019monte"
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
: [Machine Learning]({{< relref "machine_learning.md" >}})

source
: <https://arxiv.org/abs/1906.10652>

authors
: Mohamed, S., Rosca, M., Figurnov, M., &amp; Mnih, A.

year
: 2019

This paper is a broad survey of Monte Carlo gradient estimation techniques for Machine Learning. My interest in this topic is mostly from an off-policy prediction standpoint, but is a really nice general survey of these techniques.

The main goal is to compute a general probabilistic object \\(\mathcal{F}\\):

\begin{equation}
\mathcal{F}(\boldsymbol{\theta}) :=\int p(\mathbf{x} ; \boldsymbol{\theta}) f(\mathbf{x} ; \boldsymbol{\phi}) d \mathbf{x}=\mathbb{E}\_{p(\mathbf{x} ; \boldsymbol{\theta})}[f(\mathbf{x} ; \boldsymbol{\phi})]
\end{equation}

This is a _mean-value analysis_ in which a function \\(f\\) of an input variable \\(\mathbf{x}\\) with parameters \\(\mathbf{\phi}\\) is evaluated on average with respect to an input distribution \\(p(\mathbf{x};\mathbf{\theta})\\) with distributional parameters \\(\mathbf{\theta}\\).

-   \\(f\\) is the _cost_
-   \\(p(\mathbf{x};\mathbf{\theta})\\) is the _measure_

We need to learn the distributional parameters \\(\theta\\) so we take the gradient

\begin{equation}
\label{eq:mohamed2019:grad\_mva}
\boldsymbol{\eta} :=\nabla\_{\boldsymbol{\theta}} \mathcal{F}(\boldsymbol{\theta})=\nabla\_{\boldsymbol{\theta}} \mathbb{E}\_{p(\mathbf{x} ; \boldsymbol{\theta})}[f(\mathbf{x} ; \boldsymbol{\phi})]
\end{equation}

Which is the _sensitivity analysis_ of \\(\mathcal{F}\\) (the gradient of the expectation with respect to the distributional parameters). This gradient problem is difficult in general!

-   Can't evaluate the expectation in closed form
-   the integrals over \\(\mathbf{x}\\) are typically high-dimensional making quadrature ineffective
-   The gradient can be wrt high dimensional distribution parameters \\(\mathbf{\theta}\\)
-   And often \\(\mathcal{F}\\) is not differentiable.

We need efficient, accurate and parallelisable solutions that minimize the number of evaluations of the cost.

This will be organized into several sections

-   General principles
-   Estimators
-   Variance Reduction
-   Conclusions, Related work, and future directions.


## General Principles of Monte Carlo Methods {#general-principles-of-monte-carlo-methods}


### Monte Carlo Estimators {#monte-carlo-estimators}

Consider the equation <eq:mohamed2019:mean_value_analysis_problem>. This integral is often not in known in a closed form. , and not amenable to evaluation using numerical methods!

Instead we can estimate the integral using the monte-carlo method:

\begin{equation}
\overline{\mathcal{F}}\_{N}=\frac{1}{N} \sum\_{n=1}^{N} f\left(\hat{\mathbf{x}}^{(n)}\right), \text { where } \hat{\mathbf{x}}^{(n)} \sim p(\mathbf{x} ; \boldsymbol{\theta}) \text { for } n=1, \ldots, N
\end{equation}

The quantity \\(\overline{\mathcal{F}}\\) is a random variable, since it depends on a specific set of random variates (samples) \\(\\{\hat{\mathbf{x}}^{(1)} \ldots \hat{\mathbf{x}}^{(n)}\\}\\). We can repeat this many times by constructing multiple sets of the random samples.

There are four properties we will consider with a monte carlo estimator:

-   **Consitency**: Does the estimator \\(\overline{\mathcal{F}}\_{N}\\) converge to the true value of the integral as \\(N\\) (or the number of samples) increases.
-   **Unbiasedness**: If we repeat the estimation process many times, we should find that the estimate is centered on the actual value of the integral on average. For example, the Monte Carlo estimator:

    \\[ \mathbb{E}\_{p(\mathbf{x} ; \boldsymbol{\theta})}\left[\overline{\mathcal{F}}\_{N}\right]=\mathbb{E}\_{p(\mathbf{x} ; \boldsymbol{\theta})}\left[\frac{1}{N} \sum\_{n=1}^{N} f\left(\mathbf{x}^{(n)}\right)\right]=\frac{1}{N} \sum\_{n=1}^{N} \mathbb{E}\_{p(\mathbf{x} ; \boldsymbol{\theta})}\left[f\left(\mathbf{x}^{(n)}\right)\right]=\mathbb{E}\_{p(\mathbf{x} ; \boldsymbol{\theta})}[f(\mathbf{x})] \\].

-   **Minimum Variance**: We will always prefer the estimators with lower variance (given all else is the same).
    1.  The resulting gradient estimates are more accurate.
    2.  When the gradient is used for stochastic optimisation, low-variance gradients make learning more efficient (allowing for larger learning rates to be used and reducing the total number of steps to convergence).

-   **Computational efficiency**: We will always prefer an estimator that is computationally efficient (allow the expectation to be computed using the fewest number of samples).


### Stochastic Optimization {#stochastic-optimization}

The gradient found in equation <eq:mohamed2019:mean_value_analysis_problem> supports two computational tasks

1.  Explanation:
    This gradient is an useful tool to _explain_ the behavior of the probabilistic systm.
2.  Optimization:
    The key quantity need for optimization of the distributional parameters \\(\mathbf{\theta}\\).

You can consider stochastic optimisation as a loop using a simulation phase and an optimisation phase. This process is a stocastic system because the system or the environment has elements of randomness. Because of this, we will call the system for an _estimate_ of the gradient or Hessian rather than the _true_ gradient or Hessian.

If the optimisation phase is use with stochastic approximation (e.g. stochastic gradient descent) then this can be thought of as a double-stochastic optimization.


### Central role of gradient estimation {#central-role-of-gradient-estimation}

To make the problem more concrete, here are 5 areas in which these estimates are critical.

<!--list-separator-->

-  Variational Inference

    General method for approximating complex and unknown distributions by the closest distribution within a tractable family.

<!--list-separator-->

-  Reinforcement Learning

    Model-free policy search, where we learn a policy---a distribution over actions---that on average maximises the accumulation of long-term rewards. You can then learn a policy using policy gradient methods with the gradient:

    \\[\boldsymbol{\eta}=\nabla\_{\boldsymbol{\theta}} \mathbb{E}\_{p(\boldsymbol{\tau} ; \boldsymbol{\theta})}\left[\sum\_{t=0}^{T} \gamma^{t} r\left(\mathbf{s}\_{t}, \mathbf{a}\_{t}\right)\right]\\]

    which again has the form of equation <eq:mohamed2019:mean_value_analysis_problem>.

    -   **cost:** is the return over the trajectory, which is a weighted sum of rewards obtained at each time step.
    -   **measure**: is the joint distribution over states and actions \\(p(\mathbf{\tau};\mathbf{\theta})\prod\_{t=0}^{T} p\left(\mathbf{s}\_{t+1} | \mathbf{s}\_{t}, \mathbf{a}\_{t}\right) p\left(\mathbf{a}\_{t} | \mathbf{s}\_{t} ; \boldsymbol{\theta}\right)\\) which is the product of a state transition distribution and the policy distribution.

<!--list-separator-->

-  Sensitivity Analysis

    Deals with the study of problems of the form <eq:mohamed2019:grad_mva>, and asks what the sensitivity (or gradient) of an expectation is to its input parameters.

<!--list-separator-->

-  Discrete Event Systems and Queuing Theory

    This is the study of waiting systems, or queues.

<!--list-separator-->

-  Experimental Design

    Here we are interested in finding the best designs--the inputs or settings to a possibly unknown system--that result in outputs that are optimal wrt some utility or score.


## Intuitive Analysis of Gradient Estimators {#intuitive-analysis-of-gradient-estimators}

The structure of the analysis problem <eq:mohamed2019:grad_mva> directly suggests two possible computations for the gradients:

-   **Derivatives of Measure**: The gradient can be computed by differentiation of the measure \\(p(\mathbf{x};\boldsymbol{\theta})\\).
    -   Examples: score function estimator <sec:mohamed2019:score_func_est>, measure-valued gradient <sec:mohamed2019:meas_valued_grads>
-   **Derivatives of Path**: The gradient can be computed by differentiation of the cost \\(f(\mathbf{x})\\), which encodes the pathway from parameters \\(\boldsymbol{\theta}\\), through the random variable \\(\mathbf{x}\\), to the cost value.
    -   Examples: Pathwise gradient <sec:mohamed2019:pathwise_grad_est>, harmonic gradient estimators, and Malliavin-weighted estimators.

The paper then goes into some intuitive exploration of a simple problem
\\[
\eta=\nabla\_{\theta} \int \mathcal{N}\left(x | \mu, \sigma^{2}\right) f(x ; k) d x ; \quad \theta \in\\{\mu, \sigma\\} ; \quad f \in\left\\{(x-k)^{2}, \exp \left(-k x^{2}\right), \cos (k x)\right\\}
\\].

In all they find that a universal ordering is difficult to determine (and in many cases impossible). They suggest three criteria on which to judge the estimators:

-   computational cost,
-   implications on the use of differentiable and non-differentiable cost functions,
-   the change in behaviour as the cost itself changes,
-   and the availability of variance reduction techniques.


## Estimators <code>[0/3]</code> {#estimators}

This section details three estimators mentioned above.


### Score Function Gradient Estimators {#score-function-gradient-estimators}


### Pathwise Gradient Estimators {#pathwise-gradient-estimators}


### Measure-valued Gradients {#measure-valued-gradients}
