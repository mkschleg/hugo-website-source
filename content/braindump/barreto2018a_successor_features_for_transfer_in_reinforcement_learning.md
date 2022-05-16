+++
title = "barreto2018a: Successor Features for Transfer in Reinforcement Learning"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:10-06:00
slug = "barreto2018a"
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
: [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}})

source
: <https://arxiv.org/abs/1606.05312>

authors
: Barreto, Andr\\'e, Dabney, W., Munos, R\\'emi, Hunt, J. J., Schaul, T., van Hasselt, Hado, & Silver, D.

year
: 2018

The two main ideas presented in this paper:

-   Successor features are an extension of <sup id="bc5263c9f3dd76d28c158c06782b4407"><a href="#dayan1993" title="Dayan, Improving {{Generalization}} for {{Temporal Difference Learning}}: {{The Successor Representation}}, {Neural Computation}, v(), (1993).">dayan1993</a></sup> Successor Representations to the non-tabular setting.
-   General Policy Improvement, a principled way to do [Policy Improvement]({{<relref "policy_improvement.md#" >}}) when you are learning multiple policies.

These ideas are presented to do transfer in [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}}).


## Successor Features {#successor-features}

The main assumption made to construct the successor features is the one-step reward must be able to be modeled as:
\\[ r(s,a,s^\prime) = \phivec(s, a, s^\prime)^\trans \wvec \\]

where \\(\wvec\\) is a learned vector. If this is the case, we can rewrite the state-action value function as

\begin{align\*}
Q^\pi(s, a) &= \expected^\pi [ r\_{t+1} + \gamma\_{t+1} r\_{t+2} + \ldots | S\_t = s, A\_t = a] \\\\\\
            &= \expected^\pi [ \phivec\_{t+1}^\trans \wvec + \gamma\_{t+1} \phivec\_{t+2}^\trans \wvec + \ldots | S\_t = s, A\_t = a] \\\\\\
            &= \expected^\pi [\sum\_{i=t}^\infty (\prod^i\_{j=t+1} \gamma\_{j+1}) \phi\_{i+1}] ^\trans \wvec = \psi^{\pi, \gamma}(s,a)
\end{align\*}

With the successor feature vector \\(\psi^{\pi, \gamma}(s,a)\\), we can transfer to new cumulant (or reward) specs readily. We just need to learn the new one-step reward model vector \\(\wvec\\).


## GPI {#gpi}

GPI extends the usual [Policy Improvement]({{<relref "policy_improvement.md#" >}}) theorem to the case when multiple policies are being learned simultaneously. The main idea is that if you have a collection of policies encoded as state-action value functions such that \\(|Q^{\pi\_i}(s,a) - \tilde{Q}^{\pi\_i}(s,a)| \leq \epsilon\\), and define your acting policy as \\(\pi(s) \in \argmax\_{a} \max\_{i} \tilde{Q}^{\pi\_i}(s, a)\\) then
\\[Q^{\pi}(s,a) \geq \max\_i Q^{\pi\_i}(s, a) - \frac{2}{1-\gamma}\epsilon\\].

This is then applied to transfer when using successor features.


## Four Rooms Enivronment {#four-rooms-enivronment}


## References {#references}


# Bibliography
<a id="dayan1993"></a>[dayan1993] Dayan, Improving Generalization for Temporal Difference Learning: The Successor Representation, <i>Neural Computation</i>,  (1993). [↩](#bc5263c9f3dd76d28c158c06782b4407)
