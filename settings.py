import datetime
import os
import pyttsx3
class Settings:
    """various settings in words learning"""

    def __init__(self):
        """initial"""

        # the mode of learning words
        # self.run_mode = False

        # the speed of mode_run
        self.run_speed_s = 3
        self.run_speed_w = 3

        self.word_file_name = 'words.txt'
        self.known_file_name = 'known_words.txt'
        # self.word_file_name = 'unknown_words_2023-10-07_17-18-36.txt'

        self._get_datetime()
        self._get_files()

        self.tts_rate = 130
        self.tts_volume = 1.0
        self.tts_prompt_rate = 230

        
        engine = pyttsx3.init() # 初始化TTS引擎
        self.tts_voices = engine.getProperty('voices') # 获取所有可用的语音
        



    def _get_datetime(self):
        # 获取当前日期和时间
        current_datetime = datetime.datetime.now()

        # 格式化日期和时间为字符串（例如：2023-09-18_14-30-00）
        self.timestamp = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    def _get_files(self):
        # 获取源文件所在的文件夹路径
        # self.current_folder = os.path.dirname(os.path.abspath(__file__))
        self.current_folder = "D:\学习\english-vocabulary-master\wd_le"
        # 生成新文件的完整路径
        # self.unknown_file = os.path.join(self.current_folder, f'unknown_words_{self.timestamp}.txt')
        self.known_file = os.path.join(self.current_folder, self.known_file_name)
        self.word_file = os.path.join(self.current_folder,self.word_file_name)
        


