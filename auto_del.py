import pyautogui
import time

for i in range(20):
    time.sleep(1)
    pyautogui.moveTo(1159, 384)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(657, 732)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1070, 527)
    pyautogui.click()
    time.sleep(5)


# skill edit button - Point(x=1159, y=384)
# wait 1 sec
# delete Point(x=657, y=732)
# wait 1 sec
# confirm delete Point(x=1070, y=527)
# wait 5 sec
# Loop