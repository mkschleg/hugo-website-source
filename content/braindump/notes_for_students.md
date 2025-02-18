+++
title = "Notes for Students"
author = ["Matthew Schlegel"]
lastmod = 2023-09-06T10:04:31-06:00
slug = "notes_for_students"
draft = false
notetype = "misc-topic"
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

Hmmmmm. Lots of resources. I’m going to just give a few that I think are really good. And give some advice. To be able to read neuroscience and computational neuroscience you really need to get the context of where they are coming from (i.e. what frameworks are they working in). There are also several fields (really ways of doing research) to pay attention to:
Psychology (looking more at explaining behaviour through stories/explainable mechanisms to eventually be used for therapy),
Neuroscience (looking at the actual wetware of the brain, measuring it, and fitting the data into a model of the brain),
computational neuroscience (trying to “simulate” the brain, but really it is more of a tool to try and explain the algorithm of specific parts of the wetware. Goal is always to match the data collected by neuroscientists),
and cognitive or behavioral science (all the above can really fit into this in some way, but I think the distinction here is they are more concerned with coming up with frameworks or a model for cognition or behavior by studying brains).
The first three fields can also be split into cognitive and behavioral, but that distinction only really gives you insight into what they might be trying to measure. It also distinguishes their framework in some respects, but the boundaries have gotten pretty thin. In the end, all of what is studied is (and must be) related to some type of behaviour (even if it isn’t directly, it needs to be eventually).
Some intro resources:
Chapter 1 of Cognitive Psychology by Sternberg (and selected chapters from there)
Chapter 2&amp;3 of Cognitive Psychology by Sternberg have a more neuroscience focus.
Computational Neuroscience coursera course. Ran by Rajesh Rao and Adrienne Fairhall from University of Washington. I think it is a great intro not only to computational neuro, but also to some basic concepts of neuro.
The Encyclopedia of Cognitive Science (on Wiley, access through library). This is a collection of works that details some of the basic models and concepts of cogsci. It is a tougher read than the above though.
I think these are really good intros. But things get much more complicated.  When reading a paper I always try and tease out: the framework, the data (i.e. how is it collected, how much, etc), and the analysis. This makes life a lot easier when trying to tease out what they are doing and how it effects my underlying models of things. Also, one paper is almost never enough to convince me something is a real effect. It often takes quite a lot of evidence for me to think something is real.
 I also really like when there are collections of papers, or larger survey papers. Something like Bubic’s Prediction, Cognition and the Brain is really useful for getting a large sample of what exists for a particular model/framework. Also, I like to take a foundational paper that people cite (say Mountcastle’s The Columnar Organization of the Neocortex and look through the citations forward and backward. Getting into the field is tough, so I think it is wise to focus on a small portion and try and understand a few papers that interest you, then branch out. It is also hard, because all the fields that exist under brain sci interact with eachother, so papers can require a lot of context which takes awhile to build.
The final piece of advice, is really just don’t get sold on a nice story. The brain is complicated, and there are a lot of really nice frameworks that it is easy to become sold on. For example, I was really into predictive perception (and still am). But the data is much more complicated than a lot of the survey papers let on, and having enough evidence to show such an architecture exists is quite difficult. But this doesn’t mean I don’t find the model interesting for my own research, even if it doesn’t pan out biologically. (edited)

Matthew Schlegel
  2 years ago
One interesting example of this is in the what happened at the start of what is known as the “cognitive revolution”. Skinner wrote “Verbal Behavior” which was rebutted by several and most notably Chomsky.
At the time, there was a lot of push back on Skinner’s (and behaviorism’s control of psych/brain sciences in general), and Chomsky’s rebuttal became a rallying cry. But in both cases they are convenient stories which rely on their frameworks (late stage “radical” behaviorism and early stage cognitivism).
Now both Skinner and Chomsky were trying to play to their framework to convince researchers to use it for their research. And chomsky was overly obtuse to sell a specific point about the limitations of behaviorism.  And a lot of his criticisms were either not true, or (in my opinion) really bad takes on learning/cognition in humans. But I think the approach skinner was taking (and the gumming up the free flow of science by the behaviorists in general) was also flawed.
I think in the end everything is always less restrictive than the extremes, especially in brain science. So going all in on a specific framework can blind you to interesting ideas outside of that framework. Especially as outsiders, there is no need to be so sold on a particular way of viewing the data, even if it has a nice story. Here is a review of the Verbal Behaviorism period which led to the cognitive revolution: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2223153/> (edited)
