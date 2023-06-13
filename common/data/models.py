from collections import Counter
from datetime import datetime, timedelta

import interactions as ipy
import pytz

import config
from common.data import retrieve as data


class User:
    """
    Represents a Discord user
    """
    baseuser: ipy.BaseUser
    id: int
    raw_dates: []  # list of dates the user has logged
    raw_stickers: []  # list of stickers the user has earned

    @classmethod
    async def create_from_id(cls, bot, user_id):
        """
        Create a user object from a user's Discord ID
        """
        self = User()
        self.id = int(user_id)
        self.raw_dates, self.raw_stickers = zip(*await data.get_user_logs(bot, user_id))
        return self

    @classmethod
    async def create_from_baseuser(cls, bot, user):
        """
        Create a user object from a interactions.py baseuser object
        """
        self = await User.create_from_id(bot, user.id)
        self.baseuser = user
        return self

    @classmethod
    async def create_list(cls, bot) -> list:
        """
        Create a list of user objects
        """
        users = []
        users_data = await data.get_all_logs(bot)
        for user_id, user_data in users_data.items():
            self = User()
            self.id = user_id
            dates, stickers = zip(*user_data)
            self.raw_dates = dates
            self.raw_stickers = stickers
            users.append(self)
        return users

    def get_log_count(self):
        return len(self.raw_dates)

    def get_streak_count(self):
        count = 0
        today = datetime.now(pytz.timezone(config.TIMEZONE))
        count += 1 if today.strftime("%Y-%m-%d") in self.raw_dates else 0
        date = today
        while True:
            date -= timedelta(days=1)
            if date.strftime("%Y-%m-%d") not in self.raw_dates:
                break
            count += 1
        return count

    def get_longest_streak_count(self):
        streaks = []  # creates a list of each streak (which is a list of dates)
        dates = list(self.raw_dates)
        dates.sort()

        prev_date = None
        cur_streak = []
        for date in dates:
            date = datetime.strptime(date, "%Y-%m-%d")
            try:
                if not prev_date:
                    cur_streak.append(date)
                    continue
                if date - prev_date > timedelta(days=1):  # if the time gap is larger than a day
                    streaks.append(cur_streak)
                    cur_streak = [date, ]
                    continue
                cur_streak.append(date)
            finally:
                prev_date = date
        streaks.append(cur_streak)
        return len(max(streaks, key=len))

    def get_first_log(self):
        if len(self.raw_dates) == 0:
            return None
        dates = list(self.raw_dates)
        dates.sort(reverse=True)
        return dates[0]

    def get_stickers(self):
        return Counter(self.raw_stickers)
