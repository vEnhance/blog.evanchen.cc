Title: Why Evan does not like JavaScript as a first language
Date: 2022-11-18 13:37
Tags: programming
Slug: javascript
Status: published
original_url: 2022/11/18/why-evan-does-not-like-javascript-as-a-first-language/

Some people have asked me why I anti-recommend JavaScript for beginners
on my website FAQ.
This post will try to give a few reasons why.

Some notes:

- I'm referring to base JS. I like TypeScript a lot for example (it's high on
  my tier list of programming languages for beginners).
  And I know about `eslint`, but you asked me about recommendations for
  beginners, and I think beginners shouldn't have to worry about setting up an
  IDE with strict linting until _after_ they can write a `for` loop by
  themselves without screwing up.
- I have multi-file projects in mind. I don't have a problem with using inline
  JavaScript for tiny 20-line snippets of code embedded in a webpage.
- I'm an amateur programmer. Professional programming is a different ball game.

## Weak typing

I'm clumsy. I make many more mistakes than the average programmer.
The other day I finally installed a Django-HTML linter in
[OTIS-WEB](https://github.com/vEnhance/otis-web) and found out that the
[majority of my templates had mismatched HTML tags I never noticed for
years](https://github.com/vEnhance/otis-web/commit/a347f306f6d4f3cebdda812fc3cecd1e18aa9c9e).

If I write some nonsense code like

```javascript
let x = 3;
let y = x.value;
```

I would like the program to, you know, crash. It doesn't.
It sets `y = undefined`.
And then 100 lines later I have to figure out why some other function
didn't do what it was supposed to, and trace back through the entire source.

It's at a point where you can generate memes by just taking two different types
of objects and adding or subtracting them and then laughing at the result.

```
Welcome to Node.js v19.1.0.
Type ".help" for more information.
> '7' + 3
'73'
> '7' - 3
4
> 'hi' + ['i', 'am', 'a', 'potato']
'hii,am,a,potato'
> const x = 42;
undefined
> '1337' + x - x
133700
> '1337' - x + x
1337
> 'wtf' - 2022 + 'i?'
'NaNi?'
```

Like, at least in Python, you'll get a `TypeError` or `AttributeError`
or something when you run the code (but not at "compile time",
because scripting languages don't have a "compile time").
Python's my native language, and it still annoyed me so much that I use both
`mypy` and `pyright` on all my Python code now to enforce what essentially
became Python with static types, despite Python's type system being janky af.
You better believe I'm doing this with JavaScript too.

## null, undefined, NaN

These keywords strike dread into my heart because I lack the professional
training to keep the differences straight in my head.

Last I checked though:

```
Welcome to Node.js v19.1.0.
Type ".help" for more information.
> null === null
true
> undefined === undefined
true
> NaN === NaN
false
```

Oh yeah, for those of you that don't know, you always use `===` and not `==`
these days because the latter operator is a
[total minefield](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality):

```
> 0 == false
true
> 0 == null
false
> 0 == undefined
false
> 0 == !!null
true
> 0 == !!undefined
true
> [] == 0
true
> const a = new Number(42);
undefined
> const b = new Number(42);
undefined
> a == b
false
> a == 42 && b == 42
true
```

Well, `==` is supposed to be symmetric at least. Except apparently in Internet
Explorer, where `window == document` is true but `document == window` is false,
in [some versions anyway](https://stackoverflow.com/a/5669517/4826845).

## Variable scope

It used to be that you could forget a `var` keyword and then suddenly your
variable became a global variable. These days we have `let` and `const` and we
just tell the beginners to always use one of these two and never use `var` (or
worse no keyword at all) so I guess it's not as bad as it used to be.

Though of course [you can still find some contrived
examples](https://wtfjs.com/wtfs/2010-02-15-accidental-global).

```
Welcome to Node.js v19.1.0.
Type ".help" for more information.
> (function() { const x = y = 1; })();
undefined
> x
Uncaught ReferenceError: x is not defined
> y
1
```

(For those of you that don't know, the whole `(function() {})()` construction is
an actual JavaScript idiom that's used to prevent exactly this situation.)

And the `this` keyword still strikes fear into my heart. I can't understand it
for the life of me.

## Modules and classes

The JavaScript base language used to have no module system.
Now we have CommonJS and ES modules instead.
Which I guess is fine, but it would have been nice to have these in the base
language, you know?
(I'm definitely not saying this because I spent an entire night fighting some
node dependency chain where one component used CommonJS, and the other used ES,
and they wouldn't play along.)

These days I think people just use `npm` or something and be glad that with
Python I have standard library that won't collapse one day because
[left-pad disappeared suddenly](https://www.theregister.com/2016/03/23/npm_left_pad_chaos/).

Similarly, JavaScript uses a prototype-based object system that I never really
understood either, because it looks like the classes I'm used to, but isn't. If
I was a professional programmer I'd probably take a few hours or days out of my
life to figure out what the heck was going on. I'm not, and whatever beginner is
reading my FAQ is _definitely_ not.

## Easter eggs

Actually these might not be a downside 🙂. I like Easter eggs. Maybe not in
day-to-day code. But examples like this make for a good laugh, and they're
harmless because if you actually run into them in real life you're doing
something wrong anyway.

```
Welcome to Node.js v19.1.0.
Type ".help" for more information.
> null > 0
false
> null == 0
false
> null >= 0
true
> 100 <= 200 <= 300
true
> 300 >= 200 >= 100
false
> regex = /nani/g;
/nani/g
> regex.test('nani?');
true
> regex.test('nani?');
false
> [7, 12, 13].sort()
[ 12, 13, 7 ]
```

See [wtfjs.com](https://wtfjs.com) for more.

## Summary

JavaScript is the language that runs the web, so it's kinda mandatory.
If you want client-side code to run everywhere, it needs to be in a browser, so
it has to be JavaScript.

But I still think people should learn how to program first, and then learn
JavaScript, rather than the other way around.
Or, at least start with [one of the gazillion languages that transpiles to
JavaScript](https://github.com/jashkenas/coffeescript/wiki/list-of-languages-that-compile-to-js)
so that you don't have to fight language quirks and linters until after your
feet are at least moderately wet.
