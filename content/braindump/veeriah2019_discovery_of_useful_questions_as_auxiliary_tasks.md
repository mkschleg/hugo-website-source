+++
title = "veeriah2019: Discovery of Useful Questions as Auxiliary Tasks"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:41-06:00
slug = "veeriah2019"
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
: [General Value Functions]({{<relref "general_value_functions.md#" >}}), [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}})[Deep Reinforcement Learning]({{<relref "deep_reinforcement_learning.md#" >}})

source
: [link](http://papers.nips.cc/paper/9129-discovery-of-useful-questions-as-auxiliary-tasks)

authors
: Veeriah, V., Hessel, M., Xu, Z., Rajendran, J., Lewis, R. L., Oh, J., van Hasselt, Hado P, …

year
: 2019

This paper considers how to "discover" a set of GVF questions for auxiliary tasks <sup id="b7fd6e9e5809238a69c909aefb245768"><a href="#jaderberg2017" title="Jaderberg, Mnih, Czarnecki, Schaul, Leibo, Silver \&amp; Kavukcuoglu, {{REINFORCEMENT LEARNING WITH UNSUPERVISED AUXILIARY TASKS}}, {International Conference on Representation Learning}, v(), (2017).">jaderberg2017</a></sup> using meta-gradient descent. They consider a multi-step meta-loss function (unlike previous approaches which only consider a single step function).

They use two neural networks:

1.  The main architecture which is responsible for learning the answers to the GVF questions and learning the main task (i.e. the action-state value function or policy parameterization). This architecture takes the last i observations \\(\obs\_{t-i+1:t}\\) as inputs. Parameterized by \\(\theta\\)
2.  The question network which is responsible for giving the cumulants and discounts for the GVF questions. The architecture takes the j future observations \\(\obs\_{t+1:t+j}\\). parameterized by \\(\eta\\).

They argue the having the wait j-steps to learn the GVFs is reasonable as the question and answer networks are only used during training, and neither is needed for action selection. I'm not sure I buy the justification.

They set up three loss functions (two normal losses and one meta-loss).

1.  The canonical [DRL]({{<relref "deep_reinforcement_learning.md#" >}}) loss \\(\mathcal{L}^{RL}\\) which is used to find the main task policy \\(\pi\_t\\) (either directly through policy search algorithms <sup id="972b5cafcdddd5e9844535cdc7870538"><a href="#williams1992" title="@incollection{williams1992,
      title = {Simple {{Statistical Gradient}}-{{Following Algorithms}} for {{Connectionist Reinforcement Learning}}},
      booktitle = {Reinforcement {{Learning}}},
      author = {Williams, Ronald J.},
      year = {1992},
      series = {The {{Springer International Series}} in {{Engineering}} and {{Computer Science}}},
      publisher = {{Springer, Boston, MA}}
    }">williams1992</a></sup> or through value function based approaches <sup id="813c364b402bc49c1d8af7f0e043bed4"><a href="#watkins1989learning" title="@phdthesis{watkins1989learning,
      title = {Learning from Delayed Rewards},
      author = {Watkins, Christopher John Cornish Hellaby},
      year = {1989},
      school = {King's College, Cambridge}
    }">watkins1989learning</a></sup>).
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

1.  [Puddle World]({{<relref "puddle_world.md#" >}})
2.  Collect-objects domain: a four-room gridworld where the agent is rewarded for collection two objects in the right order. The agents moves deterministically in one of the four directions. The locations of the two objects are the same across episodes.
3.  [Atari]({{<relref "atari.md#" >}})

They show the usual minor improvements or similar results to previous experiments.


## References {#references}


# Bibliography
<a id="jaderberg2017"></a>[jaderberg2017] Jaderberg, Mnih, Czarnecki, Schaul, Leibo, Silver & Kavukcuoglu, REINFORCEMENT LEARNING WITH UNSUPERVISED AUXILIARY TASKS, <i>International Conference on Representation Learning</i>,  (2017). [↩](#b7fd6e9e5809238a69c909aefb245768)

<a id="williams1992"></a>[williams1992] @incollectionwilliams1992,
  title = Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning,
  booktitle = Reinforcement Learning,
  author = Williams, Ronald J.,
  year = 1992,
  series = The Springer International Series in Engineering and Computer Science,
  publisher = Springer, Boston, MA
 [↩](#972b5cafcdddd5e9844535cdc7870538)

<a id="watkins1989learning"></a>[watkins1989learning] @phdthesiswatkins1989learning,
  title = Learning from Delayed Rewards,
  author = Watkins, Christopher John Cornish Hellaby,
  year = 1989,
  school = King's College, Cambridge
 [↩](#813c364b402bc49c1d8af7f0e043bed4)
