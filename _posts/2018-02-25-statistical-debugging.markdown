---
title: Statistical Debugging
layout: post
tags: Remind-Me Statistics Update
---
Ver. ***1.4.1***

Not sure if you have noticed this, but I usually test new features and fix bugs directly on the live bot itself (Which probably explains why the bot goes offline for quite some time sometimes). This means that any changes I make would cause the bot to restart with those new changes. This is all well and good for fixing bugs, but not so good if I create a new feature that has bugs everywhere. Trying to run a separate local copy of the bot proved to be an issue as some of the methods I use to get bot statistics only works in Linux. This update should fix these issues and allow it to be able to run on any OS.

Some other noticable changes include **,stats** is now an alias to **,statistics**, and **,remindme** can now be called with just **,rm**.


Changelog:
* Renamed **,stats** command to **,statistics**
* Changed 'CS Pound Memory Usage' to display in MB instead of a percentage
* Improved response time of **,statistics**
* Added **,rm** alias to **,remindme** command
* Added **,stats** alias to **,statistics** command
* Fixed 'System Memory Usage' not displaying when running on OSX
* Fixed 'CS Pound Memory Usage' not displaying when running on OSX
* Fixed 'CS Pound Uptime' not displaying when running on OSX

Command Usage
============
```
,statistics
,stats
,rm <Xh|Xhr|Xm|Xs>
```
