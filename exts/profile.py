"""
Extension for profile interaction
"""
import random

import interactions as ipy

from common.data.models import User

import config
from common.ui import embeds


class LogExtension(ipy.Extension):

    @ipy.slash_command(
        name="profile",
        description="View your or another user's activity profile",
        scopes=[config.GUILD_ID]
    )
    @ipy.slash_option(
        name="user",
        description="The user's profile to view. If none provided, you will see your own.",
        required=False,
        opt_type=ipy.OptionType.USER
    )
    async def profile_cmd(self, ctx: ipy.InteractionContext, user: ipy.BaseUser = None):
        if not user:
            user = ctx.author
        if user.bot:
            await ctx.send(
                "This user is a bot so doesn't have a profile! We can all imagine though :)",
                ephemeral=config.EPHEMERAL_RESPONSES
            )
            return
        userObj = await User.create_from_baseuser(self.bot, user)
        await ctx.send(embed=embeds.user_profile(userObj), ephemeral=config.EPHEMERAL_RESPONSES)
