# import pyttsx3
# import keyboard
# # print('fdsfsdfsg\b',end='')
# # print('aaaa')
# # print(True)
# # print(False)
# # print(~True)
# # print(~False)
# # while True:
# #     if keyboard.is_pressed('space'):
# #         print('fd')
# engine = pyttsx3.init()
# engine.say('')
# engine.runAndWait()
# # engine.say('I will speak this ,i wil speak chinese')
# # engine.runAndWait()

# # 获取当前的语速
# # rate = engine.getProperty('rate')
# # print(rate)
# # # 设置新的语速
# # engine.setProperty('rate', 125)
# # # 获取当前的音量
# # volume = engine.getProperty('volume')
# # print(volume)
# # # 设置新的音量
# # engine.setProperty('volume', 1.0)
# # 获取当前的语音
# voices = engine.getProperty('voices')
# # 设置为男声
# engine.setProperty('voice', voices[0].id)
# engine.say("Hello World!")
# engine.runAndWait()
# # 设置为女声
# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
# # 说出一段文字
# engine.say("Hello World,i wil speak chinese")
# engine.say('defy')
# engine.runAndWait()
# print(voices[0].id)
# print(voices[1].id)


# import pyttsx3
# from settings import Settings
# settings =  Settings()
# engine = pyttsx3.init() # 初始化TTS引擎
# # voices = engine.getProperty('voices') # 获取所有可用的语音

# # for voice in settings.tts_voices: # 遍历所有语音
# #     print(voice.id) # 打印每个语音的id
# #     engine.setProperty('voice',voice.id) # 设置要使用的语音id
# #     engine.say('军旗是一种双人或四人的棋类游戏，目的是抢夺对方的军旗或使对方无棋可走。军旗有两种玩法，一种是翻棋，一种是布局。翻棋是指开局时棋子都背面朝上，双方轮流翻开棋子，确定阵营后开始对抗。布局是指双方各自将25个棋子摆放在自己的兵站或大本营中，按照一定的规则进行摆放。军旗的棋子有十种，分别是司令、军长、师长、旅长、团长、营长、连长、排长、工兵、炸弹，以及地雷和军旗。各种棋子的大小顺序和吃子规则如下：') # 说出文本
# #     engine.runAndWait() # 等待说完
# engine.setProperty('voice',settings.tts_voices[1].id) # 设置要使用的语音id
# engine.say('Cmder is a software package created out of ')
# engine.runAndWait() # 等待说完


# from pynput.keyboard import Key, Listener

# def on_press(key):
#   print('{0} pressed'.format(key))

# def on_release(key):
#   print('{0} release'.format(key))
#   if key == Key.esc:
#     # Stop listener
#     return False

# # Collect events until released
# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# from pynput.keyboard import Key, Listener, KeyCode
# from pynput.keyboard import Key, Listener,KeyCode
# import sys
# # 定义一个函数，用于处理按键事件
# def on_press(key):
#     # 如果按下的是q键，就打印"Quit"
#     if key == KeyCode.from_char('q'):
#         print("Quit")
#         sys.exit()
#     # 如果按下的是空格键，就打印"Space"
#     elif key == Key.space:
#         print("Space")
#         return False
#     # 如果按下的是左箭头键，就打印"Left"
#     elif key == Key.left:
#         print("Left")

# # 创建一个键盘监听器
# listener = Listener(on_press=on_press)
# # 启动监听器
# listener.start()
# # 定义一个变量，用于控制循环是否继续
# running = True
# # 循环运行
# while running:
#     # 等待监听器结束
#     running = listener.join()

# # 等待用户按下Ctrl+C退出
# listener.join()

# from pynput import keyboard

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()


# from threading import Timer
# from pynput.keyboard import Listener

# def on_press(key):
#     print(key)

# with Listener(on_press=on_press) as l:
#     # 设置一个定时器，在5秒后调用l.stop()方法
#     Timer(5, l.stop).start()
#     # 等待监听器结束
#     l.join()
#     print('5秒过去了')


# import sys
# import keyboard
# from settings import Settings
# from time import sleep
# import time
# from line import Line
# import pyttsx3
# from prompt import Prompt
# from pynput.keyboard import Key, Listener, KeyCode
# from pynput.keyboard import KeyCode
# from threading import Timer

# class WordsLearning:
#     def __init__(self):
#         self.settings = Settings()
#         self.initialize_text_to_speech()
#         self.space_true = False
#         self.engine = pyttsx3.init()
#         self.engine.setProperty('voice', self.settings.tts_voices[3].id)
#         self.engine.setProperty('rate', self.settings.tts_prompt_rate)
#         self.line = Line(self.settings, self.text_to_speech_engine)
#         self.engine.setProperty('rate', self.settings.tts_rate)
        
#     def run_learning(self):
#         while True:
#             self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
#             self.listener.start()
#             Timer(5, self.listener.stop).start()
#             print('timer start')
#             self.listener.join()
#             print('5秒过去了')
#             if self.space_true == True:
#                 print('self.space_true is True')
#                 self.engine.setProperty('voice', self.settings.tts_voices[2].id)
#                 self.line.present_read_word_1()
#                 self.engine.setProperty('voice', self.settings.tts_voices[1].id)
#                 self.line.present_read_word_2()

#     def initialize_text_to_speech(self):
#         self.text_to_speech_engine = pyttsx3.init()
#         self.text_to_speech_engine.setProperty('volume', self.settings.tts_volume)
#         self.text_to_speech_engine_prompt = pyttsx3.init()
#         self.text_to_speech_engine_prompt.setProperty('volume', self.settings.tts_volume)

#     def on_press(self, key):
#         pass

#     def on_release(self, key):
#         if key == KeyCode.from_char('q'):
#             self.exit_learning()
#         elif key == Key.left:
#             self.line.append_unknown()
#             sleep(0.1)
#         elif key == Key.right:
#             self.space_true = False
#             print('right')
#             sleep(0.1)
#         elif key == Key.space:
#             if self.space_true == True:
#                 self.space_true = False
#                 print('RUNNING\n')
#             elif self.space_true == False:
#                 self.space_true = True
#                 print('PAUSED\n')
#                 sleep(0.1)

#     def exit_learning(self):
#         print('words learning exits')
#         if self.line.unknown_words != []:
#             print("the words you don't know are below:")
#             with open(self.settings.unknown_file, 'a', encoding='utf-8') as file:
#                 for line in self.line.unknown_words:
#                     print(line.rstrip())
#                     file.write(f"{line}")
#         print("\nBest regards\nfrom UpstreamWind")
#         sys.exit()

# if __name__ == '__main__':
#     wl = WordsLearning()
#     wl.run_learning()
# import sys
# import os
# import keyboard
# from settings import Settings
# from time import sleep
# import time
# from line import Line
# import pyttsx3
# from prompt import Prompt
# from pynput.keyboard import Key, Listener, KeyCode
# from pynput.keyboard import KeyCode
# from threading import Timer


# settings = Settings()
# lines = []
# known_words = []
# with open(settings.word_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             lines.append(line)
# with open(settings.known_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             known_words.append(line)
# lines = tuple(line for line in lines if line not in known_words)
# print(lines)

# a = [1,2,3,4]
# print(a.reverse())
# print(a)
# b = a
# c = []
# c = a[:]
# b.append(5)
# c.append(6)
# print(f'{a}\n{b}\n{c}')

from prompt import Prompt

p = Prompt()
print(p.content)
p.content.reverse()
p.content.pop()
print(p.content)