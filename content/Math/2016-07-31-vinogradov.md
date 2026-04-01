---
title: Vinogradov's Three-Prime Theorem (with Sammy Luo and Ryan Alweiss)
date: 2016-07-31 13:37
slug: vinogradov
tags: math, number theory
original_url: 2016/07/31/vinogradovs-three-prime-theorem-with-sammy-luo-and-ryan-alweiss/
status: published
---

This was my final paper for 18.099, seminar in discrete analysis, jointly with Sammy Luo and Ryan Alweiss.

We prove that every sufficiently large odd integer can be written as the sum of three primes,
conditioned on a strong form of the prime number theorem.

## 1. Introduction

In this paper, we prove the following result:

> **Theorem 1** **(Vinogradov)** <span id="thmvinogradov"></span>
>
> Every sufficiently large odd integer $N$ is the sum of three prime numbers.

In fact, the following result is also true, called the "weak Goldbach conjecture".

> **Theorem 2** **(Weak Goldbach conjecture)** <span id="thmgoldbach"></span>
>
> Every odd integer $N \ge 7$ is the sum of three prime numbers.

The proof of Vinogradov's theorem becomes significantly simpler if one assumes
the generalized Riemann hypothesis;
this allows one to use a strong form of the prime number theorem ([Theorem 9](#thmpnt)).
This conditional proof was given by Hardy and Littlewood in the 1923's.
In 1997, Deshouillers, Effinger,
te Riele and Zinoviev showed that the generalized Riemann hypothesis in fact
also implies the weak Goldbach conjecture by improving the bound to $10^{20}$
and then exhausting the remaining cases via a computer search.

As for unconditional proofs, Vinogradov was able to eliminate the dependency on
the generalized Riemann hypothesis in 1937, which is why the [Theorem 1](#thmvinogradov) bears his name.
However, Vinogradov's bound used the ineffective Siegel-Walfisz theorem; his student K.
Borozdin showed that $3^{3^{15}}$ is large enough.
Over the years the bound was improved,
until recently in 2013 when Harald Helfgott claimed the first unconditional
proof of [Theorem 2](#thmgoldbach), see [here](http://arxiv.org/abs/1312.7748).

In this exposition we follow Hardy and Littlewood's approach, i.e.
we prove [Theorem 1](#thmvinogradov) assuming the generalized Riemann hypothesis,
following the exposition of [Rhee](http://etotheipi.weebly.com/uploads/8/1/2/0/8120131/_threeprimes.pdf).
An exposition of the unconditional proof by Vinogradov is given by
[Rouse](http://math.uchicago.edu/~may/REU2013/REUPapers/Rouse.pdf).

## 2. Synopsis

<span id="secsetup"></span> We are going to prove that <span id="eqGG"></span>
$$\sum_{a+b+c = N} \Lambda(a) \Lambda(b) \Lambda(c) \asymp \frac12 N^2 \mathfrak G(N) \qquad (1)$$
where

$$
\mathfrak G(N) \coloneqq \prod_{p \mid N} \left( 1 -
\frac{1}{(p-1)^2} \right) \prod_{p \nmid N} \left( 1 + \frac{1}{(p-1)^3} \right)
$$

and $\Lambda$ is the von Mangoldt function defined as usual.
Then so long as $2 \nmid N$, the quantity $\mathfrak G(N)$ will be bounded away from zero;
thus [(1)](#eqGG) will imply that in fact there are many ways to write $N$ as
the sum of three distinct prime numbers.

The sum [(1)](#eqGG) is estimated using Fourier analysis. Let us define the following.

> **Definition 3.** Let $\mathbb T = \mathbb R/\mathbb Z$ denote the circle group,
> and let $e : \mathbb T \rightarrow \mathbb C$ be the exponential function
> $\theta \mapsto \exp(2\pi i \theta)$.
> For $\alpha\in\mathbb T$, $\{\alpha\}$ denotes the minimal distance from $\alpha$ to an integer.

Note that $|e(\theta)-1|=\Theta(\{\theta\})$.

> **Definition 4.** For $\alpha \in \mathbb T$ and $x > 0$ we define
> $$S(x, \alpha) = \sum_{n \le x} \Lambda(n) e(n\alpha).$$

Then we can rewrite [(1)](#eqGG) using $S$ as a "Fourier coefficient":

> **Proposition 5.** <span id="proprewrite"></span> We have <span id="eqint"></span>
>
> $$
> \sum_{a+b+c = N} \Lambda(a) \Lambda(b) \Lambda(c) = \int_{\alpha \in \mathbb T} S(N,
> \alpha)^3 e(-N\alpha) d\alpha. \qquad (2)
> $$

_Proof:_ We have
$$S(N,\alpha)^3=\sum_{a,b,c\leq N}\Lambda(a)\Lambda(b)\Lambda(c)e((a+b+c)\alpha),$$
so

$$
\begin{aligned}
  \int_{\alpha \in \mathbb T} S(N, \alpha)^3 e(-N\alpha) d\alpha
    &= \int_{\alpha \in \mathbb T} \sum_{a,b,c\leq N}
       \Lambda(a)\Lambda(b)\Lambda(c)e((a+b+c)\alpha) e(-N\alpha) d\alpha \\
    &= \sum_{a,b,c\leq N}\Lambda(a)\Lambda(b)\Lambda(c)
       \int_{\alpha \in \mathbb T}e((a+b+c-N)\alpha) d\alpha \\
    &= \sum_{a,b,c\leq N}\Lambda(a)\Lambda(b)\Lambda(c)I(a+b+c=N) \\
    &= \sum_{a+b+c=N}\Lambda(a)\Lambda(b)\Lambda(c),
\end{aligned}
$$

as claimed. $\Box$

In order to estimate the integral in [Proposition 5](#proprewrite),
we divide $\mathbb T$ into the so-called "major" and "minor" arcs. Roughly,

- The "major arcs" are subintervals of $\mathbb T$ centered at a rational number with small denominator.
- The "minor arcs" are the remaining intervals.

These will be made more precise later.
This general method is called the _Hardy-Littlewood circle method_,
because of the integral over the circle group $\mathbb T$.

The rest of the paper is structured as follows.
In [Section 3](#secprelim), we define the Dirichlet character and other number-theoretic objects,
and state some estimates for the partial sums of these objects conditioned on the Riemann hypothesis.
These bounds are then used in [Section 4](#secfourier) to provide corresponding estimates on $S(x, \alpha)$.
In [Section 5](#secarc) we then define the major and minor arcs rigorously and
use the previous estimates to given an upper bound for the integral over both areas.
Finally, we complete the proof in [Section 6](#secfinish).

## 3. Prime number theorem type bounds

<span id="secprelim"></span> In this section,
we collect the necessary number-theoretic results that we will need.
It is in this section only that we will require the generalized Riemann hypothesis.

As a reminder, the notation $f(x)\ll g(x)$, where $f$ is a complex function and $g$ a nonnegative real one,
means $f(x)=O(g(x))$, a statement about the magnitude of $f$.
Likewise, $f(x)=g(x)+O(h(x))$ simply means that for some $C$,
$|f(x)-g(x)|\leq C|h(x)|$ for all sufficiently large $x$.

### 3.1. Dirichlet characters

In what follows, $q$ denotes a positive integer.

> **Definition 6.** A **Dirichlet character modulo $q$** $\chi$ is a
> homomorphism $\chi : (\mathbb Z/q)^\times \rightarrow \mathbb C^\times$.
> It is said to be **trivial** if $\chi = 1$; we denote this character by $\chi_0$.

By slight abuse of notation, we will also consider $\chi$ as a function
$\mathbb Z \rightarrow \mathbb C^\ast$ by setting $\chi(n) = \chi(n \pmod q)$
for $\gcd(n,q) = 1$ and $\chi(n) = 0$ for $\gcd(n,q) > 1$.

> **Remark 7.** The Dirichlet characters form a multiplicative group of order $\phi(q)$ under multiplication,
> with inverse given by complex conjugation.
> Note that $\chi(m)$ is a primitive $\phi(q)$-th root of unity for any $m \in (\mathbb Z/q)^\times$,
> thus $\chi$ takes values in the unit circle.

Moreover, the Dirichlet characters satisfy an orthogonality relation

Experts may recognize that the Dirichlet characters are just the elements of the
Pontryagin dual of $(\mathbb Z/q)^\times$.
In particular, they satisfy an orthogonality relationship <span id="eqorthog"></span>

$$
\frac{1}{\phi(q)} \sum_{\chi \text{ mod } q} \chi(n) \overline{\chi(a)} =
\begin{cases} 1 & n = a \pmod q \\ 0 & \text{otherwise} \end{cases} \qquad (3)
$$

and thus form an orthonormal basis for functions $(\mathbb Z/q)^\times \rightarrow \mathbb C$.

### 3.2. Prime number theorem for arithmetic progressions

> **Definition 8.** The **generalized Chebyshev function** is defined by
> $$\psi(x, \chi) = \sum_{n \le x} \Lambda(n) \chi(n).$$

The Chebyshev function is studied extensively in analytic number theory,
as it is the most convenient way to phrase the major results of analytic number theory.
For example, the prime number theorem is equivalent to the assertion that
$$\psi(x, \chi_0) = \sum_{n \le x} \Lambda(n) \asymp x$$
where $q = 1$ (thus $\chi_0$ is the constant function $1$).
Similarly, Dirichlet's theorem actually asserts that any $q \ge 1$,

$$
\psi(x, \chi) = \begin{cases} x + o_q(x) & \chi = \chi_0 \text{ trivial} \\
o_q(x) & \chi \neq \chi_0 \text{ nontrivial}. \end{cases}
$$

However, the error term in these estimates is quite poor (more than
$x^{1-\varepsilon}$ for every $\varepsilon$).
However, by assuming the Riemann Hypothesis for a certain "$L$-function" attached to $\chi$,
we can improve the error terms substantially.

> **Theorem 9** **(Prime number theorem for arithmetic progressions)**
>
> <span id="thmpnt"></span> Let $\chi$ be a Dirichlet character modulo $q$,
> and assume the Riemann hypothesis for the $L$-function attached to $\chi$.
>
> 1.  If $\chi$ is nontrivial, then
>
>     $$\psi(x, \chi) \ll \sqrt{x} (\log qx)^2.$$
>
> 2.  If $\chi = \chi_0$ is trivial, then
>
>     $$\psi(x, \chi_0) = x + O\left( \sqrt x (\log x)^2 + \log q \log x \right).$$

[Theorem 9](#thmpnt) is the strong estimate that we will require when putting
good estimates on $S(x, \alpha)$,
and is the only place in which the generalized Riemann Hypothesis is actually required.

### 3.3. Gauss sums

> **Definition 10.** For $\chi$ a Dirichlet character modulo $q$, the **Gauss sum** $\tau(\chi)$ is defined by
> $$\tau(\chi)=\sum_{a=0}^{q-1}\chi(a)e(a/q).$$

We will need the following fact about Gauss sums.

> **Lemma 11.** <span id="lemgauss"></span> Consider Dirichlet characters modulo $q$. Then:
>
> 1.  We have $\tau(\chi_0) = \mu(q)$.
> 2.  For any $\chi$ modulo $q$, $\left\lvert \tau(\chi) \right\rvert \le \sqrt q$.

### 3.4. Dirichlet approximation

We finally require Dirichlet approximation theorem in the following form.

> **Theorem 12** **(Dirichlet approximation)**
>
> <span id="thmapprox"></span> Let $\alpha \in \mathbb R$ be arbitrary, and $M$ a fixed integer.
> Then there exists integers $a$ and $q = q(\alpha)$, with $1 \le q \le M$ and $\gcd(a,q) = 1$, satisfying
> $$\left\lvert \alpha - \frac aq \right\rvert \le \frac{1}{qM}.$$

## 4. Bounds on $S(x, \alpha)$

<span id="secfourier"></span> In this section, we use our number-theoretic results to bound $S(x,\alpha)$.

First, we provide a bound for $S(x,\alpha)$ if $\alpha$ is a rational number with "small" denominator $q$.

> **Lemma 13.** <span id="lem31"></span> Let $\gcd(a,q) = 1$. Assuming [Theorem 9](#thmpnt), we have
> $$S(x, a/q) = \frac{\mu(q)}{\phi(q)} x + O\left( \sqrt{qx} (\log qx)^2 \right)$$
> where $\mu$ denotes the Möbius function.

_Proof:_ Write the sum as
$$S(x, a/q) = \sum_{n \le x} \Lambda(n) e(na/q).$$
First we claim that the terms $\gcd(n,q) > 1$ (and $\Lambda(n) \neq 0$)
contribute a negligibly small $\ll \log q \log x$. To see this, note that

- The number $q$ has $\ll \log q$ distinct prime factors, and
- If $p^e \mid q$, then $\Lambda(p) + \dots + \Lambda(p^e) = e\log p = \log(p^e) < \log x$.

So consider only terms with $\gcd(n,q) = 1$. To bound the sum, notice that

$$
\begin{aligned}
  e(n \cdot a/q)
    &= \sum_{b \text{ mod } q} e(b/q) \cdot \mathbf 1(b \equiv an) \\
    &= \sum_{b \text{ mod } q} e(b/q) \left( \frac{1}{\phi(q)}
       \sum_{\chi \text{ mod } q} \chi(b) \overline{\chi(an)} \right)
\end{aligned}
$$

by the orthogonality relations. Now we swap the order of summation to obtain a Gauss sum:

$$
\begin{aligned}
  e(n \cdot a/q)
    &= \frac{1}{\phi(q)} \sum_{\chi \text{ mod } q}
       \overline{\chi(an)} \left( \sum_{b \text{ mod } q} \chi(b) e(b/q) \right) \\
    &= \frac{1}{\phi(q)} \sum_{\chi \text{ mod } q} \overline{\chi(an)} \tau(\chi).
\end{aligned}
$$

Thus, we swap the order of summation to obtain that

$$
\begin{aligned}
  S(x, \alpha)
    &= \sum_{\substack{n \le x \\ \gcd(n,q) = 1}} \Lambda(n) e(n \cdot a/q) \\
    &= \frac{1}{\phi(q)} \sum_{\substack{n \le x \\ \gcd(n,q) = 1}}
       \sum_{\chi \text{ mod } q} \Lambda(n) \overline{\chi(an)} \tau(\chi) \\
    &= \frac{1}{\phi(q)} \sum_{\chi \text{ mod } q} \tau(\chi)
       \sum_{\substack{n \le x \\ \gcd(n,q) = 1}} \Lambda(n) \overline{\chi(an)} \\
    &= \frac{1}{\phi(q)} \sum_{\chi \text{ mod } q} \overline{\chi(a)} \tau(\chi)
       \sum_{\substack{n \le x \\ \gcd(n,q) = 1}} \Lambda(n)\overline{\chi(n)} \\
    &= \frac{1}{\phi(q)} \sum_{\chi \text{ mod } q}
       \overline{\chi(a)} \tau(\chi) \psi(x, \overline\chi) \\
    &= \frac{1}{\phi(q)} \left( \tau(\chi_0) \psi(x, \chi_0)
       + \sum_{1 \neq \chi \text{ mod } q} \overline{\chi(a)} \tau(\chi) \psi(x, \overline\chi) \right).
\end{aligned}
$$

Now applying both parts of [Lemma 11](#lemgauss) in conjunction with [Theorem 9](#thmpnt) gives

$$
\begin{aligned}
  S(x,\alpha)
    &= \frac{\mu(q)}{\phi(q)} \left( x + O\left( \sqrt x (\log qx)^2 \right) \right)
       + O\left( \sqrt x (\log x)^2 \right) \\
    &= \frac{\mu(q)}{\phi(q)} x + O\left( \sqrt{qx} (\log qx)^2 \right)
\end{aligned}
$$

as desired. $\Box$

We then provide a bound when $\alpha$ is "close to" such an $a/q$.

> **Lemma 14.** <span id="lem32"></span> Let $\gcd(a,q) = 1$ and $\beta \in \mathbb T$.
> Assuming [Theorem 9](#thmpnt), we have

$$
S(x, a/q + \beta) = \frac{\mu(q)}{\phi(q)} \left( \sum_{n \le x} e(\beta n)
\right) + O\left( (1+\{\beta\}x) \sqrt{qx} (\log qx)^2 \right).
$$

_Proof:_ For convenience let us assume $x \in \mathbb Z$. Let $\alpha = a/q + \beta$.
Let us denote $\text{Err}(x, \alpha) = S(x,\alpha) - \frac{\mu(q)}{\phi(q)} x$,
so by [Lemma 13](#lem31) we have $\text{Err}(x,\alpha) \ll \sqrt{qx}(\log x)^2$. We have

$$
\begin{aligned}
  S(x, \alpha)
    &= \sum_{n \le x} \Lambda(n) e(na/q) e(n\beta) \\
    &= \sum_{n \le x} e(n\beta) \left( S(n, a/q) - S(n-1, a/q) \right) \\
    &= \sum_{n \le x} e(n\beta) \left( \frac{\mu(q)}{\phi(q)}
       + \text{Err}(n, \alpha) - \text{Err}(n-1, \alpha) \right) \\
    &= \frac{\mu(q)}{\phi(q)} \left( \sum_{n \le x} e(n\beta) \right)
       + \sum_{1 \le m \le x-1} \left( e( (m+1)\beta) - e( m\beta ) \right) \text{Err}(m, \alpha) \\
    &\qquad + e(x\beta) \text{Err}(x, \alpha) - e(0) \text{Err}(0, \alpha) \\
    &\le \frac{\mu(q)}{\phi(q)} \left( \sum_{n \le x} e(n\beta) \right)
       + \left( \sum_{1 \le m \le x-1} \{\beta\} \text{Err}(m, \alpha) \right)
       + \text{Err}(0, \alpha) + \text{Err}(x, \alpha) \\
    &\ll \frac{\mu(q)}{\phi(q)} \left( \sum_{n \le x} e(n\beta) \right)
       + \left( 1+x\left\{ \beta \right\} \right) O\left( \sqrt{qx} (\log qx)^2 \right)
\end{aligned}
$$

as desired. $\Box$

Thus if $\alpha$ is close to a fraction with small denominator, the value of $S(x, \alpha)$ is bounded above.
We can now combine this with the Dirichlet approximation theorem to obtain the following general result.

> **Corollary 15.** <span id="lem33"></span> Suppose $M = N^{2/3}$ and suppose
> $\left\lvert \alpha - a/q \right\rvert \le \frac{1}{qM}$ for some $\gcd(a,q) = 1$ with $q \le M$.
> Assuming [Theorem 9](#thmpnt), we have
> $$S(x, \alpha) \ll \frac{x}{\varphi(q)} + x^{\frac56+\varepsilon}$$
> for any $\varepsilon > 0$.

_Proof:_ Apply [Lemma 14](#lem32) directly. $\Box$

## 5. Estimation of the arcs

<span id="secarc"></span> We'll write
$$f(\alpha) \coloneqq S(N,\alpha)=\sum_{n \le N} \Lambda(n)e(n\alpha)$$
for brevity in this section.

Recall that we wish to bound the right-hand side of [(2)](#eqint) in [Proposition 5](#proprewrite).
We split $[0,1]$ into two sets, which we call the "major arcs" and the "minor arcs." To do so,
we use Dirichlet approximation, as hinted at earlier.

In what follows, fix
$$\begin{aligned} M &= N^{2/3} \\ K &= (\log N)^{10}. \end{aligned}$$

### 5.1. Setting up the arcs

> **Definition 16.** For $q \le K$ and $\gcd(a,q) = 1$, $1 \le a \le q$, we define
>
> $$
> \mathfrak M(a,q) = \left\{ \alpha \in \mathbb T \mid \left\lvert \alpha -
> \frac aq \right\rvert \le \frac 1M \right\}.
> $$

These will be the **major arcs**. The union of all major arcs is denoted by $\mathfrak M$.
The complement is denoted by $\mathfrak m$.

Equivalently, for any $\alpha$, consider $q = q(\alpha) \le M$ as in [Theorem 12](#thmapprox).
Then $\alpha \in \mathfrak M$ if $q \le K$ and $\alpha \in \mathfrak m$ otherwise.

> **Proposition 17.** <span id="remmajorarc"></span> $\mathfrak M$ is composed
> of finitely many disjoint intervals $\mathfrak M(a,q)$ with $q \le K$.
> The complement $\mathfrak m$ is nonempty.

_Proof:_ Note that if $q_1, q_2 \le K$ and $a/q_1 \neq b/q_2$ then
$\left\lvert \frac{a}{q_1} - \frac{b}{q_2} \right\rvert \ge \frac{1}{q_1q_2} \gg \frac{3}{qM}$. $\Box$

In particular both $\mathfrak M$ and $\mathfrak m$ are measurable.
Thus we may split the integral in [(2)](#eqint) over $\mathfrak M$ and $\mathfrak m$.
This integral will have large magnitude on the major arcs, and small magnitude on the minor arcs,
so overall the whole interval $[0,1]$ it will have large magnitude.

### 5.2. Estimate of the minor arcs

First, we note the well known fact $\phi(q) \gg q/\log q$.
Note also that if $q=q(\alpha)$ as in the last section and $\alpha$ is on a minor arc,
we have $q > (\log N)^{10}$, and thus $\phi(q) \gg (\log N)^{9}$.

As such Corollary 3.3 yields that $f(\alpha) \ll \frac{N}{\phi(q)}+N^{.834} \ll \frac{N}{(\log N)^9}$.

Now,

$$
\begin{aligned}
\left\lvert \int_{\mathfrak m}f(\alpha)^3e(-N\alpha) d\alpha \right\rvert
&\le \int_{\mathfrak m}\left\lvert f(\alpha)\right\rvert ^3 d\alpha \\
&\ll \frac{N}{(\log N)^9} \int_{0}^{1}\left\lvert f(\alpha)\right\rvert ^2 d\alpha \\
&=\frac{N}{(\log N)^9}\int_{0}^{1}f(\alpha)f(-\alpha) d\alpha \\
&=\frac{N}{(\log N)^9}\sum_{n \le N} \Lambda(n)^2 \\
&\ll \frac{N^2}{(\log N)^8},
\end{aligned}
$$

using the well known bound $\sum_{n \le N} \Lambda(n)^2 \ll \frac{N}{\log N}$.
This bound of $\frac{N^2}{(\log N)^8}$ will be negligible compared to lower
bounds for the major arcs in the next section.

### 5.3. Estimate on the major arcs

We show that
$$\int_{\mathfrak M}f(\alpha)^3e(-N\alpha) d\alpha \asymp \frac{N^2}{2} \mathfrak G(N).$$
By [Proposition 17](#remmajorarc) we can split the integral over each interval and write

$$
\int_{\mathfrak M} f(\alpha)^3e(-N\alpha) d\alpha =
  \sum_{q \le (\log N)^{10}} \sum_{\substack{1 \le a \le q \\ \gcd(a,q)=1}}
  \int_{-1/qM}^{1/qM}f(a/q+\beta)^3e(-N(a/q+\beta)) d\beta.
$$

Then we apply [Lemma 14](#lem32), which gives

$$
\begin{aligned}
  f(a/q+\beta)^3
    &= \left(\frac{\mu(q)}{\phi(q)}\sum_{n \le N}e(\beta n) \right)^3 \\
    &+ \left(\frac{\mu(q)}{\phi(q)}\sum_{n \le N}e(\beta n)\right)^2
       O\left((1+\{\beta\}N)\sqrt{qN} \log^2 qN\right) \\
    &+ \left(\frac{\mu(q)}{\phi(q)}\sum_{n \le N}e(\beta n)\right)
       O\left((1+\{\beta\}N)\sqrt{qN} \log^2 qN\right)^2 \\
    &+ O\left((1+\{\beta\}N)\sqrt{qN} \log^2 qN\right)^3.
\end{aligned}
$$

Now, we can do casework on the side of $N^{-.9}$ that $\{\beta\}$ lies on.

- If $\{\beta\} \gg N^{-.9}$,
  we have $\sum_{n \le N}e(\beta n) \ll \frac{2}{|e(\beta)-1|} \ll \frac{1}{\{\beta\}} \ll N^{.9}$,
  and $(1+\{\beta\}N)\sqrt{qN} \log^2 qN \ll N^{5/6+\varepsilon}$,
  because certainly we have $\{\beta\}<1/M=N^{-2/3}$.
- If on the other hand $\{\beta\}\ll N^{-.9}$, we have $\sum_{n \le N}e(\beta n) \ll N$ obviously,
  and $O(1+\{\beta\}N)\sqrt{qN} \log^2 qN) \ll N^{3/5+\varepsilon}$.

As such, we obtain

$$
f(a/q+\beta)^3 \ll \left( \frac{\mu(q)}{\phi(q)}\sum_{n \le N}e(\beta n) \right)^3
  + O\left(N^{79/30+\varepsilon}\right)
$$

in either case. Thus, we can write

$$
\begin{aligned}
  &\qquad \int_{\mathfrak M} f(\alpha)^3e(-N\alpha) d\alpha \\
  &= \sum_{q \le (\log N)^{10}} \sum_{\substack{1 \le a \le q \\ \gcd(a,q)=1}}
     \int_{-1/qM}^{1/qM} f(a/q+\beta)^3e(-N(a/q+\beta)) d\beta \\
  &= \sum_{q \le (\log N)^{10}} \sum_{\substack{1 \le a \le q \\ \gcd(a,q)=1}}
     \int_{-1/qM}^{1/qM}\left[\left(\frac{\mu(q)}{\phi(q)}\sum_{n \le N}e(\beta n)\right)^3
     + O\left(N^{79/30+\varepsilon}\right)\right]e(-N(a/q+\beta)) d\beta \\
  &= \sum_{q \le (\log N)^{10}} \frac{\mu(q)}{\phi(q)^3} S_q
     \left(\sum_{\substack{1 \le a \le q \\ \gcd(a,q)=1}} e(-N(a/q))\right)
     \left( \int_{-1/qM}^{1/qM}\left(\sum_{n \le N}e(\beta n)\right)^3e(-N\beta) d\beta \right ) \\
  &\qquad +O\left(N^{59/30+\varepsilon}\right).
\end{aligned}
$$

just using $M \le N^{2/3}$. Now, we use
$$\sum_{n \le N}e(\beta n) = \frac{1-e(\beta N)}{1-e(\beta)} \ll \frac{1}{\{\beta\}}.$$
This enables us to bound the expression

$$
\int_{1/qM}^{1-1/qM}\left (\sum_{n \le N}e(\beta n)\right) ^ 3 e(-N\beta)d\beta
  \ll \int_{1/qM}^{1-1/qM}\{\beta\}^{-3} d\beta
  = 2\int_{1/qM}^{1/2}\beta^{-3} d\beta
  \ll q^2M^2.
$$

But the integral over the entire interval is

$$
\begin{aligned}
  \int_{0}^{1}\left(\sum_{n \le N}e(\beta n) \right)^3 e(-N\beta)d\beta
    &= \int_{0}^{1} \sum_{a,b,c \le N} e((a+b+c-N)\beta) \\
    &\ll \sum_{a,b,c \le N} \mathbf 1(a+b+c=N) \\
    &= \binom{N-1}{2}.
\end{aligned}
$$

Considering the difference of the two integrals gives

$$
\int_{-1/qM}^{1/qM}\left(\sum_{n \le N}e(\beta n) \right)^3 e(-N\beta) d\beta
  - \frac{N^2}{2} \ll q^2 M^2 + N \ll (\log N)^c N^{4/3},
$$

for some absolute constant $c$.

For brevity, let
$$S_q = \sum_{\substack{1 \le a \le q \\ \gcd(a,q)=1}} e(-N(a/q)).$$
Then

$$
\begin{aligned}
  \int_{\mathfrak M} f(\alpha)^3e(-N\alpha) d\alpha
    &= \sum_{q \le (\log N)^{10}} \frac{\mu(q)}{\phi(q)^3}S_q
       \left( \int_{-1/qM}^{1/qM}\left(\sum_{n \le N}e(\beta n)\right)^3e(-N\beta) d\beta \right ) \\
    &\qquad +O\left(N^{59/30+\varepsilon}\right) \\
    &= \frac{N^2}{2}\sum_{q \le (\log N)^{10}} \frac{\mu(q)}{\phi(q)^3}S_q
       + O((\log N)^{10+c} N^{4/3}) + O(N^{59/30+\varepsilon}) \\
    &= \frac{N^2}{2}\sum_{q \le (\log N)^{10}} \frac{\mu(q)}{\phi(q)^3}
       + O(N^{59/30+\varepsilon}).
\end{aligned}
$$

The inner sum is bounded by $\phi(q)$. So,

$$
\left\lvert \sum_{q>(\log N)^{10}} \frac{\mu(q)}{\phi(q)^3} S_q \right\rvert \le
  \sum_{q>(\log N)^{10}} \frac{1}{\phi(q)^2},
$$

which converges since $\phi(q)^2 \gg q^c$ for some $c > 1$. So

$$
\int_{\mathfrak M} f(\alpha)^3e(-N\alpha) d\alpha =
  \frac{N^2}{2}\sum_{q = 1}^\infty \frac{\mu(q)}{\phi(q)^3}S_q + O(N^{59/30+\varepsilon}).
$$

Now, since $\mu(q)$, $\phi(q)$,
and $\sum_{\substack{1 \le a \le q \\ \gcd(a,q)=1}} e(-N(a/q))$ are multiplicative functions of $q$,
and $\mu(q)=0$ unless $q$ is squarefree,

$$
\begin{aligned}
  \sum_{q = 1}^\infty \frac{\mu(q)}{\phi(q)^3} S_q
    &= \prod_p \left(1+\frac{\mu(p)}{\phi(p)^3}S_p \right) \\
    &= \prod_p \left(1-\frac{1}{(p-1)^3} \sum_{a=1}^{p-1} e(-N(a/p))\right) \\
    &= \prod_p \left(1-\frac{1}{(p-1)^3}\sum_{a=1}^{p-1} (p\cdot \mathbf 1(p|N) - 1)\right) \\
    &= \prod_{p|N}\left(1-\frac{1}{(p-1)^2}\right)
       \prod_{p \nmid N}\left(1+\frac{1}{(p-1)^3}\right) \\
    &= \mathfrak G(N).
\end{aligned}
$$

So,

$$
\int_{\mathfrak M} f(\alpha)^3e(-N\alpha) d\alpha
  = \frac{N^2}{2}\mathfrak{G}(N) + O(N^{59/30+\varepsilon}).
$$

When $N$ is odd,

$$
\mathfrak{G}(N) = \prod_{p|N}\left(1-\frac{1}{(p-1)^2}\right)
  \prod_{p \nmid N}\left(1+\frac{1}{(p-1)^3}\right)
  \geq \prod_{m\geq 3}\left(\frac{m-2}{m-1}\frac{m}{m-1}\right)
  = \frac{1}{2},
$$

so that we have
$$\int_{\mathfrak M} f(\alpha)^3e(-N\alpha) d\alpha \asymp \frac{N^2}{2}\mathfrak{G}(N),$$
as desired.

## 6. Completing the proof

<span id="secfinish"></span>

Because the integral over the minor arc is $o(N^2)$, it follows that

$$
\sum_{a+b+c=N} \Lambda(a)\Lambda(b)\Lambda(c)
  = \int_{0}^{1} f(\alpha)^3 e(-N\alpha) d \alpha
  \asymp \frac{N^2}{2}\mathfrak{G}(N)
  \gg N^2.
$$

Consider the set $S_N$ of integers $p^k\leq N$ with $k>1$.
We must have $p \le N^{\frac{1}{2}}$,
and for each such $p$ there are at most $O(\log N)$ possible values of $k$.
As such,

$$
|S_N| \ll \pi(N^{1/2}) \log N \ll N^{1/2}.
$$

Thus

$$
\sum_{\substack{a+b+c=N \\ a\in S_N}} \Lambda(a)\Lambda(b)\Lambda(c)
  \ll (\log N)^3 |S|N
  \ll \log(N)^3 N^{3/2},
$$

and similarly for $b\in S_N$ and $c\in S_N$.
Notice that summing over $a\in S_N$ is equivalent to summing over composite $a$, so

$$
\sum_{p_1+p_2+p_3=N} \Lambda(p_1)\Lambda(p_2)\Lambda(p_3)
  = \sum_{a+b+c=N} \Lambda(a)\Lambda(b)\Lambda(c) + O(\log(N)^3 N^{3/2})
  \gg N^2,
$$

where the sum is over primes $p_i$. This finishes the proof.
