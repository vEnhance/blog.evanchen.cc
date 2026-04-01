Title: Cardinals
Date: 2015-11-16 13:37
Tags: set theory
Slug: cardinals
Status: published
original_url: 2015/11/16/cardinals/

(Standard post on cardinals, as a prerequisite for forthcoming theory model post.)

An ordinal measures a total ordering. However, it does not do a fantastic job at measuring size.
For example, there is a bijection between the elements of $\omega$ and $\omega+1$:

$$
\begin{array}{rccccccc}
  \omega+1 = & \{ & \omega & 0 & 1 & 2 & \dots & \} \\
  \omega = & \{ & 0 & 1 & 2 & 3 & \dots & \}.
\end{array}
$$

In fact, as you likely already know, there is even a bijection between $\omega$ and $\omega^2$:

$$
\begin{array}{l|cccccc}
  + & 0 & 1 & 2 & 3 & 4 & \dots \\ \hline
  0 & 0 & 1 & 3 & 6 & 10 & \dots \\
  \omega & 2 & 4 & 7 & 11 & \dots & \\
  \omega \cdot 2 & 5 & 8 & 12 & \dots & & \\
  \omega \cdot 3 & 9 & 13 & \dots & & & \\
  \omega \cdot 4 & 14 & \dots & & & &
\end{array}
$$

So ordinals do not do a good job of keeping track of size.
For this, we turn to the notion of a cardinal number.

## 1. Equinumerous Sets and Cardinals

> **Definition 1.** Two sets $A$ and $B$ are **equinumerous**, written $A \approx B$,
> if there is a bijection between them.

<p></p>

> **Definition 2.** A **cardinal** is an ordinal $\kappa$ such that for no
> $\alpha < \kappa$ do we have $\alpha \approx \kappa$.

<p></p>

> **Example 3 (Examples of Cardinals).** Every finite number is a cardinal. Moreover, $\omega$ is a cardinal.
> However, $\omega+1$, $\omega^2$, $\omega^{2015}$ are not, because they are countable.

<p></p>

> **Example 4 ($\omega^\omega$ is Countable).** Even $\omega^\omega$ is not a cardinal,
> since it is a countable union
>
> $$\omega^\omega = \bigcup_n \omega^n$$
>
> and each $\omega^n$ is countable.

<p></p>

> **Question 5.** Why must an infinite cardinal be a limit ordinal?

<p></p>

> **Remark 6.** There is something fishy about the definition of a cardinal:
> it relies on an _external_ function $f$.
> That is, to verify $\kappa$ is a cardinal I can't just look at $\kappa$ itself;
> I need to examine the entire universe $V$ to make sure there does not exist a
> bijection $f : \kappa \rightarrow \alpha$ for $\alpha < \kappa$.
> For now this is no issue, but later in model theory this will lead to some highly counterintuitive behavior.

## 2. Cardinalities

Now that we have defined a cardinal, we can discuss the size of a set by linking it to a cardinal.

> **Definition 7.** The **cardinality** of a set $X$ is the _least_ ordinal
> $\kappa$ such that $X \approx \kappa$. We denote it by $\left\lvert X \right\rvert$.

<p></p>

> **Question 8.** Why must $\left\lvert X \right\rvert$ be a cardinal?

<p></p>

> **Remark 9.** One needs the Well-Ordering Theorem (equivalently,
> Choice) in order to establish that such an ordinal $\kappa$ actually exists.

Since cardinals are ordinals, it makes sense to ask whether $\kappa_1 \le \kappa_2$, and so on.
Our usual intuition works well here.

> **Proposition 10 (Restatement of Cardinality Properties).** Let $X$ and $Y$ be sets.
>
> 1.  $X \approx Y$ if and only $\left\lvert X \right\rvert = \left\lvert Y \right\rvert$,
>     if and only if there is a bijection between $X$ and $Y$.
> 2.  $\left\lvert X \right\rvert \le \left\lvert Y \right\rvert$ if and only if
>     there is an injective map $X \hookrightarrow Y$.

<p></p>

> **Question 11.** Prove this.

## 3. Aleph Numbers

(Prototypical example for this section: $\aleph_0$ is $\omega$, and $\aleph_1$ is the first uncountable.)

First, let us check that cardinals can get arbitrarily large:

> **Proposition 12.** We have $\left\lvert X \right\rvert < \left\lvert \mathcal P(X) \right\rvert$ for every set
> $X$.

_Proof:_ There is an injective map $X \hookrightarrow \mathcal P(X)$ but there
is no injective map $\mathcal P(X) \hookrightarrow X$ by Cantor's diagonal argument. $\Box$

Thus we can define:

> **Definition 13.** For a cardinal $\kappa$, we define $\kappa^+$ to be the least cardinal above $\kappa$,
> called the **successor cardinal**.

This $\kappa^+$ exists and has $\kappa^+ \le \left\lvert \mathcal P(\kappa) \right\rvert$.

Next, we claim that:

> **Exercise 14.** Show that if $A$ is a set of cardinals, then $\cup A$ is a cardinal.

Thus by transfinite induction we obtain that:

> **Definition 15.** For any $\alpha \in \mathrm{On}$, we define the **aleph numbers** as
>
> $$
> \begin{aligned}
>   \aleph_0 &= \omega \\
>   \aleph_{\alpha+1} &= \left( \aleph_\alpha \right)^+ \\
>   \aleph_{\lambda} &= \bigcup_{\alpha < \lambda} \aleph_\alpha.
> \end{aligned}
> $$
>
> Thus we have the following sequence of cardinals:
> $$0 < 1 < 2 < \dots < \aleph_0 < \aleph_1 < \dots < \aleph_\omega < \aleph_{\omega+1} < \dots$$
> By definition, $\aleph_0$ is the cardinality of the natural numbers,
> $\aleph_1$ is the first uncountable ordinal, ….

We claim the aleph numbers constitute all the cardinals:

> **Lemma 16 (Aleph Numbers Constitute All Infinite Cardinals).** If $\kappa$ is
> a cardinal then either $\kappa$ is finite (i.e.
> $\kappa \in \omega$) or $\kappa = \aleph_\alpha$ for some $\alpha \in \mathrm{On}$.

_Proof:_ Assume $\kappa$ is infinite, and take $\alpha$ minimal with $\aleph_\alpha \ge \kappa$.
Suppose for contradiction that we have $\aleph_\alpha > \kappa$.
We may assume $\alpha > 0$, since the case $\alpha = 0$ is trivial.

If $\alpha = \overline{\alpha} + 1$ is a successor, then
$$\aleph_{\overline{\alpha}} < \kappa < \aleph_{\alpha} = (\aleph_{\overline{\alpha}})^+$$
which contradicts the fact the definition of the successor cardinal.
If $\alpha = \lambda$ is a limit ordinal,
then $\aleph_\lambda$ is the supremum $\bigcup_{\gamma < \lambda} \aleph_\gamma$.
So there must be some $\gamma < \lambda$ has $\aleph_\gamma > \kappa$,
which contradicts the minimality of $\alpha$. $\Box$

> **Definition 17.** An infinite cardinal which is not a successor cardinal is called a **limit cardinal**.
> It is exactly those cardinals of the form $\aleph_\lambda$, for $\lambda$ a limit ordinal, plus $\aleph_0$.

## 4. Cardinal Arithmetic

(Prototypical example for this section: $\aleph_0 \cdot \aleph_0 = \aleph_0 + \aleph_0 = \aleph_0$.)

Recall the way we set up ordinal arithmetic.
Note that in particular, $\omega + \omega > \omega$ and $\omega^2 > \omega$.
Since cardinals count size, this property is undesirable, and we want to have

$$
\begin{aligned}
  \aleph_0 + \aleph_0 &= \aleph_0 \\
  \aleph_0 \cdot \aleph_0 &= \aleph_0
\end{aligned}
$$

because $\omega + \omega$ and $\omega \cdot \omega$ are countable.
In the case of cardinals, we simply "ignore order".

The definition of cardinal arithmetic is as expected:

> **Definition 18 (Cardinal Arithmetic).** Given cardinals $\kappa$ and $\mu$, define
>
> $$
> \kappa + \mu \coloneqq \left\lvert \left( \left\{ 0 \right\}
> \times \kappa \right) \cup \left( \left\{ 1 \right\} \times \mu \right) \right\rvert
> $$
>
> and
>
> $$k \cdot \mu \coloneqq \left\lvert \mu \times \kappa \right\rvert .$$

<p></p>

> **Question 19.** Check this agrees with what you learned in pre-school for finite cardinals.

This is a slight abuse of notation since we are using the same symbols as for ordinal arithmetic,
even though the results are different ($\omega \cdot \omega = \omega^2$ but
$\aleph_0 \cdot \aleph_0 = \aleph_0$).
In general, I'll make it abundantly clear whether I am talking about cardinal
arithmetic or ordinal arithmetic.
To help combat this confusion, we use separate symbols for ordinals and cardinals.
Specifically, $\omega$ will always refer to $\{0,1,\dots\}$ viewed as an ordinal;
$\aleph_0$ will always refer to the same set viewed as a cardinal. More generally,

> **Definition 20.** Let $\omega_\alpha = \aleph_\alpha$ viewed as an ordinal.

However, as we've seen already we have that $\aleph_0 \cdot \aleph_0 = \aleph_0$.
In fact, this holds even more generally:

> **Theorem 21 (Infinite Cardinals Squared).** Let $\kappa$ be an infinite cardinal.
> Then $\kappa \cdot \kappa = \kappa$.

_Proof:_ Obviously $\kappa \cdot \kappa \ge \kappa$, so we want to show $\kappa \cdot \kappa \le \kappa$.

The idea is to repeat the same proof that we had for $\aleph_0 \cdot \aleph_0 = \aleph_0$,
so we re-iterate it here. We took the "square" of elements of $\aleph_0$,
and then _re-ordered_ it according to the diagonal:

$$
\begin{array}{l|cccccc}
  & 0 & 1 & 2 & 3 & 4 & \dots \\ \hline
  0 & 0 & 1 & 3 & 6 & 10 & \dots \\
  1 & 2 & 4 & 7 & 11 & \dots & \\
  2 & 5 & 8 & 12 & \dots & & \\
  3 & 9 & 13 & \dots & & & \\
  4 & 14 & \dots & & & &
\end{array}
$$

Let's copy this idea for a general $\kappa$.

We proceed by transfinite induction on $\kappa$. The base case is $\kappa = \aleph_0$, done above.
For the inductive step, first we put the "diagonal" ordering $<_{\text{diag}}$
on $\kappa \times \kappa$ as follows:
for $(\alpha_1, \beta_1)$ and $(\alpha_1, \beta_2)$ in $\kappa \times \kappa$ we
declare $(\alpha_1, \beta_1) <_{\text{diag}} (\alpha_2, \beta_2)$ if

- $\max \left\{ \alpha_1, \beta_1 \right\} < \max \left\{ \alpha_2, \beta_2 \right\}$ (they are on different diagonals),
  or
- $\max \left\{ \alpha_1, \beta_1 \right\} = \max \left\{ \alpha_2, \beta_2 \right\}$ and $\alpha_1 < \alpha_2$
  (same diagonal).

Then $<_{\text{diag}}$ is a well-ordering of $\kappa \times \kappa$,
so we know it is in order-preserving bijection with some ordinal $\gamma$.
Our goal is to show that $\left\lvert \gamma \right\rvert \le \kappa$.
To do so, it suffices to prove that for any $\overline{\gamma} \in \gamma$,
we have $\left\lvert \overline{\gamma} \right\rvert < \kappa$.

Suppose $\overline{\gamma}$ corresponds to the point $(\alpha, \beta) \in \kappa$ under this bijection.
If $\alpha$ and $\beta$ are both finite, then certainly $\overline{\gamma}$ is finite too.
Otherwise, let $\overline{\kappa} = \max \{\alpha, \beta\} < \kappa$;
then the number of points below $\overline{\gamma}$ is at most

$$
\left\lvert \alpha \right\rvert \cdot \left\lvert \beta \right\rvert
  \le \overline{\kappa} \cdot \overline{\kappa} = \overline{\kappa}
$$

by the inductive hypothesis. So
$\left\lvert \overline{\gamma} \right\rvert \le \overline{\kappa} < \kappa$ as desired. $\Box$

From this it follows that cardinal addition and multiplication is really boring:

> **Theorem 22 (Infinite Cardinal Arithmetic is Trivial).** Given cardinals $\kappa$ and $\mu$,
> one of which is infinite, we have
>
> $$\kappa \cdot \mu = \kappa + \mu = \max\left( \kappa, \mu \right).$$

_Proof:_ The point is that both of these are less than the square of the maximum. Writing out the details:

$$
\begin{aligned}
  \max \left( \kappa, \mu \right)
    &\le \kappa + \mu \\
    &\le \kappa \cdot \mu \\
    &\le \max \left( \kappa, \mu \right) \cdot \max \left( \kappa, \mu \right) \\
    &= \max\left( \kappa, \mu \right).
\end{aligned}
$$

$\Box$

## 5. Cardinal Exponentiation

(Prototypical example for this section: $2^\kappa = \left\lvert \mathcal P(\kappa) \right\rvert$.)

> **Definition 23.** Suppose $\kappa$ and $\lambda$ are cardinals. Then
>
> $$\kappa^\lambda \coloneqq \left\lvert \mathscr F(\lambda, \kappa) \right\rvert.$$
>
> Here $\mathscr F(A,B)$ is the set of functions from $A$ to $B$.

As before, we are using the same notation for both cardinal and ordinal arithmetic. Sorry!

In particular, $2^\kappa = \left\lvert \mathcal P(\kappa) \right\rvert > \kappa$,
and so from now on we can use the notation $2^\kappa$ freely.
(Note that this is totally different from ordinal arithmetic;
there we had $2^\omega = \bigcup_{n\in\omega} 2^n = \omega$.
In cardinal arithmetic $2^{\aleph_0} > \aleph_0$.)

I have unfortunately not told you what $2^{\aleph_0}$ equals.
A natural conjecture is that $2^{\aleph_0} = \aleph_1$; this is called the **Continuum Hypothesis**.
It turns out to that this is _undecidable_ -- it is not possible to prove or
disprove this from the $\mathsf{ZFC}$ axioms.

## 6. Cofinality

(Prototypical example for this section: $\aleph_0$, $\aleph_1$, … are all regular,
but $\aleph_\omega$ has cofinality $\omega$.)

> **Definition 24.** Let $\lambda$ be a limit ordinal, and $\alpha$ another ordinal.
> A map $f : \alpha \rightarrow \lambda$ of ordinals is called **cofinal** if
> for every $\overline{\lambda} < \lambda$,
> there is some $\overline{\alpha} \in \alpha$ such that $f(\overline{\alpha}) \ge \overline{\lambda}$.
> In other words, the map reaches arbitrarily high into $\lambda$.

<p></p>

> **Example 25 (Example of a Cofinal Map)**
>
> 1.  The map $\omega \rightarrow \omega^\omega$ by $n \mapsto \omega^n$ is cofinal.
> 2.  For any ordinal $\alpha$, the identity map $\alpha \rightarrow \alpha$ is cofinal.

<p></p>

> **Definition 26.** Let $\lambda$ be a limit ordinal.
> The **cofinality** of $\lambda$, denoted $\text{cof }(\lambda)$,
> is the smallest ordinal $\alpha$ such that there is a cofinal map $\alpha \rightarrow \lambda$.

<p></p>

> **Question 27.** Why must $\alpha$ be an infinite cardinal?

Usually, we are interested in taking the cofinality of a cardinal $\kappa$.

Pictorially, you can imagine standing at the bottom of the universe and looking
up the chain of ordinals to $\kappa$.
You have a machine gun and are firing bullets upwards,
and you want to get arbitrarily high but less than $\kappa$.
The cofinality is then the number of bullets you need to do this.

We now observe that "most" of the time, the cofinality of a cardinal is itself.
Such a cardinal is called **regular**.

> **Example 28 ($\aleph_0$ is Regular).** $\text{cof }(\aleph_0) = \aleph_0$,
> because no finite subset of $\omega$ can reach arbitrarily high.

<p></p>

> **Example 29 ($\aleph_1$ is Regular).** $\text{cof }(\aleph_1) = \aleph_1$.
> Indeed, assume for contradiction that some countable set of ordinals
> $A = \\ \alpha_0, \alpha_1, \dots \\ \subseteq \omega_1$ reaches arbitrarily high inside $\omega_1$.
> Then $\Lambda = \cup A$ is a _countable_ ordinal, because it is a countable union of countable ordinals.
> In other words $\Lambda \in \omega_1$. But $\Lambda$ is an upper bound for $A$, contradiction.

On the other hand, there _are_ cardinals which are not regular;
since these are the "rare" cases we call them **singular**.

> **Example 30 ($\aleph_\omega$ is Not Regular).** Notice that
> $\aleph_0 < \aleph_1 < \aleph_2 < \dots$ reaches arbitrarily high in $\aleph_\omega$,
> despite only having $\aleph_0$ terms. It follows that $\text{cof }(\aleph_\omega) = \aleph_0$.

We now confirm a suspicion you may have:

> **Theorem 31 (Successor Cardinals Are Regular).** If
> $\kappa = \overline{\kappa}^+$ is a successor cardinal, then it is regular.

_Proof:_ We copy the proof that $\aleph_1$ was regular.

Assume for contradiction that for some $\mu \le \overline{\kappa}$,
there are $\mu$ sets reaching arbitrarily high in $\kappa$ as a cardinal.
Observe that each of these sets must have cardinality at most $\overline{\kappa}$.
We take the union of all $\mu$ sets, which gives an ordinal $\Lambda$ serving as an upper bound.

The number of elements in the union is at most
$$\#\text{sets} \cdot \#\text{elms} \le \mu \cdot \overline{\kappa} = \overline{\kappa}$$
and hence $\left\lvert \Lambda \right\rvert \le \overline{\kappa} < \kappa$. $\Box$

## 7. Inaccessible Cardinals

So, what about limit cardinals?
It seems to be that most of them are singular: if $\aleph_\lambda \ne \aleph_0$ is a limit ordinal,
then the sequence $\{\aleph_\alpha\}_{\alpha \in \lambda}$ (of length $\lambda$) is certainly cofinal.

> **Example 32 (Beth Fixed Point).** Consider the monstrous cardinal
>
> $$\kappa = \aleph_{\aleph_{\aleph_{\ddots}}}.$$
>
> This might look frighteningly huge, as $\kappa = \aleph_\kappa$,
> but its cofinality is $\omega$ as it is the limit of the sequence
>
> $$\aleph_0, \aleph_{\aleph_0}, \aleph_{\aleph_{\aleph_0}}, \dots$$
> More generally, one can in fact prove that
> $$\text{cof }(\aleph_\lambda) = \text{cof }(\lambda).$$
> But it is actually conceivable that $\lambda$ is so large that
> $\left\lvert \lambda \right\rvert = \left\lvert \aleph_\lambda \right\rvert$.

A regular limit cardinal other than $\aleph_0$ has a special name: it is **weakly inaccessible**.
Such cardinals are so large that it is impossible to prove or disprove their existence in $\mathsf{ZFC}$.
It is the first of many so-called "large cardinals".

An infinite cardinal $\kappa$ is a strong limit cardinal if
$$\forall \overline{\kappa} < \kappa \quad 2^{\overline{\kappa}} < \kappa$$
for any cardinal $\overline{\kappa}$. For example, $\aleph_0$ is a strong limit cardinal.

> **Question 33.** Why must strong limit cardinals actually be limit cardinals? (This is offensively easy.)

A regular strong limit cardinal other than $\aleph_0$ is called **strongly inaccessible**.

## 8. Exercises

> **Problem 1.** Compute $\left\lvert V_\omega \right\rvert$.

> **Problem 2.** Prove that for any limit ordinal $\alpha$, $\text{cof }(\alpha)$ is a _regular_ cardinal.

> **Problem 3 (Strongly Inaccessible Cardinals).** <span
> id="probstrongly_inaccessible"></span> Show that for any strongly inaccessible $\kappa$,
> we have $\left\lvert V_\kappa \right\rvert = \kappa$.

> **Problem 4 (Konig's Theorem).** Show that
>
> $$\kappa^{\text{cof }(\kappa)} > \kappa$$
>
> for every infinite cardinal $\kappa$.

(This post is a draft of a chapter from my [Napkin project](http://www.mit.edu/~evanchen/napkin.html).)
