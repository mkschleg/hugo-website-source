+++
title = "Principle Component Analysis"
author = ["Matthew Schlegel"]
lastmod = 2022-11-08T14:21:47-07:00
slug = "principle_component_analysis"
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
: [Linear Algebra]({{< relref "linear_algebra.md" >}}), [Machine Learning]({{< relref "machine_learning.md" >}}), [Dimensionality Reduction]({{< relref "dimensionality_reduction.md" >}})

PCA is a linear transformation of data into a lower dimensional space. Approximately, it is reducing the number of variables to those which maximally explain the variance of the input distribution.

<div class="note">

PCA doesn't consider the output variable \\(\yvec\\) and only considers the input space.

</div>

The procedure of PCA is very straightforward. We will use Julia to explore this in code along side the mathematics.

Take the randomly generated data \\(\Xmat \sim \mathscr{N}(\boldsymbol{\mu}, \Sigmamat)\\)

```julia
import Random
import Distributions
import LinearAlgebra
using Statistics
Random.seed!(42)
n = 10
r = rand(n, n) # -> Random square matrix
Σ = 0.5 .* (r .+ transpose(r)) # -> fulfill hermitian quality
Σ = Σ * Σ' # -> make positive definite
μ = rand(n)
mvnormal = Distributions.MvNormal(μ, Σ)
X = rand(mvnormal, 1000); # generate random samples!
```

```text
10×1000 Matrix{Float64}:
  0.154199  -1.49158    -0.0868507  …  2.71999    0.328476  3.28587
 -1.73977   -4.54743    -1.64781       1.26305   -0.964122  2.36852
  1.75934   -0.22245    -2.66986       1.87835    0.143766  3.42757
  0.483097   0.0193946  -2.20942       0.681505   0.966159  0.579813
 -0.316423  -2.78624    -1.98411       1.12531   -0.894616  2.90124
 -0.312561  -2.18022    -0.973733   …  2.1518    -0.56188   2.36528
  0.511511  -1.7023     -1.02764       2.60661   -0.481111  3.61041
 -1.50101   -3.1519     -0.200225      2.43156   -1.74699   2.20487
 -0.821829  -1.15865    -1.73997       1.98992   -0.664556  1.59292
  0.596334  -0.457017   -0.955204      2.23139    0.829376  2.52783
```

Lets then center and normalize the data (good practice when applying PCA)

```julia
for r in eachrow(X)
    r .= (r .- mean(r))/sqrt(var(r))
end
(μ = [mean(r) for r in eachrow(X)], σ = [var(r) for r in eachrow(X)])
```

|   |   |                                                                                                                                                                                                                                      |   |   |                                                                                                                                                                                               |
|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| μ | = | (3.8524738954492934e-16 -1.7541523789077474e-17 5.813127756937319e-16 4.786449014915206e-17 -9.214851104388799e-17 -1.056932319443149e-16 -3.312905505481467e-16 2.808864252301646e-17 6.272760089132134e-17 2.3436808049837057e-16) | σ | = | (1.0000000000000004 0.9999999999999989 1.0000000000000018 1.0000000000000009 1.0000000000000013 1.0000000000000016 1.0000000000000002 1.0000000000000004 1.000000000000001 1.000000000000001) |

Now for the PCA steps:

1.  Find the covariance matrix:
    ```julia
    cov_X = reduce(hcat, [[cov(X[i, :], X[j, :]) for i in 1:size(X, 1)] for j in 1:size(X, 1)]);
    ```

2.  Find the [Eigenvalues and Eigenvectors]({{< relref "eigendecomposition.md" >}}) of the covariance matrix over features (not instances):
    ```julia
      eig_decomp = LinearAlgebra.eigen(cov_X)
    ```

    ```text
      LinearAlgebra.Eigen{Float64, Float64, Matrix{Float64}, Vector{Float64}}
      values:
      10-element Vector{Float64}:
       0.007715000421140434
       0.022122836945468412
       0.050975169388851244
       0.1019179524919782
       0.15467299923069255
       0.167709613102825
       0.29591848119171205
       0.35809938668170255
       0.5306327788236761
       8.310235781721957
      vectors:
      10×10 Matrix{Float64}:
       -0.257659    0.550342   -0.358217   …   0.315542   -0.259167  -0.327279
       -0.140607   -0.0141494   0.185948       0.0283486  -0.301952  -0.315263
       -0.428342   -0.182125   -0.160589       0.199804    0.328478  -0.317831
       -0.044105    0.11834     0.472907      -0.196097    0.579875  -0.302697
        0.0958392  -0.117859   -0.404129      -0.537977    0.183993  -0.306393
        0.342345   -0.655594   -0.0355161  …   0.188939   -0.296173  -0.330094
        0.474422    0.36916     0.433542       0.010172   -0.189465  -0.331819
       -0.484712   -0.128023    0.232115      -0.409266   -0.380797  -0.306969
        0.376203    0.182543   -0.419783      -0.175664    0.105664  -0.320347
        0.0219657  -0.141647    0.0709813      0.545598    0.289595  -0.301763
    ```

3.  Order the [eigenvector]({{< relref "eigendecomposition.md" >}})s by the [eigenvalues]({{< relref "eigendecomposition.md" >}}). Conveniently these are already ordered based on the [eigenvalues]({{< relref "eigendecomposition.md" >}}) and the [eigenvector]({{< relref "eigendecomposition.md" >}})s are the columns of the matrix. We need to choose how many components we want to use. The best way to do this is through the total explained variance of the k features.
    ```julia
    tot = sum(eig_decomp.values)
    cumsum([(i/tot)*100 for i in reverse(eig_decomp.values)])
    ```

    ```text
      10-element Vector{Float64}:
        83.10235781721954
        88.4086856054563
        91.98967947227332
        94.94886428419045
        96.6259604152187
        98.17269040752562
        99.1918699324454
        99.70162162633392
        99.9228499957886
       100.0
    ```

4.  The first 4 components explain the majority of the variance (\\(95\\%\\)) so lets just use the first 4! So lets create a projection matrix from the first four [eigenvector]({{< relref "eigendecomposition.md" >}})s!
    ```julia
      proj_mat = reduce(hcat, [eig_decomp.vectors[:, size(eig_decomp.vectors, 2) - i] for i in 0:3])
    ```

    ```text
      10×4 Matrix{Float64}:
       -0.327279  -0.259167   0.315542   -0.0801132
       -0.315263  -0.301952   0.0283486  -0.320827
       -0.317831   0.328478   0.199804   -0.240223
       -0.302697   0.579875  -0.196097    0.0395761
       -0.306393   0.183993  -0.537977   -0.424623
       -0.330094  -0.296173   0.188939   -0.0328097
       -0.331819  -0.189465   0.010172   -0.219942
       -0.306969  -0.380797  -0.409266    0.463266
       -0.320347   0.105664  -0.175664    0.551859
       -0.301763   0.289595   0.545598    0.287157
    ```

5.  Now we can project our data:
    ```julia
    proj_x = proj_mat' * X
    ```

    ```text
    4×1000 Matrix{Float64}:
      1.10367   3.89547    3.30802   …  -2.37649   1.35173    -3.32848
      0.802943  1.36961   -1.41826      -0.660894  0.753229   -0.613667
      0.311876  0.253764  -0.122628      0.267786  0.36768     0.291698
     -0.306181  0.639849   0.373242      0.483446  0.0351702  -0.535202
    ```
