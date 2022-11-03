import pyautogui
import time
time.sleep(4)

count = 0
while count <= 10:
  pyautogui.typewrite("Hello" + str("o")*count)
  pyautogui.press("enter")
  count += 1
  