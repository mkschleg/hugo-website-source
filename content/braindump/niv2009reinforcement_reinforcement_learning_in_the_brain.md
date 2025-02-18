+++
title = "niv2009reinforcement: Reinforcement learning in the brain"
author = ["Matthew Schlegel"]
lastmod = 2023-01-31T13:54:29-07:00
slug = "niv2009reinforcement"
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
: [Brain]({{< relref "brain.md" >}}), [Reinforcement Learning in the Brain]({{< relref "reinforcement_learning_in_the_brain.md" >}}), [Reinforcement Learning]({{< relref "reinforcement_learning.md" >}})

source
: [link](https://www.sciencedirect.com/science/article/pii/S0022249608001181?casa_token=lgOWwyFDA5YAAAAA:2a5tx84lb8-GRkVh_puGph5Wx6yccKjuq7_wf9HOw_2RguIRXOe2RG13vtsrCNRs4EP-8JrvCGxL)

authors
: Niv, Y.

year
: 2009


## Quotes {#quotes}

> Most notably, much evidence suggest that the neuromodulator dopamine provides basal ganglia target structures with phasic signals that convey a reward prediction error that can influence learning and action selection, particularly in stimulus-driven habitual instrumental behavior.

<!--quoteend-->

> That is, RL models (1) generate predictions regarding the molar and molecular forms of optimal behavior. (2) suggests a means by which optimal prediction and action selection can be achieved, and (3) expose explicitly the computations that must be realized in the service of these.

<!--quoteend-->

> Specifically, extracellular recordings in behaving animals and functional imaging of human decision-making have revealed in the brain the existence of a key RL signal, the temporal difference reward prediction error. In this review we will focus on these links between the theory of reinforcement learning and its implementation in animal and human neural processing.

<!--quoteend-->

> Rescorla and Wagner postulated that the associative strength of each of the conditional stimuli \\(V(CS\_i)\\) will change according to
> \\[
> V\_{new}(CS\_i) = V\_{old}(CS\_i) + \eta \left[ \lambda\_{US} - \sum\_i V\_{old}(CS\_i) \right].
> \\]
> In this _error correcting_ learning rule, learning is driven by the discrepancy between what was predicted (\\(\sum\_i V(CS\_i)\\) where \\(i\\) indexes all the CSs present in the trial) and what actually happened (\\(\lambda\_{US}\\) whose magnitude is related to the worth of the unconditional stimulus, and which quantifies the maximal associative strength that the unconditional stimulus can support.)

<!--quoteend-->

> At the basis of the Rescorla-Wagner model are two important (and innovative) assumptions or hypotheses: (1) learning happens only when events are not predicted, and (2) predictions due to different stimuli are summed to form the total prediction in a trial.

Issues with the Rescorla-Wagner model:

1.  By treating the conditional and unconditional stimuli as qualitatively different, it does not extend to the important phenomenon of second order conditioning. If stimulus B predicts an affective outcome and stimulus A predicts stimulus B, then stimulus A also gains reward predictive value in **second order conditioning**.
2.  The basic unit of learning is a conditioning _trial_ as a discrete temporal object. Not only does this impose an experimenter-oriented parsing of otherwise continuous events, but it also fails to account for the sensitivity of conditioning to the different temporal relations between the conditional and the unconditional stimuli _within_ a trial.

(<a href="#citeproc_bib_item_7">Werbos 1977</a>) in his "heuristic dynamic programming methods", and later (<a href="#citeproc_bib_item_1">Barto, Sutton, and Watkins 1989</a>) suggested that in a "model-free" case in which we can not assume knowledge of the dynamics of the environment, the environment itself can supply this information stochastically and incrementally.

> Contrary to the "dopamine equals reward" hypothesis, the disappearance of the dopaminergic response to reward delivery did not accompany extinction, but rather it followed acquisition of the conditioning relationship---as the cells ceased to respond to reward the monkeys began showing conditioned responses of anticipatory licking and arm movements to the reward-predictive stimulus.

<!--quoteend-->

> The close correspondence between the phasic dopaminergic firing patterns and the characteristics of a temporal difference prediction error led Montague et al. (1996) to sugges the _reward prediction error hypothesis_ of dopamine. Whithin this theoretical framework, it was immediately clear why dopamine is necessary for reward mediated learning in the basal ganglia.

While the reward prediction error hypothesis is precise, there are many open questions and challenges.

1.  [Dopaminergic Neurons]({{< relref "dopaminergic_neurons.md" >}}) do not seem to be involved in the signaling or predictions errors for aversive outcomes (<a href="#citeproc_bib_item_3">Mirenowicz and Schultz 1996</a>), (<a href="#citeproc_bib_item_5">Tobler, Dickinson, and Schultz 2003</a>), (<a href="#citeproc_bib_item_6">Ungless, Magill, and Bolam 2004</a>).
    -   [Dopaminergic Neurons]({{< relref "dopaminergic_neurons.md" >}}) do signal negative prediction errors due to the absence of appetitive outcomes.
2.  [Dopaminergic Neurons]({{< relref "dopaminergic_neurons.md" >}}) fire to stimuli not clearly related to reward prediction, specifically in the presence of novel stimuli (<a href="#citeproc_bib_item_4">Schultz 1998</a>), although they are not (yet) predictive of any outcome, aversive or appetitive.
    -   (<a href="#citeproc_bib_item_2">Kakade and Dayan 2002</a>) addressed this possibility directly, and suggests that the novelty responses can function as 'novelty bonuses'---quantities that are added to other available reward (\\(r^{new}\_t = r\_t + \text{novelty}(S\_t))\\) and enhance exploration of novel stimuli.
    -   This has been confirmed by (<a href="#citeproc_bib_item_8">Wittmann et al. 2008</a>) using fMRI readings.
3.  Another challenge is how hierarchical structure plays a role in learning behaviors. A quintessential example of this is the everyday task of making coffee, which comprises several high-level 'modules' such as 'grind beans', 'pour water', 'add sugar', each of which, in turn, comprises many lower-level motor actions.


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Barto, A. G., R. S. Sutton, and C. J. C. H. Watkins. 1989. “Sequential Decision Problems and Neural Networks.” In <i>Advances in Neural Information Processing Systems</i>. Morgan-Kaufmann.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Kakade, Sham, and Peter Dayan. 2002. “Dopamine: Generalization and Bonuses.” <i>Neural Networks</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Mirenowicz, Jacques, and Wolfram Schultz. 1996. “Preferential Activation of Midbrain Dopamine Neurons by Appetitive Rather than Aversive Stimuli.” <i>Nature</i>. Nature Publishing Group.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>Schultz, Wolfram. 1998. “Predictive Reward Signal of Dopamine Neurons.” <i>Journal of Neurophysiology</i>. American Physiological Society.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>Tobler, Philippe N., Anthony Dickinson, and Wolfram Schultz. 2003. <a href="https://www.ncbi.nlm.nih.gov/pubmed/14614099">“Coding of Predicted Reward Omission by Dopamine Neurons in a Conditioned Inhibition Paradigm.</a>” <i>Journal of Neuroscience</i>. Society for Neuroscience.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_6"></a>Ungless, Mark A., Peter J. Magill, and J. Paul Bolam. 2004. “Uniform Inhibition of Dopamine Neurons in the Ventral Tegmental Area by Aversive Stimuli.” <i>Science</i>. American Association for the Advancement of Science.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_7"></a>Werbos, P. 1977. “Advanced Forecasting Methods for Global Crisis Warning and Models of Intelligence.” <i>General System Yearbook</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_8"></a>Wittmann, Bianca C., Nathaniel D. Daw, Ben Seymour, and Raymond J. Dolan. 2008. “Striatal Activity Underlies Novelty-Based Choice in Humans.” <i>Neuron</i>.</div>
</div>
