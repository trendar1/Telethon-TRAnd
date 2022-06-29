import os
from typing import Set


class Config(object):
    LOGGER = True

    # MUST NEEDED VARS
    # set this value with your name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    # Get the values for following 2 from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    # Datbase url heroku sets it automatically else get this from elephantsql
    DB_URI = os.environ.get("DATABASE_URL", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN") or os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USERNAME = None
    TZ = os.environ.get("TZ", "Asia/Baghdad")
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/trendar1/Telethon-TRAnd")
    AUTONAME = os.environ.get("AUTONAME", "@VV399")
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID") or 0)
    PRIVATE_CHANNEL_BOT_API_ID = int(os.environ.get("PRIVATE_CHANNEL_BOT_API_ID") or 0)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
    PM_LOGGER_GROUP_ID = int( os.environ.get("PM_LOGGER_GROUP_ID") or os.environ.get("PM_LOGGR_BOT_API_ID") or 0 )
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL") or 0)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Trand")
    THUMB_IMAGE = os.environ.get("THUMB_IMAGE", "https://telegra.ph/file/db95c981b448537cd4073.jpg")
    # specify NO_LOAD with plugin names for not loading in userbot
    NO_LOAD = [x for x in os.environ.get("NO_LOAD", "").split()]
    # for custom pic for .digitalpfp
    DIGITAL_PIC = os.environ.get("DIGITAL_PIC", None)
    # your default pic telegraph link
    DEFAULT_PIC = os.environ.get("DEFAULT_PIC", None)
    # set this with your default bio
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    # set this with your deafult name
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r".")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r".")
    # set this with required folder path to act as download folder
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "downloads")
    # set this with required folder path to act as temparary folder
    TEMP_DIR = os.environ.get("TEMP_DIR", "./temp/")
    # time to update autoprofile cmds
    CHANGE_TIME = int(os.environ.get("CHANGE_TIME", 60))
    # SpamWatch, CAS, SpamProtection ban Needed or not
    ANTISPAMBOT_BAN = os.environ.get("ANTISPAMBOT_BAN", False)
    # is dual logging needed or not true or false
    DUAL_LOG = os.environ.get("DUAL_LOG", False)
    # progress bar progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "▰")
    UNFINISHED_PROGRESS_STR = os.environ.get("UNFINISHED_PROGRESS_STR", "▱")

    # API VARS FOR USERBOT
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture for screen shot
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    # This is required for the speech to text plugin. Get your USERNAME from
    # https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    # Genius lyrics get this value from https://genius.com/developers both has
    GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
    # Get your own API key from https://www.remove.bg/
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    # Get this value from https://free.currencyconverterapi.com/
    CURRENCY_API = os.environ.get("CURRENCY_API", None)
    # Google Drive plugin https://telegra.ph/G-Drive-guide-for-catuserbot-01-01
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
    G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
    G_DRIVE_INDEX_LINK = os.environ.get("G_DRIVE_INDEX_LINK", None)
    # For transfer channel 2 step verification code of telegram
    TG_2STEP_VERIFICATION_CODE = os.environ.get("TG_2STEP_VERIFICATION_CODE", None)
    # JustWatch Country for watch plugin
    WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "IN")
    # Last.fm plugin  https://telegra.ph/Guide-for-LASTFM-02-03
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    # SpamWatch API you can get it from get api from http://t.me/SpamWatchBot?start=token
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    # can get from https://coffeehouse.intellivoid.net/
    RANDOM_STUFF_API_KEY = os.environ.get("RANDOM_STUFF_API_KEY", None)
    # github vars
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Deepai value can get from https://deepai.org/
    DEEP_AI = os.environ.get("DEEP_AI", None)
    from telethon.tl.types import ChatBannedRights
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # specify LOAD and NO_LOAD
    LOAD = []
    # warn mode for anti flood
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get(
        "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
    )
    # for sed plugin
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
        "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )
    # time.py
    COUNTRY = str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    # For updater plugin
    UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "master")
    # dont touch this at all
    SUDO_USERS: Set[int] = set()
    CATUBLOGO = None
    BOTLOG = False
    BOTLOG_CHATID = 0


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
#edit dragon
#By:  @VV399
