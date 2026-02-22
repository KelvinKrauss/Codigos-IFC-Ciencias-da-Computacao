import math

l1 = float(input ())
l2 = float(input ())
l3 = float(input ())
l = (l1 + l2 + l3)  / 2
area = math.sqrt(l * (l - l1) * (l - l2) * (l - l3))
print(area)