import sqlite3
from datetime import datetime

import pytz

import config


async def add_user_log(bot, user_id, sticker_id: int) -> bool:
    today = datetime.now(pytz.timezone(config.TIMEZONE)).strftime("%Y-%m-%d")
    try:
        await bot.dbconn.execute(
            "INSERT INTO user_log (user_id, date, sticker_id) VALUES (?, ?, ?)", (str(user_id), today, sticker_id)
        )
    except sqlite3.IntegrityError:
        return False
    await bot.dbconn.commit()
    return True


async def add_sticker(bot, sticker: str, rarity: int):
    try:
        await bot.dbconn.execute(
            "INSERT INTO stickers (emoji, rarity) VALUES (?, ?)", (sticker, rarity)
        )
    except sqlite3.IntegrityError:
        return False
    await bot.dbconn.commit()
    return True

async def set_reminder_time(bot, user_id, reminder_time):
    await bot.dbconn.execute(
        "INSERT INTO user_preferences (user_id, reminder_time, reminders_enabled) VALUES (?, ?, ?) "
        "ON CONFLICT(user_id) DO UPDATE SET reminder_time = ?, reminders_enabled = ?",
        (str(user_id), reminder_time, True, reminder_time, True)
    )
    await bot.dbconn.commit()

async def disable_reminders(bot, user_id):
    await bot.dbconn.execute(
        "INSERT INTO user_preferences (user_id, reminders_enabled) VALUES (?, ?) "
        "ON CONFLICT(user_id) DO UPDATE SET reminders_enabled = ?",
        (str(user_id), False, False)
    )
    await bot.dbconn.commit()