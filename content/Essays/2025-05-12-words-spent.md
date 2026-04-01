---
title: Words Spent
date: 2025-05-12 13:37
slug: words-spent
tags: writing
original_url: 2025/05/12/words-spent/
status: published
---

One of my favorite Djikstra programming quotes is about
thinking via ["lines of code spent"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD08xx/EWD854.html)
rather than "lines of code produced".
I started using this as a philosophy in my writing too: **words spent**.

## Background

One of the things that's surprised me about student writing
is how poorly words are spent.
You'll have a solution where the trivial boilerplate steps are
painfully verbose, and then the actually important parts
are missing all the critical details.

I wonder how much of this is because of crummy writing advice.
In school essays, even when you have nothing meaningful to say,
teachers often impose a minimum word count[^develop] as a "proof of work".
The implied conclusion is that writing many words is the goal.
Which is same mistake that counting "lines of code produced" is.

More careful teachers might talk about being concise,
and might impose a _maximum_ word count instead (or in addition).
Then students get the idea you have this elastic
dial that goes from "too little detail" to "too much detail",
and you need to guess the magic "just right" to win your teacher's approval.

But that's also mistaken.
The "right" numbers of words should _depend on what you have to say_,
just as the number of lines of code should reflect the complexity
of the program you're trying to implement.

[^develop]:
    In ninth grade, my English teacher preferred the euphemism
    "develop your ideas" for "write more words".
    It wasn't until halfway through the year I realized why
    she kept writing that on all my essays.

## Proposal

My proposal is to use "words spent" --- just that two-word phrase ---
as a guideline to steer writers away from bad habits they've learned in school.
I've been using it myself recently and
I think it really conveys the right instincts concisely.

Examples:

- People instinctively know to **avoid costs**.
  If you treat word count as "words spent", you won't try to inflate it.
  - Orwell's advice "if a word can be cut out, always cut it out"
    becomes an obvious corollary. Of course you cut unneeded costs.
- People also instinctively know that **costs can be necessary**.
  If you buy a car for 5000 dollars, you don't expect much from it.
- **Cost prioritization** becomes instinctive.
  You know you should be spending the most words on the most important parts.
  In principle, the reader can guess what matters
  by how many words are spent on it.
- **Cost efficiency** becomes natural too.
  You want _good_ words that do more with less.

## Example usage

### Individual sentences

You _could_ use "words spent" to guide individual sentences.
For example, in a different blog post, I had a draft with the passage:

> Olga and I were originally planning to do a variant on Slitherlinks,
> and we had some prototypes that felt decent by mid-February.
> I was trying to not be too ambitious because of the tight deadline,
> so I was trying to keep things simple.
> We had a verifier up and running too like I did for BWMS,
> so we felt we could iterate quickly once we got the meta specification.

but on re-reading I deleted a third of the words:

> Olga and I were originally planning Slitherlinks variants,
> and had some decent prototypes by mid-February.
> I wanted to keep things simple because of the tight deadline.
> We had a verifier written (like with BWMS), so we could iterate quickly.

(It may be possible to overdo this.
If I'm being really aggressive, almost every sentence has some fat,
but at some point the sentences start to sound unnatural.
I would gladly spend three extra words to make a paragraph flow better,
even if those words technically don't change the meaning of the paragraph.)

### Overall picture

But I think it's more important to use "words spent" at a higher level,
rather than micromanaging individual sentences too much.
Here are some examples of ways it's improved my writing style overall:

- Sometimes in my writing you'll see claims whose proof is the single word
  "Clear" or similar. I'm never terse out of laziness[^lazy].
  It's always because I've decided it's not worth the words spent to say more.

- Conversely, when writing math exposition, I really value **good examples**.
  So I know that I should spend a lot of words on examples,
  and spend fewer words on formal definitions or proofs
  that I want to de-emphasize.

- I know pictures aren't words, but treat them the same way.
  (Okay, fine: "a picture is worth 1000 words".)
  Point is, **good diagrams and pictures are really cost-efficient**.
  They might take a lot of time for me to draw,
  but the author's _time_[^time] is irrelevant to this discussion.
  You can easily convey something in a half-page diagram
  that even 1000 words can't do. If so, do it.
  (Tables can be really good too.)

Zooming out even further, here's some thoughts on
how the [Napkin][napkin] and [LAMV][lamv] books fit into this framework.

I think I was happy with the [Napkin][napkin]
because I was cost-efficient: tons of diagrams,
emphasis on intuition over proofs, etc.
That's why Napkin is a good birds-eye view of topics,
without getting bogged down by fine or technical details.
It's not a textbook --- concisely conveying intuition is the goal of Napkin.

But on the other extreme, [LAMV][lamv] _was_
meant to outright replace the class textbook.
That was _really freaking expensive_, especially for the target audience,
who typically really need things spelled out in full.
So I think LAMV was successful exactly _because_ it put in writing
all the detailed exposition[^gpt] that others were simply unable or unwilling to do.
In this case the enormous cost paid off.

[napkin]: https://web.evanchen.cc/napkin.html
[lamv]: https://web.evanchen.cc/1802.html

[^lazy]: If I'm trying to be lazy, it'll say "to be added later" instead.

[^time]:
    Time spent is not words spent! Another bad anti-lesson.
    Students whose only writing experience is in school might mistakenly
    conflate words spent with time spent.
    But if you're actually trying to write well,
    your words spent could easily go _down_
    over time as you figure out how to be more cost-efficient.
    Good programmers do this all the time too (refactoring code to be shorter
    or deleting unnecessary components).

[^gpt]:
    Actually it could have been even more verbose if I was careless.
    If you read the preface of LAMV, I mention that a lot of the solutions
    to the example questions were initially drafted by ChatGPT,
    but then for which I would slim down the output like crazy:
    usually by a factor of 2 or 3.
    (Actually, now that I think about it, I wonder if humans
    might tend to spend too few words out of laziness,
    whereas GPT spends too many words because it doesn't take time
    to write words the same way humans do.)
