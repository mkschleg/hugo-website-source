+++
title = "Recurrent Neural Network"
author = ["Matthew Schlegel"]
lastmod = 2023-03-20T12:43:36-06:00
slug = "recurrent_neural_network"
draft = false
notetype = "note"
+++

tags
: [Neural Network]({{< relref "neural_network.md" >}})

See other extensions: [LSTM]({{< relref "lstm.md" >}}), [GRU]({{< relref "gru.md" >}}), (<a href="#citeproc_bib_item_1">Chandar et al. 2019</a>), (<a href="#citeproc_bib_item_3">Goudreau et al. 1994</a>), (<a href="#citeproc_bib_item_4">Sutskever, Martens, and Hinton 2011</a>), (<a href="#citeproc_bib_item_2">Cho et al. 2014</a>)


## Getting Started {#getting-started}

Some basic RNN resources. Here is some stuff to get you started:
Really early RNN Work:

-   <http://srsc-mac1.ulb.ac.be/axcWWW/papers/pdf/91-NC.pdf>
-   (bptt) <http://axon.cs.byu.edu/Dan/678/papers/Recurrent/Werbos.pdf>
-   (rtrl) <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.52.9724&rep=rep1&type=pdf>

LSTMs:

-   <http://www7.informatik.tu-muenchen.de/~hochreit>
-   <https://www.researchgate.net/profile/Felix_Gers/publication/12292425_Learning_to_Forget_Continual_Prediction_with_LSTM/links/5759414608ae9a9c954e84c5/Learning-to-Forget-Continual-Prediction-with-LSTM.pdf>
-   (In RL) <http://papers.nips.cc/paper/1953-reinforcement-learning-with-long-short-term-memory.pdf>

Some other useful things:

-   (review on more modern learning techniques) <https://ieeexplore.ieee.org/abstract/document/6639349>
-   (On the difficulty of training) <http://proceedings.mlr.press/v28/pascanu13.pdf>
-   (overview on some basic RNN algorithms) <https://pdfs.semanticscholar.org/cccd/3fd7a45e7643f26391bd539ffbede0690f36.pdf>
-   (Colah’s blog) <https://colah.github.io/posts/2015-08-Understanding-LSTMs/>

Some ideas that I believe could use some more research:

-   (Echo State Netwoks) <http://www.scholarpedia.org/article/Echo_state_network>
-   (Bi Directional LSTMs/RNNs) <https://ieeexplore.ieee.org/document/4288069>



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Chandar, Sarath, Chinnadhurai Sankar, Eugene Vorontsov, Samira Ebrahimi Kahou, and Yoshua Bengio. 2019. “Towards Non-saturating Recurrent Units for Modelling Long-term Dependencies.” In <i>AAAI</i>. <a href="https://arxiv.org/abs/1902.06704">https://arxiv.org/abs/1902.06704</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Cho, Kyunghyun, Bart van Merriënboer, Dzmitry Bahdanau, and Yoshua Bengio. 2014. “On the Properties of Neural Machine Translation: EncoderDecoder Approaches.” In <i>Proceedings of SSST-8, Eighth Workshop on Syntax, Semantics and Structure in Statistical Translation</i>. Doha, Qatar: Association for Computational Linguistics.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>Goudreau, M.W., C.L. Giles, S.T. Chakradhar, and D. Chen. 1994. “First-Order versus Second-Order Single-Layer Recurrent Neural Networks.” <i>IEEE Transactions on Neural Networks</i>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>Sutskever, Ilya, James Martens, and Geoffrey Hinton. 2011. “Generating Text with Recurrent Neural Networks.” In <i>Proceedings of the 28th International Conference on International Conference on Machine Learning</i>. ICML’11. Bellevue, Washington, USA: Omnipress.</div>
</div>
