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