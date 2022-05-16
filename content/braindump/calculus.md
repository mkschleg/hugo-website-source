+++
title = "Calculus"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:12-06:00
slug = "calculus"
draft = false
notetype = "topic"
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
: [Math]({{<relref "math.md#" >}})

source
:


## Introduction {#introduction}

Calculus is a large subject, and a subject with many interpretations and derivations. Instead of trying to cover all such interpretations, we will look at a more geometric based interpretation with some intuition derived from a physical perspective. It is my hard felt belief that many of these topics are fully realized and appreciated in the study of physical systems (either classical mechanics or electrostatics/electrodynamics). While I could have created this page of notes entirely from the perspective of a physicist, tackling the more general interpretations and forms of these constructs is more useful for the typical machine learning researcher.

In these notes, I assume you have been exposed to several concepts in mathematics:

-   Algebra
-   Limits (including L'Hopital's rule)
-   Geometry

In the final section (section [CFMLR:ML](#CFMLR:ML)), there will be many topics discussed that are critical for doing machine learning research. We assume some passing knowledge of these topics

-   Probability and Statistics
-   Deep Learning
-   Supervised Learning

I've separated these notes into several sections (sections you would often see in any introductory calculus text):

-   Differential Calculus: Building up intuition and definitions for derivatives, gradients, and higher order operations.
-   Integral Calculus: Starting with the fundamental theory of calculus we will uncover the relation between rate of change and the area under the curve.
-   Calculus for Machine Learning: Now that we have some intuition and rigor built up around the concepts of calculus, we will discuss some of the most used notions from a machine learning context.


### Resources used while making these notes: {#resources-used-while-making-these-notes}

I don't do a good job at citing various calculations, or concepts. Much of what I've learned about this subject has come from my physics background with two main resources:

-   An introduction to Electromagnitism
-   Classical Mechanics.

I also pulled much of the formal language from

-   Vector Calculus
-   Wikipedia
-   Mathpedia
-   Wolframalpha

This should not be used as a primary resource for calculus or as a substitution for a more formal book, but a first introduction to the ideas of calculus and how they can apply to machine learning. As such there are many things missing, and many nuanced ideas flattened to be easily digested by many types of Machine Learning researchers.


## Differential Calculus {#CFMLR:DIFF}

If you have never taken a calculus class before, you may be wandering to yourself "what is a derivative or a gradient?" How do they relate to integrals? If you are a machine learning researcher, you may be asking "I know I need gradients to perform (Stochastic) Gradient Descent, but why should we use the gradient and not some other direction?" These are all good questions, and answerable within the context of these notes. This section will dive into the first question.

We will start our discussion with single variate derivatives to make visualization and intuition much easier. As we get into higher dimensional functions (really anything beyond 4 or 5) intuition tends to fly out the window and visualization becomes mostly impossible (at least visualization without projection). With the tools and intuition we build in the single variate case, we will be able to reason about higher dimensional functions. This gives us a powerful tool to understand and work with high dimensional data and function approximators without needing to visualize these functions. If you are familiar with differential calculus, feel free to move on to the next section, but encourage you to read these sections as a review (or to feel pleased about how far you've come in your mathematical understanding).

We will then move to higher dimensional functions, discuss higher order (more than one derivative) operators, different uses of the gradient operator, a special case for non-smooth functions, and finally a discussion on several useful techniques for taking derivatives.


### Single variate derivatives {#single-variate-derivatives}

Lets start by thinking about a hard ball being dropped from a reasonable distance, say at the top of a ladder. Say we wanted to come up with some function of how long the ball will fall in a certain amount of time. One way to do this (requiring the least amount of experimental setup) would be to measure the time a ball dropped at varying heights and then fit this data to some function of time. If we were to take these measurements, the simplest function (approximating the distance rather well) is a parabola

\\[\text{Distance the ball travels after dropping} = f(t) = c t^2 \quad \text{where } c \in \reals, t \ge 0\\].

<aside>
  <aside></aside>

You may be asking where does the ball hit the ground (i.e. what is my stopping condition?). The stopping condition will be the distance the ball has to travel to hit the ground, or the initial position of the ball relative to the release point. While this could be modeled in the above equation, it is easier to just ignore this and reason about a ball that is falling infinitely (with no air resistance) with gravity set at sea level. Trust me when I say these assumptions make the calculations significantly easier to manage, and are more than reasonable for our purposes here.

\vspace{0.2cm}

You may also be wondering about what the constant is representing. Well under normal conditions on earth (i.e. sea level) \\(c\approx \frac{1}{2} \* 9.8\frac{m}{s}\\).  You can derive this quantity from your measurements to a reasonable amount of accuracy.

</aside>

Given this equations, we could ask ourselves how much further has the ball fallen at some time \\(t=2\\). This is quite easy to calculate \\(f(t=2) = c \* 4\\). At \\(t=0\\), we trivially shouldn't fall any distance \\(f(t=0) = c\*0 = 0\\). We may also ask, starting at a certain time \\(t\\), how much distance will I fall after some amount of time \\(dt\\). Many of you may be thinking "isn't this related to the velocity or speed of the ball?", and the answer is a resounding YES! But obviously not the velocity of the ball at time \\(t\\) or at time \\(t+dt\\). So what would the velocity be? Well if you remember from algebra, we can find the rate of change between two points as the slope of the line intersecting both points

\\[\text{Rate of change} = \frac{f(t+dt) - f(t)}{t + dt - t} = \frac{f(t+dt) - f(t)}{dt}\\].

This will give us the average rate of change or average velocity of the ball over the interval \\([t+dt,t]\\). Another reasonable question you may ask yourself is, "how would I get the exact velocity of the ball at time \\(t\\)?". This means what happens to my velocity equation as my change in time decreases to zero. We can't just set \\(dt=0\\) and substitute in, as this would be undefined! Instead we must look at the trend of the function as \\(dt\\) approaches 0. This is known as a limit, leading us to

\\[\text{velocity}(t) = \lim\_{dt \rightarrow 0} \frac{f(t+dt)-f(t)}{dt} \\].

This is the exact definition of a derivative, and we can state

\\[\frac{d f(t)}{dt} = f^\prime(t) = \dot{f}(t) = \lim\_{dt \rightarrow 0} \frac{f(t+dt)-f(t)}{dt} \\].

<aside>
  <aside></aside>

\textbf{A Note on Notation}: We will mostly be using Leibniz's notation (\\(\frac{d f(t)}{dt}\\)) as this easily transitions to higher dimensional functions. But it would be good to know several notation conventions exist and are widely used:

-   Newton Notation: \\(\dot{f}(t) \defeq \frac{d f(t)}{dt}\\)
-   Lagrange Notation: \\(f^\prime(t) \defeq \frac{d f(t)}{dt}\\)

It should be clear why Leibniz's notation is preferred, as it clearly denotes the variable our derivative is being taken over. This will become important when we move to the multi-variate case!

</aside>

You can imagine the two points you are drawing a line through getting extremely close together until they become the same point! This quantity specifies the slope of the tangent line to the function \\(f(t)\\). We can now calculate our first derivative together (using our parabola function)

\begin{align\*}
\frac{d f(t)}{dt} &= \lim\_{dt \rightarrow 0} \frac{f(t+dt)-f(t)}{dt} \\\\\\
&= \lim\_{dt \rightarrow 0} \frac{c(t+dt)^2-ct^2}{dt}	\\\\\\
&= \lim\_{dt \rightarrow 0} \frac{ct^2+ 2ct\*dt + dt^2-ct^2}{dt}\\\\\\
&= \lim\_{dt \rightarrow 0} \frac{2ct\*dt + dt^2}{dt}\\\\\\
&= \lim\_{dt \rightarrow 0} 2ct + dt\\\\\\
\frac{d f(t)}{dt} &= 2ct
\end{align\*}

Because we used a variable \\(t\\) instead of an actual value, we can now ask what velocity our ball is at any place along the parabola!

<aside>
  <aside></aside>

Another way of thinking about a derivative is to consider \\(dx\\) as some perturbation to our function \\(f(x)\\). The derivative tells us for a given input \\(x\\), how \\(f(x)\\) will vary over these perturbations (i.e. how f(x) will vary along the tangent line). This is an incredibly useful value for machine learning as we will see later, and tells us the best search direction in optimizing our function approximators.

</aside>

We can now make this a little bit more formal (although we have covered all the important bits above).

<div class="definition">
  <div></div>

\textbf{Derivative: } Given a continuous, smooth function \\(f: \reals \mapsto \reals\\). We say \\(f(x)\\) is differentiable at \\(x=a\\) if and only if
\\[\lim\_{dx->0^-} \frac{f(a+dx) - f(a)}{dx} = \lim\_{dx->0^+} \frac{f(a+dx) - f(a)}{dx}\\].

We say \\(f(x)\\) is of differentiability class \\(C^{k>1}\\) if it is differentiable at all \\(a \in domain(f)\\). We define the derivative with respect to its input \\(x\\) as:
\\[\frac{d f(x)}{dx} = \lim\_{dx->0} \frac{f(x+dx) - f(x)}{dx}\\]

</div>

<!--list-separator-->

-  Second order single-variate derivatives

    We know now that the derivative of a function is the instantaneous rate of change, or in the physical context the derivative of an object's position function is the velocity of the object. The next question we should ask is "what happens if I take the derivative again?" Well, the answer is quite straightforward: the derivative of the velocity is the instantaneous rate of change of the velocity at time t or the acceleration.

    If we vary the parameter of our function \\(f(t)\\) from left to right, the double derivative gives us a sense of the trend of the function. If the double derivative is positive we would expect the velocity of our function to be increasing meaning our function should eventually be heading towards positive infinity. The inverse is true when the double derivative is negative. In more concrete terms, the second derivative is measuring the **concavity** of our function.

    <div class="definition">
      <div></div>

    \textbf{Concavity} The concavity (or convexity) of a function is an important concept for machine learning and optimization.

    </div>

    We can determine if our function \\(f(x)\\) is concave up (convex) or concave down  at any point in its domain \\(x^\prime\\) using the value of the second derivative. This is a very simple procedure: if the second derivative is positive \\(\frac{d^2 f(x^\prime)}{dx^2} > 0\\) then the function is concave up (also known as convex), if the second derivative is negative \\(\frac{d^2 f(x^\prime)}{dx^2} < 0\\) the second derivative is concave down. What if the second derivative is zero \\(\frac{d^2 f(x^\prime)}{dx^2} = 0\\)?

    <div class="definition">
      <div></div>

    \textbf{Inflection point} any point where the second derivative of our function is zero and there is a sign change. A bit more formally with \\(\epsilon\\) as a small positive real number, \\(x^\prime\\) is an inflection point of a function \\(f(x)\\) if

    \begin{align\*}
    &\frac{d^2 f(x^\prime)}{dx^2} = 0 \\\\\\
    &sign(\frac{d^2 f(x^\prime + \epsilon)}{dx^2}) \neq sign(\frac{d^2 f(x^\prime - \epsilon)}{dx^2})
    \end{align\*}

    This only holds as long as \\(x^\prime + \epsilon\\) and \\(x^\prime + \epsilon\\) are in the neighborhood of \\(x^\prime\\). There are other sufficiency conditions for an inflection point, which may be covered at a latter time in these notes.

    </div>

    <aside>
      <aside></aside>

    We can start constructing classes of functions according to their derivatives, which we denote as differentiability class or smoothness class. We first start with the \\(C^{0}\\) set of functions which contains all continuous functions. The next class \\(C^{1}\\) contains all functions such that their derivatives are in \\(C^{0}\\) (i.e. continuous). We can define the kth class as \\(C^{k}\\) with functions whose \\([1, 2, \ldots, kth]\\) -derivatives are continuous. We declare a function smooth if it is infinitely differentiable and of the set \\(C^{\infty}\\). One such function is the exponential, also the cosine and sinusoidal functions.

    </aside>

<!--list-separator-->

-  A note on extrema

    With the derivative and second derivative, we have finally built up enough tools to find the extrema of our function! An extrema point of a function are broken into two categories: minima and maxima. We can also specify whether these extrema hold over the functions domain (i.e. they are globally extreme) or if they are only extreme to the local region of the point. A function may have many local extrema, but will only have up to one global minima and up to one global maxima. Also, any given function is not guaranteed to have any extrema (for instance a line with slope \\(\neq 0\\))!

    If you stare at a visual representation of our parabola function \\(f(t) = at^2 + bt + c\\) it is quite clear where the minima is, but how do we find this for any function we could possibly dream up? You may notice at the mimima our function changes direction, and in fact this is a shared property of all extrema (but not a sufficient condition). We can construct a set of candidate points for a functions extrema \\(\tilde{E}\_x \subset domain(f)\\) by finding the set of points where the derivative is zero:

    \\[\text{The set of candidate extrema } E\_x = \\{x \in domain(f) \text{ such that } \frac{d f(x)}{dx} = 0\\}\\].

    Now that we have our candidate set \\(\tilde{E}\_x\\) we need to test to see if these points are minima or maxima. The most straightforward method of doing this is through the second derivative test! From our discussion above it should be clear what this entails, but for completeness a point \\(x^\prime \in \tilde{E}\_x\\) is a

    -   a minima if \\(\frac{d^2 f(x^\prime)}{dx^2} > 0\\)
    -   a maxima if \\(\frac{d^2 f(x^\prime)}{dx^2} < 0\\).

    Unfortunately, this test is insufficient to check for minima, or maxima if the second derivative is zero! In these instances you will need to check higher order tests to determine the type of extrema. These higher order tests are out of the scope of these notes, but are easily found in any calculus textbook or online.


### The Gradient Operator {#the-gradient-operator}

We now know how to take the derivative with respect to a single variable, and actually this gives us enough tooling to move straight to higher dimensions! We are going to make some assumptions about our function which we will loosen as we progress in our study. First, our function \\(f(\cdot)\\) is continuous and smooth. We can actually specify how smooth a function is using derivatives, but we will discuss this later. Our function also has a range \\(\in \reals\\). This means it can take any value in the real number set (or a subset of this) and is a scalar value. We will look at what happens if our function is a vector in the next section.

Now that the we have our assumptions specified, lets think about what a derivative may mean with higher dimensional domains. How might we do this? We could imagine perturbing each dimension jointly. Say for a two parameter function \\(f(x,y)\\), we could perturb along the vector \\([dx, dy]\\) and take the limits together using the above formulation (assuming our space follows the Euclidean metric)

\\[\lim\_{dx \rightarrow 0} \lim\_{dy \rightarrow 0} \frac{f(x+dx, y+dy) - f(x,y)}{\sqrt{(x+dx - x)^2 + (y+dy - y)^2}}
   = \lim\_{dx \rightarrow 0} \lim\_{dy \rightarrow 0}\frac{f(x+dx, y+dy) - f(x,y)}{\sqrt{(dx)^2 + (dy)^2}}\\].

Something you may notice is the inner limit can be immediately applied, as the denominator will not become problematic until both limits are applied. We then recover our usual notion of a gradient, but for a single variable of our multi-variate function. This is called a **partial derivative**

\\[\frac{\partial}{\partial x} f(x, y) = \lim\_{dx \rightarrow 0} \frac{f(x+dx, y) - f(x, y)}{dx}\\]

Intuitively this gives us how much the function will change if we only apply a perturbation to the x component. We can also construct a partial for the second parameter of our function

\\[\frac{\partial}{\partial y} f(x, y) = \lim\_{dy \rightarrow 0} \frac{f(x, y + dy) - f(x, y + dy)}{dy}\\].

Now that we have derivatives representing the rate of change of each variable we can construct vectors from the partial derivatives to get the exact direction the function is moving in the space. We have finally come to one definition of the gradient!

\\[\text{Gradient of $f(x,y)$} \defeq \begin{bmatrix} \frac{\partial}{\partial x} f(x,y) \\ \frac{\partial}{\partial y} f(x,y)\end{bmatrix} = \begin{bmatrix} \frac{\partial}{\partial x} \\ \frac{\partial}{\partial y} \end{bmatrix} f(x,y) = \vec{\nabla} f(x,y) = \nabla f(x,y)\\]

Notice that the gradient operator is a vector operator it self, and is sometimes referred as the _vector differential operator_ or _del_. By convention we leave off the vector identification and always assume the gradient is a vector with the same length as the number of parameters our function takes. Another convention is the operator always appearing on the left of a scalar function (or really any function). If you are familiar with linear algebra, you should see why (i.e. a left product _could_ be different from a right product). We will also treat the gradient as a column vector from here on out.

Thus far we have defined the gradient over only two dimensions, but of course we can easily extend this to n dimensions.

\\[\nabla \defeq \begin{bmatrix} \partialderiv{}{x\_1}\\ \vdots \\ \partialderiv{}{x\_n} \end{bmatrix}\\]


### Gradients over vector fields {#gradients-over-vector-fields}

The functions we have been considering thus far have been **scalar fields** where \\(f: A \subset \reals^n \rightarrow \reals\\). Now that we know how gradients work over scalar functions, we will look at how gradients will work over vector fields.

<div class="definition">
  <div></div>

\textbf{Vector Fields}: a \textbf{vector field} in \\(\reals^n\\) is a map \\(\mathbf{F}: A \subset \reals^n \mapsto \reals^n\\) that assigns to each point \\(\xvec\\) in its domain A a vector \\(\mathbf{F}(\xvec)\\). If n = 2, \\(\mathbf{F}\\) is called a \textbf{vector field in the plane}, and if n=3, \\(\mathbf{F}\\) is a \textbf{vector field in space}.

We have already covertly encountered a vector field in these notes! Specifically, the gradient of any scalar function is a vector field over the domain of the scalar function!

</div>

<aside>
  <aside></aside>

We are only considering vector fields in these notes, but you could imagine functional maps such as \\(\mathbf{F}: A \subset \reals^n \mapsto \reals^m\\). We revisit this type of function in our study of the Jacobian (to make the definition more general). There are several interesting properties which pop up when we consider functions of this form, but leave a discussion on these as beyond the scope of these notes.

</aside>

There are three ways the gradient operator can interact with a vector field. We will explore each separately starting with the Jacobian

<!--list-separator-->

-  Jacobian

    The Jacobian is the outer product of the gradient operator and our vector field. More concretely

    \\[\text{The Jacobian: } \jacobian \defeq \nabla \otimes \Fmat =
        \left[\partialderiv{\Fmat}{x\_1}, \cdots, \partialderiv{\Fmat}{x\_n}\right] =
        \left[\begin{array}{ccc}{
         \frac{\partial \Fmat\_{1}}{\partial x\_{1}}} & {\cdots} & {\frac{\partial \Fmat\_{1}}{\partial x\_{n}}} \\\\\\
         {\vdots} & {\ddots} & {\vdots} \\\\\\
         {\frac{\partial \Fmat\_{m}}{\partial x\_{1}}} & {\cdots} & {\frac{\partial \Fmat\_{m}}{\partial x\_{n}}}
        \end{array}\right]\\]

    Some properties:

    -

<!--list-separator-->

-  Divergence

    The divergence is the inner product of the gradient operator and a vector field \\(\Fmat\\),

    \\[\text{The Divergence: } div(\Fmat) \defeq \nabla \cdot \Fmat = \sum\_{i=i}^n \partialderiv{\Fmat\_i}{x\_i}\\]

    Some properties:

<!--list-separator-->

-  Curl

    The curl is the cross product of the gradient operator and a vector field \\(\Fmat\\). We will only consider the curl up to three dimensions for simplicity.

    \\[\text{The Curl: } curl(\Fmat) \defeq \nabla \times \Fmat =
        \left|\begin{array}{ccc}
        {\hat{\imath}} & {\hat{\jmath}} & {\hat{k}} \\\\\\
        {\frac{\partial}{\partial x}} & {\frac{\partial}{\partial y}} & {\frac{\partial}{\partial z}} \\\\\\
        {\Fmat\_{x}} & {\Fmat\_{y}} & {\Fmat\_{z}}\end{array}\right|\\]


### Higher Order Operators {#higher-order-operators}

Now that we have covered a gradients interactions with vector fields we can consider higher order gradients (analogous to higher order derivatives). As you may have already noticed, when we apply the gradient operator on to a function of the form \\(f: \reals^d \mapsto \reals\\) we produce a new function which is a vector field! This observation allows for multiple ways of constructing second order operators, two of which we cover below.

<!--list-separator-->

-  Hessian

    The Hessian is an important construct for machine learning, particularly in optimization and step-size adaptation where the Hessian is often evoked (although not computed). We will look at Newtonian methods in section [CFMLR:ML](#CFMLR:ML).

    To construct the Hessian, we will simply take the Jacobian of the gradient of our function.

<!--list-separator-->

-  Laplace Operator

    While the Hessian is more widely used in Machine Learning contexts, the Laplace operator is still good to know about. It is significantly simpler as a construct, and is constructed as the divergence of the gradient of our function.


### Finding Extrema {#finding-extrema}

We look for extrema in the multi-variate case just as we did for the single variate case. We look for points which have gradients equal to the zero vector. We then use the multi-variate second derivative test.


### Sub-gradients {#sub-gradients}

-   Non-continuous functions (absolute value, relu).


### Some useful techniques and derivatives {#some-useful-techniques-and-derivatives}

We will look at several useful techniques and formulas for calculating derivatives. While not an exhaustive list, many of these techniques consistently appear in machine learning.

<!--list-separator-->

-  Product Rule

    \\[\nabla\_{\xvec} f(\xvec)g(\xvec) = f(\xvec) \nabla\_{\xvec} g(\xvec) + g(\xvec) \nabla\_{\xvec} f(\xvec)\\]

<!--list-separator-->

-  Chain Rule

    \\[\nabla\_{\xvec} (f \circ g)(\xvec) = \nabla\_g f(g(\xvec)) \nabla\_{\xvec}g(\xvec)\\]

<!--list-separator-->

-  Implicit Differentiation

<!--list-separator-->

-  Useful Derivatives

    -   \\(x^n\\)
        \\[\partialderiv{}{x} x^n = nx^{n-1} \quad \triangleright \quad n \neq 0, n\in\reals\\]
    -   \\(e^x\\)
        \\[\partialderiv{}{x} e^x = e^x\\]
        \\[\partialderiv{}{x} a^x = \ln(a)\*a^x \quad \triangleright \quad a > 0\\]
    -   \\(ln(x)\\)
        \\[\partialderiv{}{x} \ln(x) = \frac{1}{x}\\]
        \\[\partialderiv{}{x} \log\_{a}(x) = \frac{1}{x\ln(a)} \quad \triangleright \quad a > 0\\]
    -   trig


## Integral Calculus {#CFMLR:INT}


### Riemmanian sums {#riemmanian-sums}


### Line Integrals (Riemmanian Integrals) {#line-integrals--riemmanian-integrals}


### Fundamental Theorem of Calculus {#fundamental-theorem-of-calculus}


### "Anti-derivative" {#anti-derivative}


### Useful techniques {#useful-techniques}

<!--list-separator-->

-  By Parts

<!--list-separator-->

-  Substitution

<!--list-separator-->

-


## Calculus for Machine Learning {#CFMLR:ML}


### Critical Points and Optimization {#critical-points-and-optimization}


### Projection {#projection}


### Probability {#probability}


### Deep Learning {#deep-learning}
