class UserService:
    def __init__(self, repo):
        self.repo = repo

    def get_users(self):
        return self.repo.get_users()

    def greet(self, name):
        if not name:
            return "Nice to meet you!"

        return f"Nice to meet you, {name}!"
    
    def get_user(self, user_id):
        return self.repo.get_user(user_id)
    
    def create_user(self, name):
        self.repo.create_user(name)

    def update_user(self, user_id, name):
        self.repo.update_user(user_id, name)

    def login(self, name, password):
        user = self.repo.find_user(name)
        
        if user is None:
            return False

        return user.password == password