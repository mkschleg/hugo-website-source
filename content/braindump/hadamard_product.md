+++
title = "Hadamard product"
author = ["Matthew Schlegel"]
lastmod = 2022-11-08T14:19:51-07:00
slug = "hadamard_product"
draft = false
notetype = "note"
+++

tags
: [Linear Algebra]({{< relref "linear_algebra.md" >}})

This is an element wise product between two vectors or [Matrices]({{< relref "linear_algebra.md#matrices" >}}).

It is quite simply the element-wise produce between two matrices: \\(\mathcal{A}, \mathcal{B}: n \times m\\).

\begin{align\*}
\left[\begin{array}{cc}
  {A\_{11}} & {A\_{12}} \\\\
  {A\_{21}} & {A\_{22}} \\\\
  {A\_{31}} & {A\_{32}}
\end{array}\right]
\odot \left[\begin{array}{cc}
  {B\_{11}} & {B\_{12}} \\\\
  {B\_{21}} & {B\_{22}} \\\\
  {B\_{31}} & {B\_{32}}
\end{array}\right]
&= \left[\begin{array}{ll}
  {A\_{11}B\_{11}} & {A\_{12}B\_{12}} \\\\
  {A\_{21}B\_{21}} & {A\_{22}B\_{22}} \\\\
  {A\_{31}B\_{31}} & {A\_{32}B\_{32}}
\end{array}\right] \\\\
\left[\begin{array}{cc}
  {2} & {1} \\\\
  {3} & {0} \\\\
  {0} & {4}
\end{array}\right]
\odot \left[\begin{array}{cc}
  {1} & {2} \\\\
  {-3} & {1} \\\\
  {1} & {2}
\end{array}\right]
&= \left[\begin{array}{ll}
  {2} & {2} \\\\
  {-9} & {0} \\\\
  {0} & {8}
\end{array}\right]
\end{align\*}
