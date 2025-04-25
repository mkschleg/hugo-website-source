+++
title = "Power Systems Control"
author = ["Matthew Schlegel"]
lastmod = 2025-04-25T10:48:50-06:00
slug = "power_systems_control"
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


## Projects {#projects}


## Questions {#questions}


## Notes/Literature {#notes-literature}


### Common terms {#common-terms}

<!--list-separator-->

-  Distributed Generation Units

<!--list-separator-->

-  Energy Storage Systems

<!--list-separator-->

-  Point of Common Coupling

<!--list-separator-->

-  Voltage Source Converters

<!--list-separator-->

-  Swing Equation


### Microgrid Control {#microgrid-control}

A microgrid can be though of a cluster of loads, [Distributed Generation Units](#distributed-generation-units) and [Energy Storage Systems](#energy-storage-systems) operated in coordination to reliably supply electricty, connected to the host power system at the distribution level at a single point of connection, i.e. the [Point of Common Coupling](#point-of-common-coupling).

<!--list-separator-->

- <span class="org-todo todo TODO">TODO</span>  (<a href="#citeproc_bib_item_2">Olivares et al. 2014</a>)

<!--list-separator-->

-  Some links

    -   An example model of a small scale microgrid: [link](https://www.mathworks.com/help/sps/ug/simplified-model-of-a-small-scale-micro-grid.html)


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_3">Stiasny et al. 2022</a>) {#b7e31a}


### <span class="org-todo todo TODO">TODO</span> (<a href="#citeproc_bib_item_1">Dommel 1969</a>) {#d26bce}


## Examples/Benchmarks {#examples-benchmarks}


### The North Sea Wind Power Hub {#the-north-sea-wind-power-hub}

Depicted below, this model represents a realistic example of an emerging converter-dominated system that must integrate securely into the legacy bulk power grid. The objective is to optimally tune the control parameters and determine the power dispatch of the NSWPH system under small-signal stability and N-1 security constraints.

The below figure depicts:

-   5 wind farms,
-   a synchronous condenser,
-   and two HVDC Voltage Source Converters

When planning dispatch of the system, operators are assumed to have control over the active and reactive power set points of the turbines.  In the future, operators may also depend on the wind hubs to provide both primary frequency and primary voltage control support services. We assume operators have the capacity to adjust the droop parameters which determine the system's participation in both primary frequency and primary voltage control.

{{< figure src="/ox-hugo/2025-04-15_15-53-52_Screenshot 2025-04-15 at 3.53.47 PM.png" >}}


### Single Machine Infinite Bus system {#single-machine-infinite-bus-system}

This is an extremely simple power bus with a single generator and infinite external grid which has a constant draw of power without a shift in voltage or angle (very idealized system).

{{< figure src="/ox-hugo/2025-04-25_10-39-40_Screenshot 2025-04-25 at 10.39.36 AM.png" >}}


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Dommel, Hermann W. 1969. “Digital Computer Solution of Electromagnetic Transients in Single-and Multiphase Networks.” <i>IEEE Transactions on Power Apparatus and Systems</i> PAS-88 (4): 388–99. doi:<a href="https://doi.org/10.1109/TPAS.1969.292459">10.1109/TPAS.1969.292459</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Olivares, Daniel E., Ali Mehrizi-Sani, Amir H. Etemadi, Claudio A. Cañizares, Reza Iravani, Mehrdad Kazerani, Amir H. Hajimiragha, et al. 2014. “Trends in Microgrid Control.” <i>IEEE Transactions on Smart Grid</i> 5 (4): 1905–19. doi:<a href="https://doi.org/10.1109/TSG.2013.2295514">10.1109/TSG.2013.2295514</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Stiasny, Jochen, Samuel Chevalier, Rahul Nellikkath, Brynjar Sævarsson, and Spyros Chatzivasileiadis. 2022. “Closing the Loop: A Framework for Trustworthy Machine Learning in Power Systems.” July 14. doi:<a href="https://doi.org/10.48550/arXiv.2203.07505">10.48550/arXiv.2203.07505</a>.</div>
</div>
