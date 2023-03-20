# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action

import datetime

class SaveReasonTotxt(Action):
   
   def __init__(self, time):
      self.time = datetime.datetime.now()

   def name(self) -> Text:
      return "SaveReasonTotxt"
   
   def save_to_txt():
      pass
   
