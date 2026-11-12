import sqlite3

DB_PATH = "habit_tracker.py"

def initialize_database():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS daily_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                log_date TEXT NOT NULL,
                planned_task TEXT,
                planned_time TEXT,
                done INTEGER,
                start_time TEXT,
                duration_minutes INTEGER,
                energy INTEGER CHECK (energy BETWEEN 1 AND 5),
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, log_date)
            )
        """)
