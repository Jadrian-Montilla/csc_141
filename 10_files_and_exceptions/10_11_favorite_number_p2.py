#1
from pathlib import Path
import json

path = Path("10_files_and_exceptions/favnumber.json")
fav = path.read_text()
number = json.loads(fav)

print(f"Is {number} your favorite?")