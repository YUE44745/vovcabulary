import os
import pyttsx3
import time
from time import sleep
class Line:
    def __init__(self,settings,text_to_speech_engine):
        self.settings = settings
        self.text_to_speech_engine = text_to_speech_engine
        self._get_lines()
        self.known_words = []
        

    def present_read_word_1(self):
        try:
            self.word , self.meaning = self.lines.pop().split('\t',1)
        except IndexError:
            pass
        # self.text_to_speech_engine.setProperty('voices',self.settings.tts_voices[2].id)
        self.text_to_speech_engine.say(self.word)
        self.text_to_speech_engine.runAndWait()
        sleep(0.5) # two speech should be interval 0.5 s
        

    def present_read_word_2(self):
        print(f'{self.word}\t{self.meaning}',end='')
        self.text_to_speech_engine.say(self.word)
        self.text_to_speech_engine.runAndWait()
        # print('//////////')
        # print('------------------------')

        
        
    def _get_lines(self):
        self.lines = []
        self.lines_copy = []
        with open(self.settings.word_file, 'r', encoding='utf-8') as file:
            for line in file:
                self.lines.append(line)
        self.lines_copy = self.lines[:]

    # def append_unknown(self):
    #     print(f'***{self.word}***{self.meaning}')
    #     self.unknown_words.append(f'{self.word}\t{self.meaning}')
    #     sleep(3)

    def append_known(self):
        print('(^_^）/')
        self.known_words.append(f'{self.word}\t{self.meaning}')
        