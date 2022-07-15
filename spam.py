#credits @themayankparmar

from pyrogram import Client
import asyncio
from config import *

API_ID = Config.API_ID
API_HASH = Config.API_HASH
SESSION = Config.SESSION
CHAT_ID = Config.CHAT_ID
MSG_ID = Config.MSG_ID

print(MSG_ID)
print(CHAT_ID)

app = Client(api_id=Config.API_ID,api_hash=Config.API_HASH,session_name=Config.SESSION
)

async def main() :
    async with app:
        while True:
            await app.send_message(Config.CHAT_ID,"++",reply_to_message_id=Config.MSG_ID)
            await asyncio.sleep(15)


app.run(main())
