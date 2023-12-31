import sys
import os
import keyboard
from pynput.keyboard import Key,Listener,KeyCode
from threading import Timer
import time
from time import sleep
import pyttsx3

from line import Line
from settings import Settings
from prompt import Prompt


class SentenceListening:
    def __init__(self):
        self.settings = Settings()
        self.initialize_text_to_speech()
        self.space_true = False


    def initialize_text_to_speech(self):
        self.text_to_speech_engine = pyttsx3.init()
        self.text_to_speech_engine.setProperty('volume',self.settings.tts_volume)
      