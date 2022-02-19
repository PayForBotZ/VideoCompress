#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello, \n\nI am a Telegram <b>Video Compress Bot</b>. \n\n<b>Please send me any Telegram big file I will compress it as s small video file!</b> \n\nClick /help for more details."

   ABOUT_TEXT = """<b>🤖 My Name: <a href='https://t.me/URLUploaderV3Bot'> @URLUploaderV3Bot </a></b>

<b>👨‍💻 Developer :<a href='https://t.me/PredatorHackerzZ'>@TheTeleRoid</a></b>

<b>📝 Language: 𝐏𝐲𝐭𝐡𝐨𝐧𝟑</b>

<b>📡 Server: <a href='https://www.heroku.com'> Heroku </a></b>

<b>📚 Library: Pyrogram 1.0.7</b>

<b>📖 Source Code:<a href='https://github.com/PredatorHackerzZ/UPLOADER-BOT'> Click Here </a></b>

<b>📢 Bot Support:<a href='https://t.me/TeleRoid14'> @TeleRoid14</a></b>

<b>🔔 Bot Updates: <a href='https://t.me/TeleRoidGroup'> @TeleRoidGroup</a></b>

<b>🌀 Telegram BotList: <a href='https://t.me/TGRobot_List'> @TGRobot_List</a></b>

<b>🚸 Powered By: <a href='https://t.me/MoviesFlixers_DL'> @HindiWebNetwok</a></b>"""

    DONATION_USER = " Nice to Now You!.. Please Donate Some Money As You Wish."
    
    ABS_TEXT = " Please don't be selfish. 😑"
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "Downloading .....📥 \n"
    
    UPLOAD_START = "Uploading .....📤 \n"
    
    COMPRESS_START = "📀 Trying to compress 📀"
    
    RCHD_BOT_API_LIMIT = "Size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}\n\nMade With ❤ By @TheTeleRoid"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\nSupport Group: @TeleRoid14"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
