mess= ["Hello! how are you doing?", "Yo, do you like books?", "I love eating tacos!"]

def show_message(send):
    for message in send:
        print(message)

sent_messages= []
def send_messages():
    while mess:
        sending = mess.pop()
        print("Sending over...\n"+ '"'+ sending+ '"\n')
        sent_messages.append(sending)

send_messages()

print(mess)
print(sent_messages)