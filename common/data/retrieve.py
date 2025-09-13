import random
import datetime


async def get_user_logs(bot, user_id) -> list:
    """
    Get a list of log dates and stickers for a specific user. An empty list will be returned if no logs.
    [(YYYY-MM-DD, sticker), (YYYY-MM-DD, sticker), (YYYY-MM-DD, sticker)]
    """
    logs = []
    async with bot.dbconn.execute(
        "SELECT user_log.date, stickers.emoji FROM user_log "
        "LEFT JOIN stickers on user_log.sticker_id = stickers.id WHERE user_log.user_id=?", (str(user_id),)
    ) as cursor:
        async for row in cursor:
            logs.append(row)
    return logs


async def get_all_logs(bot) -> dict:
    """
    Get a dictionary of log dates for each user. Only includes users that have at least one log.
    { 1: [(YYYY-MM-DD, sticker), (YYYY-MM-DD, sticker)], 2: [(YYYY-MM-DD, sticker)] }
    """
    datas = []
    logs = {}
    async with bot.dbconn.execute(
        "SELECT user_log.user_id, user_log.date, stickers.emoji FROM user_log "
        "LEFT JOIN stickers on user_log.sticker_id = stickers.id"
    ) as cursor:
        async for row in cursor:
            datas.append(row)
    for user_id, date, emoji in datas:
        logs.setdefault(user_id, []).append((date, emoji))
    return logs


async def get_stickers(bot) -> list:
    """
    Get a list of stickers (list with the id, name and rarity). An empty list will be returned if no stickers exist
    """
    stickers = []
    async with bot.dbconn.execute("SELECT id, emoji, rarity FROM stickers") as cursor:
        async for row in cursor:
            stickers.append(row)
    return stickers


async def get_sticker(bot) -> tuple:
    """
    Get a random sticker, taking into account it's rarity. Returns a tuple containing the ID and name.
    """
    stickers = await get_stickers(bot)
    reference = {s[1]: s[0] for s in stickers}  # {name, id} - to get the id later, create a reference dictionary
    ids, emojis, rarities = zip(*stickers)
    sticker_chance = random.choices(emojis, rarities, k=sum(rarities))
    sticker = random.choice(sticker_chance)
    return reference[sticker], sticker


async def get_all_users(bot) -> list:
    """
    Get a list of all users in the database.
    """
    users = []
    async with bot.dbconn.execute("SELECT DISTINCT user_id FROM user_log") as cursor:
        async for row in cursor:
            users.append(row[0])
    return users

async def get_users_without_todays_log(bot) -> list:
    """
    Get a list of users who have not logged today.
    """
    users_without_log = []
    all_users = await get_all_users(bot)
    today = datetime.date.today()
    async with bot.dbconn.execute("SELECT DISTINCT user_id FROM user_log WHERE date = ?", (today,)) as cursor:
        users_with_log = [row[0] async for row in cursor]
    
    for user_id in all_users:
        if user_id not in users_with_log:
            users_without_log.append(user_id)
            
    return users_without_log

async def get_users_to_remind(bot) -> list:
    """
    Get a list of users who need to be reminded at the current time.
    """
    now_utc = datetime.datetime.utcnow().strftime("%H:%M")
    users_to_remind = []
    async with bot.dbconn.execute(
        "SELECT user_id FROM user_preferences WHERE reminder_time = ? AND reminders_enabled = ?",
        (now_utc, True)
    ) as cursor:
        async for row in cursor:
            users_to_remind.append(row[0])
    return users_to_remind
