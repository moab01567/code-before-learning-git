import pyautogui
import time


time.sleep(5)
for i in range(1000):
    time.sleep(0.5)
    print("click:",i)
    pyautogui.click()