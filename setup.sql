CREATE TABLE IF NOT EXISTS user_log (
    id TEXT,
    date DATE,
    UNIQUE(id, date)
);