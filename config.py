from datetime import datetime
import os
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardButton


if os.path.exists("config.env"):
    load_dotenv("config.env")
else:
    load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
    REDIRECT_WEBSITE = os.environ.get("REDIRECT_WEBSITE", None)
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "advancefiletestbot")
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "False"), False)
    CHANNELS = int(os.environ.get("CHANNELS", "0"))

    # Constants
    CHAT_CACHE = {}
    INVITE_LINKS = {}


class Script(object):
    START_MESSAGE = """<b>ʜᴇʏ ᴛʜᴇʀᴇ, {mention}\n\nᴛʜɪs ɪs ᴀ ғɪʟᴇs sʜᴀʀᴇ ʙᴏᴛ sᴘᴇᴄɪғɪᴄᴀʟʟʏ ᴍᴀᴅᴇ ғᴏʀ <a href='https://t.me/series_paradox'>sᴇʀɪᴇs ᴘᴀʀᴀᴅᴏx</a>\nᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ɢᴇᴛ ᴡʜᴀᴛ ʏᴏᴜ'ʀᴇ ʟᴏᴏᴋɪɴɢ ғᴏʀ...\n\n• ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/paradoxbotz'>Paradox Botz</a></b>"""

    HELP_MESSAGE = os.environ.get(
        "HELP_MESSAGE",
        "This is a file, videos, images, audio saver bot with some advanced features",
    )

    NEW_USER_MESSAGE = """#NewUser

🧾 Name : {mention}
👤 User Id : `{user_id}`"""

    NOT_ALLOWED_TEXT = "You are not allowed to send text messages here."
    ARROGANT_REPLY = "You are not my father so don't try to play with me"
    ABOUT_MESSAGE = f"""<b>○ Main Channel: N/A\n○ Movies Channel: @Movies_Paradox\n○ Series Channel: @Series_Paradox\n○ Chat Group: @ParadoxChats\n\n~ For Fsubs/Promo Contact: @Not_Xenov</b>"""


class Buttons(object):
    START_BUTTONS = [
        # "force subscribe" button
        [
            InlineKeyboardButton("Force Subscribe", callback_data="force_sub_config"),
        ],
        [
            InlineKeyboardButton("Auto Delete", callback_data="auto_delete_config"),
        ],
        [
            InlineKeyboardButton("💡 Help", callback_data="help"),
        ],
    ]
    BACK_BUTTON = [[InlineKeyboardButton("☜ Back", callback_data="start")]]
    USER_START_BUTTONS = [
        [
            InlineKeyboardButton("👾 Bots Update 👾", url="https://t.me/paradoxbotz"),
        ],
        [
            InlineKeyboardButton("• About Me", callback_data="about"),
            InlineKeyboardButton("Close •", callback_data="close"),
        ],
    ]

class CONST(object):
    START_TIME = datetime.now()
