+++
title = "jaderberg2017: Reinforcement Learning with Unsupervised Auxiliary Tasks"
author = ["Matthew Schlegel"]
lastmod = 2022-10-27T20:19:31-06:00
slug = "jaderberg2017"
draft = false
notetype = "paper"
+++

tags
: [Reinforcement Learning]({{< relref "reinforcement_learning.md" >}}), [Deep Reinforcement Learning]({{< relref "deep_reinforcement_learning.md" >}}), [Auxiliary Tasks]({{< relref "auxiliary_tasks.md" >}})

source
: <https://arxiv.org/pdf/1611.05397.pdf>

**Unreal Agent:**

-   Base agent is a CNN-LSTM ANN trained on-policy using A3C (<a href="#citeproc_bib_item_1">Mnih et al. 2016</a>) using a replay buffer of observations, rewards, and actions.
-   Pixel control: auxiliary policies \\(Q^\text{aux}\\) are trained to maximize change in pixel intensity of different regions.
-   Reward prediction: given three recent frames, the network must predict the reward that will be obtained in the next unobserved timestep.
-   Value Function Replay: further training of the value function using the agent network.

The overall architecture jointly optimizes all of its objectives.


## Auxiliary Control Tasks {#auxiliary-control-tasks}

These are defined as an additional pseudo-reward function in the environment. This is similar to a control [GVF]({{< relref "general_value_functions.md" >}}). In this paper, they use Q-Learning as described by (<a href="#citeproc_bib_item_1">Mnih et al. 2016</a>) for learning the auxiliary control tasks. They use two types of rewards:

-   **Pixel Changes**: Learn a policy for maximally changing the pixels in each cell of an \\(n \times n\\) non-overlapping grid placed over the input image.
-   **Network Features**: maximially activating each of the units in a specific hidden layer.


## Auxiliary Reward Task {#auxiliary-reward-task}

In addition to the control tasks, they also propose to add a reward prediction task. This is to predict the one-step reward at the end of a short sequence of states (for the LSTM).


## Value function replay {#value-function-replay}

[Experience Replay]({{< relref "experience_replay.md" >}}) is used not only for the usual case, but also in value function replay. This effectively resamples recent historical sequences from behaviour policy distributions and performing extra value function regression in addition to the on-policy updates in [A3C]({{< relref "mnih2016asynchronous_asynchronous_methods_for_deep_reinforcement_learning.md" >}}). The [ER buffer]({{< relref "experience_replay.md" >}}) is also used in the auxiliary control tasks described above.


## Results {#results}

Across all domains tested they show an improvement over baseline [A3C]({{< relref "mnih2016asynchronous_asynchronous_methods_for_deep_reinforcement_learning.md" >}}).

They test across several domains:

-   [Atari]({{< relref "atari.md" >}})
-   [DeepMind Lab]({{< relref "deepmind_lab.md" >}})

They use a set of other baselines which are all ablation studies on the UNREAL architecture.


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Mnih, Volodymyr, Adria Puigdomenech Badia, Mehdi Mirza, Alex Graves, Timothy Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu. 2016. “Asynchronous Methods for Deep Reinforcement Learning.” In <i>International Conference on Machine Learning</i>.</div>
</div>
