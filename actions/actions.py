# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SessionStarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Welcome to Pottermania! 🪄 The ultimate challenge to determine whether you're a mere muggle or a true wizard. Prove your knowledge, and you might just earn your place amongst the next generation of Hogwarts apprentices! ✨ But before we begin… what's your name, young aspiring wizard or witch? ⚡🦉")
        return []
    
class ActionCheckQuiz(Action):
    def name(self) -> str:
        return "action_check_quiz"

    def required_slots(self) -> List[str]:
        return ["guardian", "character", "shop", "ball", "potion"]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[EventType]:

        missing_slots = [slot for slot in self.required_slots() if not tracker.get_slot(slot)]
        missing_count = len(missing_slots)

        if missing_count == 0:
            dispatcher.utter_message(text="Congratulations, you passed with all correct answers! 🌟 Brilliant work outstanding mage, you've earned a first-class ticket to Hogwarts! 🧙‍♂️")
        elif missing_count <= 2:
            dispatcher.utter_message(text="You passed! A few answers might have slipped past, but that's still magical 🔮 Keep casting your spells, and next year, you'll be ready to join the ranks of Hogwarts' finest!")
        else:
            dispatcher.utter_message(text="You did not pass ❌📚 Keep studying, and one day, you might leave your Muggle roots behind!")

        return []