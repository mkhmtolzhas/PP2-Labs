import time
import pyautogui

text_to_type = "Я люблю тебя жаным💖💖💖"

for i in range(100):
    time.sleep(3)
    pyautogui.typewrite(text_to_type)
    time.sleep(3)  
    pyautogui.press("enter")
    # time.sleep(10)
