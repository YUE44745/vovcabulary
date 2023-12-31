import sys
from settings import Settings
from wd_le import WordsLearning
# from st_ls import

class EnglishLearning:
    def __init__(self):
        self.settings = Settings()
        self.set_mode_rate()
        self.run_eng_learning()
        
        
    def set_mode_rate(self):
        # mode
        print("sentence listening or words learning?['s'or'w'or'q']:")
        self.user_input = input()
        if self.user_input == "s":
            self.mode_s = True
            self.mode_w = False
        elif self.user_input == "w":
            self.mode_s = False
            self.mode_w = True
        elif self.user_input == "q":
            sys.exit()
        else:
            print("Invalid input. Please enter 's' or 'w'.")
        print("choose the rate['f''m''l']")
        # rate
        self.user_rate = input()
        if self.mode_s:
            if self.user_rate == "f":
                self.settings.run_speed_s = 0.5 # time gap
            elif self.user_rate == "m":
                self.settings.run_speed_s = 1.5 # 
            elif self.user_rate == "l":
                self.settings.run_speed_s = 3 # 
            else:
                print("Invalid input. Please enter f, m or l.")
        elif self.mode_w:
            if self.user_rate == "f":
                self.settings.run_speed_w = 0.5 # time gap
            elif self.user_rate == "m":
                self.settings.run_speed_w = 1.5 # 
            elif self.user_rate == "l":
                self.settings.run_speed_w = 3.0 # 
            else:
                print("Invalid input. Please enter f, m or l.")

    def run_eng_learning(self):
        while True:
            if self.mode_s:
                pass
            elif self.mode_w:
                wl = WordsLearning()
                wl.instance_optional(self.settings.run_speed_w)
                wl.run_learning()
        



if __name__ == '__main__':
    el = EnglishLearning()
    el.run_eng_learning()