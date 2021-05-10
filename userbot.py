# import logging
from pyrogram import Client, idle

PLUGINS = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client("tgvc", plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> Ʌɗɩtƴɑ Ɱʉsɩƈ Ƥɭɑƴɘr Stɑrtɘɗ')
idle()
app.stop()
print('\n>>> Ʌɗɩtƴɑ Ɱʉsɩƈ Ƥɭɑƴɘr Støƥpɘɗ')
