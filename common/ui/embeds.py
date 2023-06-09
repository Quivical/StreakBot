from datetime import datetime, timedelta

import interactions as ipy
import pytz

import config
from common.ui import emoji


def _last_7_days(user):
    seperator_string = "---"
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


def _sticker_collection(user):
    string = ""
    stickers = user.get_stickers()
    for sticker, count in stickers.most_common():
        string += sticker + f"`x{count}`  "
    return string[:-2] if string != "" else "*No stickers*"


def user_profile(user):
    fields = [
        ipy.EmbedField(
            name=":fire: Streak:",
            value=f"{emoji.convert_num_to_emoji(user.get_streak_count())}  "
                  f"(Longest: **{user.get_longest_streak_count()}**)",
            inline=True
        ),
        ipy.EmbedField(
            name=":chart_with_upwards_trend: Total:",
            value=f"{emoji.convert_num_to_emoji(user.get_log_count())} days logged",
            inline=True
        ),
        ipy.EmbedField(
            name=":calendar_spiral: Last 7 Days:",
            value=f"{_last_7_days(user)}"
        ),
        ipy.EmbedField(
            name=":file_folder: Sticker Collection:",
            value=f"{_sticker_collection(user)}"
        )
    ]
    return ipy.Embed(
        author=ipy.EmbedAuthor(name=user.baseuser.tag, icon_url=user.baseuser.avatar_url),
        title=f"User Profile | {user.baseuser.display_name}",
        color=config.EMBED_COLOUR,
        fields=fields
    )
