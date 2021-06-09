# opkikubot - UserBot
# Copyright (C) 2020 opkikubot
#
# This file is a part of < https://github.com/opgohil/opkikubot/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/opgohil/opkikubot/blob/main/LICENSE/>.


from telethon.errors import ChatSendInlineForbiddenError

from . import *

REPOMSG = (
    "• **OPKIKU USERBOT** •\n\n",
    "• Repo - [Click Here](https://github.com/OPGOHIL/OPKIKUBOT)\n",
    "• Support - @OPGOHIL",
)


@opkiku_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await opkikubot_bot.inline_query(Var.BOT_USERNAME, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == opkikubot_bot.uid:
            await e.delete()
    except ChatSendInlineForbiddenError:
        await eor(e, REPOMSG)
