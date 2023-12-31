'''
Author:Upstreamwind
Time:2023.9.29
MORE messages can be viewed in ReadMe.md
Thank you
Best regards form Upstreamwind
'''
import sys
import os
import keyboard
from settings import Settings
from time import sleep
import time
from line import Line
import pyttsx3
from prompt import Prompt
from pynput.keyboard import Key, Listener, KeyCode
from pynput.keyboard import KeyCode
from threading import Timer





class WordsLearning:
    def __init__(self):
        self.settings = Settings()
        self.initialize_text_to_speech()
        self.space_true = False
        '''
        The helpless is the voice setting is useless,
        except the "engine",what weird is that 
        I just set the the property of the engine with the voice aspect,
        but it influence the other engine,
        like "text_to_speech_engine".
        This is a very weird and special problem,
        so I have to make the code so complexed.
        1. Befor each speech,I set the voice again and again.
        2. And other voice settings which are suitable are commented out.
        I am so sorry for this reluctant result.
        '''

        ''' just set the voice and rate '''
        ''' //////////////////// '''
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice',self.settings.tts_voices[3].id)
        self.engine.setProperty('rate',self.settings.tts_prompt_rate)
        # set the voice
        ''' /////////////////// '''

        self.print_prompt()
        self.line = Line(self.settings,self.text_to_speech_engine)
        self.engine.setProperty('rate',self.settings.tts_rate)
        
    def run_learning(self):
        while True:
            self.listener = Listener(on_press=self.on_press,on_release=self.on_release)
            self.listener.start()
            Timer(self.settings.run_speed_w, self.listener.stop).start()
            print('-----------------')
            self.listener.join()
            # print('-----------------')
            if self.space_true == True:
                # print('self.space_true is True')
                self.engine.setProperty('voice',self.settings.tts_voices[2].id)
                self.line.present_read_word_1()
                self.engine.setProperty('voice',self.settings.tts_voices[1].id)
                self.line.present_read_word_2()

    def initialize_text_to_speech(self):
        self.text_to_speech_engine = pyttsx3.init()
        self.text_to_speech_engine.setProperty('volume',self.settings.tts_volume)
        self.text_to_speech_engine_prompt = pyttsx3.init()
        self.text_to_speech_engine_prompt.setProperty('volume',self.settings.tts_volume)
    def print_prompt(self):
        """ print prompt messages"""
        self.prompt = Prompt()
        print(self.prompt.content[0])
        # self.text_to_speech_engine.setProperty('voices',self.settings.tts_voices[1].id)
        self.text_to_speech_engine_prompt.say(f'{self.prompt.content[0]}')
        self.text_to_speech_engine_prompt.runAndWait()
        try:
            self.prompt.content.reverse()
            self.prompt.content.pop()
            while True:
                print(f'{self.prompt.content.pop()}')
        except IndexError:
            pass


    def on_press(self,key):
        pass

    def on_release(self, key):
        # print('{0} release'.format(key))
        if key == KeyCode.from_char('q'):
            # sys.exit()
            self.exit_learning()
            # return False
        elif key == Key.left:
            # self.line.append_unknown()
            self.line.append_known()
            return False
        elif key == Key.right:
            print('--->')
            return False
        elif key == Key.space:
            if self.space_true == True:
                self.space_true = False
                print('PAUSED\n')
            elif self.space_true == False:
                self.space_true = True
                print('RUNNING\n')
                return False
        elif key == KeyCode.from_char('s'):
            self.set_rate()
                

    def exit_learning(self):
        print('words learning exits\n')
        # if self.line.unknown_words != []:
        #     print("the words you don't know are below:\n")
        #     with open(self.settings.unknown_file,'a',encoding='utf-8') as file:
        #         for line in self.line.unknown_words:
        #             print(line.rstrip())
        #             file.write(f"{line}")
        #         print("\nAnd they have been stored in file.")

            
        if self.line.known_words != []:
            print("the words you have known are below:\n")
            for line in self.line.known_words:
                print(line.rstrip()) # show all
            
            with open(self.settings.known_file,'r',encoding='utf-8') as file:
                self.all_known_words = []
                for line in file:
                    self.all_known_words.append(line)

            self.line.known_words = list(line for line in self.line.known_words if line not in self.all_known_words)
                 
            with open(self.settings.known_file,'a',encoding='utf-8') as file:
                for line in self.line.known_words:   
                    file.write(f"{line}")
                file.write(f"{self.settings.timestamp}\n")
                print("\nAnd they have been stored in file 'known_words.txt'.\n")

            self.line.lines = list(line for line in self.line.lines_copy if line not in self.all_known_words)
            self.line.lines = list(line for line in self.line.lines if line not in self.line.known_words)
            
            print("the words you should memorize more are bleow\n")
            with open(self.settings.word_file,'w',encoding='utf-8') as file:
                for line in self.line.lines:
                    print(line.rstrip())
                    file.write(f"{line}")
                print("\nAnd they have been stored in file 'words.txt'.\n")
        print("\nBest regards\nFrom UpstreamWind")
        os._exit(0)


    def instance_optional(self,run_speed_w):
        self.settings.run_speed_w = run_speed_w

    def set_rate(self):
        print("choose the rate['f''m''l']")
        # rate
        self.user_rate = input()
        if self.user_rate == "sf":
            self.settings.run_speed_w = 0.5 # time gap
        elif self.user_rate == "sm":
            self.settings.run_speed_w = 1.5 # 
        elif self.user_rate == "sl":
            self.settings.run_speed_w = 3 # 
        else:
            print("Invalid input. Please enter f, m or l.")

if __name__ == '__main__':
    wl = WordsLearning()
    wl.run_learning()
