import asyncio

from pyrogram import Client, filters
from configs.main_config import HANDLERS
from configs.love_config import HEART
from WataRobot.plugins.modules.methods import *


@Client.on_message(filters.command("love", HANDLERS) & filters.me)
async def love(_, message):
    for frame in HEART:
        await try_edit_message(message, frame)
        await asyncio.sleep(0.16)
    return

