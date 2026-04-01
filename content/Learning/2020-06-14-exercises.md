---
title: On choosing exercises
date: 2020-06-14 13:37
slug: exercises
tags: math, teaching
original_url: 2020/06/14/on-choosing-exercises/
status: published
---

> Finally, if you attempt to read this without working through a significant
> number of exercises (see §0.0.1), I will come to your house and pummel you
> with \[Gr-EGA\] until you beg for mercy. It is important to not just have a
> vague sense of what is true, but to be able to actually get your hands dirty.
> As Mark Kisin has said, "You can wave your hands all you want, but it still
> won’t make you fly."
>
> --- Ravi Vakil, [The Rising Sea:
> Foundations of Algebraic Geometry](http://math.stanford.edu/~vakil/216blog/index.html)

When people learn new areas in higher math,
they are usually required to do some exercises.
I think no one really disputes this: you have to actually _do_ math to make any progress.

However, from the teacher's side,
I want to make the case that there is some art to picking exercises, too.
In the process of writing my [Napkin](http://web.evanchen.cc/napkin.html)
as well as [taking way too many math classes](http://web.evanchen.cc/upload/math-coursework.pdf)
I began to see some patterns in which exercises or problems I tended to add to the Napkin,
or which exercises I found helpful when learning myself.
So, I want to explicitly record some of these thoughts here.

## 1. How not to do it

So in my usual cynicism I'll start by saying what I _think_ people typically do,
and why I don't think it works well.
As far as I can tell, the criteria used in most classes is:

1.  The student is reasonably able to (at least in theory) eventually solve it.
2.  A student with a solid understanding of the material should be able to do it.
3.  (Optional) The result itself is worth knowing.

Both of these criteria are good. My problem is that I don't think they are sufficient.

To explain why, let me give a concrete example of something
that is definitely assigned in many measure theory classes.

> **Okay example** (completion of a measure space).
> Let $(X, \mathcal A, \mu)$ be a measure space.
> Let ${\overline{\mathcal A}}$ denote all subsets of $X$
> which are the union of a set in $\mathcal A$ and a null set.
> Show that ${\overline{\mathcal A}}$ is a sigma-algebra
> there is a unique extension of the measure $\mu$ to it.

I can see why it's tempting to give this as an exercise.
It is a very fundamental result that the student should know.
The proof is not too difficult, and the student will understand it better
if they do it themselves than if they passively read it.
And, if a student really understands measures well,
they should find the exercise quite straightforward.
For this reason I think this is an _okay_ choice.

But I think we can do better.

In many classes I've taken, nearly all the exercises looked like this one.
I think when you do this, there are a couple blind spots that sometimes get missed:

- There's a difference between "things you should be able to do _after learning Z well_"
  and "things you should be able to do _when first learning Z_".
  I would argue that the above example is the former category,
  but not the latter one --- if a student is learning about measures for the first time,
  my first priority would be to make sure they get a good conceptual understanding first,
  and in particular can understand _why_ the statement _should be true_.
  Then we can worry about actually proving it.
- Assigning an exercise which checks if you understand
  X is not the same as actually teaching it.
  Okay exercises can _verify_ if you understand something,
  great exercises will _actively help you_ understand it.

## 2. An example that I found enlightening

In contrast, this year I was given an exercise which I thought was
so instructive that I'll post it here. It comes from algebraic geometry.

> **Exercise**: The _punctured gyrotop_ is the open subset $U$ of
> $$X = \operatorname{Spec}(\mathbb C[x,y,z] / (xz, yz))$$
> obtained by deleting the origin $(x,y,z)$ from $X$. Compute $\mathcal O_X(U)$.

It was after I did this exercise that I finally felt like
I understood why distinguished open sets are so important when defining an affine scheme.
For that matter, it finally clicked why sheaves on a base are worth caring about.

I had read lots and lots of words and pushed symbols around all day.
I had even proved, on paper already, that $\mathcal O(U \sqcup V) = \mathcal O(U) \times \mathcal O(V)$.
But I never really felt it. This exercise changed that for me,
because suddenly I had an example in front of me that I could actually see.

## 3. Some suggested additional criteria

So here are a few suggested guidelines which I think can help pick exercises like that one.

### A. They should be as concrete as possible.

This is me yelling at people to use more examples, once again.
But I think having students work through examples as an exercise
is just as important (if not more) than reading them aloud in lecture.

One other benefit of using concrete examples is that you can
**avoid the risk of students solving the exercise by "symbol pushing"**.
I think many of us know the feeling of solving some textbook exercise
by just unwinding a definition and doing a manipulation,
or black-boxing some theorem and blindly applying it.
In this way one ends up with correct but unenlightening proofs.
The issue is that nothing written down resonates with
[System 1](https://blog.evanchen.cc/sys1/),
and so the result doesn't get internalized.

When you give a concrete exercise with a specific group/scheme/whatever,
there is much less chance of something like that happening.
You almost _have_ to see the example in order to work with it.
I really think internalizing theorems and definitions is better done in this concrete way,
rather than the more abstract or general manipulations.

### B. They should be enjoyable.

Math majors are humans too.
If a whole page of exercises looks boring, students are less likely to do them.

This is one place where I think people could really learn from the math contest community.
When designing exams like IMO or USAMO, people _fight_ over which problems they think are the prettiest.
The nicest and most instructive exam problems are passed down from generation to
generation like prized heirlooms.
(Conveniently, the problems are even named, e.g. "IMO 2008/3", which I privately think helps a _ton_;
it gives the problems a name and face.
The most enthusiastic students will often be able to recall where a good problem
was from if shown the statement again.)
Imagine if the average textbook exercises had even a tenth
of that enthusiasm put into crafting them.

Incidentally, I think being concrete helps a lot with this.
Part of the reason I enjoyed the punctured gyrotop so much was that
I could immediately draw a picture of it,
and I had a sense that I should be able to compute the answer,
even though I wasn't experienced enough yet to see what it was.
So it was as if the exercise was leading me on the whole way.

For an example of how _not_ to do it, [here's what I think my geometry book
would look like if done wrong](http://web.evanchen.cc/textbooks/tr011ey.pdf).

### C. They should not be too tricky.

People are always dumber than you think when they first learn a subject;
things which should be obvious often are not.
So difficulty should be used in moderation: if you assign a hard exercise,
you should assume by default the student will not solve it,
so there better be some reason you're adding some extra frustration.

I should at this point also mention some advice most people won't be able to take
(because it is so time-consuming): I think it's valuable to write full solutions for students,
especially on difficult problems.
When someone is learning something for the first time,
that is the _most important_ time for the students to be able to read the full details of solutions,
precisely because they are not yet able to do it themselves.

In math contests, the ideal feedback cycle is something like:
a student works on a problem P, makes some progress (possibly solving it),
then they look at the solution and see what they were missing
or where they could have cleaned up their solution or what they could have done differently, et cetera.
This lets them update their intuition or toolkit before going on.
If you cut out this last step by not providing solutions,
you lose the only real chance you had to give feedback to the student.

## 4. Memorability

I have, on more occasions than I'm willing to admit, run into the following situation.
I solve some exercise in a textbook.
Sometime later, I am reading about some other result,
and I need some intermediate result,
which looks like it could be true but I don't how to prove it immediately.
So I look it up, and then find out it was the exercise I did
(and then have to re-do the exercise again because I didn't write up the solution).

I think you can argue that if you don't even _recognize_ the statement later,
you didn't learn anything from it.
So I think the following is a good summarizing test:
_how likely is the student to actually remember it later?_
