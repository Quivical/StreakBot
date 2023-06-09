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