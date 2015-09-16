#!/usr/bin/env python

import settings

from bot import Bot

bot = Bot(settings.SLACK_TOKEN)

bot.start()
