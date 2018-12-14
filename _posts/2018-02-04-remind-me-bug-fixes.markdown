---
title: Remind Me bug fixes
layout: post
tags: Remind-Me Update
---
Ver. ***1.2.1***

<img src="{{ site.baseurl }}/images/posts/crazy_remind_me_times.png" width="500" alt="Crazy Remind Me Times"><br>
This update is just a quick patch to fix a major issue to Remind Me. It turns out that super long Remind Me times and CS Pound do not work well together, causing it to crash when one is set. After testing to see how long I can Remind Me for before the bot crashes, I decided to settle with 24 hours instead. It is very unlikely for the pound to have more than a 1-day gap between opening times, and most server events cycle after each day, so 24 hours seems like a good candidate.

Changelog:
* Fixed long times crashing **,remindme** command
