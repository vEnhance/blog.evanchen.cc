---
title: NP-hard advice questions
date: 2024-02-04 13:37
slug: np-hard-advice
tags: advice, teaching
original_url: 2024/02/04/np-hard-advice-questions/
status: published
---

Sometimes I get asked broad advice questions on solving problems, for example
questions like:

1. How do I know when to switch or prioritize approaches I come up with?
2. How do I know which points or lines to add in geometry problems?
3. How can I tell if I'm making progress on a problem?
4. How can I guess the answer if "find all" or "find min/max" problems?
5. How can I tell whether a conjecture I made is true or not?
6. What should I do on a problem when I am stuck?

and so on.

I think all of these questions have a certain quality that, for lack of a better
name, I'll dub as being "_NP-hard_".
This is a bit of abuse of terminology borrowed from
[complexity theory](https://en.wikipedia.org/wiki/NP-hardness),
but let me explain why I think the name fits.

We know that solving math problems is generally difficult.
There's no surefire way to take a math problem, even one that's simply stated,
and generate a solution to it.
If we take that as given, one corollary of that is the above questions
should _also_ not have simple surefire answers, by _reductio ad absurdum_;
if you could come up with algorithms to answer the above questions,
you would now have a recipe for solving problems in general.[^np]

[^np]:
    This matches what the term NP-hardness means in theoretical CS.
    Roughly, a problem is NP-hard if an efficient way to answer it
    would lead to efficient ways to answer other NP problems as well.

But this doesn't imply that nothing[^analogy]
can be said about questions like the ones above.
It just means there is no _simple complete answer_
(besides truisms like "it varies by problem" or "rely on experience").
But there can still be, e.g.

- useful heuristics or "rules of thumb" that work some of the time;
- ways to answer the question is specific cases;
- most importantly, you can get better at these skills with practice;
  lots of experience will give you more accurate instincts.

[^analogy]:
    We can continue the analogy to theoretical CS with the concept of
    [approximation algorithms](https://w.wiki/8x5M).
    In an NP-hard problem, even when we don't expect to be able to
    find an exact answer easily; we can still get some estimates.
    Or, the [knapsack problem](https://w.wiki/8x5P) might be NP-hard in general,
    but a lot of special cases (like when the weights are superincreasing,
    or a "randomly generated" instance)
    can still be solved exactly.

I created this blog post so that I could start linking it to describe
what I mean by "NP-hard" when I get a question like this.
Here's my concrete advice for this situation:
**if you ask one of these questions, do at the level of specific examples**.
So, rather than ask "how do I know which point to add in geometry problems?",
you would be much better off asking "how should I have known to
add the points $X$, $Y$, $T$ in IMO 2019/2?"[^imo19],
and repeating this across other geometry problems
for which you have the same question.

The analogous strategy can help people trying to give convincing advice.
One cannot give an adequate answer to NP-hard questions that always work.
So rather than try to describe an abstract recipe,
it's more useful to a reader to see specific well-chosen examples,
letting them update their instincts through that experience.
In literary terms: [show, don't tell](https://w.wiki/8x5z).

[^imo19]:
    This real-life example comes from my solution in
    [my IMO 2019 write-up](https://web.evanchen.cc/exams/IMO-2019-notes.pdf).
    Since someone is going to invariably ask in the comments:
    the reason for introducing these points is to eliminate
    both $P_1$ and $Q_1$ and the weird angle conditions in one stroke.
    The points $X$ and $Y$ anchor the angle condition into the
    cyclic quadrilaterals $P_1CXA$ and $Q_1CYB$,
    while changing the goalpost to showing $P_1XYQ_1$ is cyclic.
    But then power of a point again changes the goal post to showing
    $T = \overline{PX} \cap \overline{QY}$
    lies on the radical axis of $(AXC)$ and $(BYC)$.
    And now the points $P_1$ and $Q_1$ can be safely deleted from the problem,
    leaving a statement that doesn't involve any circles anymore,
    which is much better.
