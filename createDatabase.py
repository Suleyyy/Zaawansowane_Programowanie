import sqlite3

def create_database():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT NOT NULL,
                  status TEXT NOT NULL)''')
    conn.commit()
    conn.close()

create_database()
