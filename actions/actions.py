# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import webbrowser
from sqlite3 import SQLITE_INSERT
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
# from rasa_core_sdk.events import EventType, UserUtteranceReverted
from rasa_sdk.events import SlotSet, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError
# from bs4 import BeautifulSoup
# You can now load the package via spacy.load('en_core_web_md')


class AboutUniversity(Action):

    def name(self) -> Text:
        return "about_university_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="What would you like to choose?",
                                 buttons=[
                                     {"title": "Scholarship",
                                         "payload": "/scholarship"},
                                     {"title": "About MTU",
                                         "payload": "What is the Vision of MTU"}
                                 ]

                                 )

        return []


class OpenLinkAction(Action):
    def name(self) -> Text:
        return "action_open_link"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the link to be opened from the button payload
        link = tracker.get_slot("url")

        # Open the link in the browser
        webbrowser.open(link)

        return []


class FallBackMessage(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I'm sorry, I really can't help with that. Kindly email us here; support@mtu.edu.ng \n or continue by choosing these options",
                                 buttons=[
                                     {"title": "admission",
                                         "payload": "gimme details on admission"},
                                     {"title": "Scholarsips",
                                      "payload": "/scholarship"},
                                     {"title": "Rebate Students",
                                      "paylaod": "/rebate"},
                                 ]
                                 )

        return [UserUtteranceReverted]

class SurveyFormAction(Action):
    def name(self) -> Text:
        return "action_survey_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # user = any()
        # staff = any(tracker.latest_message.get("intent", {}).get("name") == "staff")

        if tracker.latest_message.get("intent", {}).get("name") == "student":
            link = "<a href='https://forms.gle/kskFHh6rLLGf8gfaA' target='_blank'> Survey Form </a>"

            dispatcher.utter_message(text=f'Kindly click on the link: {link}')
        elif tracker.latest_message.get("intent", {}).get("name") == "staff":

            link = "<a href='https://forms.gle/CcBVucDCoBeMxqv36' target='_blank'> Survey Form </a>"

            dispatcher.utter_message(text=f'Kindly click on the link: {link}')

        return []



