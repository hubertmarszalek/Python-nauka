class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def changePassword(self, oldpassword, newpassword):
        if self.password == oldpassword:
            self.password = newpassword
            return True
        else:
            return False


    def showInfo(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

class UserManager:
    def __init__(self):
        self.users = []

    def addUser(self, user):
        self.users.append(user)

    def showAllInfo(self):
        for user in self.users:
            user.showInfo()

    def findUser(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None



adam = User("adam", "235d")
print(adam.showInfo())

adam.changePassword("235d", "<PASSWORD>")
print(adam.showInfo())

jessica = User("jessica", "235d")
print(jessica.showInfo())
jessica.changePassword("235d", "<PASSWORD>")
print(jessica.showInfo())

manager = UserManager()
manager.addUser(adam)
manager.addUser(jessica)
manager.showAllInfo()



