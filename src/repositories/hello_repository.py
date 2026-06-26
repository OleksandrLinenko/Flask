class HelloRepository:

    def get_users(self):
        return ["Bob", "John", "Bill"]

    def find_user(self, name):
        users = self.get_users()
        return name if name in users else None