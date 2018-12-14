---
title: Statistical Stats
layout: post
tags: Remind-Me Statistics Update
---
Ver. ***1.4***

<img src="{{ site.baseurl }}/images/posts/stats_command.png" width="400" alt="Stats Command"><br>
At the moment the only statistical information the bot has is the current version of the bot, displayed in the playing status. Some of the other bots I have been looking at have a specific command that shows many of the bot's statistics, such as CPU/RAM usage, server and user counts. So now I have created my own **,stats** command, and moved the bot version there, along with some other information.

Also a small problem I have seen with users setting Remind Me's is typing 'hr' instead of just 'h' for hours. It has now been updated to work for both 'hr' and 'h'!

Changelog:
* Added **,stats** command
* Fixed 'hr' not working with **,remindme** command

## Command Usage
```
,remindme <Xh|Xhr|Xm|Xs>
,stats
```
