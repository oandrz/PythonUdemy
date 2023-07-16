import json

class DataManager:

    def __init__(self, path):
        self.path = path

    def getAllPasswords(self):
        with open(self.path) as file:
            cache = json.load(file)

        return cache

    def getPasswordForUrl(self, url, handle_error, handle_success):
        try:
            with open(self.path) as file:
                cache = json.load(file)
        except FileNotFoundError:
            handle_error(("No Data Saved", "We don't have any data saved"))
        else:
            try:
                handle_success(cache[url])
            except KeyError:
                handle_error(("Url Not Found", "We don't have that url"))

    def savePassword(self, url, email, password):
        param = {
            url: {
                "email": email,
                "password": password
            }
        }
        try:
            with open(self.path, mode='r') as file:
                cache = json.load(file)
                cache.update(param)
            with open(self.path, mode='w') as file:
                json.dump(cache, file, indent=4)
        except FileNotFoundError:
            with open(self.path, mode='w') as file:
                json.dump(param, file, indent=4)
