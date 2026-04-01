Title: Tannakian Reconstruction
Date: 2016-02-28 13:37
Tags: algebra, representation theory
Slug: tannakian
Status: published
original_url: 2016/02/28/tannakian-reconstruction/

These notes are from the February 23, 2016 lecture of [18.757](http://www-math.mit.edu/~laurajoy/rep.html),
_Representations of Lie Algebras_, taught by Laura Rider.

Fix a field $k$ and let $G$ be a finite group.
In this post we will show that one can reconstruct the group $G$ from the
monoidal category of $k[G]$-modules (i.e. its $G$-representations).

## 1. Hopf algebras

We won't do anything with Hopf algebras _per se_, but it will be convenient to have the language.

Recall that an associative $k$-algebra is a $k$-vector space $A$ equipped with a
map $m : A \otimes A \rightarrow A$ and $i : k \hookrightarrow A$ (unit), satisfying some certain axioms.

Then a **$k$-coalgebra** is a map
$$\Delta : A \rightarrow A \otimes A \qquad \varepsilon : A \rightarrow k$$
called comultiplication and counit respectively, which satisfy the dual axioms.
See <https://en.wikipedia.org/wiki/Coalgebra>.

Now a **Hopf algebra** $A$ is a bialgebra $A$ over $k$ plus a so-called **antipode** $S : A \rightarrow A$.
We require that the diagram
![Hopf algebra diagram.]({static}/images/rep-tan-1.png)
commutes.

Given a Hopf algebra $A$ **group-like** element in $A$ is an element of
$$G = \left\{ x \in A \mid \Delta(x) = x \otimes x \right\}.$$

> **Exercise 1.** Show that $G$ is a group with multiplication $m$ and inversion $S$.

Now the example

> **Example 2** **(Group algebra is Hopf algebra)**
>
> The group algebra $k[G]$ is a Hopf algebra with
>
> - $m$, $i$ as expected.
> - $\varepsilon$ the counit is the trivial representation.
> - $\Delta$ comes form $g \mapsto g \otimes g$ extended linearly.
> - $S$ takes $g \mapsto g^{-1}$ extended linearly.

> **Theorem 3.** The group-like elements are precisely the basis elements $1_k \cdot g \in k[g]$.

_Proof:_ Assume $V = \sum_{g \in G} a_g g$ is grouplike. Then by assumption we should have
$$\sum_{g \in G} a_g (g \otimes g) = \Delta(v) = \sum_{g \in G} \sum_{h \in G} a_ga_h (g \otimes h).$$
Comparing each coefficient, we get that
$$a_ga_h = \begin{cases} a_g & g = h \\ 0 & \text{otherwise}. \end{cases}$$
This can only occur if some $a_g$ is $1$ and the remaining coefficients are all zero. $\Box$

## 2. Monoidal functors

Recall that **monoidal category** (or tensor category) is a category
$\mathscr C$ equipped with a functor
$\otimes : \mathscr C \times \mathscr C \rightarrow \mathscr C$ which has an
identity $I$ and satisfies some certain coherence conditions.
For example, for any $A,B,C \in \mathscr C$ we should have a natural isomorphism
$$A \otimes (B \otimes C) \xrightarrow{a_{A,B,C}} (A \otimes B) \otimes C.$$
The generic example is of course suggested by the notation: vector spaces over $k$, abelian groups,
or more generally modules/algebras over a ring $R$.

Now take two monoidal categories $(\mathscr C, \otimes_\mathscr C)$ and $(\mathscr D, \otimes_\mathscr D)$.
Then a **monoidal functor** $F : \mathscr C \rightarrow \mathscr D$ is a functor
for which we additionally need to select an isomorphism
$$F(A \otimes B) \xrightarrow{t_{A,B}} F(A) \otimes F(B).$$
We then require that the diagram
![Monoidal functor commutative diagram.]({static}/images/rep-tan-2.png)
commutes, plus some additional compatibility conditions with the identities of
the $\otimes$'s (see [Wikipedia](https://en.wikipedia.org/wiki/Monoidal_functor#Definition) for the list).

We also have a notion of a natural transformation of two functors $t : F \rightarrow G$;
this is just making the squares
![Natural transformation commutative diagram.]({static}/images/rep-tan-3.png)
commute. Now, suppose $F : \mathscr C \rightarrow \mathscr C$ is a monoidal functor.
Then an **automorphism** of $F$ is a natural transformation $t : F \rightarrow F$ which is invertible, i.e.
a natural isomorphism.

## 3. Application to $k[G]$

With this language, we now reach the main point of the post.
Consider the category of $k[G]$ modules endowed with the monoidal $\otimes$
(which is just the tensor over $k$, with the usual group representation).
We want to reconstruct $G$ from this category.

Let $U$ be the forgetful functor
$$U : \mathsf{Mod}_{k[G]} \rightarrow \mathsf{Vect}_k.$$
It's easy to see this is in fact an monoidal functor.
Now let $\operatorname{Aut}^{\otimes}(U)$ be the set of monoidal automorphisms of $U$.

The key claim is the following:

> **Theorem 4** **($G$ is isomorphic to $\operatorname{Aut}^\otimes(U)$)**
>
> Consider the map
> $$i : G \rightarrow \operatorname{Aut}^\otimes(U) \quad\text{by}\quad g \mapsto T^g.$$
> Here, the natural transformation $T^g$ is defined by the components
> $$T^g_{(V,\phi)} : (V, \phi) \rightarrow U(V, \phi) = V \quad\text{by}\quad v \mapsto \phi(g) v.$$
> Then $i$ is an isomorphism of groups.

In particular, using only $\otimes$ structure this exhibits an isomorphism
$G \cong \operatorname{Aut}^\otimes(U)$.
Consequently this solves the problem proposed at the beginning of the lecture.

_Proof:_ It's easy to see $i$ is a group homomorphism.

To see it's injective, we show $1_G \neq g \in G$ gives $T^g$ isn't the identity automorphism. i.e.
we need to find some representation for which $g$ acts nontrivially on $V$.
Now just take the regular representation, which is faithful!

The hard part is showing that it's surjective. For this we want to reduce it to the regular representation.

> **Lemma 5.** Any $T \in \operatorname{Aut}^\otimes(U)$ is completely determined by
> $T_{k[G]}(1_{k[G]}) \in k[G]$.

_Proof:_ Let $(V, \phi)$ be a representation of $G$.
Then for all $v \in V$, we have a unique morphism of representations
$$f_v : k[G] \rightarrow (V, \phi) \quad\text{by}\quad 1_{k[G]} \mapsto v.$$
If we apply the forgetful functor to this, we have a diagram
![Forgetful functor applied.]({static}/images/rep-tan-4.png)

$\Box$

Next, we claim

> **Lemma 6.** $T_{k[G]}(1_{k[G]})$ is a grouplike element of $k[G]$.

_Proof:_ Draw the diagram
![Proof of Lemma 6.]({static}/images/rep-tan-51.png)
and note that it implies
$$\Delta(T_{k[G]}(1_{k[G]})) = T_{k[G]}(1_{k[G]}) \otimes T_{k[G]}(1_{k[G]}).$$
$\Box$

This implies surjectivity, by our earlier observation that grouplike elements in
$k[G]$ are exactly the elements of $G$. $\Box$
