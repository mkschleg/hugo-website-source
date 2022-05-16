+++
title = "mnih2014: Recurrent Models of Visual Attention"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:28-06:00
slug = "mnih2014"
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
: [Perception]({{<relref "perception.md#" >}})

source
: <http://papers.nips.cc/paper/5542-recurrent-models-of-visual-attention>

authors
: Mnih, V., Heess, N., Graves, A., & kavukcuoglu, koray

year
: 2014

The authors propose a model for visual perception in machine learning combining a sequence based learning scheme modeled more closely after how the retina works. This model has several benefits:

1.  The number of parameters and the amount of computation can be controlled independently of the size of the input images.
2.  The model is able to ignore clutter present in the image more readily than a traditional convolutional network.

They show in their experiments that the recurrent attention model (RAM) outperforms a traditional convolutional architecture when controlling for the number of parameters on difficult object classification tasks.


## Model {#model}

We first describe the architecture and inference procedure the model is working with and then the training procedure.


### Architecture and Inference {#architecture-and-inference}

**Inputs:**
The agent receives an observation from the environment in the form of an image, which the agent can get a bandwidth limited subsample from \\(\rho(\xvec\_t, \lvec\_{t-1})\\) around location \\(l\_{t-1}\\) which is chosen by the network. This region is formed similar to the focal point of the retina where the central region is high resolution with progressively  lower resolution towards the edges. This is then passed through what is called the "glimpse network" which encodes the pixels in a feature vector \\(\gvec\_t = f\_g(\xvec\_t, \lvec\_{t-1}; \theta\_g)\\).

**Internal State:**
The agent maintains an internal state summarizing the history of information from the glimpse network. This is implemented here as a recurrent neural network (e.g. LSTMs) with state update \\(\hvec\_t = f\_h(\hvec\_{t-1}, \gvec\_t; \theta\_h)\\).

**Actions**:
There are two action sets and thus two policy networks deciding what actions to take at a given environment step. The first is the location in the image the agent will get a glimpse of \\(l\_t \sim p(\cdot| f\_l(\hvec\_t; \theta\_l))\\), and the actions which effect the state of the world \\(a\_t \sim p(\cdot | f\_a(\hvec\_t; \theta\_a))\\)

**Rewards**:
The rewards structure is dictated by the environment in the usual RL way and is usually sparse. They define the rewards for object recognition if the object is classified correctly after T (set a priori) steps.


### Training {#training}

The network is trained through the REINFORCE algorithm with a baseline of the average reward <sup id="f92357491a8e0e2eb96e86e338e23324"><a href="#sutton2000" title="@incollection{sutton2000,
  title = {Policy {{Gradient Methods}} for {{Reinforcement Learning}} with {{Function Approximation}}},
  booktitle = {Advances in {{Neural Information Processing Systems}} 12},
  author = {Sutton, Richard S and McAllester, David A. and Singh, Satinder P. and Mansour, Yishay},
  editor = {Solla, S. A. and Leen, T. K. and M{\u}ller, K.},
  year = {2000},
  publisher = {{MIT Press}}
}">sutton2000</a></sup>. They also define a hybrid supervised loss for the object classification tasks.


## References {#references}


# Bibliography
<a id="sutton2000"></a>[sutton2000] @incollectionsutton2000,
  title = Policy Gradient Methods for Reinforcement Learning with Function Approximation,
  booktitle = Advances in Neural Information Processing Systems 12,
  author = Sutton, Richard S and McAllester, David A. and Singh, Satinder P. and Mansour, Yishay,
  editor = Solla, S. A. and Leen, T. K. and M\"uller, K.,
  year = 2000,
  publisher = MIT Press
 [↩](#f92357491a8e0e2eb96e86e338e23324)
