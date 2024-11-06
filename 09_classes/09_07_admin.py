# 2 
class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.place = location
        self.work = occupation
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.fname} likes to eat lobsters and solve puzzles.")
    
    def greet_user(self):
        print(f"Hello! I am {self.fname} {self.lname}, pleased to meet you!")
class Admin(User):
    def __init__(self, first_name, last_name, age, location, occupation):
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = ["Can ban users", "Can remove posts", 
                           "Can create AD", "Can adjust guidelines", 
                           "Can add blacklisted words", "Can read reports"]
    def show_privileges(self):
        print(self.fname + ", as an admin you:")
        for access in self.privileges:
            print(access)

moderator = Admin("Mike", "Scott", 34, "N/A", "Moderation")
moderator.show_privileges()