+++
title = "LSTM"
author = ["Matthew Schlegel"]
lastmod = 2022-11-11T10:53:21-07:00
slug = "lstm"
tags = ["Recurrent", "Representation"]
draft = false
notetype = "note"
+++

tags
: [Recurrent Neural Network]({{< relref "recurrent_neural_network.md" >}}) [Neural Network]({{< relref "neural_network.md" >}}), [Machine Learning]({{< relref "machine_learning.md" >}})

source
: <https://colah.github.io/posts/2015-08-Understanding-LSTMs/>

The Long-Short Term Memory recurrent unit was first developed in (<a href="#citeproc_bib_item_1">Hochreiter and Urgen Schmidhuber 1997</a>), who showed the architecture could extend the effective horizon of the predictions made by recurrent networks. The main idea of the architecture was to have a linear path back through time to deal with the vanishing gradient problem. This is exactly what they introduced, where they have a memory component which gets modified through various gates in the architecture, but whose temporal connection is always linear. Meaning there are only a few non-linear operations between the current hiddenstate and a previous observation.

While the architecture was developed in (<a href="#citeproc_bib_item_1">Hochreiter and Urgen Schmidhuber 1997</a>), it became popular as it was later refined into what is most commonly used today using [Backpropagation Through Time]({{< relref "backpropagation_through_time.md" >}}) as the base training algorithm.

The architecture is made up of several gates: 2 Input Gates, a Forget Gate, and an Output Gate. The architecture has been modified considerably since, and several variants exist including the [GRU]({{< relref "gru.md" >}}).



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Hochreiter, Sepp, and J Urgen Schmidhuber. 1997. “Long Short-Term Memory.” <i>Neural Computation</i>.</div>
</div>
