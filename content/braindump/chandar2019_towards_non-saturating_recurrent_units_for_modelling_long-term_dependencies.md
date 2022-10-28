+++
title = "chandar2019: Towards Non-saturating Recurrent Units for Modelling Long-term Dependencies"
author = ["Matthew Schlegel"]
lastmod = 2022-10-27T20:18:30-06:00
slug = "chandar2019"
draft = false
notetype = "paper"
+++

tags
: [Recurrent Neural Network]({{< relref "recurrent_neural_network.md" >}}), [Machine Learning]({{< relref "machine_learning.md" >}})

source
: <https://www.aaai.org/ojs/index.php/AAAI/article/view/4200>

In this paper they introduce a new recurrent cell named "NRU" for Non-saturating Recurrent Unit. There are two main contributions in this architecture which make it unique from other cells (i.e [LSTM]({{< relref "lstm.md" >}})).

-   The study and use of non-saturating activation functions (i.e. [ReLU Activations]({{< relref "relu_activation.md" >}})) for the non-linear transfer functions
-   They separate out a memory vector from the hidden state which can be a different size to the hidden state. This enables more information to be stored.

See the paper for a full description of the architecture.

Experiments:

The claim is that the NRU lessens the effect of the vanishing gradient problem and enables longer time dependencies to be modeled.

While the claim of the vanishing gradient problem isn't as fully explored as in (<a href="#citeproc_bib_item_1">Wu et al. 2016</a>), they support this in the "model analysis" section with some preliminary evidence of lack of divergence on the copy task. While this is a start, the instabilities seen in the training curves (i.e. figures 1 and 2) are worrying. What is causing these spikes in error? How would this effect an agent needing to make decisions in the real world? None of these questions are fully explored in the paper. They also don't focus on these issues in the main analysis of the results, focusing instead on the "faster convergence rates". I'm also a bit haphazard as I don't see confidence bounds or a mention on runs used. This leads to further questions about should we care about convergence at all costs, or is there a balance between fast convergence and reliable representations.



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Wu, Yuhuai, Saizheng Zhang, Ying Zhang, Yoshua Bengio, and Russ R Salakhutdinov. 2016. “On Multiplicative Integration with Recurrent Neural Networks.” In <i>Advances in Neural Information Processing Systems 29</i>, edited by D. D. Lee, M. Sugiyama, U. V. Luxburg, I. Guyon, and R. Garnett. Curran Associates, Inc.</div>
</div>
