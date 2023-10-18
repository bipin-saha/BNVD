import time
import pyautogui

currentMouseX, currentMouseY = pyautogui.position()
counter = 1
while True:
    time.sleep(5)
    #print(pyautogui.position())
    pyautogui.click()
    #pyautogui.click(735, 437)
    time.sleep(15)
    #pyautogui.click(1713, 401)
    time.sleep(15)
    #pyautogui.click(1669, 991)
    time.sleep(15)
    #pyautogui.click(749, 980)
    time.sleep(15)
    print('Click: ',counter)
    counter = counter + 1
