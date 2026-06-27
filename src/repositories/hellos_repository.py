class HelloRepository:

    def __init__(self):
        self._users = ["Bob", "John", "Bill"]

    def get_users(self):
        return self._users

    def add_user(self, user):
        self._users.append(user)

    def remove_user(self, user):
        self._users.remove(user)

    def find_user(self, name):
        return name if name in self._users else None