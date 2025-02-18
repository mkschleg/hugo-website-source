+++
title = "SVD"
author = ["Matthew Schlegel"]
lastmod = 2022-11-08T14:23:38-07:00
slug = "svd"
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
: [Linear Algebra]({{< relref "linear_algebra.md" >}})

Singular value decomposition (SVD) is a [matrix factorization]({{< relref "linear_algebra.md#matrix-factorizations" >}}). It generalizes [eigendecomposition]({{< relref "eigendecomposition.md#eigendecomposition" >}}) of a square normal matrix to any complex matrix \\(\Mmat \in \complexs^{m\times n} \\). Specifically, it is a factorization of the form

\\[\Mmat = \Umat\boldsymbol{\Sigma}\Vmat^\*.\\]

-   \\(\Umat\\) is a [complex unitary matrix]({{< relref "linear_algebra.md#unitary-matrix" >}}).
-   \\(\Sigmamat\\) is a \\(m\times n\\) [rectangular diagonal matrix]({{< relref "linear_algebra.md#diagonal-matrix" >}}) with non-negative real numbers on the diagonal.
-   \\(\Vmat\\) is a  [complex unitary matrix]({{< relref "linear_algebra.md#unitary-matrix" >}}).

Singular values are always positive (by convention) and are found from the two conditions:
\\[\Mmat \vvec = \sigma \uvec \text{ and } \Mmat^\* \uvec = \sigma \vvec\\]

where \\(\vvec\\) and \\(\uvec\\) are called right and left singular vectors respectively.

This decomposition always exists for any complex rectangular matrix.


## Rotation, Coordinate Scaling, and reflection {#rotation-coordinate-scaling-and-reflection}

One nice interpretation of singular value decomposition is as a series of rotations scalings. Every matrix can be seen as a linear function on a vector. To visualize this we will use julia and a random linear transform matrix \\(M\\).

```julia
using Plots
import LinearAlgebra: LinearAlgebra, svd
import Random

function plot_data(dat, clrs)
    Plots.scatter([(dd[1], dd[2]) for dd in eachcol(dat)], color=clrs, xlim=(-1.5, 1.5), ylim=(-1, 1), legend=false)
end
```

```text
┌ Info: Precompiling Plots [91a5bcdd-55d7-5caf-9e0b-520d859cae80]
└ @ Base loading.jl:1664
plot_data (generic function with 1 method)
```

Below we construct the data used in the shape of a circle to make the scaling and rotations very clear. We color each quadrant a different color to get the full effect.

```julia
rng = Random.Xoshiro(10)
d = rand(rng, 2, 5000) * 2 .- 1.0
ids = (d[1, :].^2 .+ d[2, :].^2 .<= 1)
d_circ = d[:, ids]
mk_color(dt) = begin
    if dt[1] < 0.0 && dt[2] < 0.0
        :green
    elseif dt[1] >= 0.0 && dt[2] < 0.0
        :yellow
    elseif dt[1] >= 0.0 && dt[2] >= 0.0
        :blue
    else
        :red
    end
end
clrs = [mk_color(d_circ[:, i]) for i in 1:size(d_circ, 2)]
plot_data(d_circ, clrs)
```

{{< figure src="/ox-hugo/svd-data.svg" >}}

Below we plot the full linear transformation.

```julia
M = rand(rng, 2, 2)
d_trans = M*d_circ
plot_data(d_trans, clrs)
```

{{< figure src="/ox-hugo/svd-transform.svg" >}}

We now use julia to find the decomposition of our matrix \\(M\\).

```julia
M_svd = svd(M)
```

```text
LinearAlgebra.SVD{Float64, Float64, Matrix{Float64}, Vector{Float64}}
U factor:
2×2 Matrix{Float64}:
 -0.864209  -0.503132
 -0.503132   0.864209
singular values:
2-element Vector{Float64}:
 1.2239572979398925
 0.40347199419954716
Vt factor:
2×2 Matrix{Float64}:
 -0.701446  -0.712723
  0.712723  -0.701446
```

With the decomposition created, we can now go through each operation in order. The first is \\(\Vmat^\*\\) as a rotation.

```julia
d_Vt = M_svd.Vt*d_circ
plot_data(d_Vt, clrs)
```

{{< figure src="/ox-hugo/svd-vt.svg" >}}

Then \\(\Sigmamat\\) is a scaling along the new axis determined by the rotation from \\(\Vmat^\*\\).

```julia
Σ = LinearAlgebra.diagm(M_svd.S)
d_ΣVt = Σ*M_svd.Vt*d_circ
plot_data(d_ΣVt, clrs)
```

{{< figure src="/ox-hugo/svd-sigvt.svg" >}}

Finally, \\(\Umat\\) rotates the new scaled data to its final position.

```julia
d_UΣVt = M_svd.U*Σ*M_svd.Vt*d_circ
plot_data(d_UΣVt, clrs)
```

{{< figure src="/ox-hugo/svd-usigvt.svg" >}}
