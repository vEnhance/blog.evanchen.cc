Title: Some Advice for Olympiad Geometry
Date: 2016-01-19 13:37
Tags: geometry, olympiad
Slug: geo-advice
Status: published
original_url: 2016/01/19/some-advice-for-olympiad-geometry/

I know some friends who are fantastic at synthetic geometry.
I can give them any problem and they'll come up with an incredibly impressive synthetic solution.
I also have some friends who are very bad at synthetic geometry,
but have such good fortitude at computations that they can get away with using
Cartesian coordinates for everything.

I don't consider myself either of these types; I don't have much ingenuity when it comes to my solutions,
and I'm actually quite clumsy when it comes to long calculations.
But nonetheless I have a high success rate with olympiad geometry problems.
Not only that, but my solutions are often very _algorithmic_,
in the sense that any well-trained student should be able to come up with this solution.

In this article I try to describe how I come up which such solutions.

## 1. The Three Reductions

Very roughly, there are three different ways I try to make progress on a geometry problem.

- (I) The standard **synthetic** techniques; angle chasing, cyclic quadrilaterals, homothety,
  radical axis / power of a point, etc.
  My own personal arsenal contains some weapons not known to many contestants as well,
  most notably inversion, harmonic bundles and quadrilaterals,
  and spiral similarity / Miquel points.For this part,
  it's highly advantageous to be well-versed with "standard" configurations and tricks.
  To give an extreme example: to solve [Iran TST 2009,
  Problem 9](https://aops.com/community/c6h594766p3530598) one
  essentially needs only recognize two configurations:
  a lemma about the midpoint of an altitude (2002 G7) and another lemma about the line $EF$ (USAJMO 2014/6).
  Not knowing either of these makes it more difficult to solve the problem synthetically in the time limit.
  As a reference, [Yufei Zhao's lemmas
  handout](https://yufeizhao.com/olympiad/geolemmas.pdf) contains a fairly
  comprehensive list of these configurations.

  Easier problems don't require as much in this way of configuration recognition.

- (II) Standard **computational** techniques (aka bashing).
  Personally, I prefer complex numbers and barycentric coordinates but I know
  other students who will use Cartesian coordinates and trigonometry to great success.
  The advantage of such methods is that they are **straightforward** and **reliable**,
  albeit tedious and time-consuming.
  It is mostly a matter of experience to understand whether a calculation can be
  carried out within the time limit -- I can basically tell just by looking at a
  setup whether it can be solved in this time.

- (III) Most surprisingly: simply **finding crucial claims**.
  Especially for harder problems like IMO 3/6 much of the time the key to
  solving a problem is making some key observation.
  Said another way: a difficult IMO 3/6 problem which asks you to prove
  $A \implies B$ might have a solution which goes like,

  $$A \implies X \implies Y \implies B.$$
  Each of the individual implications might be no harder than an IMO 1/4 but the
  difficulty rests in finding what to prove.
  The most reliable way to do such things is to draw **large, in-scale diagrams**.
  If you are good at recognizing cyclic quadrilaterals, collinear points, etc.
  then the correct claims will naturally suggest themselves; conversely,
  good diagrams will prevent you from wasting time trying to prove things that
  aren't true (effectively letting you test your claims "experimentally" before trying to prove them).

Type (III) deserves some comment here.
There is more to making progress on a problem than simply trying things you think will solve the problem:
there is some "scouting" involved that you will need to do for any difficult problems.
As a terrible analogy, in StarCraft you have to scout an experienced opponent to
understand what they're doing before you try to attack them.
The situation with IMO 3/6 is no different:
you have to have some understanding of the problem before you stand a chance of being able to solve it.

Easy problems can often succumb to just one class of attacks,
but the interesting and difficult problems can require two or all three classes in order to solve.
How much you use each type of strategy is in my opinion a matter of personal
taste -- some people don't use (II) at all and rely on (I) to prove everything, and even vice versa!
I like to think I balance (I) and (II) evenly.
But (III) is indispensable, and in any case I think part of the reason I have
been so successful with geometry problems is precisely that I can draw on all three strategies in tandem,
rather than being limited to one or two.

In fact, a good rule of thumb that I use for judging the difficulty of a problem
is how many of the above methods I had to use:
the $n$-th problem on an IMO paper should require me to resort to about $n$ of these strategies.

## 2. Concrete Examples

I'll now give some concrete examples of the things I said above.
Warning: spoilers follow, and hyperlinks lead to my solutions on Art of Problem Solving.
You are encouraged to try the problems yourself before reading the comments.

> **Example** ([EGMO 2012/1](https://aops.com/community/p2658992)). Let $ABC$ be a
> triangle with circumcenter $O$.
> The points $D$, $E$, $F$ lie in the interiors of the sides $BC$, $CA$, $AB$ respectively,
> such that $\overline{DE}$ is perpendicular to $\overline{CO}$ and
> $\overline{DF}$ is perpendicular to $\overline{BO}$. Let $K$ be the circumcenter of triangle $AFE$.
> Prove that the lines $\overline{DK}$ and $\overline{BC}$ are perpendicular.

This is a pretty typical entry-level geometry problem.
Do some angle chasing (I) to find one cyclic quad (III), and then follow through to solve the problem (I).
If you are good enough, you don't even need to find the cyclic quad in advance;
just play around with the angles until you notice it.

> **Example** ([IMO 2014, Problem 4](https://aops.com/community/h597090)). Let $P$ and $Q$ be on
> segment $BC$ of an acute triangle $ABC$ such that $\angle PAB=\angle BCA$ and $\angle CAQ=\angle ABC$.
> Let $M$ and $N$ be the points on $AP$ and $AQ$, respectively,
> such that $P$ is the midpoint of $AM$ and $Q$ is the midpoint of $AN$.
> Prove that the intersection of $BM$ and $CN$ is on the circumference of triangle $ABC$.

You can solve this problem by barycentric coordinates (II) instantly (textbook example).
Also similar triangles (I) solves the problem pretty quickly as well.
Again, this problem is "easy" in the sense that one can directly approach it with either (I) or (II),
not needing (III) at all.

> **Example** ([USAMO 2015/2](https://aops.com/community/c5h1083097p4769957)). Quadrilateral
> $APBQ$ is inscribed in circle $\omega$ with $\angle P = \angle Q = 90^{\circ}$ and $AP = AQ < BP$.
> Let $X$ be a variable point on segment $\overline{PQ}$.
> Line $AX$ meets $\omega$ again at $S$ (other than $A$).
> Point $T$ lies on arc $AQB$ of $\omega$ such that $\overline{XT}$ is perpendicular to $\overline{AX}$.
> Let $M$ denote the midpoint of chord $\overline{ST}$.
> As $X$ varies on segment $\overline{PQ}$, show that $M$ moves along a circle.

This was not supposed to be a very difficult problem, but it seems to have nearly swept the JMO group.
Essentially, the key to this problem is to notice that the center of the desired
circle is in fact the midpoint of $AO$ (with $O$ the center of the circle).
This is a huge example of (III) -- after this observation,
one can solve the problem very quickly using complex numbers (II).
It is much harder (though not impossible) to solve the problem without knowing the desired center.

> **Example** ([USAMO 2014/5](https://aops.com/community/c5h587672p3478581)). Let $ABC$ be
> a triangle with orthocenter $H$ and let $P$ be the second intersection of the
> circumcircle of triangle $AHC$ with the internal bisector of the angle $\angle BAC$.
> Let $X$ be the circumcenter of triangle $APB$ and $Y$ the orthocenter of triangle $APC$.
> Prove that the length of segment $XY$ is equal to the circumradius of triangle $ABC$.

Personally I think the most straightforward solution is to use (I) to eliminate the orthocenter condition,
and then finish with complex numbers (II).
Normally, you won't see a medium-level problem that dies immediately to (II),
and the only reason a problem like this could end up as a problem 5 is that
there is a tiny bit of (I) that needs to happen before the complex numbers becomes feasible.

> **Example** ([IMO 2014/3](https://aops.com/community/c6h596927p3542092)). Convex quadrilateral
> $ABCD$ has $\angle ABC = \angle CDA = 90^{\circ}$.
> Point $H$ is the foot of the perpendicular from $A$ to $BD$.
> Points $S$ and $T$ lie on sides $AB$ and $AD$, respectively, such that $H$ lies inside triangle $SCT$ and
>
> $$\angle CHS - \angle CSB = 90^{\circ}, \quad \angle THC - \angle DTC = 90^{\circ}.$$
>
> Prove that line $BD$ is tangent to the circumcircle of triangle $TSH$.

Like most IMO 3/6's I had to resort to using all three methods in order to solve this problem.
The first important step was finding out what to do with the angle condition.
It turns out that in fact, it's equivalent to the circumcenter of triangle $TCH$
lying on side $AD$ of the triangle (III); proving this is then a matter of angle chasing (I).
Afterwards, one has to recognize a tricky usage of the angle bisector theorem
(I) to reduce it to something that can be computed with trigonometry (II).
This leads to a direct solution that, while not elegant,
also requires much less ingenuity then most of the solutions found by friends I know.

I really want to stress that being proficient in all three strategies is key to
getting "straightforward" solutions like this to IMO 3/6 caliber problems.
If you miss any of these components, you are not going to solve the problem.

> **Example** ([IMO 2011/6](https://aops.com/community/c6h418983p3518149)). Let $ABC$ be an
> acute triangle with circumcircle $\Gamma$.
> Let $\ell$ be a tangent line to $\Gamma$, and let $\ell_a$, $\ell_b$,
> $\ell_c$ be the lines obtained by reflecting $\ell$ in the lines $BC$, $CA$, and $AB$, respectively.
> Show that the circumcircle of the triangle determined by the lines $\ell_a$, $\ell_b$,
> and $\ell_c$ is tangent to the circle $\Gamma$.

The ultimate example of these three principles.
Using a trick that showed up on APMO 2014/5 and RMM 2013/3,
one constructs the tangency point $T$ and connects the points $A_1$, $B_1$, $C_1$,
as I explain in [this post](https://aops.com/community/c6h594766p3530598),
yielding points $A_2$, $B_2$, $C_2$.
After that, a very careful examination of the diagram (possibly several
diagrams) leads to a conjecture that $A_1A=AP$, et cetera.
This is the key observation (III), and leads to highly direct solution via (II).
But the point of this problem is that you need to _have the guts_ to construct
those auxiliary points and then boldly claim they are the desired "squared" points.

## 3. Comparison with Other Subjects

The approaches I've described highlight some of the features of olympiad
geometry which distinguish it from other subjects.

- Unlike other olympiad subjects, you can actually obtain a big advantage by just knowing lots of theory.
  Experienced contestants simply "recognize" a large body of common
  configurations that those without access to training materials have never seen before.
  Similarly, there are a lot of fancy techniques that can make a big difference.
  This is much less true of other subjects (for example combinatorics is the opposite extreme).
- There's less variance in the subject: lots of Euclidean geometry problems feel the same,
  and all of them use the same body of techniques.
  It reminds me of chess: it's very "narrow" in the sense that at the end of the day,
  there are only so many possible moves.
  (Olympiad inequalities also has this kind of behavior.) Again combinatorics is the opposite of this.
- You have a reliable backup in case you can't find the official solution: bash.
  Moreover, in general there are often many different ways to solve a problem; not true of other subjects.
- If you want to make some "critical claim" you can quickly test it empirically (by drawing a good diagram).
