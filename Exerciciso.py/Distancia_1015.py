import math

p1 = (input().split(" ")) # x1, y1 = [x1, x2]
p2 = (input().split(" "))

x1, y1 = p1
x2, y2 = p2

B = ((float(x2) - float(x1))**2) + ((float(y2) - float(y1))**2)

D = math.sqrt(B)


print("%0.4f" %D)