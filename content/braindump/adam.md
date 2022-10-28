+++
title = "ADAM"
author = ["Matthew Schlegel"]
lastmod = 2022-10-27T20:18:01-06:00
slug = "adam"
draft = false
notetype = "note"
+++

tags
: [Optimizers]({{< relref "optimizers.md" >}}), [Neural Network]({{< relref "neural_network.md" >}})

source
: <https://ruder.io/optimizing-gradient-descent/index.html#adam>

An optimizer which effectively combines RMSProp and Momentum. The algorithm is as follows. Using the gradient \\(g\_t\\), we compute moving averages (or decaying averages) of the first and second moments.

\begin{align\*}
m\_t &= \beta\_m m\_{t-1} + (1-beta\_m) g\_t \\\\
v\_t &= \beta\_v v\_{t-1} + (1-beta\_v) g^2\_t
\end{align\*}

Both of these estimated averages are biased towards zero, and thus to unbias these moving averages we scale by \\(\frac{1}{1-\beta^t}\\)

\begin{align\*}
\hat{m}\_t &= \frac{m\_t}{1-\beta\_m^t} \\\\
\hat{v}\_t &= \frac{v\_t}{1-\beta\_v^t}
\end{align\*}

The first and second moments are then used to calculate the update to the weights:

\begin{align\*}
\theta\_{t+1} = \frac{\eta}{\sqrt{\hat{v}\_t} + \epsilon} \hat{m}\_t
\end{align\*}

Where \\(\eta, \epsilon, \beta\_m, \beta\_v\\) are all hyper parameters.

Typical settings:

\begin{align\*}
\beta\_m &= 0.9 \\\\
\beta\_v &= 0.999 \\\\
\epsilon &= 10^{-8}
\end{align\*}
