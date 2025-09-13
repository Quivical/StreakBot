CREATE TABLE IF NOT EXISTS user_log (
    id INTEGER PRIMARY KEY,
    user_id TEXT,
    date DATE,
    sticker_id INTEGER,
    UNIQUE(user_id, date)
);

CREATE TABLE IF NOT EXISTS stickers (
    id INTEGER PRIMARY KEY,
    emoji TEXT UNIQUE,
    rarity INTEGER
);

CREATE TABLE IF NOT EXISTS user_preferences (
    user_id TEXT PRIMARY KEY,
    reminder_time TEXT,
    reminders_enabled BOOLEAN DEFAULT TRUE
);