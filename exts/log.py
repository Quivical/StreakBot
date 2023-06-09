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
        well_done_phrases = (
            "Well done",
            "Way to go",
            "Excellent work",
            "Great job",
            "Good work",
            "Way to go",
            "Neat",
            "Bravo",
            "That’s great",
            "Good for you",
            "Good job",
            "Ace",
            "Incredible",
            "You rock"
        )
        extra_phrases = (
            "You nailed it this time.",
            "You exceeded all expectations.",
            "Kudos to you for your outstanding performance.",
            "Nothing can stop you now.",
            "You should be proud of yourself.",
            "You deserve a round of applause!",
            "Keep up the good work.",
            "You have what it takes to succeed."
        )
        await ctx.send(
            f"**{random.choice(well_done_phrases)}!** "
            f"{random.choice(extra_phrases)} "
            f"Your activity has been logged for today and you've earned the {sticker[1]} sticker.",
            ephemeral=config.EPHEMERAL_RESPONSES
        )
