# opkikubot - UserBot
# Copyright (C) 2020 opkikubot
#
# This file is a part of < https://github.com/opgohil/opkikubot/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/opgohil/opkikubot/blob/main/LICENSE/>.

from pyopkikubot import *
from pyopkikubot.dB.database import Var
from pyopkikubot.functions.all import *
from telethon import Button, custom

from strings import get_languages, get_string

OWNER_NAME = opgohil_bot.me.first_name
OWNER_ID = opgohil_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
