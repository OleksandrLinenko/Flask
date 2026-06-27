class HelloService:

    def __init__(self, repo):
        self._repo = repo

    def get_users(self):
        return self._repo.get_users()

    def greet(self, name):
        if not name:
            return "User not found"
        return f"Hello, {name}!"
    