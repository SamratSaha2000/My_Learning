import numpy as np
import turtle as tu
foo=tu.Turtle()
too=tu.Turtle()
too.pencolor('green')
foo.pencolor('brown')

too.forward(100)
too.left(90)
foo.left(90)

foo.speed(10000)
too.speed(10000)
#recursion
def fractal2(l):
    if(l<0.01):
        return
    else:
        too.forward(l)
        too.left(30)
        fractal2(l/2)
        too.right(60)
        fractal2(l/2)
        too.left(30)
        too.backward(l)

        
def fractal1(l):
    if(l<0.1):
        return
    else:
        foo.forward(l)
        foo.left(30)
        fractal1(l/2)
        foo.right(60)
        fractal1(l/2)
        foo.left(30)
        foo.backward(l)
fractal2(100)
fractal1(100)


