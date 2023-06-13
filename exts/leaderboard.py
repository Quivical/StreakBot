"""
Extension for leaderboard
"""

import interactions as ipy

from common.ui import embeds

import config
from common.data.models import User


class LeaderboardExtension(ipy.Extension):

    @ipy.slash_command(
        name="leaderboard",
        description="View the leaderboard",
        scopes=[config.GUILD_ID]
    )
    async def leaderboard_cmd(self, ctx: ipy.InteractionContext):
        users = await User.create_list(self.bot)
        await ctx.send(embed=embeds.leaderboard(users), ephemeral=config.EPHEMERAL_RESPONSES)
