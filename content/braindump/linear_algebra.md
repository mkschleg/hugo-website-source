+++
title = "Linear Algebra"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:28:13-07:00
slug = "linear_algebra"
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
: [Math]({{< relref "math.md" >}})


## Vector Space {#vector-space}

A **vector space** is a set of vectors together with rules for vector addition and multiplication by scalars. The addition and multiplication rules must be consistent with the following properties (for \\(x\in\mathbb{F}^n\\), \\(c\in\mathbb{F}\\), \\(\mathbb{F} = \\{\mathbb{R}, \mathbb{C}\\}\\) ):

1.  \\(\xvec+\yvec = \yvec+\xvec\\)
2.  \\(\xvec+(\yvec+\zvec) = (\xvec+\yvec) + \zvec\\)
3.  There is a unique zero vector \\(\mathbf{0} + \xvec = \xvec\\)
4.  For each \\(\xvec\\) there is a unique vector \\(-\xvec\\) such that \\(\xvec + (-\xvec) = \mathbf{0}\\).
5.  \\(1\xvec = \xvec\\)
6.  \\((c\_1c\_2)\xvec = c\_1(c\_2\xvec)\\)
7.  \\(c(\xvec + \yvec) = c\xvec + c\yvec\\)
8.  \\((c\_1 + c\_2)\xvec = c\_1\xvec + c\_2\xvec\\)

<div class="definition">

A **vector space** is a set of vectors which is closed under rules for vector addition and multiplication by scalars (i.e. rules to take linear combinations of vectors).

</div>


### Vector Subspaces {#vector-subspaces}

A **vector subspace** is a non-empyt subset of a vector space which is closed under the same linear combination rules. The most trivial vector subspace of \\(\reals^n\\) is the set containing the zero vector.

<div class="definition">

A **subspace** of a vector space is a nonempty subset that satisfies the requirements for a vector space: **Linear combinations stay in the subspace**.

</div>


### Column (row) space of a matrix {#column--row--space-of-a-matrix}

The column space of a matrix is all possible linear combinations of the columns of a matrix. The row space is the same except with linear combinations of the rows of a matrix.


### Nullspace of a matrix {#nullspace-of-a-matrix}

<div class="definition">

Given a matrix \\(\Amat \in \reals^{M\times N}\\). The **nullspace** of \\(\Amat\\) is all vectors \\(\xvec\\) such that \\(\Amat\xvec = \mathbf{0}\\).

</div>

The nullspace is:

-   A subspace of \\(\reals^M\\)


### Dual Space {#dual-space}

The dual vector space is the set \\(V^\star\\) of all **linear functionals** \\(f: V \mapsto \mathbb{F}\\). Since linear functionals are vector space homomorphisms this is sometimes denoted as \\(Hom(V, \mathbb{F})\\). The dual space is itself a vector space, meaning (for \\(\phi, \psi \in V^\star\\) and \\(\xvec \in V\\))

1.  \\((\phi + \psi)(\xvec) = \phi(\xvec) + \psi(\xvec)\\)
2.  \\((\alpha \phi)(\xvec) = \alpha\phi(\xvec)\\).

The dual vector space has the same dimensions as the original vector space, and has a canonical dual basis (or **cobasis**) \\(\theta^j\\) defined by the original basis \\(e\_i\\)

\\[\langle e\_i, \theta^j \rangle = \delta^j\_i \quad \triangleright \delta^j\_i \text{ is the Kronecker delta function}\\].

Notation gets a bit confusing in higher order linear algebra and tensor algebra. Typically, I will attempt to denote an index of the cobasis as an upstairs index while the basis as a downstairs index.


### Vector operations {#vector-operations}


#### Dot Product {#dot-product}

The dot product between two vectors
\\[\vvec \cdot \wvec = \sum\_i \vvec\_i \wvec\_i\\]
and can also be thought of as
\\[\lVert\vvec\rVert \lVert\wvec\rVert cos(\theta)\\]
where \\(\theta\\) is the angle between the two vectors. The angle can be found through
\\[
\theta = \text{arccos}(\frac{\vvec \cdot \wvec}{\lVert\wvec\rVert \lVert\vvec\rVert})
\\]


#### Cross Product {#cross-product}

The cross product between two vectors in \\(\reals^3\\) under the canonical basis.
\\[
\vvec \times \wvec = \begin{bmatrix}
(\vvec\_2\wvec\_3 - \vvec\_3\wvec\_2) \\\\
(\vvec\_1\wvec\_3 - \vvec\_3\wvec\_1) \\\\
(\vvec\_1\wvec\_2 - \vvec\_2\wvec\_1)
\end{bmatrix}
\\]

It can also be through of more formally as a determinant of the matrix

\begin{vmatrix}
\ivec & \jvec & \kvec \\\\
\vvec\_1 & \vvec\_2 & \vvec \_3 \\\\
\wvec\_1 & \wvec\_2 & \wvec\_3
\end{vmatrix}


## Bases (Linear Algebra) {#bases--linear-algebra}


## Matrices {#matrices}

We first start from a set of linear equations, to build up intuition about what a matrix is representing. We will then move to a more general case and discuss operations of matrices


### From Eqns to a Matrix {#from-eqns-to-a-matrix}

We star with a set of equations with nine coefficients, three unknowns, and three right-hand sides.

\begin{align\*}
     2u + v + w &= 5 \\\\
     4u - 6v &=-2 \\\\
     -2u + 7v + 2w &=9
\end{align\*}

We represent the right hand side with a **column vector** (or a 1 by 3 matrix). The unknowns of the system are represented as a column vector as well.

\\[x=\left[\begin{array}{l}{u} \\\ {v} \\\ {w}\end{array}\right]\\]

We define a square 3 by 3 matrix of the coefficients

\\[A=\left[\begin{array}{ccc}
   {2} & {1} & {1} \\\\
   {4} & {-6} & {0} \\\\
   {-2} & {7} & {2}
   \end{array}\right]\\]

While we present a square matrix here, matrices can be rectangular generally with \\(m\\) rows and \\(n\\) columns called an \\(m\\) by \\(n\\) matrix.

We can then define the equation as the **matrix form** \\(Ax = b\\)

\\[\text { Matrix form } A x=b \quad\left[\begin{array}{ccc}{2} & {1} & {1} \\\ {4} & {-6} & {0} \\\ {-2} & {7} & {2}\end{array}\right]\left[\begin{array}{c}{u} \\\ {v} \\\ {w}\end{array}\right]=\left[\begin{array}{c}{5} \\\ {-2} \\\ {9}\end{array}\right]\\].


### Matrix Operations {#matrix-operations}


#### Matrix Addition {#matrix-addition}

This is straightforward. We add each coefficient of the lhs to the corresponding coefficient in the rhs.

\begin{equation}
\left[\begin{array}{cc}
   {2} & {1} \\\\
   {3} & {0} \\\\
   {0} & {4}
\end{array}\right]
+ \left[\begin{array}{cc}
   {1} & {2} \\\\
   {-3} & {1} \\\\
   {1} & {2}
\end{array}\right]
= \left[\begin{array}{ll}
   {3} & {3} \\\\
   {0} & {1} \\\\
   {1} & {6}
\end{array}\right]
\end{equation}


#### Matrix Product {#matrix-product}

The first straightforward product is the scalar product. This is straightforward and follows from the definition of addition

\\[2\Amat = \Amat + \Amat; \\{\Amat \in \mathcal{R}^{m \times n}\\}\\]

We can also define a product between two matrices \\(\Amat: n \times m\\) and \\(\Bmat: m \times k\\).

\begin{align\*}
\left[\begin{array}{ccc}
  {A\_{11}} & {A\_{12}} & {A\_{13}} \\\\
  {A\_{21}} & {A\_{22}} & {A\_{23}}
\end{array}\right]
\times \left[\begin{array}{cc}
  {B\_{11}} & {B\_{12}} \\\\
  {B\_{21}} & {B\_{22}} \\\\
  {B\_{31}} & {B\_{32}}
\end{array}\right]
&= \left[\begin{array}{ll}
  {\sum\_{i=1}^3 A\_{1i} B\_{i1}} & {\sum\_{i=1}^3 A\_{1i} B\_{i2}} \\\\
  {\sum\_{i=1}^3 A\_{2i} B\_{i1}} & {\sum\_{i=1}^3 A\_{2i} B\_{i2}}
\end{array}\right]
\end{align\*}


##### Hadamard Product {#hadamard-product}

The Hadamard product is often used in machine learning. It is quite simply the element-wise produce between two matrices: \\(\Amat, \Bmat: n \times m\\).

\begin{align\*}
\begin{bmatrix}
  {A\_{11}} & {A\_{12}} \\\\
  {A\_{21}} & {A\_{22}} \\\\
  {A\_{31}} & {A\_{32}}
\end{bmatrix}
\hadamard \begin{bmatrix}
  {B\_{11}} & {B\_{12}} \\\\
  {B\_{21}} & {B\_{22}} \\\\
  {B\_{31}} & {B\_{32}}
\end{bmatrix}
= \begin{bmatrix}
  {A\_{11}B\_{11}} & {A\_{12}B\_{12}} \\\\
  {A\_{21}B\_{21}} & {A\_{22}B\_{22}} \\\\
  {A\_{31}B\_{31}} & {A\_{32}B\_{32}}
\end{bmatrix}
\end{align\*}

<div class="instance">

\begin{bmatrix}
  {2} & {1} \\\\
  {3} & {0} \\\\
  {0} & {4}
\end{bmatrix}

\hadamard \begin{bmatrix}
  {1} &amp; {2} <br />
  {-3} &amp; {1} <br />
  {1} &amp; {2}
\end{bmatrix}
&amp;= \begin{bmatrix}
  {2} &amp; {2} <br />
  {-9} &amp; {0} <br />
  {0} &amp; {8}
\end{bmatrix}
\end{align\*}

</div>


##### Kronecker Product {#kronecker-product}


#### Matrix Transpose {#matrix-transpose}

Transpose mirrors a matrix along its diagonal starting from the top left corner.
\\[[\Amat^\trans]\_{ji} = \Amat\_{ij}\\].


##### Conjugate Transpose {#conjugate-transpose}

The conjugate transpose of a matrix is defined by

\\[
\left(\Amat^H\right)\_{ij} = \left(\overbar{\Amat}\_{ji}\right)
\\]


#### Matrix Inverse {#matrix-inverse}

The inverse of a matrix follows from the inverse of a scalar (i.e. \\(\alpha \alpha^\inv = 1\\)). For a matrix we instead want the product of a matrix and its inverse to be the identity matrix:

\\[\Amat\Amat^\inv = \eye\\]

The inverse for a square matrix exists iff its determinant is not zero \\(\text{det}(\Amat) = |\Amat| \neq 0\\). If this condition is met, we can calculate the inverse using the adjugate

\\[\Amat = \frac{1}{|\Amat|} \text{adj}(\Amat)\\].

See below for the adjugate of a matrix.


##### Moore-penrose Inverse {#moore-penrose-inverse}


#### Matrix Trace {#matrix-trace}

The trace of a matrix is the sum of arguments on the main diagonal.

\\[\text{tr}(\Amat) = \sum\_{i=1}^n a\_{ii}\\]

**Properties:**

-   \\(\text{tr}(\Amat + \Bmat) = \text{tr}(\Amat) + \text{tr}(\Bmat)\\)
-   \\(\text{tr}(\Amat) = \text{tr}(\Amat^\trans)\\)
-   \\(\text{tr}(\Amat^{\trans} \Bmat)
           = \text{tr}(\Amat \Bmat^\trans)
           = \text{tr}(\Bmat^{\top} \Amat)
           = \text{tr}(\Bmat \Amat^{\top})
           =\sum\_{i, j} \Amat\_{i j} \Bmat\_{i j}\\)


#### <span class="org-todo todo TODO">TODO</span> Matrix Adjugate {#matrix-adjugate}

The adjugate of a matrix is the transpose of the cofactor matrix. The cofactor matrix is


### Matrix Definiteness {#matrix-definiteness}

A matrix is positive (or negative) definite if all its eigen values are \\(>0\\) (or \\(<0\\)). Another way to say this is a matrix is positive definite if \\(\xvec^\trans \Mmat  \xvec > 0\\) for all \\(x\in\reals\\).

A matrix is semi-definite if its eigen values can be 0, or \\(\xvec^\trans \Mmat \xvec \ge 0\\).


### Matrix Factorizations {#matrix-factorizations}

A Matrix factorization or decomposition is a factorization of a [matrix](#matrices) into a set of matrix products.


### Diagonalization of a Matrix {#diagonalization-of-a-matrix}


### Symmetric matrices {#symmetric-matrices}


### Rank {#rank}


### Special types of matrices {#special-types-of-matrices}


#### Normal Matrix {#normal-matrix}

A Normal matrix is a complex square matrix which commutes with its [Conjugate Transpose](#matrix-transpose).

\\[\Amat \Amat^\* = \Amat^\* \Amat\\]


#### Diagonal Matrix {#diagonal-matrix}

A diagonal matrix is a matrix which only has elements on its diagonal (starting in the top left corner) and the other elements are zero. A rectangular diagonal matrix is the same.

**Some examples:**

\begin{bmatrix}
1& 0& 0 \\\\
0& 2& 0 \\\\
0& 0& 3.4
\end{bmatrix}

\begin{bmatrix}
1& 0 & 0 & 0 \\\\
0& 21& 0 & 0 \\\\
0& 0 & 32& 0 \\\\
\end{bmatrix}


#### Triangle Matrix {#triangle-matrix}

If all entries of \\(\Amat\\) below the main diagonal are zero, \\(\Amat\\) is called an **upper triangular matrix**. Similarly, if all the entries above the diagonal are zero, the matrix is called **lower triangular matrix**.


#### Unitary Matrix {#unitary-matrix}

A complex square matrix is **unitary** if its [conjugate transpose](#matrix-transpose) is also its [inverse](#matrix-inverse).

\\[ \Umat^\* \Umat = \Umat\Umat^\* = \Umat \Umat^\inv = \Imat \\]

If the matrix \\(\Umat\\) is a real square matrix than it is **orthogonal** if
\\[ \Umat \Umat^\transpose = \Umat^\transpose \Umat = \Umat^\inv \Umat = \identity \\]


#### Tridiagonal Matrix {#tridiagonal-matrix}


#### Block Matrix {#block-matrix}


#### Sparse Matrix {#sparse-matrix}


#### Hessenberg Matrix {#hessenberg-matrix}


#### Hessian Matrix {#hessian-matrix}


#### Vandermonde Matrix {#vandermonde-matrix}


#### Stochastic Matrix {#stochastic-matrix}


#### Hankel Matrix {#hankel-matrix}


#### (0,1) Matrix {#0-1--matrix}


## Determinant {#determinant}

There are four main uses for the determinant of a [Matrix](#matrices) defined by a series of equations.

1.  They test for invertibility. If the determinant of A is zero, then A is singular. If the determinant is non-zero than the matrix can be inverted, meaning there is at least one solution to the set of equations.
2.  The determinant of a matrix is the volume of a box in n-dimensional space. The edges of the box come from the rows of the matrix (or the matrix inferred from the equations). We can define another box with the columns of the matrix, which would result in a box with the same volume.
3.  The determinant gives a formula for each pivot, and we can predict when a pivot entry will be zero (requiring a row exchange in elimination).
4.  The determinant measures the dependence of \\(\mathbf{A}^{-1} \mathbf{b}\\) on each element of \\(\mathbf{b}\\). If one parameter is changed in an experiment, or one observation is corrected, the "influence coefficient" in \\(\mathbf{A}^{-1}\\) is a ratio of determinants


### Properties {#properties}

1.  The determinant of the identity matrix is
    \\[\det\mathbf{I} = 1\\]
2.  The determinant changes sign when (any) two rows are exchanged

    \\[\text{det} \left(\begin{array}{cc}
            c & d \\\\
            a & b
            \end{array} \right) = \left|\begin{array}{cc}
            c & d \\\\
            a & b
            \end{array} \right| = -\det\left(\begin{matrix}
            a & b \\\\
            c & d \end{matrix}\right)\\]

3.  The determinant depends linearly on the first row.
4.  If two rows of \\(\mathbf{A}\\) are equal, then \\(\det\mathbf{A} = 0\\).
5.  Subtracting a multiple of one row from another row leaves the same determinant.
6.  If \\(\mathbf{A}\\) has a row of zeros, then \\(\det\mathbf{A} = 0\\).
7.  If \\(\mathbf{A}\\) is triangular then the determinant is the product \\(\det\mathbf{A} = \prod\_{i=1}^n \mathbf{A}\_{ii}\\).
8.  If \\(\mathbf{A}\\) is singular than the determinant is zero.
9.  The determinant of \\(\mathbf{A}\mathbf{B}\\) is the product of \\(\det\mathbf{A} \times \det\mathbf{B}\\).
10. The transpose \\(\mathbf{A}^\top\\) has the same determinant as \\(\mathbf{A}\\).


### Calculating the Determinant {#calculating-the-determinant}

First for a two by two matrix:

\\[ \left |\begin{array}{cc}
  a & b \\\\
  c & d
  \end{array}\right| = ad - bc\\]

Then a three by three matrix:

\\[ \left |\begin{array}{ccc}
  a & b & c\\\\
  d & e & f\\\\
  g & h & i =
  \end{array}\right| =a \cdot\left|\begin{array}{ll}
e & f \\\\
h & i
\end{array}\right|-b \cdot\left|\begin{array}{ll}
d & f \\\\
g & i
\end{array}\right|+c \cdot\left|\begin{array}{ll}
d & e \\\\
g & h
\end{array}\right|\\]
