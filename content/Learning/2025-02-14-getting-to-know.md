---
title: Getting to know problems
date: 2025-02-14 13:37
slug: getting-to-know
tags: math, study, teaching
original_url: 2025/02/14/getting-to-know-problems/
status: published
---

I recently had a student writing to me asking for advice on problem-solving. The
student gave a few examples of problems they didn't solve (like I
[tell people to](https://web.evanchen.cc/contact.html#advice)). One of the
things that struck me about the message was their description of their work on
[USAMO 2021/4](https://aops.com/community/p21498580), whose statement reads:

> A finite set $S$ of positive integers has the property that,
> for each $s\in S$, and each positive integer divisor $d$ of $s$,
> there exists a unique element $t\in S$ satisfying $\gcd(s,t) = d$.
> (The elements $s$ and $t$ could be equal.)
> Given this information, find all possible values for the
> number of elements of $S$.

Roughly (for privacy reasons, this isn't exactly what the student said),
the student talked about having done small cases on the size $|S|$,
and figuring out that $|S|$ was even, but then running out of ideas.
They gave a few other examples of problems that had a similar issue
where they tried some stuff and then just ran out of ideas.

I ended up writing a long email in response that I thought might be interesting
to the high schoolers reading this blog, so here it is.

(begin quote)

I get the feeling that you are rushing to try to guess the solution to the
problem rather than getting to know the problem better. For example, for the
sets problem, trying to do cases by the number of elements in $S$ is actually
extremely unnatural. You really should be much more interested in the question
"what's a set satisfying this look like? Can I give any examples at all? Can I
find a way to _generate_ big examples?" and so on. However, you got so latched
on to what the extraction was (the number of elements in the set) that it feels
like you stopped trying to engage your curiosity ("all the while, I did not
think about the condition of the problem"). I don't know how to explain it but
trying to do $|S|=1,2,3,4,5$ in order just feels so obviously wrong to me that
it wouldn't even occur to me consider this. When I see a condition like this, my
reaction is more like "is that even usually possible" and "what would that even
look like", both because it's a pretty abstract condition (I immediately want to
see concrete examples) and because it's requiring so much (it's a requirement on
_every_ $s$ _and then_ every $d$ dividing $s$: double for-all).

Here's a silly analogy I just thought of (experimental analogy, so don't take it
too seriously --- also, as I said I don't actually know how to make this
actionable advice, it's just a description).

You can imagine maybe you're going on a first date with someone. Sure, there's
eventually a checklist of things that you probably should know, like what major
they are, where they're from, what their phone number is, etc. But it's not a
criminal investigation where you go off a list of questions and write the
answers in a list (see 1:00-1:40 of
[this scene from SVTFOE](https://youtu.be/ztV4Th6HYLc?&t=58)). It's supposed to
be a conversation that flows naturally back and forth where you get to know the
other person better because you're genuinely interested in them.

Problem-solving is like that. It should follow your natural curiosity ("I want
to know what's going on" not "I want the solution asap"). And it should go back
and forth (when you try something, you get more information than just "did it
work"). "Promptly running out of ideas" is like promptly running out of
conversation during a first date. It might sometimes happen if you and the other
person just don't have chemistry (for example if you're trying to solve [USA TST
2025/3](https://aops.com/community/p33455239) without the right background
knowledge), but if it happens all the time you're not doing first dates
correctly.

([TSTST 2013/7](https://aops.com/community/p3181485) is an anti-example where
actually the way to solve the problem is to pay the bill and leave ASAP. Don't
even try to count $T_n$ because it's so obviously impossible. Just find a method
that gives you groups of $n$.)

(end quote)
