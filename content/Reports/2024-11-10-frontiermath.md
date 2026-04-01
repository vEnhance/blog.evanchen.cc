---
title: FrontierMath
date: 2024-11-10 13:37
slug: frontiermath
tags: math, problem writing
original_url: 2024/11/10/frontiermath/
status: published
---

This is a short blog post on the [FrontierMath benchmark][fmarxiv],
a set of lots of difficult math problems with easily verifiable answers.
Just to be clear, everything written here is my own thoughts
and doesn't necessarily reflect the intention of any collaborators.

When you're setting a problem for a competition like the IMO or Putnam,
three properties that are often considered desirable are:

1. It should require **creative insight**.
   Competitions avoid problems that are too similar to existing ones
   or too easily solved by simply applying standard textbook techniques.
   You want the problems to really feel different
   and force the solver to feel like they came up with a new idea to solve it.
   This is sort of what the spirit of math olympiads is about.

2. It should not take a lot of **implementation**,
   i.e. once a set of key ideas has been identified,
   actually carrying out the proof or calculation should not be too difficult.
   This is because a human is supposed to solve these problems
   with nothing but pencil and paper.

3. It should be **elementary**, that is, it should not rely on heavily
   specialized esoteric knowledge. The statement should be accessible
   to anyone with a high school or undergraduate background,
   and the solution shouldn't be based on high-powered tools.
   References and web search are inaccessible to human contestants.

The FrontierMath benchmark does something different from the IMO and Putnam,
which is that **they keep the first requirement, but outright invert the second
and third requirement**. That is, a problem in the FrontierMath benchmark
_should_ test for insight rather than just standard techniques or knowledge, but
is _also_ imagined the solver has access to a Python console and a lot of
reference text it can look at. So the problem authors don't pull punches on any
of these three axes. This makes sense: an AI system working on difficult
problems does indeed have access to computational resources and can "look things
up" in its training data.

And because of this, the FrontierMath benchmark is able to get away with
something that the IMO cannot: problems that only require a short verifiable
answer. Many IMO problems do not have an "answer"; those that do
typically have answers that are easy to guess but hard to prove.
That's fine for human contestants whose proofs are then evaluated
by IMO coordinators such as yours truly.
But because an AI system has vastly greater computational power,
it's actually possible to design problems with easily verifiable solutions
using the same idea that [IOI](https://ioinformatics.org/)
or [Project Euler](https://projecteuler.net/) does ---
basically, "write a proof" is replaced by "implement an algorithm in code".
This added capability makes it possible to design genuinely serious problems
with still easily checkable answers in a way pencil-and-paper contests cannot.
This is of course not a perfect replacement,
but based on what I saw the organizers were pretty ruthless about
rejecting problems for which they felt it was possible to guess the answer
with [engineer's induction](https://cjquines.com/files/engineering.pdf).

If you want to get a sense of the problems on the benchmark,
[Appendix A of the paper][fmarxiv] has some randomly selected sample problems
for nerd-sniping reasons, one from each difficulty tier of the benchmark.
You can judge for yourself how hard you think the problems are from that.
(EpochAI also posted
[a video on Twitter](https://x.com/EpochAIResearch/status/1854996368814936250)
if that's your kind of thing.
But for most people reading this blog, I imagine
looking at the actual sample problems will probably be much more informative
than the lights-and-camera presentation for the public.)

[fmarxiv]: https://arxiv.org/abs/2411.04872
