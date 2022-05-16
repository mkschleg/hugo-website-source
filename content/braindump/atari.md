+++
title = "Atari"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:09-06:00
slug = "atari"
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

The set of atari games used heavily in [Deep Reinforcement Learning]({{<relref "deep_reinforcement_learning.md#" >}}) research. See more details in <sup id="b73dabcd50cb59db9f72d72aceedb4e3"><a href="#bellemare2013" title="Bellemare, Naddaf, Veness \&amp; Bowling, The {{Arcade Learning Environment}}: {{An Evaluation Platform}} for {{General Agents}}, {Journal of Artificial Intelligence Research}, v(), (2013).">bellemare2013</a></sup>. The experimental design in <sup id="b418008d392eb4ce22034bd3e0ff50d9"><a href="#mnih2015" title="Mnih, Kavukcuoglu, Silver, Rusu, Veness, Bellemare, Graves, Riedmiller, Fidjeland, Ostrovski, Petersen, Beattie, Sadik, Antonoglou, King, Kumaran, Wierstra, Legg \&amp; Hassabis, Human-Level Control through Deep Reinforcement Learning, {Nature}, v(), (2015).">mnih2015</a></sup> has lead to several issues in the [DRL]({{<relref "deep_reinforcement_learning.md#" >}}) community detailed in <sup id="d78e008b348b7d7beaaf33d2759eb119"><a href="#machado2018" title="Machado, Bellemare, Talvitie, Veness, Hausknecht \&amp; Bowling, Revisiting the {{Arcade Learning Environment}}: {{Evaluation Protocols}} and {{Open Problems}} for {{General Agents}}, {Journal of Artificial Intelligence Research}, v(), (2018).">machado2018</a></sup>. The code for the arcade learning environment can be found at <https://github.com/mgbellemare/Arcade-Learning-Environment>.


## References {#references}


# Bibliography
<a id="bellemare2013"></a>[bellemare2013] Bellemare, Naddaf, Veness & Bowling, The Arcade Learning Environment: An Evaluation Platform for General Agents, <i>Journal of Artificial Intelligence Research</i>,  (2013). [↩](#b73dabcd50cb59db9f72d72aceedb4e3)

<a id="mnih2015"></a>[mnih2015] Mnih, Kavukcuoglu, Silver, Rusu, Veness, Bellemare, Graves, Riedmiller, Fidjeland, Ostrovski, Petersen, Beattie, Sadik, Antonoglou, King, Kumaran, Wierstra, Legg & Hassabis, Human-Level Control through Deep Reinforcement Learning, <i>Nature</i>,  (2015). [↩](#b418008d392eb4ce22034bd3e0ff50d9)

<a id="machado2018"></a>[machado2018] Machado, Bellemare, Talvitie, Veness, Hausknecht & Bowling, Revisiting the Arcade Learning Environment: Evaluation Protocols and Open Problems for General Agents, <i>Journal of Artificial Intelligence Research</i>,  (2018). [↩](#d78e008b348b7d7beaaf33d2759eb119)
