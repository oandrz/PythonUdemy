class DataManager:

    def __init__(self, path):
        self.path = path

    def getAllPasswords(self):
        with open(self.path) as file:
            passwords = file.readline()

        return passwords

    def savePassword(self, url, email, password):
        with open(self.path, mode='a') as file:
            file.write(f"{url} | {email} | {password}\n")
