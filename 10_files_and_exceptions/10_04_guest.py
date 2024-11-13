#2
from pathlib import Path

user = input("Please enter your name: ")

path = Path('10_files_and_exceptions/guest.txt')
path.write_text(user)