import random
import pyttsx3
import datetime
import os

# 读取单词和中文释义
def read_words_from_file(file_path):
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word, meaning = line.strip().split('\t')
            words.append((word, meaning))
    return words

# 写入不会的单词到新文件
def write_unknown_words(file_path, unknown_words):
    with open(file_path, 'a', encoding='utf-8') as file:
        for word, meaning in unknown_words:
            file.write(f"{word}\t{meaning}\n")

# 初始化文本到语音引擎
def initialize_text_to_speech():
    engine = pyttsx3.init()
    return engine

# 主程序
def main():
    word_file_name = 'words.txt'  # 包含单词的文件

    # 获取当前日期和时间
    current_datetime = datetime.datetime.now()

    # 格式化日期和时间为字符串（例如：2023-09-18_14-30-00）
    timestamp = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    # 获取源文件所在的文件夹路径
    current_folder = os.path.dirname(os.path.abspath(__file__))

    # 生成新文件的完整路径
    unknown_file = os.path.join(current_folder, f'unknown_words_{timestamp}.txt')
    word_file = os.path.join(current_folder,word_file_name)

    words = read_words_from_file(word_file)
    unknown_words = []

    engine = initialize_text_to_speech()

    while words:
        random.shuffle(words)
        word, meaning = words.pop()

        print(f'单词：{word}')
        print(f'中文释义：{meaning}')

        # 读出单词发音
        engine.say(word)
        engine.runAndWait()

        user_input = input('是否认识这个单词？(y/n): ').strip().lower()
        if user_input == 'n':
            unknown_words.append((word, meaning))
        
        # 继续下一个单词
        input('按 Enter 继续下一个单词...')

    # 将不会的单词写入新文件
    write_unknown_words(unknown_file, unknown_words)
    print('所有单词已经学习完毕，不会的单词已保存到' + unknown_file + '中。')

if __name__ == "__main__":
    main()
