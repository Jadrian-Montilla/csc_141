from one_user import User
class Privileges:
    def __init__(self, privileges=["Can ban users", "Can remove posts", 
                           "Can create AD", "Can adjust guidelines", 
                           "Can add blacklisted words", "Can read reports"]):
        self.privileges = privileges
    def show_privileges(self):
        print("As an admin you:")
        for access in self.privileges:
            print(access)
        
class Admin(User):
    def __init__(self, first_name, last_name, age, location, occupation):
        super().__init__(first_name, last_name, age, location, occupation)
        self.privilege = Privileges()
    