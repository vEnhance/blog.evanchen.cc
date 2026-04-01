Title: PDF Compression
Date: 2014-02-01 13:37
Tags: linux
Slug: pdf-compress
Status: published
original_url: 2014/02/01/pdf-compression/

I always scan copies of letters into my computer before I send them out.
So I had a bunch of large PDF's sitting around hogging my Dropbox space.

One day I found [this blog post](http://pandemoniumillusion.wordpress.com/2008/05/07/compress-a-pdf-with-pdftk/)
which claimed that simply running (in Bash) the commands

```
$ pdf2ps original.pdf temp.ps
$ ps2pdf temp.ps new.pdf
```

would decrease the file size.
(The two commands are part of GhostScript,
which I had installed on my Linux boxes anyways.) I couldn't resist trying it -- and miraculously, it worked.
It generally decreases my scans by a factor of 10 (from 20MB to 2MB or so).

I have no clue why this works,
although it probably has something to do with the fact that the PDF's are scanned pages .
Anyone care to enlighten me?
