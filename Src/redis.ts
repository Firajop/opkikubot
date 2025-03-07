/**
* opkikubot - UserBot
* Copyright (C) 2020 opgohil
*
* This file is a part of < https://github.com/opgohil/opkikubot/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/opgohil/opkikubot/blob/main/LICENSE/>.
**/

import redis from 'redis';
import env from './env';

const host = env.REDIS_URI.split(":")[0];
const port = Number(env.REDIS_URI.split(":")[1]);

const client = redis.createClient({
    host: host,
    port: port,
    password: env.REDIS_PASSWORD
});

export default client;
