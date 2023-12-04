from turtle import *

def show_win():
    shape('turtle')
    color('black')
    width(3)
    speed(200)

    up()
    left(90)
    forward(250)
    left(90)
    forward(300)

    #In position to start Thanks
    right(180)

    #T
    down()
    forward(25)
    right(90)
    forward(75)
    right(180)
    forward(75)
    right(90)
    forward(25)


    up()
    forward(25)

    #H
    down()
    right(90)
    forward(75)
    right(180)
    forward(37.5)
    right(90)
    forward(40)
    left(90)
    forward(37.5)
    left(180)
    forward(75)

    up()
    left(90)
    forward(25)

    #A
    down()
    left(90)
    forward(75)
    right(90)
    forward(40)
    right(90)
    forward(37.5)
    right(90)
    forward(40)
    right(180)
    forward(40)
    right(90)
    forward(37.5)

    up()
    left(90)
    forward(25)

    #N
    down()
    left(90)
    forward(75)
    right(155)
    forward(80)
    left(155)
    forward(75)

    up()
    right(90)
    forward(25)

    #K
    down()
    right(90)
    forward(75)
    right(180)
    forward(37.5)
    right(45)
    forward(51)
    right(180)
    forward(51)
    left(90)
    forward(51)
    right(180)
    forward(51)

    up()
    right(135)
    forward(150)

    #Y
    down()
    left(45)
    forward(51)
    right(180)
    forward(51)
    right(90)
    forward(51)
    right(180)
    forward(51)
    right(45)
    forward(37.5)

    up()
    left(90)
    forward(60)

    #O
    down()
    forward(50)
    left(90)
    forward(75)
    left(90)
    forward(50)
    left(90)
    forward(75)

    up()
    left(90)
    forward(75)

    #U
    down()
    forward(50)
    left(90)
    forward(75)
    left(90)
    up()
    forward(50)
    down()
    left(90)
    forward(75)

    up()
    forward(75)
    right(90)
    forward(330)

    #F
    down()
    right(180)
    forward(50)
    right(180)
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(40)
    left(180)
    forward(40)
    left(90)
    forward(45)

    up()
    left(90)
    forward(75)

    #O
    down()
    forward(50)
    left(90)
    forward(75)
    left(90)
    forward(50)
    left(90)
    forward(75)

    up()
    left(90)
    forward(75)

    #R
    down()
    left(90)
    forward(75)
    right(90)
    forward(50)
    right(90)
    forward(35)
    right(90)
    forward(50)
    left(140)
    forward(66)

    up()
    left(40)
    right(180)
    forward(325)
    left(90)
    forward(50)

    #P
    down()
    left(90)
    forward(50)
    right(90)
    forward(37.5)
    right(90)
    forward(50)
    right(90)
    forward(37.5)
    left(180)
    forward(75)

    up()
    left(90)
    forward(75)

    #L
    down()
    left(90)
    forward(75)
    right(180)
    forward(75)
    left(90)
    forward(50)

    up()
    forward(25)

    #A
    down()
    left(90)
    forward(75)
    right(90)
    forward(40)
    right(90)
    forward(37.5)
    right(90)
    forward(40)
    right(180)
    forward(40)
    right(90)
    forward(37.5)

    up()
    left(90)
    forward(50)
    left(90)
    forward(40)
    right(90)

    #Y
    down()
    left(45)
    forward(51)
    right(180)
    forward(51)
    right(90)
    forward(51)
    right(180)
    forward(51)
    right(45)
    forward(37.5)

    up()
    left(90)
    forward(60)

    #I
    down()
    left(90)
    forward(75)

    up()
    right(90)
    forward(25)
    right(90)
    forward(75)
    right(270)

    #N
    down()
    left(90)
    forward(75)
    right(155)
    forward(80)
    left(155)
    forward(75)

    up()
    right(90)
    forward(75)
    right(180)

    #G
    down()
    forward(50)
    left(90)
    forward(75)
    left(90)
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(30)

    up()
    left(90)
    forward(230)
    right(90)
    forward(190)
    right(180)

    def curve(): 
        for i in range(200): 
            right(1) 
            forward(1)

    fillcolor('red')
    begin_fill()
    left(140)
    forward(113)
    curve()
    left(120)
    curve()
    forward(112) 
    end_fill() 



    mainloop()