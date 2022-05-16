+++
title = "LSTM"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:27-06:00
slug = "lstm"
draft = false
notetype = "note"
+++

tags
: [Recurrent Neural Network]({{<relref "recurrent_neural_network.md#" >}}) [Neural Network]({{<relref "neural_network.md#" >}}), [Machine Learning]({{<relref "machine_learning.md#" >}})

source
: <https://colah.github.io/posts/2015-08-Understanding-LSTMs/>

The Long-Short Term Memory recurrent unit was first developed in <sup id="c59a89800a027b3aa9da101668e63284"><a href="#hochreiter1997" title="Hochreiter \&amp; Urgen Schmidhuber, {{LONG SHORT}}-{{TERM MEMORY}}, {Neural Computation}, v(), (1997).">hochreiter1997</a></sup>, who showed the architecture could extend the effective horizon of the predictions made by recurrent networks. The main idea of the architecture was to have a linear path back through time to deal with the vanishing gradient problem. This is exactly what they introduced, where they have a memory component which gets modified through various gates in the architecture, but whose temporal connection is always linear. Meaning there are only a few non-linear operations between the current hiddenstate and a previous observation.

While the architecture was developed in <sup id="c59a89800a027b3aa9da101668e63284"><a href="#hochreiter1997" title="Hochreiter \&amp; Urgen Schmidhuber, {{LONG SHORT}}-{{TERM MEMORY}}, {Neural Computation}, v(), (1997).">hochreiter1997</a></sup>, it became popular as it was later refined into what is most commonly used today using [Backpropagation Through Time]({{<relref "backpropagation_through_time.md#" >}}) as the base training algorithm.

The architecture is made up of several gates: 2 Input Gates, a Forget Gate, and an Output Gate. The architecture has been modified considerably since, and several variants exist including the [GRU]({{<relref "gru.md#" >}}).


# Bibliography
<a id="hochreiter1997"></a>[hochreiter1997] Hochreiter & Urgen Schmidhuber, LONG SHORT-TERM MEMORY, <i>Neural Computation</i>,  (1997). [↩](#c59a89800a027b3aa9da101668e63284)
