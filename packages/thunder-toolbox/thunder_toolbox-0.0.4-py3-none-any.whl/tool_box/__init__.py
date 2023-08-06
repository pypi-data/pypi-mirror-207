import pyautogui
import time


class KeyBoardTools:

    @staticmethod
    def printer(text):
        return print(text)

    @staticmethod
    def type_write(text, interval=None):
        if not interval:
            return pyautogui.write(text)
        else:
            return pyautogui.write(text, interval)

    @staticmethod
    def press_key(key):
        return pyautogui.press(key)

    @staticmethod
    def spammer(text, count=0, freeze_time=3):
        time.sleep(freeze_time)
        for ctr in range(count):
            pyautogui.typewrite(text)
            pyautogui.press('enter')
        return "Spamming done!"
