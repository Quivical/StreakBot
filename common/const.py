"""
Sets up constants to be used throughout the program
Creates loggers and the bot instance.
"""

import logging
import os

import interactions as ipy

from dotenv import load_dotenv

import config

load_dotenv()

# Log to file handler
log_fh = logging.FileHandler(config.LOG_LOCATION, encoding="UTF-8")
log_fh.setFormatter(config.LOG_FORMAT)

# Log to console handler
log_sh = logging.StreamHandler()

# Setup logic logging
logger = logging.getLogger("bot")
logger.setLevel(logging.DEBUG)
log_fh.setLevel(config.BOT_LOG_LVL_FILE)
log_sh.setLevel(config.BOT_LOG_LVL_CON)
logger.addHandler(log_fh)
logger.addHandler(log_sh)

# Setup ipy logging
ipy_logger = logging.getLogger("ipy")
ipy_logger.setLevel(logging.DEBUG)
log_fh.setLevel(config.IPY_LOG_LVL_FILE)
log_sh.setLevel(config.IPY_LOG_LVL_CON)
ipy_logger.addHandler(log_fh)
ipy_logger.addHandler(log_sh)

bot = ipy.Client(
    token=os.environ["APP_TOKEN"],
    intents=ipy.Intents.DEFAULT,
    activity=ipy.Activity.create(name=config.BOT_ACTIVITY, type=config.BOT_ACTIVITY_TYPE),
    logger=ipy_logger,
    auto_defer=True,
    disable_dm_commands=True,
    send_command_tracebacks=False,
    delete_unused_application_cmds=True
)

