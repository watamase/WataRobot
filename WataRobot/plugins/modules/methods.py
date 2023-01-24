import asyncio
import pyrogram

from pyrogram.errors import MessageIdInvalid, FloodWait


async def try_edit_message(message: pyrogram.types.Message, text: str) -> None:
    try:
        await message.edit_text(text)
    except MessageIdInvalid:
        print("[!] Message id invalid.")
    except FloodWait as e:
        await asyncio.sleep(e.value)
    return


async def try_delete_message(message: pyrogram.types.Message) -> None:
    try:
        await message.delete()
    except MessageIdInvalid:
        print("[!] Message id invalid.")
    return


async def try_reply_message(message: pyrogram.types.Message, text: str) -> None:
    try:
        await message.reply(text)
    except MessageIdInvalid:
        print("[!] Message id invalid.")
    return

