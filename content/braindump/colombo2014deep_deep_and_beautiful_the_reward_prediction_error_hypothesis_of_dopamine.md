+++
title = "colombo2014deep: Deep and beautiful. The reward prediction error hypothesis of dopamine"
author = ["Matthew Schlegel"]
lastmod = 2025-02-21T10:25:58-07:00
slug = "colombo2014deep"
draft = false
notetype = "paper"
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
: [Reinforcement Learning in the Brain]({{< relref "reinforcement_learning_in_the_brain.md" >}}),

source
: [link](https://pdf.sciencedirectassets.com/271970/1-s2.0-S1369848613X0007X/1-s2.0-S1369848613001313/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCICe0AjtWNBeNCarhxKbn07rR7HaATiRZj1un%2FG%2BWfjUkAiB2N%2FT6v5BImg0DQ8BjSIXzZucxxulosbGzXGSUA8SD%2ByqyBQh%2BEAUaDDA1OTAwMzU0Njg2NSIMs9yTcbRQLrwUBFcLKo8Fjj73Jk9RrCT436%2B1W49oo0cHFiSVINhkbnG%2FNkLA49m1Yv0F87lzl9TnuSUkX27yUMTHerdE332FhR0OVEfNkZqlaNVdIZf0Tzf5aq7qpbwGL747JK9G939et67V10av7EVOl2O7jX%2BRwFrg%2F%2F7XppOr72ubwHiz4HAQQagso9n5FRV7rwFhmZ%2FezQF7gOmO%2FRaNgocLwcrC7DBCJeDrZZcubEDwDGbS3nQNG%2B%2B6eksJLOhwgBBmhMliZbBjC0SznQGp3Vs%2BS%2FR1KH0X6gj6G4H%2FQoLWhe6J1km%2Br4OLhjHdg5uPGio4%2FIUM1KeLOlpLoVsjAfWDHhAhbby08BHjiC6DU1QsC52faq%2BNsd5WL1G54Fm33LchID8nho4lwGPzZhOQBAAlnQLcYr%2FPpvXDfoYnoH3CfrD8aYSicwNtVmj4Ab5fCTyggriPiNJ7V19tid%2BRjid6b4JRbloC4Ajp5tupVq%2FiwWYWt19L9ACGmuHVlqLq4McAuFMcQFyKragDpXY7DkSYsu68Vu9g%2Bb%2FBgmABweEL%2BeTfHNkoMoDBtLO39iKitqCEf4AbCUGPxqg4n83jNMyxnkJq0ViZFsgBUBJBDaVIGaF70oSzfj%2FcgUbe6UphECtqH5zgyTTVUvigyiBYC8hxtb9Y998hJZbsCqbIza%2By8LU2C4XcL%2B9jUOYEAqDcLP1%2B632xbWzu0CGmQvskQ1Yh6BzAbPjUiNBssV%2F91lAxnkWzbIMXd5nLMahXe1k6%2FdPgUS5y3QB2NMAhOWyka8zfk4Uv%2Fzy8ehpZnJgj6IzQq6J3RN4pGP2aOUEVac%2FgZHACyfwGUkOMHLzqXRfj%2FoHXgdF9efJzgAt15OdrcxIFq3i%2FpqRwvxyinjCFiOOgBjqyAav3p5A2BUFAaLh5xTXCc7qd%2FjV92DA6TEqG%2Fmr2AqCSNDAD0n%2FmQyDCXBulG63L5XcnHMHUe%2Fm5J3OHI91UTl98rdJt2%2F0pw7n6l%2BFdwJ%2BuUSFKkecnp%2FJJDVjAyhh4c9ZY2yWoseSnFhRSm9XfbvVHeM0%2BKySJvWbppeM%2Fs46sjBJ5dKW9vItTYiKXgBL4EP228z1FReoq6alxvbFbMXMnervRFgEZ8r%2B1p9TXsiI3INY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230320T205956Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYU677YGHR%2F20230320%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=930660c4cde5cfa54b6285deab4d5d5d9c4ef28c7053cd320e92d8a0aa4c8616&hash=2ea49de6437182a640ae64cfa00d804bff4fa2cf6d46ffefba1833fbf828b883&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1369848613001313&tid=spdf-7747791b-1fa5-46cd-ad17-04312fd5109f&sid=cc5c90908931394a8a093a7-5ab0069aaf1dgxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=050252000c5f0056010c&rr=7ab0e1bb48f6c365&cc=ca)

authors
: Colombo, M.

year
: 2014


## References {#references}



<style>.csl-entry{text-indent: -1.5em; margin-left: 1.5em;}</style><div class="csl-bib-body">
</div>
