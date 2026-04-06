---
title: Book pitch
date: 2021-08-16 13:37
slug: book-pitch
tags: math, teaching
original_url: 2021/08/16/book-pitch/
status: published
---

This is a pitch for a new text that I'm thinking of writing.
I want to post it here to solicit opinions from the general community before
investing a lot of time into the actual writing.

## Summary

There are a lot of students who ask me a question isomorphic to:

> How do I learn to write proofs?

I've got this on my Q&A. For the contest kiddos out there,
it basically amounts to saying "read the official solutions to any competition".

But I think I can do better.

## Requirements

> Calling into question the obvious, by insisting that it be "rigorously proved", is to say to a student,
> "Your feelings and ideas are suspect. You need to think and speak our way."
>
> Now there is a place for formal proof in mathematics, no question.
> But that place is not a student’s first introduction to mathematical argument.
> At least let people get familiar with some mathematical objects, and learn what to expect from them,
> before you start formalizing everything.
>
> --- Paul Lockhart

There was a while I tried to look around to find an introduction-to-proofs textbook that I liked.
I specifically wanted to have the following requirements:

- **Pragmaticism**: the textbook should not start with foundational issues like
  logical quantifiers or set theory.
  I have held a long belief that these are emphatically not the right way to start proofs,
  because _in practice_ when one really does proofs,
  one is usually not thinking too much about the axioms of set theory.
- **Substantial**: the results one proves as practice should feel interesting. They should have meat.
  For example, the statement that a tree always has one fewer edge than vertex is not obvious at first,
  so when one sees the proof it gives an idea.
  I believe this is important because I want to develop a student's intuition,
  rather than try to teach them to work against it.
- **Intuitive**: I reject the approach of some other instructors in which
  students start by proving basic results from first principles like the well-ordering principle,
  "all right angles are congruent", etc.
  I think this is an experience that is worth having, but it should not be the first experience one has.
  (This is the same reason people's first programming language is Python and not assembly.)
- **Combinatorial**: for competition reasons.
  My currently recommended combinatorics textbook by Pascal96 is a bit on the difficult side.
  It would be nice to cover some ground here.

The closest I got was Joseph Rotman's _Journey Into Mathematics_ textbook,
which satisfies the first three conditions but not the fourth (the book draws from algebra, geometry,
and number theory). I adore Rotman's book and the copy I read at age 12 is tattered from extended use.
I'd like to get the combinatorics in, too.

## Picking a fight

I should state now this is against common wisdom.
[Terence Tao](https://terrytao.wordpress.com/career-advice/theres-more-to-mathematics-than-rigour-and-proofs/)
for example describes mathematical education in three parts: pre-rigorous, rigorous, post-rigorous.
Relevant quotes:

> \[In the rigorous stage\], one is expected to be able to comfortably
> manipulate abstract mathematical objects without focusing too much on what such objects actually "mean".
> … The transition from the first stage to the second is well known to be rather traumatic.

My thesis is that **for high school students with an enriched math background,
the rigorous and post-rigorous stages should be merged or even inverted**.
Attending a math circle, going to math camps,
or participating in competitions gives you a much better intuition than a
typical starting undergraduate would otherwise have access to.
I propose that we take advantage of this intuition, rather than ignore or suppress it.

## Content

I'm eyeing graph theory as a topic to start off on, if not use wholesale.
I think it is an amazing topic for teaching proofs with.
Definitions that make sense, proofs that are intuitive but not obvious,
lots of pictures that don't lose rigor, and so on. I imagine I would start there and see where it takes me.

If I go through with it, I think it would take about a year for me to get some
initial drafts available to the public.

## Pay-what-you-want model

I want to try this out. I think it would look something like:

1. You can download the nicely typeset PDF for 20 dollars;
2. The entire source code is publicly readable on GitHub,
   so if you can't pay or don't want to pay just download the source and compile it.
   It might not have some formatting polishes or whatever but all the content is going to be there.
3. If you don't have a computer to compile things on, email me nicely and I'll send you a copy.
4. Pull requests welcome, and if you fix some sufficient number of typos or
   some major errors I'll add your name to acknowledgments.

But I'm not sure yet.

## Questions for the audience

1. Is this something people would want to see?
2. Is there any existing text that already satisfies my requirements?
3. Is the payment model fair?
4. Other comments or suggestions?
