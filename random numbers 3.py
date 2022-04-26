from cmath import sqrt
import random
import math

#1
x1 = random.randint(-10,10)
y1 = random.randint(-10,10)
print(x1,y1)
x2 = random.randint(-10,10)
y2 = random.randint(-10,10)
print(x2,y2)
midpointx = (x1+x2)/2
midpointy = (y1+y2)/2
print(midpointx,midpointy)

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)