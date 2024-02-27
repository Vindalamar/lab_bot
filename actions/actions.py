# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import csv
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_get_exercise"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        point = str(tracker.get_slot("POINT"))
        equip = str(tracker.get_slot("EQUIPMENT"))
        points = point.split(',')
        equips = equip.split(',')
        if "None" in equips:
            equips.append("Body Only")

        results = []
        with open("cache/megaGymDataset.csv", 'r') as file:
            for row in csv.reader(file):
                if row[4] in points:
                    if row[2] in equips:
                        results.append(row)
                    elif "All" in equips:
                        results.append(row)

        if len(results) == 0:
            dispatcher.utter_message(text="Sorry I don't have fitting exercise :(")
            return []

        final = random.choice(results)
        s = "I've got something for you: \n" + final[0] + '\n' + final[3] + "\nit's suited for " + final[1] + ' level'
        if final[5] != "None":
            dispatcher.utter_message(text=s + "\nI have video for this one!: " + final[5])
            return []

        dispatcher.utter_message(text=s)
        return []
