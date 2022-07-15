#credits @themayankparmar (Telegram)

from pyrogram import Client
import asyncio
from config import *

API_ID = API_ID
API_HASH = API_HASH
SESSION = SESSION
CHAT_ID = CHAT_ID
MSG_ID = MSG_ID

app = Client(api_id=Config.API_ID, api_hash=Config.API_HASH, session_name=Config.SESSION
)

async def main() :
    async with app:
        while true:
            await app.send_message(CHAT_ID, "++", reply_to_message_id=MSG_ID)
            await asyncio.sleep(5)


app.run(main())
