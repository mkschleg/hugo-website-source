+++
title = "Gaussian Elimination"
author = ["Matthew Schlegel"]
lastmod = 2021-09-13T14:17:18-06:00
slug = "gaussian_elimination"
draft = false
notetype = "note"
+++

tags
: [Linear Algebra]({{<relref "linear_algebra.md#" >}}), [Math]({{<relref "math.md#" >}})

Elimination is all about _solving linear equations_ (which is central to linear algebra generally). As an example we have two equations with two unknowns

\begin{align\*}
	1x + 2y = 3 \\\\\\
	4x + 5y = 6
\end{align\*} (from [[id:F614A77A-E9CF-47C7-8C96-5B21D3673D4B][Linear Algebra and its Applications]])

To solve for the unknowns $x$ and $y$ we can use elimination:

1. subtract 4 times the first equation from the second equation (eliminates $x$ from the second equation)

   \\[(4x + 5y) - 4(1x + 2y) = 6 - 4\*3 \hspace{0.3cm} \rightarrow \hspace{0.3cm} -3y=-6 \\]

   From this we know that $y=2$.

2. Back-substitution: We then put in the known $y=2$ into the first equation

   \\[ 1x + 2(2) = 3 \hspace{0.3cm} \rightarrow \hspace{0.3cm} x = -1\\]


This simple example illustrates how useful gaussian elimination can be. We can look at another set of equations to understand how the method extends beyond two equations

\begin{align\*}
2 u+v+w &= 5 \\\\\\
4 u-6 v &= -2 \\\\\\
-2 u+7 v+2 w &= 9
\end{align\*}

The method starts by **substracting multiples of the first equation from the other equations**. The coefficient 2 is the **first pivot**. To find the right multipliers to subtract we take the first pivot and dived it into the numbers in the subsequent numbers underneath.

\begin{align\*}
2 u+v+w &= 5 \\\\\\
-8v - 2w &= -12 \\\\\\
8v + 3w &= 14
\end{align\*}

The next pivot is the first coefficient in the second equation, where we now only consider equations below this to remove the second unknown.

\begin{align\*}
2 u+v+w &= 5 \\\\\\
-8v - 2w &= -12 \\\\\\
1w &= 2
\end{align\*}

The system is then solved from bottom to top through **back-substitution**. The forward elimination produced the pivots 2, -8, 1. It subtracted multiples of each row from the rows beneath to reach a **trangular** system, which is solved in reverse order.

This method is simple and more efficient than its [Determinant]({{<relref "determinant.md#" >}}) counterpart. It is also useful to consider when this simple algorithm will break down. The most obvious case is when we encounter a pivot which is 0. By definition, elimination breaks down and must stop. This can occur when the system is singular or when it is non-singular. If the system is non-signular, than this can be fixed by changing the order of equations and restarting elimination. The singular case is incurable, as there is no solution to be found.
