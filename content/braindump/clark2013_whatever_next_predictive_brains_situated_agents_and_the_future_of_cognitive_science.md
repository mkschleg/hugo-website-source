+++
title = "clark2013whatever: Whatever next? Predictive brains, situated agents, and the future of cognitive science"
author = ["Matthew Schlegel"]
lastmod = 2022-11-09T14:06:17-07:00
slug = "clark2013whatever"
draft = false
notetype = "paper"
+++

tags
: [Predictive Processing]({{< relref "predictive_processing.md" >}}), [Perception]({{< relref "perception.md" >}})

source
: <https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-science/33542C736E17E3D1D44E8D03BE5F4CD9>

Clark argues for the notion that brains are prediction machines. They are bundles of cells that support perception and action by constantly attempting to match incoming sensory inputs with top-down expectations or predictions. This is inspired by the work of (<a href="#citeproc_bib_item_5">Rao and Ballard 1999</a>) and others in developing the brain as a inference machine.


## Introduction: Prediction Machines {#introduction-prediction-machines}


### From Helmholtz to action-oriented predictive processing {#from-helmholtz-to-action-oriented-predictive-processing}

"The whole function of the brain is summed up in: error correction." - W. Ross Ashby

One possible theory of the how the brain works is related to this notion, in that the brain's key trick is to implement dumb processes that correct error in the multi-layered prediction of input. In mammalian brains, such errors look to be corrected within a cascade of cortical processing events in which higher-level systems attempt to prediction the inputs to lower-level ones on the basis of their own emerging models. Errors in predicting lower level inputs cause the higher-level models to adapt so as to reduce the discrepancy.

These hierarchical models follow from [Hermann von Helmholtz]({{< relref "hermann_von_helmholtz.md" >}}) (1860) in depicting perception as a process of probabilistic, knowledge-driven inference.

This insight informed many who followed in the "analysis-by-synthesis" paradigm. This paradigm suggest the brain does not build its current model of distal causes simply by accumulating from the bottom-up, but instead tries to predict the current suite of cues from its best models of the possible causes.

Work in connectionist networks was also inspired by [Hermann von Helmholtz]({{< relref "hermann_von_helmholtz.md" >}}) (specifically Hinton, McClelland, Rumelhart...). Specifically, the Helmholtz machin sought to learn new representations in a multilevel system without requiring the provision of copious pre-classified samples (i.e. a generative model).

The strategy of using top-down connections to try to generate, using high-level knowledge, a kind of "virtual version" of the sensory data via a deep multilevel cascade lies at the heart of [Hierarchical Predictive Coding]({{< relref "hierarchical_predictive_coding.md" >}}) (<a href="#citeproc_bib_item_5">Rao and Ballard 1999</a>). These approaches combine the use of top-down probabilistic generative models with a specific vision of how the downward influence might operate. Specifically, [Hierarchical Predictive Coding]({{< relref "hierarchical_predictive_coding.md" >}}) depicts the top-down flow as attempting to predict and fully "explain awa" the driving sensory signal, leaving only residual "prediction errors".


### Escaping the black box {#escaping-the-black-box}

The task of the brain, or really any learning/intelligent system, when viewed from a certain distance can seem impossible. It must discover information about the likely causes of impinging signals without any form of direct access to their source.

_Notice how different this conception is to ones in which the problem is posed as one of estabilishing a mapping relation between environmental and inner states. The task is not to find such a mapping but to infer the nature of the signal source (the world) from just the varying input signal itself._

Such a scheme as predictive coding suggests the backward connections from V2 to V1 would carry a prediction of expected activity in V1, while forward connections for V1 to V2 would carry forward the error signal indicating residual activity.

<a href="#citeproc_bib_item_5">Rao and Ballard</a> implemented a simple bidirectional hierarchical network of such predictive estimators. The model displayed hierarchical structure (i.e. the lower level indicating edges, while the higher level combining such edges), "extra-classical receptive field" effects (suggesting such non-classical surround effects) which may be a rather direct consequence of the use of hierarchical predictive coding.


### Dynamic predictive coding by the retina {#dynamic-predictive-coding-by-the-retina}

<a href="#citeproc_bib_item_3">Hosoya, Baccus, and Meister</a>'s (<a href="#citeproc_bib_item_3">2005</a>) account of dynamic predictive coding moves context center states. The neural circuits predict, on the basis of local image characteristics, the likely image characteristics of nearby spots in space and time. The encoded value is not the raw image data, but the residual or departures from the predictable structure. The saves bandwidth and highlights the "news-worthy" aspects of the incoming signal. Hosoya predicted that, in the interestes of efficient, adaptively potent, encoding, the behavior of the [retinal ganglion cell]({{< relref "visual_system.md" >}}) should vary as a result of adaptation to the current scene or context, exhibiting what they term "dynamic predictive coding".


### [Binocular rivalry]({{< relref "binocular_rivalry.md" >}}) {#binocular-rivalry--binocular-rivalry-dot-md}

This occurs when each eye is presented a separate image. The viewers report perceiving various parts of the two images pop in and out until a single image becomes dominant. A cycle of the two images is continuous. The predictive coding hypothesis explains this more effectively than other hypothesis, for reasons not discussed in these notes.


### Action-oriented predictive processing {#action-oriented-predictive-processing}

This work by (<a href="#citeproc_bib_item_1">Brown, Friston, and Bestmann 2011</a>) generalizes the basic [Hierarchical Predictive Coding]({{< relref "hierarchical_predictive_coding.md" >}}) model to include action. The fundamental attraction of these accounts lies in their ability to offer a deeply unified account of perception, cognition, and action.


### The free energy formulation {#the-free-energy-formulation}

Free-energy formulations originate in statistical physics and were introduced into the machine-learning literature in treatments that include (<a href="#citeproc_bib_item_4">Neal and Hinton 1998</a>) (among others). These formulations can arguably be used (<a href="#citeproc_bib_item_2">Friston 2010</a>) to display the prediction error minimization strategy as itself a consequence of a more fundamental mandate to minimize an information-theoretic isomorph of thermodynamic free-energy in a system's exchanges with the environment.

[Isomorphism]({{< relref "isomorphism.md" >}}): any mathematical mapping (morphism) which can be inversed through an inverse morphism.

Thermodynamic free energy is a measure of the energy available to do useful work. Transposed to the cognitive/information domain, it emerges as the difference between the way the world is represented as being, and the way it actually is. The better the fit, the lower the information-theoretic free energy (i.e. more of the system's resources are being put to "effective work" in representing the world). We can say prediction error reports the information-theoretic free energy.

[Free-Energy Principle]({{< relref "free_energy_principle.md" >}}): all the quantities that can change; i.e. that are part of the system, will change to minimize free-energy.


## Representation, inference, and the continuity of perception, cognition, and action {#representation-inference-and-the-continuity-of-perception-cognition-and-action}

The hierarchical predictive processing account, along with the more recent generalizations to action represents a departure from many of the previous ways of thinking:

-   Offers a distinctive account of neural representation, neural computation, and the representation relation itself.
-   Depicts perceptions, cognition, and action as profoundly unified and continuous.
-   Offers a neurally plausible and computationally tractable gloss on the claim that the brain performs some form of Bayesian inference.


### Explaining away {#explaining-away}

To represent the world in perception according to these models depends critcally upon cancelling out sensory prediction error! I.e. we must "explain away" the driving (incoming) sensory signal by matching it with a cascade of predictions pitched at a variety of spatial and temporal scales. These predictions reflect what the system "knows" about the world.

<aside>

To know is a really dangerous statement in this context. I think the conjecture that knowing something means we can predict that something is quite nice. But is the prediction itself knowledge, or is having knowledge simply being able to predict. In terms of ML and RL, are the weights knowledge, or the prediction made through the function knowledge? So when we say "predictive knowledge" we must mean the actual prediction itself.

</aside>

Perception here becomes "theory-laden" in at least one (rather specific) sense: "What we perceive depends heavily upon the set of priors (including any relevant hyper-priors) that the brain brings to bear in its best attempt to predict the current sensory signal." Perception demands the success of sume mutually supportive stack of states of a generative model at minimizing prediction error by hypothesizing an interacting set of distal causes that predict, accommodate, and "explain away" the driving sensory signal.

The appeal to "explaining away" reflects the key property of hierarchical predictive processing models: The brain is in the business of active, ongoing, input prediction and does not (even in the early sensory case) merely react to external stimuli.

While we have been focused on the predictive part of the coding, we must not forget that the actual full encoding is a kind of _duplex_ architecture: one that at each level combines traditional representation of inputs with representations of error. According to the duplex proposal what gets "explained away" is the error signal, which is depicted as computed by dedicated "error units." The duplex architecture is a delicate balance between a cascade of feature-detection and the forward flow of sensory information now entirely replaced by a forward flow of prediction error.


### Encoding, inference, and the "Bayesian Brain" {#encoding-inference-and-the-bayesian-brain}

This goes into details about the brain encoding predictions as probability distributions instead of singular values. So when a prediction is made about the distance of an object, instead of a single value we have a number of predictions which correspond to the probability of that object being a certain distance.


### The delicate dance between top-down and bottom-up {#the-delicate-dance-between-top-down-and-bottom-up}


### Summary so far {#summary-so-far}


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Brown, Harriet, Karl J. Friston, and Sven Bestmann. 2011. “Active Inference, Attention, and Motor Preparation.” <i>Frontiers in Psychology</i>. Frontiers.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Friston, Karl. 2010. “The Free-Energy Principle: A Unified Brain Theory?” <i>Nature Reviews Neuroscience</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Hosoya, Toshihiko, Stephen A. Baccus, and Markus Meister. 2005. “Dynamic Predictive Coding by the Retina.” <i>Nature</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>Neal, Radford M., and Geoffrey E. Hinton. 1998. “A View of the Em Algorithm That Justifies Incremental, Sparse, and Other Variants.” In <i>Learning in Graphical Models</i>, edited by Michael I. Jordan. NATO ASI Series. Dordrecht: Springer Netherlands.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>Rao, Rajesh P. N., and Dana H. Ballard. 1999. “Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects.” <i>Nature Neuroscience</i>.</div>
</div>
