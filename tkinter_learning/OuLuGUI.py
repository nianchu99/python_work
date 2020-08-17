import tkinter as tk
import re
from spiderForOuLu import start

'''
Text是tkinter类中提供的一个多行文本区域，显示多行文本，用来收集(显示)用于输入的文字(类似Html中的textarea)，
格式化文本显示，允许你用不同的样式和属性来显示和编辑文本，同时支持内嵌图象和窗口。
'''

# coding:utf-8
import tkinter as Tkinter  # 导入TKinter模块
list_of_words = []

ytm = Tkinter.Tk()  # 创建Tk对象
ytm.title("Look Up words")  # 设置窗口标题
ytm.geometry("520x660")  # 设置窗口尺寸
l1 = Tkinter.Label(ytm, text="Please enter words", font=('Hack', 30))  # 标签
l1.grid(row=0, column=1)
# l1.pack()  # 指定包管理器放置组件
user_text = Tkinter.Text(bg='cyan', font= ('Hack', 20), width=27, height=24)  # 创建文本框
# user_text.pack()
user_text.grid(row=1, column=1)


def clear():
    user_text.delete('1.0', 'end')


def getuser():
    global list_of_words
    words = user_text.get('1.0', 'end')  # 获取文本框内容
    list_of_words = re.split(r'[\s\,\;\n]+', words)
    start(list_of_words)



confirm_button = Tkinter.Button(ytm, text="Confirm", font=('Blackboard', 25), command=getuser, width=6,
                                height=1)  # command绑定获取文本框内容方法
clear_button = Tkinter.Button(ytm, text="Clear", font=('Blackboard', 25), command=clear, width=6, height=1)
confirm_button.grid(row=2, column=2)
clear_button.grid(row=2, column=0)

# cancel_button.pack(side='right')

# return the list_of_words

ytm.mainloop()  # 进入主循环

'''
增加一个Button用以清除Text中原有的内容
'''
