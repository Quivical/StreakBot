"""
Extension for logging activity
"""
import random

import interactions as ipy

from common.data import write, retrieve

import config
from common.data.models import User


class LogExtension(ipy.Extension):

    @ipy.slash_command(
        name="log",
        description="Log that you'vae completed today's activity",
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

        # Form a unique sentence.
        # Combines a well done phrase, extra phrase and always tells the user their activity is logged.
        await ctx.send(
            f"**{random.choice(config.LOG_WELL_DONE_PHRASES)}!** "
            f"{random.choice(config.LOG_EXTRA_PHRASES)} "
            f"Your activity has been logged for today and you've earned the {sticker[1]} sticker.",
            ephemeral=config.EPHEMERAL_RESPONSES
        )
