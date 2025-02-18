+++
title = "wu2016multiplicative: On Multiplicative Integration with Recurrent Neural Networks"
author = ["Matthew Schlegel"]
lastmod = 2022-11-08T14:24:01-07:00
slug = "wu2016multiplicative"
draft = false
notetype = "paper"
+++

tags
: [Recurrent Neural Network]({{< relref "recurrent_neural_network.md" >}}), [Neural Network]({{< relref "neural_network.md" >}}), [Machine Learning]({{< relref "machine_learning.md" >}})

source
: <http://papers.nips.cc/paper/6215-on-multiplicative-integration-with-recurrent-neural-networks>

This paper explores a new architectural building block for recurrent neural networks, specifically one which integrates information from the internal state of the unit and the data stream through a multiplicative update. They use the [Hadamard product]({{< relref "hadamard_product.md" >}}) to integrate this information together, although there are other choices here which they don't discuss (such as various tensor products).

**Additive building block**:

\\[\phi(\mathbf{W}\mathbf{x} + \mathbf{U}\mathbf{z} + \mathbf{b})\\]

**Multiplicative building block**:

\\[\phi(\mathbf{W}\mathbf{x} \odot \mathbf{U}\mathbf{z} + \mathbf{b})\\]

They have "more general versions", which basically include a number of new bias units for a better transformation.

**Claims:**

-   This architecture integrates information in a way that allows for difference in scale much better than additive blocks (i.e. small numbers aren't completely overwhelmed by large numbers.)
-   The backward flow of gradients through time is effected less by the exploding and vanishing gradient problem due to the inclusion of \\(\mathbf{W}\mathbf{x}\_k\\) in the gradient.

Do the experiments support the claims?

Gradient Properties:

-   First they look at the gradients when the [RNNs]({{< relref "recurrent_neural_network.md" >}}) have linear activation mappings (to focus on the internal mechanisms).  They measure the log of the L2-norm of the gradient for each epoch (averaged over the training set) using the Penn-Treebank dataset using the [ADAM]({{< relref "adam.md" >}}) optimizer. They are able to show the norm of the gradient grows much more in vanilla architecture (using additive operations) vs what occurs in the new architecture.

-   Lastly they look at the effects on activations by creating a histogram over activations for the training set using tanh activations. They show that the vanilla RNN is effectively fully saturated while the new version is not.

These experiments support their claim about the better gradient properties of the multiplicative mechanisms.

They also show that the more general form (including new bias units) is better than the simple form on the benchmark, although they don't seem to include confidence bounds.

They then do the usual showing it performs better than current SOTA (i.e. LSTMs and LSTMs w/ Batch-norm).
