+++
title = "sutton1988: Learning to predict by the methods of temporal differences"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:25-06:00
slug = "sutton1988"
draft = false
notetype = "paper"
+++

tags
: [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}})

source
: <https://link.springer.com/article/10.1007/BF00115009>

**TLDR**: This is [Rich Sutton]({{<relref "rich_sutton.md#" >}})'s seminal work where he establishes [Temporal Difference]({{<relref "temporal_difference_learning.md#" >}}) as a class of methods for multi-step prediction, and contrasts these methods with previous approaches. He also introduces eligibility traces and relates these to other styles of supervised learning. He then provides several examples of TD working in action. He finally proves convergence and optimality (under certain assumptions) for these types of methods.

**Impact**: This paper has had a long lasting impact. Primarily, in establishing temporal difference learning **and** in the process establishing the [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}}) field.
