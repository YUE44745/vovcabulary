'''
Author:Upstreamwind
Time:2023.9.29
MORE messages can be viewed in ReadMe.md
Thank you
Best regards form Upstreamwind
'''
import sys
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
        # print(f'{self.settings.tts_voices[1].id}special') 
        self.engine.setProperty('voice',self.settings.tts_voices[3].id)
        self.engine.setProperty('rate',self.settings.tts_prompt_rate)
        # set the voice
        ''' /////////////////// '''

        self.print_prompt()
        self.line = Line(self.settings,self.text_to_speech_engine)

        self.engine.setProperty('rate',self.settings.tts_rate)
        # self.mode_flag = False  # this is a future function

        
        



        
        
    def run_learning(self):
        while True:
            self.listener = Listener(on_press=self.on_press,on_release=self.on_release)
            self.listener.start()
            # 设置一个定时器，在5秒后调用l.stop()方法
            Timer(5, self.listener.stop).start()
            print('timer start')
            # 等待监听器结束
            self.listener.join()
            print('5秒过去了')
            # self._check_events()
            if self.space_true == True:
            #     ''' add a listener '''
            #     # 创建一个键盘监听器
            #     listener = Listener(on_press=self.on_press,on_release=self.on_release)
            #     # 启动监听器
            #     listener.start()
            #     # 等待用户按下Ctrl+C退出
            #     listener.join()
            #     print('set a listener')
            # # if self.space_true:
            # else:
                print('self.space_true is True')
                self.engine.setProperty('voice',self.settings.tts_voices[2].id)
                self.line.present_read_word_1()
                self.engine.setProperty('voice',self.settings.tts_voices[1].id)
                self.line.present_read_word_2()
                # sleep(3)
                

    
    def initialize_text_to_speech(self):
        '''there are two engine'''
        self.text_to_speech_engine = pyttsx3.init()
        # self.text_to_speech_engine.setProperty('rate',self.settings.tts_rate)
        self.text_to_speech_engine.setProperty('volume',self.settings.tts_volume)
        # voices = self.text_to_speech_engine.getProperty('voices')
        # self.text_to_speech_engine.setProperty('voices',voices[1].id)
        self.text_to_speech_engine_prompt = pyttsx3.init()
        # self.text_to_speech_engine_prompt.setProperty('rate',self.settings.tts_prompt_rate)
        self.text_to_speech_engine_prompt.setProperty('volume',self.settings.tts_volume)
        # self.text_to_speech_engine_prompt.setProperty('voices',voices[2].id)
       
    ''' because the consumption,I have to use a specialized block.This block is not used '''
    '''       
    def _check_events(self):
        start_time = time.time()       
        while time.time() - start_time < self.settings.run_speed or self.space_true:
            if keyboard.is_pressed('q'or'Q'):  #退出程序
                self.exit_learning()
            # elif keyboard.is_pressed('m'or'M'): #模式切换
            #     print('enter in')
            #     self.mode_flag = True
            #     sleep(0.1)
            # elif keyboard.is_pressed('1'): #模式1
            #     if self.mode_flag:
            #         self.mode_flag_run = True
            #         self.mode_flag = False
            #     sleep(0.1)
            # elif keyboard.is_pressed('2'): #模式2
            #     if self.mode_flag:
            #         self.mode_flag_present = True
            #         self.mode_flag = False
            #     sleep(0.1)
            elif keyboard.is_pressed('left'): #unknow words append in
                self.line.append_unknown()
                sleep(0.1)
                break
            elif keyboard.is_pressed('right'): #go to the next word directly 
                self.space_true = False
                sleep(0.1)
                break  
            elif keyboard.is_pressed('space'): #stop and continue detecting
                if self.space_true == True:
                    self.space_true = False
                    print('RUNNING\n')
                elif self.space_true == False:
                    self.space_true = True
                    print('PAUSED\n')
                sleep(0.1)  
            elif keyboard.is_pressed('0'):
                sleep(0.1)    
    '''
        
    def print_prompt(self):
        """ print prompt messages"""
        self.prompt = Prompt()
        print(self.prompt.content[0])
        # self.text_to_speech_engine.setProperty('voices',self.settings.tts_voices[1].id)
        self.text_to_speech_engine_prompt.say(f'{self.prompt.content[0]}')
        self.text_to_speech_engine_prompt.runAndWait()
        print(f'{self.prompt.content[1]}\n{self.prompt.content[2]}\n{self.prompt.content[3]}\n{self.prompt.content[4]}\n')


    def on_press(self,key):
        print('{0} pressed'.format(key))

    def on_release(self,key):
        print('{0} release'.format(key))
        if key == KeyCode.from_char('q'):
                # Stop listener
                sys.exit()
                self.exit_learning()    
                return False
        elif key == Key.left:#unknow words append in
                self.line.append_unknown()
                sleep(0.1)
        elif key == Key.right:#go to the next word directly 
                self.space_true = False
                print('right')
                sleep(0.1)
        elif key == Key.space: #stop and continue detecting
                if self.space_true == True:
                    self.space_true = False
                    print('RUNNING\n')
                elif self.space_true == False:
                    self.space_true = True
                    print('PAUSED\n')
                    sleep(0.1)  



       
    def exit_learning(self):
        """ 在最后程序结束之前，将不会的单词写入文件中 """
        print('words learning exits')
        if self.line.unknown_words != []:
            print("the words you don't know are below:")
            with open(self.settings.unknown_file,'a',encoding='utf-8') as file:
                for line in self.line.unknown_words:
                    print(line.rstrip())
                    file.write(f"{line}")
            # print(self.mode_flag,self.mode_flag_present,self.mode_flag_run)
            print("And they have been stored in file.")
        print("\nBest regards\nfrom UpstreamWind")
        sys.exit()




if __name__ == '__main__':
    wl = WordsLearning()
    wl.run_learning()

