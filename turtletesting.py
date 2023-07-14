import turtle

pegasus = turtle.Turtle()

pegasus.getscreen().bgcolor("orange")

pegasus.speed(0)

def Star(pegasus, size):
    for i in range(5):
        pegasus.forward(size)
        pegasus.left(216)

    size -= 10
    
    if size >= 10:
        pegasus.left(90)
        Star (pegasus, size)

Star(pegasus, 500)

turtle.done()