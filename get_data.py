import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

day = int(sys.argv[1])
year = int(sys.argv[2])
session = os.getenv('session')

r = requests.get(
    f"https://adventofcode.com/{year}/day/{day}/input",
    headers={"Cookie": f"session={session}"}
)

if r.status_code == 200:
    file = f"day_{day}.txt"

    with open(file, "w") as f:
        f.write(r.text)
        print(f"File {file} creato")
else:
    print(f"Errore {r.status_code}")