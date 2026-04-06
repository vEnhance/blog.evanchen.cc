---
title: Algebraic Topology Functors
date: 2016-11-23 13:37
slug: algtop-functor
tags: algebraic topology, category theory, math
original_url: 2016/11/23/algebraic-topology-functors/
status: published
---

This will be old news to anyone who does algebraic topology,
but oddly enough I can't seem to find it all written in one place anywhere,
and in particular I can't find the bit about $\mathsf{hPairTop}$ at all.

In algebraic topology you (for example) associate every topological space $X$ with a group,
like $\pi_1(X, x_0)$ or $H_5(X)$. All of these operations turn out to be _functors_.
This isn't surprising, because as far as I'm concerned the definition of a
functor is "any time you take one type of object and naturally make another object".

The surprise is that these objects also respect homotopy in a nice way;
proving this is a fair amount of the "setup" work in algebraic topology.

## 1. Homology, $H_n : \mathsf{hTop} \rightarrow \mathsf{Grp}$

Note that $H_5$ is a functor
$$H_5 : \mathsf{Top} \rightarrow \mathsf{Grp}$$
i.e. to every space $X$ we can associate a group $H_5(X)$.
(Of course, replace $5$ by integer of your choice.) Recall that:

> **Definition 1.** Two maps $f, g : X \rightarrow Y$ are **homotopy
> equivalent** if there exists a [homotopy](https://en.wikipedia.org/wiki/Homotopy) between them.

Thus for a map we can take its **homotopy class** $[f]$ (the equivalence class under this relationship).
This has the nice property that $[f \circ g] = [f] \circ [g]$ and so on.

> **Definition 2.** Two spaces $X$ and $Y$ are **homotopic** if there exists a
> pair of maps $f : X \rightarrow Y$ and $g : Y \rightarrow X$ such that
> $[f \circ g] = [\mathrm{id}_X]$ and $[g \circ f] = [\mathrm{id}_Y]$.

In light of this, we can define

> **Definition 3.** The category $\mathsf{hTop}$ is defined as follows:
>
> - The objects are topological spaces $X$.
> - The morphisms $X \rightarrow Y$ are _homotopy classes_ of continuous maps $X \rightarrow Y$.

> **Remark 4.** Composition is well-defined since $[f \circ g] = [f] \circ [g]$.
> Two spaces are isomorphic in $\mathsf{hTop}$ if they are homotopic.

> **Remark 5.** As you might guess this "quotient" construction is called a
> [quotient category](https://en.wikipedia.org/wiki/Quotient_category).

Then the big result is that:

> **Theorem 6.** The induced map $f_\sharp = H_n(f)$ of a map
> $f: X \rightarrow Y$ depends only on the homotopy class of $f$. Thus $H_n$ is a functor
> $$H_n : \mathsf{hTop} \rightarrow \mathsf{Grp}.$$

The proof of this is geometric, using the so-called _prism operators_.
In any case, as with all functors we deduce

> **Corollary 7.** $H_n(X) \cong H_n(Y)$ if $X$ and $Y$ are homotopic.

In particular, the _contractable_ spaces are those spaces $X$ which are homotopy equivalent to a point.
In which case, $H_n(X) = 0$ for all $n \ge 1$.

## 2. Relative Homology, $H_n : \mathsf{hPairTop} \rightarrow \mathsf{Grp}$

In fact, we also defined homology groups
$$H_n(X,A)$$
for $A \subseteq X$. We will now show this is functorial too.

> **Definition 8.** Let $\varnothing \neq A \subset X$ and $\varnothing \neq B \subset X$ be subspaces,
> and consider a map $f : X \rightarrow Y$. If $f(A) \subseteq B$ we write
> $$f : (X,A) \rightarrow (Y,B).$$
> We say $f$ is a **map of pairs**, between the pairs $(X,A)$ and $(Y,B)$.

> **Definition 9.** We say that $f,g : (X,A) \rightarrow (Y,B)$ are
> **pair-homotopic** if they are "homotopic through maps of pairs".

More formally, a **pair-homotopy** $f, g : (X,A) \rightarrow (Y,B)$ is a map
$F : [0,1] \times X \rightarrow Y$, which we'll write as $F_t(X)$,
such that $F$ is a homotopy of the maps $f,g : X \rightarrow Y$ and each $F_t$ is itself a map of pairs.

Thus, we naturally arrive at two categories:

- $\mathsf{PairTop}$, the category of _pairs_ of topological spaces, and
- $\mathsf{hPairTop}$, the same category except with maps only equivalent up to homotopy.

> **Definition 10.** As before,
> we say pairs $(X,A)$ and $(Y,B)$ are **pair-homotopy equivalent** if they are
> isomorphic in $\mathsf{hPairTop}$.
> An isomorphism of $\mathsf{hPairTop}$ is a **pair-homotopy equivalence**.

Then, the prism operators now let us derive

> **Theorem 11.** We have a functor
> $$H_n : \mathsf{hPairTop} \rightarrow \mathsf{Grp}.$$
> The usual corollaries apply.

Now, we want an analog of contractable spaces for our pairs: i.e.
pairs of spaces $(X,A)$ such that $H_n(X,A) = 0$ for $n \ge 1$. The correct definition is:

> **Definition 12.** Let $A \subset X$.
> We say that $A$ is a **deformation retract** of $X$ if there is a map of pairs
> $r : (X, A) \rightarrow (A, A)$ which is a pair homotopy equivalence.

> **Example 13** **(Examples of Deformation Retracts)**
>
> 1. If a single point $p$ is a deformation retract of a space $X$, then $X$ is contractable,
>     since the retraction $r : X \rightarrow \{*\}$ (when viewed as a map
>     $X \rightarrow X$) is homotopic to the identity map $\mathrm{id}_X : X \rightarrow X$.
> 2. The punctured disk $D^2 \setminus \{0\}$ deformation retracts onto its boundary $S^1$.
> 3. More generally, $D^{n} \setminus \{0\}$ deformation retracts onto its boundary $S^{n-1}$.
> 4. Similarly, $\mathbb R^n \setminus \{0\}$ deformation retracts onto a sphere $S^{n-1}$.

Of course in this situation we have that
$$H_n(X,A) \cong H_n(A,A) = 0.$$

## 3. Homotopy, $\pi_1 : \mathsf{hTop}_\ast \rightarrow \mathsf{Grp}$

As a special case of the above, we define

> **Definition 14.** The category $\mathsf{Top}_\ast$ is defined as follows:

- The objects are pairs $(X, x_0)$ of spaces $X$ with a distinguished basepoint $x_0$.
  We call these **pointed spaces**.
- The morphisms are maps $f : (X, x_0) \rightarrow (Y, y_0)$, meaning $f$ is continuous and $f(x_0) = y_0$.

Now again we mod out:

> **Definition 15.** Two maps $f , g : (X, x_0) \rightarrow (Y, y_0)$ of
> **pointed spaces** are homotopic if there is a homotopy between them which also fixes the basepoints.
> We can then, in the same way as before, define the quotient category $\mathsf{hTop}_\ast$.

And lo and behold:

> **Theorem 16.** We have a functor
> $$\pi_1 : \mathsf{hTop}_\ast \rightarrow \mathsf{Grp}.$$
> Same corollaries as before.
