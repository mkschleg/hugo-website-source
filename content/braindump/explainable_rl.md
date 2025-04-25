+++
title = "Explainable RL"
author = ["Matthew Schlegel"]
lastmod = 2025-04-25T08:05:01-06:00
slug = "explainable_rl"
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

tags
: [Human-in-the-Loop Reinforcement Learning]({{< relref "human_in_the_loop_reinforcement_learning.md" >}})

Explainable RL is the study of how to assign explanations to the policies learned through RL algorithms, or how to modify RL algorithms/representations such that they are explainable.


## Message To Matt {#message-to-matt}

bThere are a ton of papers that I think are relevant. A part from the thesis you sent, I found <https://dl.acm.org/doi/full/10.1145/3616864> to a be a really great review for XRL specifically, and proposes a new taxonomy to cover XRL topics that doesn't follow the XSL taxonomy. For an overview, Table 2 and Table 3 are great. Table 2 categorizes the papers based on the metrics used to evaluate the XRL method, and table 3 goes over the types of explanations. Below is a high-level overview of the main papers highlighted by the Milani that I think might be pertinent.

There are quite a few ways you can develop explanations based on the features/observations to the agent. Some papers from the review that seem relevant (really depends on the type of explainability we might be looking for):

Converting to an interpretable format: Post hoc convert an RL policy into an interpretable form.

-   <https://proceedings.neurips.cc/paper/2018/hash/e6d8545daa42d5ced125a4bf747b3688-Abstract.html>: "VIPER" Create a decision tree policy from an RL policy using imitation learning
-   <https://proceedings.mlr.press/v80/verma18a.html>: "PERL": Similar to VIPER, but uses a domain specific programmatic language to define policies to search over.

Learning interpretable policies: Directly learn a policy where the policy space is defined by an interpretable form. These methods mostly use decision trees to learn policies. CUSTARD is one such method (<https://ojs.aaai.org/index.php/AAAI/article/view/17192>). There are lots of these, each using a different learning algorithm or enabling a different type of decision tree. You can see paragraphs 3, 4, and 5 on page 16 of the Milani review paper. A recent paper is (<https://ojs.aaai.org/index.php/AAAI/article/view/35451>) which learns a "skill tree" in a robotics domain, seems pretty interesting.

Directly Generate Explanations: These generate explanations for actions taken by the policy. This includes Saliency maps and some natural language approaches.

-   _Natural Language_: These methods tend to restrict the sets of potential queries and responses to be domain specific (to make the learning of the map from policy to explanation easier). <https://dl.acm.org/doi/abs/10.1145/2909824.3020233> is highlighted in the Milani, but I'm not following how the learning process works here.
-   _Saliency maps_ are used throughout image based explanations. These provide some nice insight into what the agent is "looking at" to make a decision. Although in supervised learning they have found that these maps may not provide the best explainability power when the agent makes are "wrong decision" (i.e. classifies a cat as a dog) when tested in human studies (I'm not remembering where I read this, but maybe in the thesis you sent). There are a lot of methods here, and the thesis has a good explanation as discussed in <https://arxiv.org/abs/1912.05743> and Pierson's thesis.
-   You can also use shapley values <https://arxiv.org/pdf/2306.05810>, or characteristic functions <https://proceedings.mlr.press/v162/waldchen22a.html> as a way of determining feature importance.

Another idea presented is looking at how the underlying MDP's structure influences the agent. I think these would be the least useful for the forestry domain as they tend to think about incorporating causal models (<https://ojs.aaai.org/index.php/AAAI/article/view/5631>) or by learning a generative state-space model to probe the agent (<https://arxiv.org/abs/1904.01318>).

One idea that is related to how the MDP influences the agent, is identifying important training points that influence the behavior (<https://proceedings.mlr.press/v119/gottesman20a/gottesman20a.pdf>).

Finally, there are the methods that take a more trajectory based approach. This would be similar to the HIGHTLIGHTs algorithms (<https://scholar.harvard.edu/files/oamir/files/highlightsmain.pdf>) described by Pierson's thesis. I think Lazy-MDPs (<https://arxiv.org/pdf/2203.08542>) are a really interesting idea related to "learning interpretable policies". The idea is to penalize "non-lazy" actions, meaning you can identify the transitions where the learned policy decides to "take over" from a default policy. You can also cluster states together to find landmarks (<https://ojs.aaai.org/index.php/ICAPS/article/view/6671>) or create abstract policy graphs (<https://ojs.aaai.org/index.php/AAAI/article/view/4097>). Another recent paper is (<https://arxiv.org/abs/2305.04073>) which tries to come up with a method to identify trajectories that lead towards learning a certain behavior.

There are a lot more ideas/papers discussed in the Milani, and I just provided an overview of papers that I think could be relevant and added papers here and there that weren't included as fas as I could tell in the review paper.

Beyond this review, I've found some extra interesting examples of using explainability in various applications:

-   for UAV path planning: <https://www.sciencedirect.com/science/article/pii/S1270963821005629>
-   for power systems voltage regulation (explainability through converting to decision trees): <https://www.sciencedirect.com/science/article/pii/S0378779625002469>
-   for traffic signal control using shapley values: <https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8917519>

There is also this review, "Explainable and Interpretable Reinforcement Learning for Robotics" by Aaron Roth, that looks very relevant. But I haven't been able to get access to it yet.

<!--list-separator-->

-  Draft v1

    There are a ton of papers that I think are relevant to the forestry + robotics domain that are worth a look. The core of which methods might be applicable are determined by the input space of the agent (i.e. sensor based, image based, or a combination of the two).

    A consistent method used are the creation of decisions trees to explain an agent's strategy. I like decision trees because that could be used for both image and sensor based agents (I believe), and don't rely much on a human visually inspecting an image (like in saliency maps).

    -

    -   (<a href="#citeproc_bib_item_5">Roth, Liang, and Manocha 2021</a>)

    Saliency maps are used throughout image based explanations. These provide some nice insight into what the agent is "looking at" to make a decision. Although in supervised learning they have found that these maps may not provide the best explainability power when the agent makes are "wrong decision" (i.e. classifies a cat as a dog) when tested in human studies.

    Another approach is through causal reasoning. The SHAP/DeepSHAP are the typical methods here, although there are a few methods looking at developing causal graphs from an agents behavior. SHAP determines the relative feature importance by looking at the causal relationship between having and not having the feature in the model at inference time (by seeing how much the output changes based on the features exclusion/inclusion).

    Here are some examples of using these techniques in applied domains:

    -   (<a href="#citeproc_bib_item_1">He, Aouf, and Song 2021</a>)
    -   (<a href="#citeproc_bib_item_5">Roth, Liang, and Manocha 2021</a>)
    -

    There are also some reviews that might be pertinent:

    -   (<a href="#citeproc_bib_item_3">Milani et al. 2024</a>)
    -   (<a href="#citeproc_bib_item_6">Roth et al. 2024</a>) ( I don't have access to this book, but it looks relevant to the robotics domain).
    -

    **Reviews**

    -   (<a href="#citeproc_bib_item_4">Pierson 2021</a>)
    -

    **Saliency Maps**

    -   (<a href="#citeproc_bib_item_4">Pierson 2021</a>)

    **Decisions Trees**

    -   (<a href="#citeproc_bib_item_5">Roth, Liang, and Manocha 2021</a>)

    **SHAP\*/\*Causal**

    -   (<a href="#citeproc_bib_item_1">He, Aouf, and Song 2021</a>)
    -   (<a href="#citeproc_bib_item_2">Madumal et al. 2020</a>)

    [Power Systems Control]({{< relref "power_systems_control.md" >}})

    -   (<a href="#citeproc_bib_item_7">Stiasny et al. 2022</a>)
    -
