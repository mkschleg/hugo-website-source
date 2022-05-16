+++
title = "Determinant"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:16-06:00
slug = "determinant"
draft = false
notetype = "note"
+++

tags
: [Linear Algebra]({{<relref "linear_algebra.md#" >}}), [Math]({{<relref "math.md#" >}})


## Uses {#uses}

There are four main uses for the determinant of a [Matrix]({{<relref "matrix.md#" >}}) defined by a series of equations.

1.  They test for invertibility. If the determinant of A is zero, then A is singular. If the determinant is non-zero than the matrix can be inverted, meaning there is at least one solution to the set of equations.
2.  The determinant of a matrix is the volume of a box in n-dimensional space. The edges of the box come from the rows of the matrix (or the matrix inferred from the equations). We can define another box with the columns of the matrix, which would result in a box with the same volume.
3.  The determinant gives a formula for each pivot, and we can predict when a pivot entry will be zero (requiring a row exchange in elimination).
4.  The determinant measures the dependence of \\(\mathbf{A}^{-1} \mathbf{b}\\) on each element of \\(\mathbf{b}\\). If one parameter is changed in an experiment, or one observation is corrected, the "influence coefficient" in \\(\mathbf{A}^{-1}\\) is a ratio of determinants


## Properties {#properties}

1.  The determinant of the identity matrix is
    \\[\det\mathbf{I} = 1\\]
2.  The determinant changes sign when (any) two rows are exchanged

    \\[\text{det} \left(\begin{array}{cc}
            c & d \\\\\\
            a & b
            \end{array} \right) = \left|\begin{array}{cc}
            c & d \\\\\\
            a & b
            \end{array} \right| = -\det\left(\begin{matrix}
            a & b \\\\\\
            c & d \end{matrix}\right)\\]

3.  The determinant depends linearly on the first row.
4.  If two rows of \\(\mathbf{A}\\) are equal, then \\(\det\mathbf{A} = 0\\).
5.  Subtracting a multiple of one row from another row leaves the same determinant.
6.  If \\(\mathbf{A}\\) has a row of zeros, then \\(\det\mathbf{A} = 0\\).
7.  If \\(\mathbf{A}\\) is triangular then the determinant is the product \\(\det\mathbf{A} = \prod\_{i=1}^n \mathbf{A}\_{ii}\\).
8.  If \\(\mathbf{A}\\) is singular than the determinant is zero.
9.  The determinant of \\(\mathbf{A}\mathbf{B}\\) is the product of \\(\det\mathbf{A} \times \det\mathbf{B}\\).
10. The transpose \\(\mathbf{A}^\top\\) has the same determinant as \\(\mathbf{A}\\).


## Calculating the Determinant {#calculating-the-determinant}

First for a two by two matrix:

\\[ \left |\begin{array}{cc}
  a & b \\\\\\
  c & d
  \end{array}\right| = ad - bc\\]

Then a three by three matrix:

\\[ \left |\begin{array}{ccc}
  a & b & c\\\\\\
  d & e & f\\\\\\
  g & h & i =
  \end{array}\right| =a \cdot\left|\begin{array}{ll}
e & f \\\\\\
h & i
\end{array}\right|-b \cdot\left|\begin{array}{ll}
d & f \\\\\\
g & i
\end{array}\right|+c \cdot\left|\begin{array}{ll}
d & e \\\\\\
g & h
\end{array}\right|\\]
