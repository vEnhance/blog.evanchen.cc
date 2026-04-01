---
title: Conversations
date: 2015-08-05 13:37
slug: conversations
tags: shower thoughts
original_url: 2015/08/05/conversations/
status: published
---

I've recently come to believe that "deep conversations" are overrated. Here is why.

## Memory

Human short term memory is pretty crummy.
[Here is an illustration from linguistics](http://en.wikipedia.org/wiki/Center_embedding):

> A man that a woman that a child that a bird that I heard saw knows loves

This is a well-formed English phrase. And yet parsing it is difficult, because you need a stack of size four.
Four is a pretty big number.

And that's after I've written the sentence down for you,
so your eyes could scan it two or three times to try and parse it.
Imagine if I instead _said this sentence aloud_.

Other examples include any object with some moderately complex structure:

> Let ABC be a triangle and let AD, BE, CF be altitudes concurrent at the orthocenter H.

This is not a very complicated diagram,
but it's also very difficult to capture in your head unless you've seen it before -- and again,
that's after I've written it down for your viewing pleasure.

Now imagine what you're talking about isn't just six lines and seven points,
but "what do you think the point of college is?",
or "should a high school diploma be required to obtain a driver's license?",
or "what is algebraic geometry about?" (all examples from my life, mind you).
The answer to these questions is far more complex than the trivial examples I've given above.
To try and talk about these things merely by voice seems fruitless.

It's worth pointing out that you can get away with things that have a lot of
_breadth_ as long they do not have _depth_ -- loosely, as long as there are not too many dependencies.
To give an example, the linguistics example is tricky because all the subjects
and verbs depend on each other.
The geometry diagram is tricky because the points are all tied together in a certain way.
But I could read the first chapter of _And Then I Thought I Was A Fish_ out loud,
or tell you the story of the cute girl I met three summers ago,
because the parts don't depend (as much) on one another:
at any point in a story you can remember the last couple sentences and still enjoy the story.
But if I try to read you the first chapter of _[The Rising Sea:
Foundations of Algebraic Geometry](http://math.stanford.edu/~vakil/216blog)_,
it would make a good bedtime story only because you'd probably fall asleep.

It just strikes me as bizarre that people talk about "deep" issues without writing a single thing down.
I think if you're having lunch with a friend and discussing something like this,
you ought to at least have a piece of paper out on the table where you can both
jot down the main ideas of what's been said.
It doesn't need to have every word because then you just get bloat, but still,
at least get the key insights somewhere visible.
(That's what presentation slides and blackboards are for, right?)

## Computation

The other strange thing is that in conversations, you have to process and respond in real-time.
You can only spend as long thinking about a sentence as it takes for the next one to be said.

This is fine if I ask you a question such as "what is your birthday?", because lookup queries are fast.
It's fine if I ask you "what did you think of X book you read?", again because it is just a lookup query.
Note that this is true _even if_ you spent a long time reading and thinking about the book,
because the computation was already done.
It's even fine if I ask "what is two plus five?" because it takes not very long to add.

But if I ask "what do you think about the war on drugs?" and you haven't been thinking much about it,
then the best answer you can give is "I don't know";
because you can't do a lookup query for an answer you haven't computed yet.

Put another way, suppose someone asks me some complex question like "how do I get better at math contests?",
and I respond "do a lot of problems that are right above your ability".
One of two possible things just happened:

1.  I had already thought about this question,
    and this is a [pre-computed answer](https://blog.evanchen.cc/2014/07/27/what-leads-to-success-at-math-contests/),
    or
2.  I came up with this in the half second between the end of your question and the start of my response.
    (Though you can increase this time by prepending "uh", "like", "I think".)

In other words, _the fast nature of conversations prevents anything other than
cache lookups and first impressions_ (or I suppose possibly a combination of both).
And if the issue you're talking about is sufficiently complex,
first impressions are likely not so insightful.
So if I sound really smart in a conversation,
the only reason is that you're asking questions I already pre-computed good answers for.

In other words, the best you can do from a typical conversation is learn what people's existing ideas are.
There isn't a tractable way to generate new ideas from feedback,
just because the time-scale involved is too small.
Eliezer Yudkowsky makes a similar point in a [Less Wrong
Post](http://lesswrong.com/lw/k8/how_to_seem_and_be_deep/t1_fjv):

> If you want to sound deep, you can never say anything that is more than a
> single step of inferential distance away from your listener's current mental state.
> That's just the way it is.

## Hypothesis

I will now point out that both issues I mentioned have easy partial fixes.
If I'm correct, then deep conversations can be substantially enhanced if we use
paper or blackboard or anything else, and agree it is socially acceptable to take a minute to respond.
Neither of these actions will completely alleviate their respective problems,
but trust me when I say having 60 seconds to think is a world of difference compared to 2.

Both of these initially struck me as weird conclusions, but they do seem to make sense on closer inspection.
In fact, I have actually seen both done in practice (albeit not simultaneously).
So this means I have a way to test what I've written in this post now…
