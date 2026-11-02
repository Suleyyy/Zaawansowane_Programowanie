import time


def consumer():
    while True:
        with open("queue.csv", "r") as file:
            lines = file.readlines()

        task_active = False
        updated_lines = []

        for line in lines:
            parts = line.strip().split(";")

            task, status = parts[0], parts[1]

            if status == "pending" and not task_active:
                print(f"Processing task: {task}")
                updated_lines.append(f"{task};in_progress\n")
                task_active = True
            else:
                updated_lines.append(line)

        if task_active:
            with open("queue.csv", "w") as file:
                file.writelines(updated_lines)

            time.sleep(30)
            task_active = False

            with open("queue.csv", "r") as file:
                lines = file.readlines()

            updated_lines = []

            for line in lines:
                parts = line.strip().split(";")
                if parts[1] == "in_progress" and not task_active:
                    task = parts[0]
                    updated_lines.append(f"{task};done\n")
                    print(f"Task completed: {task}")
                    task_active = True
                else:
                    updated_lines.append(line)

            with open("queue.csv", "w") as file:
                file.writelines(updated_lines)
        else:
            time.sleep(5)


consumer()
