+++
title = "sutton2020john: John McCarthy's definition of intelligence"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:38-06:00
slug = "sutton2020john"
draft = false
notetype = "paper"
+++

\\( \newcommand{\states}{\mathcal{S}}
\newcommand{\actions}{\mathcal{A}}
\newcommand{\observations}{\mathcal{O}}
\newcommand{\rewards}{\mathcal{R}}
\newcommand{\traces}{\mathbf{e}}
\newcommand{\transition}{P}
\newcommand{\reals}{\mathbb{R}}
\newcommand{\naturals}{\mathbb{N}}
\newcommand{\expected}{\mathbb{E}}
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
\newcommand{\gvec}{\mathbf{g}}
\newcommand{\hvec}{\mathbf{h}}
\newcommand{\lvec}{\mathbf{l}}
\newcommand{\mvec}{\mathbf{m}}
\newcommand{\nvec}{\mathbf{n}}
\newcommand{\pvec}{\mathbf{p}}
\newcommand{\qvec}{\mathbf{q}}
\newcommand{\rvec}{\mathbf{r}}
\newcommand{\svec}{\mathbf{s}}
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
\newcommand{\Imat}{\mathbf{I}}
\newcommand{\Pmat}{\mathbf{P}}
\newcommand{\Umat}{\mathbf{U}}
\newcommand{\Vmat}{\mathbf{V}}
\newcommand{\Wmat}{\mathbf{W}}
\newcommand{\Xmat}{\mathbf{X}}
\newcommand{\Qmat}{\mathbf{Q}}
\newcommand{\thetavec}{\boldsymbol{\theta}}
\newcommand{\phivec}{\boldsymbol{\phi}}
\newcommand{\muvec}{\boldsymbol{\mu}}
\newcommand{\sigmavec}{\boldsymbol{\sigma}}
\newcommand{\jacobian}{\mathbf{J}}
\\)

tags
: [Artificial Intelligence]({{<relref "artificial_intelligence.md#" >}}), [Intelligence]({{<relref "intelligence.md#" >}})

source
: <http://www.incompleteideas.net/papers/Sutton-JAGI-2020.pdf>

authors
: Sutton, R. S.

year
: 2020

In this paper, the authors take John McCarthy's statement on artificial intelligence being

> "Intelligence is the computational part of the ability to achieve goals in the world."

and considers the consequences of the various parts. While the statement at large seems quite explainable, the understanding of what it means for an agent to "achieve goals" is unclear. In the paper, the author discusses that defining this is a stance of the observer onto a system. For instance, to someone who uses a thermostat they see the thermostat trying to maintain the temperature, which can be thought of as the goal from the point of this observer. But a handy man who needs to fix the thermostat will consider the system from a mechanistic view, which removes the mirage of intelligence or "having goals". In light of this idea that have a goal is just a stance of the observer we can add to the definition of intelligence:

> Intelligence is the computational part of the ability to achieve goals. A goal achieving system is one that is more usefully understood in terms of outcomes than in terms of mechanisms.

<aside>
  <aside></aside>

We can only understand agents we create in terms of mechanisms. So likely we will never really consider things we engineer to be intelligent. The mystery of what we perceive as intelligence is hidden behind the ability to describe it mechanistically. Once we do, does this mean we will no longer perceive intelligence as something separate from the biology of it? This actually would be useful in the long run, and remove the varnish of the word.

</aside>


## References {#references}


</Users/Matt/GD/bib/full_library.bib>
