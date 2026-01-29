class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def changePassword(self, oldpassword, newpassword):
        if self.password == oldpassword:
            self.password = newpassword
            print("Hasło zmienione")
        else:
            print("Niepoprawne stare hasło")


    def showInfo(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")


adam = User("adam", "235d")
print(adam.showInfo())

adam.changePassword("235d", "<PASSWORD>")
print(adam.showInfo())