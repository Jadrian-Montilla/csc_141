#1
from pathlib import Path

Catpath = Path("10_files_and_exceptions/cats.txt")
#Catpath = Path("documents/cats.txt")
Dogpath = Path("10_files_and_exceptions/dogs.txt")

try:
    Cinfo = Catpath.read_text()
    for line in Cinfo.splitlines():
        print(line)
except FileNotFoundError:
    pass

print("\n")

try:
    Dinfo = Dogpath.read_text()
    for line in Dinfo.splitlines():
        print(line)
except FileNotFoundError:
    pass