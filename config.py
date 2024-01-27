import os


class Config(object):
    API_HASH = os.environ.get("5c7ba9544c4d7cf3fecefebf1fd6f8bc")
    BOT_TOKEN = os.environ.get("5886805913:AAH-oFGt_P9un1Sx_eUOQDKNVbN2Hc3QgGA")
    TELEGRAM_API = os.environ["15912260"]
    OWNER = os.environ.get("533890503")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    PASSWORD = os.environ.get("123")
    DATABASE_URL = os.environ.get("mongodb+srv://volx:1K1usJxEaVH7VBOE@cluster0.kis63yl.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001569773228")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
