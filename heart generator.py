import math
from turtle import *


def diaa(k):

    return 15 * math.sin(k) ** 3


def diab(k):

    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


speed(0)
bgcolor("black")
for i in range(10000):
    goto(diaa(i) * 20, diab(i) * 20)
for j in range(5):
    color("#000000")
goto(0, 0)
done()
