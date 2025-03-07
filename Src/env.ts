/**
* opkikubot - UserBot
* Copyright (C) 2020 opgohil
*
* This file is a part of < https://github.com/opgohil/opkikubot/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/opgohil/opkikubot/blob/main/LICENSE/>.
**/

import { cleanEnv, str } from 'envalid';
import dotenv from 'dotenv';

dotenv.config();

export default cleanEnv(process.env, {
    BOT_TOKEN: str(),
    WEBSOCKET_URL: str(),
    REDIS_URI: str(),
    REDIS_PASSWORD: str(),
    LOG_CHANNEL: str()
});
