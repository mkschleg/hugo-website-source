+++
title = "Matrix"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:28-06:00
slug = "matrix"
draft = false
notetype = "note"
+++

tags
: [Linear Algebra]({{<relref "linear_algebra.md#" >}}), [Math]({{<relref "math.md#" >}})

We star with a set of equations with nine coefficients, three unknowns, and three right-hand sides.

\begin{align\*}
   2u + v + w &= 5 \\\\\\
   4u - 6v &=-2 \\\\\\
   -2u + 7v + 2w &=9
\end{align\*}

We represent the right hand side with a **column vector** (or a 1 by 3 matrix). The unknowns of the system are represented as a column vector as well.

\\[x=\left[\begin{array}{l}{u} \\ {v} \\ {w}\end{array}\right]\\]

We define a square 3 by 3 matrix of the coefficients

\\[A=\left[\begin{array}{ccc}
    {2} & {1} & {1} \\\\\\
    {4} & {-6} & {0} \\\\\\
    {-2} & {7} & {2}
\end{array}\right]\\]

While we present a square matrix here, matrices can be rectangular generally with \\(m\\) rows and \\(n\\) columns called an \\(m\\) by \\(n\\) matrix.

We can then define the equation as the **matrix form** \\(Ax = b\\)

\begin{align\*}
A x &= b \\\\ \left[\begin{array}{ccc}{2} & {1} & {1} \\\\ {4} & {-6} & {0} \\\\ {-2} & {7} & {2}\end{array}\right]\left[\begin{array}{c}{u} \\\\ {v} \\\\ {w}\end{array}\right]&=\left[\begin{array}{c}{5} \\\\ {-2} \\\\ {9}\end{array}\right]
\end{align\*}.


## Operations {#operations}


### Addition {#addition}

This is straightforward. We add each coefficient of the lhs to the corresponding coefficient in the rhs.

 \begin{align\*}
\left[\begin{array}{cc}
    {2} & {1} \\\\\\
    {3} & {0} \\\\\\
    {0} & {4}
 \end{array}\right] +
 \left[\begin{array}{cc}
     {1} & {2} \\\\\\
     {-3} & {1} \\\\\\
     {1} & {2}
  \end{array}\right]
   = \left[\begin{array}{ll}
     {3} & {3} \\\\\\
     {0} & {1} \\\\\\
     {1} & {6}
  \end{array}\right]
 \end{align\*}


### Product {#product}

The first straightforward product is the scalar product. This is straightforward and follows from the definition of addition

\\[2\mathbf{A} = \mathbf{A} + \mathbf{A}; \\{\mathbf{A} \in \mathcal{R}^{m \times n}\\}\\]

We can also define a product between two matrices \\(\mathbf{A}: n \times m\\) and \\(\mathbf{B}: m \times k\\).

\begin{align\*}
\left[\begin{array}{ccc}
  {A\_{11}} & {A\_{12}} & {A\_{13}} \\\\\\
  {A\_{21}} & {A\_{22}} & {A\_{23}}
\end{array}\right]
\times \left[\begin{array}{cc}
  {B\_{11}} & {B\_{12}} \\\\\\
  {B\_{21}} & {B\_{22}} \\\\\\
  {B\_{31}} & {B\_{32}}
\end{array}\right]
&= \left[\begin{array}{ll}
  {\sum\_{i=1}^3 A\_{1i} B\_{i1}} & {\sum\_{i=1}^3 A\_{1i} B\_{i2}} \\\\\\
  {\sum\_{i=1}^3 A\_{2i} B\_{i1}} & {\sum\_{i=1}^3 A\_{2i} B\_{i2}}
\end{array}\right]
\end{align\*}

<!--list-separator-->

-  [Hadamard product]({{<relref "hadamard_product.md#" >}})

    The Hadamard product is often used in machine learning. It is quite simply the element-wise produce between two matrices: \\(\mathcal{A}, \mathcal{B}: n \times m\\).

    \begin{align\*}
    \left[\begin{array}{cc}
      {A\_{11}} & {A\_{12}} \\\\\\
      {A\_{21}} & {A\_{22}} \\\\\\
      {A\_{31}} & {A\_{32}}
    \end{array}\right]
    \odot \left[\begin{array}{cc}
      {B\_{11}} & {B\_{12}} \\\\\\
      {B\_{21}} & {B\_{22}} \\\\\\
      {B\_{31}} & {B\_{32}}
    \end{array}\right]
    &= \left[\begin{array}{ll}
      {A\_{11}B\_{11}} & {A\_{12}B\_{12}} \\\\\\
      {A\_{21}B\_{21}} & {A\_{22}B\_{22}} \\\\\\
      {A\_{31}B\_{31}} & {A\_{32}B\_{32}}
    \end{array}\right] \\\\\\
    \left[\begin{array}{cc}
      {2} & {1} \\\\\\
      {3} & {0} \\\\\\
      {0} & {4}
    \end{array}\right]
    \odot \left[\begin{array}{cc}
      {1} & {2} \\\\\\
      {-3} & {1} \\\\\\
      {1} & {2}
    \end{array}\right]
    &= \left[\begin{array}{ll}
      {2} & {2} \\\\\\
      {-9} & {0} \\\\\\
      {0} & {8}
    \end{array}\right]
    \end{align\*}

<!--list-separator-->

-  Kronecker Product


### Transpose {#transpose}

Transpose mirrors a matrix along its diagonal starting from the top left corner.
\\[[\mathbf{A}^\top]\_{ji} = \mathbf{A}\_{ij}\\].


### Inverse {#inverse}

The inverse of a matrix follows from the inverse of a scalar (i.e. \\(\alpha \alpha^{-1} = 1\\)). For a matrix we instead want the product of a matrix and its inverse to be the identity matrix:

\\[\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}\\]

The inverse for a square matrix exists iff its determinant is not zero \\(\text{det}(\mathbf{A}) = |\mathbf{A}| \neq 0\\). If this condition is met, we can calculate the inverse using the adjugate

\\[\mathbf{A} = \frac{1}{|\mathbf{A}|} \text{adj}(\mathbf{A})\\].

See below for the adjugate of a matrix.

<!--list-separator-->

-  Moore-penrose Inverse


### Trace {#trace}

The trace of a matrix is the sum of arguments on the main diagonal.

\\[\text{tr}(\mathbf{A}) = \sum\_{i=1}^n a\_{ii}\\]

<!--list-separator-->

-  Properties:

    -   \\(\text{tr}(\mathbf{A} + \mathbf{B}) = \text{tr}(\mathbf{A}) + \text{tr}(\mathbf{B})\\)
    -   \\(\text{tr}(\mathbf{A}) = \text{tr}(\mathbf{A}^\top)\\)
    -   \\(\text{tr}(\mathbf{A}^{\top} \mathbf{B})
               = \text{tr}(\mathbf{A} \mathbf{B}^\top)
               = \text{tr}(\mathbf{B}^{\top} \mathbf{A})
               = \text{tr}(\mathbf{B} \mathbf{A}^{\top})
               =\sum\_{i, j} \mathbf{A}\_{i j} \mathbf{B}\_{i j}\\)


### Adjugate {#adjugate}

The adjugate of a matrix is the transpose of the cofactor matrix. The cofactor matrix is
