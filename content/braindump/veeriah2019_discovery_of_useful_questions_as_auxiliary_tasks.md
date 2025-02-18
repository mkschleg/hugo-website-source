+++
title = "veeriah2019discovery: Discovery of Useful Questions as Auxiliary Tasks"
author = ["Matthew Schlegel"]
lastmod = 2022-11-09T14:03:35-07:00
slug = "veeriah2019discovery"
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
: [General Value Functions]({{< relref "general_value_functions.md" >}}), [Reinforcement Learning]({{< relref "reinforcement_learning.md" >}})[Deep Reinforcement Learning]({{< relref "deep_reinforcement_learning.md" >}})

source
: [link](http://papers.nips.cc/paper/9129-discovery-of-useful-questions-as-auxiliary-tasks)

authors
: Veeriah, V., Hessel, M., Xu, Z., Rajendran, J., Lewis, R. L., Oh, J., van Hasselt, Hado P, …

year
: 2019

This paper considers how to "discover" a set of GVF questions for auxiliary tasks (<a href="#citeproc_bib_item_1">Jaderberg et al. 2017</a>) using meta-gradient descent. They consider a multi-step meta-loss function (unlike previous approaches which only consider a single step function).

They use two neural networks:

1.  The main architecture which is responsible for learning the answers to the GVF questions and learning the main task (i.e. the action-state value function or policy parameterization). This architecture takes the last i observations \\(\obs\_{t-i+1:t}\\) as inputs. Parameterized by \\(\theta\\)
2.  The question network which is responsible for giving the cumulants and discounts for the GVF questions. The architecture takes the j future observations \\(\obs\_{t+1:t+j}\\). parameterized by \\(\eta\\).

They argue the having the wait j-steps to learn the GVFs is reasonable as the question and answer networks are only used during training, and neither is needed for action selection. I'm not sure I buy the justification.

They set up three loss functions (two normal losses and one meta-loss).

1.  The canonical [DRL]({{< relref "deep_reinforcement_learning.md" >}}) loss \\(\mathcal{L}^{RL}\\) which is used to find the main task policy \\(\pi\_t\\) (either directly through policy search algorithms (<a href="#citeproc_bib_item_3">Williams 1992</a>) or through value function based approaches (<a href="#citeproc_bib_item_2">Watkins 1989</a>)).
2.  The auxiliary task loss function \\(\mathcal{L}^{ans}\\) which will likely take the form of a mini-batch semi-gradient TD (maybe multi-step) update.
3.  The meta loss \\(m\\) which is the sum of the \\(\mathcal{L}^{RL}\\) associated with the main task updates \\(\mathcal{L}^{Meta} = \sum\_{k=1}^L \mathcal{L}^{RL}(\theta\_{t,k})\\)

Where the weights of the main network are updated in the inner loop via:

\\[
\theta\_{t,k} \leftarrow \theta\_{t, k-1} - \alpha \nabla\_{\theta\_{t, k-1}} \left(\mathcal{L}^{RL}(\theta\_{t, k-1}) + \mathcal{L}^{ans}(\theta\_{t, k-1})\right)
\\]

and the meta weights \\(\eta\\) are updated in the outer loop via:

\\[
\eta\_{t+1} \leftarrow \eta\_t - \beta \nabla\_{\eta\_t} \sum\_{k=1}^L \mathcal{L}^{RL}(\theta\_{t,k})
\\]

and the weights of the main network are then set to:

\\[
\theta\_{t+1} \leftarrow \theta\_{t, L}
\\]

In this paper they use actor-critic to learn the policy, semi-gradient mini-batch TD for the answer network. To learn the feature encoder network they try using both the loss functions and just the loss function for the answer network.

They Provide experiments in a few domains:

1.  [Puddle World]({{< relref "puddle_world.md" >}})
2.  Collect-objects domain: a four-room gridworld where the agent is rewarded for collection two objects in the right order. The agents moves deterministically in one of the four directions. The locations of the two objects are the same across episodes.
3.  [Atari]({{< relref "atari.md" >}})

They show the usual minor improvements or similar results to previous experiments.


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Jaderberg, Max, Volodymyr Mnih, Wojciech Marian Czarnecki, Tom Schaul, Joel Z Leibo, David Silver, and Koray Kavukcuoglu. 2017. “Reinforcement Learning with Unsupervised Auxiliary Tasks.” <i>International Conference on Representation Learning</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Watkins, Christopher John Cornish Hellaby. 1989. “Learning from Delayed Rewards.” King’s College, Cambridge.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Williams, Ronald J. 1992. “Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning.” In <i>Reinforcement Learning</i>. The Springer International Series in Engineering and Computer Science. Springer, Boston, MA.</div>
</div>
