import turtle
import pyautogui
import pyperclip
import time
'''
turtle.getscreen().colormode(255)

turtle.write('陈翘楚',font=('Times',40,'bold'))
turtle.penup()
turtle.goto(140,0)
turtle.pendown()
turtle.write('LOVE 雷博闻',fpyautogui.scroll(200)ont=('Times',40,'bold'))

turtle.done()

'''
'''
numbers = ''
for i in range(200):
    numbers = numbers + str(i) + '\n'

pyperclip.copy(numbers)

time.sleep(5)
pyautogui.scroll(200) #向上滚动

photo = pyautogui.screenshot()
photo.getpixel((20,50))
bollem = pyautogui.pixelMatchesColor(20, 50,(21, 17, 18))
print(bollem)
'''
'''
print(pyautogui.locateOnScreen('apple.png'))
print(pyautogui.locateOnScreen('boxes.jpg'))
print(pyautogui.locateOnScreen('centres.jpg'))
numberCentre = pyautogui.center(pyautogui.locateOnScreen('centres.jpg'))
print(numberCentre)
pyautogui.click(numberCentre)



time.sleep(2)
pyautogui.click()

pyautogui.write('')
'''

'''
pyautogui.typewrite('enter')
pyautogui.typewrite('I want to say : no matter what had happened,i also love you : CQC 272!', 0.25)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
'''

import json
# 验证matlab的一个测试
num = []
a = 0
for i in range(-10000,10001):
	if(i > 1000 and i % 17 == 0):
		num[a] = i
		a = a  + 1
		
		
for j in range(len(num), len(num) - 9):
	print(num[j])
				

