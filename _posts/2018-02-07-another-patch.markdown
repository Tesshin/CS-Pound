---
title: Another patch!
layout: post
tags: Pet Remind-Me Time Update
---
Ver. ***1.2.3***

<img src="{{ site.baseurl }}/images/posts/pound_alias.png" width="500" alt="Pound Alias"><br>
I don't think these small patches will ever end... Anyways, this update brings some small changes to all the commands. Currently, the title of the embed shown in the **,pet** command is just a generic 'Pet'. With this update it now shows "[Owner]'s Pet", which is hopefully better. I have also fixed a new issue with **,pet**, this time with PPS pets. Because there is no API for Chicken Smoothie, I'm just pulling everything as is off the pet link. PPS pets have an extra row at the top showing that it is a PPS pet, which broke the code I had written to read off each row. I have now accommodated for that and it should work now!

As for the **,time** command, I often browse through #pound-talk or #commands channels in CS servers to see how users are using the commands and if any bugs will appear. While browsing for some reason I see users trying to call the **,time** command with **,pound** instead, which makes sense, but doesn't work. This update now allows both **,time** and **,pound** to be able to be used to check the pound times!

The changes for **,remindme** is only a small fix to it only working with lowercase letters. Now it can work with uppercase letters or even a mix of both!

Changelog:
* Added owner's name to **,pet** command's embed title
* Added **,pound** alias for **,time** command
* Fixed PPS pets not working with **,pet** command
* Fixed capitalised letters not working with **,remindme** command

## Command Usage
```
,pound
,remindme <XH|XM|XS>
```
