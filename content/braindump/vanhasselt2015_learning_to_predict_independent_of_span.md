+++
title = "vanhasselt2015: Learning to Predict Independent of Span"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:40-06:00
slug = "vanhasselt2015"
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
: [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}}), [Theory]({{<relref "theory.md#" >}}), [General Value Functions]({{<relref "general_value_functions.md#" >}})

source
: [paper](https://arxiv.org/abs/1508.04582)

authors
: van Hasselt, Hado, & Sutton, R. S.

year
: 2015

This paper is dedicated to deriving algorithms which learning to make prediction "independent of span"

**Span**: The _span_ of a multi-step prediction is the number of steps elapsing between when the prediction is made and when its target or ideal value is known.
For example:

-   If we make predictions on each day and predict the stock market's price in 30 days, then the span=30
-   If we make predictions on every hour and the prediction is made in 30 days, the span=24 \* 30=720.

The span of a prediction may also very over time. The prediction made in 30 days has a shorter span than the prediction made several months into the future. We will consider the overall span of the prediction to be the maximal span. This can occur if predictions are made a long time-scales or with a short time between predictions.

**Main Goal**: This paper focuses on the construction of learning algorithms whose computational complexity per time step (in both time and memory) is constant (i.e. doesn't scale with time) and independent of span.

<aside>
  <aside></aside>

For much of this document they discuss "trust" of a Target. And as I think more on this, the LMS rule they are deriving from is assuming Z is the perfect target for what they are trying to predict. Instead, Z should be pulled from a distribution and we need to average (or some other operation) multiple weights together to come to some reasonable algorithm. This is assuming our sequence of features will always end in a single outcome. But maybe this is a reasonable assumption? I guess given enough information in the feature vector we could say this is correct in a deterministic setting that only appears stochastic with insufficient information.

</aside>

1.  Derive a span-independent algorithm to update the prediction for single final outcome [sec:vanhasselt2015:traces](#sec:vanhasselt2015:traces)
2.  Derive span-independent updates that update the predictions _online_ towards interim targets that temporarily stand in for the final outcome [sec:vanhasselt2015:online](#sec:vanhasselt2015:online)
3.  Consider how to do these algorithms efficiently [sec:vanhasselt2015:efficiency](#sec:vanhasselt2015:efficiency)
4.  Formalize these ideas and show they lead naturally to a form of TD(\\(\lambda\\)) [sec:vanhasselt2015:tdlambda](#sec:vanhasselt2015:tdlambda)
5.  Show how to combine all prior ideas into a single algorithm [sec:vanhasselt2015:onetorulethem](#sec:vanhasselt2015:onetorulethem)
6.  Two important generalizations: cumulative returns, and soft terminations [sec:vanhasselt2015:generalizations](#sec:vanhasselt2015:generalizations)
7.  Convergence of the new algorithm [sec:vanhasselt2015:convergence](#sec:vanhasselt2015:convergence)
8.  Discussion/Conclusions [sec:vanhasselt2015:discussion](#sec:vanhasselt2015:discussion)


## Independence of span and the emergence of traces {#sec:vanhasselt2015:traces}

**Notations**:

-   \\(t\\) time step with \\(t=0\\) as the initial point
-   \\(\boldsymbol{\theta}\_t\\) for the feature vector produced at time step \\(t\\)
-   \\(Z\\) the final outcome occurring at time step \\(T\\)

Here we are considering the general case of multi-step predictions (\\(T>1\\)) where predictions are made at each time step. In the supervised learning case the predictor will only make a single prediction for the entire episode (or time sequence \\(t=0...T\\)).

-   Predictions are linear with learned weight vector at time t \\(\boldsymbol{\theta}\_t\\) and prediction at time t \\(\boldsymbol{\theta}\_t^\top \boldsymbol{\phi}\_t\\)

When the final time is reached we can make an update assuming the LMS loss function:

\\[\boldsymbol{\theta}\_{t+1} \doteq \boldsymbol{\theta}\_{t}+\alpha\_{t} \boldsymbol{\phi}\_{t}\left(Z-\boldsymbol{\phi}\_{t}^{\top} \boldsymbol{\theta}\_{t}\right), \quad t=0, \ldots, T-1\\]

This is called the _forward view_ as you have to look forward to the end of the episode to update the weight vector. All resources (memory and computation) scale with the length of the episode as you have to store each feature vector, and calculate each weight at the end of the episode.

With some careful analysis we can find a computationally spread way of dealing with this update. See paper for a fuller explanation. In the end we get to

\\[\boldsymbol{\theta}\_T=\underbrace{\mathbf{F}\_{T-1} \mathbf{F}\_{T-2} \cdots \mathbf{F}\_{0} \boldsymbol{\theta}\_{0}}\_{\dot{=} \boldsymbol{a}\_{T-1}}+\underbrace{\left(\sum\_{t=0}^{T-1} \mathbf{F}\_{T-1} \mathbf{F}\_{T-2} \cdots \mathbf{F}\_{t+1} \alpha\_{t} \phi\_{t}\right)}\_{\dot{\doteq} \boldsymbol{e}\_{T-1}} Z\\]

where \\(\mathbf{F}\_{t} \doteq \mathbf{I}-\alpha\_{t} \boldsymbol{\phi}\_{t} \boldsymbol{\phi}\_{t}^{\top}\\).

We can then define both updates to \\(\boldsymbol{a}\_t\\) and \\(\boldsymbol{e}\_t\\) in incremental terms where the eligibility vector is analogous to the conventional eligibility trace using _dutch traces_! This suggests that eligibility traces are not specific to TD learning at all; and are more fundamental to predictions over time. This span-independent algorithm is denoted as the backwards view and can be summarized as:

\begin{align}
{\mathbf{a}\_{0} \doteq \theta\_{0}, \quad \text { then } a\_{t+1} \doteq a\_{t}+\alpha\_{t} \phi\_{t}\left(0-\phi\_{t}^{\top} a\_{t}\right), \quad t=1, \ldots, T-1} \nonumber \\\\\\
{e\_{-1} \doteq 0, \quad \text { then } e\_{t} \doteq e\_{t-1}+\alpha\_{t} \phi\_{t}\left(1-\phi\_{t}^{\top} e\_{t-1}\right), \quad t=0, \ldots, T-1} \\\\\\
{\boldsymbol{\theta}\_{T} \doteq \boldsymbol{a}\_{T-1}+Z \boldsymbol{e}\_{T-1}} \nonumber
\end{align}

While the overall computation (\\(O(Tn)\\)) is still the same, the amount of memory has been significantly reduced \\(O(n)\\), meaning the memory is constant wrt the span of the prediction.


## Online Updating and the emergence of TD errors {#sec:vanhasselt2015:online}

The main thesis of this section revolves around the fact that an online algorithm cannot update it's prediction weights towards the final outcome \\(Z\\) during the episode. This is because \\(Z\\) is only available at the end of an episode. This becomes problematic when we want to make interim predictions based on what we believe the outcome could be. The main idea is to use interim targets (based on all the data available up to the horizon) denoted by \\(Z^h\\) where \\(h\\) is the timestep the target is presented to the algorithm.

<div class="note">
  <div></div>

They use the convention of

-   The superscript denoting the upper limit of the data considered available in an online update
-   The subscript is used for the time step whose prediction is being modified (i.e. the weights).

</div>

The following clarifies notation, where we use the previously defined algorithm to learn a new set of weights \\(\theta\_h^h\\) for each new interim target where \\(\theta\_T^T = \theta\_T\\).

\begin{array}{ll}
\boldsymbol{\theta}\_{0}^{h} &\doteq \boldsymbol{\theta}\_{0}, & h=0, \ldots, T \\\\\\
\boldsymbol{\theta}\_{t+1}^{h} &\doteq \boldsymbol{\theta}\_{t}^{h}+\alpha\_{t} \boldsymbol{\phi}\_{t}\left(Z^{h}-\boldsymbol{\phi}\_{t}^{\top} \boldsymbol{\theta}\_{t}^{h}\right), & t=0, \ldots, h-1, \quad h=1, \ldots, T \\\\\\
& =\mathbf{F}\_{t} \boldsymbol{\theta}\_{t}^{h}+\alpha\_{t} \boldsymbol{\phi}\_{t} Z^{h} .
\end{array}

This creates a set of all possible weights which can be written as the lower triangular matrix, where each row is the new horizon and the diagonal denotes the weights learned by the algorithm derived in [sec:vanhasselt2015:traces](#sec:vanhasselt2015:traces) for each interim target. The authors then set out to develop an algorithm which is able to traverse the diagonal without having to calculate the entire lower triangular matrix of weights. To do this they follow the same technique as in [sec:vanhasselt2015:traces](#sec:vanhasselt2015:traces): take the forward view algorithm and unroll to create the backward view variant. The resulting algorithm (by combining this unrolling and the forward view to traverse the diagonal) is

\begin{array}{ll}
\traces\_{t} &\doteq \traces\_{t-1} + \alpha\_t\phivec\_t(1-\phivec\_t^\trans \traces\_{t-1}) \quad \triangleright \traces\_{-1} \doteq \mathbf{0} \\\\\\
\thetavec\_{t+1} &\doteq \thetavec\_{t} + \traces\_t (Z^{t+1} - Z^t) + \alpha\_t \phivec\_t (Z^t - \phivec\_t^\trans\thetavec\_t), \quad t=0, \ldots, T-1
\end{array}

<div class="note">
  <div></div>

Although the backward view algorithm yields different predictions during the episode, the final weights \\(\thetavec\_T\\) is exactly the same as those computed by the conventional LMS algorithm that constituted the first, offline, forward view algorithm considered in this paper. And in fact all three algorithms they've so far developed result in the same final weights (which is the desired effect thus far).

</div>


## Unifying online and offline learning and the emergence of averaging {#sec:vanhasselt2015:efficiency}


## Bootstrapping {#sec:vanhasselt2015:tdlambda}


## Combining two notions of trust and the emergence of averaged TD(\\(\lambda\\)) {#sec:vanhasselt2015:onetorulethem}


## Generalizing to cumulative returns and soft terminations {#sec:vanhasselt2015:generalizations}


## Convergence Analysis {#sec:vanhasselt2015:convergence}


## Discussion {#sec:vanhasselt2015:discussion}

This is the discussion section
