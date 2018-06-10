from turtle import *
from datetime import *
from tkinter import *
import time
def Skip(step):
  penup()
  forward(step)
  pendown()
def mkHand(name, length):
  #注册Turtle形状，建立表针Turtle
  reset()
  Skip(-length*0.1)
  begin_poly()
  forward(length*1.1)
  end_poly()
  handForm = get_poly()
  #注册Turtle形状命令register_shape(name,shape=None)
  register_shape(name, handForm)
def Init():
  global secHand, minHand, hurHand, printer
  mode("logo")# 重置Turtle指向北
  #建立三个表针Turtle并初始化
  #第二个参数为长度
  mkHand("secHand", 125)
  mkHand("minHand", 130)
  mkHand("hurHand", 90)
  secHand = Turtle()
  secHand.shape("secHand")
  minHand = Turtle()
  minHand.shape("minHand")
  hurHand = Turtle()
  hurHand.shape("hurHand")
  for hand in secHand, minHand, hurHand:
    hand.shapesize(1, 1, 3)
    hand.speed(0)
  #建立输出文字Turtle
  printer = Turtle()
  printer.hideturtle()
  printer.penup()
def SetupClock(radius):
  #建立表的外框
  reset()
  pensize(7)
  for i in range(60):
    Skip(radius)
    if i % 5 == 0:
      forward(20)
      Skip(-radius-20)
    else:
      dot(5)
      Skip(-radius)
    right(6)

def Date(t):
  y = t.year
  m = t.month
  d = t.day
  return "%s %d %d" % (y, m, d)
def Tick():
  i=1
  t=datetime.today()
  second=t.second
  minute0=t.minute
  hour0=t.hour
  while i==1:
    minute = minute0 + second/60.0
    hour = hour0 + minute/60.0
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
    gan=((t.year-3)%60)%10
    zhi=((t.year-3)%60)%12
    shuxiang=t.year%12
    if gan==1:
      messagegan="甲"
    if gan==2:
      messagegan="乙"
    if gan==3:
      messagegan="丙"
    if gan==4:
      messagegan="丁"
    if gan==5:
      messagegan="戊"
    if gan==6:
      messagegan="己"
    if gan==7:
      messagegan="庚"
    if gan==8:
      messagegan="辛"
    if gan==9:
      messagegan="壬"
    if gan==0:
      messagegan="癸"
    if zhi==1:
      messagezhi="子"
    if zhi==2:
      messagezhi="丑"
    if zhi==3:
      messagezhi="寅"
    if zhi==4:
      messagezhi="卯"
    if zhi==5:
      messagezhi="辰"
    if zhi==6:
      messagezhi="巳"
    if zhi==7:
      messagezhi="午"
    if zhi==8:
      messagezhi="未"
    if zhi==9:
      messagezhi="申"
    if zhi==10:
      messagezhi="酉"
    if zhi==11:
      messagezhi="戌"
    if zhi==0:
      messagezhi="亥"
    if shuxiang==0:
      messageshuxiang="猴"
    if shuxiang==1:
      messageshuxiang="鸡"
    if shuxiang==2:
      messageshuxiang="狗"
    if shuxiang==3:
      messageshuxiang="猪"
    if shuxiang==4:
      messageshuxiang="鼠"
    if shuxiang==5:
      messageshuxiang="牛"
    if shuxiang==6:
      messageshuxiang="虎"
    if shuxiang==7:
      messageshuxiang="兔"
    if shuxiang==8:
      messageshuxiang="龙"
    if shuxiang==9:
      messageshuxiang="蛇"
    if shuxiang==10:
      messageshuxiang="马"
    if shuxiang==11:
      messageshuxiang="羊"
    if t.year%4==0 and t.year%100!=0 or t.year%400==0:
      nian="闰年"
    else:
      nian="平年"
    message=messagegan+messagezhi+"年"
    messagebar=messageshuxiang+"年"
    tracer(False)
    printer.forward(80)
    printer.write(message, align="center",
                  font=("Courier", 14, "bold"))
    printer.back(20)
    printer.write(messagebar, align="center",
                  font=("Courier", 14, "bold"))
    printer.back(20)
    printer.write(nian, align="center",
                  font=("Courier", 14, "bold"))
    printer.back(140)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    tracer(True)
    second=second+1
    time.sleep(1)
def main():
  tracer(False)
  Init()
  SetupClock(160)
  tracer(True)
  Tick()
  mainloop()
if __name__ == "__main__":    
  main()
  
