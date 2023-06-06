from datetime import datetime, timedelta

import pytz

import config
from common.data import retrieve as data


class User:
    """
    Represents a Discord user
    """
    id: int
    raw_dates: []  # list of dates the user has logged

    @classmethod
    async def create_from_id(cls, bot, user_id):
        """
        Create a user object from a user's Discord ID
        """
        self = User()
        self.id = int(user_id)
        self.raw_dates = await data.get_user_logs(bot, user_id)
        return self

    @classmethod
    async def create_list(cls, bot):
        """
        Create a list of user objects
        """
        users = await data.get_all_logs(bot)
        user_objects = []
        for user_id, dates in users:
            self = User()
            self.id = int(user_id)
            self.raw_dates = dates
            user_objects.append(self)
        return user_objects

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
