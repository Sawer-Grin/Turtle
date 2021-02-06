from random import randint
import turtle
import math

# task characteristics
number_of_turtles = 40
steps_of_time_number = 500
turtle.speed(50000)

# pool_log - array to prevent entry into other program branches
pool_log = [True for i in range(number_of_turtles)]


# pool - array of objects
pool = [turtle.Turtle(shape='circle') for k in range(number_of_turtles)]

# throwing objects on the field
for unit in pool:
    unit.penup()
    unit.speed(5000000)
    unit.goto(randint(-380, 380), randint(-380, 380))
    unit.left(randint(0, 361))

# drawing area
turtle.penup()
turtle.goto(-400, -400)
turtle.pendown()
turtle.forward(800)
turtle.left(90)
turtle.forward(800)
turtle.left(90)
turtle.forward(800)
turtle.left(90)
turtle.forward(800)
turtle.penup()
turtle.home()
turtle.pendown()

# traffic
for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)

    # collision cycle
    for unit in pool:
        for second_unit in pool:
            if second_unit != unit:
                x, y = second_unit.pos()
                if unit.distance(x, y) <= 20:
                    gama = unit.heading()
                    alpha = second_unit.heading()
                    # teta - angle of a straight line that passes between two paths
                    teta = (gama + alpha) / 2
                    if math.fabs(gama - alpha) == 180:
                        unit.left(180)
                        second_unit.left(180)
                    else:

                        # delta - the angle between any path and the middle line
                        flag = True
                        if gama > alpha:
                            delta = gama - teta
                            unit.right(delta * 2)
                            second_unit.left(delta * 2)
                            delta = math.radians(delta)
                            unit.forward(11 / math.sin(delta))
                            second_unit.forward(11 / math.sin(delta))
                            flag = False
                        elif (alpha > gama) and flag:
                            delta = alpha - teta
                            second_unit.right(delta * 2)
                            unit.left(delta * 2)
                            delta = math.radians(delta)
                            second_unit.forward(11 / math.sin(delta))
                            unit.forward(11 / math.sin(delta))
    p = 0

    # cycle responsible for pushing off boundaries
    for unit in pool:
        x, y = unit.pos()
        csi = unit.heading()
        if (y >= 395) and pool_log[p]:
            if (180 > csi > 90) and pool_log[p]:
                unit.left(180 - (csi - 90) * 2)
                beta = math.radians(csi - 90)
                unit.forward(6 / math.cos(beta))
                pool_log[p] = False
            elif (0 < csi < 90) and pool_log[p]:
                unit.right(180 - (90 - csi) * 2)
                beta = math.radians(90 - csi)
                unit.forward(6 / math.cos(beta))
                pool_log[p] = False
            elif (csi == 90) and pool_log[p]:
                unit.left(180)
                unit.forward(10)
                pool_log[p] = False
        elif (x <= -395) and pool_log[p]:
            if (270 > csi > 180) and pool_log[p]:
                unit.left(180 - (csi - 180) * 2)
                beta = math.radians(csi - 180)
                unit.forward(6 / math.cos(beta))
                pool_log[p] = False
            elif (90 < csi < 180) and pool_log[p]:
                unit.right(180 - (180 - csi) * 2)
                beta = math.radians(180 - csi)
                unit.forward(6 / math.cos(beta))
                pool_log[p] = False
            elif (csi == 180) and pool_log[p]:
                unit.left(180)
                unit. forward(10)
                pool_log[p] = False
        elif (y <= -395) and pool_log[p]:
            if (360 > csi > 270) and pool_log[p]:
                unit.left(180 - (csi - 270) * 2)
                beta = math.radians(csi - 270)
                unit.forward(6 / math.cos(beta))
                pool_log[p] = False
            elif (180 < csi < 270) and pool_log[p]:
                unit.right(180 - (270 - csi) * 2)
                beta = math.radians(270 - csi)
                unit.forward(6 / math.cos(beta))
                pool_log[p] = False
            elif (csi == 270) and pool_log[p]:
                unit.left(180)
                unit.forward(10)
                pool_log[p] = False
        elif (x >= 395) and pool_log[p]:
            if (360 > csi > 270) and pool_log[p]:
                unit.right(180 - (360 - csi) * 2)
                csi = math.radians(csi)
                unit.forward(6 / math.cos(csi))
                pool_log[p] = False
            elif (90 > csi > 0) and pool_log[p]:
                unit.left(180 - csi * 2)
                beta = math.radians(360 - csi)
                unit.forward(6 / math.cos(beta))
                pool_log[p] = False
            elif (csi == 0) and pool_log[p]:
                unit.left(180)
                unit.forward(10)
                pool_log[p] = False
        else:
            pool_log[p] = True
        p += 1