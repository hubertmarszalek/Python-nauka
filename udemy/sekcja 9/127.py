class SimCard:
    def __init__(self) -> None:
        self.contacts = []

    def addContact(self, name, telephone):
        if isinstance(name, str) == False: return
        if isinstance(telephone, int) == False: return

        user = {
            "name": name,
            "telephone": telephone

        }
        self.contacts.append(user)

    def showContacts(self):
        for c in self.contacts:
            print(c["name"] + " " + str(c["telephone"]))

sim = SimCard()
sim.addContact("Ola", 987654321)
sim.addContact("Adam", 12345678)
sim.addContact(100, 92345678)
sim.addContact("Kasia", "numer")
sim.showContacts()



class ToDoList:
    def __init__(self):
        self.tasks = []


    def addTask(self, title, done):
        if isinstance(title, str) == False: return
        if isinstance(done, bool) == False: return

        task = {
            "title": title,
            "done": done
        }

        self.tasks.append(task)

    def showTasks(self):
        for task in self.tasks:
            status = "[X]" if task["done"] else "[ ]"
            print(f"{status} {task['title']}")


task1 = ToDoList()
task1.addTask("zrobic zakupy", True)
task1.showTasks()
task2 = ToDoList()
task2.addTask("umyc auto", False)
task2.showTasks()