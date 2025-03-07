# opkikubot - UserBot
# Copyright (C) 2020 opkikubot
#
# This file is a part of < https://github.com/opgohil/opkikubot/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/opgohil/opkikubot/blob/main/LICENSE/>.

from telethon import custom, events
from telethon.utils import get_display_name

from . import *


@opkikubot_bot.on(
    events.NewMessage(
        incoming=True,
        func=lambda e: (e.mentioned),
    ),
)
async def all_messages_catcher(e):
    if udB.get("TAG_LOG"):
        try:
            NEEDTOLOG = int(udB.get("TAG_LOG"))
        except Exception:
            return LOGS.warning("you given Wrong Grp/Channel ID in TAG_LOG.")
        x = await opkiku_bot.get_entity(e.sender_id)
        if x.bot or x.verified:
            return
        y = await opkiku_bot.get_entity(e.chat_id)
        if y.username:
            yy = f"[{get_display_name(y)}](https://t.me/{y.username})"
        else:
            yy = f"[{get_display_name(y)}](https://t.me/c/{y.id}/{e.id})"
        xx = f"[{get_display_name(x)}](tg://user?id={x.id})"
        msg = f"https://t.me/c/{y.id}/{e.id}"
        if e.text:
            cap = f"{xx} tagged you in {yy}\n\n```{e.text}```\nㅤ"
        else:
            cap = f"{xx} tagged you in {yy}"

        btx = "📨 View Message"

        try:
            if e.text:
                cap = get_string("tagnot_1").format(xx, yy, e.text, msg)
            else:
                cap = get_string("tagnot_2").format(xx, yy, msg)
            await asst.send_message(
                NEEDTOLOG,
                cap,
                link_preview=False,
                buttons=[[custom.Button.url(btx, msg)]],
            )
        except BaseException:
            if e.text:
                cap = get_string("tagnot_1").format(xx, yy, e.text, msg)
            else:
                cap = get_string("tagnot_2").format(xx, yy, msg)
            try:
                await ultroid_bot.send_message(NEEDTOLOG, cap, link_preview=False)
            except BaseException:
                pass
    else:
        return
