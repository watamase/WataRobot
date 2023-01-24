from pyrogram import Client, filters
from configs.main_config import HANDLERS
from configs.info_config import *
from WataRobot.plugins.modules.methods import *


@Client.on_message(filters.command("info", HANDLERS) & filters.me)
async def info(_, message) -> None:
    reply_message = message.reply_to_message

    if not reply_message:
        await try_edit_message(message, user_info_text(message.from_user))
    else:
        if reply_message.from_user:
            await try_edit_message(message, user_info_text(reply_message.from_user))
        else:
            await try_edit_message(message, chat_info_text(reply_message.sender_chat))
    return

