from pyrogram import Client
import asyncio
from config import *

API_ID = Config.API_ID
API_HASH = Config.API_HASH
SESSION = Config.SESSION
CHAT_ID = Config.CHAT_ID
MSG_ID = Config.MSG_ID
TIME = Config.TIME
MESSAGE = Config.MESSAGE

print(MSG_ID)
print(CHAT_ID)
print(TIME)
print(MESSAGE)

app = Client(api_id=Config.API_ID,api_hash=Config.API_HASH,session_name=Config.SESSION
)

async def main() :
    async with app:
        while True:
            await app.send_message(Config.CHAT_ID,"MESSAGE",reply_to_message_id=Config.MSG_ID)
            await asyncio.sleep(Config.TIME)


app.run(main())
