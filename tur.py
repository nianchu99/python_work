import turtle
turtle.getscreen().colormode(255)
import math
'''使用循环绘制出一个正方形
for i in  range(3):
    turtle.fd(100)
    turtle.left(90)

turtle.fd(100)
turtle.done()

# 利用绝对角度绘制出一个等腰直角三角形

turtle.fd(100 * math.sqrt(2))
turtle.seth(135)
turtle.fd(100)
turtle.seth(225)
turtle.fd(100)
turtle.done()
'''
'''总结一下：
pencolor更改颜色
pensize更改笔的粗细
speed更改速度
circle画一个圆或者给定角度的圆
penup抬笔
pendown下笔
goto移动到指定的位置
bgcolor设置画布颜色
getscreen().colormode(255)更改RGB配置模式
hideturtle隐藏箭头
fillcolor设置填充颜色
begin_fill开始填充
end_fill结束填充
填充的开始和结束分别在circle的前后
bk后退
home回到起始点
pen（）里面可以设置笔的参数，包括pensize，pencolor,fillcolor     
setpos可以修改画笔的起始位置

# 奥运五环
def tianchong():
    turtle.fillcolor(255,106,106)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

turtle.speed(50)
turtle.pensize(10)
turtle.pencolor('cyan')
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()

turtle.pencolor('yellow')
tianchong()
turtle.penup()
turtle.goto(50,-100)
turtle.pendown()

turtle.pencolor('red')
tianchong()
turtle.penup()

turtle.goto(150,-100)
turtle.pendown()

turtle.pencolor('pink')
tianchong()
turtle.penup()

turtle.goto(100,-50)
turtle.pendown()

turtle.pencolor('black')
tianchong()
turtle.penup()

turtle.goto(200,-50)
turtle.pendown()

turtle.pencolor(127,255,212)
tianchong()
turtle.done()
# 127 255 212
# 240 255 240

# 火柴人

turtle.pensize(10)
def tianchong():
    turtle.fillcolor(255,106,106)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
tianchong()
turtle.right(45)
turtle.fd(60)
turtle.home()
turtle.seth(225)
turtle.fd(60)
turtle.home()
turtle.penup()
turtle.goto(-30,-30)
turtle.pendown()
turtle.seth(270)
turtle.fd(100)

turtle.penup()
turtle.goto(30,-30)
turtle.pendown()
turtle.fd(100)


turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.write('陈翘楚',font =('Times', 18, 'bold'))
turtle.hideturtle()

turtle.done()                
'''
'''
# 奇怪的画圆方法
times = 180
turtle.pensize(10)
for time in range(times):   #使用循环，每次转动2度，循环180次
    turtle.fd(3)
    turtle.right(2)

turtle.done()
# turtle时钟和事件响应
turtle.bgcolor('black')
# 定义一个画车的函数
def tianchong():
    turtle.fillcolor(255,106,106)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
def drawCar():
    turtle.pencolor('yellow')
    # 先画后轮子
    tianchong()
    # 提笔往前挪，画前轮
    turtle.penup()
    turtle.fd(200)
    turtle.pendown()
    tianchong()
    # 画车轮廓
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(135)
    turtle.forward(60)
    turtle.right(45)
    turtle.forward(2)
    turtle.left(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(50)
    turtle.forward(60)
    turtle.left(40)
    turtle.forward(18)
    turtle.left(90)
    turtle.forward(240)
    # 画后轮与车轮廓接触线
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.write("this car is made by nianchu,2020")

    # 车上方写标题
    turtle.penup()
    turtle.setpos(60, 140)
    turtle.pendown()
    turtle.write("豪车！", font=("Times", 22, "bold"))

    # 隐藏那个画笔箭头
    turtle.hideturtle()


#定义个画笑脸的函数
def drawFace():
    turtle.color('yellow')
    turtle.speed(0.1)
    #先画笑脸轮廓,画一个半径为100像素的圆
    turtle.circle(100)
    #提笔到左上角（-40，120）位置，画一个小圆，表示右眼
    turtle.penup()
    turtle.setpos(-40,120)
    turtle.pendown()
    turtle.circle(10)
    #提笔到中部位置，先画一条短线表示上嘴唇
    turtle.penup()
    turtle.setpos(-10,60)
    turtle.pendown()
    turtle.forward(20)
    #继续下移一定距离，画一条短弧线表示下嘴唇
    turtle.penup()
    turtle.setpos(-10,40)
    turtle.pendown()
    totalTimes=4
    for times in range(totalTimes):
        turtle.forward(5)
        turtle.left(10)

    #提笔到右上角（40，120）位置，画一个小圆，表示右眼
    turtle.penup()
    turtle.setpos(40,120)
    turtle.pendown()
    turtle.circle(10)
    #提示语
    turtle.penup()
    turtle.setpos(-80,-30)
    turtle.pendown()
    for i in range(2):
        turtle.write("等待{}秒中，准备带你去看豪车了哦！".format(i+1),font=32)
        turtle.setpos(-80, -50)

    #隐藏那个画笔箭头
    turtle.hideturtle()

# 先画笑脸，等待2s后重置画笔，然后开始画车
turtle.ontimer(drawFace(),t=2000)
turtle.reset()
turtle.onclick(drawCar())
turtle.done()
'''
turtle.pencolor('#336699')
turtle.fd(100)
turtle.done()