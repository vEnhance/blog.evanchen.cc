Title: Notes on Publishing My Textbook
Date: 2016-11-11 13:37
Tags: politics
Slug: publishing
Status: published
original_url: 2016/11/11/notes-on-publishing-my-textbook/

> _Hmm, so hopefully this will be finished within the next 10 years._
>
> --- An email of mine at the beginning of this project

My [Euclidean geometry book](http://www.mit.edu/~evanchen/geombook.html) was published last March or so.
I thought I'd take the time to write about what the whole process of publishing this book was like,
but I'll start with the disclaimer that my process was probably not very typical
and is unlikely to be representative of what everyone else does.

## Writing the Book

### The Idea

I'm trying to pinpoint exactly when this project changed from "daydream" to "let's do it",
but I'm not quite sure; here's the best I can recount.

It was sometimes in the fall of 2013, towards the start of the school year; I think late September.
I was a senior in high school, and I was only enrolled in two classes.
It was fantastic, because it meant I had lots of time to study math.
[The superintendent of the school eventually found out, though,
and forced me to enroll as an "office assistant" for three periods a
day.](https://blog.evanchen.cc/2016/05/27/fill-in-the-blank/) Nonetheless,
office assistant is not a very busy job, and so I had lots of time, all the time, every day.

Anyways, I had written a bit of geometry material for my math club the previous year,
which was intended to be a light introduction.
But in doing so I realized that there was much, much more I wanted to say,
and so somewhere on my mental to-do list I added "flesh these notes out".
So one day, sitting in the office, after having spent another hour playing StarCraft,
I finally got down to this item on the list.
I hadn't meant it to be a book; I was just wanted to finish what I had started the previous year.
But sometimes your own projects spiral out of your control, and that's what happened to me.

Really, I hadn't come up with a brilliant idea that no one had thought of before.
To my knowledge, no one had even _tried_ yet.
If I hadn't gone and decided to write this book, someone else would have done it; maybe not right away,
but within many years. Indeed, I was honestly surprised that I was the first one to make an attempt.
The USAMO has been a serious contest since at least the 1990's and 2000's,
and the demand for this book certainly existed well before my time.
Really, I think this all just goes to illustrate that the Efficient Market
Hypothesis is not so true in these kind of domains.

### Setting Out

Initially, this text was titled _A Voyage in Euclidean Geometry_ and the
filename Voyage.pdf would persist throughout the entire project even though the
title itself would change throughout.

The beginning of the writing was actually quite swift.
Like everyone else, I started out with an empty LaTeX file.
But it was different from blank screens I've had to deal with in my life;
rather than staring in despair (think English essay mode), I exploded.
I was _bursting_ with things I wanted to write.
It was the result of having years of competitive geometry bottled up in my head.
In fact, I still have the version 0 of the table of contents that came to life
as I started putting things together.

- Angle Chasing (include "Fact 5")
- Centers of the Triangle
  - The Medial Triangle
  - The Euler Line
  - The Nine-Point Circle
- Circles
  - Incircles and Excircles
  - The Power of a Point
  - The Radical Axis
- Computational Geometry
  - All the Areas (include Extended Sine Law, Ceva/Menelaus)
  - Similar Triangles
  - Homothety
  - Stewart's Theorem
  - Ptolemy's Theorem
- Some More Configurations (include symmedians)
  - Simson lines
  - Incircles and Excenters, Revisited
  - Midpoints of Altitudes
- Circles Again
  - Inversion
  - Circles Inscribed in Segments
  - The Miquel Point (include Brokard, this could get long)
  - Spiral Similarity
- Projective Geometry
  - Harmonic Division
  - Brokard's Theorem
  - Pascal's Theorem
- Computational Techniques
  - Complex Numbers
  - Barycentric Coordinates

Of course the table of contents changed drastically over time, but that wasn't important.
The point of the initial skeleton was to provide a **bucket sort** for all the things that I wanted to cover.
Often, I would have three different sections I wanted to write,
but like all humans I can only write one thing at a time,
so I would have to create section headers for the other two and try to get the
first section done as quickly as I could so that I could go and write the other two as well.

I did take the time to do some things correctly, mostly LaTeX. Some examples of things I did:

- Set up proper amsthm environments: earlier versions of the draft had "lemma", "theorem", "problem",
  "exercise", "proposition", all distinct
- Set up an organized master LaTeX file with `\include`'s for the chapters,
  rather than having just one fat file.
- Set up shortcuts for setting up diagrams and so on.
- Set up a "hints" system where hints to the problems would be printed in random order at the end of the book.
- Set up a special command for new terms (\vocab).
  At the beginning all it did was made the text bold,
  but I suspected that later I might do other things (like indexing).

In other words, whenever possible I would pay $O(1)$ cost to get back $O(n)$ returns.
Indeed the point of using LaTeX for a long document is so that you can "say what you mean":
you type `\begin{theorem} … \end{theorem}`, and all the formatting is taken care of for you.
Decide you want to change it later, and you only have to change the relevant code in the beginning.

And so, for three hours a day, five days a week, I sat in the main office of Irvington High School,
pounding out chapter after chapter.
I was essentially typing up what had been four years of competition experience; when you're 17 years old,
that's a big chunk of your life.

I spent surprisingly little time revising (before first submission). Mostly I just fired away.
I have always heard things about how important it is to rewrite things and how
first drafts are always terrible, but I'm glad I ignored that advice at least at the beginning.
It was immensely helpful to have the skeleton of the book laid out in a tangible
form that I could actually see.
[That's one thing I really like about writing;
helps you collect your thoughts together.](https://blog.evanchen.cc/2015/03/14/writing/)

It's possible that this is part of my writing style; compared to what everyone says I should do,
I don't do very much rewriting. My first and final drafts tend to look pretty similar.
I think this is just because when I write something that's not an English essay,
I already have a reasonably good idea what I want to say,
and that the process of writing it out does much of the polishing for me.
I'm also typically pretty hesitant when I write things:
I do a lot of pausing for a few minutes deciding whether this sentence is really
what I want before actually writing it down, even in drafts.

### Some Encouragement

By late October, I had about 80 or so pages content written.
Not that impressive if you think about it; I think it works out to something like 4 pages per day.
In fact, looking through my data,
I'm pretty sure I had a pretty consistent writing rate of about 30 minutes per page.
It didn't matter, since I had so much time.

At this point, I was beginning to think about possibly publishing the book,
so it was coming out reasonably well.
It was a bit embarrassing, since as far as I could tell,
publishing books was done by people who were actually professionals in some way or another.
So I reached out to a couple of teachers of mine (not high school) who I knew
had published textbooks in one form or another; I politely asked them what their thoughts were,
and if they had any advice. I got some gentle encouragement, but also a pointer to self-publishing:
turns out in this day and age, there are services like Lulu or CreateSpace that will just let you publish…
whatever you want. This gave me the guts to keep working on this,
because it meant that there was a minimal floor: even if I couldn't get a traditional publisher,
the worst I could do was self-publish through Amazon,
which was at any rate strictly better than the plan of uploading a PDF somewhere.

So I kept writing. The seasons turned, and by February, the draft was 200 pages strong.
In April, I had staked out a whopping 333 pages.

## The Review Process

### Entering the MAA's Queue

I was finally beginning to run out of things I wanted to add, after about six months of endless typing.
So I decided to reach out again; this time I contacted a professor (henceforth Z) that I knew,
whom I knew well from time at the Berkeley Math Circle.
After some discussion, Z agreed to look briefly at an early draft of the
manuscript to get a feel for what it was like.
I must have exceeded his expectations,
because Z responded enthusiastically suggesting that I submit it to the Problem Book Series of the MAA.
As it turns out, he was on the editorial board, so in just a few days my book was in the official queue.

This was all in April. The review process was scheduled to begin in June,
and likely take the entirety of the summer.
I was told that if I had a more revised draft before the review that I should also send it in.

It was then I decided I needed to get some feedback.
So, I reached out to a few of my close friends asking them if they'd be willing
to review drafts of the manuscript. This turned out to not go quite as well as I hoped, since

- Many people agreed eagerly, but then didn't actually follow through with going
  through and reading chapter by chapter.
- I was stupid enough to send the entire manuscript rather than excerpts,
  and thus ran myself a huge risk of getting the text leaked.
  Fortunately, I have good friends, but it nagged at me for quite a while. Learned my lesson there.

That's not to say it was completely useless; I did get some typos fixed. But just not as many as I hoped.

### The First Review

Not very much happened for the rest of the summer while I waited impatiently;
it was a long four month wait for me.
Finally, in the end of August 2014, I got the comments from the board;
I remember I was practicing the piano at Harvard when I saw the email.

There had been six reviews. While I won't quote the exact reviews, I'll briefly summarize them.

1.  There is too much idiosyncratic terminology.
2.  This is pretty impressive, but will need careful editing.
3.  This project is fantastic; the author should be encouraged to continue.
4.  This is well developed; may need some editing of contents since some topics are very advanced.
5.  Overall I like this project. That said, it could benefit from some reading and editing.
    For example, here are some passages in particular that aren't clear.
6.  This manuscript reads well, written at a fairly high level. The motivation provided are especially good.
    It would be nice if there were some solutions or at least longer hints for
    the (many) problems in the text. Overall the author should be encouraged to continue.

The most surprising thing was how short the comments were.
I had expected that, given the review had consumed the entire summer,
the reviewers would at least have read the manuscript in detail.
But it turns out that mostly all that had been obtained were cursory impressions from the board members:
the first four reviews were only a few sentences long!
The fifth review was more detailed, but it was essentially a "spot check".

I admit, I was really at a loss for how I should proceed.
The comments were not terribly specific,
and the only real action-able item were to use less extravagant terms in
response to 1 (I originally had "configuration", "exercise" vs "problem",
etc.) and to add solutions (in response to 5).
When I showed the comments to Z, he commented that while they were positive,
they seemed to suggest that the publication may not be anytime soon.
So I decided to try submitting a second draft to the MAA,
but if that didn't work I would fall back on the self-publishing route.

The reviewers had commented about finding a few typos,
so I again enlisted the help of some friends of mine to eliminate them. This time I was a lot smarter.
First, I only sent the relevant excerpts that I wanted them to read,
and watermarked the PDF's with the names of the recipients.
Secondly, this time I paid them as well: specifically,
I gave $40 + \min(40, 0.1n^2)$ dollars for each chapter read,
where $n$ was the number of errors found.
I also gave a much clearer "I need this done by X" deadline.
This worked significantly better than my first round of edits.
Note to self: people feel more obliged to do a good job if you pay them!

All in all my friends probably eliminated about 500 errors.

I worked as rapidly as I could, and within four weeks I had the new version. The changes that I made were:

- In response to the first board comment,
  I eliminated some of the most extravagant terminology ("demonstration", "configuration",
  etc.) in favor of more conventional terms ("example", "lemma").
- I picked about 5-10 problems from each chapter and added full solutions for them.
  This inflated the manuscript by another 70 pages, for a new total of 400 pages.
- Many typos and revisions were corrected, thanks to my team of readers.
- Some formatting changes; most notably,
  I got the idea to put theorems and lemmas in boxes using mdframed (most of my
  recent olympiad handouts have the same boxes).
- Added several references.

I sent this out and sat back.

### The Second Review

What followed was another long waiting process for what again were ended up
being cursory comments. The delay between the first and second review was
definitely the most frustrating part --- there seemed to be nothing I could do other than sit and wait.
I seriously considered dropping the MAA and self-publishing during this time.

I had been told to expect comments back in the spring.
Finally, in early April I poked the editorial board again asking whether there had been any progress,
and was horrified to find out that the process hadn't even started out due to a miscommunication.
Fortunately, the editor was apologetic enough about the error that she asked the
board to try to expedite the process a little. The comments then arrived in mid-May, six weeks afterwards.

There were eight reviewers this time. In addition to some stylistic changes suggested (e.g.
avoid contractions), here were some of the main comments.

- The main complaint was that I had been a bit too informal.
  They were right on all accounts here: in the draft I had sent,
  the chapters had opened with some quotes from years of MOP (which confused the board,
  for obvious reasons) and I had some snarky comments about high school geometry
  (since I happen to despise the way Euclidean geometry is taught in high
  school.) I found it amusing that no one had brought it up yet, and happily obliged to fix them.
- Some reviewers had pointed out that some of the topics were very advanced.
  In fact, one of the reviewers actually recommend _against_ the publication of
  the book on the account that no one would want to buy it.
  Fortunately, the book ended up getting accepted anyways.
- In that vein, there were some remarks that this book, although it serves its target audience well,
  is written at a fairly advanced level.

Some of the reviews were cursory like before,
but some of them were line-by-line readings of a random chapter,
and so this time I had something more tangible to work with.

So I proceeded to make the changes.
For the first time, I finally had the brains to start using **git** to track the changes I made to the book.
This was an enormously good idea, and I wish I had done so earlier.

Here are some selected changes that were made (the full list of changes is quite long).

- Eliminate a bunch of snarky comments about high school, and the MOP quotes.
- Eliminate about 250 contractions.
- Eliminate about 50 instances of unnecessary future tense.
- Eliminate the real product from the text.
- Added in about seven new problems.
- Added and improved significantly on the index of the book, making it far more complete.
- Fix more references.
- Change the title to "Euclidean Geometry in Mathematical Olympiads" (it was originally "Geometra Galactica").
- Change the name of Part II from "Dark Arts" to "Analytic Techniques". (Hehe.)
- Added people to the acknowledgments.
- Changes in formatting: most notably I change the font size from 11pt to 10pt to decrease the page count,
  since my book was already twice as long as many of the other books in the series.
  This dropped me from about 400 pages back to about 350 pages.
- Fix about 200 more typos. Thanks to those of you who found them!

I sent out the third draft just as June started, about three weeks after I had received the comments.
(I like to work fast.)

### The Last Revisions

There were another two rounds afterwards.
In late June, I got a small set of about three pages of additional typos and clarifying suggestions.
I sent back the third draft one day later.

Six days later, I got back a list of four remaining edits to make.
I sent an updated fourth draft 17 minutes after receiving those comments.
Unfortunately, it then took another five weeks for the four changes I made to be acknowledged.
Finally, in early August, the changes were approved and the editorial board
forwarded an official recommendation to MAA to publish the book.

### Summary of Review Timeline

In summary, the timeline of the review process was

- First draft submitted: April 6, 2014
- Feedback received: August 28, 2014
  Second draft submitted: November 5, 2014
- Feedback received: May 19, 2015
  Third draft submitted: June 23, 2015
- Feedback received: June 29, 2015
  Fourth draft submitted: June 29, 2015
- Official recommendation to MAA made: August 2015

I think with traditional publishers there is a lot of waiting;
my understanding is that the editorial board largely consists of volunteers, so this seems inevitable.

## Approval and Onwards

On September 3, 2015, I got the long-awaited message:

> It is a pleasure to inform you that the MAA Council on Books has approved the
> recommendation of the MAA Problem Books editorial board to publish your manuscript,
> _Euclidean Geometry in Mathematical Olympiads._

I got a fairly standard royalty contract from the publisher, which I signed off without much thought.

### Editing

I had a total of zero math editors and one copy editor provided.
It shows through on the [enormous list of
errors](http://www.mit.edu/~evanchen/geombook.html) (and this is _after_ all the
mistakes my friends helped me find).

Fortunately, my copy editor was quite good (and I have a lot of sympathy for this poor soul,
who had to read every word of the entire manuscript).
My Git history indicates that approximately 1000 corrections were made; on average, this is about 2 per page,
which sounds about right. I got the corrections on hard copy in the mail; the entire printout of my book,
except well marked with red ink.

Many of the changes fell into general shapes:

- Capitalization. I was unwittingly inconsistent with "Law of Cosines" versus
  "Law of cosines" versus "law of cosines", etc and my copy editor noticed every one of these.
  Similarly, cases of section and chapter titles were often not consistent;
  should I use "Angle Chasing" or "Angle chasing"? The main point is to pick one convention and stick with it.
- My copy editor pointed out every time I used "Problems for this section" and had only one problem.
- Several unnecessary "quotes" and _italics_ were deleted.
- Oxford commas. My god, so many Oxford commas.
  You just don't notice when the IMO Shortlist says "the circle through the points E, G,
  and H" but the European Girls' Olympiad says "show that KH, EM and BC are concurrent".
  I swear there were at least 100 of these in the book.
  I tried to write a regular expression to find such mistakes,
  but there were lots of edge cases that came up, and I still had to do many of these manually.
- Inconsistency of em dashes and en dashes. This one worked better with regular expressions.

But of course there were plenty of other mistakes like missing spaces, missing degree spaces,
punctuation errors, etc.

### Cover Art

This was handled for me by the publisher:
they gave me a choice of five or so designs and I picked one I liked.

(If you are self-publishing, this is actually one of the hardest parts of the publishing logistics;
you need to design the cover on your own.)

### Proofs

It turns out that after all the hard work I spent on formatting the draft,
the MAA has a standard template and had the production team re-typeset the entire book using this format.
Fortunately, the publisher's format is pretty similar to mine, and so there were no huge cosmetic changes.

At this point I got the proofs,
which are essentially the penultimate drafts of the book as they will be sent to the printers.

### Affiliation and Miscellani

There was a bit more back-and-forth with the publisher towards the end.
For example, they asked me if I would like my affiliation to be listed as MIT or to not have an affiliation.
I chose the latter. I also send them a bio and photograph, and an author questionnaire,
asking me for some standard details.

Marketing was handled by the publisher based on these details.

## The End

Without warning, I got an email on March 25 announcing that the PDF versions of
my book were now available on MAA website. The hard copies followed a few months afterwards.
That marked the end of my publication process.

If I were to do this sort of thing again,
I guess the main decision would be whether to self-publish or go through a formal publisher.
The main disadvantage seems to be the time delay,
and possibly also that the royalties are lesser than in self-publishing.
On the flip side, the advantages of a formal publisher were:

- Having a real copy editor read through the entire manuscript.
- Having a committee of outsiders knock some common sense into me (e.g.
  not calling the book "Geometra Galactica").
- Having cover art and marketing completely done for me.
- It's more prestigious; having a real published book is (for whatever reason) a very nice CV item.

Overall I think publishing formally was the right thing to do for this book, but your mileage may vary.

Other advice I would give to my past self, mentioned above already: keep paying $O(1)$ for $O(n)$,
use git to keep track of all versions,
and be conscious about which grammatical conventions to use (in particular, stay consistent).

Here's a better concluding question: what surprised me about the process, i.e,
what was different than what I expected? Here's a partial list of answers:

- It took even longer than I was expecting.
  Large committees are inherently slow; this is no slight to the MAA,
  it is just how these sorts of things work.
- I was surprised that at no point did anyone really check the manuscript for mathematical accuracy.
  In hindsight this should have been obvious;
  I expect reading the entire book properly takes at least 1-2 years.
- I was astounded by how many errors there were in the text, be it math or grammatical or so on.
  During the entire process something like 2000 errors were corrected (admittedly several were minor,
  like Oxford commas). Yet even as I published the book, I _knew_ that there had to be errors left.
  But it was still irritating to hear about them post-publication.

All in all, the entire process started in September 2013 and ended in March 2016, which is 30 months.
The time was roughly 30% writing, 50% review, and 20% production.
