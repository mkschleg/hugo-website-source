+++
title = "spratling2017: A review of predictive coding algorithms"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:36-06:00
slug = "spratling2017"
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
: [Hierarchical Predictive Coding]({{<relref "hierarchical_predictive_coding.md#" >}})

source
: [link](https://www.sciencedirect.com/science/article/pii/S027826261530035X?casa%5Ftoken=InNrJSl5f4QAAAAA:PBmcJF887TTbvY-o5oAjUxTxRSc2zJh8OtlXDO61erpnGmXMzlHRVeFeAVEc4Sb0ISGM%5FsYvYUg)

authors
: Spratling, M. W.

year
: 2017


## Linear Predictive Coding (digital signal processing) {#linear-predictive-coding--digital-signal-processing}

This form of predictive coding was designed for the manipulation and analysis of a continuous signal sampled discretely (i.e. a "time-series" signal). Linear predictive coding assumes that the sample at a given time-step can be predicted according to the previous n steps through a linear approximator:

\\[
x\_t \approx r\_t = w\_1 x\_{t-1} + w\_2 x\_{t-2} + \ldots + w\_n x\_{t-n}
\\]

where \\(x\_t\\) is the signal of interest at time step \\(t\\) and the vector \\(\wvec \in \reals\\) is the linear model learned through linear regression or some other algorithm to minimize the sum of squared errors of the time-series in a certain frame determined by the discrete set \\(\boldsymbol{\tau}\\)

\\[
\mathcal{L} = \sum\_{t \in \boldsymbol{\tau}} (x\_t - r\_t)^2
\\]

There are several classical time-series approaches which have been developed the learn this kind of signal (i.e. [Autocorrelation]({{<relref "autocorrelation.md#" >}})).


## Predictive Coding in the Retina {#predictive-coding-in-the-retina}

The core idea of modeling the Retinal using predictive coding is that the predictable component of the signal is removed from the signal and the residual (i.e. the error) is transmitted. This reduces the effective range of the transmitted signal allowing for more efficient transmission.

The residual error is simple
\\[
e\_t = x\_t - r\_t
\\]

While initially discussed in terms of temporal predictions, this has also been formulated for spatial prediction. This is to say the predictive local intensity value is calculated from intensity values measured at nearby locations as well as those with preceding time <sup id="d99e6ac5b4c5ec160fcf0e921d0d097c"><a href="#srinivasan1982" title="Srinivasan, Laughlin, Dubs \&amp; Horridge, Predictive Coding: A Fresh View of Inhibition in the Retina, {Proceedings of the Royal Society of London. Series B. Biological Sciences}, v(), (1982).">srinivasan1982</a></sup>.

It has been proposed that the coefficients average the intensity of light, and this average is subtracted from the retinal signals <sup id="d99e6ac5b4c5ec160fcf0e921d0d097c"><a href="#srinivasan1982" title="Srinivasan, Laughlin, Dubs \&amp; Horridge, Predictive Coding: A Fresh View of Inhibition in the Retina, {Proceedings of the Royal Society of London. Series B. Biological Sciences}, v(), (1982).">srinivasan1982</a></sup>. This is an interesting take, and quite possible for the retina, specifically in understanding the differences between low light and high light settings possibly not appearing later down stream.

The process can be thought of through the lens of redundancy reduction or said to be an [Efficient Coding]({{<relref "efficient_coding.md#" >}}).

<div class="note">
  <div></div>

If only the residual error is transmitted, then the receiver (in the case of the retina this would be the lateral geniculate nucleaus and cortex) cannot recover the components of the signal that have been removed. Redundancy is not being reduced, but entirely removed.

</div>


## Predictive Coding in the Cortex: Rao and Ballard {#predictive-coding-in-the-cortex-rao-and-ballard}

<sup id="7b979f5b998905dc446bf66499306a20"><a href="#rao1999" title="Rao \&amp; Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, {Nature Neuroscience}, v(), (1999).">rao1999</a></sup> 's model for cortical function proposes the cortex is built of several layers of predictive coding networks. Each layer implements the predictive coding algorithm described above for spatial inputs (as far as I can tell) instead of time-series inputs, although both could be used. The output of each cortical region is the residual error. The feed forward connections are believed to transmit these errors while the cortical feedback connections are predicted "causes". This hypothesizes that cortical feedback connections act to suppress information which is predicted by higher-level cortical region.

The linear version of <sup id="7b979f5b998905dc446bf66499306a20"><a href="#rao1999" title="Rao \&amp; Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, {Nature Neuroscience}, v(), (1999).">rao1999</a></sup> 's algorithm is:

\begin{align\*}
\yvec^{Si} &\leftarrow \nu \yvec^{Si} + \mu \Wmat^{Si} \evec^{Si-1} - \eta \evec^{Si} \\\\\\
\evec^{Si-1} &= \yvec^{Si-1} - \Vmat^{Si}\yvec^{Si}.
\end{align\*}

where \\(\nu\\), \\(\eta\\), and \\(\mu\\) are non-negative parameters and \\(\Wmat = \Vmat^\top\\)


## Predictive Coding in the Cortex: PredCoding/Biased Competation - DIM {#predictive-coding-in-the-cortex-predcoding-biased-competation-dim}

This is a reformulation of <sup id="7b979f5b998905dc446bf66499306a20"><a href="#rao1999" title="Rao \&amp; Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, {Nature Neuroscience}, v(), (1999).">rao1999</a></sup> 's PC model to be compatible w/ [Biased Competition]({{<relref "biased_competition.md#" >}}) theories of cortical function. Specifically,

\begin{align\*}
\evec &= \xvec \oslash (\epsilon\_2 + \Vmat \yvec) \\\\\\
\yvec &\leftarrow (\epsilon\_1 + \yvec) \otimes \Wmat\evec
\end{align\*}

This formulation solves several issues with the <sup id="7b979f5b998905dc446bf66499306a20"><a href="#rao1999" title="Rao \&amp; Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, {Nature Neuroscience}, v(), (1999).">rao1999</a></sup> proposal:

1.  No longer requires neurons be able to produce both positive and negative firing rates. In the new algorithm activations are bounded to be non-negative inherently.
2.  PC/BC-DIM is related to a particular method of performing non-negative matrix factorisation (NMF), and thus gets around the need to use gradient descent to find the coefficient values (which can be slow or unstable if \\(\mu\\) is small or large respectively). This stability and speed has enabled the development of large scale simulations containing 10s of millions of neurons and 100s of billions of connections.
3.  A different grouping of neurons which is more biologically feasible.
4.  The requirement that \\(\Wmat = \Vmat^\top\\) is related w/ the PC/BC-DIM variant.


## Predictive Coding in the Cortex: Free energy {#predictive-coding-in-the-cortex-free-energy}

This scheme is similar to <sup id="7b979f5b998905dc446bf66499306a20"><a href="#rao1999" title="Rao \&amp; Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, {Nature Neuroscience}, v(), (1999).">rao1999</a></sup>, but unlike the above algorithms the variables in the free energy model represent the statistics of the signals rather than the values of the signals. The network is thus not representing individual samples, but reconstructs the underlying probability distribution (or at least what is reconstructible given the observations).


## References {#references}


# Bibliography
<a id="srinivasan1982"></a>[srinivasan1982] Srinivasan, Laughlin, Dubs & Horridge, Predictive Coding: A Fresh View of Inhibition in the Retina, <i>Proceedings of the Royal Society of London. Series B. Biological Sciences</i>,  (1982). [↩](#d99e6ac5b4c5ec160fcf0e921d0d097c)

<a id="rao1999"></a>[rao1999] Rao & Ballard, Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects, <i>Nature Neuroscience</i>,  (1999). [↩](#7b979f5b998905dc446bf66499306a20)
