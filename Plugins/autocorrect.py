# opkikubot - UserBot
# Copyright (C) 2020 opkikubot
#
# This file is a part of < https://github.com/opgohil/opkikubot/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/opgohil/opkikubot/blob/main/LICENSE/>.

"""
✘ Commands Available

• `{i}autocorrect`
    To on/off Autocorrect Feature.

"""

from gingerit.gingerit import GingerIt
from googletrans import Translator
from telethon import events

from . import *

tr = Translator()


@opkiku_cmd(pattern="autocorrect")
async def acc(e):
    if Redis("AUTOCORRECT") != "True":
        udB.set("AUTOCORRECT", "True")
        await eor(e, "AUTOCORRECT Feature On")
    else:
        udB.delete("AUTOCORRECT")
        await eor(e, "AUTOCORRECT Feature Off")


@opkiku_bot.on(events.NewMessage(outgoing=True))
async def gramme(event):
    if Redis("AUTOCORRECT") != "True":
        return
    t = event.text
    tt = tr.translate(t)
    if t.startswith((HNDLR, ".", "?", "#", "_", "*", "'", "@", "[", "(", "+")):
        return
    if t.endswith(".."):
        return
    if tt.src != "en":
        return
    xx = GingerIt()
    x = xx.parse(t)
    res = x["result"]
    await event.edit(res)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
