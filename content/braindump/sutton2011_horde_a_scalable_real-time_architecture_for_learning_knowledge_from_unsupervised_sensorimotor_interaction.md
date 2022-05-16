+++
title = "sutton2011: Horde: A Scalable Real-time Architecture for Learning Knowledge from Unsupervised Sensorimotor Interaction"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:38-06:00
slug = "sutton2011"
draft = false
notetype = "paper"
+++

tags
: [Reinforcement Learning]({{<relref "reinforcement_learning.md#" >}}), [General Value Functions]({{<relref "general_value_functions.md#" >}})

source
: [paper](http://www.ifaamas.org/Proceedings/aamas2011/papers/A6%5FR70.pdf)

authors
: Sutton, R. S., Modayil, J., Delp, M., Degris, T., Pilarski, P. M., White, A., & Precup, D.

year
: 2011

This paper focuses on building world knowledge through value function predictions on the sensorimotor stream. This new class of sensorimotor predictions are coined General Value Functions, and posited to be able to encapsulate the model of the world through gradient temporal-difference training. They also posit that this architecture, deemed the Horde, is a step towards a real-time architecture for efficient learning.


## The Problem of Expressive and Learnable Knowledge {#the-problem-of-expressive-and-learnable-knowledge}

They make the claim that knowledge representation is hard, which is a reasonable claim and one I agree with. They posit that prior approaches are either limited from their abstraction away from the data stream (first-order predicate logic), or lack of generality (differential equations and state-transition matrices). They argue that a class of value predictions will produce a more general form of knowledge (predictive knowledge), which will better encapsulate the agent's knowledge of the world. Several other approaches and theories of the representation of knowledge learned through the sensorimotor stream have been proposed including: <sup id="6559eff0f05dfd4be9c8d6726d937b72"><a href="#drescher1991" title="Drescher, Made-{{Up Minds}} : {{A Constructivist Approach}} to {{Artificial Intelligence}}, {The MIT Press} (1991).">drescher1991</a></sup>, <sup id="5b398cfbcb2305295f2d74a4f0698fd0"><a href="#cunningham2013intelligence" title="Cunningham, Intelligence: {{Its}} Organization and Development, {Elsevier} (2013).">cunningham2013intelligence</a></sup>, <sup id="de504f8eba81fc76f28f894ea7b665dd"><a href="#becker1973model" title="Becker, A {{Model}} for the {{Encoding}} of {{Experiential Information}}. {{Computer Models}} of {{Thought}} and {{Language}}. {{RC Schank}} and {{KM Colby}}, v(), (1973).">becker1973model</a></sup>.

-   <sup id="6559eff0f05dfd4be9c8d6726d937b72"><a href="#drescher1991" title="Drescher, Made-{{Up Minds}} : {{A Constructivist Approach}} to {{Artificial Intelligence}}, {The MIT Press} (1991).">drescher1991</a></sup> explored a simulated robot baby learning conditional probability tables for boolean events
-   <sup id="87e79d486dd48b577ba1a9f855458a30"><a href="#ring1997" title="Ring, {{CHILD}}: {{A First Step Towards Continual Learning}}, {Machine Learning}, v(), (1997).">ring1997</a></sup> explored continual learning of a hierarchical representation of sequences

These systems among others learned knowledge but remained far from learning from sensorimotor data. They claim that a knowledge representation built on predictions made from value functions will provide a broader knowledge representation.


## Value functions as semantics {#value-functions-as-semantics}

They argue that value functions have a clear semantic meaning (or "truth") grounded in the sensorimotor data. This "truth" or "accuracy" comes from the underlying approximation of a value function as an expected discounted sum of cumulants into the future. While this is convenient, and the meaning of accuracy here is valid this does not entirely lead to value functions having semantic meaning. It is also a bit unclear if it is useful to describe knowledge in terms of semantic meaning.

The main hypothesis of the work is to define the value-function approach as a theory spanning all of world-knowledge.

They then go to define value functions and the reinforcement learning setting. These terms are standard. They return to the discounted return given a specification. They ground the answer of the specification in data based on the expected squared error of the estimate and true return. Because all specifications have "answers" in this way, a knowledge representation built on value function predictions will be grounded by the true answers ("grounding semantics") of knowledge about the reward function.


## From Values to Knowledge (General Value Functions) {#from-values-to-knowledge--general-value-functions}

By extending the prior notion of rewards, termination, and policy to a more general cumulant, pseudo-termination, and pseudo-policy function, the prior grounding semantics of reward knowledge extends to grounding semantics of sensorimotor knowledge. These extensions also lead to a more general class of predictions made through temporal-difference.

There are specifically two types of GVFs which must be seperated in learning:

-   Predictive knowledge: gvfs with fixed policies which predict the outcome of acting on a policy.
-   Control (procedural) knowledge: gvfs which look to maximize some signal.


## The Horde Architecture {#the-horde-architecture}

The horde architecture is simply a large collection of GVFs (both predictive and control), which is said to encapsulate world knowledge. In this architecture they use GQ(&lambda;) to train the "answer" function from the semantics of the "predictive question". These are then trained in a massively parallel scheme with online updates.


## Results {#results}

They perform experiments on the critterbot to show the "success" of the architecture.


### Prediction {#prediction}

They provide experiential evidence of the horde making accurate predictions about the time-to-obstacle and time-to-stop.

-   Time-to-obstacle:
    Question functions: \\(\pi(s, forward) = 1, r(s) = 1, z(s)=0, \forall s\in\mathcal{S}, \gamma(s) = 1\\) when ir sensor over a set threshold.
-   Time to stop
    Semantically the same, except the policy is now the stopping policy, and the reward is 0 and the quesiton terminates when the agent stops (vel is below some threshold.).


### Off-policy learning of multiple spinning control policies {#off-policy-learning-of-multiple-spinning-control-policies}

They show they can learn policies off-policy.


### Light seeking {#light-seeking}

They show they can learn a policy to maximize a signal.


## Thoughts {#thoughts}

-   The use of "accurate world knowledge" is devoid of meaning in this context. What is world knowledge, how is it related to a more general sense of knowledge, in what measure is this world knowledge accurate? By starting the paper with broad overly general terms, and without defining these terms, it is hard to find the true meaning and ideals of the work.

-   The claim that a knowledge system built on value function predictions will provide a more general representation of knowledge is not well supported, and claimed as an assumption without experiential evidence. While this claim may be true, the lack of support is troubling.

-   defining value functions with semantic meaning is unfortunate and leads to people thinking about them in terms of symbols (symbols whose true "value" is learned but symbols non-the-less).

-   They also tacitly imply that value functions are the only form of knowledge looked at which has semantic meaning in the data (which I'm unclear if this is accurate).


# Bibliography
<a id="drescher1991"></a>[drescher1991] Drescher, Made-Up Minds : A Constructivist Approach to Artificial Intelligence, The MIT Press (1991). [↩](#6559eff0f05dfd4be9c8d6726d937b72)

<a id="cunningham2013intelligence"></a>[cunningham2013intelligence] Cunningham, Intelligence: Its Organization and Development, Elsevier (2013). [↩](#5b398cfbcb2305295f2d74a4f0698fd0)

<a id="becker1973model"></a>[becker1973model] Becker, A Model for the Encoding of Experiential Information. Computer Models of Thought and Language. RC Schank and KM Colby, <i></i>,  (1973). [↩](#de504f8eba81fc76f28f894ea7b665dd)

<a id="ring1997"></a>[ring1997] Ring, CHILD: A First Step Towards Continual Learning, <i>Machine Learning</i>,  (1997). [↩](#87e79d486dd48b577ba1a9f855458a30)
