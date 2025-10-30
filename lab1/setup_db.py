import sqlite3

DB_PATH = "vulnerable.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT
                )""")
    cur.execute("DELETE FROM users")
    users = [
        ('Alice', 'alice@email.com'),
        ('Bob', 'bob@email.com'),
        ('Charlie', 'charlie@email.com'),
    ]
    cur.executemany("INSERT INTO users (name, email) VALUES (?,?)", users)
    conn.commit()
    conn.close()
    
    print("DB inicializada en ", DB_PATH)
if __name__ == '__main__':
    init_db()