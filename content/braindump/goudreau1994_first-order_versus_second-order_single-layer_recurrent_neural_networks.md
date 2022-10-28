+++
title = "goudreau1994: First-order versus second-order single-layer recurrent neural networks"
author = ["Matthew Schlegel"]
lastmod = 2022-10-27T20:19:04-06:00
slug = "goudreau1994"
draft = false
notetype = "paper"
+++

tags
: [Recurrent Neural Network]({{< relref "recurrent_neural_network.md" >}}), [Machine Learning]({{< relref "machine_learning.md" >}})

source
: [paper](https://ieeexplore.ieee.org/abstract/document/286928?casa_token=E4AtxCXObRwAAAAA:zRCrX-jTWDkLzRKo7vz5JB6T-hrWO52VCzU1_5nON0MqQ9CgLMe0N5t0Wd6QhXKbXOwPHX3o8FY)

authors
: Goudreau, M., Giles, C., Chakradhar, S., &amp; Chen, D.

year
: 1994

This paper goes through the difference between first and second-order recurrent neural networks.

Notation:

-   \\(\mathbf{x}^t \in \mathbb{R}^N\\) is the input vector at time \\(t\\)
-   \\(\mathbf{h}^{t-1} \in \mathbb{R}^M\\) is the hidden state at time \\(t-1\\)
-   \\(\mathbf{W}\\) is the RNN weight matrix
-   \\(\mathbf{z}^{t} = [\mathbf{x}^t; \mathbf{h}^{t-1}]\\)

**First order**

\\[
\mathbf{h}^t\_{i} = g\left(\sum\_{j=1}^{M+N} \mathbf{W}\_{ij} z^{t}\_{j}  \right)
\\]

**Second order**

\\[
\mathbf{h}^t\_{i} = g\left(\sum\_{j=1}^{M} \sum{k=1}^{N} \mathbf{W}\_{ijk} \mathbf{x}^{t}\_{j} \mathbf{h}^{t-1}\_{k}  \right)
\\]

The second order RNN looks very similar to a tensor contraction across \\(\mathbf{x}\\) and \\(\mathbf{y}\\). This should be thought through as we combine different types of information in the state update. In the paper the non-linear function is the hard-limiter function

\\[
g(x) = \begin{cases}
0 & \quad \text{if } x \leq 0\\\\
1 & \quad \text{if } x > 0
\end{cases}
\\]

The rest of the paper is dedicated to showing that the second order RNN can implement any finite state recognizer (theorem 2), while a first-order RNN cannot. There is a modification to the first-order RNN which can implement the parity problem (including several layers after the RNN).
