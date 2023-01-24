from configs.main_config import API_ID, API_HASH
from pyrogram import Client

WataRobot = Client(
    name="WataRobot",
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root=f"{__name__}/plugins"),
)

