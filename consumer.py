import sqlite3
import time


def consumer():
    while True:
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE status = 'pending' LIMIT 1")
        task = c.fetchone()
        if task:
            print(f"Processing task: {task[1]}")
            c.execute("UPDATE tasks SET status = 'in_progress' WHERE id = ?", (task[0],))
            conn.commit()
            conn.close()
            time.sleep(30)
            conn = sqlite3.connect('tasks.db')
            c = conn.cursor()
            c.execute("UPDATE tasks SET status = 'completed' WHERE id = ?", (task[0],))
            conn.commit()
            conn.close()
            print(f"Completed task: {task[1]}")
        else:
            conn.close()
            time.sleep(5)
        


consumer()
