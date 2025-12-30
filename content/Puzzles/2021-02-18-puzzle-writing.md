Title: Some puzzle-writing thoughts from an amateur
Date: 2021-02-18 01:37
Tags: mystery hunt, puzzle hunt
Slug: puzzle-writing
Status: published
original_url: 2021/02/18/some-puzzle-writing-thoughts-from-an-amateur/

The [2021 Mystery Hunt](https://perpendicular.institute/)
concluded a while ago, and wow, what an experience.
I was lucky enough to be on the organizing team,
and I am so proud right now to be able to say I am a ✈️✈️✈️ Galactic Trensdetter ✈️✈️✈️.
(If you don't know what a puzzle hunt is,
[betaveros has a great introduction](https://blog.vero.site/post/puzzlehunts).)

I came in to the MIT Mystery Hunt with no writing experience at all,
and ended up being listed as the author of a few.
It was a trial by fire, to say the least.

In this post I want to say a bit about the parts
of the puzzle-writing process that surprised me the most,
in the hopes that maybe it would be helpful to future authors.
A nice introduction is given by e.g.
[David Wilson](http://www.mit.edu/~dwilson/puzzles/puzzlewriting.html),
which I read many times before I actually attempted to write my first puzzle.
Most of what's said here repeats or builds off of what is already there.

_Spoiler warning_: this post contains
minor spoilers for some of my (Evan's) puzzles,
but nothing that would completely ruin the puzzle.
The eight puzzles I made major contributions for the 2021 hunt are
[A Bit of Light][light],
[Blind Calculation][blind],
[Clueless][clueless],
[Divided Is Us][divided],
[Escape From Life][escape],
[Le chiffre indéchiffrable][chiffre],
[Nutrition Facts][fat],
[The IMO Shortlist][shortlist].

## 0. Overview

When I first went in to puzzle writing,
I had the idea that a puzzle was a series of steps
that the solver takes to go from the initial data to an answer.
The puzzle-designer's job was to make figuring out the steps challenging but rewarding
(rather than trivial or frustrating).
This point of view is really focused on the _mechanical_ part of the puzzle.

After my hunt experiences, I found myself internally guided
by splitting puzzle-writing goals into two _orthogonal_ parts:
the _mechanical_ half and the _aesthetic_ half.
(Or if you are feeling zen, "science" and "art".)
The mechanical part refers to the details of how the solver
works through the puzzle, but the aesthetic part refers to
things like the theming of the puzzle or so on.
I'll talk a bit more about these below.

## 1. Finding a core mechanism

I think the thing that was most helpful for me in starting
was to **be on the lookout for things that "feel puzzly"**.
I'm still not sure exactly what I mean when I say that,
but I think I vaguely mean things satisfying one or more of the following criteria:

- Thing is very "well-defined"; for example,
  it has a canonical reference you can find on the Internet.
- Thing has a grid.
- Thing lends itself to puns or wordplay.
- Thing has a natural mapping,
  e.g. a way to turn a number into a word (say, episode numbers of a show).
- Thing has numbers that work well with A=1, B=2, ..., Z=26.
- Thing has a concept of compass directions for
  [flag semaphore](https://en.wikipedia.org/wiki/Flag_semaphore).

[devjoe's index](http://devjoe.appspot.com/huntindex/index/keywords.html)
is useful both for getting ideas,
and also to make a routine search of whether an idea you have is already used.
For example, when writing the [IMO Shortlist][shortlist],
the first thing I did was look through to see if math contests
more generally had been done in any Mystery Hunt (answer: no).

I'm already starting to mention encodings,
so I'll do that now for those of you that have never seen them.
Basically, there is a list of puzzle encodings that all
experienced solvers are expected to be able to notice in Mystery Hunt.
This has the upshot that they can be used freely in puzzles!
Examples are:

- Anything with numbers could be A=1, B=2, ..., Z=26.
- Anything with a grid could be [Braille](https://en.wikipedia.org/wiki/Braille).
- Anything with directions at all could be [semaphore](https://en.wikipedia.org/wiki/Flag_semaphore).
- Any time you have a bunch of strings, the first letters might spell a message.
- Any time you have a sequence with exactly two kinds of objects
  (ones or zeros, on or off, true or false, red or blue, dot or dash)
  consider binary (which could then become letters by A1Z26)
  or occasionally Morse code.
- Any time you have words of the same length, see if their letters overlap.
- Any time you have a bijection f from a set to itself,
  you should see if that function forms a cycle.
  If so, take that as an ordering.

The [extraction part of Brian Chen's introduction to puzzle
hunts](https://blog.vero.site/post/puzzlehunts#how-to-extract-the-answer)
goes over all of these in more detail.

![Table of common encodings from
  [puzzledpint.com][pint]]({static}/images/puzzled-pint-sheet.webp)

[pint]: http://puzzledpint.com/files/2415/7835/9513/CodeSheet-201912.pdf

Examples of moments in my life when I saw something and said
"this would be good puzzle material", and flew with it:

- [Blind Calculation][blind] came about
  because I was staring at an abacus on my table and saw a grid.
- [Escape From Life][escape] came about
  because I thought that [this website (spoiler)](https://conwaylife.com/wiki/Main_Page)
  was a puzzle gold-mine.
  (I had a lot of fun drawing a SHIPTIE as a ship with a tie.)
- [Nutrition Facts][fat] came about
  because I was staring at a nutrition facts label
  and noticed how there were a lot of numbers with relations between them.

One thing I occasionally found helpful was to **start with the answer to the puzzle first**
to help narrow down the focus a bit.
For the 2021 MIT Mystery Hunt, there was a big pool of several hundred answers,
about 50 of which were for the Students round
(shorter easy puzzles, like the fish puzzles from 2015).
The Students answers were put in a big pool,
and you could request one of them to start and then write a puzzle with it.
[Blind Calculation][blind] and [Nutrition Facts][fat] were both started this way,
where I was first given the answer to the puzzle,
and then I started looking for objects that both felt puzzly and fit thematically.
But it's not necessary; the other six puzzles I wrote were because
I had an idea in an area I knew well, came up with a mechanism,
and got an answer assigned once I had a plan written out.

## 2. Aesthetic

I think the thing that surprised me most is that you can have a really
successful puzzle which is almost trivial mechanically
(in the sense the solver has pretty clear instructions
on what to do the entire way through).
For example, this year's hunt featured a puzzle called _Boggle Battle_
where most of the work to be done was playing cooperative
[Boggle](https://perpendicular.institute/puzzle/boggle-battle/)
with friends, and the only "puzzly" part was the extraction.
Similarly, [So You Think You Can Count](https://perpendicular.institute/puzzle/so-you-think-you-can-count/)
has minimal puzzle elements, and doesn't have an extraction at all
(upon reaching 100, the solvers are simply given the answer).
They both got high ratings during testsolving
because the solvers had fun anyways.

![Helpful Firefly, an iconic character from
  So You Think You Can Count?]({static}/images/mh2021-firefly.png)

I think the conclusion I drew from this was that while mechanics are important
(e.g. things like checksumming, eliminating false trails, no extra information, etc.)
caring about the aesthetics of the puzzle is more important.
(Of course, like many things in life, they are not completely orthogonal:
thematic coherence is one of the best confirmations a puzzle-solver can have
when they have a guess at the next step.)

In particular, one useful guideline is to **consider cutting any steps
that don't feel thematically coherent**.

But this was not always a prohibition!
For example, despite the advice that it's better to have only one a-ha per puzzle,
I found out that I could generally get away with having multiple a-ha's
for a puzzle as long as all of them felt _thematically coherent_ with each other.
[Le chiffre indéchiffrable][chiffre] is a decent example of this in my opinion,
where despite multiple steps and moving parts,
the steps all seem to resonate with each other.

An anti-example of this might be the extraction step of [IMO Shortlist][shortlist],
which arguably felt a little out of place, although I ended up keeping it anyways
for lack of a better alternative.

## 3. Writing

Once I had the general mechanism for the problem down,
there were often still a lot of smaller local decisions to make
as I composed the puzzle.
Editors were helpful at this step to provide feedback;
but there are some guidelines that I would constantly check against
during the writing process (preemptively addressing concerns).

Some examples (by no means the only ones):

- Do whatever you can to confirm correct paths, e.g. make it so that
  if a solver tries the right thing, they immediately get a confirmation of some sort.
- Try to make sure all the information is used, and minimize arbitrary choices.
  For example, alphabetize things when the given order doesn't matter.
  (There are some exceptions to this, e.g. one common puzzle mechanic
  is that you have a sea of letters and draw some lines, and look
  at the intersected letters.
  [Thor](https://puzzlepotluck.com/3/19) from puzzle potluck 3 is an example.
  Necessarily, some of the "distracting" letters are never used.)
- Provide enough redundancy or checkpoints so that a team
  can still solve the puzzle even with a few errors.
  For example, you might try to set things up so that one error
  leads to just a single garbled letter in a phrase which can be noticed
  and fixed; or, if you have a list of objects to identify,
  having them in alphabetical order will also help fix mistakes.

Basically, I would constantly put myself into the shoes of the solver.
At each milestone in the puzzle,
I would imagine what they were looking at, and how they might react it.
I often paid special attention to thinking about
what feedback they would get if they did the correct thing,
and what feedback they would get if they made a mistake
(e.g. "if they make a small error here, the number they get probably
won't be an integer, so they'll know right away they made a mistake"),
and what possible wrong paths the solver could take.

It's also worth paying a bit of attention to **accessibility** of the puzzle.
For my puzzles, this mostly consisted of:

- Adding alt-texts to images (especially any text in the image).
- Including enlarged versions of any image I used
  (typically, if you click an image, it opens the full-resolution image).
- Keeping colorblind or black/white printing in mind when choosing colors
  (or choosing not to use colors).
  Though I had to violate this blatantly for [Clueless][clueless],
  where the exact choice of colors was important to the puzzle.

## 4. Testsolving

If you are a software programmer, then debugging is part of your life.
No matter how experienced you are,
you are going to have some bugs in your code.
The compiler will catch some of them; testing will catch others.
You might have fewer bugs over time as you get more experienced,
but they will never go away completely.

I think the same is largely true for puzzle-writing.

I don't mean this in the sense that the puzzle will literally have an outright error or typo
every so often (though if we're being honest here, all my first drafts sure did).
What I really mean is that,
the first version of the puzzle will have unexpected issues,
and often the only reasonable way to find them out is through test-solving.
I had the common experience of watching my puzzle completely fall apart
because the solvers were doing something totally different from what I wanted.

For example, in [Clueless][clueless]:

- The "(starts)" text wasn't there originally.
  I thought it was clear that 1 should start.
  The test-solvers didn't, and tried to get scenarios to work
  by having 2, 3, or 4 start instead.
- The texts like "FIVES WIN THIS" used to be at the top in bold,
  and test-solvers tried to use this information too early
  in ways that to me made no sense.
  I tried to move it the bottom to make it less prominent.
- There used to only be four scenarios, but the solvers got stuck quickly.
  It was necessary to add one easy scenario to help as a foothold
  to clarify what rules were allowed.

In the programming analogy, the editors are the compilers:
they try to point out preliminary issues.
The test-solvers are the unit tests.
Since test-solver time is a valuable resource,
it's important to have a version that is ready to testsolve for them,
but at the same time, I wish I hadn't agonized so hard sometimes
on minor decisions before testsolving,
because the feedback from testsolving often led to huge revisions anyways.

So, even though I mostly worked without coauthors,
the editors and test-solvers were the primary source of feedback
for revising the puzzle.

## 5. Closing thoughts

This is all for now.
I'm hoping to make a later post with more details
about the creation process of each of the eight individual puzzles mentioned above.

In the meantime, I'd like to give one last shout-out to everyone on Galactic
who helped me so much in getting onboarded into the puzzle-writing process.
Thanks y'all!

[light]: https://perpendicular.institute/puzzle/a-bit-of-light/
[blind]: https://perpendicular.institute/puzzle/blind-calculation/
[clueless]: https://perpendicular.institute/puzzle/clueless/
[divided]: https://perpendicular.institute/puzzle/divided-is-us/
[escape]: https://perpendicular.institute/puzzle/escape-from-life/
[chiffre]: https://perpendicular.institute/puzzle/le-chiffre-indéchiffrable/
[fat]: https://perpendicular.institute/puzzle/nutrition-facts/
[shortlist]: https://perpendicular.institute/puzzle/the-imo-shortlist/
