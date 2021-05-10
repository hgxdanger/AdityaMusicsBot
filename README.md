# Ʌɗtɩƴɑ Ɱʉsɩƈ Ƥɭɑƴɘr (ɄsɘrƁøt)

Ʌɗtɩƴɑ Ƭɘɭɘʛrɑɱ ɄsɘrƁøt Ƭø Ƥɭɑƴ Ʌʉɗɩø Iɳ Ƭɘɭɘʛrɑɱ Vøɩƈɘ Ƈɦɑts.

<p align="center">
  <img src="https://telegra.ph/file/8b4520f3f471e3ce253ee.jpg">
</p>

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AdityaHalder/AdityaMusicsBot/)

- Generate Pyrogram session string by
  running [generate-pyrogram-session-string.py](generate-pyrogram-session-string.py)
  by yourself or
  through [Replit](https://replit.com/@dashezup/generate-pyrogram-session-string)
- Enable the worker after deploy the project to Heroku
- send `.ping`, `.uptime`, or `.sysinfo` from userbot account itself or its
  contacts to check if the userbot is running
- Send `.join` to a voice chat enabled group chat from userbot account itself
  or its contacts
- Reply to an audio with `/play` to start playing it in the voice chat, every
  member of the group can use the `.play` and other common commands now,
  check `.help` for more commands

## Introduction

**Features**

- Playlist, queue
- Loop one track when there is only one track in the playlist
- Automatically downloads audio for the first two tracks in the playlist to
  ensure smooth playing
- Automatically pin the current playing track
- Show current playing position of the audio

**How to Use**

You can't play and listen in the same voice chat at the same time, it's
recommended to run the userbot with your alt account and control the userbot
with your main account by adding your main account as a contact of the alt
account.

1. Start the userbot, try `.ping`, `.uptime` or `.sysinfo` command to check if
   the bot was running.
2. send `.join` to a voice chat enabled group chat from userbot account itself
   or its contacts, be sure to make the userbot account as group admin and give
   it at least the following permissions:
    - Delete messages
    - Manage voice chats (optional)
3. reply to an audio with `/play` to start playing it in the voice chat, every
   member of the group can use common commands such like `/play`, `/current`
   and `.help` now.
4. check `.help` for more commands
