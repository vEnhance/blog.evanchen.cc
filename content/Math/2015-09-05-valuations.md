---
title: Some Notes on Valuations
date: 2015-09-05 13:37
slug: valuations
tags: number theory
original_url: 2015/09/05/some-notes-on-valuations/
status: published
---

There are some notes on valuations from the first lecture of Math 223a at Harvard.

## 1. Valuations

Let $k$ be a field.

> **Definition 1.** A **valuation**
> $$\left\lvert - \right\rvert : k \rightarrow \mathbb R_{\ge 0}$$
> is a function obeying the axioms
>
> - $\left\lvert \alpha \right\rvert = 0 \iff \alpha = 0$.
> - $\left\lvert \alpha\beta \right\rvert = \left\lvert \alpha \right\rvert \left\lvert \beta \right\rvert$.
> - Most importantly: there should exist a real constant $C$,
>   such that $\left\lvert 1+\alpha \right\rvert < C$ whenever $\left\lvert \alpha \right\rvert \le 1$.

The third property is the interesting one.
Note in particular it can be rewritten as
$\left\lvert a+b \right\rvert < C\max \{ \left\lvert a \right\rvert, \left\lvert b \right\rvert \}$.

Note that we can recover $\left\lvert 1 \right\rvert = \left\lvert 1 \right\rvert \left\lvert 1 \right\rvert \implies
\left\lvert 1 \right\rvert = 1$ immediately.

> **Example 2** **(Examples of Valuations)**
>
> If $k = \mathbb Q$, we can take the standard absolute value. (Take $C=2$.)
>
> Similarly, the usual $p$-adic evaluation, $\nu_p$, which sends $p^a t$ to $p^{-a}$.
> Here $C = 1$ is a valid constant.
>
> These are the two examples one should always keep in mind: with number fields,
> all valuations look like one of these too.

In fact, over $\mathbb Q$ it turns out that every valuation "is" one of these
two valuations (for a suitable definition of equality). To make this precise:

> **Definition 3.** We say $\left\lvert - \right\rvert_1 \sim \left\lvert - \right\rvert_2$ (i.e.
> two valuations on a field $k$ are equivalent) if there exists a constant
> $k > 0$ so that $\left\lvert \alpha \right\rvert_1 = \left\lvert \alpha \right\rvert_2^k$ for every $\alpha \in
> k$.

In particular, for any valuation we can force $C = 2$ to hold by taking an
equivalent valuation to a sufficient power.

In that case, we obtain the following:

> **Lemma 4.** In a valuation with $C = 2$, the triangle inequality holds.

_Proof:_ First, observe that we can get

$$
\left\lvert \alpha + \beta \right\rvert \le 2 \max \left\{ \left\lvert \alpha \right\rvert,
\left\lvert \beta \right\rvert \right\}.
$$

Applying this inductively, we obtain
$$\left\lvert \sum_{i=1}^{2^r} a_i \right\rvert \le 2^r \max_i \left\lvert a_i \right\rvert$$
or zero-padding,
$$\sum_{i=1}^{n} a_i \le 2n\max_i \left\lvert a_i \right\rvert.$$
From this, one can obtain

$$
\left\lvert \alpha+\beta \right\rvert^n \le \left\lvert \sum_{j=0}^n \binom nj
\alpha^j \beta^{n-j} \right\rvert \le 2(n+1) \sum_{j=0}^n \left\lvert \binom nj
\right\rvert \left\lvert \alpha \right\rvert^j \left\lvert \beta
\right\rvert^{n-j} \le 4(n+1)\left( \left\lvert \alpha \right\rvert+\left\lvert
\beta \right\rvert \right)^n.
$$

Letting $n \rightarrow \infty$ completes the proof. $\Box$

Next, we prove that

> **Lemma 5.** If $\omega^n=1$ for some $n$, then $\left\lvert \omega \right\rvert = 1$.
> In particular, on any finite field the only valuation is the trivial one which
> sends $0$ to $0$ and all elements to $1$.

_Proof:_ Immediate, since $\left\lvert \omega \right\rvert^n = 1$. $\Box$

## 2. Topological field induced by valuations

Let $k$ be a field. Given a valuation on it, we can define a basis of open sets
$$\left\{ \alpha \mid \left\lvert \alpha - a \right\rvert < d \right\}$$
across all $a \in K$, $d \in \mathbb R_{> 0}$.
One can check that the same valuation gives rise to the same topological spaces,
so it is fine to assume $C = 2$ as discussed earlier; thus, in fact we can make $k$ into a _metric space_,
with the valuation as the metric.

In what follows, we'll always assume our valuation satisfies the triangle inequality. Then:

> **Lemma 6.** Let $k$ be a field with a valuation.
> Viewing $k$ as a metric space, it is in fact a **topological field**,
> meaning addition and multiplication are continuous.

_Proof:_ Trivial; let's just check that multiplication is continuous. Observe that

$$
\begin{aligned} \left\lvert (a+\varepsilon_1)(b+\varepsilon_2) - ab
\right\rvert & \le \left\lvert \varepsilon_1\varepsilon_2 \right\rvert +
\left\lvert a\varepsilon_2 \right\rvert + \left\lvert b\varepsilon_1 \right\rvert \\ &\rightarrow 0.
\end{aligned}
$$

$\Box$

Now, earlier we saw that two valuations which are equivalent induce the same topology.
We now prove the following converse:

> **Proposition 7.** If two valuations $\left\lvert - \right\rvert_1$ and
> $\left\lvert - \right\rvert_2$ give the same topology, then they are in fact equivalent.

_Proof:_ Again, we may safely assume that both satisfy the triangle inequality.
Next, observe that $\left\lvert a \right\rvert < 1 \iff a^n \rightarrow 0$
(according to the metric) and by taking reciprocals,
$\left\lvert a \right\rvert > 1 \iff a^{-n} \rightarrow 0$.

Thus, given any $\beta$, $\gamma$ and integers $m$, $n$ we derive that
$$\left\lvert \beta^n\gamma^m \right\rvert_1 < 1 \iff \left\lvert \beta^n\gamma^m \right\rvert < 1$$
with similar statements holding with "$<$" replaced by "$=$", "$>$". Taking logs, we derive that

$$
n \log\left\lvert \beta \right\rvert_1 + m \log \left\lvert \gamma
\right\rvert_1 < 0 \iff n \log\left\lvert \beta \right\rvert_2 + m \log
\left\lvert \gamma \right\rvert_1 < 0
$$

and the analogous statements for "$=$", "$>$".
Now just choose an appropriate sequence of $m$, $n$ and we can deduce that

$$
\frac{\log \left\lvert \beta_1 \right\rvert}{\log \left\lvert \beta_2
\right\rvert} = \frac{\log \left\lvert \gamma_1 \right\rvert}{\log \left\lvert \gamma_2 \right\rvert}
$$

so it equals a fixed constant $c$ as desired. $\Box$

## 3. Discrete Valuations

> **Definition 8.** We say a valuation $\left\lvert - \right\rvert$ is
> **discrete** if its image around $1$ is discrete,
> meaning that if $\left\lvert a \right\rvert \in [1-\delta,1+\delta] \implies \left\lvert a \right\rvert = 1$
> for some real $\delta$. This is equivalent to requiring that
> $\{\log\left\lvert a \right\rvert\}$ is a discrete subgroup of the real numbers.

Thus, the real valuation (absolute value) isn't discrete, while the $p$-adic one is.

## 4. Non-Archimedean Valuations

Most importantly:

> **Definition 9.** A valuation $\left\lvert - \right\rvert$ is
> **non-Archimedean** if we can take $C = 1$ in our requirement that
> $\left\lvert a \right\rvert \le 1 \implies \left\lvert 1+a \right\rvert \le C$.
> Otherwise we say the valuation is **Archimedean**.

Thus the real valuation is Archimedean while the $p$-adic valuation is non-Archimedean.

> **Lemma 10.** Given a non-Archimedean valuation $\left\lvert - \right\rvert$,
> we have $\left\lvert b \right\rvert < \left\lvert a \right\rvert \implies \left\lvert a+b \right\rvert = \left\lvert
> a \right\rvert$.

_Proof:_ We have that

$$
\left\lvert a \right\rvert = \left\lvert (a+b)-b \right\rvert \le \max\left\{ \left\lvert a+b \right\rvert,
\left\lvert b \right\rvert \right\}.
$$

On the other hand, $\left\lvert a+b \right\rvert \le \max \{ \left\lvert a \right\rvert, \left\lvert b \right\rvert
\}$. $\Box$

Given a field $k$ and a non-Archimedean valuation on it, we can now consider the set
$$\mathcal O = \left\{ a \in k \mid \left\lvert a \right\rvert \le 1 \right\}$$
and by the previous lemma, this turns out to be a ring.
(This is the point we use the fact that the valuation is non-Archimedean;
without that $\mathcal O$ need not be closed under addition). Next, we define
$$\mathcal P = \left\{ a \in k \mid \left\lvert a \right\rvert < 1 \right\} \subset \mathcal O$$
which is an ideal. In fact it is maximal,
because $\mathcal O/\mathcal P$ is the set of units in $\mathcal O$, and is thus necessarily a field.

> **Lemma 11.** Two valuations are equal if they give the same ring $\mathcal O$ (as sets,
> not just up to isomorphism).

_Proof:_ If the valuations are equivalent it's trivial.

For the interesting converse direction (they have the same ring),
the datum of the ring $\mathcal O$ lets us detect whether
$\left\lvert a \right\rvert < \left\lvert b \right\rvert$ by simply checking
whether $\left\lvert ab^{-1} \right\rvert < 1$. Hence same topology, hence same valuation. $\Box$

We will really only work with valuations which are obviously discrete.
On the other hand, to detect non-Archimedean valuations, we have

> **Lemma 12.** $\left\lvert - \right\rvert$ is Archimedean if
> $\left\lvert n \right\rvert \le 1$ for every $n = 1 + \dots + 1 \in k$.

_Proof:_ Clearly Archimedean $\implies$ $\left\lvert n \right\rvert \le 1$.
The converse direction is more interesting; the proof is similar to the analytic trick we used earlier.
Given $\left\lvert a \right\rvert \le 1$, we wish to prove $\left\lvert 1+a \right\rvert \le 1$.
To do this, first assume the triangle inequality as usual, then

$$
\left\lvert 1+a \right\rvert^n < \sum_j \left\lvert \binom nj
\right\rvert\left\lvert a \right\rvert^j \le \sum_{j=0}^n \left\lvert a
\right\rvert^j \le \sum_{j=0}^n 1 = n+1.
$$

Finally, let $n \rightarrow \infty$ again. $\Box$

In particular, any field of finite characteristic in fact has
$\left\lvert n \right\rvert = 1$ and thus all valuations are non-Archimedean.

## 5. Completions

We say that a field $k$ is **complete** with respect to a valuation
$\left\lvert - \right\rvert$ if it is complete in the topological sense.

> **Theorem 13.** Every field $k$ is with a valuation
> $\left\lvert - \right\rvert$ can be embedded into a complete field
> $\overline{k}$ in a way which respects the valuation.

For example, the completion of $\mathbb Q$ with the Euclidean valuation is $\mathbb R$.
_Proof:_ Define $\overline{k}$ to be the topological completion of $k$; then extend by continuity; $\Box$
Given $k$ and its completion $\overline{k}$ we use the same notation for the valuations of both.

> **Proposition 14.** A valuation $\left\lvert - \right\rvert$ on
> $\overline{k}$ is non-Archimedean if and only if the valuation is non-Archimedean on $k$.

_Proof:_ We saw non-Archimedean $\iff$ $\left\lvert n \right\rvert \le 1$ for every $n = 1 + \dots + 1$.
$\Box$

> **Proposition 15.** Assume $\left\lvert - \right\rvert$ is non-Archimedean on
> $k$ and hence $\overline{k}$.
> Then the set of values achieved by $\left\lvert - \right\rvert$ coincides for $k$ and $\overline{k}$,
> i.e. $\{ \left\lvert k \right\rvert \} = \{ \left\lvert \overline{k} \right\rvert \}$.

Not true for Archimedean valuations; consider $\left\lvert \sqrt2 \right\rvert = \sqrt2 \notin \mathbb Q$.
_Proof:_ Assume $0 \neq b \in \overline{k}$;
then there is an $a \in k$ such that
$\left\lvert b-a \right\rvert < \left\lvert b \right\rvert$ since $k$ is dense in $\overline{k}$.
Then, $\left\lvert b \right\rvert \le \max \{ \left\lvert b-a \right\rvert, \left\lvert a \right\rvert \}$ which
implies $\left\lvert b \right\rvert = \left\lvert a \right\rvert$. $\Box$

## 6. Weak Approximation Theorem

> **Proposition 16** **(Weak Approximation Theorem)**
>
> Let $\left\lvert-\right\rvert_i$ be distinct nontrivial valuations of $k$ for $i=1,\dots,n$.
> Let $k_i$ denote the completion of $k$ with respect to $\left\lvert-\right\rvert_i$. Then the image
> $$k \hookrightarrow \prod_{i=1}^n k_i$$
> is dense.

This means that distinct valuations are as different as possible; for example,
if $\left\lvert-\right\rvert _1 = \left\lvert-\right\rvert _2$ then we might get, say,
a diagonal in $\mathbb R \times \mathbb R$ which is as far from dense as one can imagine.
Another way to think of this is that this is an analogue of the Chinese Remainder Theorem.

_Proof:_ We claim it suffices to exhibit $\theta_i \in k$ such that
$$\left\lvert \theta_i \right\rvert_j \begin{cases} > 1 & i = j \\ < 1 & \text{otherwise}. \end{cases}$$
Then

$$
\frac{\theta_i^r}{1+\theta_i^r} \rightarrow \begin{cases} 1 & \text{ in }
\left\lvert-\right\rvert_i \\ 0 & \text{ otherwise}. \end{cases}
$$

Hence for any point $(a_1, \dots, a_n)$ we can take the image of
$\sum \frac{\theta_i^r}{1+\theta_i^r} a_i \in k$. So it would follow that the image is dense.

Now, to construct the $\theta_i$ we proceed inductively. We first prove the result for $n=2$.
Since the topologies are different, we exhibit $\alpha$,
$\beta$ such that $\left\lvert \alpha_1 \right\rvert < \left\lvert \alpha_2 \right\rvert$ and $\left\lvert \beta_1
\right\rvert > \left\lvert \beta_2 \right\rvert$, and pick $\theta=\alpha\beta^{-1}$.

Now assume $n \ge 3$; it suffices to construct $\theta_1$. By induction, there is a $\gamma$ such that

$$
\left\lvert \gamma \right\rvert_1 > 1 \quad\text{and}\quad \left\lvert \gamma
\right\rvert_i < 1 \text{ for } i = 2, \dots, n-1.
$$

Also, there is a $\psi$ such that
$$\left\lvert \delta \right\rvert_1 > 1 \quad\text{and}\quad \left\lvert \delta \right\rvert_n < 1.$$
Now we can pick

$$
\theta_1 = \begin{cases} \gamma & \left\lvert \gamma \right\rvert_n < 1 \\
\phi^r\gamma & \left\lvert \gamma \right\rvert_n = 1 \\
\frac{\gamma^r}{1+\gamma^r} & \left\lvert \gamma \right\rvert_n > 1 \\ \end{cases}
$$

for sufficiently large $r$. $\Box$
