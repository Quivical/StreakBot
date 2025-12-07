"""
Extension for auditing user actions.
"""
import interactions as ipy
from common.const import logger

class AuditExtension(ipy.Extension):

    @ipy.listen()
    async def on_command_completion(self, event: ipy.api.events.CommandCompletion):
        ctx = event.ctx
        user = ctx.author
        command_name = ctx.command.name if ctx.command else "Unknown"
        
        args_list = []
        if ctx.kwargs:
            for k, v in ctx.kwargs.items():
                args_list.append(f"{k}: {v}")
        
        args_str = " | ".join(args_list) if args_list else "No Args"

        logger.info(
            f"ACTION: User: {user.username} (ID: {user.id}) | "
            f"Command: {command_name} | "
            f"Args: [{args_str}] | "
            f"Channel: {ctx.channel_id} | "
            f"Guild: {ctx.guild_id}"
        )

    @ipy.listen()
    async def on_command_error(self, event: ipy.api.events.CommandError):
        ctx = event.ctx
        user = ctx.author
        command_name = ctx.command.name if ctx.command else "Unknown"
        error = event.error
        
        args_list = []
        if ctx.kwargs:
            for k, v in ctx.kwargs.items():
                args_list.append(f"{k}: {v}")
        
        args_str = " | ".join(args_list) if args_list else "No Args"

        logger.warning(
            f"ACTION (FAILED): User: {user.username} (ID: {user.id}) | "
            f"Command: {command_name} | "
            f"Args: [{args_str}] | "
            f"Error: {error} | "
            f"Channel: {ctx.channel_id} | "
            f"Guild: {ctx.guild_id}"
        )
