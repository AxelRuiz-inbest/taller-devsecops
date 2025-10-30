import sqlite3
from app import DB_PATH


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """Create TABLE IF NOT EXISTS users ( id Integer PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)"""
    )
    cur.execute("DELETE FROM users")
    users = [
        ("Alice", "alic@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
    ]
    cur.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
    conn.commit()
    conn.close()
    print("DB inicializada en", DB_PATH)


if __name__ == "__main__":
    init_db()
