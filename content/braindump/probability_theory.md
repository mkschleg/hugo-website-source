+++
title = "Probability Theory"
author = ["Matthew Schlegel"]
lastmod = 2022-10-27T20:20:28-06:00
slug = "probability_theory"
draft = false
notetype = "topic"
+++

tags
: [Math]({{< relref "math.md" >}})


## Random variables and probability functions {#random-variables-and-probability-functions}

First lets define some basic objects for thinking about the world probabilistically. For an event space \\(\Sigma\\) with events sampled from that space \\(A \in \Sigma\\). We assign a real value \\(\Prob(A) \in \reals\\) to every event in the space and call \\(\Prob\\) a probability distribution or probability measure if it follows the following axioms:

1.  \\(\Prob(A) \geq 0 \forall A\\)
2.  \\(\Prob(\Sigma) = \sum\_{A \in \Sigma} \Prob(A) = 1\\)
3.  If the events are disjoint then

\\[\Prob(\cup\_{i} A\_i) = \sum\_i \Prob(A\_i)\\]

A Random Variable is a mapping from outcome spaces to real numbers \\(X: \Sigma \rightarrow \reals\\) that assigns a real value to \\(X(\omega)\\) to each outcome \\(\omega\\).

Given a random variable \\(X\\) we can define the cumulative distribution function (CDF) \\(F\_X: \reals \rightarrow [0, 1]\\) of a random variable \\(X\\) is defined by
\\[
F\_X(x) = \Prob(X \leq x)
\\]

(Example from (<a href="#citeproc_bib_item_1">Wasserman, n.d.</a>)) Flip a fair coin twice and let \\(X\\) be the number of heads. Then \\(\Prob(X=0)=\Prob(X=2) = \frac{1}{4}\\) and \\(\Prob(X=1) = \frac{1}{2}\\). The distribution function is
\\[
F\_{X}(x) = \begin{cases}
0 \quad &x<0 \\\\
\frac{1}{4} \quad &0 \leq x < 1 \\\\
\frac{3}{4} \quad &1 \leq x < 2 \\\\
1 \quad &x \geq 2.
\end{cases}
\\]

A function F which maps the real line to \\([0, 1]\\) is a CDF if and only if:

1.  F is non-decreasing: \\(x\_1 < x\_2 \rightarrow F(x\_1) \leq F(x\_2)\\)
2.  F is normalized: \\(\lim\_{x\rightarrow-\infty} F(x) = 0\\) and \\(\lim\_{x\rightarrow\infty} F(x) = 1\\)
3.  F is right continuous: \\(F(x) = F(x^+)\\) where \\(x^+\\) implies approaching \\(x\\) from above.

We must define two probability functions depending on whether the random variable \\(X\\) is [discrete]({{< relref "discrete.md" >}}) or [continuous]({{< relref "continuous.md" >}}). If the variable is discrete then we define the probability mass function for \\(X\\) by
\\[
f\_X(x) = \Prob(X=x).
\\]

If the random variable \\(X\\) is [continuous]({{< relref "continuous.md" >}}) if there exits a function \\(f\_X\\) such that

-   \\(f\_X(x) \geq 0 \forall x \in X\\)
-   \\(\int\_{-\infty}^{\infty} f\_X(x)dx = 1\\)
-   and for every \\(a \leq b\\)
    \\[
      \Prob(x < X < b) = \int\_a^b f\_X(x)dx.
      \\]

The function \\(f\_X\\) is called a probability density function we have that
\\[
F\_X(x) = \int\_{-\infty}^{x} f\_X(t)dt
\\]

and \\(f\_X(x) = F^\prime\_X(x)\\) at all points \\(x\\) at which \\(F\_X\\) is differentiable.


## Expectations and different moments {#expectations-and-different-moments}

The expected value, or mean, or first moment of \\(X\\) is defined to be


## Basic Inequalities {#basic-inequalities}


## Central Limit Theorem {#central-limit-theorem}


## Questions {#questions}

-   Central limit theorem
-   Different kinds of probability distributions and when you would use them?
-   What is PDF and CDF?
-   What are the different moments and what do they mean?
-   What is skewness?
-   Different kinds of proving convergence.


## Books {#books}

-   [Probability via Expectations]({{< relref "probability_via_expectations.md" >}})
