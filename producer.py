def createTask():
    with open("queue.csv", "a") as file:
        file.write(f"Rozmowa ...;pending\n")


for _ in range(100):
    createTask()
