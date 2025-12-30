Title: Hard and soft techniques
Date: 2019-05-03 13:37
Tags: math, olympiad
Slug: hard-and-soft
Status: published
original_url: 2019/05/03/hard-and-soft-techniques/

In yet another contest-based post,
I want to distinguish between two types of thinking:
things that could help you solve a problem,
and things that could help you understand the problem better.
Then I'll talk a little about how you can use the latter.
(I've talked about this in my own classes for a while by now,
but only recently realized I've never gotten the whole thing in writing. So here goes.)

## 1. More silly terminology

As usual, to make these things easier to talk about, I'm going to introduce some words to describe these two.
Taking a page from martial arts, I'm going to run with **hard** and **soft** techniques.

A **hard** technique is something you try in the hopes it will prove something
--- ideally, solve the problem, but at least give you some intermediate lemma.
Perhaps a better definition is "things that will end up in the actual proof".
Examples include:

- Angle chasing in geometry, or proving quadrilaterals are cyclic.
- Throwing complex numbers at a geometry problem.
- Plugging in some values into a functional equation (which gives more equations to work with).
- Taking a given Diophantine equation modulo $p$ to get some information, or taking $p$-adic evaluations.
- Trying to perform an induction, for example by deleting an element.
- Trying to write down an inequality that when summed cyclically gives the desired conclusion.
- Reducing the problem to one or more equivalent claims.

and so on. I'm sure you can come up with more examples.

In contrast, a **soft** technique is something you
might try to help you understand the problem better --- even if it might not prove anything.
Perhaps a better definition is "things not written up". Examples include:

- Examining particular small cases of the problem.
- Looking at the equality cases of a min/max problem.
- Considering variants of the problem (for example, adding or deleting conditions).
- Coming up with lots of concrete examples and playing with them.
- Trying to come with a counterexample to the problem's assertion and seeing what the obstructions are.
- Drawing pictures, even on non-geometry problems (see JMO2 and JMO5 in my [2019
  notes](http://web.evanchen.cc/exams/JMO-2019-notes.pdf) for example).
- Deciding whether or not a geometry problem is "purely projective".
- Counting the algebraic degrees of freedom in a geometry problem.
- Checking all the linear/polynomial solutions to a functional equation,
  in order to get a guess what the answer might be.
- Blindly trying to guess solutions to an algebraic equation.
- Making up an artificial unnatural function in a functional equation,
  and then trying to see why it doesn't work
  (or occasionally being surprised that it does work).
- Thinking about why a certain hard technique you tried failed,
  or even better convincing yourself it cannot work
  (for example, this Diophantine equation has a solution modulo every prime,
  so stop trying to one-shot by mods).
- Giving a heuristic argument that some claim should be true or false
  ("probably $2^n \bmod n$ is odd infinitely often"), or even easy/hard to prove.

and so on. There is some grey area between these two,
some of the examples above might be argued to be in the other category
(especially in context of specific problems), but hopefully this gives you a sense of what I'm talking about.

If you look at things I wrote back when I was in high school,
you'll see this referred to as "attacking" and "scouting" instead.
This is too silly for me now even by my standards, but back then it was because I played a lot of _StarCraft:
Brood War_ (I've since switched to StarCraft II).
The analogy there is pretty self-explanatory:
knowing what your opponent is doing is important because your army composition
and gameplay decisions should change in reaction to more information.

## 2. Using soft techniques: an example

Now after all that blabber, here's the action item for you all: **you should try soft techniques when stuck**.

When you first start doing a problem, you will often have some good ideas for what to try.
(For example: a wild geometry appeared,
let's scout for cyclic quadrilaterals.) Sometimes if you are lucky enough
(especially if the problem is easier) this will be enough to topple the problem, and you can move on.
But more often what happens is that eventually you run out of steam, and the problem is still standing.
When that happens, my advice is to try doing some soft techniques if you haven't already done so.

Here's an example that I like to give.

> **Example 1** **(USA TST 2009)**
>
> Find all real numbers $x$, $y$, $z$ which satisfy
>
> $$\begin{aligned} x^3 &= 3x - 12y + 50,\\ y^3 &= 12y + 3z - 2,\\ z^3 &= 27z + 27x. \end{aligned}$$

A common first thing that people will try to do is add the first two equations,
since that will cause the $12y$ terms to cancel.
This gives a factor of $x+y$ in the left and an $x+z$ in the right,
so then maybe you try to submit that into the $27(x+z)$ in the last equation,
so you get $z^3 = 9(x^3+y^3-48)$, cool, there's no more linear terms. Then...

Usually this doesn't end well.
You add this and subtract that and in the end all you see is equation after equation,
and after a while you realize you're not getting anywhere.

So we're stuck now. What to do? I'll now bring in two of the soft techniques I mentioned earlier:

1.  Let's imagine the problem had $\mathbb R$ replaced with $\mathbb C$.
    In this new problem, you can _imagine_ solving for $y$ in terms of $x$ using the first equation, then $z$ in terms of $y$,
    and then finally putting everything into the last equation to find a degree $27$ polynomial in $x$.
    I say "imagine" because wow would that be ugly.

But here's the kicker: it's a polynomial.
It should have exactly $27$ complex roots, with multiplicity.
That's a lot. Really?

So here's a hint you might take:
there's a good reason this is over $\mathbb R$ but not $\mathbb C$.
Often these kind of things end up being because there's an inequality going on somewhere,
so there will only be a few real solutions even though there might be tons of complex ones.

2.  Okay, but there's an even more blatant thing we don't know yet: _what is the answer, anyways_?

    This was more than a little bit embarrassing.
    We're half an hour in to the problem and thoroughly stuck, and we don't even have a single $(x,y,z)$ that works?
    Maybe it'd be a good idea to fix that, like, _right now_.
    In the simplest way possible: guess and check.

    It's much easier than it sounds, since if you pick a value of $z$,
    say, then you get $x$ from the third equation, $y$ from the first,
    then check whether it fits the second.
    If we restrict our search to integer values of $z$,
    then there aren't so many that are reasonable.

I won't spoil what the answer $(x,y,z)$ is,
other than saying there is an integer triple and it's not hard to find it as I described.
Once you have these two meta-considerations, you suddenly have a much better foothold,
and it's not too hard to solve the problem from here (for a USA TST problem anyways).

I pick this example because it really illustrates how hopeless
repeatedly using hard techniques can be if you miss the right foothold
(and also because in this problem it's unusually tempting to just think that more manipulation is enough).
It's not _impossible_ to solve the problem without first realizing what the answer is,
but it is certainly way more difficult.

## 3. Improving at soft techniques

What this also means is that, in the after-math of a problem
(when you've solved or given up on a problem and are reading and reflecting on the solution),
you should also add soft techniques into the list of possible answers to "how might I have thought of that?".
An example of this is at the end of my earlier post
[On Reading Solutions](https://blog.evanchen.cc/2017/03/06/on-reading-solutions/),
in which I describe how you can come up with solutions to two Putnam problems
by thinking carefully about what should be the equality case.

Doing this is harder than it sounds,
because the soft techniques are the ones that by definition won't appear in most written solutions,
and many people don't explicitly even recognize them.
But soft techniques are the things that tell you which hard techniques to use,
which is why they're so valuable to learn well.

In writing this post, I'm hoping to make the math contest world more aware
that these sorts of non-formalizable ideas are things that can (and should) be acknowledged and discussed,
the same way that the hard techniques are.
In particular, just as there are a plethora of handouts on every hard technique in the olympiad literature,
it should also be possible to design handouts aimed at practicing one or more particular soft techniques.

At MOP every year, I'm starting to see more and more classes to this effect
(alongside the usual mix of classes called "inversion" or "graph theory" or "induction" or whatnot)
. I would love to see more! End speech.
