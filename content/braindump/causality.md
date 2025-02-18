+++
title = "Causality"
author = ["Matthew Schlegel"]
lastmod = 2023-03-20T13:16:09-06:00
slug = "causality"
tags = ["Causality"]
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
: [Statistics]({{< relref "statistics.md" >}}), [Machine Learning]({{< relref "machine_learning.md" >}}), [AI]({{< relref "artificial_intelligence.md" >}})

This note will talk about the [Statistics]({{< relref "statistics.md" >}}) and [AI]({{< relref "artificial_intelligence.md" >}}) notions of causality. This will also host as a place to link to various resources and notes on these resources.


## Common Cause principle {#common-cause-principle}

It is well known that statistical properties alone do not determine causal structures.

<a id="figure--fig:reichenbach-cpp-fig"></a>

{{< figure src="/ox-hugo/reichenbach_ccp_fig.png" caption="<span class=\"figure-number\">Figure 1: </span>Reichenbach's common cause principle establishes a link between statistical properties and causal structures. A statistical dependence between two observables \\(X\\) and \\(Y\\) indicates taht they are caused by a (potentially new) variable \\(Z\\). In the figures cause is denoted through arrows." >}}

<div class="principle">

<div class="title">

Reichenbach's common cause principle:

</div>

If two random variables X and Y are statistically dependent, then there exists a third variable Z that causally influences both. (As a special case, Z may coincide with either X or Y.) Furthermore, this variable Z screens X and Y from each other in the sense that given Z, they become independent.

</div>

While this principle lays out a primal causal model, estimating such a model from data (especially if the data isn't [causally sufficient](#causal-sufficiency)) is extremely difficult and in many cases the model is not identifiable. While this should give us pause into the motivations of using causality in machine learning, making assumptions about the data generation process without hard assumptions on the agent's used internal [Causal Model](#causal-model) might produce powerful techniques or insights into designing algorithms. This direction might also provide groundwork for understanding when problems in perception are hopeless (<a href="#citeproc_bib_item_3">Scholkopf et al. 2012</a>). With this in mind we will cautiously move forward.


## Terms and special cases {#terms-and-special-cases}


### Disentangled model {#disentangled-model}

<https://arxiv.org/abs/2102.11107>


### Independent Causal Mechanisms Principle {#independent-causal-mechanisms-principle}


### Markov Factorizations {#markov-factorizations}


### Domain adaptation {#domain-adaptation}


### Classes of Causal models {#classes-of-causal-models}


### Causal hierarchy {#causal-hierarchy}


## Some assumptions for tractability {#some-assumptions-for-tractability}

These are defined under a simple functional causal model where \\(C\\) is a cause variable (with id noise \\(N\_C\\)), the function \\(\psi\\) is a deterministic mechanism, and \\(E = \psi(C, N\_E)\\) with \\(N\_E\\) is independent noise.


### Causal Sufficiency {#causal-sufficiency}

Assuming two independent noise variables \\(N\_C\\) and \\(N\_E\\) with random variables with distributions \\(P(N\_C)\\) and \\(P(N\_E)\\). The function \\(\phi\\) and the noise \\(N\_E\\) jointly determine \\(P(E|C)\\) via \\(E=\phi(C, N\_E)\\). This conditional is thought as the mechanism transforming cause \\(C\\) into effect \\(E\\).


### Independence of mechanism and input {#independence-of-mechanism-and-input}

The mechanism \\(\psi\\) is independent of the distribution of the cause.


### Richness of functional causal models {#richness-of-functional-causal-models}

Two-variable functional causal models are so "rich" that the causal direction cannot be inferred.


### Additive noise models {#additive-noise-models}

The additive noise model assumes for some function \\(\phi\\)

\\[ E = \phi( C) + N\_E \\]

The importance of this is that under usual conditions (i.e. if \\(\phi\\) is linear and \\(N\_E\\) was gaussian), two real-valued random variables X and Y can be fit by an ANM model in at most one direction (which is considered the causal direction).


### The Causal Markov condition {#the-causal-markov-condition}

Let \\(G\\) be a causal graph with vertices \\(\mathbf{V}\\) and \\(P\\) be a probability distribution over the vertices in \\(\mathbf{V}\\) generated by the causal structure represented by \\(G\\). \\(G\\) and \\(P\\) satisfy the causal markov condition if and only if for every \\(W \in \mathbf{V}\\), \\(W\\) is independent of \\(V(\text{\bf Descendants}(W) \cup \text{\bf Parents}(W))\\) given \\(\text{\bf Parents}(W)\\).


### The Causal Minimality Condition {#the-causal-minimality-condition}


### The Faithfulness Condition {#the-faithfulness-condition}


## Causal Model {#causal-model}


## As it relates to time series {#as-it-relates-to-time-series}


### Granger Causality {#granger-causality}


## Questions {#questions}


### Inferring the causal model from data. {#inferring-the-causal-model-from-data-dot}

Say we observe the data from the toy examples in inference's blog. How do you disentangle this to find the causal mechanisms? Are you able to run something through the function \\(\phi\\)? This seem unrealistic, especially if you _just_ have the data...


### Counterfactuals aren't testable {#counterfactuals-aren-t-testable}

If we are using a causal model to build some type of way to do counterfactual reasoning, how can we measure performance of models? In toy domains it is easy to do generate the correct distributions, but my time in RL has taught me that nothing is so simple when moving beyond toy problems. (i.e. distribution shifts can have major implications for the space the agent is in vs where it has seen before). Acting in the world begets distributional change, which effects the original problem. Does causal inference reason about these distributional shifts? What are the knock on effects?


### Inferring which causal model is correct from data {#inferring-which-causal-model-is-correct-from-data}

Given the toy examples and two causal models, can we infer which model is correct given the observed data. I suspect the answer to this is no, and we need to do interventions to uncover the actual causal model. But then I'm confused by the motivation. We are motivated to learn the causal structure of a problem w/o being able to do A/B testing... If we can't uncover the causal structure w/o intervention and A/B testing, then what is the point of causal inference?

Apparently this can be done w/ additive noise models and nonlinear causal relationships with an extremely simple mechanism described by (<a href="#citeproc_bib_item_1">Hoyer et al. 2009</a>). (i.e. do n regressions and check the causal relationship based on the correlation with the resulting irreducible error).


### Is the independence of mechanism and input a reasonable assumption for learning systems? {#is-the-independence-of-mechanism-and-input-a-reasonable-assumption-for-learning-systems}

I'm reminded of weapons of math destruction. Can we assume the underlying mechanisms for generating effects are independent of the distributions we use? I guess you can always separate out the different functions for different variables, i.e. instead of \\(C \rightarrow\_\psi E\\) you have \\((C\_1, C\_2, C\_3, \ldots) \rightarrow\_\psi E\\). So in this instance we will have a multi-input causal structure.


### Is the restriction to non-linear w/ additive gaussian noise true, or is it just invertability of the causal mechanism? {#is-the-restriction-to-non-linear-w-additive-gaussian-noise-true-or-is-it-just-invertability-of-the-causal-mechanism}


### Can we infer between various causal graphs with un-seen latent causes? {#can-we-infer-between-various-causal-graphs-with-un-seen-latent-causes}


### How does the causal inference in (<a href="#citeproc_bib_item_1">Hoyer et al. 2009</a>) depend on model performance? {#how-does-the-causal-inference-in--depend-on-model-performance}


###  {#d41d8c}


## Causal State Representations {#causal-state-representations}

-   (<a href="#citeproc_bib_item_4">Zhang et al. 2021</a>)


## Reading list {#reading-list}


### Causal state representations {#causal-state-representations}

<https://arxiv.org/pdf/1906.10437.pdf>


### Learning Causal State Representations of Partially Observable Environments {#learning-causal-state-representations-of-partially-observable-environments}

<https://arxiv.org/abs/2102.11107>


### Causal Effect Identifiability under Partial-Observability {#causal-effect-identifiability-under-partial-observability}

<http://proceedings.mlr.press/v119/lee20a.html>


### <https://arxiv.org/abs/2106.04619> {#https-arxiv-dot-org-abs-2106-dot-04619}


### Nonlinear causal discovery with additive noise models {#nonlinear-causal-discovery-with-additive-noise-models}

<https://papers.nips.cc/paper/2008/file/f7664060cc52bc6f3d620bcedc94a4b6-Paper.pdf>


### Granger Causality {#granger-causality}


### (<a href="#citeproc_bib_item_2">Scholkopf 2019</a>) {#f8c6c3}


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Hoyer, Patrik, Dominik Janzing, Joris M Mooij, Jonas Peters, and Bernhard Schölkopf. 2009. “Nonlinear Causal Discovery with Additive Noise Models.” In <i>Advances in Neural Information Processing Systems</i>. Curran Associates, Inc.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Scholkopf, Bernhard. 2019. “Causality for Machine Learning.” <i>arXiv:1911.10500 [Cs, Stat]</i>. <a href="https://arxiv.org/abs/1911.10500">https://arxiv.org/abs/1911.10500</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Scholkopf, Bernhard, Dominik Janzing, Jonas Peters, Eleni Sgouritsa, Kun Zhang, and Joris M Mooij. 2012. “On Causal and Anticausal Learning.” In <i>ICML</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>Zhang, Amy, Zachary C. Lipton, Luis Pineda, Kamyar Azizzadenesheli, Anima Anandkumar, Laurent Itti, Joelle Pineau, and Tommaso Furlanello. 2021. “Learning Causal State Representations of Partially Observable Environments.” <i>arXiv:1906.10437 [Cs, Stat]</i>. <a href="https://arxiv.org/abs/1906.10437">https://arxiv.org/abs/1906.10437</a>.</div>
</div>
