prompts = {}

polling_active = True

while polling_active:
    Name = input("What's your name? ")
    prompt = input(Name + ", if you could go to any place, where would you? ")

    prompts[Name] = prompt

    repeat = input("Do you want to respond again? y/n ")
    if repeat == "n":
        polling_active = False

print ("results: ")
for Name, prompt in prompts.items():
    print(Name + " Would like to go to " + prompt)