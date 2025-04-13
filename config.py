import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "26169469"))
API_HASH = os.environ.get("API_HASH", "1e2225f3d65b401d7d5bb921af531712")


OWNER_ID = int(os.environ.get("OWNER_ID", "5326198063"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Animebeasttamil:animebeast6374@cluster0.qzrwt.mongodb.net/")
DB_NAME = os.environ.get("DB_NAME", "Animebeasttamil")


CHANNEL_ID = int(os.environ.get("DB_CHANNEL_ID", "-1002111172286"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002075562432"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002164285498"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002484366937"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1200")) # auto delete in seconds


PORT = os.environ.get("PORT", "8020")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))


START_PIC = os.environ.get("START_PIC","https://i.ibb.co/KcCkXZBj/x.jpg")
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files of Anime beast tamil and other users can access it from special link.")
try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "6848088376").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "False") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hello  {mention}\n\n<b> Welcome My Friend I am a File Sharing Bot of anime beast tamil And Every Users Can Access It From Special Link.</b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello  {mention}\n\n<b>You Need To Join In our given Channels to Get file From me\n\nPlease Join Channel👇💫</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
