+++
title = "Dynamic Programming"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:26:18-07:00
slug = "dynamic_programming"
draft = false
notetype = "note"
+++

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

**Dynamic programming** (DP) refers to a collection of algorithms that can be used to compute optimal policies given a _perfect model_ of the environment as an MDP. These algorithms are of limited use to the full RL problem as they require a perfect model and have an immense up-front computational cost. These algorithms are still interesting theoretically, and provide a nice foundation to begin thinking about learning optimal policies. In this chapter, we will limit ourselves to finite MDPs. A key idea of DP, and of RL generally, is the use of value functions to organize and structure the search for good policies.


## Policy Evaluation (prediction) {#policy-evaluation--prediction}

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


## Policy Improvement {#policy-improvement}

Once we have a state value function \\(v\_\pi\\), we would like to use it to find a better policy (if one exists). The most straightforward method is to construct an action value function

\\[q\_\pi(s,a) \defeq \expected[R\_{t+1} + \gamma v\_\pi(S\_{t+1}) | S\_t =s, A\_t = a].\\]

If \\(q\_\pi(s,a) > v\_\pi(s)\\) then you can improve the policy \\(\pi\\) by selecting action \\(a\\) in state \\(s\\) and then following \\(\pi\\) elsewhere. This is a special case of the _policy improvement theorem_. Let &pi; and &pi;' be any pair of deterministic policies such that

\\[q\_\pi(s, \pi'(s)) \ge v\_\pi(s) \quad \triangleright \quad \forall s \in \states\\].

Then the policy &pi;' must be as good as, or better than &pi;, meaning \\(v\_{\pi'}(s) \ge v\_\pi(s)\\).

Instead of focusing on changing the policy at a a single state, we can improve the policy over all states simultaneously: \\(\pi' \defeq \argmax\_a q\_\pi(s,a)\\).


## Policy Iteration {#policy-iteration}

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


## Value Iteration {#value-iteration}

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


## Asynchronous Dynamic Programming {#asynchronous-dynamic-programming}

_Asynchronous DP_ algorithms: in-place iterative DP algorithms that are not organized in terms of systematic sweeps of the state set. These algorithms update the values of states in any order whatsoever, using whatever values of other states happen to be available. The only restriction for convergence is an asynchronous algorithm must continue to update the values of all the states.


## Generalized Policy Iteration {#generalized-policy-iteration}

_Generalized policy iteration_ (GPI): the general idea of letting policy-evaluation and policy-improvement porcesses interact, independent of the granularity and other details of the two processes.


## Efficiency of Dynamic Programming {#efficiency-of-dynamic-programming}

If \\(n\\) and \\(k\\) denote the number of states and actions, a DP method takes a number of computational operations that is less than some polynomial function of \\(n\\) and \\(k\\) (i.e. DP methods are in polynomial time). DP is sometimes through to be of limited applicability because of the _curse of dimensionality_, the fact that the number of states often grows exponentially with the number of state variables.
