from datetime import datetime, timedelta

import interactions as ipy
import pytz

import config
from common.ui import emoji


def _last_7_days(user):
    seperator_string = "`---`"
    string = ""
    start = datetime.now(pytz.timezone(config.TIMEZONE)) - timedelta(days=6)
    for day in range(7):
        if start.strftime("%Y-%m-%d") in user.raw_dates:
            string += ":white_check_mark:"
        else:
            string += ":negative_squared_cross_mark:"

        string += seperator_string
        start += timedelta(days=1)
    return string[:-len(seperator_string)]


def user_profile(user):
    fields = [
        ipy.EmbedField(
            name="Current Streak",
            value=f"{emoji.convert_num_to_emoji(user.get_streak_count())}",
            inline=True
        ),
        ipy.EmbedField(
            name="Total Days",
            value=f"{emoji.convert_num_to_emoji(user.get_log_count())}",
            inline=True
        ),
        ipy.EmbedField(
            name="Longest Streak",
            value=f"{emoji.convert_num_to_emoji(user.get_longest_streak_count())}",
            inline=True
        ),
        ipy.EmbedField(
            name="Last 7 Days",
            value=f"{_last_7_days(user)}"
        ),
        ipy.EmbedField(
            name="Sticker Collection (X/XX)",
            value="Work in Progress"
        )
    ]
    return ipy.Embed(
        author=ipy.EmbedAuthor(name=user.baseuser.tag, icon_url=user.baseuser.avatar_url),
        title=f"User Profile | {user.baseuser.display_name}",
        color=config.EMBED_COLOUR,
        timestamp=ipy.Timestamp.utcnow(),
        fields=fields,
        footer=ipy.EmbedFooter(
            text="Log your activity daily with /log",
            icon_url=config.BOT_AVATAR_URL
        )
    )
