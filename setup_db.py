import sqlite3
BB_PATH = "vulnerable.db"

def init_db():
    conn = sqlite3.connect(BB_PATH)
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )""")
    cur.execute("DELETE FROM users")
    users = [
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com'),
        ('Charlie', 'charlie@example.com'),
    ]
    cur.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
    conn.commit()
    conn.close()
    print("DB inicializada en", BB_PATH)

if __name__ == "__main__":
    init_db()