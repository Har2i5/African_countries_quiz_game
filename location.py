###  The code below aids to get the position of x and y by clicking on any area of the map  ###
import turtle

screen = turtle.Turtle()

screen = turtle.Screen()
screen.title("Guess The Name Of The African Country")
image = "african_map.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)  #This prints out the x and y positions

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
screen.exitonclick()