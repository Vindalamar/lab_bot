from typing import Any, Text, Dict, List
import csv
import random
from pathlib import Path
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


def run():
    # point = ["Abdominals"]
    equip = ["Other"]
    points = ["Abdominals"]

    results = []
    with open("newdb.txt", 'w') as f:
        with open("megaGymDataset.csv") as file:
            for row in csv.reader(file):
                f.write(row[0] + row[1] + row[3] + row[4])
    print(Path("data") / "megaGymDataset.csv")
    if len(results) == 0:
        print("Sorry I don't have fitting exercise :(")
        return []

    final = random.choice(results)
    s = final[0] + '\n' + final[3] + "\nit's suited for " + final[1] + ' level'

    print("I've got something for you: \n" + s)
    return []

if __name__ == '__main__':
    run()

