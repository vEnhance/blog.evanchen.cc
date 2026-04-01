---
title: Hangul spellcheck for Vim
date: 2024-10-31 13:37
slug: hangul-spellcheck
tags: korean, linux
original_url: 2024/10/31/hangul-spellcheck-for-vim/
status: published
---

_There's got to be a better way to do this. Someone please enlighten me._

Modern Korean is written in 한글 (Hangul), which uses a syllabic alphabet. It
includes spaces between words, unlike Chinese or Japanese, which means that it's
possible to have meaningful spellchecking.

So of course one day I decided I wanted to configure Vim to support
spellchecking Hangul. Unfortunately, there's no file `ko.utf-8.spl` at
[ftp.vim.org](http://ftp.vim.org/vim/runtime/spell/), and in a cursory search I
couldn't find an.

On the other hand, the `hunspell` tool does
[have a Korean dictionary](https://github.com/spellcheck-ko/hunspell-dict-ko),
and there's a
[PKGFILE provided for ARCH](https://aur.archlinux.org/packages/hunspell-ko),
so by running `pikaur -S hunspell-ko` I was able to obtain the files

- `/usr/share/hunspell/ko_KR.aff`
- `/usr/share/hunspell/ko_KR.dic`.

In theory, if you then run the Vim command

`:mkspell /tmp/ko /usr/share/hunspell/ko_KR`

then Vim would create the file `/tmp/ko.utf-8.spl`, which you can then place
into `~/.vim/spell` and get spellchecking.

Unfortunately, theory is not the same as practice, by which I mean that
the process threw a bunch of warnings and the resulting file
it totally didn't work --- every word was being marked as misspelled.

So I spent a bit of time trying to debug it, and being like,
"how come these two words that look exactly the same are showing up as different?"

It turns out there's actually (at least) two different ways to encode of Hangul
into Unicode, namely
[_NFD_ (decomposed) and _NFC_ (composed)](https://w.wiki/BCBd).
The input program I'm using produces NFC glyphs, where each Hangul syllable block is
a single code point; but the spellcheck file
`/usr/share/hunspell/ko_KR.dic` instead has entries in NFD,
where each _atom_ within the syllable block is a character.

![That diff is spooky.]({static}/images/ko-nfd-nfc-diff.png)

Actually, NFD makes sense for a spellchecker,
because you'd want something like 한 (Romanized `han`) and 항 (Romanized `hang`)
to have an edit distance of 1/3 rather than 1.
Then, in order to deal with NFC inputs, the `/usr/share/hunspell/ko_KR.aff`
provides many
[`ICONV` and `OCONV` directives](https://manpages.ubuntu.com/manpages/trusty/en/man4/hunspell.4.html) that tell
the
spellchecker how to convert from NFC input into NFD and then back.
So `hunspell` works well.

The problem is that Vim's `:mkspell` command apparently doesn't actually support
`ICONV` and `OCONV`.
In order to force it to work, I ended up just writing a Python script
that stripped all the unsupported commands from `ko_KR.aff`,
and converted `ko_KR.dic` into NFC format.

```python
import unicodedata

UNSUPPORTED_WORDS = (
    "LANG",
    "WORDCHARS",
    "ICONV",
    "OCONV",
    "AF",
    "MAXCPDSUGS",
    "MAXNGRAMSUGS",
    "MAXDIFF",
    "COMPOUNDMORESUFFIXES",
)

# Make the aff file but take out things unsupported by Vim
with open("/usr/share/hunspell/ko_KR.aff", "r", encoding="utf-8") as infile, open(
    "ko_KR.aff", "w", encoding="utf-8"
) as outfile:
    for line in infile:
        if not any(line.startswith(word) for word in UNSUPPORTED_WORDS):
            print(line.strip(), file=outfile)

# Make the dic file but re-normalize it to NFC
with open("/usr/share/hunspell/ko_KR.dic", "r", encoding="utf-8") as infile:
    content = infile.read()
content = unicodedata.normalize("NFC", content)
with open("ko_KR.dic", "w", encoding="utf-8") as outfile:
    print(content, file=outfile)
```

After storing these mutilated files into
`~/dotfiles/vim/spell/korean-setup/ko_KR`
and running
`:mkspell /tmp/ko ~/dotfiles/vim/spell/korean-setup/ko_KR`,
the outputted `/tmp/ko.utf-8.spl` can now check for spelling errors
(at least if the words are in NFC format).

![It's working. Sorta.]({static}/images/ko-spellcheck-demo.png)

A summary of this process is posted on my
[dotfiles GitHub](https://github.com/vEnhance/dotfiles/tree/main/vim/spell/korean-setup).
To actually use this, just
[download the `ko.utf-8.spl` file directly](https://github.com/vEnhance/dotfiles/tree/main/vim/spell),
no need to re-follow the steps.

The issue is that because the spellcheck dictionary is using NFC now,
while it can highlight the red words, the "suggestions" provided
aren't particularly good.
If you look at the suggestions for the spellcheck for the
typo'd word 항글, the top 10 are:

```text
 1 "한글"
 2 "고글"
 3 "궁글"
 4 "담글"
 5 "답글"
 6 "댓글"
 7 "덧글"
 8 "동글"
 9 "둥글"
10 "빙글"
```

The problem is that because NFD encodes the characters by block,
any change to the entire first syllable cause an equally bad edit distance.
So while I've managed to get quick highlighting of mistakes,
the autocorrection of those mistakes isn't really there.

I feel like this whole process was a convoluted hack.
Is there a better way to do this?
