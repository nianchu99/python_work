import pyautogui as p,time

time.sleep(1)
p.click()
p.typewrite(['tab'])
p.typewrite("public static void main(String[] args{")

p.press('enter')

p.typewrite("System.out.println();")

p.typewrite(['enter', 'enter', 'enter'])
print()
