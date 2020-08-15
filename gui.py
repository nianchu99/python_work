import pyautogui
import os
import time

pyautogui.PAUSE = 1.5
print(pyautogui.size())
print("Press Command - C to quit.")


try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + '  ' + ' Y:' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b'*len(positionStr), end='', flush=True)
except KeyboardInterrupt:
	print("\nDone .")
"""
click
doubleClick
rightClick
middleClick
typewrite -控制键盘输出
"""
