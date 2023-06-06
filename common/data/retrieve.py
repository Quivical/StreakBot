async def get_user_logs(bot, user_id) -> list:
    """
    Get a list of log dates for a specific user. An empty list will be returned if no logs.
    [YYYY-MM-DD, YYYY-MM-DD, YYYY-MM-DD]
    """
    dates = []
    async with bot.dbconn.execute("SELECT date FROM user_log WHERE id=?", (str(user_id),)) as cursor:
        async for row in cursor:
            dates.append(row[0])
    return dates


async def get_all_logs(bot) -> dict:
    """
    Get a dictionary of log dates for each user. Only includes users that have at least one log.
    { 1: [YYYY-MM-DD, YYYY-MM-DD], 2: [YYYY-MM-DD, YYYY-MM-DD, YYYY-MM-DD] }
    """
    dates = []
    logs = {}
    async with bot.dbconn.execute("SELECT id, date FROM user_log") as cursor:
        async for row in cursor:
            dates.append(row)
    for user_id, date in dates:
        logs.setdefault(user_id, []).append(date)
    return logs
