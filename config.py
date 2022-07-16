import os
class Config:
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = str(os.environ.get("API_HASH", None))
    SESSION = str(os.environ.get("SESSION", None))
    CHAT_ID = int(os.environ.get("CHAT_ID", None))
    MSG_ID = int(os.environ.get("MSG_ID", None))
    TIME = int(os.environ.get("TIME", None))
    MESSAGE = str(os.environ.get("MESSAGE", None))
