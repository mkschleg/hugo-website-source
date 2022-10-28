+++
title = "liu2018: Breaking the Curse of Horizon: Infinite-Horizon Off-Policy Estimation"
author = ["Matthew Schlegel"]
lastmod = 2022-10-27T20:19:52-06:00
slug = "liu2018"
draft = false
notetype = "paper"
+++

tags
: [Reinforcement Learning]({{< relref "reinforcement_learning.md" >}}), [Off-policy]({{< relref "reinforcement_learning.md#off-policy" >}})

source
: [paper](http://papers.nips.cc/paper/7781-breaking-the-curse-of-horizon-infinite-horizon-off-policy-estimation)

authors
: Liu, Q., Li, L., Tang, Z., &amp; Zhou, D.

year
: 2018

The key contribution of this paper is a new approach to estimating the density ratio of two stationary state distributions. This is significant for correcting the data distributions, as we can directly correct both action and state distributions using a single step horizon of IS ratios. This reduces the potential variance of IS style approaches.

Many state-of-the-art off-policy estimation methods are based on IS (as we know). When the trajectory is long, the usual method for applying IS ratios is to take a product across all the IS ratios in a trajectory. This results in a high variance estimator, with increasing variance as the trajectory length increases. They coin this as "the curse of horizon" in off-policy learning.

They instead suggest to apply IS to the average visitation distribution of single steps of state-action pairs, rather than on the whole trajectories.

The background described for an MDP is standard. They assume finite state and action spaces for all the theory, but empirically the methods extend beyond this setting.

They setup the _infinite horizon_ problem, where there is no terminating states in the MDP. \\(p\_\pi(\cdot)\\) is the distribution of trajectory \\(\tau = \\{s\_t, a\_t, r\_t\\}\_{t=0}^{\infty}\\) under policy \\(\pi\\). The expected reward combines both the average reward case and typical case as

\\[R\_\pi \triangleq \lim\_{T\rightarrow \infty} \mathbb{E}\_{\tau \sim p\_\pi} [R^T(\tau)]\\]

where we specify

\\[R^T(\tau) \triangleq \frac{\sum\_{t=0}^T \gamma^t r\_t}{\sum\_{t=0}^T \gamma^t}\\].

The average reward case occurs when \\(\gamma = 1\\), and the discounted reward \\(0<\gamma<1\\).

They then describe the background for Value functions and Importance sampling. I will forgoe these, as they are straightforward.

**The Curse of Horizon**

The importance weight \\(w\_{0:T} = \prod\_{t=0}^T \frac{\pi(a\_t|s\_t)}{\pi\_0(a\_t|s\_t)}\\) is a product of T density ratios, whose variance can grow exponentially with T. While WIS estimators can empirically have reduced variance, the exponential dependence on horizon is unavoidable in general. This is coined the _curse of horizon_.


## Off-Policy estimation via Stationary State Density Ratio Estimation {#off-policy-estimation-via-stationary-state-density-ratio-estimation}

They show through a simple example that applying importance weighting on the state space, rather than the trajectory space, can significantly reduce the variance (which seems pretty obvious). This reduces the dependency on the trajectory length. The average visitation distribution is

\\[d\_\pi(s) = \lim\_{T\rightarrow\infty} \frac{(\sum\_{t=0}^T \gamma^t d\_{\pi, t}(s))}{\sum\_{t=0}^T \gamma^t}\\]

This can be split into the discounted case \\(d\_\pi(s) = (1-\gamma)\sum\_{t=0}^\infty \gamma^t d\_{\pi, t}(s)\\) when \\(\gamma \in (0,1)\\); and the average reward case \\(d\_\pi(s) = lim\_{T\rightarrow\infty} \frac{1}{T+1} \sum\_{t=0}^T d\_{\pi, t}(s)\\).

We can then construct a (weighted-)IS estimator to the desired quantity \\(R\_\pi\\) with samples obtained from \\(d\_{\pi\_0}(s,a) = d\_{\pi\_0}(s)\pi\_0(a|s)\\).

\\[\hat{R}\_{\pi}=\sum\_{i=1}^{m} \sum\_{t=0}^{T} w\_{t}^{i} r\_{t}^{i},
\quad \quad \text { where } \quad
w\_{t}^{i} :=\frac{\gamma^{t} w\_{\pi / \pi\_{0}}\left(s\_{t}^{i}\right) \beta\_{\pi / \pi\_{0}}\left(a\_{t}^{i} | s\_{t}^{i}\right)}{\sum\_{t^{\prime}, i^{\prime}} \gamma^{t} w\_{\pi / \pi\_{0}}\left(s\_{t^{\prime}}^{i^\prime}\right) \beta\_{\pi / \pi\_{0}}\left(a\_{t^{\prime}}^{i^\prime} | s\_{t^{\prime}}^{i^{\prime}}\right)}\\]

This estimator works in the space of \\((s,a)\\) instead of trajectories, potentially having a significant impact on the variance of the estimator.

While this estimator falls from the prior discussion rapidly, the task of estimating the stationary distributions (or their ratio) is still of concern.

They show the stationary ratio can be estimated with the following loss function in the discounted case

\\[L(w, f)=\gamma \mathbb{E}\_{\left(s, a, s^{\prime}\right) \sim d\_{\pi\_{0}}}\left[\Delta\left(w ; s, a, s^{\prime}\right) f\left(s^{\prime}\right)\right]+(1-\gamma) \mathbb{E}\_{s \sim d\_{0}}[(1-w(s)) f(s)]\\]

They show through theorem 4 that \\(w(s) = w\_{\pi/\pi\_0}(s)\\) if and only if \\(L(w, f) = 0\\). So minimizing this objective will lead to a good estimation of the density ratio. When \\(\gamma=1\\) this reduces to their prescribed average reward case, which only guarantees \\(w(s) \propto w\_{\pi/\pi\_0}(s)\\). Thy then provide some more guarantees to the estimator, even providing theoretical bounds.


## Experiments {#experiments}


### Taxi Environment {#taxi-environment}

This is a relatively classic domain for off-policy control type algorithms, where the goal is to pick up or drop off passengers. This is simulated in a simple 2D grid world. They extend the domain to be continuous. They test their algorithm using a policy learned through Q-learning over 1000 iterations and another policy which was learned after 950 transitions.

-   **QUESTION**: How off-policy is this actually? For policy evaluation we want arbitrarily distant policies. How do we create a study of this nature?

**Results**: their method does the best


### Pendulum {#pendulum}

They follow a similar methodology as above. Their results are relatively similar...


### SUMO {#sumo}

This is an open-source traffic simulator, with predefined interfaces. The domain seems pretty simple. The goal is to reduce traffic congestion by controlling the traffic light.
