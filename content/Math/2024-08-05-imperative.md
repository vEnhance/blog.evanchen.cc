---
title: Imperative statements in geometry don't matter
date: 2024-08-05 13:37
slug: imperative
tags: math, olympiad
original_url: 2024/08/05/imperative/
status: published
---

There's this pet peeve I have where people sometimes ask things like what kind
of strategies they should use for, say, collinearity problems in geometry.

Like, I know there are valid answers like Menelaus or something.
But the reason it bugs me is because "the problem says to prove collinearity"
is about as superficial as it gets.
It would be like asking for advice for problems that have "ABC" in them.

To drive my point, consider the following setup:

Let $ABC$ be a triangle with circumcircle $\Gamma$
and incenter $I$ and let $M$ be the midpoint of $\overline{BC}$.
Denote by $D$ the foot of the perpendicular from $I$ to $\overline{BC}$.
The line through $I$ perpendicular to $\overline{AI}$ meets
sides $AB$ and $AC$ at $F$ and $E$ respectively.
Suppose the circumcircle of $\triangle AEF$
intersects $\Gamma$ at a point $X$ other than $A$.

Then the following problem statements are all trivially equivalent:

1. Prove that lines $XD$ and $AM$ meet on $\Gamma$.

2. Line $XD$ meets $\Gamma$ again at $K$.
   Prove that $A$, $M$, $K$ are collinear.

3. Line $AM$ meets $\Gamma$ again at $K$.
   Prove that $X$, $D$, $K$ are collinear.

4. Line $AM$ meets $\Gamma$ again at $K$.
   Prove that line $XK$, line $BC$, and the line
   through $I$ perpendicular to $\overline{BC}$ are concurrent.

5. Line $AM$ and $XD$ meet at $K$.
   Prove that $A$, $B$, $K$, $C$ are concyclic.

Which is why any advice based on just which keywords are appearing in the
problem is likely next to useless, because it can't distinguish
between cosmetic rephrasings of the problem.
