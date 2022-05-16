+++
title = "chung2014: Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:14-06:00
slug = "chung2014"
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
: [Recurrent Neural Network]({{<relref "recurrent_neural_network.md#" >}}), [Machine Learning]({{<relref "machine_learning.md#" >}})

source
: [Paper](https://arxiv.org/abs/1412.3555)

authors
: Chung, J., Gulcehre, C., Cho, K., & Bengio, Y.

year
: 2014

This paper does an empirical evaluation of several recurrent gates including [LSTM]({{<relref "lstm.md#" >}})s <sup id="c59a89800a027b3aa9da101668e63284"><a href="#hochreiter1997" title="Hochreiter \&amp; Urgen Schmidhuber, {{LONG SHORT}}-{{TERM MEMORY}}, {Neural Computation}, v(), (1997).">hochreiter1997</a></sup>, [GRU]({{<relref "lstm.md#" >}}) <sup id="95f0c4256ce447646943f9e9ec548f84"><a href="#cho2014" title="Cho, van Merri\enboer, Bahdanau \&amp; Bengio, On the {{Properties}} of {{Neural Machine Translation}}: {{Encoder}}\textendash{{Decoder Approaches}}, in in: {Proceedings of {{SSST}}-8, {{Eighth Workshop}} on {{Syntax}}, {{Semantics}} and {{Structure}} in {{Statistical Translation}}}, edited by {Association for Computational Linguistics} (2014)">cho2014</a></sup>, and Vanilla [RNN]({{<relref "recurrent_neural_network.md#" >}})s. The paper also provides descriptions for the different cells tested and a nice high level description of the generative model employed by RNNs.

**Results**

-   They find that GRUs are competitive to LSTMs on the tasks they tested (i.e. Music Datasets and Ubisoft Datasets).
-   GRUs Needed less Wall time as well to learn adequately, and were competitive in terms of number of epochs (as compared w/ the LSTMs they are much better in walltime).
