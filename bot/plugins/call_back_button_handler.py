#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52 | @AbirHasan2005

# the logging things

from bot.helper_funcs.utils import(
    delete_downloads
)
import logging
import os
import json
import shutil
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)

import datetime
from pyrogram.types import CallbackQuery
#from bot.helper_funcs.admin_check import AdminCheck
from bot import (
    AUTH_USERS,
    DOWNLOAD_LOCATION,
    LOG_CHANNEL
)

async def button(bot, update: CallbackQuery):
    cb_data = update.data
    try:
        g = await AdminCheck(bot, update.message.chat.id, update.from_user.id)
        print(g)
    except:
        pass
    LOGGER.info(update.message.reply_to_message.from_user.id)
    if (update.from_user.id == update.message.reply_to_message.from_user.id) or g:
        print(cb_data)
        if cb_data == "fuckingdo":
            if update.from_user.id in AUTH_USERS:
                status = DOWNLOAD_LOCATION + "/status.json"
                with open(status, 'r+') as f:
                    statusMsg = json.load(f)
                    statusMsg['running'] = False
                    f.seek(0)
                    json.dump(statusMsg, f, indent=2)
                    if 'pid' in statusMsg.keys():
                        try:
                            os.kill(statusMsg["pid"], 9)
                        except:
                            pass
                        delete_downloads()
                    try:
                        await bot.delete_messages(update.message.chat.id, statusMsg["message"])
                    except:
                        pass
                    try:
                        await update.message.edit_text("🚦🚦 Last Process Stopped 🚦🚦")
                        chat_id = LOG_CHANNEL
                        utc_now = datetime.datetime.utcnow()
                        ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)
                        ist = ist_now.strftime("%d/%m/%Y, %H:%M:%S")
                        bst_now = utc_now + datetime.timedelta(minutes=00, hours=6)
                        bst = bst_now.strftime("%d/%m/%Y, %H:%M:%S")
                        now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
                        await bot.send_message(chat_id, f"**Last Process Cancelled, Bot is Free Now !!** \n\nProcess Done at `{now}`", parse_mode="markdown")
                    except:
                        pass
            else:
                try:
                    await update.message.edit_text("You are not allowed to do that 🤭")
                except:
                    pass
        elif cb_data == "fuckoff":
            try:
                await update.message.edit_text("Okay! Fine 🤬")
            except:
                pass
				
        elif "about" in cb_data:
        await update.message.edit(
            text=Localisation.ABOUT_TEXT,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
					[
						InlineKeyboardButton("🆘 Help", callback_data="help"),
						InlineKeyboardButton("🐱 SourceCode", url="https://github.com/PredatorHackerzZ")
					],
					[
						InlineKeyboardButton("🏡 Home", callback_data="home"),
						InlineKeyboardButton("🔐 Close", callback_data="close")
					]
	        ]
            )
        )

    elif "help" in cb_data:
        await update.message.edit(
            text=Localisation.HELP_MESSAGE,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                                        [
						InlineKeyboardButton("👥 About ", callback_data="about"),
						InlineKeyboardButton("🤑 Donate", callback_data="donate")
					],
					[
						InlineKeyboardButton("🏡 Home", callback_data="home"),
						InlineKeyboardButton("🔐 Close ", callback_data="close")
					]
                ]
            )
        )

    elif "donate" in cb_data:
        await update.message.edit(
            text=Localisation.DONATION_USER,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                                        [
						InlineKeyboardButton("💰 PayPal ", url="https://paypal.me/AbhishekKumarIN47"),
						InlineKeyboardButton("☕ Ko-Fi ", url="https://ko-fi.com/Abhishekkumarin47")
					],
					[
						InlineKeyboardButton("🏡 Home", callback_data="home"),
						InlineKeyboardButton("🔐 Close ", callback_data="close")
					]
                ]
            )
        )

    elif "home" in cb_data:
        await update.message.edit(
            text=Translation.START_TEXT.format(update.from_user.mention),
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
						InlineKeyboardButton("⭕ Channel ⭕", url="https://t.me/TeleRoidGroup"),
						InlineKeyboardButton("😇 Support", url="https://t.me/TeleRoid14")
					],
					[
						InlineKeyboardButton("👥 About", callback_data="about"),
						InlineKeyboardButton("🆘 Help", callback_data="help")
					],
                                        [
						InlineKeyboardButton("🔐 Close", callback_data="close")
	            ]
                ]
            )
        )

@Bot.on_callback_query()
async def button(bot, update):
 
      if  'close'  in update.data:
                await update.message.delete()
