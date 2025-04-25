+++
title = "Data Driven PDE Solvers"
author = ["Matthew Schlegel"]
lastmod = 2025-04-25T11:12:04-06:00
slug = "data_driven_pde_solvers"
tags = ["DDPDE"]
draft = false
notetype = "research-topic"
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

| citation                                                                       | estimate pde dynamics from data | estimate PDE parameters with model | estimate quantity described by pdes |
|--------------------------------------------------------------------------------|---------------------------------|------------------------------------|-------------------------------------|
| (<a href="#citeproc_bib_item_9">Guo, Li, and Iorio 2016</a>)                   | Y                               | N                                  | N                                   |
| (<a href="#citeproc_bib_item_14">Khoo, Lu, and Ying 2021</a>)                  | N                               | N                                  | Y                                   |
| (<a href="#citeproc_bib_item_31">Raissi, Perdikaris, and Karniadakis 2019</a>) | Y                               | Y                                  | N                                   |
| (<a href="#citeproc_bib_item_17">Kovachki et al. 2024</a>)                     | Y                               | N                                  | N                                   |
| (<a href="#citeproc_bib_item_38">Stiasny et al. 2022</a>)                      | Y                               | Y                                  | N                                   |

| citation                                                                       | example pdes/their field                                                                                                           | Relevant to power systems | Novel NN approaches | Data Simulated |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------|----------------|
| (<a href="#citeproc_bib_item_9">Guo, Li, and Iorio 2016</a>)                   | laminar flow of fluids around geometries                                                                                           | N                         | N (Conv Nets)       | Y              |
| (<a href="#citeproc_bib_item_14">Khoo, Lu, and Ying 2021</a>)                  | [NLSE]({{< relref "partial_differential_equations.md#effective-conductance-in-a-non-homogeneous-media" >}}), Effective Conductance | N                         | N                   | Y              |
| (<a href="#citeproc_bib_item_31">Raissi, Perdikaris, and Karniadakis 2019</a>) | Several                                                                                                                            | Y                         | N                   | Y              |
| (<a href="#citeproc_bib_item_17">Kovachki et al. 2024</a>)                     | Several                                                                                                                            | Y                         | Y                   | Y              |
| (<a href="#citeproc_bib_item_38">Stiasny et al. 2022</a>)                      | [The North Sea Wind Power Hub]({{< relref "power_systems_control.md#the-north-sea-wind-power-hub" >}})                             | Y                         | N                   | Y              |

| citation                                                                       | generative | discriminative | Type of estimate | Category | Discretization Method                                                                 |
|--------------------------------------------------------------------------------|------------|----------------|------------------|----------|---------------------------------------------------------------------------------------|
| (<a href="#citeproc_bib_item_9">Guo, Li, and Iorio 2016</a>)                   | Y          | N              | Field            |          | Grid                                                                                  |
| (<a href="#citeproc_bib_item_14">Khoo, Lu, and Ying 2021</a>)                  | N          | Y              | Scalar           |          | N/A                                                                                   |
| (<a href="#citeproc_bib_item_31">Raissi, Perdikaris, and Karniadakis 2019</a>) | Y          | Y              | Function/Field   |          | [Latin Hypercube Sampling]({{< relref "latin_hypercube_sampling.md" >}}), fixed grid, |
| (<a href="#citeproc_bib_item_17">Kovachki et al. 2024</a>)                     | Y          | N              | Function/Field   |          | Avoids discretization through NN architecture                                         |
| (<a href="#citeproc_bib_item_38">Stiasny et al. 2022</a>)                      | N          | Y              | Function/Field   |          | Discretized on a set \\(\Delta t\\)                                                   |


## Questions/Thoughts {#questions-thoughts}

-   Are there methods for learning from data driven by controllers? How well does this work on real-world data? Can we get better explanations of how the controller performs? Can we learn the implicit PDE of a controller we can't analyze? How do we validate we have learned it correctly?
-   Can Data Driven PDEs be used for explainability in RL? What would that look like? Can we ask counterfactuals or specific stability related questions using
-   Could we learn a mapping from rewards (a function over states) to policies (a function over states and actions) with samples from an off-policy dataset? What does the learning objective look like when we include stochasticity into the input and outputs (or must it only be deterministic?)
-   Could we use a neural operator that learns over the PDE induced by the current agent's policy. This could then be used in the explainability space to understand what we expect the agent to do over time, and simulate the PDE into the future to give confidence to the human operator.
-   Could we use this as input to the agent? What policy would the PDE depend on, maybe a set of experts? How much data would this take to train, and how much data would we need for the subsequent RL learning.
-   How can Neural Operators be used to understand or predict how well an agent will do in the future? Can this be done? How reliable would it be? Would it give a human operator some confidence? Maybe as a comparison with experts.
-   Can the parameters of an expert be a parameter that we can learn over in the set \\(\mathcal{A}\\)? Would we need to smoothly transition between experts? Would we need a new set of parameters per expert?


## Problem Settings {#problem-settings}

In these papers, there are several problem settings that each have their own flavour of solution. Not all of these are relevant to our work, but it is good to have an idea of what all of them are so we can know what kinds of papers are worth incorporating into this literature review.


### Estimate PDE dynamics from data {#estimate-pde-dynamics-from-data}

This is the most difficult problem setting. The goal is to be able to estimate the dynamics of a PDE from a set of conditions or measurements.

One way this plays out is through knowing something about the physical characteristics of the underlying PDE. For instance, one can estimate the steady state flow of fluid around a geometry given a representation of that geometry (<a href="#citeproc_bib_item_9">Guo, Li, and Iorio 2016</a>). The output of the network should be a generative prediction of what the fluid flow output of a simulator would look like.

Another way this can be done is by taking a set of measurements of a system and approximating its dynamics in a discretization agnostic manner as in (<a href="#citeproc_bib_item_17">Kovachki et al. 2024</a>). The interesting part of neural operators is that thy might not need to have knowledge of the underlying physical mechanics as (<a href="#citeproc_bib_item_31">Raissi, Perdikaris, and Karniadakis 2019</a>) or (<a href="#citeproc_bib_item_9">Guo, Li, and Iorio 2016</a>) do. But a problem may arise in needing more data to estimate the actual PDE if it is complicated (my guess).


### Estimate PDE model parameters from data {#estimate-pde-model-parameters-from-data}

The unknonw parameters of a PDE are difficult to ascertain, but by enabling gradients to be informed by the underlying PDEs we could use data to estimate the unknown parameters, or use this information to better estimate other quantities/forecasts (<a href="#citeproc_bib_item_31">Raissi, Perdikaris, and Karniadakis 2019</a>).


### Estimate emergent quantity derived from PDE dynamics {#estimate-emergent-quantity-derived-from-pde-dynamics}

This is not really estimating PDEs, but is related in some ways. In (<a href="#citeproc_bib_item_14">Khoo, Lu, and Ying 2021</a>), they estimate characteristic qualities of a system without needing to model the entire set of dynamics or learn the unknown variables of the underlying PDEs. This could be interesting for a number of applications in power systems related to stability analysis.


## Power Systems domain {#power-systems-domain}

What we should do is:

1.  Organize the larger set of PDE solution methods into subsets based on the above table and general ideas from the literature (i.e. the
2.  Create


### Power flow analysis for steady state grid networks {#power-flow-analysis-for-steady-state-grid-networks}


### Stability Analysis {#stability-analysis}


### Electro-Magnetic Transient Simulation {#electro-magnetic-transient-simulation}

[Electro Magnetic Transient Simulation](https://www.mathworks.com/discovery/emt-simulation.html)


### Co-Simulation {#co-simulation}

Joint simulation of loosely coupled stand-alone sub-simulators


## Power Systems Specific Applications {#power-systems-specific-applications}


### (<a href="#citeproc_bib_item_38">Stiasny et al. 2022</a>) <a href="#citeproc_bib_item_38">2022</a> {#c02149}

Proposes a method that uses (<a href="#citeproc_bib_item_31">Raissi, Perdikaris, and Karniadakis 2019</a>) as it's core regulariztion method. Also requires data to be generated. Does a nice overview of all the problems related to using Machine Learning in power systems and how the community should be transparent in their research.

This paper mostly has a nice trove of papers they cite which applies PINNs to power systems, and other applications of NNs in power systems (including work on generating formal/informal guarantees on a NNs outputs).


### (<a href="#citeproc_bib_item_2">Bertozzi et al. 2024</a>) <a href="#citeproc_bib_item_2">2024</a> {#42f9f3}

This is an ok review paper for a broad look at power systems research using data driven techniques. It does have some nice papers cited that
should be looked through.

Generally, they don't provide their own contribution a part from the review (the organization is surface level).


### (<a href="#citeproc_bib_item_25">Misyris, Venzke, and Chatzivasileiadis 2020</a>) <a href="#citeproc_bib_item_25">2020</a> {#cf9497}

This is a direct application of physics informed neural networks (<a href="#citeproc_bib_item_31">Raissi, Perdikaris, and Karniadakis 2019</a>) onto the [Single Machine Infinite Bus system]({{< relref "power_systems_control.md#single-machine-infinite-bus-system" >}}). The swing equation for this toy example is

\\[
m\_1 \ddot{\delta} + d\_1 \dot{\delta} + B\_{12} V\_1 V\_2 \text{sin}(\delta) - P\_1 = 0
\\]

with the equations being incorporated in through the equations

\begin{align}
u\_\theta(t,x) &=& \delta(t, P\_1) \\\\
f\_\delta(t, P\_1) = m\_1 \ddot{\delta} + d\_1 \dot{\delta} + B\_{12}V\_1V\_2 \text{sin}(\delta) - P\_1
\end{align}

Where U is parameterized by weights \\(\theta \subset \reals\\) and the partials \\(\ddot{\delta}\\) and \\(\dot{\delta}\\) are taken with respect to time through an autodiff package.

I highly recommend looking at <https://github.com/gmisy/Physics-Informed-Neural-Networks-for-Power-Systems> for more details on how this is implemented. Specifically in the \`net_f\` functions.

They do experiments in inference (when \\(m\_1\\) and \\(d\_1\\) are known), and in identification where \\(m\_1\\) and \\(d\_1\\) are unknown and need to be identified.


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_40">Stiasny, Misyris, and Chatzivasileiadis 2021</a>) {#599f02}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_39">Stiasny, Chevalier, and Chatzivasileiadis 2021</a>) {#603c70}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_28">Pagnier and Chertkov 2021</a>) {#b1861e}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_27">Nellikkath and Chatzivasileiadis 2022</a>) {#21f611}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_26">Nellikkath and Chatzivasileiadis 2021</a>) {#0fbea6}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_41">Stiasny, Misyris, and Chatzivasileiadis 2023</a>) {#488058}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_42">Stock et al. 2024</a>) {#978024}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_35">Singh et al. 2020</a>) {#ba300a}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_7">Donon et al. 2019</a>) {#db075f}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_36">Singh, Kekatos, and Giannakis 2022</a>) {#54d2d9}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_21">Lin, Liu, and Zhu 2022</a>) {#f301b0}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_10">Huang and Wang 2023</a>) {#86f46c}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_8">Feng et al. 2025</a>) {#9a4c72}


### Other resources to look through {#other-resources-to-look-through}

<!--list-separator-->

-  <http://www.chatziva.com/>

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  <https://zicokolter.com/publications/>


## Finite-dimensional operators (i.e. approximate the parametric map through convolutional networks) {#finite-dimensional-operators--i-dot-e-dot-approximate-the-parametric-map-through-convolutional-networks}


### (<a href="#citeproc_bib_item_9">Guo, Li, and Iorio 2016</a>) <a href="#citeproc_bib_item_9">2016</a> {#6c4cab}

This paper focuses on using convolutional neural networks to estimate the stead state laminar flow of air around arbitrary geometries. The main idea is to use supervised learning to estimate the output of an [LCB]({{< relref "lattice_boltzmann_method.md" >}}) simulator and shorten the inference time of the design side. This paper is very specific to aerodynamics, and likely can't be extended to [Power Systems Control]({{< relref "power_systems_control.md" >}}). There are several issues that cannot be overcome.

In any case, the pattern being set is gather data from a simulation and speed up inference time through an architecture and objective function designed for the problem setting.


### (<a href="#citeproc_bib_item_14">Khoo, Lu, and Ying 2021</a>) <a href="#citeproc_bib_item_14">2021</a> {#90b9b1}

This paper focuses on two PDEs from physics:

-   [Effective conductance in a non-homogeneous media]({{< relref "partial_differential_equations.md#effective-conductance-in-a-non-homogeneous-media" >}})
-   [Nonlinear Schrodinger Equation]({{< relref "partial_differential_equations.md#nonlinear-schrodinger-equation" >}})

The main goal is to estimate a quantity described by these PDEs and their **random** coefficients. Usually, Monte-carlo sampling is typically used for this problem, which has an inherently noisy estimate of the desired quantities.


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_11">Jiang et al. 2020</a>) <a href="#citeproc_bib_item_11">2020</a> {#3dde51}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_1">Adler and Öktem 2017</a>) <a href="#citeproc_bib_item_1">2017</a> {#6cba6c}


### Side Ideas: {#side-ideas}

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  (<a href="#citeproc_bib_item_46">Zhu and Zabaras 2018</a>)

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  Continuous convolution networks (<a href="#citeproc_bib_item_44">Ummenhofer et al. 2019</a>)

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  (<a href="#citeproc_bib_item_3">Bhatnagar et al. 2019</a>)

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  Theoretical analysis of deep neural networks and parametric pdes (<a href="#citeproc_bib_item_18">Kutyniok et al. 2022</a>)


## Physics informed machine learning {#physics-informed-machine-learning}


### (<a href="#citeproc_bib_item_31">Raissi, Perdikaris, and Karniadakis 2019</a>)  <a href="#citeproc_bib_item_31">2019</a> {#301dca}

The main idea of this paper is to use the underlying model derived from prior knowledge of the problem as a regularizer during the training phase of a neural network. This is a accomplished by allowing the auto differentiation tools to propogate through the space and time components of the input to the neural network.

The system looks like

\\[
u\_t + \mathcal{N}[u; \lambda] = 0, x\in \Omega, t\in[0, T]
\\]

Where \\(u(t,x)\\) denotes the latent solution, \\(\mathcal{N}[u; \lambda]\\) is a non-linear operator parameterized by \\(\lambda\\), and \\(T, \Omega\\) define the boundary spaces as a subset of the reals.

This paper also introduces a nice set of categories for data driven approaches to solving PDEs:

-   **Data-driven solutions of partial differential equations**: Inference, filtering, and smoothing. Given a fixed model parameters \\(\lambda\\), what can be said about the unknown hidden state \\(u(t,x)\\) of the system?
-   **Data-driven discovery of partial differential equations**: which is learning, system identification, or data-driven discovery of PDEs, i.e. _What are the parameters \\(\lambda\\) which best describe the observed data?_


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_12">Karniadakis et al. 2021</a>) {#e2a9f5}


## Neural Operators {#neural-operators}


### <span class="org-todo todo IN_PROGRESS">IN-PROGRESS</span> (<a href="#citeproc_bib_item_17">Kovachki et al. 2024</a>) {#b3a0d4}

Neural operators are designed to learn general solutions for maps between two function spaces and to be discretization-invariant. Current data-driven solutions using neural networks are not discretization invariant and often require new networks/datasets/training for different levels of discretization. Neural operators describe a process to estimate these maps with the following properties:

1.  acts on any discretization of the input function, i.e. accepts any set of points in the input domain,
2.  can be evaluated at any point of the output domain
3.  converges toa  continuum operator as the discretization is refined. (Converging to a continuum operator means that as the discretization is refined, the function more closely estimates the true continuous function).


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_5">Chen et al. 2025</a>) {#5ca6c2}


## DeepONets {#deeponets}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_23">Lu et al. 2021</a>) {#5856f8}


###  {#d41d8c}


## Non-neural network approaches {#non-neural-network-approaches}


## Non-data-driven approaches {#non-data-driven-approaches}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_24">Matthies and Keese 2005</a>) {#407988}


## Uncatogorized [ General Learning Approaches ] {#uncatogorized-general-learning-approaches}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_22">Long et al. 2018</a>) {#8b92f3}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_32">Rico-Martinez, Anderson, and Kevrekidis 1994</a>) {#044534}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_19">Lagaris, Likas, and Fotiadis 1998</a>) {#2b784b}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_30">Psichogios and Ungar 1992</a>) {#f282f3}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_34">Rudy et al. 2017</a>) {#e8134d}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_29">Parish and Duraisamy 2016</a>) {#d0a3c8}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_20">Lin, Tegmark, and Rolnick 2017</a>) {#a568ed}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_16">Kondor and Trivedi 2018</a>) {#8ad041}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_45">Vlachas et al. 2018</a>) {#42cd59}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_4">Carleo and Troyer 2017</a>) {#95e2e8}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_6">Cheng et al. 2013</a>) {#b62e17}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_13">Khoo, Lu, and Ying 2018</a>) {#05406c}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_33">Rudd and Ferrari 2015</a>) {#da849f}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_37">Stefanou 2009</a>) {#42bd1f}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_43">Torlai and Melko 2016</a>) {#eb898e}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_15">Kondor 2018</a>) {#60d292}


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Adler, Jonas, and Ozan Öktem. 2017. “Solving Ill-Posed Inverse Problems Using Iterative Deep Neural Networks.” <i>Inverse Problems</i> 33 (12). IOP Publishing: 124007. doi:<a href="https://doi.org/10.1088/1361-6420/aa9581">10.1088/1361-6420/aa9581</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Bertozzi, Otavio, Harold R. Chamorro, Edgar O. Gomez-Diaz, Michelle S. Chong, and Shehab Ahmed. 2024. “Application of Data-Driven Methods in Power Systems Analysis and Control.” <i>Iet Energy Systems Integration</i> 6 (3): 197–212. doi:<a href="https://doi.org/10.1049/esi2.12122">10.1049/esi2.12122</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Bhatnagar, Saakaar, Yaser Afshar, Shaowu Pan, Karthik Duraisamy, and Shailendra Kaushik. 2019. “Prediction of Aerodynamic Flow Fields Using Convolutional Neural Networks.” <i>Computational Mechanics</i> 64 (2): 525–45. doi:<a href="https://doi.org/10.1007/s00466-019-01740-0">10.1007/s00466-019-01740-0</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>Carleo, Giuseppe, and Matthias Troyer. 2017. “Solving the Quantum Many-Body Problem with Artificial Neural Networks.” <i>Science</i> 355 (6325). American Association for the Advancement of Science: 602–6. doi:<a href="https://doi.org/10.1126/science.aag2302">10.1126/science.aag2302</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>Chen, Keyan, Yile Li, Da Long, Zhitong Xu, Wei Xing, Jacob Hochhalter, and Shandian Zhe. 2025. “Pseudo-Physics-Informed Neural Operators: Enhancing Operator Learning from Limited Data.” February 4. doi:<a href="https://doi.org/10.48550/arXiv.2502.02682">10.48550/arXiv.2502.02682</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_6"></a>Cheng, Mulin, Thomas Y. Hou, Mike Yan, and Zhiwen Zhang. 2013. “A Data-Driven Stochastic Method for Elliptic PDEs with Random Coefficients.” <i>SIAM/ASA Journal on Uncertainty Quantification</i> 1 (1). Society for Industrial and Applied Mathematics: 452–93. doi:<a href="https://doi.org/10.1137/130913249">10.1137/130913249</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_7"></a>Donon, Balthazar, Benjamin Donnot, Isabelle Guyon, and Antoine Marot. 2019. “Graph Neural Solver for Power Systems.” In <i>2019 International Joint Conference on Neural Networks (IJCNN)</i>, 1–8. doi:<a href="https://doi.org/10.1109/IJCNN.2019.8851855">10.1109/IJCNN.2019.8851855</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_8"></a>Feng, Renhai, Khan Wajid, Muhammad Faheem, Jiang Wang, Fazal E. Subhan, and Muhammad Shoaib Bhutta. 2025. “Uniform Physics Informed Neural Network Framework for Microgrid and Its Application in Voltage Stability Analysis.” <i>IEEE Access</i> 13: 8110–26. doi:<a href="https://doi.org/10.1109/ACCESS.2025.3527047">10.1109/ACCESS.2025.3527047</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_9"></a>Guo, Xiaoxiao, Wei Li, and Francesco Iorio. 2016. “Convolutional Neural Networks for Steady Flow Approximation.” In <i>Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining</i>, 481–90. KDD ’16. New York, NY, USA: Association for Computing Machinery. doi:<a href="https://doi.org/10.1145/2939672.2939738">10.1145/2939672.2939738</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_10"></a>Huang, Bin, and Jianhui Wang. 2023. “Applications of Physics-Informed Neural Networks in Power Systems - A Review.” <i>IEEE Transactions on Power Systems</i> 38 (1): 572–88. doi:<a href="https://doi.org/10.1109/TPWRS.2022.3162473">10.1109/TPWRS.2022.3162473</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_11"></a>Jiang Chiyu “Max”, Soheil Esmaeilzadeh, Kamyar Azizzadenesheli, Karthik Kashinath, Mustafa Mustafa, Hamdi A. Tchelepi, Philip Marcus, Mr Prabhat, and Anima Anandkumar. 2020. “MESHFREEFLOWNET: A Physics-Constrained Deep Continuous Space-Time Super-Resolution Framework.” In <i>SC20: International Conference for High Performance Computing, Networking, Storage and Analysis</i>, 1–15. doi:<a href="https://doi.org/10.1109/SC41405.2020.00013">10.1109/SC41405.2020.00013</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_12"></a>Karniadakis, George Em, Ioannis G. Kevrekidis, Lu Lu, Paris Perdikaris, Sifan Wang, and Liu Yang. 2021. “Physics-Informed Machine Learning.” <i>Nature Reviews Physics</i> 3 (6). Nature Publishing Group: 422–40. doi:<a href="https://doi.org/10.1038/s42254-021-00314-5">10.1038/s42254-021-00314-5</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_13"></a>Khoo, Yuehaw, Jianfeng Lu, and Lexing Ying. 2018. “Solving for High-Dimensional Committor Functions Using Artificial Neural Networks.” <i>Research in the Mathematical Sciences</i> 6 (1): 1. doi:<a href="https://doi.org/10.1007/s40687-018-0160-2">10.1007/s40687-018-0160-2</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_14"></a>———. 2021. “Solving Parametric PDE Problems with Artificial Neural Networks.” <i>European Journal of Applied Mathematics</i> 32 (3): 421–35. doi:<a href="https://doi.org/10.1017/S0956792520000182">10.1017/S0956792520000182</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_15"></a>Kondor, Risi. 2018. “N-Body Networks: A Covariant Hierarchical Neural Network Architecture for Learning Atomic Potentials.” March 5. doi:<a href="https://doi.org/10.48550/arXiv.1803.01588">10.48550/arXiv.1803.01588</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_16"></a>Kondor, Risi, and Shubhendu Trivedi. 2018. “On the Generalization of Equivariance and Convolution in Neural Networks to the Action of Compact Groups.” In <i>Proceedings of the 35th International Conference on Machine Learning</i>, 2747–55. PMLR. <a href="https://proceedings.mlr.press/v80/kondor18a.html">https://proceedings.mlr.press/v80/kondor18a.html</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_17"></a>Kovachki, Nikola, Zongyi Li, Burigede Liu, Kamyar Azizzadenesheli, Kaushik Bhattacharya, Andrew Stuart, and Anima Anandkumar. 2024. “Neural Operator: Learning Maps Between Function Spaces.” May 2. doi:<a href="https://doi.org/10.5555/3648699.3648788">10.5555/3648699.3648788</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_18"></a>Kutyniok, Gitta, Philipp Petersen, Mones Raslan, and Reinhold Schneider. 2022. “A Theoretical Analysis of Deep Neural Networks and Parametric PDEs.” <i>Constructive Approximation</i> 55 (1): 73–125. doi:<a href="https://doi.org/10.1007/s00365-021-09551-4">10.1007/s00365-021-09551-4</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_19"></a>Lagaris, I.E., A. Likas, and D.I. Fotiadis. 1998. “Artificial Neural Networks for Solving Ordinary and Partial Differential Equations.” <i>IEEE Transactions on Neural Networks</i> 9 (5): 987–1000. doi:<a href="https://doi.org/10.1109/72.712178">10.1109/72.712178</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_20"></a>Lin, Henry W., Max Tegmark, and David Rolnick. 2017. “Why Does Deep and Cheap Learning Work So Well?” <i>Journal of Statistical Physics</i> 168 (6): 1223–47. doi:<a href="https://doi.org/10.1007/s10955-017-1836-5">10.1007/s10955-017-1836-5</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_21"></a>Lin, Shanny, Shaohui Liu, and Hao Zhu. 2022. “Risk-Aware Learning for Scalable Voltage Optimization in Distribution Grids.” <i>Electric Power Systems Research</i> 212 (November): 108605. doi:<a href="https://doi.org/10.1016/j.epsr.2022.108605">10.1016/j.epsr.2022.108605</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_22"></a>Long, Zichao, Yiping Lu, Xianzhong Ma, and Bin Dong. 2018. “PDE-Net: Learning PDEs from Data.” In <i>Proceedings of the 35th International Conference on Machine Learning</i>, 3208–16. PMLR. <a href="https://proceedings.mlr.press/v80/long18a.html">https://proceedings.mlr.press/v80/long18a.html</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_23"></a>Lu, Lu, Pengzhan Jin, Guofei Pang, Zhongqiang Zhang, and George Em Karniadakis. 2021. “Learning Nonlinear Operators via DeepONet Based on the Universal Approximation Theorem of Operators.” <i>Nature Machine Intelligence</i> 3 (3). Nature Publishing Group: 218–29. doi:<a href="https://doi.org/10.1038/s42256-021-00302-5">10.1038/s42256-021-00302-5</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_24"></a>Matthies, Hermann G., and Andreas Keese. 2005. “Galerkin Methods for Linear and Nonlinear Elliptic Stochastic Partial Differential Equations.” <i>Computer Methods in Applied Mechanics and Engineering</i>, Special Issue on Computational Methods in Stochastic Mechanics and Reliability Analysis, 194 (12): 1295–1331. doi:<a href="https://doi.org/10.1016/j.cma.2004.05.027">10.1016/j.cma.2004.05.027</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_25"></a>Misyris, George S., Andreas Venzke, and Spyros Chatzivasileiadis. 2020. “Physics-Informed Neural Networks for Power Systems.” In <i>2020 IEEE Power &#38; Energy Society General Meeting (PESGM)</i>, 1–5. doi:<a href="https://doi.org/10.1109/PESGM41954.2020.9282004">10.1109/PESGM41954.2020.9282004</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_26"></a>Nellikkath, Rahul, and Spyros Chatzivasileiadis. 2021. “Physics-Informed Neural Networks for Minimising Worst-Case Violations in DC Optimal Power Flow.” In <i>2021 IEEE International Conference on Communications, Control, and Computing Technologies for Smart Grids (SmartGridComm)</i>, 419–24. doi:<a href="https://doi.org/10.1109/SmartGridComm51999.2021.9632308">10.1109/SmartGridComm51999.2021.9632308</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_27"></a>———. 2022. “Physics-Informed Neural Networks for AC Optimal Power Flow.” <i>Electric Power Systems Research</i> 212 (November): 108412. doi:<a href="https://doi.org/10.1016/j.epsr.2022.108412">10.1016/j.epsr.2022.108412</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_28"></a>Pagnier, Laurent, and Michael Chertkov. 2021. “Physics-Informed Graphical Neural Network for Parameter &#38; State Estimations in Power Systems.” February 12. doi:<a href="https://doi.org/10.48550/arXiv.2102.06349">10.48550/arXiv.2102.06349</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_29"></a>Parish, Eric J., and Karthik Duraisamy. 2016. “A Paradigm for Data-Driven Predictive Modeling Using Field Inversion and Machine Learning.” <i>Journal of Computational Physics</i> 305 (January): 758–74. doi:<a href="https://doi.org/10.1016/j.jcp.2015.11.012">10.1016/j.jcp.2015.11.012</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_30"></a>Psichogios, Dimitris C., and Lyle H. Ungar. 1992. “A Hybrid Neural Network-First Principles Approach to Process Modeling.” <i>Aiche Journal</i> 38 (10): 1499–1511. doi:<a href="https://doi.org/10.1002/aic.690381003">10.1002/aic.690381003</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_31"></a>Raissi, M., P. Perdikaris, and G.E. Karniadakis. 2019. “Physics-Informed Neural Networks: A Deep Learning Framework for Solving Forward and Inverse Problems Involving Nonlinear Partial Differential Equations.” <i>Journal of Computational Physics</i> 378 (February): 686–707. doi:<a href="https://doi.org/10.1016/j.jcp.2018.10.045">10.1016/j.jcp.2018.10.045</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_32"></a>Rico-Martinez, R., J.S. Anderson, and I.G. Kevrekidis. 1994. “Continuous-Time Nonlinear Signal Processing: A Neural Network Based Approach for Gray Box Identification.” In <i>Proceedings of IEEE Workshop on Neural Networks for Signal Processing</i>, 596–605. doi:<a href="https://doi.org/10.1109/NNSP.1994.366006">10.1109/NNSP.1994.366006</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_33"></a>Rudd, Keith, and Silvia Ferrari. 2015. “A Constrained Integration (CINT) Approach to Solving Partial Differential Equations Using Artificial Neural Networks.” <i>Neurocomputing</i> 155 (May): 277–85. doi:<a href="https://doi.org/10.1016/j.neucom.2014.11.058">10.1016/j.neucom.2014.11.058</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_34"></a>Rudy, Samuel H., Steven L. Brunton, Joshua L. Proctor, and J. Nathan Kutz. 2017. “Data-Driven Discovery of Partial Differential Equations.” <i>Science Advances</i> 3 (4). American Association for the Advancement of Science: e1602614. doi:<a href="https://doi.org/10.1126/sciadv.1602614">10.1126/sciadv.1602614</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_35"></a>Singh, Manish K., Sarthak Gupta, Vassilis Kekatos, Guido Cavraro, and Andrey Bernstein. 2020. “Learning to Optimize Power Distribution Grids Using Sensitivity-Informed Deep Neural Networks.” In <i>2020 IEEE International Conference on Communications, Control, and Computing Technologies for Smart Grids (SmartGridComm)</i>, 1–6. doi:<a href="https://doi.org/10.1109/SmartGridComm47815.2020.9302942">10.1109/SmartGridComm47815.2020.9302942</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_36"></a>Singh, Manish K., Vassilis Kekatos, and Georgios B. Giannakis. 2022. “Learning to Solve the AC-OPF Using Sensitivity-Informed Deep Neural Networks.” <i>IEEE Transactions on Power Systems</i> 37 (4): 2833–46. doi:<a href="https://doi.org/10.1109/TPWRS.2021.3127189">10.1109/TPWRS.2021.3127189</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_37"></a>Stefanou, George. 2009. “The Stochastic Finite Element Method: Past, Present and Future.” <i>Computer Methods in Applied Mechanics and Engineering</i> 198 (9): 1031–51. doi:<a href="https://doi.org/10.1016/j.cma.2008.11.007">10.1016/j.cma.2008.11.007</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_38"></a>Stiasny, Jochen, Samuel Chevalier, Rahul Nellikkath, Brynjar Sævarsson, and Spyros Chatzivasileiadis. 2022. “Closing the Loop: A Framework for Trustworthy Machine Learning in Power Systems.” July 14. doi:<a href="https://doi.org/10.48550/arXiv.2203.07505">10.48550/arXiv.2203.07505</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_39"></a>Stiasny, Jochen, Samuel Chevalier, and Spyros Chatzivasileiadis. 2021. “Learning without Data: Physics-Informed Neural Networks for Fast Time-Domain Simulation.” In <i>2021 IEEE International Conference on Communications, Control, and Computing Technologies for Smart Grids (SmartGridComm)</i>, 438–43. doi:<a href="https://doi.org/10.1109/SmartGridComm51999.2021.9631995">10.1109/SmartGridComm51999.2021.9631995</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_40"></a>Stiasny, Jochen, George S. Misyris, and Spyros Chatzivasileiadis. 2021. “Physics-Informed Neural Networks for Non-linear System Identification for Power System Dynamics.” In <i>2021 IEEE Madrid PowerTech</i>, 1–6. doi:<a href="https://doi.org/10.1109/PowerTech46648.2021.9495063">10.1109/PowerTech46648.2021.9495063</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_41"></a>Stiasny, Jochen, Georgios S. Misyris, and Spyros Chatzivasileiadis. 2023. “Transient Stability Analysis with Physics-Informed Neural Networks.” March 15. doi:<a href="https://doi.org/10.48550/arXiv.2106.13638">10.48550/arXiv.2106.13638</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_42"></a>Stock, Simon, Davood Babazadeh, Christian Becker, and Spyros Chatzivasileiadis. 2024. “Bayesian Physics-informed Neural Networks for System Identification of Inverter-dominated Power Systems.” March 20. doi:<a href="https://doi.org/10.48550/arXiv.2403.13602">10.48550/arXiv.2403.13602</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_43"></a>Torlai, Giacomo, and Roger G. Melko. 2016. “Learning Thermodynamics with Boltzmann Machines.” <i>Physical Review B</i> 94 (16). American Physical Society: 165134. doi:<a href="https://doi.org/10.1103/PhysRevB.94.165134">10.1103/PhysRevB.94.165134</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_44"></a>Ummenhofer, Benjamin, Lukas Prantl, Nils Thuerey, and Vladlen Koltun. 2019. “Lagrangian Fluid Simulation with Continuous Convolutions.” <a href="https://openreview.net/forum?id=B1lDoJSYDH">https://openreview.net/forum?id=B1lDoJSYDH</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_45"></a>Vlachas, Pantelis R., Wonmin Byeon, Zhong Y. Wan, Themistoklis P. Sapsis, and Petros Koumoutsakos. 2018. “Data-Driven Forecasting of High-Dimensional Chaotic Systems with Long Short-Term Memory Networks.” <i>Proceedings of the Royal Society a: Mathematical, Physical and Engineering Sciences</i> 474 (2213). Royal Society: 20170844. doi:<a href="https://doi.org/10.1098/rspa.2017.0844">10.1098/rspa.2017.0844</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_46"></a>Zhu, Yinhao, and Nicholas Zabaras. 2018. “Bayesian Deep Convolutional Encoder–Decoder Networks for Surrogate Modeling and Uncertainty Quantification.” <i>Journal of Computational Physics</i> 366 (August): 415–47. doi:<a href="https://doi.org/10.1016/j.jcp.2018.04.018">10.1016/j.jcp.2018.04.018</a>.</div>
</div>
