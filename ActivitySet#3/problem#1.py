import math
x1 = float(input('enter the coordinate: '))
y1 = float(input('enter the coordinate: '))
x2 = float(input('enter the coordinate: '))
y2 = float(input('enter the coordinate: '))
x3 = float(input('enter the coordinate: '))
y3 = float(input('enter the coordinate: '))
len1 = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
len2 = math.sqrt((x3-x2)*(x3-x2) + (y3-y2)*(y3-y2))
area = len1*len2
print(area)