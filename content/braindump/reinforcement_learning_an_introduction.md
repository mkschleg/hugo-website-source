+++
title = "Reinforcement Learning: An Introduction"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:29:00-07:00
slug = "reinforcement_learning_an_introduction"
draft = false
notetype = "book"
+++

<div class="ox-hugo-toc toc">

<div class="heading">Table of Contents</div>

- [Introduction](#introduction)
    - [Reinforcement Learning](#reinforcement-learning)
- [Chapter 2](#chapter-2)
- [Finite Markov Decision Processes](#sec:RLI:mdps)
    - [The Agent-Environment Interface](#the-agent-environment-interface)
    - [Goals and Rewards](#goals-and-rewards)
    - [Returns and Episodes](#returns-and-episodes)
    - [Unified Notation for Episodic and Continuing Tasks](#unified-notation-for-episodic-and-continuing-tasks)
    - [Policies and Value Functions](#policies-and-value-functions)
    - [Optimal Policies and Optimal Value Functions](#optimal-policies-and-optimal-value-functions)
    - [Optimality and Approximation](#optimality-and-approximation)
- [Dynamic Programming](#dynamic-programming)
    - [Policy Evaluation (prediction)](#policy-evaluation--prediction)
    - [Policy Improvement](#policy-improvement)
    - [Policy Iteration](#policy-iteration)
    - [Value Iteration](#value-iteration)
    - [Asynchronous Dynamic Programming](#asynchronous-dynamic-programming)
    - [Generalized Policy Iteration](#generalized-policy-iteration)
    - [Efficiency of Dynamic Programming](#efficiency-of-dynamic-programming)
- [Monte Carlo Methods](#monte-carlo-methods)
    - [Monte Carlo Prediction](#monte-carlo-prediction)
    - [Monte Carlo Estimation of Action Values](#monte-carlo-estimation-of-action-values)
    - [Monte Carlo Control](#monte-carlo-control)
    - [Monte Carlo Control without Exploring Starts](#monte-carlo-control-without-exploring-starts)
    - [Off-policy Prediction via Importance Sampling](#off-policy-prediction-via-importance-sampling)
    - [Incremental Implementation](#incremental-implementation)
    - [Off-policy Monte Carlo Control](#off-policy-monte-carlo-control)
    - [Discounting-aware Importance Sampling](#discounting-aware-importance-sampling)
    - [Per-decision Importance Sampling](#per-decision-importance-sampling)
- [Temporal-Difference Learning](#temporal-difference-learning)
    - [TD Prediction](#td-prediction)
    - [Advantages of TD Prediction Methods](#advantages-of-td-prediction-methods)
    - [Optimality of TD(0)](#optimality-of-td--0)
    - [Sarsa: On-policy TD Control](#sarsa-on-policy-td-control)
    - [Q-learning: Off-policy TD Control](#q-learning-off-policy-td-control)
    - [Expected Sarsa](#expected-sarsa)
    - [Maximization Bias and Double Learning](#maximization-bias-and-double-learning)
    - [Games Afterstates, and Other Special Cases](#games-afterstates-and-other-special-cases)
- [Chapter 7](#chapter-7)
- [Planning and Learning with Tabular Methods](#planning-and-learning-with-tabular-methods)
    - [Models and Planning](#models-and-planning)
    - [Dyna: Integrated Planning, Acting, and Learning](#dyna-integrated-planning-acting-and-learning)
    - [When the Model Is Wrong](#when-the-model-is-wrong)
    - [Prioritized Sweeping](#prioritized-sweeping)
    - [Expected vs. Sample Updates](#expected-vs-dot-sample-updates)
    - [Trajectory Sampling](#trajectory-sampling)
    - [Real-time Dynamic Programming](#real-time-dynamic-programming)
    - [Planning at Decision Time](#planning-at-decision-time)
    - [Heuristic Search](#heuristic-search)
    - [Rollout Algorithms](#rollout-algorithms)
    - [Monte Carlo Tree Search](#monte-carlo-tree-search)
- [On-policy Prediction with Approximation](#on-policy-prediction-with-approximation)
    - [Value-function Approximation](#value-function-approximation)
    - [The Prediction Objective (\\(\bar{VE}\\))](#the-prediction-objective--bar-ve)
    - [Stochastic-gradient and Semi-gradient Methods](#stochastic-gradient-and-semi-gradient-methods)
    - [Linear Methods](#linear-methods)
    - [Feature Construction for Linear Methods](#feature-construction-for-linear-methods)
    - [Selecting Step-Size Parameters Manually](#selecting-step-size-parameters-manually)
    - [Nonlinear Function Approximation: Artificial Neural Networks](#nonlinear-function-approximation-artificial-neural-networks)
    - [Least-Squares TD](#least-squares-td)
    - [Memory-based Function Approximation](#memory-based-function-approximation)
    - [Kernel-based Function Approximation](#kernel-based-function-approximation)
    - [Looking Deeper at On-policy Learning: Interest and Emphasis](#looking-deeper-at-on-policy-learning-interest-and-emphasis)
- [Chapter 10](#chapter-10)
- [Chapter 11](#chapter-11)
- [<span class="org-todo todo TODO">TODO</span> Eligibility Traces](#sec:RLI:traces)
- [Policy Gradient Methods](#policy-gradient-methods)
    - [Policy approximation and its advantages](#policy-approximation-and-its-advantages)
    - [The Policy Gradient Theorem](#the-policy-gradient-theorem)
    - [REINFORCE](#reinforce)
    - [Actor-critic](#actor-critic)
    - [Policy Gradient for Continuing Problems](#policy-gradient-for-continuing-problems)
    - [Policy Parameterization for Continuous Actions](#policy-parameterization-for-continuous-actions)
- [Chapter 14](#chapter-14)
- [Chapter 15](#chapter-15)
- [Chapter 16](#chapter-16)
- [References](#references)

</div>
<!--endtoc-->

\\( \newcommand{\states}{\mathcal{S}}
\newcommand{\actions}{\mathcal{A}}
\newcommand{\observations}{\mathcal{O}}
\newcommand{\rewards}{\mathcal{R}}
\newcommand{\traces}{\mathbf{e}}
\newcommand{\transition}{P}
\newcommand{\reals}{\mathbb{R}}
\newcommand{\naturals}{\mathbb{N}}
\newcommand{\complexs}{\mathbb{C}}
\newcommand{\field}{\mathbb{F}}
\newcommand{\numfield}{\mathbb{F}}
\newcommand{\expected}{\mathbb{E}}
\newcommand{\var}{\mathbb{V}}
\newcommand{\by}{\times}
\newcommand{\partialderiv}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\defineq}{\stackrel{{\tiny\mbox{def}}}{=}}
\newcommand{\defeq}{\stackrel{{\tiny\mbox{def}}}{=}}
\newcommand{\eye}{\Imat}
\newcommand{\hadamard}{\odot}
\newcommand{\trans}{\top}
\newcommand{\inv}{{-1}}
\newcommand{\argmax}{\operatorname{argmax}}
\newcommand{\Prob}{\mathbb{P}}
\newcommand{\avec}{\mathbf{a}}
\newcommand{\bvec}{\mathbf{b}}
\newcommand{\cvec}{\mathbf{c}}
\newcommand{\dvec}{\mathbf{d}}
\newcommand{\evec}{\mathbf{e}}
\newcommand{\fvec}{\mathbf{f}}
\newcommand{\gvec}{\mathbf{g}}
\newcommand{\hvec}{\mathbf{h}}
\newcommand{\ivec}{\mathbf{i}}
\newcommand{\jvec}{\mathbf{j}}
\newcommand{\kvec}{\mathbf{k}}
\newcommand{\lvec}{\mathbf{l}}
\newcommand{\mvec}{\mathbf{m}}
\newcommand{\nvec}{\mathbf{n}}
\newcommand{\ovec}{\mathbf{o}}
\newcommand{\pvec}{\mathbf{p}}
\newcommand{\qvec}{\mathbf{q}}
\newcommand{\rvec}{\mathbf{r}}
\newcommand{\svec}{\mathbf{s}}
\newcommand{\tvec}{\mathbf{t}}
\newcommand{\uvec}{\mathbf{u}}
\newcommand{\vvec}{\mathbf{v}}
\newcommand{\wvec}{\mathbf{w}}
\newcommand{\xvec}{\mathbf{x}}
\newcommand{\yvec}{\mathbf{y}}
\newcommand{\zvec}{\mathbf{z}}
\newcommand{\Amat}{\mathbf{A}}
\newcommand{\Bmat}{\mathbf{B}}
\newcommand{\Cmat}{\mathbf{C}}
\newcommand{\Dmat}{\mathbf{D}}
\newcommand{\Emat}{\mathbf{E}}
\newcommand{\Fmat}{\mathbf{F}}
\newcommand{\Gmat}{\mathbf{G}}
\newcommand{\Hmat}{\mathbf{H}}
\newcommand{\Imat}{\mathbf{I}}
\newcommand{\Jmat}{\mathbf{J}}
\newcommand{\Kmat}{\mathbf{K}}
\newcommand{\Lmat}{\mathbf{L}}
\newcommand{\Mmat}{\mathbf{M}}
\newcommand{\Nmat}{\mathbf{N}}
\newcommand{\Omat}{\mathbf{O}}
\newcommand{\Pmat}{\mathbf{P}}
\newcommand{\Qmat}{\mathbf{Q}}
\newcommand{\Rmat}{\mathbf{R}}
\newcommand{\Smat}{\mathbf{S}}
\newcommand{\Tmat}{\mathbf{T}}
\newcommand{\Umat}{\mathbf{U}}
\newcommand{\Vmat}{\mathbf{V}}
\newcommand{\Wmat}{\mathbf{W}}
\newcommand{\Xmat}{\mathbf{X}}
\newcommand{\Ymat}{\mathbf{Y}}
\newcommand{\Zmat}{\mathbf{Z}}
\newcommand{\Sigmamat}{\boldsymbol{\Sigma}}
\newcommand{\identity}{\Imat}
\newcommand{\epsilonvec}{\boldsymbol{\epsilon}}
\newcommand{\thetavec}{\boldsymbol{\theta}}
\newcommand{\phivec}{\boldsymbol{\phi}}
\newcommand{\muvec}{\boldsymbol{\mu}}
\newcommand{\sigmavec}{\boldsymbol{\sigma}}
\newcommand{\jacobian}{\mathbf{J}}
\newcommand{\ind}{\perp\!\!\!\!\perp}
\newcommand{\bigoh}{\text{O}}
\\)

tags
: [Reinforcement Learning]({{< relref "reinforcement_learning.md" >}})

source
: <http://www.incompleteideas.net/book/the-book-2nd.html>


## Introduction {#introduction}

We learn by interacting with the world around us. This has been thought about since the time of [Hermann von Helmholtz]({{< relref "hermann_von_helmholtz.md" >}}), with his unconscious inferences.


### Reinforcement Learning {#reinforcement-learning}


## Chapter 2 {#chapter-2}


## Finite Markov Decision Processes {#sec:RLI:mdps}

This chapter introduces the formal problem of finite Markov decision processes (finite MDPs). You can think of MDPs as the mathematically idealized form of reinforcement learning (while the former came much earlier in the development of mathematical models for decision processes and stochastic processes).


### The Agent-Environment Interface {#the-agent-environment-interface}

The learner and decision maker is called the _agent_. The thing it interacts with, comprising everything outside the agent, is the _environment_. These two systems interact continually, the agent selecting actions and the environment responding to these action and presenting new situations to the agent. The environment also gives rise to the rewards, special observations that the agent seeks to maximize over time. More specifically, the agent and environment interact at each of a sequence of discrete time steps, \\(t=0,1,2,3,\ldots\\). At each step \\(t\\), the agent receives some representation of the environment's _state_, \\(S\_t \in \states\\), and on that basis selects and _action_, \\(A\_t \in \actions(s)\\). At step \\(t+1\\) the agent receives a numerical _reward_, \\(R\_{t+1} \in \rewards \subset \reals\\) and a new state \\(S\_{t+1}\\). The assumption is there exists some relationship between the agent's action and the environment's reaction. This gives rise to a _trajectory_

\\[S\_0, A\_0, R\_1, S\_1, A\_1, R\_2, S\_2, A\_2, R\_3, \ldots\\].

If the MDP is _finite_ the states, actions, and rewards (\\(\states\\), \\(\actions\\), and \\(\rewards\\)) all have a finite number of elements. The random variables \\(R\_t\\) and \\(S\_t\\) have well defined discrete probability distributions dependent only on the preceding state and action

\\[p(s', r | s, a) \defeq Pr\\{S\_t=s', R\_t=r | S\_{t-1}=s, A\_{t-1} = a\\} \quad \triangleright \text{forall } s',s\in\states, r\in \rewards, a\in\actions(s) \\].

The function \\(p: \states\times\rewards\times\states\times\actions\\) defines the _dynamics_ of the MDP.


### Goals and Rewards {#goals-and-rewards}

A core axiom on which reinforcement learning stands is noted as the _reward hypothesis_

> That all of what we mean by goals and purposes can be well thought of as the maximization of the expected value of the cumulative sum of a received scalar signal (called reward).

<aside>

This "hypothesis" is vacuous in my opinion. There are no useful tests which could draw out to a broader understanding of what it means for an agent to have a goal or purpose. I believe this hypothesis cannot be tested just from two ambiguous statements; "what we mean by" and "well thought of"; which make any counters impossible as the counter can be "that isn't what we mean" or "we can still think of it as". It is much better phrased as an assumption or axiom, as long as goals and purposes are more fully described. It is annoying to have circuitous on this: "what is the agent's goal" well it is to maximize reward, "what is the reward" well it is a signal defining the goal.

</aside>

<div class="question">

Why is the reward hypothesis a hypothesis and not an assumption or axiom.

</div>


### Returns and Episodes {#returns-and-episodes}

The agent seeks to maximize the _expected return_, where the return, denoted \\(G\_t\\), is defined as some specific function of the reward sequence. In the simplest case the return is

\\[G\_t \defeq R\_{t+1} + R\_{t+2} + R\_{t+3} + \ldots + R\_T\\]

where \\(T\\) is thought of as the "final" time step, or end of an _episode_. Each episode ends in a _terminal state_.

We can also think of _continuing tasks_ where there are no terminal states. Because there is no termination, the above sum will eventually diverge to infinity. _Discounting_ is one way of limiting the sum to a finite number:

\\[G\_t \defeq \sum\_{k=0}^{\infty} \gamma^k R\_{t+k+1} \quad \text{for } 0\le\gamma<1\\].

We can define the return recursively

\\[G\_t \defeq R\_{t+1} + \gamma G\_{t+1} \quad \text{where } G\_T = 0\\].

Because this is an exponentially decayed function, if the reward is a constant +1 we can say:

\\[G\_t = \frac{1}{1-\gamma}\\].


### Unified Notation for Episodic and Continuing Tasks {#unified-notation-for-episodic-and-continuing-tasks}

We can define a return for both episodic and continuing tasks

\begin{equation} \label{eqn:RLI:return}
G\_t \defeq \sum\_{k=t+1}^T \gamma^{k-t-1}R\_k
\end{equation}

Where either \\(T=\infty\\) **or** \\(\gamma = 1\\).


### Policies and Value Functions {#policies-and-value-functions}

-   _value function_: an estimate of the expected return, and can be thought of as "how good"
-   _policy_: a mapping from states to probabilities of selecting each possible action (\\(\pi(a|s)\\)).

The _value function_ of a state s while following policy \\(\pi\\) is

\begin{equation} \label{eqn:RLI:valuefunc}
v\_{\pi}(s) \defeq \expected\_{\pi}\left[G\_{t} | S\_{t}=s\right]=\expected\_{\pi}\left[\sum\_{k=0}^{\infty} \gamma^{k} R\_{t+k+1} | S\_{t}=s\right], \text { for all } s \in \states.
\end{equation}

The value of a terminal state (if any exist) is always zero. We say the function \\(v\_\pi\\) is the _state-value function for policy &pi;_. Similarly, we define the _action-value function for policy &pi;_ as

\begin{equation} \label{eqn:RLI:actionvaluefunc}
q\_{\pi}(s, a) \defeq \expected\_{\pi}\left[G\_{t} | S\_{t}=s, A\_{t}=a\right]=\expected\_{\pi}\left[\sum\_{k=0}^{\infty} \gamma^{k} R\_{t+k+1} | S\_{t}=s, A\_{t}=a\right].
\end{equation}

A fundamental property of value functions used throughout reinforcement learning and dynamic programming is that they satisfy recursive relationships (similar to equation <eqn:RLI:return>)! For any policy \\(\pi\\) and any state \\(s\\), the following consistency condition holds:

\begin{align}
v\_{\pi}(s)
&\defeq \mathbb{E}\_{\pi}\left[G\_{t} | S\_{t}=s\right] \nonumber \\\\
&=\expected\_{\pi}\left[R\_{t+1}+\gamma G\_{t+1} | S\_{t}=s\right] \nonumber \\\\
&=\sum\_{a} \pi(a | s) \sum\_{s^{\prime}} \sum\_{r} p\left(s^{\prime}, r | s, a\right)\left[r+\gamma \expected\_{\pi}\left[G\_{t+1} | S\_{t+1}=s^{\prime}\right]\right] \nonumber\\\\
&=\sum\_{a} \pi(a | s) \sum\_{s^{\prime}, r} p\left(s^{\prime}, r | s, a\right)\left[r+\gamma v\_{\pi}\left(s^{\prime}\right)\right], \quad \text { for all } s \in \mathcal{S} \label{eqn:RLI:bellman}
\end{align}

The recursive form defined in equation <eqn:RLI:bellman> is known as the _Bellman equation for \\(v\_\pi\\)_. It expresses the relationship between the value of a state and the values of its successor states. The value function \\(v\_\pi\\) is the unique solution to its Bellman equation.


### Optimal Policies and Optimal Value Functions {#optimal-policies-and-optimal-value-functions}

Value functions define a partial ordering over policies. A policy &pi; is defined to be better than or equal to another policy &pi;' if its expected return is greater than or equal to that of &pi;' for all states. More clearly, \\(\pi\geq\pi'\\) iff \\(v\_\pi(s) \geq v\_{\pi'}(s)\\) for all \\(s\in\states\\). We will denote all optimal policies by \\(\pi\_\star\\). All optimal polices share the same value function

\begin{equation}
v\_\star (s) \defeq \max\_\pi v\_\pi(s) \quad \text{for all } s\in\states.
\end{equation}

We can also define the _optimal action-value function_

\begin{equation}
q\_\star (s,a)\defeq \max\_\pi q\_\pi(s,a) \quad \text{for all } s\in\states, a\in\actions.
\end{equation}

We can also define a special Bellman equation for the optimal value function called the _Bellman optimality equation_

\begin{align}
v\_\star(s)  &= \max\_a \sum\_{s',r} p(s', r | s, a) \left[r+\gamma v\_\star(s')\right] \\\\
q\_\star(s,a) &= \sum\_{s',r} p(s',r|s,a)\left[r+\gamma \max\_{a'}q\_\star (s', a')\right]
\end{align}

For finite MDPs, the Bellman optimality equation has a unique solution independent of the policy. While we can explicitly solve the Bellman optimality equation, there are a number of assumptions that are rarely true in real world examples:

1.  we accurately know the dynamics of the environment
2.  we have enough computational resources to complete the computation of the solution
3.  the Markov property

Many reinforcement learning methods can be clearly understood as approximately solving the Bellman equation, using actual experienced transitions in place of knowledge of the expected transitions.


### Optimality and Approximation {#optimality-and-approximation}

We are forced to settle for an approximate solution to the Bellman equation. But this is ok. The online nature of reinforcement learning makes it possible to approximate optimal policies in ways that put more effort into learning to make good decisions for frequently encountered states, at the expense of less effort for infrequently encountered states. This is "one key property" that distinguishes reinforcement learning from other approaches to approximately solving MDPs.


## Dynamic Programming {#dynamic-programming}

**Dynamic programming** (DP) refers to a collection of algorithms that can be used to compute optimal policies given a _perfect model_ of the environment as an MDP. These algorithms are of limited use to the full RL problem as they require a perfect model and have an immense up-front computational cost. These algorithms are still interesting theoretically, and provide a nice foundation to begin thinking about learning optimal policies. In this chapter, we will limit ourselves to finite MDPs. A key idea of DP, and of RL generally, is the use of value functions to organize and structure the search for good policies.


### Policy Evaluation (prediction) {#policy-evaluation--prediction}

**Policy Evaluation**: compute the state-value function \\(v\_\pi\\) for an arbitrary policy \\(\pi\\). Also known as the prediction problem. Recall from Chapter 3:

\begin{align}
v\_\pi(s) &\defeq \expected\_\pi[G\_t | S\_t=s] \nonumber\\\\
         &= \sum\_{a}\pi(a|s)\sum\_{s', r} p(s', r|s, a)[r+\gamma v\_\pi(s')] \label{eqn:RLI:dp:valuefunc}
\end{align}

If the environment's dynamics are completely known, then \ref{eqn:RLI:dp:valuefunc} is a system of \\(|\states|\\) simultaneous linear equations in \\(|\states|\\) unknowns. This calculation is straightforward but tedious. For our purposes, iterative solution methods are most suitable. If \\(v\_0\\) is chosen arbitrarily (except for any terminal states which must be 0), then we can iteratively solve for the value function

\begin{align\*}
v\_{k+1}(s) &\defeq \expected\_\pi[R\_{t+1} + \gamma v\_k(S\_{t+1}) | S\_t = s] \\\\
& = \sum\_{a}\pi(a|s)\sum\_{s', r} p(s', r|s, a)[r+\gamma v\_{k}(s')] \label{eqn:RLI:dp:iterative}
\end{align\*}

The sequence of \\(v\_k\\) can be shown to converge to \\(v\_\pi\\) in general as \\(k\rightarrow\infty\\). This algorithm is called _iterative policy evaluation_. This algorithm can also be done in-place.


### Policy Improvement {#policy-improvement}

Once we have a state value function \\(v\_\pi\\), we would like to use it to find a better policy (if one exists). The most straightforward method is to construct an action value function

\\[q\_\pi(s,a) \defeq \expected[R\_{t+1} + \gamma v\_\pi(S\_{t+1}) | S\_t =s, A\_t = a].\\]

If \\(q\_\pi(s,a) > v\_\pi(s)\\) then you can improve the policy \\(\pi\\) by selecting action \\(a\\) in state \\(s\\) and then following \\(\pi\\) elsewhere. This is a special case of the _policy improvement theorem_. Let &pi; and &pi;' be any pair of deterministic policies such that

\\[q\_\pi(s, \pi'(s)) \ge v\_\pi(s) \quad \triangleright \quad \forall s \in \states\\].

Then the policy &pi;' must be as good as, or better than &pi;, meaning \\(v\_{\pi'}(s) \ge v\_\pi(s)\\).

Instead of focusing on changing the policy at a a single state, we can improve the policy over all states simultaneously: \\(\pi' \defeq \argmax\_a q\_\pi(s,a)\\).


### Policy Iteration {#policy-iteration}

Once a policy &pi; has been improved using \\(v\_\pi\\) to yield a better policy &pi;', we can then compute \\(v\_{\pi'}\\) and improve it again to yield an even better policy! We can create a chain of evaluations and improvements continuing until we get to a policy which is no longer changing. Because a finite MDP has only a finite number of policies, this process must converge to an optimal policy and optimal value function in a finite number of iterations. This is called **policy iteration**.

<div class="algorithm">

\begin{algorithmic}
\State 1. Initialization
\State $V(s) \in \reals$ and $\pi(s) \in \actions(s)$ arbitrarily for $s\in\states$
\State
\State 2. Policy Evaluation
\Repeat
\State $\Delta \leftarrow 0$
\ForAll{$s \in \states$}
\State $v \leftarrow V(s)$
\State $V(s) \leftarrow \sum\_{s',r}p(s',r|s,\pi(s)) [r+\gamma V(s')]$
\State $\Delta \leftarrow max(\Delta, |v-V(s)|)$
\EndFor
\Until{$\Delta < \theta$}
\State
\State 3. Policy Improvement
\State $policy\\\_stable \leftarrow true$
\ForAll{$s\in\states$}
\State $old-action\leftarrow\pi(s)$
\State $\pi(s) \leftarrow \argmax\_a \sum\_{s',r}p(s',r|s,\pi(s)) [r+\gamma V(s')]$
\State If $old\\\_action \neq \pi(s)$, then $policy\\\_stable \leftarrow false$
\EndFor
\State If $policy\\\_stable$, then stop and return $V\approx v\_\star$ and $\pi \approx \pi\_\star$; else go to 2.
\end{algorithmic}

\caption{Policy Iteration (using iterative policy evaluation) for estimating $\pi \approx \pi^\*$}

</div>


### Value Iteration {#value-iteration}

Instead of having a full policy evaluation step in-between policy improvement steps, we can truncate policy evaluation to a single sweep through the state-space without changing the convergence properties of the algorithm. This algorithm is known as _value iteration_ and can be written simply as

\\[v\_{k+1}(s) \defeq \max\_a \sum\_{s',r} p(s', r|s,a)[r+\gamma v\_k(s')] \quad \triangleright \quad \forall s\in\states\\].

Value iteration effectively combines one sweep of policy evaluation and one sweep of policy improvement. Faster convergence is often achieved by interposing multiple policy evaluation sweeps between each policy improvement sweep. In general, the entire class of truncated policy iteration algorithms can be through of as sequences of sweeps.

<div class="algorithm">

\begin{algorithmic}
\State Algorithm parameter: a small threshold $\theta > 0$ determining accuracy of estimation.
\State Initialize $V(s)$, for all $s\in\states^+$, arbitrarily except that $V(terminal)=0$
\Repeat
\State $\Delta \leftarrow 0$
\ForAll{$s\in\states$}
\State $v\leftarrow V(s)$
\State $V(s) \leftarrow \max\_a \sum\_{s',r} p(s', r|s,a)[r+\gamma V(s')]$
\State $\Delta \leftarrow \max(\Delta, |v-V(s)|)$
\EndFor
\Until{$\Delta < \theta$}
\State Output a deterministic policy, $\pi \approx\pi\_\star$, such that
\State $\pi(s) = \argmax\_a \sum\_{s',r} p(s', r|s,a)[r+\gamma V(s')]$
\end{algorithmic}

\caption{Value Iteration, for estimating $\pi\approx\pi^\star$}

</div>


### Asynchronous Dynamic Programming {#asynchronous-dynamic-programming}

_Asynchronous DP_ algorithms: in-place iterative DP algorithms that are not organized in terms of systematic sweeps of the state set. These algorithms update the values of states in any order whatsoever, using whatever values of other states happen to be available. The only restriction for convergence is an asynchronous algorithm must continue to update the values of all the states.


### Generalized Policy Iteration {#generalized-policy-iteration}

_Generalized policy iteration_ (GPI): the general idea of letting policy-evaluation and policy-improvement porcesses interact, independent of the granularity and other details of the two processes.


### Efficiency of Dynamic Programming {#efficiency-of-dynamic-programming}

If \\(n\\) and \\(k\\) denote the number of states and actions, a DP method takes a number of computational operations that is less than some polynomial function of \\(n\\) and \\(k\\) (i.e. DP methods are in polynomial time). DP is sometimes through to be of limited applicability because of the _curse of dimensionality_, the fact that the number of states often grows exponentially with the number of state variables.


## Monte Carlo Methods {#monte-carlo-methods}

Monte Carlo methods require only _experience_--sample sequences of states, action, and rewards from actual or simulated interaction with an environment. These methods are a way to solve the reinforcement learning problem based on averaging sample returns. In this section we will only go into Monte Carlo methods for episodic tasks, forgoing continuing tasks (discounting) entirely.


### Monte Carlo Prediction {#monte-carlo-prediction}

A Monte Carlo method estimates a value for a particular state by averaging the returns of seen after the state is visited.

-   _first-visit_ MC estimates \\(v\_\pi(s)\\) as the average of the returns following first visits to \\(s\\).
-   _every-visit_ MC averages the returns following all visits to \\(s\\).

Both the above methods are well known and converge to the optimal, albeit with slightly different theoretical properties. It is quite easy to see why first-visit converges (by the law of large numbers). Every-visit still converges quadratically, but is a bit more onerous (<a href="#citeproc_bib_item_3">Singh and Sutton 1996</a>).

<div class="algorithm">

\begin{algorithmic}
\State Input: a policy $\pi$ to be evaluated
\State Initialize: $V(s)\in\reals \forall s\in\states$, $Returns(s) \leftarrow$ empty list.
\ForAll{$e\in$Episodes}
\State Generate an episode following $\pi$: $S\_0, A\_0, R\_1, S\_1, A\_1, R\_2, \ldots, S\_{T-1}, A\_{T-1}, R\_T$
\State $G \leftarrow 0$
\ForAll{$t \in \\{T-1, T-2, \ldots, 0\\}$}
\State $G\leftarrow \gamma G + R\_{t+1}$
\If{$S\_t \notin \\{S\_0, S\_1, \ldots, S\_{t-1}\\}$}
\State Append $G$ to $Returns(S\_t)$
\State $V(s\_t) \leftarrow average(Returns(S\_t))$
\EndIf
\EndFor
\EndFor
\end{algorithmic}

\caption{First-visit MC prediction, for estimating $V \approx v\_\pi$}

</div>

<aside>

According to (<a href="#citeproc_bib_item_3">Singh and Sutton 1996</a>) every-visit Monte Carlo methods resolve to a TD update with accumulating traces, and first-visit Monte Carlo methods resolve to a TD update with replacing traces. This will become more clear when we discuss eligibility traces in section  <sec:RLI:traces>.

</aside>


### Monte Carlo Estimation of Action Values {#monte-carlo-estimation-of-action-values}

Without a model of the environment, estimating state value functions is not enough to prepare behavior. Instead, one must estimate action-state value functions (as discussed in section <sec:RLI:mdps>). The evaluation algorithm is very similar to that of state value functions. The one modification to the original algorithm is the need for the agent to explore (even when given a deterministic policy) to estimate the return for each action from every state.


### Monte Carlo Control {#monte-carlo-control}

<div class="algorithm">

\begin{algorithmic}
\State Initialize:
\State $\quad\pi(s) \in \actions(s)$ (arbitrarily)
\State $\quad Q(s,a) \in \reals$ (arbitrarily)
\State $\quad Returns(s,a) \leftarrow $ empty list.
\For{each episode}
\State Choose $S\_0 \in \states, A\_0 \in \actions(S\_0)$ randomly from all states and actions
\State Generate an episode of length $T>0$
\State $G \leftarrow 0$
\For{$t = \\{T-1, T-2, \ldots, 0\\}$}
\State $G \leftarrow \gamma G + R\_{t+1}$
\If{$S\_t, A\_t \notin \\{S\_0, A\_0, \ldots S\_{t-1}, A\_{t-1}\\}$}
\State Append $G$ to $Returns(S\_t, A\_t)$
\State $Q(S\_t, A\_t) \leftarrow average(Returns(S\_t, A\_t))$
\State $\pi(S\_t) \leftarrow \argmax\_a Q(S\_t, a)$
\EndIf
\EndFor
\EndFor
\end{algorithmic}

\caption{Monte Carlo ES (Exploring Starts), for estimating $\pi \approx \pi\_\*$}

</div>


### Monte Carlo Control without Exploring Starts {#monte-carlo-control-without-exploring-starts}

In the case that the prior assumption of "exploring starts" is not met, the easiest way to fulfill the assumption that all actions are chosen infinitely often is for the agent to continue to select them. This section details an on-policy version of the above algorithm which accomplishes this, in the next section an off-policy method will be introduced.

In on-policy control the policy is generally soft (i.e. \\(\pi(a | s) > 0 \quad \forall s \in \states \text{ and } a \in \actions\\) ) and gradually shifted to the deterministic optimal policy.

<div class="note">

This Assumes there is an optimal deterministic policy, which depending on the problem setting may not be true. But this assumption is reasonable in the MDP setting as stated.

</div>

The on-policy method in this setting uses what are called $&epsilon;$-greedy policies. Effectively they assign probability \\(1-\epsilon + \frac{\epsilon}{|\actions(s)|}\\) to the action with the highest estimated value and \\(frac{\epsilon}{|\actions(s)|}\\) to the remaining values. While not shown here, one can find the sketch of a proof showing policy improvement works for $&epsilon;$-greedy policies in a similar way to deterministic policies w/ exploring starts in (<a href="#citeproc_bib_item_5">Sutton and Barto 2018</a>) page 101.


### Off-policy Prediction via Importance Sampling {#off-policy-prediction-via-importance-sampling}

This section introduces the notion of learning from data which is generated from a policy which is different from the policy of interest (i.e. the optimal). These learning strategies are called off-policy.

-   _target_ policy \\(\pi\\): The policy of interest.
-   _behavior_ policy \\(b\\): The policy used to act in the environment.

In order to use experience generated from \\(b\\) to learn about policy \\(\pi\\) they must have shared support over the state action space (i.e. \\(\pi(a|s) > 0 \text{ implies } b(a|s) > 0\\)). The core of the algorithm comes in correcting the mismatch in distributions through what is called the _importance ratio_ \\(\rho(A, S) = \frac{\pi(A|S)}{b(A|S)}\\) and over a trajectory \\(\rho\_{t:T-1} = \prod\_{k=t}^{T-1} \rho(A\_k | S\_k)\\). Importance sampling can then be applied to the expectation over returns to get the proper value function

\\[
\expected [\rho\_{t:T-1} G\_t | S\_t = s] = v\_{\pi}(s).
\\]

There are plenty of problems when applying importance ratios immediately to the problem. One of particular concern is that ordinary importance sampling can have infinite variance (depending on the problem), which leads to unstable slow learning. Other algorithms have been invented to handle the infinite variance issue (i.e. weighted importance sampling, resampling).


### Incremental Implementation {#incremental-implementation}

The episode-by-episode incremental version of Monte Carlo prediction methods are straight forward taking the form:

\\[
V\_{n+1} = V\_n + \frac{1}{n} [G\_n - V\_n].
\\]

These can also be defined w/ OIS and WIS (see (<a href="#citeproc_bib_item_5">Sutton and Barto 2018</a>) page 109).


### Off-policy Monte Carlo Control {#off-policy-monte-carlo-control}

This is a straightforward extension of the off-policy Monte Carlo prediction algorithms presented above to GPI.


### Discounting-aware Importance Sampling {#discounting-aware-importance-sampling}


### Per-decision Importance Sampling {#per-decision-importance-sampling}


## Temporal-Difference Learning {#temporal-difference-learning}


### TD Prediction {#td-prediction}


### Advantages of TD Prediction Methods {#advantages-of-td-prediction-methods}


### Optimality of TD(0) {#optimality-of-td--0}


### Sarsa: On-policy TD Control {#sarsa-on-policy-td-control}


### Q-learning: Off-policy TD Control {#q-learning-off-policy-td-control}


### Expected Sarsa {#expected-sarsa}


### Maximization Bias and Double Learning {#maximization-bias-and-double-learning}


### Games Afterstates, and Other Special Cases {#games-afterstates-and-other-special-cases}


## Chapter 7 {#chapter-7}


## Planning and Learning with Tabular Methods {#planning-and-learning-with-tabular-methods}

This chapter develops a unified view of reinforcement learning methods that require a model of the environment, such as dynamic programming and heuristic search, and methods that can be used without a model.

-   _model-free_ methods: These methods are those discussed in the first 6 chapters of the book. Specifically Monte-carlo methods, TD methods, and similar such methods not requiring a model of the environment's dynamics.
-   _model-based_ methods: These methods deploy a type of _planning_ for their main component for training value functions and policies. Dynamic programming can be considered as model-based in this context.


### Models and Planning {#models-and-planning}

**model**: A model is a representation of the environment's dynamics. This can be a non-parametric model such as an experience replay buffer, or a parametric model generating sample transitions. You can also represent a model through predictions in the world (not discussed directly here), or through options in an option-model.

From the book: A model of the environment is anything that an agent can use to predict how the environment will respond to its actions.

-   _distribution models_: produce a description of all possibilities and their probabilities (**type of model assumed by dynamic programming**)
-   _sample models_: produce just one of the possibilities sampled according to the probabilities.

Distribution models are stronger than sample models as they can be used to produce samples, but these types of models are hard to learn/obtain.

We say the model is used to _simulate_ the environment and produce _simulated experience_.

**planning**: In this book, the term refers to any computational process that takes a model as input and produces or improves a policy for interacting with the modeled environment.

-   _State-space planning_: a search through the state space for an optimal policy or an optimal path to a goal.
-   _Plan-space planning_: a search through the space of plans. These types of methods include evolutionary methods and "partial-order planning"

The view taken in this book is that all state-space planning methods share a common structure, which is also present in the learning methods. There are two basic ideas to this view:

1.  all state-space planning methods involve computing value functions as a key intermediate step toward improving the policy
2.  they compute value functions by updates applied to simulated experience.


### Dyna: Integrated Planning, Acting, and Learning {#dyna-integrated-planning-acting-and-learning}

There are at least two roles for real experience:

-   _Model-learning_: it can be used to improve the model
-   _Direct RL_: it can be used to directly improve the value function and policy using and _model-free_ method.

When using simulated experience (from the model) to learn, this is called _indirect RL_.

Dyna-Q includes all of the above processes occuring continually. The planning method is the random-sample one-step tabular Q-planning method (simply sampling a transition from a model from a randomly chosen state action pair; see page 161 of (<a href="#citeproc_bib_item_5">Sutton and Barto 2018</a>)). The model-learning method is table-based and assumes the environment is deterministic (making this the least usable model learning approach beyond tabular domains).

They show an example of a maze comparing Q-learning (Dyna-Q with \\(n=0\\) planning steps), and Dyna-Q with \\(n=\\{5, 50\\}\\) planning steps. It quite clearly shows model-based methods working better than model-free methods, but this result can only be generalized to tabular settings. It is quite straightforward with a deterministic tabular environment, a model is accurate from basic experience. Unfortunately, such models are hard to learn/uncover.


### When the Model Is Wrong {#when-the-model-is-wrong}

When the model is incorrect, the planning process is likely to compute a suboptimal policy. This is shown in the blocking maze experiment. Another method was introduced, Dyna-Q+, which introduces a heuristic (i.e. reward shaping and state counting) to determine when the environment might change, or when the agent should go and explore parts of the environment again. This is again not possible in larger environments, as model based learning is hard in such environments to achieve the fidelity needed to perform well.

Specifically the Dyna-Q+ algorithm keeps track of each state-action pair of how many time steps have elapsed since the pair was last tried in a real interaction with the environment. The indirect RL then set a reward for these samples as \\(r + \kappa\sqrt{\tau}\\), for a small set \\(\kappa\\). This would inject bias into the agent's policy to explore parts of the state-space not seen in a while.

This is fine with a finite state-space, but a state-space which is large this could cause the agent to do something bad. Also this assumes any change to the environment is good, which is a bold assumption.


### Prioritized Sweeping {#prioritized-sweeping}

The main idea is that we want to plan backward from any state whose value has changed. This idea can be termed _backward focusing_ of planning computations. Instead of uniformly sampling across all transitions which have changed values, we could prioritize on the _urgency_ of the change (i.e. update the changes with the most impact first). This is implemented using a priority queue over state-action pairs.

This idea is easily extended to stochastic environments, and we can use similar ideas from Dyna-Q+ for non-stationary environments.


### Expected vs. Sample Updates {#expected-vs-dot-sample-updates}

Expected updates take considerably more computation than sample updates. For instance consider the expectation update

\\[ Q(s, a) \leftarrow \sum\_{s^{\prime}, r} \hat{p}\left(s^{\prime}, r | s, a\right)\left[r+\gamma \max \_{a^{\prime}} Q\left(s^{\prime}, a^{\prime}\right)\right] \\]

and the corresponding sample update

\\[ Q(s, a) \leftarrow Q(s, a)+\alpha\left[R+\gamma \max \_{a^{\prime}} Q\left(S^{\prime}, a^{\prime}\right)-Q(s, a)\right]. \\]

The expected updates consider all possible events taking the expectation over these events to get a cleaner update. The sample updates only consider a single sample from the environment, and implicitly do the expectation over several visits to this states local area. The computational differences is significant here. If a correct estimate of the transition dynamics is available, and there is roughly \\(|\states \times \rewards|\\) more computation available then the expected update would produce a better estimator.

They present a nice plot which illustrates why sample updates are better. In summary, the amount of computation needed to perform a expected update as above is incredibly large as the number of states and actions increases. The sample-updates almost definitely win in real world applications.


### Trajectory Sampling {#trajectory-sampling}

This is a contrast to prior model based methods presented (specifically Dyna-Q), where a uniform sampling of the state-space was performed. This implicitly assigns equal computation to all states, which is undesirable. One alternative is trajectory based sampling, where the agent simulates a trajectory based on a randomly sampled state-action pair. This is ok, but also requires a model which can simulate such a trajectory (which is a really difficult ask).

Another approach that I can think of is through an ER buffer, where we are selecting states and action according to the desired distribution induced by the behavior. It is difficult to imagine every being able to sample according to the uniform policy in large scale problems, but given the toy examples the on-policy distribution seems to be the correct thing for faster learning.


### Real-time Dynamic Programming {#real-time-dynamic-programming}

This is an example of an _asynchronous-DP_ method. Here the update order is dictated by the order states are visited in real or simulated trajectories.

**Properties:**

-   RTDP is guaranteed to find a policy that is optimal on the relevant states without visiting every state infinitely often, or even without visiting some states at all (in undiscounted episodic tasks for MDPs with absorbing goal states that generate zero rewards). This convergence happens with probability one when each episode begins in a randomly chosen state sampled from the set of start states and ending at the goal state.
-   As the value function approaches the optimal value function, the policy used by the agent to generate trajectories approaches an optimal policy because it is always greedy wrt the current value function.


### Planning at Decision Time {#planning-at-decision-time}

_Background planning_: Planning to gradually improve the value function or policy on the basis of simulated experience obtained from a model. Selecting actions is then a matter of comparing the current state's action values. Planning is not focused on the current state.

_Decision-time planning_: When planning is begun and completed _after_ encountering each new state \\(S\_t\\), as a computation whose output is the selection of a single action \\(A\_t\\). Planning focuses on a particular state (i.e. the current state or those already visited).


### Heuristic Search {#heuristic-search}

For each state encountered, a large tree of possible continuations is considered. The approximate value function is applied to the leaf nodes and then backed up toward the current state at the root.


### Rollout Algorithms {#rollout-algorithms}

These algorithms are based on Monte Carlo control applied to simulated trajectories that all begin at the current environment state. They estimate action values for a given policy by averaging the returns of many simulated trajectories that start with each possible action and then follow the given policy. These algorithms were described by (<a href="#citeproc_bib_item_6">Tesauro 1994</a>) in their self-learning backgammon agent.

The goal of a rollout algorithm is to improve on the rollout policy, not to find the one-step optimal policy.


### Monte Carlo Tree Search {#monte-carlo-tree-search}

This is an example of a rollout algorithm enhanced by the addition of a means for accumulating value estimates obtained from the Monte Carlo simulations in order to successively direct simulations toward more highly-rewarding trajectories.

1.  **Selection** Starting at the root node, a _tree policy_ based on the action values attached to the edges of the tree traverses the tree to select a leaf node.
2.  **Expansion** On some iterations, the tree is expanded from the selected leaf node by adding one or more child nodes reached from the selected node via unexplored actions.
3.  **Simulation** From the selected node, or from one of the added child nodes, simulation of a complete episode is run with actions selected by the rollout policy.
4.  **Backup** The return generated by the simulated episode is backed up to update, or initialize, the action values attached to the edges of the tree traversed by the tree policy. **No values are saved for the states and actions visited by the rollout policy beyond the tree**.


## On-policy Prediction with Approximation {#on-policy-prediction-with-approximation}

This chapter begins the study of function approximation in reinforcement learning, where the estimate of the value function \\(v\_\pi\\) and policy \\(\pi\\) could be a parameterized functional with weight vector \\(\wvec\in\reals^d\\). \\(\hat{v}(s,\wvec) \approx v\_\pi(s)\\). Typically the number of weights is much less than the number of states (\\(d \ll |\states|\\)).


### Value-function Approximation {#value-function-approximation}

We will refer to an individual update by the notation \\(s \mapsto u\\) where \\(s\\) is the state updated, and \\(u\\) is the update target. For example,

-   the Monte Carlo update for value prediction: \\(S\_t \mapsto G\_t\\),
-   the TD(0) update: \\(S\_t \mapsto R\_{t+1} + \gamma\hat{v}(S\_{t+1}, \wvec\_t)\\),
-   n-step TD update: \\(S\_t\mapsto G\_{t:t+n}\\).
-   DP policy-evaluation update: \\(s\mapsto \expected\_{\pi}[R\_{t+1} + \gamma \hat{v}(S\_{t+1}, \wvec\_t) | S\_t = s]\\).


### The Prediction Objective (\\(\bar{VE}\\)) {#the-prediction-objective--bar-ve}

The most obvious objective is the _Mean Squared Value Error_ \\(\overline{VE}\\), where it is constructed as you would expect, except weighted by the state distribution induced by the behavior

\begin{equation} \label{eqn:RLI:VE}
\overline{VE}(\wvec) \defeq \sum\_{s\in\states} \mu(s) \left[ v\_{\pi}(s) - \hat{v}(s, \wvec) \right]^2
\end{equation}

The square root of this measure gives a rough measure of how much the approximate values differ from the true values and is often used in plots.

<div class="tcolorbox">

In an episodic task, the on-policy distribution depends on how the initial states of the episodes are chosen. Let \\(h(s)\\) be the starting state distribution,

\begin{align\*}
	\eta(s) &= h(s) + \sum\_{\bar{s}} \eta(\bar{s}) \sum\_{a} \pi(a|\bar{s}) p(s|\bar{s}, a) \\\\
	\mu(s) &= \frac{\eta(s)}{\sum\_{s'} \eta(s')}, \text{ for all } s\in\states
\end{align\*}

When there is discounting, \\(\gamma\\) can be included in the second term of \\(\eta(s)\\).

</div>


### Stochastic-gradient and Semi-gradient Methods {#stochastic-gradient-and-semi-gradient-methods}

This is a pretty straightforward derivation of gradient Monte Carlo and semi-gradient TD(0).

<div class="algorithm">

\begin{algorithmic}
\Require the policy $\pi$ to be evaluated
\Require a differentiable function $\hat{v}: \states \times \reals^d \rightarrow \reals$ \\\\
\Comment step size $\alpha > 0$\\\\
\Comment Initialize value-function weights $\wvec\in\reals^d$ arbitrarily
\Loop forever (for each episode)
\State Generate an episode using $\pi$
\For{each step of episode}
\State $\wvec \leftarrow \wvec + \alpha [G\_t - \hat{v}(S\_t,\wvec)]\nabla \hat{v}(S\_t, \wvec)$
\EndFor
\EndLoop
\end{algorithmic}

\caption{Gradient Monte Carlo Algorithm}

</div>

<div class="algorithm">

\begin{algorithmic}
\Require the policy $\pi$ to be evaluated
\Require a differentiable function $\hat{v}: \states \times \reals^d \rightarrow \reals$ \\\\
\Comment step size $\alpha > 0$\\\\
\Comment Initialize value-function weights $\wvec\in\reals^d$ arbitrarily
\Loop{forever (for each episode)}
\State Initialize S
\For{each step of episode}
\State Choose $A \sim \pi(\cdot|S)$
\State Take action $A$, observe $R, S'$
\State $\wvec \leftarrow \wvec + \alpha [R + \gamma\hat{v}(S', \wvec) - \hat{v}(S,\wvec)]\nabla \hat{v}(S\_t, \wvec)$
\State $S \leftarrow S'$
\EndFor
\EndLoop
\end{algorithmic}

\caption{Semi-gradient TD(0) Algorithm}

</div>


### Linear Methods {#linear-methods}

One special case of function approximation is where the approximate value is a linear function of the weight vector.

-   \\(\hat{v}(s, \wvec) =  \wvec^\trans x(s)\\)
-   \\(\nabla\hat{v}(s, \wvec) = x(s)\\)

\begin{equation}\label{eqn:RLI:linear-update}
\wvec\_{t+1} = \wvec\_t + \alpha [U\_t - \hat{v}(S\_t, \wvec\_t)]x(S\_t)
\end{equation}

Under linear function approximation the Monte Carlo algorithm presented above converges to the global optimum of the \\(\overline{VE}\\) objective under the normal constraints.

Semi-gradient TD(0) also converges, but to a local optimum. See the box for more details.

<div class="tcolorbox">

We first need to rewrite the above update \ref{eqn:RLI:linear-update}

\\[\wvec\_{t+1} = \wvec\_t + \alpha\left( R\_{t+1} \xvec\_t - \xvec\_t(\xvec\_t - \gamma\xvec\_{t+1})^\trans \wvec\_t \right)\\]

Once the system reaches a steady state, the expected next weight vector can be written

\\[\expected[\wvec\_{t+1}|\wvec\_t] = \wvec\_t + \alpha(\bvec - \Amat\wvec\_t)\\]

where

\\[\bvec \defeq \expected[R\_{t+1}\xvec\_t] \in \reals^d \text{ and } \Amat\defeq \expected\left[ \xvec\_t(\xvec\_t - \gamma \xvec\_{t+1})^\trans\right]\in\reals^d\times\reals^d  \\]

This system must then converge to (if it converges at all) \\(\wvec\_{TD} \defeq \Amat^\inv \bvec\\).

What sorts of properties are required for convergence? By rewriting the expected next weight vector

\\[\expected[\wvec\_{t+1}|\wvec\_t] = (\eye - \alpha\Amat)\wvec\_t + \alpha\bvec\\]

we can see that \\(\Amat\\) is the only important component for convergence. Consider a special case where \\(\Amat\\) is a diagonal matrix. If any of the components are negative, then the corresponding diagonal element of \\(\eye - \alpha\Amat\\) will be greater than one, and the corresponding component of \\(\wvec\_t\\) will be amplified leading to divergence. In general, we can say \\(\wvec\_t\\) will converge whenever \\(\Amat\\) is _positive definite_ (i.e. \\(y^\trans\Amat y\\) for any \\(y\neq 0\\)). The rest of the proof follows once we know \\(\Amat\\) is _positive definite_.

We can rewrite this matrix:

\begin{align\*}
\Amat
&= \sum\_s \mu(s) \sum\_a \pi(a|s) \sum\_{r,s'} p(r, s'|s, a)\xvec(s)(\xvec(s) - \gamma \xvec(s'))^\trans \\\\
&= \sum\_s \mu(s)\xvec(s) \left( \xvec(s) - \gamma \sum\_{s'} p(s'|s)\xvec(s') \right) \\\\
&= \Xmat^\trans \Dmat (\eye - \gamma \Pmat)\Xmat
\end{align\*}

From here, it is clear that the inner matrix is key to determining the positive definiteness of \\(\Amat\\). It has been shown prior that a matrix of this form is positive definite if all of its columns sum to a nonnegative number. See (<a href="#citeproc_bib_item_4">Sutton 1988</a>) for a detailed proof. Also note that \\(\muvec\\), which is the \\(|\states|\\) vector of the \\(\mu(s)\\) distribution, is a stationary distribution thus \\(\muvec = \Pmat^\trans\muvec\\) The column sums of this matrix is then:

\begin{align\*}
\mathbf{1}^\trans \Dmat(\eye - \gamma \Pmat)
&= \muvec^\trans(\eye - \gamma \Pmat) \\\\
&= \muvec^\trans - \gamma \muvec^\trans \Pmat \\\\
&= (1-\gamma)\muvec^\trans
\end{align\*}

All the components of \\((1-\gamma)\muvec^\trans\\) are positive, and therefore \\(\Amat\\) is positive definite, and TD(0) is stable.

It has also been shown at the TD fixed point that the \\(\overline{VE}\\) is within a bounded expansion of the lowest possible error.

\\[\overline{VE}(\wvec\_{TD}) \leq \frac{1}{1-\gamma} \min\_{\wvec} \overline{VE}(\wvec)\\]

</div>

<div class="algorithm">

\begin{algorithmic}
\Require the policy $\pi$ to be evaluated
\Require a differentiable function $\hat{v}: \states \times \reals^d \rightarrow \reals$
\Require All store and access operations ($S\_t$ and $R\_t$) can take their index mod $n+1$ \\\\
\Comment step size $\alpha > 0$\\\\
\Comment Initialize value-function weights $\wvec\in\reals^d$ arbitrarily
\For{each episode}
\State Initialize and store $S\_0 \neq \text{terminal}$
\State $T \leftarrow \infty$
\Repeat
\If{t < T}
\State Take an action according to $\pi(\cdot|S\_t)$
\State Observe and store $R\_{t+1}$ and $S\_{t+1}$
\State If $S\_{t+1}$ is terminal, then $T \leftarrow t+1$
\EndIf
\State $\tau \leftarrow t - n + 1$
\Comment $\tau$ is the time whose state's estimate is being updated
\If{$\tau \geq 0$}
\State $G \leftarrow \sum\_{i=\tau+1}^{\min(\tau + n, T)} \gamma^{i-\tau-1} R\_i$
\State If $\tau + n < T$, then: $G \leftarrow G+\gamma^{n} \hat{v}(S\_{\tau + n}, \wvec)$
\State $\wvec \leftarrow \wvec + \alpha [G - \hat{v}(S,\wvec)]\nabla \hat{v}(S\_t, \wvec)$
\EndIf
\Until{$\tau = T-1$}
\EndFor
\end{algorithmic}

\caption{n-step Semi-gradient TD Algorithm}

</div>


### Feature Construction for Linear Methods {#feature-construction-for-linear-methods}

This section is exactly what you would expect. It lays out a number of ways to construct features for a reinforcement learning agent.

<!--list-separator-->

-  Polynomials

    This is straightforward, and takes advantage of the Taylor series formulation. This formulation can represent highly-complex interactions among the problem's state dimensions.

    Suppose each state s corresponds to k numbers, \\(\\{s\_1, s\_2, \ldots, s\_k\\}\\), with each \\(s\_i \in \reals\\). For a k-dimensional state space, each order-n polynomial-basis feature \\(x\_i\\) can be written as:

    \\[x\_i(s) = \prod\_{j=1}^k s\_j^{c\_i,j} \text{ where } c\_{i,j} \in \\{0,1,\ldots,n\\}\\]

    Just like a Taylor series, more polynomials will be more accurate at the cost of storing such order-n polynomial functions (which grow exponentially with \\(k\\)).

<!--list-separator-->

-  Fourier Basis

    This feature creation technique is based on the Fourier series. You can represent any _even_ function, or a function which is symmetric about the origin with interval \\([0,\tau/2]\\), with only a cosine basis. You can represent an _odd_ function with only sinusoidal basis. We focus on _even_ functions here, setting \\(\tau=2\\) so the features are defined over the half-&tau; interval \\([0,1]\\). The one-dimensional order-n Fourier cosine basis is

    \\[x\_i = cos(i\pi s), s\in[0,1], i = 0, \ldots, n\\]

    This can also be applied in the multi-dimensional state case as well, but not discussed in these notes (see (<a href="#citeproc_bib_item_5">Sutton and Barto 2018</a>) page 213).

    If using a Fourier cosine feature creation method, it has been found useful to define a learning rate for each feature separately. (<a href="#citeproc_bib_item_2">Konidaris, Osentoski, and Thomas 2011</a>) suggest setting the learning rate parameter for features \\(x\_i\\) to \\(\alpha\_i = \alpha/\sqrt{(c^i\_1)^2 + \ldots + (c^i\_k)^2}\\).

<!--list-separator-->

-  Coarse Coding

    Coarse coding is a simple idea. The basic idea is to have a bunch of overlapping "areas" (or "receptive fields"), which correspond to features in a large binary feature vector. When a state is within a certain region, the feature is said to be _present_ and has an active unit within the feature vector.

    **Properties**:

    -   If we train at one state, a point in the space, then the weights of all overlapping fields will be affected by a learning update. The approximate value function will be affected at all states within the union of the fields, with a greater effect the more circles a point has "in common" with the state.
    -   If the RFs are small, the generalization will be over a short distance.
    -   If the RFs are large, the generalization will be over a large distance.
    -   The shape of the field will determine the nature of the generalization.
    -   Features with large receptive fields give broad generalization, but might also seem to limit the learned function to a coarse approximation. This is not necessarily the case as initial generalization from one point to another is controlled by the size and shape of RFs, but acuity is controlled by the total number of overlapping features.

    <!--list-separator-->

    -  Tile Coding

        This is a simple form of coarse coding, which automatically creates a set of tilings. Each of which tile the space through state aggregation. The power comes in the off-set of the tilings, where this creates a number of overlapping (but not completely) RFs which can be used in learning.

        I won't go into details here, but this is obviously one of Rich's favorites, as the explanation is long and much more complete as compared to other feature creating techniques. If you look at the results, the Fourier basis does surprisingly similar to the tile coding with 50 tilings in the simple example.

    <!--list-separator-->

    -  Radial Basis Functions

        Radial basis functions (RBFs) are a natural instantiation of coarse coding with continuous-valued features. Rather than a feature being 0 or 1, it can be anything in the interval representing the closeness to the center of a receptive field represented through a gaussian function. If the feature is 1 then the feature represents the "center" or "prototype" of the gaussian. This is similar to a kernel representation, although the kernel prototypes here are not not necessarily chosen through a principled algorithm. More on kernel-based function approximation below.


### Selecting Step-Size Parameters Manually {#selecting-step-size-parameters-manually}

An ok rule of thumb is:

\\[\alpha \defeq (\tau \expected[\xvec^\trans \xvec])^\inv\\].

In coarse coding this simply resolves to
\\[\alpha = \frac{1}{\tau \times \text{number of active features (tilings)}}\\]


### Nonlinear Function Approximation: Artificial Neural Networks {#nonlinear-function-approximation-artificial-neural-networks}

This is a straightforward treatment of ANNs, although this book is quite biased towards linear methods as exemplified by the sheer lack of details in this sections. There are many other books that go through these much clearer, specifically for RL (<a href="#citeproc_bib_item_1">François-Lavet et al. 2018</a>).


### Least-Squares TD {#least-squares-td}

Least-squares TD is a straightforward algorithm which solves for the fixed point weights (i.e. \\(\wvec\_{TD} = \Amat^\inv \bvec\\)) directly rather than through an iterative process. As a reminder

\\[\bvec \defeq \expected[R\_{t+1}\xvec\_t] \in \reals^d
   \quad \text{ and } \quad
   \Amat \defeq \expected\left[ \xvec\_t(\xvec\_t - \gamma \xvec\_{t+1})^\trans\right] \in \reals^d\times\reals^d  \\]

which can be estimated relatively straightforwardly given a trajectory of data:

\begin{equation}
\widehat{\bvec}\_{t} = \frac{1}{t}\sum\_{k=0}^{t-1} R\_{k+1} \xvec\_{k}
\quad \text{ and } \quad
\widehat{\Amat}\_{t} = \frac{1}{t}\sum\_{k=0}^{t-1} \xvec\_{k}\left(\xvec\_{k}-\gamma \xvec\_{k+1}\right)^{\top}+\varepsilon \mathbf{I}
\end{equation}

We can estimate just the sums, without taking average, as when creating the weight vector the average cancels out.

\\[\wvec\_t \defeq \widehat{\Amat}\_t^\inv \widehat{\bvec}\_t \\]

The major computational component of this algorithm is the inverse of the matrix \\(\widehat{\Amat}\\). This can be side stepped through the Sherman-Morrison formula (see more details in the box).

\begin{equation}
\widehat{\Amat}\_t^\inv =
\widehat{\Amat}\_{t-1}^\inv -
\frac{\widehat{\Amat}\_{t-1}^\inv \xvec\_t(\xvec\_t - \gamma \xvec\_{t+1})^\trans \widehat{\Amat}\_{t-1}^\inv}
{1 + (\xvec\_t - \gamma\xvec\_{t+1})^\trans \widehat{\Amat}\_{t-1}^\inv \xvec\_t}
\end{equation}

<div class="tcolorbox">

\begin{theorem}
Suppose $\Amat \in \reals^{n \times n}$ is an /invertable square matrix/ and $\uvec, \vvec \in \reals^n$ are column vectors. Then $\Amat + \uvec\vvec^\trans$ is invertable iff $1 + \vvec^\trans\Amat^\inv\uvec \neq 0$. Specifically,

\\[(\Amat + \uvec\vvec^\trans)^\inv = \Amat^\inv - \frac{A^\inv \uvec\vvec^\trans \Amat^\inv}{1+\vvec^\trans\Amat^\inv\uvec}\\]

\end{theorem}

\begin{proof}

We prove this in the backward direction, and do this by verifing the properties of the inverse. Specifically ($\Xmat = (\Amat + \uvec\vvec^\trans)$),

\begin{align\*}
\Xmat\Xmat^\inv
&= (\Amat + \uvec\vvec^\trans)\left(\Amat^\inv - \frac{A^\inv \uvec\vvec^\trans \Amat^\inv}{1+\vvec^\trans\Amat^\inv\uvec} \right) \\\\
&= \Amat\Amat^\inv + \uvec\vvec^\trans \Amat^\inv -
   \frac{\Amat\Amat^\inv\uvec\vvec^\trans\Amat^\inv + \uvec\vvec^\trans\Amat^\inv\uvec\vvec^\trans\Amat^\inv}
        {1 + \vvec^\trans\Amat^\inv\uvec} \\\\
&= \eye + \uvec\vvec^\trans \Amat^\inv -
   \frac{\uvec(1 + \vvec^\trans\Amat^\inv\uvec)\vvec^\trans\Amat^\inv}
        {1 + \vvec^\trans\Amat^\inv\uvec} \\\\
&= \eye + \uvec\vvec^\trans \Amat^\inv - \uvec\vvec^\trans \Amat^\inv
\hspace{1cm} \triangleright 1 + \vvec^\trans \Amat^\inv \uvec \in \reals, \neq 0 \\\\
&= \eye
\end{align\*}

Reciprocally, if $1 + \vvec^\trans \Amat^\inv \uvec = 0$, then $x=\Amat^\inv\uvec$, we can see $(\Amat + \uvec\vvec^\trans)x = 0$ and therefore $(\Amat + \uvec\vvec^\trans)$ has a non-trivial kernel and is therefore not invertible.

\href{https://en.wikipedia.org/wiki/Sherman–Morrison\_formula}{wikipedia}

\end{proof}

</div>


### Memory-based Function Approximation {#memory-based-function-approximation}

This approach does not update a parametric function towards some objective. Instead it stores examples of transitions/states and their corresponding value estimate. When a new state arrives the value is estimated through a set of examples which are similar to the state. This is sometimes called _lazy learning_.

Some approaches:

-   Nearest neighbor
-   Weighted average
-   Locally weighted regression


### Kernel-based Function Approximation {#kernel-based-function-approximation}

This is the typical Kernel regression formulation.


### Looking Deeper at On-policy Learning: Interest and Emphasis {#looking-deeper-at-on-policy-learning-interest-and-emphasis}

Instead of treating each state uniformly, we can also treat states according to some _interest_ function \\(I\_t\\) indicating the degree to which we are interested in accurately.

\begin{align\*}
\wvec\_{t+n} &\defeq \wvec\_{t+n-1} + \alpha M\_t[G\_{t:t+n} - \hat{v}(S\_t, \wvec\_{t+n-1})]\nabla \hat{v}(S\_t, \wvec\_{t+n-1}), 0\leq t < T \\\\
M\_t &= I\_t + \gamma^n M\_{t-1}
\end{align\*}


## Chapter 10 {#chapter-10}


## Chapter 11 {#chapter-11}


## <span class="org-todo todo TODO">TODO</span> Eligibility Traces {#sec:RLI:traces}


## Policy Gradient Methods {#policy-gradient-methods}

This chapter considers policy gradient methods, or methods which search for the policy directly rather than through an _action-value methods_. The policy gradient methods directly parameterize a policy to select actions (either deterministically or through some stochastic process).

The notation is standard in this chapter:

-   \\(\thetavec \in \reals^{d'}\\) for the policy's parameter vector,
-   \\(\pi(a|s,\thetavec) = \text{Pr}\\{A\_t=a | S\_t=s, \thetavec=\theta\\}\\) for the probability that action a is taken at time t given the parameterization and state of the environment,
-   \\(\wvec \in \reals^d\\) is the value function parameterization where \\(\hat{v}(s,\wvec)\\) is the estimated value.

The methods considered here look to maximize some performance measure \\(J(\thetavec)\\) with respect to the policy parameter through gradient ascent.

\\[\Delta\thetavec = \alpha \nabla J(\thetavec\_t) \approx \alpha \hat{\nabla J(\thetavec\_t)}\\]

where \\(\hat{\nabla J(\thetavec\_t)}\\) is the stochastic estimate of the gradient wrt the objective and policy parameterization.

-   _Policy gradient method_: any method which directly parameterizes a policy and learns through maximizing some objective function.
-   _actor-critic method_: A policy gradient method which also learns an estimate of the value function.

The only requirement for a policy gradient method is \\(\pi(a|s, \thetavec)\\) must be continuous and differentiable wrt its parameters over all \\(a\in\actions, s\in\states\\). We also never want the policy to become deterministic!


### Policy approximation and its advantages {#policy-approximation-and-its-advantages}

The most natural of parameterization is to form parameterized numerical preferences \\(h(s,a,\thetavec)\in\reals\\). The policy is then defined through the soft-max distribution called the _soft-max in action preferences_:

\\[\pi(a|s, \thetavec) = \frac{e^(h(s,a,\thetavec))}{\sum\_{a'} h(s,a',\thetavec)}\\].

Some advantages:

-   The approximate policy can approach a deterministic policy (as opposed to something like &epsilon;-greedy).
-   Enables the selection of actions with arbitrary probabilities. In problems with significant function approximation, the best approximate policy may be stochastic (for example Poker).
-   The policy may be a simpler function to approximate as opposed to the value function.
-   The selection of a policy parameterization could be a good way of injecting prior knowledge about the desired form of the policy.


### The Policy Gradient Theorem {#the-policy-gradient-theorem}

With a continuous policy parameterization the action probabilities change smoothly as a function of the learned parameters! Because of this, much stronger theoretical guarantees are available for policy-gradient methods than for action-value methods.

**Episodic case:**
The performance measure:
\\[J(\thetavec) =  v\_{\pi\_{\thetavec}}(s\_0)\\]

The challenge in policy gradients is the performance depends of both the action selections and the distribution of states in which those selections are made. Unfortunately, both of these are affected by the policy parameter, which means a straightforward gradient estimate requires intimate knowledge of the state distribution induced by the current policy.

The policy gradient theorem for the episodic case establishes an expression for the gradient which does not depend on the state distribution.

\\[\nabla J(\thetavec) \propto \sum\_s \mu(s) \sum\_a q\_{\pi}(s,a) \nabla \pi(a|s,\thetavec)\\]

The constant of proportionality is the average length of an episode.


### REINFORCE {#reinforce}

**All-actions Method:** The rhs of the policy gradient theorem is a sum over states weighted by how often the states occur under the target policy \\(\pi\\); if \\(\pi\\) is followed, then states will be encountered in these proportions, therefore

\\[\nabla J(\thetavec) \propto \mathbb{E}\_\pi \left[\sum\_a q\_{\pi}(S\_t, a) \nabla \pi(a|S\_t, \thetavec) \right]\\]

We could stop here and instantiate stochastic gradient ascent here, where we approximate the value function. We can continue down the line of reasoning presented in the policy gradient theorem and remove the weighting of the policy and replace the value function with the return. This results in

\\[\nabla J(\thetavec) \approx \mathbb{E}\_\pi \left[ G\_t \frac{\nabla \pi(A\_t | S\_t \thetavec)}{\pi(A\_t | S\_t \thetavec)} \right]\\]

yielding the REINFORCE with Monte Carlo update (<a href="#citeproc_bib_item_7">Williams 1992</a>):

\\[\Delta \theta\_t = \alpha G\_t \frac{\nabla \pi(A\_t | S\_t \thetavec)}{\pi(A\_t | S\_t \thetavec)} \\]

We can change out the comparison of the action value to an arbitrary baseline b(s) resulting in an update

\\[\Delta \theta\_t = \alpha (G\_t - b(S\_t)) \frac{\nabla \pi(A\_t | S\_t \thetavec)}{\pi(A\_t | S\_t \thetavec)} \\]

This baseline can be learned or set.


### Actor-critic {#actor-critic}

We can use the same methods used for TD(0), Sarsa(0), and other algorithms for estimating the return and using it as a critic in the policy gradient framework.

\begin{align\*}
\Delta \theta\_t
&= \alpha (G\_{t:t+1} - \hat{v}(S\_t|\wvec)) \frac{\nabla \pi(A\_t | S\_t \thetavec)}{\pi(A\_t | S\_t \thetavec)} \\\\
&= \alpha (R\_{t+1} + \gamma \hat{v}(S\_{t+1}|\wvec) - \hat{v}(S\_t|\wvec)) \frac{\nabla \pi(A\_t | S\_t \thetavec)}{\pi(A\_t | S\_t \thetavec)} \\\\
&= \alpha \delta\_t \frac{\nabla \pi(A\_t | S\_t \thetavec)}{\pi(A\_t | S\_t \thetavec)}
\end{align\*}

This generalizations for n-step and &lambda;-return methods is straightforward, and not specified in these notes. See page 332 of (<a href="#citeproc_bib_item_5">Sutton and Barto 2018</a>)


### Policy Gradient for Continuing Problems {#policy-gradient-for-continuing-problems}

The performance metric for the continuing problem is in terms of the average rate of reward per time step:

\\[J(\thetavec) \defineq r(\pi) \defineq \lim\_{h\rightarrow\infty} \frac{1}{h} \expected [R\_t| S\_0, A\_{0:t-1} \sim \pi] \\]

As in the episodic case, the policy gradient theorem results in a gradient equation which is devoid of the gradient of the stationary distribution, and is in fact the same as above.


### Policy Parameterization for Continuous Actions {#policy-parameterization-for-continuous-actions}

We can parameterize the policy according to the parameters of a distribution, or other such approaches. This is pretty straightforward.


## Chapter 14 {#chapter-14}


## Chapter 15 {#chapter-15}


## Chapter 16 {#chapter-16}


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>François-Lavet, Vincent, Peter Henderson, Riashat Islam, Marc G. Bellemare, and Joelle Pineau. 2018. “An Introduction to Deep Reinforcement Learning.” <i>Foundations and Trends® in Machine Learning</i> 11 (3-4): 219–354. doi:<a href="https://doi.org/10.1561/2200000071">10.1561/2200000071</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Konidaris, George, Sarah Osentoski, and Philip Thomas. 2011. “Value Function Approximation in Reinforcement Learning Using the Fourier Basis.” In <i>Twenty-Fifth AAAI Conference on Artificial Intelligence</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Singh, Satinder, and Richard Sutton. 1996. “Reinforcement Learning with Replacing Eligibility Traces.” <i>Machine Learning</i> 22 (1): 123–58. doi:<a href="https://doi.org/10.1023/A:1018012322525">10.1023/A:1018012322525</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>Sutton, Richard. 1988. “Learning to Predict by the Methods of Temporal Differences.” <i>Machine Learning</i> 3 (1): 9–44. doi:<a href="https://doi.org/10.1007/BF00115009">10.1007/BF00115009</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>Sutton, Richard, and Andrew G. Barto. 2018. <i>Reinforcement Learning: An Introduction</i>. Second edition. Adaptive Computation and Machine Learning Series. Cambridge, Massachusetts: The MIT Press.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_6"></a>Tesauro, Gerald. 1994. “TD-Gammon, a Self-Teaching Backgammon Program, Achieves Master-Level Play.” <i>Neural Computation</i> 6: 215–19.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_7"></a>Williams, Ronald J. 1992. “Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning.” In <i>Reinforcement Learning</i>, 5–32. The Springer International Series in Engineering and Computer Science. Springer, Boston, MA. doi:<a href="https://doi.org/10.1007/978-1-4615-3618-5_2">10.1007/978-1-4615-3618-5_2</a>.</div>
</div>
