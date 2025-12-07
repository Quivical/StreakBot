"""
Extension for logging activity
"""
import random
from datetime import datetime
import pytz

import interactions as ipy

from common.data import write, retrieve

import config
from common.data.models import User


class LogExtension(ipy.Extension):

    @ipy.slash_command(
        name=config.LOG_COMMAND_NAME,
        description=config.LOG_COMMAND_DESC,
        scopes=[config.GUILD_ID]
    )
    async def log_cmd(self, ctx: ipy.InteractionContext):
        sticker = await retrieve.get_sticker(self.bot)  # (id, name)
        if not await write.add_user_log(self.bot, ctx.author.id, sticker[0]):
            await ctx.send(
                "You've already logged activity for today! Come back tomorrow.",
                ephemeral=config.EPHEMERAL_RESPONSES
            )
            return

        # Time specific phrases
        tz = pytz.timezone(config.TIMEZONE)
        now = datetime.now(tz)

        extra_phrases = list(config.LOG_EXTRA_PHRASES)

        if now.hour < 4:  # Early: Midnight to 4AM
            extra_phrases.extend(config.LOG_EARLY_PHRASES)
        elif now.hour >= 22:  # Late: 8PM to Midnight
            extra_phrases.extend(config.LOG_LATE_PHRASES)

        # Form a unique sentence.
        # Combines a well done phrase, extra phrase and always tells the user their activity is logged.
        await ctx.send(
            f"**{random.choice(config.LOG_WELL_DONE_PHRASES)}!** "
            f"{random.choice(extra_phrases)} "
            f"Your activity has been logged for today and you've earned the {sticker[1]} sticker.",
            ephemeral=config.EPHEMERAL_RESPONSES
        )

    @ipy.listen(disable_default_listeners=True)
    async def on_command_error(self, event: ipy.api.events.CommandError):
        await event.ctx.send("**Something went wrong!** This has been logged.", ephemeral=True)
        await self.bot.on_command_error(self.bot, event)  # call default error handler
