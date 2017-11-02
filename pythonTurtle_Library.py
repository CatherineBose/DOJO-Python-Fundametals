# # # try this either as a .py file or in the python shell
# # import turtle
# # # the distance we want the pointer to travel each time
# # DIST = 200
# # for x in range(0,6):
# #     print "x", x
# #     for y in range(1,5):
# #         print "y", y
# #         # turn the pointer 90 degrees to the right
# #         turtle.right(45)
# #         # advance according to set distance
# #         turtle.forward(DIST)
# #     # add to set distance
# #     DIST += 20

# #To draw circle 
# # import turtle
 
# # myTurtle = turtle.Turtle()
# # myTurtle.circle(50)
# # turtle.getscreen()._root.mainloop()

# import turtle
 
# myTurtle = turtle.Turtle(shape="turtle")
# myTurtle.circle(50)
 
# myTurtle.penup()
# myTurtle.setposition(-120, 0)
# myTurtle.pendown()
# myTurtle.circle(50)
 
# myTurtle.penup()
# myTurtle.setposition(60,60)
# myTurtle.pendown()
# myTurtle.circle(50)
 
# myTurtle.penup()
# myTurtle.setposition(-60, 60)
# myTurtle.pendown()
# myTurtle.circle(50)
 
# myTurtle.penup()
# myTurtle.setposition(-180, 60)
# myTurtle.pendown()
# myTurtle.circle(50)
 
# turtle.getscreen()._root.mainloop()
from random import shuffle
arr = [1, 2, 3, 4, 5]
shuffle(arr)
print arr