+++
title = "Causality"
author = ["Matthew Schlegel"]
lastmod = 2021-10-11T11:31:35-04:00
slug = "causality"
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
\newcommand{\ind}{\perp\!\!\!\!\perp}
\\)

This note will talk about the [Statistics]({{<relref "statistics.md#" >}}) and [AI]({{<relref "artificial_intelligence.md#" >}}) notions of causality. This will also host as a place to link to various resources and notes on these resources.


## Common Cause principle {#common-cause-principle}

It is well known that statistical properties alone do not determine causal structures.

<a id="org792ea8c"></a>

{{< figure src="/ox-hugo/reichenbach_ccp_fig.png" caption="Figure 1: Reichenbach's common cause principle establishes a link between statistical properties and causal structures. A statistical dependence between two observables \\(X\\) and \\(Y\\) indicates taht they are caused by a (potentially new) variable \\(Z\\). In the figures cause is denoted through arrows." >}}

<div class="principle">
  <div></div>

<div class="title">
  <div></div>

Reichenbach's common cause principle:

</div>

If two random variables X and Y are statistically dependent, then there exists a third variable Z that causally influences both. (As a special case, Z may coincide with either X or Y.) Furthermore, this variable Z screens X and Y from each other in the sense that given Z, they become independent.

</div>

While this principle lays out a primal causal model, estimating such a model from data (especially if the data isn't [causally sufficient](#causal-sufficiency)) is extremely difficult and in many cases the model is not identifiable. While this should give us pause into the motivations of using causality in machine learning, making assumptions about the data generation process without hard assumptions on the agent's used internal [Causal Model](#causal-model) might produce powerful techniques or insights into designing algorithms. This direction might also provide groundwork for understanding when problems in perception are hopeless <sup id="b00c0ffe2b498797f6925d0886d290da"><a href="#scholkopf" title="Sch\olkopf, Janzing, Peters, Sgouritsa, Zhang \&amp; Mooij, On {{Causal}} and {{Anticausal Learning}}, v(), ().">scholkopf</a></sup>. With this in mind we will cautiously move forward.


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

Apparently this can be done w/ additive noise models and nonlinear causal relationships with an extremely simple mechanism described by <sup id="a94adfeafb37f4427d6434d2810495ef"><a href="#hoyer2009" title="Hoyer, Janzing, Mooij, Peters \&amp; Sch\olkopf, Nonlinear Causal Discovery with Additive Noise Models, in in: {Advances in {{Neural Information Processing Systems}}}, edited by {Curran Associates, Inc.} (2009)">hoyer2009</a></sup>. (i.e. do n regressions and check the causal relationship based on the correlation with the resulting irreducible error).


### Is the independence of mechanism and input a reasonable assumption for learning systems? {#is-the-independence-of-mechanism-and-input-a-reasonable-assumption-for-learning-systems}

I'm reminded of weapons of math destruction. Can we assume the underlying mechanisms for generating effects are independent of the distributions we use? I guess you can always separate out the different functions for different variables, i.e. instead of \\(C \rightarrow\_\psi E\\) you have \\((C\_1, C\_2, C\_3, \ldots) \rightarrow\_\psi E\\). So in this instance we will have a multi-input causal structure.


### Is the restriction to non-linear w/ additive gaussian noise true, or is it just invertability of the causal mechanism? {#is-the-restriction-to-non-linear-w-additive-gaussian-noise-true-or-is-it-just-invertability-of-the-causal-mechanism}


### Can we infer between various causal graphs with un-seen latent causes? {#can-we-infer-between-various-causal-graphs-with-un-seen-latent-causes}


### How does the causal inference in <sup id="a94adfeafb37f4427d6434d2810495ef"><a href="#hoyer2009" title="Hoyer, Janzing, Mooij, Peters \&amp; Sch\olkopf, Nonlinear Causal Discovery with Additive Noise Models, in in: {Advances in {{Neural Information Processing Systems}}}, edited by {Curran Associates, Inc.} (2009)">hoyer2009</a></sup> depend on model performance? {#how-does-the-causal-inference-in-depend-on-model-performance}


###  {#}


## Causal State Representations {#causal-state-representations}

-   <sup id="cf8e9083815e9b7d8318497cd8335abc"><a href="#zhang2021" title="Zhang, Lipton, Pineda, Azizzadenesheli, Anandkumar, Itti, Pineau \&amp; Furlanello, Learning {{Causal State Representations}} of {{Partially Observable Environments}}, {arXiv:1906.10437 [cs, stat]}, v(), (2021).">zhang2021</a></sup>


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


### <sup id="ddc8f7a086caeb6d5bd95f9b7cdc5334"><a href="#scholkopf2019" title="Scholkopf, Causality for {{Machine Learning}}, {arXiv:1911.10500 [cs, stat]}, v(), (2019).">scholkopf2019</a></sup> {#}


## References {#references}


# Bibliography
<a id="scholkopf"></a>[scholkopf] Sch\"olkopf, Janzing, Peters, Sgouritsa, Zhang & Mooij, On Causal and Anticausal Learning, <i></i>,  . [↩](#b00c0ffe2b498797f6925d0886d290da)

<a id="hoyer2009"></a>[hoyer2009] Hoyer, Janzing, Mooij, Peters & Sch\"olkopf, Nonlinear Causal Discovery with Additive Noise Models, in in: Advances in Neural Information Processing Systems, edited by Curran Associates, Inc. (2009) [↩](#a94adfeafb37f4427d6434d2810495ef)

<a id="zhang2021"></a>[zhang2021] Zhang, Lipton, Pineda, Azizzadenesheli, Anandkumar, Itti, Pineau & Furlanello, Learning Causal State Representations of Partially Observable Environments, <i>arXiv:1906.10437 [cs, stat]</i>,  (2021). [↩](#cf8e9083815e9b7d8318497cd8335abc)

<a id="scholkopf2019"></a>[scholkopf2019] Scholkopf, Causality for Machine Learning, <i>arXiv:1911.10500 [cs, stat]</i>,  (2019). [↩](#ddc8f7a086caeb6d5bd95f9b7cdc5334)
