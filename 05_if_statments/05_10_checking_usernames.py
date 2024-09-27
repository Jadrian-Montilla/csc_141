current_users = ["Mikael2$", "Penalope2", "Marjar1029", "SyperNova", "PhilsMail"]
new_users = ["SyperNova", "Mikael2$", "PaulaSmarla2", "VanillaNilla", "MaysflowerSword"]
CULower = ["mikael2$", "penalope2", "marjar1029", "sypernova", "philsmail"]

for user in new_users:
    if user in current_users:
        print("\nThis username "+user+", is already being used. Please make another")
    elif user in CULower:
        print("\nThis username "+user+", is already being used. Please make another")
    else:
        print("\nThis username, " +user+ ", is available")

