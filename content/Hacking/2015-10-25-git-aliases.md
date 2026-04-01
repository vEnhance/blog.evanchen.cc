Title: Git Aliases
Date: 2015-10-25 13:37
Tags: linux
Slug: git-aliases
Status: published
original_url: 2015/10/25/git-aliases/

For Git users:

I've recently discovered the joy that is git aliases,
courtesy of [this blog post](http://durdn.com/blog/2012/11/22/must-have-git-aliases-advanced-examples/).
To return to the favor, I thought I'd share the ones that I came up with.

For those of you that don't already know, Git allows you to make aliases -- shortcuts for commands.
Specifically, if you add the following lines to your .gitconfig:

    [alias]
    	cm = commit
    	co = checkout
    	br = branch

Then running `git cm` will expand as `git commit`, `git co master` is `git checkout master`, and so on.
You can see how this might make you happy because it could save a few keystrokes.
But I think it's more useful than that -- let me share what I did.

The first thing I did was add

    pu = pull origin
    psh = push origin

and permanently save myself the frustration of forgetting to type `origin`. Not bad.
Even more helpful was the command

    undo = reset --soft HEAD~1

Thus if I make a commit and then decide I want to undo it, rather than having
to remember (or Google) what the correct incantations were, I just have to type `git undo`.
It's really an undo button!

Now for the fun part -- some of Git's useful commands are pretty verbose and take up lots of space.
For example, here's what git status looks like:

![git status]({static}/images/git-status.png)

Kind of verbose if you ask me, and by now I know what "git pull" does.
Fortunately, it turns out that there are some options you can run to make this look nicer.
All you have to do is say `git status -s -b`, or in the context of this post, set the alias

    ss = status -s -b

Then you get

![git ss]({static}/images/git-alias-ss.png)

which is much cooler.

Similarly, `git log` takes up a lot of space. I have the following format,
which I've edited from the above blog post to suit my own tastes.

    ls = log -n 16 --pretty=format:"%C(yellow)%h\\ %C(cyan)[%cn]\\ %C(reset)%s\\ %C(red)%d" --decorate
    ll = log -n 6 --pretty=format:"%C(yellow)%h\\ %C(cyan)[%cn]\\ %C(reset)%s\\ %C(red)%ad" --decorate --date=short --stat

These give in my opinion the much more readable format
![git-alias-l.png]
If you're on a branch that does merges, you might also have fun with

    tree = log -n 16 --pretty=format:"%C(yellow)%h\\ %C(cyan)[%cn]\\ %C(reset)%s\\ %C(red)%d" --decorate --graph

which will put these into a graphical tree for your viewing pleasure.

And finally a few more that I find nice, some again taken directly from the link above:

    fail = commit --amend # to avoid stupid "oops typo" commits
    rb = rebase
    rbc = rebase --continue
    bis = bisect
    dc = checkout -
    assume = update-index --assume-unchanged
    unassume = update-index --no-assume-unchanged
    assumed = "!git ls-files -v | grep ^h | cut -c 3-"

(Here "dc" is short for "discard", since `git dc file` discards the changes to that file.)
And that's just the beginning of what you can do!

Preemptive answer: I'm also using
[git-completion](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash) (for
tab-completing in git) and
[git-prompt](https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh) with the line

    export PS1='[\033[0;32m]${debian_chroot:+($debian_chroot)}\u@\h [\033[0;33m]\w$(__git_ps1 " [\033[1;31m]#%s")\n[\033[0m]\$ '

in my bashrc. That's where the branch indicators are coming from.
The terminal is XFCE4.
