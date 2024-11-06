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