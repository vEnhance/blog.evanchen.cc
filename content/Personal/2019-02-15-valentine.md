Title: Story: the morning after Valentine's Day
Date: 2019-02-15 13:37
Tags: linux, programming, slice of life
Slug: valentine
Status: published
original_url: 2019/02/15/story-the-morning-after-valentines-day/

When I finally open my eyes and look at the clock, it is 8am. It doesn't _feel_ like it's only been eight hours, though. I've just had a long and complicated dream that I can't remember much of anymore, except that I think I was running a lot, and trying to not die, so I somehow feel sore.

_That NyQuil stuff really works_, I think to myself, and crawl out of bed. (Even though it's like trying to drink mouthwash.) I haven't slept that soundly all week. Or maybe I'm finally slowly recovering from my cold, and that's why that night was better? All I know is that I'm glad I didn't spend another night coughing my lungs out and struggling to get some shut-eye.

I drag my sorry butt out of bed and head over to my nearby computer. It's the Friday morning before [Harvard-MIT math tournament](http://www.hmmt.co/), which means that the server is getting more traffic than usual, and I was supposed to have upgraded the server in anticipation yesterday night. But Valentine's Day was too hectic for me this year, and I never got around to it.

Not hectic for any romantic reasons. It was because I had 5.5 hours of class more or less consecutively, after which I rushed back to my place to teach for another four hours straight, all the while coughing like a banshee. Okay, so maybe I would have slept fine without the NyQuil.

---

Officially, this is supposed to be the software team's job. But the HMMT website has become a complete mess that I think I might be the only person left that still knows more than half of what it's doing. (Well, actually, Banana seems have figured out a lot of it too.) It is sort the equivalent of Frankenstein's monster, with parts being sewn in and out over the last who-knows-how-many-years by random undergraduates with various degrees of competence, and held together by the seams with spit and prayers. The top of the main settings files still reads

    Django settings for mysite project.
    For more information on this file,
    see https://docs.djangoproject.com/en/1.6/topics/settings/
    For the full list of settings and their values,
    see https://docs.djangoproject.com/en/1.6/ref/settings/

where the "1.6" version number still makes me wince every time I see it (that means this file was created _before_ I made the IMO). I am looking forward to the end of this tournament season so I can burn the whole website to the ground and re-write it.

(Making matters worse, in terms of "various degrees of competence", I am on the low end, with no formal CS experience at all. Not good I am in charge.)

So it's time to bump up the servers belatedly. I need to bump the web server and then the database up from t2.micro to m1.medium. There will be some downtime, but no big deal --- everyone's probably still asleep. This should only take a few minutes, and then I can work on getting the grader ready for the approximately 100,000 grading inputs that we're going to force-feed it on Saturday.

So I push a few buttons, and let Amazon Web Services do its magic, just like the last five times I had to do this.

---

Something's wrong. It's been ten minutes already, and the website still won't load. The upgrades should be done by now. I refresh again, and realize that it's throwing a 500 error.

I feel a twinge of despair, which causes my cough to start to return. Looks like the NyQuil wore off. _It always starts like this. One little error, followed by another, and then..._ I clench my teeth and SSH into the new server, and navigate to the log files (which I remember having to set up myself a few years ago, precisely for situations like this).

And indeed, when I get there, the same message is repeated, over and over, for the last several minutes, like a harbinger of doom:

    OperationalError: (1045, "Access denied for user 'ebroot'@'xx.xx.xx.xx' (using password: YES)")

Oh, well, here we go.

---

My first guess is [VPC groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html), which have bitten me plenty in the past. Unfortunately, tinkering with these has no effect, so it seems like there is something new going on.

I double-check and triple-check the password, but it seems right. (This is the same error you get if you enter the wrong password!) So that's not it, either.

This is a connection issue, so, the first thing I want to do is figure out whether the issue is with the upgraded server or the upgraded database. So, I go to my command bar and launch MySQL workbench, which promptly gives me

    mysql-workbench: command not found

Oh, right, I don't have Workbench installed on my desktop. So I go over to my laptop, which does have it, and try to fire up a connection to the database. This time, it gives me

    喊叫 org.freedesktop.secrets 發生錯誤

Uhh, what? Okay, I have a keyring error of some sort here. I decide it's not worth it to try to fix the workbench, and decide to do it the old fashioned way. I fire another terminal and call mysql, which promptly returns with:

    mysql: command not found

Great. Okay, well, I guess I can install it, no problem. So I type in `sudo pacman -S mysql` which gives

    :: 有 2 個提供者可供 mysql：

    :: 軟體庫 extra

    1) mariadb

    :: 軟體庫 community

    2) percona-server

    輸入某個數字（預設=1）:

Huh? Oh, [Arch Linux prefers MariaDB over MySQL](https://wiki.archlinux.org/index.php/MySQL), I remember now. That means SQL, unlike MariaDB, is not pre-packaged, and I'll need to download it from the [Arch User Repository](https://wiki.archlinux.org/index.php/AUR) and compile it form source. So I download the PKGBUILD and let it start going.

Unfortunately, this means that the binary needs to build from source, and so maybe minutes later I'm staring at the build progress and it's at 14%. All the while the website is down, and people are starting to notice. I can feel the tension all over my body as I realize that the tournament will simply not function if I can't get this back up and working, and the [nightmare from February 2018](https://s3.amazonaws.com/hmmt-archive/february/2018/apology.html) starts coming back to my mind again. I explode into a symphony of coughs as I struggle to gain my composure.

The compile-from-source doesn't respond to my please. I decided that's not good enough, and I have to do something faster.

---

At this point I decide I maybe should get help, so I hit up Banana who has saved HMMT on numerous occasions as well, and ask him why I can't connect to the HMMT database. He's done so successfully on his computer in the past, and he even has a little script he's written to do so. His response puzzles me:

"Seems connectable. Might need to reset your DNS?"

Uh, what?

This is the only lead I have to go after, so I start prodding him like crazy, since I can't seem to get it to do anything from my end. At first I get a couple suggestions, which don't work, but eventually Banana finally gives me:

"Uhhhh. Can you try running db-connect on your machine and going from there? I have to start hauling."

Right. Unlike me, Banana is actually helping the directors move around the 30 gallons of apple juice and 50 gallons of mango nectar and way-too-many gallons of water that will be used today or tomorrow. So I am really on my own.

---

At least I now know that it's on the database end, sorta. I quickly locate db-connect: it's the mini-script that Banana has been using to do the connection. Maybe this will let me get in and see what's happening. I type:

    ./db-connect.sh dev

which promptly gives

    mysql: command not found

Ah right, we're still working on that, huh? The sql compilation is going nowhere fast, and so I have to think of something else.

I think of one possible approach: the workbench won't work on my laptop, but maybe it'll work on my desktop? I order pacman to install MySQL Workbench on my desktop too, and after a couple dozen agonizing seconds, the download is all done. To my delight, there is no error about org.freedesktop.secrets, and so I impatiently set everything up and login to find:

    ERROR 1045 (28000):
    Access denied for user 'ebroot'@'xx.xx.xx.xx' (using password: YES)

_Oh, no, no, no._ I explode into another fit of coughs which prevent me from screaming at the monitor in frustration.

---

At this point, I decide this isn't worth fighting. I can figure it out another time. For now, _the show must go on_.

That means that if I restore a backup of the old database --- reverting it back to how it was yesterday, when everything went totally fine --- then I can at least get the computer to work now, and worry about what the error was later.

Unfortunately, this is a painfully slow process. (The way backups work is that they don't _replace_ the existing database. Instead, it creates a brand new database somewhere on the cloud, but that has a copy of the same data as the point in time.) I load the backup, and twitch in agony as it slowly creates a new database from the image, setting everything back to how it was earlier. I hope that's good enough.

After what feels like an eternity, the database is all set. I change the pointer of my now-working WorkBench to the new database and try to connect to see what happens, only to be greeted with 45 seconds of nothing, followed by a simple error message telling me that the connection failed.

Why? Oh yeah, I didn't send the VPC for the new database. I do that, exhaling, it should be fine now, and connect to the new restored database, only to find:

    ERROR 1045 (28000):
    Access denied for user 'ebroot'@'xx.xx.xx.xx' (using password: YES)

I practically choke on my own spit, which results in another several seconds of me wheezing like heck.

_Nooooooooooooooooooooooo._

Okay, I have to fix this now.

---

The only clue I have is that the database script from Banana still works. But on my computer I can't for some reason run it.

I go back to Google (which I have been using extensively the whole time), and then after another few minutes of frantic searching, realize that MariaDB is actually good enough for me: once I have that installed, I'll have a (slightly different) SQL client, but the script should work. Hmm.

Since MariaDB is pre-packaged, that means the installation is easy, and I run it. This might be it. I fire the script again, and run into:

    mysql: unknown option '--enable-cleartext-plugin'

Oh, huh. Okay, well, maybe it doesn't matter. I delete that flag from the script, and get

    mysql: unknown variable 'ssl-mode=VERIFY_IDENTITY'

Uhh. Let's cross our fingers that doesn't matter either? I try that again, and --- much to my amazement --- the connection works.

I start examining the db-connect script closely, and see that instead of the user `ebroot` it's connecting using some user name `dev`. So maybe there is some new permission issues with `ebroot`? With my new connection, I try to

    GRANT ALL PRIVILEGES ON *.* TO 'ebroot'@'%';

which then returns with the following message:

    ERROR 1045 (28000):
    Access denied for user 'dev'@'%' (using password: YES)

Uhhh.

Okay, maybe something else. I read the db-connect script again. Is there anything else that's different? Well, there's one more change in the code that I can at least work with: there is a CA certificate that's being used.

I fire up WorkBench again, and try to log in again, but this time I pass a newfound CA certificate (appropriately named _rds-combined-ca-bundle.pem_) and to my relief, I find that I can now log in as ebroot. That's the issue!

---

Except I have no idea how to make Django do that and I have no intention if finding out. But another Google search suggests the answer: now that I'm finally connected with ebroot I type

    ALTER USER 'ebroot'@'%' REQUIRE NONE;

And breathed a sigh of relief when I refreshed hmmt.co, and harmony was restored in the world.

I looked at the clock. It was 11am. There goes my whole morning. I go downstairs to drink a bottle of Soylent for breakfast, resolving to never become a programmer for a living, or at least to get some proper training first if I ever consider it.

Meanwhile, the rest of the Harvard-MIT math tournament go on with their day, blissfully unaware of the debacle narrowly averted.
