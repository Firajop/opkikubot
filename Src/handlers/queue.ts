/**
* opkikubot - UserBot
* Copyright (C) 2020 opgohil
*
* This file is a part of < https://github.com/opgohil/opkikubot/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/opgohil/opkikubot/blob/main/LICENSE/>.
**/

import { Composer } from 'telegraf';
import { getQueue } from '../tgcalls';
import escapeHtml from '@youtwitface/escape-html';
import { getDuration } from '../utils';

export const queueHandler = Composer.command('queue', async ctx => {
    const { chat } = ctx.message;

    if (chat.type !== 'supergroup') {
        return;
    }

    const queue = getQueue(chat.id);
    const message =
        queue && queue.length > 0
            ? queue.map((data, index) => {
                const { info, from } = data;
                return `<b>${index + 1} -</b> <a href="https://www.youtube.com/watch?v=${info.id}">${escapeHtml(info.title)}</a> (${getDuration(info.duration)})\n<b>Requested By :</b> <a href="tg://user?id=${from.id}">${from.f_name}</a>\n`
            }).join('\n')
            : 'The queue is empty.';

    await ctx.replyWithHTML(message, { disable_web_page_preview: true });
});
