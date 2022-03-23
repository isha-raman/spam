import pyautogui, time
time.sleep(10)
for i in range(50):
    pyautogui.typewrite("spam")
    pyautogui.press("enter")