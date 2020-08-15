import pyautogui
import time

time.sleep(2)

pyautogui.click(button='right')

# numberCentre = pyautogui.center(pyautogui.locateOnScreen('notes.jpg'))
location = pyautogui.locateOnScreen('note.jpg')
print(location)
location1 = pyautogui.center(location)
print(location1)
pyautogui.click(location1)


"""头都大了还是不对"""