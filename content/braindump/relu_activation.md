+++
title = "ReLU Activation"
author = ["Matthew Schlegel"]
lastmod = 2022-10-27T20:20:40-06:00
slug = "relu_activation"
draft = false
notetype = "note"
+++

tags
: [Neural Network]({{< relref "neural_network.md" >}})

A simple activation function which clips the output of the internal operations to be positive.

\\[ f(\mathbf{x}\_i) = \begin{cases}
\mathbf{x}\_i, & \text{ for } \mathbf{x\_i} \ge 0 \\\\
0 & \text{ o.w.}
\end{cases}
\\]

The main hallmark of this activation function is the smaller effect of the vanishing gradient problem in deep neural networks. This comes at a cost of stability and the greater risk of dead neurons.
