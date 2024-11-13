#1
from pathlib import Path

path = Path("10_files_and_exceptions/learning_python.txt")
text = path.read_text()
print(text+ "\n")


lines = text.splitlines()
for mess in lines:
    print(mess.replace("Python", "C")+ "\n")
