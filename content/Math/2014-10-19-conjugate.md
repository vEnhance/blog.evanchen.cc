---
title: Why do roots come in conjugate pairs?
date: 2014-10-19 13:37
slug: conjugate
tags: math, number theory
original_url: 2014/10/19/why-do-roots-come-in-conjugate-pairs/
status: published
---

This is an expanded version of an answer I gave to a question that came up while
I was assisting the [2014-2015 WOOT class](http://www.artofproblemsolving.com/School/woot.php).
It struck me as an unusually good way to motivate higher math using stuff that
people notice in high school but for some reason decide to not think about.

In high school precalculus, you'll often be asked to find the roots of some
polynomial with integer coefficients. For instance,
$$x^3 - x^2 - x - 15 = (x-3)(x^2+2x+5)$$
has roots $3$, $1+2i$, $-1-2i$. Or as another example,
$$x^3 - 3x^2 - 2x + 2 = (x+1)(x^2-4x+2)$$
has roots $-1$, $2 + \sqrt 2$, $2 - \sqrt 2$.
You'll notice that the "weird" roots, like $1 \pm 2i$ and $2 \pm \sqrt 2$, are coming up in pairs.
In fact, I think precalculus explicitly tells you that the imaginary roots come in conjugate pairs.
More generally, it seems like all the roots of the form $a + b \sqrt c$ come in "conjugate pairs".
And you can see why.

But a polynomial like
$$x^3 - 8x + 4$$
has no rational roots. (The roots of this are approximately $-3.0514$, $0.51730$, $2.5341$.) Or even simpler,
$$x^3 - 2$$
has only one real root, $\sqrt[3]{2}$.
These roots, even though they are irrational, have no "conjugate" pairs. Or do they?

Let's try and figure out exactly what's happening. Let $\alpha$ be any complex number.
We define the **minimal polynomial** of $\alpha$ to be the monic polynomial $P(x)$ such that

- $P(x)$ has rational coefficients, and leading coefficient $1$,
- $P(\alpha) = 0$.
- The degree of $P$ is as small as possible.

For example, $\sqrt 2$ has minimal polynomial $x^2-2$.
Note that $100x^2 - 200$ is also a polynomial of the same degree which has $\sqrt 2$ as a root;
that's why we want to require the polynomial to be monic.
That's also why we choose to work in the rational numbers; that way,
we can divide by leading coefficients without worrying if we get non-integers.

Why do we care? The point is as follows: suppose we have another polynomial $A(x)$ such that $A(\alpha) = 0$.
Then we claim that $P(x)$ actually divides $A(x)$!
That means that all the other roots of $P$ will also be roots of $A$.

The proof is by contradiction: if not,
by [polynomial long division](https://www.google.com/url?q=http://www.khanacademy.org/math/algebra2/polynomial_and_rational/dividing_polynomials/v/polynomial-division&sa=U&ei=cMY1VJaMLIbbPd3vgRA&ved=0CAgQFjAD&client=internal-uds-cse&usg=AFQjCNHZW0qzK1RReo9G1jjk-I_iGcTLYg),
we can find a quotient and remainder $Q(x)$, $R(x)$ such that
$$A(x) = Q(x) P(x) + R(x)$$
and $R(x) \not\equiv 0$. Notice that by plugging in $x = \alpha$, we find that $R(\alpha) = 0$.
But $\deg R < \deg P$, and $P(x)$ was supposed to be the minimal polynomial. That's impossible!

Let's look at a more concrete example. Consider $A(x) = x^3-3x^2-2x+2$ from the beginning.
The minimal polynomial of $2 + \sqrt 2$ is $P(x) = x^2 - 4x + 2$ (why?).
Now we know that if $2 + \sqrt 2$ is a root, then $A(x)$ is divisible by $P(x)$.
And that's how we know that if $2 + \sqrt 2$ is a root of $A$, so must $2 - \sqrt 2$.

As another example, the minimal polynomial of $\sqrt[3]{2}$ is $x^3-2$.
So $\sqrt[3]{2}$ actually has **two** conjugates, namely,
$\alpha = \sqrt[3]{2} \left( \cos 120^\circ + i \sin 120^\circ \right)$ and
$\beta = \sqrt[3]{2} \left( \cos 240^\circ + i \sin 240^\circ \right)$.
Thus any polynomial which vanishes at $\sqrt[3]{2}$ also has $\alpha$ and $\beta$ as roots!

You can generalize this by replacing $\mathbb Q$ with any field and all of this still works.
One central idea of Galois theory is that these "conjugates" all "look the same"
as far as $\mathbb Q$ can tell.

As another aside: does the minimal polynomial exist for every $\alpha$?
It turns out the answer is no,
and the numbers for which there is no minimal polynomial are called the
[transcendental numbers](http://en.wikipedia.org/wiki/Transcendental_number).
