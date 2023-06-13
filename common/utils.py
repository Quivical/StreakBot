import interactions as ipy


async def check_emoji(emoji: str, guild: ipy.Guild) -> bool:
    """
    Check if an emoji within a guild is valid - returning True if valid, False if not.
    First attempts to convert to a PartialEmoji to check format, then if custom, will poll the API.
    """
    try:
        emoji_obj = ipy.PartialEmoji.from_str(emoji)
        if not emoji_obj.id:  # non-custom
            return True
        return True if await guild.fetch_custom_emoji(emoji_obj.id) else False  # TODO: suppress 404 error?
    except ValueError:
        return False


async def execute_sql_script_from_file(conn, filename):
    with open(filename, 'r') as script_file:
        file_content = script_file.read()
    commands = file_content.split(";")
    for command in commands:
        await conn.execute(command)
    await conn.commit()
