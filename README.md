# opkikubot  

  <b>OPKIKU - UserBot</b>
</h1>

<b>A stable pluggable Telegram userbot + vc music bot, based on Telethon.</b>   


[![Forks](https://img.shields.io/github/forks/opgohil/opkikubot?style=flat-square&color=orange)](https://github.com/opgohil/opkikubot/fork)
[![Size](https://img.shields.io/github/repo-size/opgohil/opkikubot?style=flat-square&color=green)](https://github.com/opgohil/opkikubot)   
[![Python](https://img.shields.io/badge/Python-v3.9-blue)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/opgohil/opkikubot/graphs/commit-activity)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/opgohil/opkikubot)   
[![Contributors](https://img.shields.io/github/contributors/TeamUltroid/Ultroid?style=flat-square&color=green)](https://github.com/opgohil/opkikubot/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/opgohil/opkikubot)   
[![Sparkline](https://stars.medv.io/opgohil/opkikubot.svg)](https://stars.medv.io/opgohil/opkikubot)

----

# Deploy
- [Heroku](#Deploy-to-Heroku)
- [Local Machine](#Deploy-Locally)

# Documentation 
[![Document](https://img.shields.io/badge/Documentation-opkikubot-blue)](https://github.com/opgohil/opkikubot)

# Tutorial 
- Full Tutorial - [![Full Tutorial](https://img.shields.io/badge/Watch%20Now-blue)]()

- Tutorial to get Redis URL and password - [here.](./resources/extras/redistut.md)
---

## Deploy to Heroku
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Deploy Locally
- [Traditional Method](#local-deploy---traditional-method)
- [Easy Method](#local-deploy---easy-method)

### Local Deploy - Easy Method
- Windows - `cd desktop ; wget https://del.dog/raw/opkikubot-termux -o locals.py ; python locals.py`
- Termux - `sh -c "$(curl -fsSL https://del.dog/raw/opkikubot-termux-deploy)"`

### Local Deploy - Traditional Method
- Get your [Necessary Variables](#Necessary-Variables)
- Clone the repository: <br />
`git clone https://github.com/opgohil/opkikubot.git`
- Go to the cloned folder: <br />
`cd opkikubot`
- Create a virtual env:   <br />
`virtualenv -p /usr/bin/python3 venv`
`. ./venv/bin/activate`
- Install the requirements:   <br />
`pip(3) install -U -r requirements.txt`
- Generate your `SESSION`:
  - For Linux users:
    `bash sessiongen`
     or
    `bash -c "$(curl -fsSL https://del.dog/tipynureen.sh)"`
  - For Termux users:
    `sh -c "$(curl -fsSL https://del.dog/Telegra-php.txt)"`
  - For Windows Users:
    `cd desktop ; wget https://del.dog/opgokikubot -o opgohil.py ; python opkikubot.py`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/opgohil/opkikubot/blob/main/.env.sample).
(You can either edit and rename the file or make a new file named `.env`.)
- Run the bot:
  - Linux Users:
   `bash resources/startup/startup.sh`
  - Windows Users:
    `python(3) -m pyopkikubot`

## Necessary Variables
- `API_ID` - Your API_ID from [my.telegram.org](https://my.telegram.org/)
- `API_HASH` - Your API_HASH from [my.telegram.org](https://my.telegram.org/)
- `SESSION` - SessionString for your accounts login session. Get it from [here](#Session-String)
- `BOT_TOKEN` - The token of your bot from [@BotFather](https://t.me/BotFather)
- `BOT_USERNAME` - The username of your bot from [@BotFather](https://t.me/BotFather)
- `LOG_CHANNEL` - A private group/channel id.
- `REDIS_URI` - Redis endpoint URL, from [redislabs](http://redislabs.com/), tutorial [here.](./resources/extras/redistut.md)
- `REDIS_PASSWORD ` - Redis endpoint Password, from [redislabs](http://redislabs.com/), tutorial [here.](./resources/extras/redistut.md)

## Session String
Different ways to get your `SESSION`:
* [![Run on Repl.it]()]()
* Linux : `bash -c "$(curl -fsSL )"`
* PowerShell : `cd desktop ; wget  ; python opkikuboy.py`
* Termux : `sh -c "$(curl -fsSL )"`

Made with ðŸ’• by [@Teamopgohil](https://t.me/opgohil). <br />

# License
OPGOHIL is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)

# Credits
* [![Teamopgohil-GUJJUOPGOHIL](https://img.shields.io/static/v1?label=Teamopgohil&message=gujjuopgohil&color=critical)](https://t.me/GUJJUOPGOHIL)
* [![Teamopkiku-yash](https://img.shields.io/static/v1?label=Teamulkiku&message=yash&color=critical)](https://t.me/KIKU_NETWORKS)



# Mandatory Vars

- Only two of the environment variables are mandatory.

- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

    - `APP_ID`:   You can get this value from https://my.telegram.org

    - `API_HASH`:   You can get this value from https://my.telegram.org

- The userbot will not work without setting the mandatory vars.
