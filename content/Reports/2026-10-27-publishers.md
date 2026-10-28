---
title: Regrets on publishing my textbook
date: 2026-10-27 13:37
slug: publishers
tags: politics
status: published
---

Ten years ago I wrote a post about the process of
[having my EGMO textbook published through the MAA](/publishing).
Since then, I've changed my mind on an important point:
I was too naive and shouldn't have just signed the usual contract with MAA.
If I could go back, I would either

- just post an open source book myself, like [Napkin][napkin]; or
- negotiate an arrangement where I can maintain an open source electronic version,
  which I did when I posted [LAMV][lamv] to [MIT OpenCourseWare][ocw].

This is now the advice I give to prospective writers;
I want to now get it on record here.
The issues that have affected EGMO the most:

[napkin]: https://web.evanchen.cc/napkin.html
[lamv]: https://web.evanchen.cc/1802.html
[ocw]: https://ocw.mit.edu/courses/res-18-016-multivariable-calculus-recitation-notes-fall-2024/

1. **It's impossible to make changes**.

   By now the [errata page](https://web.evanchen.cc/textbooks/geombook-errata.pdf)
   for the textbook is just downright embarrassing.
   And I just _can't do anything about it_.[^2ed]
   Whereas with Napkin and LAMV, I can fix errors as soon as I know
   (or better yet, let people submit pull requests to fix them).
   Clarifications or suggestions similarly can't be incorporated.

2. **It's not open source because you ceded the copyright**.

   For example, if someone wants to do a fan translation for EGMO,
   there is a long process of having to negotiate translation rights with the publisher.
   This eventually finished for Chinese and Japanese,
   but I think some other languages stalled on this point,
   which I think is a real shame.

   Whereas if you have an open version of a book, anyone
   (even multiple groups collaborating) can contribute to a translation freely.
   I'm imagining how nice it would be if I just had a public git repository[^ask]
   that anyone could do localization for in their native language.

3. **It's not accessible.**

   Someone who can't afford the textbook can't legally obtain it.
   More generally, if you put up a barrier to obtaining your work,
   it's always the audience that pays the cost.

[^2ed]:
    Unless I publish a second edition. But I think it's not worth it.

[^ask]:
    I did in fact send an email in 2022 asking whether I could post the
    source files on GitHub and was told no.

Some prospective authors ask me about royalties.
To be clear, there is nothing wrong with being paid for writing a book.
But a traditional publisher may not help you much with this either.
A standard royalty rate might be 10%:
if a reader pays \$60, you get \$6.
So the money is mostly going to the publisher, not you.
A pay-what-you-want system might work better, e.g. this is what Lozanovski's textbook
[A Beautiful Journey through Olympiad Geometry](https://www.olympiadgeometry.com/the-book.html) does.

There are two things that a publisher generally does help with:

- There is some amount of prestige to having your book actually published.
  In particular, there's a bit of a quality signal from that.[^shine]
- It is also nice to have print copies.

[^shine]:
    That said, my general sense is that if you really have a good textbook,
    and you make it freely available on the Internet,
    then it can also just speak for itself.

But it's actually possible to have both of these things without incurring
the penalties described above, if you know this going in.
My favorite category theory book,
[Basic Category Theory by Tom Leinster](https://arxiv.org/abs/1612.09375),
works this way, where Cambridge University Press publishes a print version
but there is also a free online version for everyone.
[Hatcher's Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html)
seems to have a similar arrangement.
So if you decide the prestige or print versions are worth the extra trouble
of going through a publisher, then my advice is to negotiate a deal that
helps you keep some control and maintains accessibility.
