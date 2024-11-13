#2
from pathlib import Path
import json

path = Path("10_files_and_exceptions/favnumber.json")

number = input("What is your favorite number?\n")
fav = json.dumps(number)
path.write_text(fav)
print(f"{str(number)} has been recorded.")