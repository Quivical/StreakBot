"""
Run this file to start the bot.
"""
import asyncio

import aiosqlite

from common import startup_utils
from common.const import bot


async def run():
    bot.dbconn = await aiosqlite.connect("db.sqlite")
    try:
        await bot.astart()
    finally:
        await bot.dbconn.close()


def main():
    if not startup_utils.is_configured_correctly():
        print("Failed startup checks; Check log file for info!")
        quit(1)
    startup_utils.load_exts(bot)
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("Exiting")


if __name__ == "__main__":
    main()
