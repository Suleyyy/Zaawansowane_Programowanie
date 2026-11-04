import sqlite3

def show_database_contents():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

show_database_contents()