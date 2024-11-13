#2
from pathlib import Path
import json

def get_number():
    path = Path("10_files_and_exceptions/favnumber.json")
    if path.exists():
        fav = path.read_text()
        number = json.loads(fav)
        print(f"Is {number} your favorite?")

    else:
        number = input("What is your favorite number?\n")
        fav = json.dumps(number)
        path.write_text(fav)
        print(f"{str(number)} has been recorded.")

get_number()