import sqlite3

def createTask(task, status):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, status))
    conn.commit()
    conn.close()

for _ in range(100):
    createTask("Task", "pending")
