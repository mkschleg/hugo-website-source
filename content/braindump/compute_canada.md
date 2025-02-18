+++
title = "Compute Canada"
author = ["Matthew Schlegel"]
lastmod = 2022-11-08T14:19:09-07:00
slug = "compute_canada"
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

There are several weird bits about compute canada. This document serves as a note for remembering many of these idiosyncrasies.


## Batching a Job {#batching-a-job}

This will primarily be concerned with tricks for batching a job and the use of \`sbatch\` and \`srun\`.

**IMPORTANT**: If your job fails you will be dinged for the **ENTIRE** resource allocation, not just what you have used. Also if your job finishes early you will still be dinged for the entire allocation! Keep this in mind as you test code (use interactive shells where possible).


### Sbatch {#sbatch}

So sbatch takes a script as argument. There are several nice arguments that can be placed at the top of the script to determine the resource allocation for a specific job.

You run sbatch

```shell
     #!/path/to/shell
     # Number of parallel tasks in your job.
     #SBATCH --ntasks=1
     # Max-Time <d|hh|mm>
     #SBATCH --time=6:00:00
     # Memory per cpu used.
     #SBATCH --mem-per-cpu=1000M
     # Number of cpus per task
     #SBATCH --cpus-per-task=1
     # Resource allocation used by this job.
     #SBATCH --account=def-whitem
```

\`sbatch\` is convenient for allocating a number of large jobs with many small jobs running concurrently, and this is a typical workflow I use. Within the script one can you gnu-parallel to run multiple jobs in parallel. Amazingly sbatch will also pass inline arguments to your script which can be accessed in the standard way for your scripting language. While I typically will use zsh, you can use any scripting language really including but not limited to Python and Julia only needing to specify at the top of the file where the language interpreter/compiler is in the usual shell way (\`#!/path/to/shell/zsh\`).


## Interactive Jobs {#interactive-jobs}

You can use salloc to open an interactive job for testing. This is highly recommended as you can test your code without allocating the full resources you require.

Some caveats:

-   You can only allocate 3 hours of time!
-   Others...

An example of the salloc command is as follows:

\`salloc --time=2:00:0 --cpus-per-task=1 --mem-per-cpu=1000M --account=def-whitem\`


## Cluster Info {#cluster-info}


### Graham {#graham}


### MP2b {#mp2b}


### Beluga {#beluga}

To start julia

```shell
module load nixpkgs/16.09  gcc/7.3.0 julia/1.1.0
```


## Tensorflow + Python3 {#tensorflow-plus-python3}


## Julia {#julia}
