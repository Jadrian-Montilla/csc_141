#10, it was very hard to understand
from pathlib import Path
path = Path('10_files_and_exceptions/guest_book.txt')

question = "\nPlease enter your name: "

users = []
while True:
    names =input(question)
    if names == 'quit':
        break

    print(f"Adding {names} to list")
    users.append(names)

line = ''
for names in users:
    line += f"{names}\n"
path.write_text(line)

