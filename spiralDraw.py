import time
import pyautogui as gui
time.sleep(3)  #  在运行pycharm之后，进入到画图界面
gui.click()  #  获取焦点
distance = 200
while distance > 0:
    gui.dragRel(distance, 0, button='left', duration=0.5)
    distance -= 5
    gui.dragRel(0, distance, button='left', duration=0.5)
    gui.dragRel(-distance, 0, button='left', duration=0.5)
    distance -= 5
    gui.dragRel(0, -distance, button='left', duration=0.5)

