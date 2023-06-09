"""
Extension for sticker management
"""

import interactions as ipy

import config
from common import utils


class StickerExtension(ipy.Extension):

    @ipy.slash_command(
        name="stickers",
        description="Manage the stickers that users can earn for their collection",
        scopes=[config.GUILD_ID]
    )
    @ipy.slash_default_member_permission(ipy.Permissions.MANAGE_GUILD)
    async def sticker_cmd(self, ctx: ipy.InteractionContext):
        ...

    @sticker_cmd.subcommand(
        sub_cmd_name="add",
        sub_cmd_description="Add a sticker to the library which users can earn for their collection"
    )
    @ipy.slash_option(
        name="emoji",
        description="The emoji to use as an obtainable sticker",
        required=True,
        opt_type=ipy.OptionType.STRING
    )
    @ipy.slash_option(
        name="rarity",
        description="The chance of getting the sticker when using /log. Must be between 1 - 100 (default: 50).",
        required=False,
        opt_type=ipy.OptionType.INTEGER,
        min_value=1,
        max_value=100
    )
    async def sticker_add_cmd(self, ctx: ipy.InteractionContext, emoji: str, rarity: int = 50):
        if not await utils.check_emoji(emoji, ctx.guild):
            return await ctx.send("The sticker must be a valid emoji!", ephemeral=config.EPHEMERAL_RESPONSES)
        await ctx.send(f"WIP: {emoji}", ephemeral=config.EPHEMERAL_RESPONSES)
