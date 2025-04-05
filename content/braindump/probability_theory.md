+++
title = "Probability Theory"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:28:52-07:00
slug = "probability_theory"
draft = false
notetype = "note"
+++

tags
: [Math]({{< relref "math.md" >}})

This is the broad note about probability theory, but should likely be split up to multiple notes, or at least each section should be made into its own note.


## Probability spaces and random variables (without measure theory) {#probability-spaces-and-random-variables--without-measure-theory}

First lets define some basic objects for thinking about the world probabilistically. For an event space \\(\Sigma\\) with events sampled from that space \\(A \in \Sigma\\). We assign a real value \\(\Prob(A) \in \reals\\) to every event in the space and call \\(\Prob\\) a probability distribution or probability measure if it follows the following axioms:

1.  \\(\Prob(A) \geq 0 \forall A\\)
2.  \\(\Prob(\Sigma) = \sum\_{A \in \Sigma} \Prob(A) = 1\\)
3.  If the events are disjoint then

\\[\Prob(\cup\_{i} A\_i) = \sum\_i \Prob(A\_i)\\]

<div title="Random Variable" class="definition">

A Random Variable is a mapping from outcome spaces to real numbers \\(X: \Sigma \rightarrow \reals\\) that assigns a real value to \\(X(\omega)\\) to each outcome \\(\omega\\).

</div>

Given a random variable \\(X\\) we can define the cumulative distribution function (CDF) \\(F\_X: \reals \rightarrow [0, 1]\\) of a random variable \\(X\\) is defined by
\\[
F\_X(x) = \Prob(X \leq x)
\\]

<div class="instance">

(Example from (<a href="#citeproc_bib_item_2">Wasserman 2004</a>)) Flip a fair coin twice and let \\(X\\) be the number of heads. Then \\(\Prob(X=0)=\Prob(X=2) = \frac{1}{4}\\) and \\(\Prob(X=1) = \frac{1}{2}\\). The distribution function is
\\[
F\_{X}(x) = \begin{cases}
0 \quad &x<0 \\\\
\frac{1}{4} \quad &0 \leq x < 1 \\\\
\frac{3}{4} \quad &1 \leq x < 2 \\\\
1 \quad &x \geq 2.
\end{cases}
\\]

</div>

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


## Expectations of a random variable {#expectations-of-a-random-variable}

The expected value, or mean, or first moment of \\(X\\) is defined to be
\\[
\expected(X) = \int x dF(x) = \begin{cases}
\sum\_x xf(x) \quad &\text{if $X$ is discrete}\\\\
\int xf(x)dx \quad &\text{if $X$ is continuous}
\end{cases}
\\]
assuming that the sum (or integral) is well-defined.

**Some properties:**

1.  If \\(X\_1, \ldots, X\_2\\) are random variables and \\(a\_1, \ldots, a\_n\\) are constants, then
    \\[\expected\left(\sum\_i a\_i X\_i \right) = \sum\_i a\_i \expected(X\_i).\\]
2.  Let \\(X\_1, \ldots, X\_2\\) be independent random variables. Then,
    \\[\expected\left(\prod\_{i=1}^n X\_i \right) = \prod\_i \expected(X\_i)\\]

The variance of a distribution is the "spread" of the distribution. The variance of a random variable \\(X\\) with mean \\(\mu\\) is defined by
\\[
\sigma^2 = \var(X) = \expected(X-\mu)^2= \int (x-\mu)^2 dF(x)
\\]

assuming this expectation exists. The _standard deviation_ is \\(sd(X) = \sqrt{\var(X)}\\). The variance has the following properties:

1.  \\(\var(X) = \expected(X^2) - \mu^2\\).
2.  If \\(a\\) and \\(b\\) are constants then \\(\var(aX + b) = a^2\var(X)\\).
3.  If \\(X\_1,\ldots,X\_n\\) are independent and \\(a\_1,\ldots,a\_n\\) are constants, then
    \\[\var\left(\sum\_{i=1}^n a\_i X\_i \right) = \sum\_{i=1}^n a\_i^2 \var(X\_i)\\].

If X and Y are random variables with means \\(\mu\_X\\) and \\(\mu\_Y\\) and standard deviations \\(\sigma\_X\\) and \\(\sigma\_Y\\), the **covariance** between \\(X\\) and \\(Y\\) is defined as
\\[\text{Cov}(X, Y) = \expected[(X-\mu\_X)(Y-\mu\_Y)]\\]
and the correlation by
\\[\rho\_{X, Y} = \rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma\_X \sigma\_Y}\\]


## Moments of a random variable {#moments-of-a-random-variable}

The nth-moment of a random variable is defined as:
\\[
\mu\_n = \expected[(X - c)^n] = \int\_{-\infty}^{\infty} (x-c)^n f(x) dx
\\]

The raw moment is defined as the moment centered around zero (i.e. \\(c=0\\) above). The first raw moment is the mean of the random variable. We can also define the central moments by setting \\(c=\mu\\) or the the center of the moment to the mean of the random variable.
\\[
\expected[(X-\expected[X])^n]
\\]
The second central moment is the variance. Finally, we can normalize the moment by powers of the standard deviation creating _standardized moments_
\\[
\expected[\frac{(X-\expected[X])^n}{\sigma^2}]
\\]
where \\(\sigma=\sqrt{\var(X)}\\) is the standard deviation.

The **skewness** and **kurtosis** are the 3rd and 4th standardized moments respectively. The **skewness** of a distribution is how "skewed" or asymmetric it is around the mean. This gives an indication on where the tail is in a unimodal distribution (i.e. left or right side). The kurtosis describes how much "tail" the distribution has, or its "tailedness".


## Basic Inequalities {#basic-inequalities}

There are a few basic inequalities that everyone should know imho.

<div title="Markov Inequality" class="theorem">

Let \\(X\\) be a non-negative random variable and suppose that \\(\expected(X)\\) exists. For any t&gt;0
\\[\Prob(X>t) \leq \frac{\expected(X)}{t}.\\]

</div>

<div title="Chebyshev’s Inequality" class="theorem">

Let \\(\mu = \expected(X)\\) and \\(\sigma^2 = \var(X)\\). Then
\\[\Prob(|X-\mu| \geq t) \leq \frac{\sigma^2}{t^2} \text{ and } \Prob(|Z|\geq k)\leq\frac{1}{k^2}\\]
where \\(Z = \frac{(X-\mu)}{\sigma}\\). In particular, \\(\Prob(|Z| > 2)\leq \frac{1}{4}\\) and \\(\Prob(|Z| > 3) \leq \frac{1}{9}\\).

</div>


## Classical convergence theorems of random variables {#classical-convergence-theorems-of-random-variables}

There are a few classic results that are important when thinking about probability and statistics in learning theory.

<div title="Law of Large Numbers" class="definition">

The **law of large numbers** says that sample average \\(\bar{X}\_n = n^\inv \sum\_{i=1}^n X\_i\\) **converges in probability** to the expectation \\(\mu = \expected(X)\\).

</div>

The **law of large number** tells us that as we sample from our data more, the sample average will converge to the actual expected value. This means that if we want a better estimate an easy solution is to gather more data, and this has been a common theme in recent machine learning research (i.e. Deep Learning soaks up data).

<div title="Central Limit Theorem" class="definition">

The **central limit theorem** says that sample average has approximately a Normal distribution for large \\(n\\). More exact, \\(\sqrt{n}(\bar{X}\_n - \mu)\\) **converges in distribution** to a \\(\text{Normal}(0, \sigma^2)\\) distribution, where \\(\sigma^2 = \var(X)\\).

</div>

The **central limit theorem** gives us a way to reason about the variance of the sample averages. Because the random variable defined by the sample average will be distributed according \\(\text{Normal}(\mu, \sigma^2)\\) we can estimate the confidence intervals for our current estimate.


## Hypothesis testing and p-values {#hypothesis-testing-and-p-values}

Hypothesis testing is at the core of empirical science, which is a core facet of todays [Machine Learning]({{< relref "machine_learning.md" >}}) research. Hypothesis testing gives us the ability to (with some certainty) measure differences or changes made by experimental interventions. For two methods, say one baseline and one new method designed by the scientist we test two hypotheses simultaneously:

-   **The Null Hypothesis**: The two algorithms perform the same.
-   **The Alternative Hypothesis**: The two algorithms do not perform the same.

Our hope is that the null hypothesis can be rejected given the data collected (i.e. if the new algorithm considerably under or overperforms the baseline).


## Some Discrete Distributions {#some-discrete-distributions}


### Bernoulli {#bernoulli}

Bernoulli distribution is that of a biased coin flip with a probability of getting heads (or a success) set to \\(\alpha\\). For a random variable \\(X \in \\{0, 1\\}\\) we define the Bernoulli distribution as:
\\[X \sim \text{Bernoulli}(\alpha) \rightarrow \Prob(X=x) = \alpha^x (1-\alpha)^{1-x} \\]

where the mean is \\(\alpha\\) and variance is \\(\alpha(1-\alpha)\\).


### Binomial {#binomial}

The binomial distribution is the probability of k successes in n trials of random pulls from the Bernoulli distribution.
\\[X\sim \text{Binomial}(\alpha, n) \rightarrow \Prob(X=k; \alpha, n) = \frac{n!}{k! (n-k)!} \alpha^k (1-\alpha)^{n-k}\\]

where the mean is \\(n\alpha\\) and the variance is \\(n\alpha(1-\alpha)\\)


### Geometric {#geometric}

The geometric distribution is how many trials we need to see before we see a successful trial.
\\[X\sim \text{Geometric}(\alpha) \rightarrow \Prob(X=k; \alpha)=\alpha(1-\alpha)^{k-1}\\]

with mean \\(\frac{1}{\alpha}\\) and variance \\(\frac{1-\alpha}{\alpha^2}\\).


### Poisson {#poisson}

The Poisson distribution is the probability of seeing k independent events in a set interval with a rate \\(\lambda\\).
\\[X \sim \text{Poisson}(\lambda) \rightarrow \Prob(X=k; \lambda) = \frac{\lambda^k e^{-\lambda}}{k!}\\]

where the mean and variance is \\(\lambda\\).


## Some Continual Distributions {#some-continual-distributions}


### Normal {#normal}

The normal (or gaussian) distribution is used quite often. For mean \\(\mu\\) and variance \\(\sigma^2\\)

\\[X \sim \text{Normal}(\mu, \sigma^2) \rightarrow f\_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \\]


### Laplace {#laplace}

The Laplace distribution is like two exponentials centered on the mean.

\\[X \sim \text{Laplace}(\mu, b) \rightarrow f\_X(x) = \frac{1}{2b} e^{-\frac{\lvert x - \mu \rvert}{b}}\\]

with mean \\(\mu\\) and variance \\(2b^2\\).


### Gamma {#gamma}

The gamma distribution is
\\[X \sim \text{Gamma}(\alpha, \beta) \rightarrow f\_X(x) = x^{\alpha-1} e^{-\beta x} \frac{\beta^\alpha}{\Gamma(\alpha)}\\]

with mean \\(\frac{\alpha}{\beta}\\) and variance \\(\frac{\alpha}{\beta^2}\\)


## Measure theory based ideas {#measure-theory-based-ideas}

I'm grabbing most of these notes from (<a href="#citeproc_bib_item_1">Ross and Pekoz 2007</a>).

Let \\(\Sigma\\) be the set of points in a sample space, with \\(\mathcal{F}\\) is a collection of subsets of \\(\Sigma\\). The subsets are called events (so I think \\(\mathcal{F}\\) is an event space?). A probability space is the triple \\((\Sigma, \mathcal{F}, P\\), where \\(P\\) is a function which gives the probability for any event in \\(\mathcal{F}\\).

<div class="definition">

The collection of sets \\(\mathcal{F}\\) is a sigma field, or a \\(\sigma\\)-field, if it has the following three properties:

1.  \\(\Sigma \in \mathcal{F}\\)
2.  \\(A \in \mathcal{F} \rightarrow A^c \in \mathcal{F}\\)
3.  \\(A\_1, A\_2, \ldots \in \mathcal{F} \rightarrow \cup\_{i=1}^\infty A\_i \in \mathcal{F}\\)

</div>

From the definition, these properties ensure that:

1.  The probability of the whole sample space can be calculated.
2.  The complement of any event has a well defined probability.
3.  The countable union of any sequence of events has a well defined probability.


## Questions {#questions}

-   Central limit theorem
-   Different kinds of probability distributions and when you would use them?
-   What is PDF and CDF?
-   What are the different moments and what do they mean?
-   What is skewness?
-   Different kinds of proving convergence.


## Books {#books}

-   [Probability via Expectations]({{< relref "probability_via_expectations.md" >}})
-   (<a href="#citeproc_bib_item_1">Ross and Pekoz 2007</a>)


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Ross, Sheldon M., and Erol A. Pekoz. 2007. <i>A Second Course in Probability</i>. Boston: www.ProbabilityBookstore.com.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>Wasserman, Larry. 2004. <i>All of Statistics: A Concise Course in Statistical Inference Brief Contents</i>. Vol. 26. Springer.</div>
</div>
