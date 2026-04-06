---
title: Email, JetPack, and Wintermelon
date: 2014-01-01 13:37
slug: wintermelon
tags: linux
original_url: 2014/01/01/email-jetpack-and-wintermelon/
status: published
---

So I guess I can resume blogging now, seeing that I'm done with college applications (at last!).
I'm not sure what I plan to blog about in general,
but I figured I might as well put this domain name to good use :) I also
realized that writing things out helped me clarify my thinking a lot (actually
Qiaochu Yuan recommended this for math in particular),
so I'll be trying to do that more often this $2014 = 2 \cdot 19 \cdot 53$ and onwards.

Onto the actual content, anyways.
In this post I'll talk about the inspiration and development for one of my afternoon projects,
which I've named **wintermelon** for no good reason.

A while back Jacob Steinhardt recommended to the SPARC alumni list that we check
our email at most twice a day.
I was able to follow this suggestion for a day,
and really was impressed by the feeling -- I realized that I had started to use email as a distraction,
something to prevent my brain from realizing it wasn't do anything.
The same went for the Art of Problem Solving forums (which I frequently visit) as well as Facebook,
so I also tried limiting the number of times I checked each of those each day.
Unfortunately, old habits do not die easily,
and I found myself automatically visiting those sites when I wasn't doing anything.

A couple days ago while I was reviewing my goals and realizing that I wasn't following this one,
I remembered the title text of [XKCD 862](http://xkcd.com/862/).

![XKCD 862.](https://imgs.xkcd.com/comics/let_go.png)

> After years of trying various methods, I broke this habit by pitting my impatience against my laziness.
> I decoupled the action and the neurological reward by setting up a simple
> 30-second delay I had to wait through, in which I couldn't do anything else,
> before any new page or chat client would load (and only allowed one to run at once).
> The urge to check all those sites magically vanished--and my 'productive' computer use was unaffected.

Sounded like fun! The XKCD version seemed a little extreme,
but I could definitely do with a script that would make me wait 50 seconds before reading Facebook.
I estimated it would take me about two hours to read/learn the API and write the code to put this together;
it turns out my estimate was roughly correct.

I'm a Firefox user, so it made sense for me to try and put this together as a Firefox extension.
A quick Google search led me to [Jetpack](https://developer.mozilla.org/en-US/docs/Jetpack),
which offered to let me build an FF extension quickly using just JS.
They had [very nice tutorials](https://addons.mozilla.org/en-US/developers/docs/sdk/latest/dev-guide/tutorials/index.html#getting-started),
too.

Drilling down, the things I needed to make this thing fly were:

1. Something to trigger every time a webpage was launched.
   This was conveniently covered under "Listen for page load".
2. Something to actually lock the webpage.
   This was easy, I just put `body.style.visibility = "hidden";` in JS.
3. Timers for a delay. This was handled by the JS `window.setTimeout()`.
4. Something to store the websites and their associated delays.
   I used regular expressions to specify the domain.
   This I did kind of painlessly through the Jetpack simple-prefs,
   but it was kind of an ugly hack in that I manually defined six settings for up to six websites.
   Maybe sometime when I'm bored I will take the time to make this work for arbitrarily many websites.
5. A way for the individual lockdown scripts to communicate with the main script and vice-versa.
   This took me a while to figure out, but it is essentially a bunch of emit/on hooks provided in Jetpack.
   I would inject a script lockdown.js into the page and the send it a signal
   with the amount of time to lock the page.

It was actually very straightforward in retrospect, and took only a couple files of actual code.
The project (which is very small) is [posted on my GitHub](https://github.com/vEnhance/wintermelon).
My estimate was about right; it took me approximately 2.5 hours from start to finish,
although I admit that I was also chatting on Google Talk in the meantime.
Actually I'm embarrassed it took as long as that.

The core of the program really is just two files. Here is lib/main.js, which is run from the start.

```javascript
var tabs = require("sdk/tabs");
var self = require("sdk/self");
var prefs = require("sdk/simple-prefs").prefs;

// TODO make these not suck
var regex_strings = new Array();
regex_strings[0] = prefs.regex1;
regex_strings[1] = prefs.regex2;
regex_strings[2] = prefs.regex3;
regex_strings[3] = prefs.regex4;
regex_strings[4] = prefs.regex5;
regex_strings[5] = prefs.regex6;

var lock_times = new Array();
lock_times[0] = prefs.time1;
lock_times[1] = prefs.time2;
lock_times[2] = prefs.time3;
lock_times[3] = prefs.time4;
lock_times[4] = prefs.time5;
lock_times[5] = prefs.time6;

// Create regular expressions
var N = regex_strings.length;
var regexes = new Array();
for (var i = 0; i < regex_strings.length; i++) {
  regexes[i] = new RegExp(regex_strings[i]);
}

var prev_hit = -1;
var lockdown = false; // Are we currently in a lockdown?

function lock(time) {
  worker = tabs.activeTab.attach({
    contentScriptFile: self.data.url("lockout.js"),
  });
  worker.port.emit("lock", time); // tell the worker to lock
  worker.port.on("unlock", unlock);
  lockdown = true; // prevent side loading
}

function gateway(tab) {
  url = tab.url;
  if (lockdown) {
    // Currently under a lockdown
    // Do not allow any other tabs to load
    lock(lock_times[prev_hit]);
    return;
  }
  for (var i = 0; i < N; i++) {
    var regex = regexes[i];
    if (regex.test(url) && regex_strings[i] != "") {
      if (prev_hit != i) {
        // Test positive, we are going to block
        lock(lock_times[i]);
        prev_hit = i; // Remember prev hit
        return;
      } else {
        prev_hit = i; // Still remember prev hit
        return;
      }
    }
  }
  prev_hit = -1; // Release
}

function unlock() {
  lockdown = false;
}

tabs.on("ready", gateway);
```

and here is the `data/lockout.js` that is called by the `lock` function:

```javascript
function lock(time) {
  document.getElementsByTagName("body")[0].style.visibility = "hidden";
  if (time >= 0) {
    window.alert("Locking for " + time + " seconds.");
    window.setTimeout(unlock, time * 1000);
  } else {
    window.alert("Locking indefinitely.");
  }
}

function unlock() {
  window.alert("Done");
  document.getElementsByTagName("body")[0].style.visibility = "visible";
  self.port.emit("unlock");
}

self.port.on("lock", lock);
```

More pragmatically, I've been using it for only a couple days, but it seems to be working!
Blank pages are not very good distractions. We'll see if this holds up.
