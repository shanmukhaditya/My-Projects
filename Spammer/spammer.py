import pyautogui, time
time.sleep(5)
f = open("New Text Document.txt",'r')

for line in f:
    #print(line)
    pyautogui.typewrite(line)
    pyautogui.press('enter')


