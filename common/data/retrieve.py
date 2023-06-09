import random


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
    print(datas)
    for user_id, date, emoji in datas:
        logs.setdefault(user_id, []).append((date, emoji))
    print(logs)
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
