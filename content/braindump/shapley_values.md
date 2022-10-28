+++
title = "Shapley Values"
author = ["Matthew Schlegel"]
lastmod = 2022-10-27T20:20:56-06:00
slug = "shapley_values"
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
\newcommand{\thetavec}{\boldsymbol{\theta}}
\newcommand{\phivec}{\boldsymbol{\phi}}
\newcommand{\muvec}{\boldsymbol{\mu}}
\newcommand{\sigmavec}{\boldsymbol{\sigma}}
\newcommand{\jacobian}{\mathbf{J}}
\newcommand{\ind}{\perp\!\!\!\!\perp}
\newcommand{\bigoh}{\text{O}}
\\)


## <span class="org-todo done DONE">DONE</span> What are shapley values? {#what-are-shapley-values}

Shapley values are a solution for a coalitional game. Specifically, they assign a value or payout according to the a player's contribution to the overall teams win/objective/yada.

For a linear function:

\\[\hat{f}(x) = \eta + \sum\_{i=1}^N \beta\_i x\_i\\]

Where \\(x\_i\\) are the features and \\(\beta\_i\\) are the weights of the linear function. The contribution of the $j$-th feature from instance \\(\mathbf{x}\in\mathcal{X}\\) is

\\[\phi\_j(\mathbf{x}) = \beta\_j (\mathbf{x}\_j - \expected[X\_j])\\].

for more general functions, we can't rule out interactions between different features in the function and thus must effectively marginalize over these interactions.

    \begin{align\*}
\phi\_j(val) &= \sum\_{S\subset\\{1, \ldots, p\\}/\\{j\\}} \frac{|S|! (p - |S| - 1)!}{p!} (val(S\cup\\{j\\}) - val(S)) \\\\
val\_x(S) &= \int \hat{f}(\mathbf{x}) d\mathbb{P}\_{X \notin S} - \expected[\hat{f}(\mathbf{x})]
    \end{align\*}


### (<a href="#citeproc_bib_item_4">Molnar, n.d.</a>) {#7c43a8}


### (NO_ITEM_DATA:lundberg) {#no-item-data-lundberg}


### (<a href="#citeproc_bib_item_6">Singal, Michailidis, and Ng 2021</a>) {#7260c4}


### (<a href="#citeproc_bib_item_2">Heskes et al. 2020</a>) {#54614a}


### (<a href="#citeproc_bib_item_3">Ma and Tourani 2020</a>) {#b588ec}

Prove that blindly using shapley values to identify/interpret/explain a model is not appropriate. Specifically, they provde two counter examples where they show the important features aren't guaranteed to have the largest shapley value (as compared to other features), and that the sum of SVs also don't correspond directly with the intuitive assumption.


## <span class="org-todo done DONE">DONE</span> How do we estimate Shapley Values? {#how-do-we-estimate-shapley-values}


### (<a href="#citeproc_bib_item_8">Strumbelj and Kononenko 2014</a>) {#5d9820}

A monte carlo method which approximates the shapley value as

\\[\phi\_i (x) = \frac{1}{M} \sum\_{m=1}^M \hat{f}(x\_{+j}) - \hat{f}(x\_{-j}) \\]

where \\(x\_{+j} = (x\_1, \ldtos, x\_{j-1}, x\_j, z\_{j+1}, \ldots)\\) and \\(x\_{-j} = (x\_1, \ldtos, x\_{j-1}, z\_j, z\_{j+1}, \ldots)\\). \\(z\\) is another instance sampled from the dataset. The order of features is randomly ordered.


### (<a href="#citeproc_bib_item_7">Song, Nelson, and Staum 2016</a>) {#0884c8}

The Shapley effect results in the same value as the Shapley value, but gives a different direction for optimization. To measure the global sensitivity of a function according to a set of features you can calculate the value:

\\[ v\_i = \sum\_{\mathcal{J}\subset\mathcal{k}\\\\\{i\\}} \frac{(k - |\mathcal{J}| - 1)! |\mathcal{J}|!}{k!} (c(P\_i(\pi) \cum {i}) - c(P\_i(\pi)))\\]

There are two cost/value functions \\(c\\) one can consider when calculating the global sensitivity of a function wrt to a set of features. The cost measures the variance of Y caused by the uncertainty of the inputs in \\(\mathcal{J}\\). The first (considered by (<a href="#citeproc_bib_item_5">Owen 2014</a>)) is

\\[\tilde{c}(\mathcal{J}) = \text{Var}[\text{E}[Y | \mathbf{X}\_\mathcal{J}]].\\]

Another choice is

\\[c(\mathcal{J}) = \text{E}[\text{Var}[Y|\mathbf{-\mathcal{J}}]]\\]

where \\(\mathbf{X}{-\mathcal{J}} = \mathbf{X}\_{K\\\J}\\).

While both costs result in the same values \\(v\_i\\), the resulting estimators are different.

The question is how does this effect the estimator in both bias and sample efficiency.


## Independent Shapley Values {#independent-shapley-values}

ISV is the style of shapley value introduced above. The empty coalition is the background input.


## <span class="org-todo todo TODO">TODO</span> Conditional Shapley Values {#conditional-shapley-values}


## <span class="org-todo todo TODO">TODO</span> Asymetric Shapley Values {#asymetric-shapley-values}

Asymetric shapley values may be what we want in the bandit case. The question is does knowing the ordering of ASVs give us the minimal intervention set?
(<a href="#citeproc_bib_item_1">Frye et al. 2021</a>)


## Recursive Shapley Values {#recursive-shapley-values}

(<a href="#citeproc_bib_item_6">Singal, Michailidis, and Ng 2021</a>)


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Frye, Christopher, Damien de Mijolla, Tom Begley, Laurence Cowton, Megan Stanley, and Ilya Feige. 2021. “Shapley Explainability on the Data Manifold.” <i>arXiv:2006.01272 [Cs, Stat]</i>. <a href="https://arxiv.org/abs/2006.01272">https://arxiv.org/abs/2006.01272</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Heskes, Tom, Evi Sijben, Ioan Gabriel Bucur, and Tom Claassen. 2020. “Causal Shapley Values: Exploiting Causal Knowledge to Explain Individual Predictions of Complex Models.” <i>arXiv:2011.01625 [Cs]</i>. <a href="https://arxiv.org/abs/2011.01625">https://arxiv.org/abs/2011.01625</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Ma, Sisi, and Roshan Tourani. 2020. “Predictive and Causal Implications of Using Shapley Value for Model Interpretation.” In <i>Proceedings of the 2020 KDD Workshop on Causal Discovery</i>. PMLR.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>Molnar, Christoph. n.d. <i>9.5 Shapley Values | Interpretable Machine Learning</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>Owen, Art B. 2014. “Sobol’ Indices and Shapley Value.” <i>SIAM/ASA Journal on Uncertainty Quantification</i>. Society for Industrial and Applied Mathematics.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_6"></a>Singal, Raghav, George Michailidis, and Hoiyi Ng. 2021. “Flow-Based Attribution in Graphical Models: A Recursive Shapley Approach.” SSRN Scholarly Paper. Rochester, NY: Social Science Research Network.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_7"></a>Song, Eunhye, Barry L. Nelson, and Jeremy Staum. 2016. “Shapley Effects for Global Sensitivity Analysis: Theory and Computation.” <i>SIAM/ASA Journal on Uncertainty Quantification</i>. Society for Industrial and Applied Mathematics.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_8"></a>Strumbelj, Erik, and Igor Kononenko. 2014. “Explaining Prediction Models and Individual Predictions with Feature Contributions.” <i>Knowledge and Information Systems</i>.</div>
  <div class="csl-entry">NO_ITEM_DATA:lundberg</div>
</div>
