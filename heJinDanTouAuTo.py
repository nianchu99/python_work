import pyautogui as p, time
from func_timeout import func_set_timeout
import func_timeout

time.sleep(0.8)
p.click()
p.mouseDown()
''''

'''
def firstStep():
    for i in range(4):
            p.hotkey('w', 'd')

@func_set_timeout(20)
def decond():
    while True:
        p.keyDown('d')
firstStep()
try:
    decond()
except func_timeout.exceptions.FunctionTimedOut:
    print('done!')
