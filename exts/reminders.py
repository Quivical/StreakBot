import interactions as discord
from datetime import datetime
import re
import pytz
import config

from common.data.retrieve import get_users_to_remind, get_user_logs
from common.data.write import set_reminder_time, disable_reminders

class Reminders(discord.Extension):
    def __init__(self, bot):
        self.bot = bot

    @discord.listen()
    async def on_ready(self):
        self.reminder_task.start()

    @discord.slash_command(name="remindme", description="Enable or disable reminders.")
    @discord.slash_option(
        name="enable",
        description="Enable or disable reminders",
        opt_type=discord.OptionType.BOOLEAN,
        required=True
    )
    @discord.slash_option(
        name="reminder_time",
        description="The time to remind you in HH:MM format (UTC). Required if enabling reminders.",
        opt_type=discord.OptionType.STRING,
        required=False
    )
    async def remindme(self, ctx: discord.InteractionContext, enable: bool, reminder_time: str = None):
        if enable:
            if reminder_time is None:
                await ctx.respond("Please provide a reminder time when enabling reminders.", ephemeral=True)
                return
            if not re.match(r"^[0-2][0-9]:[0-5][0-9]$", reminder_time):
                await ctx.respond("Invalid time format. Please use HH:MM.", ephemeral=True)
                return

            await set_reminder_time(self.bot, ctx.author.id, reminder_time)
            await ctx.respond(f"Your reminder time has been set to {reminder_time} UTC.", ephemeral=True)
        else:
            await disable_reminders(self.bot, ctx.author.id)
            await ctx.respond("Your reminders have been disabled.", ephemeral=True)

    @discord.Task.create(discord.IntervalTrigger(seconds=59))
    async def reminder_task(self):
        users_to_remind = await get_users_to_remind(self.bot)
        today = datetime.now(pytz.timezone(config.TIMEZONE)).strftime("%Y-%m-%d")

        for user_id in users_to_remind:
            user_logs = await get_user_logs(self.bot, user_id)
            has_logged_today = any(log[0] == today for log in user_logs)

            if not has_logged_today:
                user = await self.bot.fetch_user(user_id)
                print(f"Attempting to remind user {user_id} at {datetime.utcnow()}.")
                try:
                    await user.send("You have not logged your activity today, silly! Please use the `/log` command to log your activity.")
                except discord.Forbidden:
                    # This happens if the user has DMs disabled or has blocked the bot.
                    pass

